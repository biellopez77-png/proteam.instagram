"""Reels de «una sola tele»: la tele 3D fija, lo que emite se escribe dentro, y en el corte la cámara entra en la pantalla.
  python3 tvreel.py still spec.json t1 t2 ... prefijo
  python3 tvreel.py video spec.json out.mp4
spec: {d, ch, dur, tv:{frames:[...]}, future:{scenes:[...]}, seg:[[tipo, t0, t1], ...], audio:{...}, lineas:[[t, texto]]}
  tipos: tv (tele, zoom lento) · in (entra en la pantalla) · fut (ProTeam a pantalla completa) · out (sale a la tele)"""
import sys, io, json, os, subprocess, tempfile, numpy as np, cv2, soundfile as sf
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
from crt import crt
D = os.path.dirname(os.path.abspath(__file__)); W, H, FPS = 1080, 1920, 30
PLATE = np.asarray(Image.open(f'{D}/out/tv/tv-plate.png').convert('RGB')).astype(np.float32) / 255
MASK = cv2.imread(f'{D}/out/tv/mask.png', 0).astype(np.float32)[..., None] / 255
SC = json.load(open(f'{D}/out/tv/screen.json')); SX, SY, SW, SH = SC['x'] - 4, SC['y'] - 4, SC['w'] + 8, SC['h'] + 8
CX, CY = SX + SW / 2, SY + SH / 2

def seg_at(spec, t):
    for s in spec['seg']:
        if s[1] <= t < s[2]: return s
    return spec['seg'][-1]

def tv_frame(scr, t, seed):
    """scr: imagen 1200x900 de lo que emite la tele -> fotograma 1080x1920 con la tele."""
    s = np.asarray(crt(scr, .85, t, seed, curve=.06).resize((SW, SH), Image.BILINEAR)).astype(np.float32) / 255
    full = np.zeros_like(PLATE); full[SY:SY + SH, SX:SX + SW] = s
    out = PLATE * (1 - MASK) + (full + PLATE * .35) * MASK
    return np.clip(out, 0, 1)

def zoom(img, z, cx=CX, cy=CY):
    M = np.float32([[z, 0, W / 2 - cx * z], [0, z, H / 2 - cy * z]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

def frame(pgs, spec, t, i):
    k, t0, t1 = seg_at(spec, t); u = (t - t0) / max(1e-6, t1 - t0)
    if k in ('tv', 'in', 'out'):
        pgs['scr'].evaluate('([s, t]) => window.screen(s, t)', [spec['tv'], t])
        scr = Image.open(io.BytesIO(pgs['scr'].screenshot())).convert('RGB')
        img = tv_frame(scr, t, i)
        if k == 'tv':
            z = 1 + .05 * ((t - t0) / max(1, t1 - t0)); img = zoom(img, z, W / 2, CY)
        else:
            e = u * u * (3 - 2 * u) if k == 'in' else 1 - (u * u * (3 - 2 * u))
            z = 1 + e * 2.4; acc = np.zeros_like(img)
            for dz in (-.06, -.03, 0):  # desenfoque de movimiento
                acc += zoom(img, max(1, z + dz * e * 2.4))
            img = acc / 3; img = img * (1 - e ** 3) + e ** 3  # se funde a blanco al entrar en la pantalla
        return (img * 255).astype(np.uint8)
    pgs['fut'].evaluate(f'window.render("ep", {t})')
    img = np.asarray(Image.open(io.BytesIO(pgs['fut'].screenshot())).convert('RGB')).astype(np.float32) / 255
    a = pgs['fut'].evaluate(f'window.crtAmount("ep", {t})')
    if a > 0: img = np.asarray(crt(Image.fromarray((img * 255).astype(np.uint8)), a, t, i)).astype(np.float32) / 255
    w = max(0, 1 - (t - t0) / .18)  # destello blanco al llegar
    img = img * (1 - w) + w
    return (np.clip(img, 0, 1) * 255).astype(np.uint8)

def pages(p, port, spec):
    b = p.chromium.launch()
    scr = b.new_page(viewport={'width': 1200, 'height': 900}); scr.goto(f'http://127.0.0.1:{port}/tools/blackout/pantalla.html'); scr.wait_for_function('window.READY===true')
    fut = b.new_page(viewport={'width': W, 'height': H}); fut.goto(f'http://127.0.0.1:{port}/tools/blackout/retro.html?d={spec["d"]}'); fut.wait_for_function('window.READY===true', timeout=60000)
    fut.evaluate('(e) => { window.EP = e; }', spec['future'])
    for pg in (scr, fut): pg.on('pageerror', lambda e: print('ERR', e))
    return b, {'scr': scr, 'fut': fut}

# ── audio ─────────────────────────────────────────────
SR = 44100
MUS = '/home/claude/tannerhelland/free-music/mp3/'
def load(name, start, dur):
    p = tempfile.mktemp(suffix='.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(start), '-t', str(dur), '-i', MUS + name, '-ac', '1', '-ar', str(SR), p], check=True)
    a, _ = sf.read(p); os.remove(p); return a
def vinyl_stop(a, L=.7):
    n = int(L * SR); seg = a[-n:]; idx = np.cumsum(np.linspace(1, 0, n)); idx = idx[idx < len(seg)]
    return np.concatenate([a[:-n], np.interp(idx, np.arange(len(seg)), seg) * np.linspace(1, .2, len(idx))])
def audio(spec, out):
    dur = spec['dur']; n = int(dur * SR); A = spec['audio']; rng = np.random.default_rng(3)
    mus = np.zeros(n); sfx = np.zeros(n); voz = np.zeros(n)
    cut = A['cut']  # momento del corte (entra en la pantalla)
    old = load(A['old'][0], A['old'][1], cut + .2)[:int(cut * SR)] * A.get('old_vol', .5)
    old = vinyl_stop(old); fi = int(.3 * SR); old[:fi] *= np.linspace(0, 1, fi); mus[:len(old)] += old
    k = int((cut - .1) * SR); L = int(.35 * SR); sfx[k:k + L] += rng.normal(0, .22, L) * np.linspace(1, 0, L)
    new_at = cut + A.get('gap', .35); newd = dur - new_at
    new = load(A['new'][0], A['new'][1], newd) * A.get('new_vol', .6)
    fl = int(1.2 * SR); new[-fl:] *= np.linspace(1, 0, fl)
    k = int(new_at * SR); mus[k:k + len(new)] += new[:n - k]
    for f in spec['tv']['frames']:  # tecleo: un clic por letra
        if f.get('static'):
            k0, k1 = int(f['t0'] * SR), int(min(dur, f['t0'] + f.get('len', .5)) * SR); sfx[k0:k1] += rng.normal(0, .15, k1 - k0)
        for Ln in f.get('lines', []):
            at = f['t0'] + Ln.get('at', 0); cps = Ln.get('cps', 22)
            for j, ch in enumerate(Ln['text']):
                tt = at + j / cps
                if ch == ' ' or (cut <= tt < spec.get('back', 1e9)): continue
                kk = int(tt * SR); LL = int(.02 * SR)
                if kk + LL < n: sfx[kk:kk + LL] += rng.normal(0, 1, LL) * np.exp(-np.arange(LL) / (SR * .003)) * .1
    import sys as _s; _s.path.insert(0, '/home/claude/tts'); import kok
    duck = np.ones(n)
    for at, txt in spec.get('lineas', []):
        p = tempfile.mktemp(suffix='.wav'); kok.say(txt, 29, p, spec.get('vel', 1.0)); v, sr = sf.read(p); os.remove(p)
        v = np.interp(np.arange(0, len(v), sr / SR), np.arange(len(v)), v); k = int(at * SR)
        voz[k:k + len(v)] += v[:n - k]; duck[max(0, k - int(.1 * SR)):k + len(v) + int(.1 * SR)] = .4
        print(f'{at:5.2f}-{at + len(v) / SR:5.2f} {txt}')
    duck = np.convolve(duck, np.ones(4000) / 4000, 'same')
    mix = mus * duck + sfx + voz / max(1e-6, np.abs(voz).max()) * .85
    mix /= max(1e-6, np.abs(mix).max()) / .92
    sf.write(out, mix, SR)

if __name__ == '__main__':
    c = sys.argv[1]; spec = json.load(open(sys.argv[2])); port = serve()
    with sync_playwright() as p:
        b, pgs = pages(p, port, spec)
        if c == 'still':
            *ts, pre = sys.argv[3:]
            for t in ts: Image.fromarray(frame(pgs, spec, float(t), 0)).save(f'{pre}-{t}.jpg', quality=88)
        else:
            out = sys.argv[3]; wav = out.replace('.mp4', '.wav'); audio(spec, wav)
            N = int(spec['dur'] * FPS)
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '9M', '-bufsize', '18M', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(N):
                ff.stdin.write(frame(pgs, spec, i / FPS, i).tobytes())
                if i % 90 == 0: print(f'{i}/{N}', flush=True)
            ff.stdin.close(); ff.wait(); print('ok', out)
        b.close()
