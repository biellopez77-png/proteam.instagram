"""Render tools/carrusel11/index.html -> feed/c11-N.jpg (1080x1350, JPEG 90)."""
import os, io
from playwright.sync_api import sync_playwright
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(H))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
    pg.goto('file://' + os.path.join(H, 'index.html')); pg.wait_for_timeout(800)
    pg.evaluate('document.fonts.ready')
    n = pg.locator('.s').count()
    for i in range(n):
        png = pg.locator('.s').nth(i).screenshot()
        Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(R, 'feed', f'c11-{i+1}.jpg'), quality=90)
    b.close(); print(n, 'diapositivas')
