"""Bodegones 3D -> 'foto': render en Chromium (swiftshader) + revelado (bloom, grano, viñeta, aberración).
  python3 photo.py silbato out/x.png [w h] [d=15]"""
import sys, threading, http.server, socketserver, functools, os, io
import numpy as np
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FLAGS = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']

def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT); h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start(); return s.server_address[1]

def develop(im, seed=0, bloom=.55, grain=9, vig=.55, dof=0):
    if dof:  # desenfoque de fondo: la parte alta del encuadre (lejos) se desenfoca
        bl = im.convert('RGB').filter(ImageFilter.GaussianBlur(dof)); w0, h0 = im.size
        mk = Image.fromarray((np.clip(1 - (np.mgrid[0:h0, 0:w0][0] / h0 - .12) / .3, 0, 1) * 255).astype(np.uint8))
        im = Image.composite(bl, im.convert('RGB'), mk)
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    lum = a.mean(2, keepdims=True); hi = np.clip((lum - .78) / .22, 0, 1) * a
    hiI = Image.fromarray((hi * 255).astype(np.uint8))
    b = sum(np.asarray(hiI.filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255 for r in (6, 18, 48)) / 3
    a = 1 - (1 - a) * (1 - b * bloom * 2)
    h, w = a.shape[:2]; yy, xx = np.mgrid[0:h, 0:w]; d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a *= (1 - vig * np.clip(d - .35, 0, 1) ** 1.6)[..., None]
    # aberración cromática leve en bordes
    s = 2; a[..., 0] = np.roll(a[..., 0], s, 1) * (d > .6) + a[..., 0] * (d <= .6)
    a[..., 2] = np.roll(a[..., 2], -s, 1) * (d > .6) + a[..., 2] * (d <= .6)
    rng = np.random.default_rng(seed); g = rng.normal(0, grain / 255, (h, w, 1)) * (0.6 + .8 * (1 - a.mean(2, keepdims=True)))
    a = np.clip(a + g, 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8))

def shoot(pairs):  # pairs: [(query, out)]
    port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(args=FLAGS)
        for q, out in pairs:
            w = int(dict(x.split('=') for x in q.split('&')).get('w', 1080)); h = int(dict(x.split('=') for x in q.split('&')).get('h', 1350))
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.on('console', lambda m: print('console:', m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: print('ERR', e))
            pg.goto(f'http://127.0.0.1:{port}/tools/blackout/studio.html?{q}'); pg.wait_for_function('window.READY===true', timeout=180000)
            raw = Image.open(io.BytesIO(pg.screenshot()))
            develop(raw, dof=int(dict(x.split('=') for x in q.split('&')).get('dof', 0))).save(out); print('ok', out)
        b.close()

if __name__ == '__main__':
    a = sys.argv[1:]; shoot([(a[i], a[i + 1]) for i in range(0, len(a), 2)])
