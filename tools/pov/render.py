"""PNG transparente (estado final) + WebM VP9 con alfa (entrada animada, 2 s a 30 fps) de cada gráfico."""
import os, sys, glob, subprocess, shutil
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(os.path.dirname(H)); O=os.path.join(R,'agencia','recursos','pov'); os.makedirs(O,exist_ok=True)
names=sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(H,'g*.html')))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for k in names:
        pg.goto('file://'+os.path.join(H,k+'.html')); pg.evaluate('document.fonts.ready')
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        tmp=os.path.join(H,'_f'); shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
        for i in range(60):
            t=i*1000/30
            pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t})")
            pg.screenshot(path=os.path.join(tmp,f'{i:03d}.png'),omit_background=True)
        shutil.copy(os.path.join(tmp,'059.png'),os.path.join(O,k+'.png'))
        subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',os.path.join(tmp,'%03d.png'),'-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','2M',os.path.join(O,k+'.webm')],check=True)
        shutil.rmtree(tmp)
    b.close()
