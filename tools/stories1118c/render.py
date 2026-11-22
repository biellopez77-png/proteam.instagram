"""Render tools/stories1118c/*.html -> stories/ (1080x1920, JPEG 90)."""
import os, io
from playwright.sync_api import sync_playwright
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(os.path.dirname(H))
out={'a':'st-1118-lo-que-no-se-ve.jpg','b':'st-1118-entra-antes.jpg','c':'st-1119-hecha-en-el-banquillo.jpg'}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
    for k,f in out.items():
        pg.goto('file://'+os.path.join(H,k+'.html')); pg.wait_for_timeout(600); pg.evaluate('document.fonts.ready')
        Image.open(io.BytesIO(pg.locator('.s').screenshot())).convert('RGB').save(os.path.join(R,'stories',f),quality=90)
    b.close()
