"""Reels de motion graphics (mg.html) -> mp4 con audio.
  python3 mgvideo.py still r03 15 t1 t2 ... out_prefix     (fotogramas de control)
  python3 mgvideo.py video reels/r03.json reels/r03.mp4    (json: {mg, d, ...})"""
import sys, io, json, subprocess, numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve, develop
W, H, FPS = 1080, 1920, 30
def page(p, port, d):
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    pg.on('pageerror', lambda e: print('ERR', e))
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/mg.html?d={d}'); pg.wait_for_function('window.READY===true', timeout=60000); return b, pg
def frame(pg, rid, t, seed):
    pg.evaluate(f'window.render("{rid}", {t})')
    return develop(Image.open(io.BytesIO(pg.screenshot())), seed=seed, bloom=.25, grain=7, vig=.35)
if __name__ == '__main__':
    port = serve(); c = sys.argv[1]
    with sync_playwright() as p:
        if c == 'still':
            rid, d, *ts, pre = sys.argv[2:]; b, pg = page(p, port, d)
            for t in ts: frame(pg, rid, float(t), 0).save(f'{pre}-{t}.jpg', quality=90)
        else:
            spec = json.load(open(sys.argv[2])); out = sys.argv[3]; rid = spec['mg']; b, pg = page(p, port, spec['d'])
            dur = spec['dur']; N = int(dur * FPS)
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                '-i', sys.argv[2].replace('.json', '.wav'), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '9M', '-bufsize', '18M',
                '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(N):
                ff.stdin.write(frame(pg, rid, min(i / FPS, spec['dur'] - .01), i).convert('RGB').tobytes())
                if i % 90 == 0: print(f'{i}/{N}', flush=True)
            ff.stdin.close(); ff.wait(); print('ok', out)
        b.close()
