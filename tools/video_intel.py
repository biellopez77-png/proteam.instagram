#!/usr/bin/env python3
"""ProTeam · sistema central de análisis de vídeo (compartido por los seis agentes).

Mide lo que se puede medir (metadatos, cortes, fotogramas, texto en pantalla, audio) y deja
las láminas de fotogramas con su marca de tiempo para que el agente las MIRE con Read.
No opina: los juicios los escribe el agente en observaciones.md, siempre con marca de tiempo.

Uso:
  python3 tools/video_intel.py analyze VIDEO --id ID [--marca proteam] [--tipo propio|competencia|referencia]
                               [--formato reel] [--tema "..."] [--fuente URL_o_nota] [--modo general|detalle|completo]
  python3 tools/video_intel.py window  ID --desde 8 --hasta 14      # modo 4: todos los fotogramas del tramo
  python3 tools/video_intel.py voz     ID tools/reelNN/voz.tsv       # locución exacta con tiempos (Reels propios)
  python3 tools/video_intel.py visto   ID LAMINA [LAMINA...]         # apunta las láminas que el agente ha mirado
  python3 tools/video_intel.py rasgos  ID                            # características medidas → intel/aprendizaje/CARACTERISTICAS.csv
  python3 tools/video_intel.py estado  ID                            # cobertura real: qué se ha mirado y qué no
  python3 tools/video_intel.py buscar  [texto]                       # busca en intel/INDEX.csv
Carpeta de salida: intel/videos/<ID>/ (láminas y datos, en git) · intel/.frames/<ID>/ (fotogramas sueltos, regenerables, fuera de git)
"""
import argparse, csv, datetime, hashlib, json, math, os, re, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTEL = os.path.join(ROOT, "intel")
INDEX = os.path.join(INTEL, "INDEX.csv")
COLS = ["id", "marca", "tipo", "formato", "tema", "fecha_analisis", "fuente", "archivo", "sha256", "duracion_s",
        "resolucion", "fps", "cortes", "modo", "cobertura", "ruta"]
FONT = os.path.join(ROOT, "tools", "fonts")

def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def font(size):
    for f in ("Manrope-Bold.ttf", "Manrope-ExtraBold.ttf"):
        p = os.path.join(FONT, f)
        if os.path.exists(p): return ImageFont.truetype(p, size)
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",):
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def tc(t):
    return f"{int(t // 60):02d}:{t % 60:05.2f}"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def read_index():
    if not os.path.exists(INDEX): return []
    with open(INDEX, newline="", encoding="utf-8") as f: return list(csv.DictReader(f))

def write_index(rows):
    os.makedirs(INTEL, exist_ok=True)
    with open(INDEX, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader()
        for r in sorted(rows, key=lambda r: r["id"]): w.writerow({c: r.get(c, "") for c in COLS})

# ───────── 1. metadatos
def probe(video):
    r = sh(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", video])
    if r.returncode: sys.exit("ffprobe no pudo leer el archivo: " + r.stderr[:300])
    j = json.loads(r.stdout); v = next((s for s in j["streams"] if s["codec_type"] == "video"), None)
    if not v: sys.exit("El archivo no tiene pista de vídeo.")
    auds = [s for s in j["streams"] if s["codec_type"] == "audio"]
    n, d = v.get("avg_frame_rate", "0/1").split("/"); fps = float(n) / float(d) if float(d) else 0
    w, h = v["width"], v["height"]
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd: rot = int(sd["rotation"])
    if abs(rot) in (90, 270): w, h = h, w
    g = math.gcd(w, h)
    dur = float(j["format"].get("duration") or v.get("duration") or 0)
    return {"contenedor": j["format"].get("format_name"), "duracion_s": round(dur, 3), "tamano_bytes": int(j["format"].get("size", 0)),
            "bitrate_kbps": round(int(j["format"].get("bit_rate", 0)) / 1000), "ancho": w, "alto": h, "relacion": f"{w // g}:{h // g}",
            "fps": round(fps, 3), "fotogramas_declarados": int(v.get("nb_frames") or round(dur * fps)), "codec_video": v.get("codec_name"),
            "pix_fmt": v.get("pix_fmt"), "pistas_audio": [{"codec": a.get("codec_name"), "canales": a.get("channels"), "hz": int(a.get("sample_rate", 0)),
            "bitrate_kbps": round(int(a.get("bit_rate", 0) or 0) / 1000)} for a in auds],
            "etiquetas": j["format"].get("tags", {})}

# ───────── 2. recorrido completo: cortes, movimiento, luz (lee TODOS los fotogramas)
def scan(video, meta):
    cap = cv2.VideoCapture(video); fps = meta["fps"] or cap.get(cv2.CAP_PROP_FPS) or 30
    prev_h = prev_g = None; rows = []; i = 0
    while True:
        ok, fr = cap.read()
        if not ok: break
        sm = cv2.resize(fr, (96, 170) if fr.shape[0] > fr.shape[1] else (170, 96))
        hsv = cv2.cvtColor(sm, cv2.COLOR_BGR2HSV); g = cv2.cvtColor(sm, cv2.COLOR_BGR2GRAY)
        h = cv2.calcHist([hsv], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256]); cv2.normalize(h, h, 1, 0, cv2.NORM_L1)
        dh = float(cv2.compareHist(prev_h, h, cv2.HISTCMP_BHATTACHARYYA)) if prev_h is not None else 0.0
        dm = float(np.mean(cv2.absdiff(prev_g, g))) / 255 if prev_g is not None else 0.0
        rows.append((i, i / fps, dh, dm, float(g.mean()) / 255, float(hsv[..., 1].mean()) / 255))
        prev_h, prev_g = h, g; i += 1
    cap.release()
    return rows, fps

def find_cuts(rows, fps):
    """Corte duro: salto de histograma claro y aislado. Fundido/transición: cambio sostenido."""
    cuts = []; dh = np.array([r[2] for r in rows]); dm = np.array([r[3] for r in rows])
    n = len(rows); mind = max(2, int(fps * 0.2)); last = -mind
    for i in range(1, n):
        lo, hi = max(1, i - int(fps * 0.4)), min(n, i + int(fps * 0.4))
        vec = np.delete(dh[lo:hi], i - lo) if hi - lo > 1 else dh[lo:hi]
        base = float(np.median(vec)) if len(vec) else 0
        if dh[i] > 0.30 and dh[i] > base * 3 + 0.12 and dm[i] > 0.04 and i - last >= mind:
            cuts.append({"fotograma": i, "t": round(rows[i][1], 3), "tipo": "corte", "fuerza": round(float(dh[i]), 3)}); last = i
    # transiciones: ventana de 0,2–1 s con cambio acumulado alto y sin corte duro dentro
    win = int(fps * 0.5); hard = {c["fotograma"] for c in cuts}; i = win
    while i < n - 1:
        acc = float(dm[i - win:i].mean())
        if acc > 0.10 and not any(abs(i - h) <= win for h in hard) and (not cuts or i - last > win * 2):
            cuts.append({"fotograma": i - win, "t": round(rows[i - win][1], 3), "tipo": "transicion_o_movimiento_fuerte", "fuerza": round(acc, 3)}); last = i; i += win * 2
        else: i += 1
    return sorted(cuts, key=lambda c: c["fotograma"])

def scenes_from(cuts, rows, fps):
    hard = [c for c in cuts if c["tipo"] == "corte"]; edges = [0] + [c["fotograma"] for c in hard] + [len(rows)]
    out = []
    for k in range(len(edges) - 1):
        a, b = edges[k], edges[k + 1]
        if b <= a: continue
        seg = rows[a:b]
        out.append({"escena": k + 1, "desde_fotograma": a, "hasta_fotograma": b - 1, "desde": round(a / fps, 3), "hasta": round(b / fps, 3),
                    "duracion_s": round((b - a) / fps, 3), "movimiento_medio": round(float(np.mean([r[3] for r in seg])), 4),
                    "luz_media": round(float(np.mean([r[4] for r in seg])), 3), "saturacion_media": round(float(np.mean([r[5] for r in seg])), 3)})
    return out

# ───────── 3. fotogramas y láminas
def grab(video, idxs, outdir, width=540):
    os.makedirs(outdir, exist_ok=True); cap = cv2.VideoCapture(video); fps = cap.get(cv2.CAP_PROP_FPS) or 30
    want = set(idxs); got = {}; i = 0; mx = max(want) if want else -1
    while i <= mx:
        ok, fr = cap.read()
        if not ok: break
        if i in want:
            h = int(fr.shape[0] * width / fr.shape[1]); p = os.path.join(outdir, f"f{i:06d}_t{i / fps:08.3f}.jpg")
            cv2.imwrite(p, cv2.resize(fr, (width, h), interpolation=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 88]); got[i] = p
        i += 1
    cap.release(); return got

def sheet(paths, fps, scene_of, out, cols, tile_w, title):
    ims = [(i, Image.open(p)) for i, p in paths]; tw = tile_w; th = int(ims[0][1].height * tw / ims[0][1].width); lab = 34; pad = 8
    rows_n = math.ceil(len(ims) / cols); W = cols * tw + (cols + 1) * pad; Hh = 44 + rows_n * (th + lab + pad) + pad
    canvas = Image.new("RGB", (W, Hh), "#0d0f14"); d = ImageDraw.Draw(canvas); d.text((pad, 10), title, fill="#f2f1ec", font=font(20))
    f1 = font(17)
    for k, (i, im) in enumerate(ims):
        x = pad + (k % cols) * (tw + pad); y = 44 + (k // cols) * (th + lab + pad)
        canvas.paste(im.resize((tw, th)), (x, y + lab))
        d.text((x + 2, y + 6), f"{tc(i / fps)}  ·  f{i}  ·  E{scene_of(i)}", fill="#8fb0ff", font=f1)
    canvas.save(out, quality=84); return out

def make_sheets(video, idxs, fps, scenes, vdir, fdir, prefix, cols, tile_w, per, label):
    got = grab(video, idxs, fdir, width=max(tile_w, 360))
    def scene_of(i):
        for s in scenes:
            if s["desde_fotograma"] <= i <= s["hasta_fotograma"]: return s["escena"]
        return 0
    os.makedirs(os.path.join(vdir, "laminas"), exist_ok=True); out = []; ids = sorted(got)
    for n in range(0, len(ids), per):
        chunk = ids[n:n + per]; name = f"{prefix}{n // per + 1:03d}.jpg"
        sheet([(i, got[i]) for i in chunk], fps, scene_of, os.path.join(vdir, "laminas", name), cols, tile_w,
              f"{label} · lámina {n // per + 1} · {tc(chunk[0] / fps)}–{tc(chunk[-1] / fps)} · fotogramas {chunk[0]}–{chunk[-1]}")
        out.append({"lamina": name, "fotogramas": chunk, "desde": round(chunk[0] / fps, 3), "hasta": round(chunk[-1] / fps, 3)})
    return out, got

# ───────── 4. texto en pantalla (OCR)
def ocr(got, fps):
    try:
        import pytesseract
    except Exception:
        return None
    lang = "spa+eng" if "spa" in sh(["tesseract", "--list-langs"]).stdout else "eng"
    res = []
    for i in sorted(got):
        im = cv2.imread(got[i]); g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); g = cv2.resize(g, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        best = ""
        for img in (g, 255 - g):
            try: d = pytesseract.image_to_data(img, lang=lang, config="--psm 11", output_type=pytesseract.Output.DICT)
            except Exception: continue
            words = [w for w, c in zip(d["text"], d["conf"]) if w.strip() and float(c) >= 60 and re.search(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9]{2,}", w)]
            t = " ".join(words)
            if len(t) > len(best): best = t
        res.append({"fotograma": i, "t": round(i / fps, 3), "texto": best})
    # agrupar texto parecido consecutivo → tiempo de exposición aproximado
    runs = []
    def key(s): return re.sub(r"[^a-z0-9áéíóúñ]", "", s.lower())[:40]
    for r in res:
        if not r["texto"]: continue
        if runs and (key(r["texto"]) == runs[-1]["_k"] or (len(key(r["texto"])) > 5 and key(r["texto"])[:12] == runs[-1]["_k"][:12])):
            runs[-1]["hasta"] = r["t"]; runs[-1]["texto"] = max(runs[-1]["texto"], r["texto"], key=len)
        else: runs.append({"desde": r["t"], "hasta": r["t"], "texto": r["texto"], "_k": key(r["texto"])})
    for r in runs: r.pop("_k"); r["palabras"] = len(r["texto"].split())
    runs = [r for r in runs if r["hasta"] > r["desde"] or r["palabras"] >= 5]  # fuera lecturas sueltas de un solo fotograma (ruido de animación)
    return {"idioma": lang, "nota": "OCR automático sobre los fotogramas muestreados: puede fallar con tipografía fina, texto animado o sobre foto. La exposición es aproximada (resolución = intervalo de muestreo). Verificar siempre en las láminas.",
            "por_fotograma": res, "bloques": runs}

# ───────── 5. audio (medido; la transcripción necesita herramienta externa)
def audio(video, meta, vdir):
    if not meta["pistas_audio"]: return {"tiene_audio": False}
    wav = os.path.join(vdir, "audio_16k.wav"); sh(["ffmpeg", "-y", "-v", "error", "-i", video, "-vn", "-ac", "1", "-ar", "16000", wav])
    if not os.path.exists(wav): return {"tiene_audio": True, "error": "no se pudo extraer"}
    raw = np.frombuffer(open(wav, "rb").read()[44:], dtype=np.int16).astype(np.float32) / 32768; sr = 16000; hop = sr // 10
    rms = [float(np.sqrt(np.mean(raw[i:i + hop] ** 2)) + 1e-9) for i in range(0, len(raw) - hop, hop)]
    db = [round(20 * math.log10(x), 1) for x in rms]
    r = sh(["ffmpeg", "-v", "info", "-i", video, "-af", "silencedetect=noise=-38dB:d=0.25,loudnorm=print_format=json", "-f", "null", "-"]).stderr
    sil = [{"desde": round(float(a), 2), "hasta": round(float(b), 2)} for a, b in zip(re.findall(r"silence_start: ([\d.]+)", r), re.findall(r"silence_end: ([\d.]+)", r))]
    ln = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r, re.S); loud = json.loads(ln.group(0)) if ln else {}
    # golpes: subidas bruscas de energía (posibles SFX, golpes de música o inicios de frase)
    hits = [round(i / 10, 1) for i in range(2, len(db)) if db[i] - min(db[i - 2:i]) > 12 and db[i] > -28]
    merged = []
    for h in hits:
        if not merged or h - merged[-1] > 0.35: merged.append(h)
    return {"tiene_audio": True, "wav": os.path.relpath(wav, ROOT), "volumen_integrado_lufs": loud.get("input_i"), "pico_real_db": loud.get("input_tp"),
            "rango_lra": loud.get("input_lra"), "silencios": sil, "subidas_bruscas_s": merged, "energia_db_cada_0_1s": db,
            "transcripcion": "PENDIENTE: no hay transcriptor local. Usa la herramienta de transcripción de ElevenLabs con audio_16k.wav, o el guion/voz.tsv si es un Reel propio, y guarda el resultado en transcripcion.json.",
            "nota": "Esto son medidas. Entonación, claridad de la locución, timbre o si hay música NO se pueden afirmar sin escuchar o transcribir."}

# ───────── órdenes
def cmd_analyze(a):
    video = os.path.abspath(a.video)
    if not os.path.exists(video): sys.exit("No existe " + video)
    digest = sha256(video); rows = read_index()
    dup = next((r for r in rows if r["sha256"] == digest and r["id"] != a.id), None)
    if dup: sys.exit(f"Este mismo archivo ya está analizado como «{dup['id']}» ({dup['ruta']}). Reutiliza ese análisis; no lo repitas.")
    vdir = os.path.join(INTEL, "videos", a.id); fdir = os.path.join(INTEL, ".frames", a.id); os.makedirs(vdir, exist_ok=True)
    meta = probe(video); rws, fps = scan(video, meta); n = len(rws)
    meta.update({"id": a.id, "fotogramas_leidos": n, "sha256": digest, "archivo": os.path.relpath(video, ROOT) if video.startswith(ROOT) else video,
                 "fuente": a.fuente, "marca": a.marca, "tipo": a.tipo, "formato": a.formato, "tema": a.tema,
                 "analizado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})
    cuts = find_cuts(rws, fps); scenes = scenes_from(cuts, rws, fps); hard = [c for c in cuts if c["tipo"] == "corte"]
    durs = [s["duracion_s"] for s in scenes]
    montaje = {"cortes_duros": len(hard), "transiciones_o_movimientos_fuertes": len(cuts) - len(hard), "planos": len(scenes),
               "duracion_media_plano_s": round(float(np.mean(durs)), 2), "plano_mas_largo_s": max(durs), "plano_mas_corto_s": min(durs),
               "cortes_por_10s": round(len(hard) / max(meta["duracion_s"], 0.1) * 10, 2),
               "tramos_estaticos": static_spans(rws, fps),
               "nota": "Detección automática por histograma y diferencia de imagen sobre TODOS los fotogramas. Un motion graphic continuo cuenta como un solo plano; un cambio de fondo brusco dentro de una animación puede contarse como corte. Confirmar en las láminas."}
    with open(os.path.join(vdir, "fotogramas.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["fotograma", "t", "timecode", "escena", "cambio_histograma", "movimiento", "luz", "saturacion"])
        for r in rws:
            sc = next((s["escena"] for s in scenes if s["desde_fotograma"] <= r[0] <= s["hasta_fotograma"]), 0)
            w.writerow([r[0], f"{r[1]:.3f}", tc(r[1]), sc, f"{r[2]:.4f}", f"{r[3]:.4f}", f"{r[4]:.3f}", f"{r[5]:.3f}"])
    laminas = []
    # Modo 1 · general: inicio, mitad y final de cada plano + el segundo 0 con detalle
    idx = set(range(0, min(n, int(fps)), max(1, int(fps / 6))))
    for s in scenes:
        a0, b0 = s["desde_fotograma"], s["hasta_fotograma"]; idx.update({a0, (a0 + b0) // 2, b0})
        if s["duracion_s"] > 3: idx.update(range(a0, b0, int(fps * 1.5)))
    l1, got1 = make_sheets(video, sorted(idx), fps, scenes, vdir, fdir, "general_", 6, 300, 18, f"{a.id} · GENERAL")
    laminas += [dict(x, modo="general") for x in l1]; got = dict(got1)
    if a.modo in ("detalle", "completo"):
        step = max(1, round(fps / a.fps)); idx2 = sorted(set(range(0, n, step)) | {c["fotograma"] for c in cuts} | {max(0, c["fotograma"] - 1) for c in cuts})
        l2, got2 = make_sheets(video, idx2, fps, scenes, vdir, fdir, "detalle_", 6, 300, 24, f"{a.id} · DETALLE {a.fps:g} fps")
        laminas += [dict(x, modo="detalle") for x in l2]; got.update(got2)
    if a.modo == "completo":
        l3, _ = make_sheets(video, list(range(n)), fps, scenes, vdir, fdir, "completo_", 10, 200, 60, f"{a.id} · TODOS LOS FOTOGRAMAS")
        laminas += [dict(x, modo="completo") for x in l3]
    texto = ocr({i: got[i] for i in sorted(got)}, fps); aud = audio(video, meta, vdir)
    data = {"meta": meta, "montaje": montaje, "cortes": cuts, "escenas": scenes, "laminas": laminas, "texto_en_pantalla": texto, "audio": aud,
            "vistas": [], "orden": " ".join(["python3 tools/video_intel.py"] + sys.argv[1:])}
    save(vdir, data); report(vdir, data)
    row = {"id": a.id, "marca": a.marca, "tipo": a.tipo, "formato": a.formato, "tema": a.tema, "fecha_analisis": meta["analizado"][:10], "fuente": a.fuente,
           "archivo": meta["archivo"], "sha256": digest, "duracion_s": meta["duracion_s"], "resolucion": f"{meta['ancho']}x{meta['alto']}", "fps": meta["fps"],
           "cortes": len(hard), "modo": a.modo, "cobertura": "0 láminas vistas", "ruta": os.path.relpath(vdir, ROOT)}
    write_index([r for r in rows if r["id"] != a.id] + [row])
    print(json.dumps({"id": a.id, "carpeta": os.path.relpath(vdir, ROOT), "duracion_s": meta["duracion_s"], "fotogramas": n, "planos": len(scenes),
                      "laminas": [x["lamina"] for x in laminas], "siguiente": "Mira TODAS las láminas con Read, apúntalas con «visto» y escribe observaciones.md con marcas de tiempo."}, ensure_ascii=False, indent=1))

def static_spans(rws, fps):
    out = []; start = None
    for r in rws:
        if r[3] < 0.004:
            if start is None: start = r[0]
        else:
            if start is not None and (r[0] - start) / fps >= 1.5: out.append({"desde": round(start / fps, 2), "hasta": round(r[0] / fps, 2), "duracion_s": round((r[0] - start) / fps, 2)})
            start = None
    if start is not None and (rws[-1][0] - start) / fps >= 1.5: out.append({"desde": round(start / fps, 2), "hasta": round(rws[-1][1], 2), "duracion_s": round((rws[-1][0] - start) / fps, 2)})
    return out

def save(vdir, data):
    slim = json.loads(json.dumps(data))
    with open(os.path.join(vdir, "analisis.json"), "w", encoding="utf-8") as f: json.dump(slim, f, ensure_ascii=False, indent=1)

def load(id_):
    p = os.path.join(INTEL, "videos", id_, "analisis.json")
    if not os.path.exists(p): sys.exit(f"No hay análisis de «{id_}». Lanza analyze primero.")
    return os.path.dirname(p), json.load(open(p, encoding="utf-8"))

def coverage(data):
    seen = set(data.get("vistas", [])); cov = {}
    for m in ("general", "detalle", "completo", "tramo"):
        ls = [x for x in data["laminas"] if x["modo"] == m]
        if ls: cov[m] = {"laminas": len(ls), "vistas": sum(1 for x in ls if x["lamina"] in seen), "sin_ver": [x["lamina"] for x in ls if x["lamina"] not in seen]}
    n = data["meta"]["fotogramas_leidos"]; fr = set()
    for x in data["laminas"]:
        if x["lamina"] in seen: fr.update(x["fotogramas"])
    cov["fotogramas_mirados"] = len(fr); cov["fotogramas_totales"] = n; cov["porcentaje_mirado"] = round(100 * len(fr) / max(n, 1), 1)
    return cov

def report(vdir, data):
    m, mo, au = data["meta"], data["montaje"], data["audio"]; L = []
    L += [f"# {m['id']} · informe técnico (medido, no opinado)", "",
          f"- **Archivo:** `{m['archivo']}` · sha256 `{m['sha256'][:16]}…` · fuente: {m['fuente'] or '—'}",
          f"- **Marca / tipo / formato / tema:** {m['marca']} / {m['tipo']} / {m['formato']} / {m['tema'] or '—'}",
          f"- **Técnica:** {m['duracion_s']} s · {m['ancho']}×{m['alto']} ({m['relacion']}) · {m['fps']} fps · {m['fotogramas_leidos']} fotogramas leídos · {m['codec_video']} · {m['bitrate_kbps']} kbps",
          f"- **Audio:** " + (", ".join(f"{a['codec']} {a['canales']} canales {a['hz']} Hz" for a in m["pistas_audio"]) or "sin pista de audio"),
          f"- **Analizado:** {m['analizado']} · orden: `{data['orden']}`", "",
          "## Montaje (automático; confirmar en láminas)",
          f"{mo['planos']} planos · {mo['cortes_duros']} cortes duros · {mo['transiciones_o_movimientos_fuertes']} transiciones o movimientos fuertes · plano medio {mo['duracion_media_plano_s']} s (más largo {mo['plano_mas_largo_s']} s, más corto {mo['plano_mas_corto_s']} s) · {mo['cortes_por_10s']} cortes cada 10 s", ""]
    if mo["tramos_estaticos"]: L += ["Tramos sin movimiento (≥ 1,5 s): " + "; ".join(f"{tc(s['desde'])}–{tc(s['hasta'])} ({s['duracion_s']} s)" for s in mo["tramos_estaticos"]), ""]
    L += ["| plano | desde | hasta | dura | movimiento | luz |", "|---|---|---|---|---|---|"]
    L += [f"| E{s['escena']} | {tc(s['desde'])} | {tc(s['hasta'])} | {s['duracion_s']} s | {s['movimiento_medio']} | {s['luz_media']} |" for s in data["escenas"]]
    tx = data.get("texto_en_pantalla")
    L += ["", "## Texto en pantalla (OCR; verificar)"]
    if tx and tx["bloques"]: L += ["| desde | hasta | palabras | texto leído |", "|---|---|---|---|"] + [f"| {tc(b['desde'])} | {tc(b['hasta'])} | {b['palabras']} | {b['texto'][:110]} |" for b in tx["bloques"]]
    else: L += ["El OCR no ha leído texto (o no hay OCR). No significa que no haya: míralo en las láminas."]
    L += ["", "## Audio (medido)"]
    if au.get("tiene_audio"):
        L += [f"Volumen integrado {au.get('volumen_integrado_lufs')} LUFS · pico real {au.get('pico_real_db')} dB · rango {au.get('rango_lra')} LU",
              "Silencios (< −38 dB, ≥ 0,25 s): " + ("; ".join(f"{tc(s['desde'])}–{tc(s['hasta'])}" for s in au["silencios"]) or "ninguno"),
              "Subidas bruscas de energía (posibles golpes o efectos): " + (", ".join(tc(x) for x in au["subidas_bruscas_s"]) or "ninguna"),
              "Transcripción: " + ("ver `transcripcion.json`" if os.path.exists(os.path.join(vdir, "transcripcion.json")) else "pendiente (ver nota en analisis.json)")]
    else: L += ["El archivo no tiene audio."]
    cov = coverage(data)
    L += ["", "## Láminas y cobertura visual", f"Fotogramas mirados por un agente: **{cov['fotogramas_mirados']} de {cov['fotogramas_totales']} ({cov['porcentaje_mirado']} %)**.", ""]
    L += ["| lámina | modo | tramo | fotogramas | vista |", "|---|---|---|---|---|"]
    L += [f"| `laminas/{x['lamina']}` | {x['modo']} | {tc(x['desde'])}–{tc(x['hasta'])} | {len(x['fotogramas'])} | {'sí' if x['lamina'] in data.get('vistas', []) else 'NO'} |" for x in data["laminas"]]
    L += ["", "Los juicios (qué funciona, qué falla y por qué) van en `observaciones.md`, cada uno con su marca de tiempo y la lámina donde se ve.", ""]
    open(os.path.join(vdir, "informe.md"), "w", encoding="utf-8").write("\n".join(L))

def cmd_window(a):
    vdir, data = load(a.id); m = data["meta"]; video = m["archivo"] if os.path.isabs(m["archivo"]) else os.path.join(ROOT, m["archivo"])
    if not os.path.exists(video): sys.exit("No encuentro el original: " + video)
    fps = m["fps"]; i0, i1 = max(0, int(a.desde * fps)), min(m["fotogramas_leidos"] - 1, int(math.ceil(a.hasta * fps)))
    tag = f"tramo_{a.desde:g}-{a.hasta:g}_".replace(".", "p")
    ls, _ = make_sheets(video, list(range(i0, i1 + 1)), fps, data["escenas"], vdir, os.path.join(INTEL, ".frames", a.id), tag, 8, 250, 40, f"{a.id} · TRAMO {a.desde:g}–{a.hasta:g} s · todos los fotogramas")
    data["laminas"] = [x for x in data["laminas"] if not x["lamina"].startswith(tag)] + [dict(x, modo="tramo") for x in ls]
    save(vdir, data); report(vdir, data); print(json.dumps({"laminas": [x["lamina"] for x in ls], "fotogramas": i1 - i0 + 1}, ensure_ascii=False))

def cmd_visto(a):
    vdir, data = load(a.id); names = {x["lamina"] for x in data["laminas"]}; bad = [x for x in a.laminas if os.path.basename(x) not in names]
    if bad: sys.exit("Láminas que no existen: " + ", ".join(bad))
    data["vistas"] = sorted(set(data.get("vistas", [])) | {os.path.basename(x) for x in a.laminas}); save(vdir, data); report(vdir, data)
    cov = coverage(data); rows = read_index()
    for r in rows:
        if r["id"] == a.id: r["cobertura"] = f"{len(data['vistas'])}/{len(data['laminas'])} láminas · {cov['porcentaje_mirado']} % de fotogramas"
    write_index(rows); print(json.dumps(cov, ensure_ascii=False, indent=1))

def cmd_voz(a):
    """Importa la locución con tiempos de un Reel propio (tools/reelNN/voz.tsv: inicio, fin, palabra)."""
    vdir, data = load(a.id); words = []
    for ln in open(a.tsv, encoding="utf-8"):
        p = ln.rstrip("\n").split("\t")
        if len(p) >= 3:
            try: words.append({"desde": float(p[0]), "hasta": float(p[1]), "palabra": p[2]})
            except ValueError: pass
    if not words: sys.exit("No he podido leer palabras con tiempos en " + a.tsv)
    frases = []; cur = []
    for i, w in enumerate(words):
        cur.append(w); nxt = words[i + 1]["desde"] if i + 1 < len(words) else None
        if re.search(r"[.?!…]$", w["palabra"]) or nxt is None or nxt - w["hasta"] > 0.45:
            frases.append({"desde": cur[0]["desde"], "hasta": cur[-1]["hasta"], "texto": " ".join(x["palabra"] for x in cur),
                           "palabras_por_s": round(len(cur) / max(cur[-1]["hasta"] - cur[0]["desde"], 0.2), 2)}); cur = []
    pausas = [{"desde": words[i]["hasta"], "hasta": words[i + 1]["desde"], "duracion_s": round(words[i + 1]["desde"] - words[i]["hasta"], 2)}
              for i in range(len(words) - 1) if words[i + 1]["desde"] - words[i]["hasta"] >= 0.35]
    dur = words[-1]["hasta"] - words[0]["desde"]
    out = {"origen": os.path.relpath(os.path.abspath(a.tsv), ROOT), "tipo": "locución generada con tiempos por palabra (exacta, no reconocida por oído)",
           "palabras": len(words), "primera_palabra_s": words[0]["desde"], "ultima_palabra_s": words[-1]["hasta"],
           "ritmo_palabras_por_s": round(len(words) / max(dur, 0.1), 2), "frases": frases, "pausas": pausas, "por_palabra": words}
    json.dump(out, open(os.path.join(vdir, "transcripcion.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    data["audio"]["transcripcion"] = "transcripcion.json (" + out["origen"] + ")"; save(vdir, data); report(vdir, data)
    print(json.dumps({k: out[k] for k in ("palabras", "primera_palabra_s", "ultima_palabra_s", "ritmo_palabras_por_s")} | {"frases": [f"{tc(f['desde'])} {f['texto']}" for f in frases], "pausas": pausas}, ensure_ascii=False, indent=1))

RASGOS = os.path.join(INTEL, "aprendizaje", "CARACTERISTICAS.csv")
RCOLS = ["id", "marca", "tipo", "formato", "duracion_s", "planos", "cortes_por_10s", "plano_medio_s", "plano_mas_largo_s", "plano_mas_corto_s",
         "tramos_estaticos", "s_estaticos", "primera_palabra_s", "ultima_palabra_s", "cola_tras_voz_s", "palabras", "palabras_por_s", "lufs",
         "apertura", "tipo_hook", "estructura", "territorio", "ficha_guardable_s", "producto", "cta",
         "saltos_3s_pct", "tiempo_medio_s", "retencion_pct", "guardados_x1000", "compartidos_x1000", "visita_llena", "leido_el"]
def cmd_rasgos(a):
    """Vuelca las características medidas a intel/aprendizaje/CARACTERISTICAS.csv (06 completa a mano las codificadas y las métricas)."""
    vdir, d = load(a.id); m, mo = d["meta"], d["montaje"]; tr = {}
    tp = os.path.join(vdir, "transcripcion.json")
    if os.path.exists(tp): tr = json.load(open(tp, encoding="utf-8"))
    rows = []
    if os.path.exists(RASGOS): rows = list(csv.DictReader(open(RASGOS, newline="", encoding="utf-8")))
    old = next((r for r in rows if r["id"] == a.id), {})
    new = dict(old); new.update({"id": a.id, "marca": m["marca"], "tipo": m["tipo"], "formato": m["formato"], "duracion_s": m["duracion_s"], "planos": mo["planos"],
        "cortes_por_10s": mo["cortes_por_10s"], "plano_medio_s": mo["duracion_media_plano_s"], "plano_mas_largo_s": mo["plano_mas_largo_s"], "plano_mas_corto_s": mo["plano_mas_corto_s"],
        "tramos_estaticos": len(mo["tramos_estaticos"]), "s_estaticos": round(sum(x["duracion_s"] for x in mo["tramos_estaticos"]), 2),
        "primera_palabra_s": tr.get("primera_palabra_s", ""), "ultima_palabra_s": tr.get("ultima_palabra_s", ""),
        "cola_tras_voz_s": round(m["duracion_s"] - tr["ultima_palabra_s"], 2) if tr else "", "palabras": tr.get("palabras", ""), "palabras_por_s": tr.get("ritmo_palabras_por_s", ""),
        "lufs": d["audio"].get("volumen_integrado_lufs", "")})
    os.makedirs(os.path.dirname(RASGOS), exist_ok=True)
    with open(RASGOS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=RCOLS); w.writeheader()
        for r in sorted([r for r in rows if r["id"] != a.id] + [new], key=lambda r: r["id"]): w.writerow({c: r.get(c, "") for c in RCOLS})
    print(json.dumps({k: v for k, v in new.items() if v != ""}, ensure_ascii=False))

def cmd_estado(a):
    _, data = load(a.id); print(json.dumps(coverage(data), ensure_ascii=False, indent=1))

def cmd_buscar(a):
    q = (a.texto or "").lower()
    for r in read_index():
        if not q or q in " ".join(r.values()).lower(): print(" · ".join(f"{k}={r[k]}" for k in ("id", "marca", "tipo", "formato", "tema", "fecha_analisis", "duracion_s", "cortes", "cobertura", "ruta")))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("analyze"); p.add_argument("video"); p.add_argument("--id", required=True); p.add_argument("--marca", default="proteam")
    p.add_argument("--tipo", default="propio", choices=["propio", "competencia", "referencia"]); p.add_argument("--formato", default="reel"); p.add_argument("--tema", default="")
    p.add_argument("--fuente", default=""); p.add_argument("--modo", default="detalle", choices=["general", "detalle", "completo"]); p.add_argument("--fps", type=float, default=4.0); p.set_defaults(f=cmd_analyze)
    p = sp.add_parser("window"); p.add_argument("id"); p.add_argument("--desde", type=float, required=True); p.add_argument("--hasta", type=float, required=True); p.set_defaults(f=cmd_window)
    p = sp.add_parser("visto"); p.add_argument("id"); p.add_argument("laminas", nargs="+"); p.set_defaults(f=cmd_visto)
    p = sp.add_parser("voz"); p.add_argument("id"); p.add_argument("tsv"); p.set_defaults(f=cmd_voz)
    p = sp.add_parser("rasgos"); p.add_argument("id"); p.set_defaults(f=cmd_rasgos)
    p = sp.add_parser("estado"); p.add_argument("id"); p.set_defaults(f=cmd_estado)
    p = sp.add_parser("buscar"); p.add_argument("texto", nargs="?"); p.set_defaults(f=cmd_buscar)
    a = ap.parse_args(); a.f(a)
