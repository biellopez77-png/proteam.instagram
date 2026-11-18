"""Render tools/stories1118d/*.html -> stories/ (1080x1920, JPEG 90). Versiones con menos texto (encargo de Biel, 18/11)."""
import os, io
from playwright.sync_api import sync_playwright
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(os.path.dirname(H))
out={'a':'st-1118-diez-dias-v3.jpg','b':'st-1118-que-categoria-v3.jpg','c':'st-1118-mandasela-v2.jpg','d':'st-1118-lo-que-no-se-ve-v2.jpg','e':'st-1118-entra-antes-v2.jpg','f':'st-1119-hecha-en-el-banquillo-v2.jpg'}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
    for k,f in out.items():
        pg.goto('file://'+os.path.join(H,k+'.html')); pg.wait_for_timeout(600); pg.evaluate('document.fonts.ready')
        Image.open(io.BytesIO(pg.locator('.s').screenshot())).convert('RGB').save(os.path.join(R,'stories',f),quality=90)
    b.close()
