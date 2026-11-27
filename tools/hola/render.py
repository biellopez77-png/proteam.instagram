"""Película «Hola, ProTeam» (estilo presentación de producto): HTML + Playwright + ffmpeg, sin IA.
  python3 tools/hola/render.py salida.mp4 [--audio musica.wav] [--still t salida.jpg]"""
import os, subprocess, sys
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__))
a = sys.argv[1:]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + os.path.join(D, 'hola.html'))
    imgs = sorted(f[:-4] for f in os.listdir(os.path.join(D, '..', 'app')) if f.endswith('.jpg'))
    pg.evaluate('(l)=>Promise.all(l.map(n=>new Promise(r=>{const i=new Image();i.onload=i.onerror=r;i.src="../app/"+n+".jpg"})))', imgs)
    pg.evaluate('document.fonts.ready.then(()=>1)')
    if a and a[0] == '--still':
        for i in range(1, len(a), 2):
            pg.evaluate(f'render({float(a[i])})'); pg.wait_for_timeout(60); pg.screenshot(path=a[i + 1], type='jpeg', quality=88)
    else:
        out = a[0]; audio = a[a.index('--audio') + 1] if '--audio' in a else None
        fps = 30; n = int(pg.evaluate('DUR') * fps)
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-']
        if audio: cmd += ['-i', audio, '-c:a', 'aac', '-b:a', '192k', '-shortest']
        cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]
        ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f'render({i / fps})'); ff.stdin.write(pg.screenshot(type='jpeg', quality=90))
            if i % 150 == 0: print(f'{i}/{n}', file=sys.stderr)
        ff.stdin.close(); ff.wait()
    b.close()
