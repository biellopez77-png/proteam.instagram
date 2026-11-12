"""Reel de Blackout Friday: escena 3D (studio.html) revelada como foto + subtítulos + cierre + audio.
  python3 video.py reels/r01.json reels/r01.mp4"""
import sys, json, io, subprocess, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from photo import serve, develop, FLAGS
F = '/home/claude/tts/'
def font(n, s): return ImageFont.truetype(F + n + '.ttf', s)
spec = json.load(open(sys.argv[1])); out = sys.argv[2]; W, H, FPS = 1080, 1920, 30
dur = spec['dur']; endc = spec['cierre_at']; N = int(dur * FPS)
MARK = Image.open(os.path.join(os.path.dirname(__file__), '..', 'proteam-mark.webp')).convert('RGBA').resize((64, 64))

def caption(im, txt, a):
    d = ImageDraw.Draw(im, 'RGBA'); f = font('manrope-latin-800-normal', 50)
    words = txt.split(); lines = []; cur = ''
    for w in words:
        if d.textlength((cur + ' ' + w).strip(), font=f) > 820: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    lines.append(cur); y = 1420
    for l in lines:
        x = (W - d.textlength(l, font=f)) / 2
        d.text((x + 2, y + 3), l, font=f, fill=(0, 0, 0, int(160 * a))); d.text((x, y), l, font=f, fill=(255, 255, 255, int(255 * a))); y += 64

def cierre(u):
    im = Image.new('RGB', (W, H), (6, 7, 9)); d = ImageDraw.Draw(im)
    a = min(1, u / .5)
    big = font('manrope-latin-800-normal', 96); ser = font('instrument-serif-latin-400-italic', 64); mono = font('ibm-plex-mono-latin-500-normal', 30)
    c = lambda v: tuple(int(x * a) for x in v)
    d.text((90, 700), 'Apaga el caos.', font=big, fill=c((244, 246, 250)))
    d.text((90, 810), 'Enciende tu equipo.', font=big, fill=c((120, 170, 255)))
    if u > .8:
        b = min(1, (u - .8) / .5); c2 = lambda v: tuple(int(x * b) for x in v)
        d.text((92, 980), '6 meses gratis para tu primer equipo', font=ser, fill=c2((210, 214, 222)))
        d.text((92, 1070), 'HASTA EL 27 NOV · 23:59', font=mono, fill=c2((140, 148, 162)))
    m = MARK.copy(); m.putalpha(m.getchannel('A').point(lambda v: int(v * a))); im.paste(m, (90, 1640), m)
    d.text((170, 1650), 'ProTeam', font=font('manrope-latin-800-normal', 44), fill=c((244, 246, 250)))
    d.text((W - 90 - d.textlength('pro-team.app', font=mono), 1662), 'pro-team.app', font=mono, fill=c((140, 148, 162)))
    return im

port = serve()
ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
    '-i', sys.argv[1].replace('.json', '.wav'), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(args=FLAGS); pg = b.new_page(viewport={'width': W, 'height': H})
    pg.goto(f'http://127.0.0.1:{port}/tools/blackout/studio.html?{spec["escena"]}&w={W}&h={H}&t=0'); pg.wait_for_function('window.READY===true', timeout=180000)
    for i in range(N):
        t = i / FPS
        if t < endc:
            pg.evaluate(f'window.render({t})'); im = develop(Image.open(io.BytesIO(pg.screenshot())), seed=i)
            fade = np.clip((endc - t) / .35, 0, 1)
            if fade < 1: im = Image.fromarray((np.asarray(im) * fade).astype(np.uint8))
            for t0, t1, txt in spec['subs']:
                if t0 <= t < t1: caption(im, txt, min(1, (t - t0) / .15, (t1 - t) / .15))
        else: im = cierre(t - endc)
        ff.stdin.write(im.convert('RGB').tobytes())
        if i % 60 == 0: print(f'{i}/{N}', flush=True)
    b.close()
ff.stdin.close(); ff.wait(); print('ok', out)
