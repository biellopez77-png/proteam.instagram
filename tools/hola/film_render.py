"""Película horizontal «ProTeam» (1920x1080, 30 fps) sincronizada con los golpes de la música.
  python3 tools/hola/film_render.py salida.mp4 musica.wav beats.json
  python3 tools/hola/film_render.py --still beats.json t1 out1.jpg [t2 out2.jpg ...]"""
import json, os, subprocess, sys
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); a = sys.argv[1:]
still = a[0] == '--still'
beats = json.load(open(a[1] if still else a[2]))['beats']
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    pg.add_init_script(f'window.BEATS={json.dumps(beats)};')
    pg.goto('file://' + os.path.join(D, 'film.html'))
    imgs = sorted(f[:-4] for f in os.listdir(os.path.join(D, '..', 'app')) if f.endswith('.jpg'))
    pg.evaluate('(l)=>Promise.all(l.map(n=>new Promise(r=>{const i=new Image();i.onload=i.onerror=r;i.src="../app/"+n+".jpg"})))', imgs)
    pg.evaluate('document.fonts.ready.then(()=>1)')
    if still:
        for i in range(2, len(a), 2):
            pg.evaluate(f'render({float(a[i])})'); pg.wait_for_timeout(80); pg.screenshot(path=a[i + 1], type='jpeg', quality=88)
    else:
        out, audio = a[0], a[1]; fps = 30; n = int(pg.evaluate('DUR') * fps)
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-', '-i', audio,
                               '-c:a', 'aac', '-b:a', '256k', '-shortest', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f'render({i / fps})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
            if i % 300 == 0: print(f'{i}/{n}', file=sys.stderr)
        ff.stdin.close(); ff.wait()
    b.close()
