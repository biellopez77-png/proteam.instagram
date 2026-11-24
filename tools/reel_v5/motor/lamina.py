"""Láminas editoriales 2D de ProTeam (carrusel 1080×1350 y Stories 1080×1920).
  python3 tools/reel_v5/motor/lamina.py ID            # renderiza carrusel.json y stories.json
  python3 tools/reel_v5/motor/lamina.py ID --hoja     # además, hoja de contacto a tamaño móvil
Fuentes en agencia/fabrica-v4/carruseles/<ID>/:
  carrusel.json {"numero":"Nº 00","seccion":"…","formato":"carrusel","laminas":[{"tipo":…}, …]}
  stories.json  {"numero":"Nº 00","seccion":"…","formato":"story","laminas":[…]}
Tipos (ver lamina.html): palabra, dentro, figuras, frase (uv:true una vez por carrusel), portada, final, pregunta, encuesta.
Fotos: nombre del banco sin 'PROTEAM_' ni '.jpg'. Duotono azul y créditos como en build.py (mismo inventario y mismas reglas de licencia).
Salida: <ID>/png/<ID>-c1.png … y <ID>-s1.png, <ID>-s2.png."""
import sys, os, json
from PIL import Image
sys.argv_orig = list(sys.argv)
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, f'{R}/tools/blackout')
from photo import serve, FLAGS
import csv
from PIL import ImageOps
import numpy as np
ID = sys.argv[1]; HOJA = '--hoja' in sys.argv
D = f'{R}/agencia/fabrica-v4/carruseles/{ID}'; os.makedirs(f'{D}/img', exist_ok=True); os.makedirs(f'{D}/png', exist_ok=True)
inv = {r['nombre']: r for r in csv.DictReader(open(f'{R}/banco/INVENTARIO.csv'))}
ST = [(0, (2, 5, 15)), (.45, (47, 60, 170)), (.75, (106, 168, 255)), (1, (244, 247, 251))]
def duo(im):
    g = np.asarray(ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)).astype(float) / 255
    return Image.fromarray(np.stack([np.interp(g, [s[0] for s in ST], [s[1][c] for s in ST]) for c in range(3)], -1).astype('uint8'))
def foto(n):
    f = f'PROTEAM_{n}.jpg'; src = f'{R}/banco/' + ('proteam' if 'CAPTURA' in n else 'fotos') + f'/{f}'; out = f'{D}/img/{n}.jpg'
    if not os.path.exists(src): sys.exit(f'falta la foto {f}')
    lic = (inv.get(f, {}).get('licencia') or '').lower()
    if 'sin verificar' in lic or 'decisi' in (inv.get(f, {}).get('uso_comercial') or '').lower(): sys.exit(f'{f}: licencia sin verificar, no se usa')
    if not os.path.exists(out):
        im = Image.open(src).convert('RGB'); im.thumbnail((2000, 2000))
        (im if 'CAPTURA' in n else duo(im)).save(out, quality=92)
    return f'../../../agencia/fabrica-v4/carruseles/{ID}/img/{n}.jpg', f
def credito(fs):
    au, li = [], []
    for f in fs:
        r = inv.get(f, {})
        if 'CAPTURA' in f: au.append('ProTeam (captura real)'); continue
        a = (r.get('autor') or '').strip() or 'Wikimedia Commons'; l = (r.get('licencia') or '').strip()
        a = a.split('(')[0].strip() or a; au.append(a); li.append('DP' if 'dominio' in l.lower() or l.upper() == 'CC0' else l)
    au = list(dict.fromkeys(au)); li = list(dict.fromkeys(li))
    return ('Foto: ' if len(au) == 1 else 'Fotos: ') + ' · '.join(au) + (' · ' + ' / '.join(li) if li else '')
jobs = []
for nombre, pre in (('carrusel', 'c'), ('stories', 's')):
    src = f'{D}/{nombre}.json'
    if not os.path.exists(src): continue
    spec = json.load(open(src)); uv = 0
    for k, p in enumerate(spec['laminas']):
        used = []
        if p.get('foto'): p['foto'], f = foto(p['foto']); used.append(f)
        if p.get('fotos'): r = [foto(x) for x in p['fotos']]; p['fotos'] = [a for a, _ in r]; used += [b for _, b in r]
        for fg in p.get('figs', []): fg['foto'], f = foto(fg['foto']); used.append(f)
        p['credito'] = credito(used) if used else ''
        p.setdefault('folio', f'p. {k + 1:02d}')
        uv += bool(p.get('uv'))
    if spec['formato'] == 'carrusel' and uv != 1: sys.exit(f'el ultravioleta va en UNA lámina del carrusel (hay {uv})')
    json.dump(spec, open(f'{D}/{nombre}.resolved.json', 'w'), ensure_ascii=False)
    for k in range(len(spec['laminas'])):
        jobs.append((f'../../../agencia/fabrica-v4/carruseles/{ID}/{nombre}.resolved.json', k, 1920 if spec['formato'] == 'story' else 1350, f'{D}/png/{ID}-{pre}{k + 1}.png'))
from playwright.sync_api import sync_playwright
port = serve(); outs = []
with sync_playwright() as pw:
    b = pw.chromium.launch(args=FLAGS)
    for sp, k, h, out in jobs:
        pg = b.new_page(viewport={'width': 1080, 'height': h})
        pg.on('pageerror', lambda e: print('ERR', e))
        pg.goto(f'http://127.0.0.1:{port}/tools/reel_v5/motor/lamina.html?spec={sp}&i={k}'); pg.wait_for_function('window.ready', timeout=60000)
        pg.screenshot(path=out); pg.close(); outs.append(out); print('ok', out)
    b.close()
if HOJA:  # tamaño móvil: 360 px de ancho, como se ve en el feed
    ims = [Image.open(o) for o in outs]; ims = [im.resize((360, int(im.height / 3))) for im in ims]
    W = sum(im.width for im in ims) + 12 * (len(ims) + 1); Hh = max(im.height for im in ims) + 24
    sh = Image.new('RGB', (W, Hh), (40, 40, 40)); x = 12
    for im in ims: sh.paste(im, (x, 12)); x += im.width + 12
    sh.save(f'{D}/hoja.png'); print('hoja', f'{D}/hoja.png')
