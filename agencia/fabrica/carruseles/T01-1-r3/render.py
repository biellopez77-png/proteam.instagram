import sys, os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); out=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch()
    for k in ['c1','c2','c3','c4','c5','c6','s1','s2']:
        h=1920 if k.startswith('s') else 1440
        pg=b.new_page(viewport={'width':1080,'height':h})
        pg.goto('file://'+os.path.join(D,k+'.html')); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(out,f'T01-1-r3-{k}.png'))
    b.close()
# JPEG 1080×1350 para la cola (recorte centrado de la caja común)
from PIL import Image
for k in ['c1','c2','c3','c4','c5','c6']:
    im=Image.open(os.path.join(out,f'T01-1-r3-{k}.png')).convert('RGB')
    im.crop((0,45,1080,1395)).save(os.path.join(out,f'T01-1-r3-{k}.jpg'),quality=92)
