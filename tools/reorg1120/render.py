import os, io, sys
from playwright.sync_api import sync_playwright
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(os.path.dirname(H)); O=os.path.join(R,'stories','reorg1120'); os.makedirs(O,exist_ok=True)
names=sys.argv[1:] or ['r1','r2','r3','r4']
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for k in names:
        pg.goto('file://'+os.path.join(H,k+'.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(400)
        Image.open(io.BytesIO(pg.locator('.s').screenshot())).convert('RGB').save(os.path.join(O,k+'.jpg'),quality=92)
    b.close()
