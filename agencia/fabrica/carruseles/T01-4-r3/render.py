import sys, os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); out=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch()
    for k in ['c1','c2','c3','c4','c5','c6','c7','s1','s2']:
        h=1920 if k.startswith('s') else 1440
        pg=b.new_page(viewport={'width':1080,'height':h})
        pg.goto('file://'+os.path.join(D,k+'.html')); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(out,f'T01-4-r3-{k}.png'))
    b.close()
