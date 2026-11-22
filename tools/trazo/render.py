"""Render de escenas de Trazo (sin IA): canvas + Playwright + ffmpeg. Coste 0 €.

  python3 tools/trazo/render.py video escenas/presentacion.js reels/t01-presentacion.mp4 [--audio sonido.wav]
  python3 tools/trazo/render.py still escenas/cuenta.js feed/cuenta-7.jpg --t 7 --w 1080 --h 1350

La escena (JS) define window.SCENE = {w, h, dur, fps, draw(ctx, t, args)}. En `still`, --t se pasa a draw como t.
"""
import argparse, base64, os, subprocess, sys
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(D)

HTML = '''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:M;font-weight:500;src:url(../fonts/manrope-latin-500-normal.woff2)}
@font-face{font-family:M;font-weight:700;src:url(../fonts/manrope-latin-700-normal.woff2)}
@font-face{font-family:M;font-weight:800;src:url(../fonts/manrope-latin-800-normal.woff2)}
@font-face{font-family:S;font-style:italic;font-weight:400;src:url(../fonts/instrument-serif-latin-400-italic.woff2)}
@font-face{font-family:P;font-weight:500;src:url(../fonts/ibm-plex-mono-latin-500-normal.woff2)}
html,body{margin:0;background:#fff}</style></head><body>
<canvas id="c"></canvas><span style="font-family:M;font-weight:800">.</span><span style="font-family:M;font-weight:700">.</span><span style="font-family:S;font-style:italic">.</span><span style="font-family:P">.</span>
<script src="trazo.js"></script><script src="__SRC__"></script>
<script>
window.LOGO=new Image();LOGO.src='__LOGO__';
const c=document.getElementById('c');
window.setup=(w,h)=>{c.width=w;c.height=h;};
window.frame=(t,args,q)=>{const ctx=c.getContext('2d');ctx.setTransform(1,0,0,1,0,0);SCENE.draw(ctx,t,args||{});return c.toDataURL('image/jpeg',q||0.92);};
</script></body></html>'''


def open_page(p, scene):
    page_path = os.path.join(D, '_page.html')
    open(page_path, 'w').write(HTML.replace("__SRC__", os.path.relpath(os.path.abspath(scene), D)).replace("__LOGO__", "data:image/webp;base64," + base64.b64encode(open(os.path.join(TOOLS, "proteam-mark.webp"), "rb").read()).decode()))
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto('file://' + page_path)
    pg.evaluate('document.fonts.ready.then(()=>1)')
    pg.wait_for_function('window.LOGO && LOGO.complete && document.fonts.status=="loaded"')
    return b, pg


def main():
    a = argparse.ArgumentParser()
    a.add_argument('mode', choices=['video', 'still'])
    a.add_argument('scene'); a.add_argument('out')
    a.add_argument('--t', type=float, default=0); a.add_argument('--w', type=int); a.add_argument('--h', type=int)
    a.add_argument('--audio'); a.add_argument('--args', default='{}')
    o = a.parse_args()
    with sync_playwright() as p:
        b, pg = open_page(p, o.scene)
        S = pg.evaluate('({w:SCENE.w,h:SCENE.h,dur:SCENE.dur||0,fps:SCENE.fps||30})')
        w, h = o.w or S['w'], o.h or S['h']
        pg.evaluate(f'setup({w},{h})')
        import json; args = json.loads(o.args); args.update({'w': w, 'h': h})
        os.makedirs(os.path.dirname(os.path.abspath(o.out)), exist_ok=True)
        if o.mode == 'still':
            u = pg.evaluate('([t,a])=>frame(t,a,0.93)', [o.t, args])
            open(o.out, 'wb').write(base64.b64decode(u.split(',')[1]))
        else:
            fps, n = S['fps'], int(S['dur'] * S['fps'])
            cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-']
            if o.audio: cmd += ['-i', o.audio, '-c:a', 'aac', '-b:a', '160k', '-shortest']
            cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', o.out]
            ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
            for i in range(n):
                u = pg.evaluate('([t,a])=>frame(t,a,0.9)', [i / fps, args])
                ff.stdin.write(base64.b64decode(u.split(',')[1]))
                if i % 150 == 0: print(f'{i}/{n}', file=sys.stderr)
            ff.stdin.close(); ff.wait()
        b.close()
    os.remove(os.path.join(D, '_page.html'))
    print(o.out)


if __name__ == '__main__':
    main()
