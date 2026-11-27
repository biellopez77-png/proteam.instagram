"""Render de «Edu y Clara». python3 tools/wurtz/render.py video out/edu-y-clara.mp4 | still t1 f1.jpg [t2 f2.jpg …]"""
import json, os, subprocess, sys, time
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); a = sys.argv[1:]
TL = json.load(open(os.path.join(D, 'out', 'timeline.json')))
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    pg.on('console', lambda m: print('console:', m.text) if m.type in ('error', 'warning') else None)
    pg.on('pageerror', lambda e: print('pageerror:', e))
    pg.add_init_script(f'window.TIMELINE={json.dumps(TL)};')
    pg.goto('file://' + os.path.join(D, 'film.html')); pg.evaluate('READY()')
    if a[0] == 'still':
        for i in range(1, len(a), 2):
            t0 = time.time(); pg.evaluate(f'render({float(a[i])})'); pg.screenshot(path=a[i + 1], type='jpeg', quality=88); print(a[i], round(time.time() - t0, 2), 's')
    else:
        out = a[1]; fps = 30; n = int(TL['total'] * fps)
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-', '-i', os.path.join(D, 'out', 'audio.wav'),
                               '-c:a', 'aac', '-b:a', '192k', '-shortest', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
        t0 = time.time()
        for i in range(n):
            pg.evaluate(f'render({i / fps})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=90))
            if i % 300 == 0: print(f'{i}/{n} {time.time() - t0:.0f}s', file=sys.stderr, flush=True)
        ff.stdin.close(); ff.wait()
    b.close()
