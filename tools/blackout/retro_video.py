"""Reels de la identidad retro (retro.html) con efecto de tele de tubo (crt.py).
  python3 retro_video.py still r01 15 t1 t2 ... prefijo
  python3 retro_video.py video reels/x.json reels/x.mp4   (json: {retro, d, dur, ...}; audio en reels/x.wav)"""
import sys, io, json, subprocess
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
from crt import crt
W, H, FPS = 1080, 1920, 30
def page(p, port, d):
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    pg.on('pageerror', lambda e: print('ERR', e))
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/retro.html?d={d}'); pg.wait_for_function('window.READY===true', timeout=60000); return b, pg
def set_ep(pg, ep): pg.evaluate('(e) => { window.EP = e; }', ep)
def frame(pg, rid, t, seed):
    pg.evaluate(f'window.render("{rid}", {t})'); a = pg.evaluate(f'window.crtAmount("{rid}", {t})')
    return crt(Image.open(io.BytesIO(pg.screenshot())), a, t, seed)
if __name__ == '__main__':
    port = serve(); c = sys.argv[1]
    with sync_playwright() as p:
        if c == 'epstill':  # epstill spec.json t1 t2 ... prefijo
            spec = json.load(open(sys.argv[2])); *ts, pre = sys.argv[3:]; b, pg = page(p, port, spec['d']); set_ep(pg, spec['ep'])
            for t in ts: frame(pg, 'ep', float(t), 0).save(f'{pre}-{t}.jpg', quality=88)
        elif c == 'still':
            rid, d, *ts, pre = sys.argv[2:]; b, pg = page(p, port, d)
            for t in ts: frame(pg, rid, float(t), 0).save(f'{pre}-{t}.jpg', quality=90)
        else:
            spec = json.load(open(sys.argv[2])); out = sys.argv[3]; b, pg = page(p, port, spec['d'])
            if 'ep' in spec: set_ep(pg, spec['ep'])
            N = int(spec['dur'] * FPS)
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                '-i', sys.argv[2].replace('.json', '.wav'), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '9M', '-bufsize', '18M',
                '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(N):
                ff.stdin.write(frame(pg, spec['retro'], i / FPS, i).convert('RGB').tobytes())
                if i % 90 == 0: print(f'{i}/{N}', flush=True)
            ff.stdin.close(); ff.wait(); print('ok', out)
        b.close()
