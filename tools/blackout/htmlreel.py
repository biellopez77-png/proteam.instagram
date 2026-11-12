"""Renderiza una página con window.frame(t) a vídeo o fotogramas sueltos.
  python3 htmlreel.py still pagina.html out_prefix t1 t2 ...
  python3 htmlreel.py video pagina.html out.mp4 DURACION [audio.wav]"""
import sys, os, subprocess, shutil
from playwright.sync_api import sync_playwright
from photo import serve, FLAGS
mode, page = sys.argv[1], sys.argv[2]; port = serve(); FPS = 25
with sync_playwright() as p:
    b = p.chromium.launch(args=FLAGS); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.on('console', lambda m: print('console:', m.text) if m.type == 'error' else None)
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/{page}'); pg.wait_for_function('window.ready', timeout=120000)
    if mode == 'still':
        pre = sys.argv[3]
        for t in sys.argv[4:]: pg.evaluate(f'frame({t})'); pg.screenshot(path=f'{pre}-{t}.png')
    else:
        out, dur = sys.argv[3], float(sys.argv[4]); D = out + '_f'; os.makedirs(D, exist_ok=True)
        n = int(dur * FPS)
        for i in range(n):
            pg.evaluate(f'frame({i / FPS})'); pg.screenshot(path=f'{D}/{i:05d}.png')
            if i % 50 == 0: print(f'{i}/{n}', flush=True)
        b.close()
        cmd = ['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{D}/%05d.png']
        if len(sys.argv) > 5: cmd += ['-i', sys.argv[5], '-c:a', 'aac', '-b:a', '192k', '-shortest']
        cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]
        subprocess.run(cmd, check=True); shutil.rmtree(D); print('ok', out)
