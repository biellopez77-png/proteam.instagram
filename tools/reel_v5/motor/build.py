"""Fabrica un reel editorial 2D de ProTeam a partir de piezas/<ID>/spec.json.
  python3 tools/reel_v5/motor/build.py ID [--still]
spec.json: {"titulo","numero","paginas":[{"tipo":..., "d":seg, ...}], "portada_t": seg}
Fotos: nombre del banco sin 'PROTEAM_' ni '.jpg' (p. ej. OBJETO_BALONES_CARRO_FOTO_001).
Las *_CAPTURA_* se usan tal cual (capturas reales de la app); el resto pasa a duotono azul."""
import sys, os, json, csv, subprocess, wave
import numpy as np
from PIL import Image, ImageOps
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
ID = sys.argv[1]; STILL = '--still' in sys.argv
PZ = f'{R}/tools/reel_v5/piezas/{ID}'; os.makedirs(f'{PZ}/img', exist_ok=True)
spec = json.load(open(f'{PZ}/spec.json'))
inv = {r['nombre']: r for r in csv.DictReader(open(f'{R}/banco/INVENTARIO.csv'))}
ST = [(0, (2, 5, 15)), (.45, (47, 60, 170)), (.75, (106, 168, 255)), (1, (244, 247, 251))]
def duo(im):
    g = np.asarray(ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)).astype(float) / 255
    return Image.fromarray(np.stack([np.interp(g, [s[0] for s in ST], [s[1][c] for s in ST]) for c in range(3)], -1).astype('uint8'))
def foto(n):
    f = f'PROTEAM_{n}.jpg'; src = f'{R}/banco/' + ('proteam' if 'CAPTURA' in n else 'fotos') + f'/{f}'; out = f'{PZ}/img/{n}.jpg'
    if not os.path.exists(src): sys.exit(f'falta la foto {f}')
    lic = (inv.get(f, {}).get('licencia') or '').lower()
    if 'sin verificar' in lic or 'decisi' in (inv.get(f, {}).get('uso_comercial') or '').lower(): sys.exit(f'{f}: licencia sin verificar, no se usa')
    if not os.path.exists(out):
        im = Image.open(src).convert('RGB'); im.thumbnail((1800, 1800))
        (im if 'CAPTURA' in n else duo(im)).save(out, quality=92)
    return f'../piezas/{ID}/img/{n}.jpg', f
def credito(fs):
    au, li = [], []
    for f in fs:
        r = inv.get(f, {})
        if 'CAPTURA' in f: au.append('ProTeam (captura real)'); continue
        a = (r.get('autor') or '').strip() or 'Wikimedia Commons'; l = (r.get('licencia') or '').strip()
        a = a.split('(')[0].strip() or a; au.append(a); li.append('DP' if 'dominio' in l.lower() or l.upper() == 'CC0' else l)
    au = list(dict.fromkeys(au)); li = list(dict.fromkeys(li))
    return ('Foto: ' if len(au) == 1 else 'Fotos: ') + ' · '.join(au) + (' · ' + ' / '.join(li) if li else '')
pag = 1
for p in spec['paginas']:
    used = []
    if p.get('foto'): p['foto'], f = foto(p['foto']); used.append(f)
    if p.get('fotos'): r = [foto(x) for x in p['fotos']]; p['fotos'] = [a for a, _ in r]; used += [b for _, b in r]
    for fg in p.get('figs', []): fg['foto'], f = foto(fg['foto']); used.append(f)
    p['credito'] = credito(used) if used else ''
    if p['tipo'] != 'cierre': p['folio'] = f'p. {pag:02d}' if p['tipo'] != 'reticula' else f'pp. {pag:02d}–{pag+1:02d}'
    pag += 2 if p['tipo'] == 'reticula' else 1 + (pag % 3 == 0) * 3
json.dump(spec, open(f'{PZ}/spec.resolved.json', 'w'), ensure_ascii=False)
# ---- sonido sintetizado (sin licencias) ----
T = sum(p['d'] for p in spec['paginas']) + .2; sr = 48000; n = int(sr * T); t = np.arange(n) / sr; a = np.zeros(n)
rng = np.random.default_rng(len(ID)); nz = rng.standard_normal(n)
f = np.fft.rfft(nz); fr = np.fft.rfftfreq(n, 1 / sr); f[(fr < 800) | (fr > 6000)] = 0; nz = np.fft.irfft(f, n); nz /= np.abs(nz).max()
def env(t0, at, de):
    x = t - t0; y = np.zeros(n); m = x >= 0; xm = x[m]; y[m] = np.where(xm < at, xm / at, np.exp(-np.minimum((xm - at) / de, 50))); return y
root = spec.get('tono', 55.0)
gate = np.clip(t / 1.0, 0, 1) * np.clip((T - t) / .6, 0, 1)
t0 = 0
for i, p in enumerate(spec['paginas']):
    d = p['d']
    if i: a += nz * env(t0 - .08, .06, .22 if p['tipo'] != 'cierre' else .45) * .22
    if p['tipo'] in ('palabra', 'reticula', 'portada', 'captura'):
        for k in ([.3, 1.0] if p['tipo'] == 'palabra' else [.1, d * .35, d * .6] if p['tipo'] == 'reticula' else [.75, .9, 1.05]):
            a += np.sin(2 * np.pi * 2400 * t) * env(t0 + k, .001, .012) * .16 + nz * env(t0 + k, .001, .02) * .1
    if p['tipo'] in ('dentro', 'cifra'): a += np.sin(2 * np.pi * 45 * t * (1 + .5 * env(t0, .001, .08))) * env(t0, .003, .35) * .45
    if p['tipo'] == 'frase':
        gate *= np.where((t > t0 - .5) & (t < t0 + .6), np.clip(np.abs(t - t0) / .55, 0, 1) ** 3, 1)
        if p.get('uv'):
            for fq in [261.6, 329.6, 392.0, 523.3]: a += np.sin(2 * np.pi * fq * t) * np.clip((t - t0 - 1.4) / .7, 0, 1) * np.exp(-np.clip(t - t0 - 2.1, 0, None) / 1.2) * .045
    if p['tipo'] == 'cierre':
        for fq in [2 * root, 3 * root, 4 * root, 6 * root]: a += np.sin(2 * np.pi * fq * t) * env(t0 + .1, .4, 1.4) * .06
    t0 += d
a += (np.sin(2 * np.pi * root * t) * .5 + np.sin(2 * np.pi * root * 1.498 * t) * .25 + np.sin(2 * np.pi * root * 2.005 * t) * .12) * .1 * gate
a = np.tanh(a * 1.6) / 1.6; a /= np.abs(a).max() * 1.12; st = np.stack([a, np.roll(a, 24)], 1)
w = wave.open(f'{PZ}/sonido.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st * 32767).astype('<i2').tobytes()); w.close()
page = f'tools/reel_v5/motor/motor.html?spec=../piezas/{ID}/spec.resolved.json'
os.chdir(f'{R}/tools/blackout')
if STILL:
    ts = []; t0 = 0
    for p in spec['paginas']: ts.append(round(t0 + p['d'] * .75, 2)); t0 += p['d']
    subprocess.run(['python3', 'htmlreel.py', 'still', page, f'{PZ}/st'] + [str(x) for x in ts], check=True, capture_output=True)
    ims = [Image.open(f'{PZ}/st-{x}.png').resize((270, 480)) for x in ts]
    sh = Image.new('RGB', (270 * len(ims), 480)); [sh.paste(im, (i * 270, 0)) for i, im in enumerate(ims)]; sh.save(f'{PZ}/hoja.png')
    [os.remove(f'{PZ}/st-{x}.png') for x in ts]; print('hoja', f'{PZ}/hoja.png'); sys.exit()
raw = f'/tmp/{ID}_raw.mp4'
subprocess.run(['python3', 'htmlreel.py', 'video', page, raw, str(T), f'{PZ}/sonido.wav'], check=True, capture_output=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-c:v', 'libx264', '-preset', 'veryfast', '-b:v', '5M', '-maxrate', '6M', '-bufsize', '10M', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', f'{PZ}/final.mp4'], check=True)
ct = spec.get('portada_t', T * .8)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ct), '-i', f'{PZ}/final.mp4', '-frames:v', '1', '-q:v', '3', f'{PZ}/cover.jpg'], check=True)
os.remove(raw); print('ok', f'{PZ}/final.mp4', round(T, 1), 's')
