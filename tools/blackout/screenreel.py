"""Reels de «una pantalla que se transforma» sobre negro (screen.html) con efecto de tubo solo en el modo antiguo.
  python3 screenreel.py still spec.json t1 t2 ... prefijo
  python3 screenreel.py video spec.json out.mp4"""
import sys, io, json, os, subprocess, tempfile, numpy as np, soundfile as sf
from PIL import Image
from playwright.sync_api import sync_playwright
from photo import serve
from crt import crt
W, H, FPS, SR = 1080, 1920, 30, 44100
MUS = '/home/claude/tannerhelland/free-music/mp3/'

def frame(pg, spec, t, i):
    r = pg.evaluate('([s, t]) => window.frame(s, t)', [spec, t])
    img = Image.open(io.BytesIO(pg.screenshot())).convert('RGB')
    return np.asarray(crt(img, r['crt'], t, i, curve=r['curve'] / max(r['crt'], 1e-3) if r['crt'] > 0 else 0)) if r['crt'] > .01 else np.asarray(img)

def load(name, start, dur):
    p = tempfile.mktemp(suffix='.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(start), '-t', str(dur), '-i', MUS + name, '-ac', '1', '-ar', str(SR), p], check=True)
    a, _ = sf.read(p); os.remove(p); return a
def vinyl_stop(a, L=.7):
    n = int(L * SR); seg = a[-n:]; idx = np.cumsum(np.linspace(1, 0, n)); idx = idx[idx < len(seg)]
    return np.concatenate([a[:-n], np.interp(idx, np.arange(len(seg)), seg) * np.linspace(1, .2, len(idx))])

def audio(spec, out):
    dur = spec['dur']; n = int(dur * SR); A = spec['audio']; rng = np.random.default_rng(3)
    mus = np.zeros(n); sfx = np.zeros(n); voz = np.zeros(n); cut = A['cut']
    if A.get('old'):
        old = load(A['old'][0], A['old'][1], cut + .2)[:int(cut * SR)] * A.get('old_vol', .5)
        old = vinyl_stop(old); fi = int(.4 * SR); old[:fi] *= np.linspace(0, 1, fi); mus[:len(old)] += old
    # en el cambio: interferencia corta y un «whoosh» que sube
    k = int((cut - .15) * SR); L = int(.5 * SR); x = np.arange(L) / SR
    sfx[k:k + L] += (rng.normal(0, .18, L) * np.exp(-x * 6)) + np.sin(2 * np.pi * (200 + 1800 * x) * x) * .05 * np.exp(-((x - .25) / .12) ** 2)
    new_at = cut + A.get('gap', .3); new = load(A['new'][0], A['new'][1], dur - new_at) * A.get('new_vol', .6)
    fl = int(1.5 * SR); new[-fl:] *= np.linspace(1, 0, fl); fi = int(.08 * SR); new[:fi] *= np.linspace(0, 1, fi)
    k = int(new_at * SR); mus[k:k + len(new)] += new[:n - k]
    if spec.get('on'):  # encendido del tubo
        L = int(.5 * SR); x = np.arange(L) / SR; sfx[:L] += np.sin(2 * np.pi * 60 * x) * np.exp(-x * 6) * .4 + rng.normal(0, .08, L) * np.exp(-x * 10)
    for Ly in spec['layers']:  # tecleo en el modo antiguo
        if Ly['type'] != 'text' or Ly['t0'] >= cut: continue
        for ln in Ly['lines']:
            at = Ly['t0'] + ln.get('at', 0); cps = ln.get('cps', 24)
            for j, ch in enumerate(ln['text']):
                tt = at + j / cps
                if ch == ' ' or tt >= min(cut, Ly['t1']): continue
                kk = int(tt * SR); LL = int(.02 * SR)
                if kk + LL < n: sfx[kk:kk + LL] += rng.normal(0, 1, LL) * np.exp(-np.arange(LL) / (SR * .003)) * .09
    sys.path.insert(0, '/home/claude/tts'); import kok
    duck = np.ones(n)
    for at, txt in spec.get('lineas', []):
        p = tempfile.mktemp(suffix='.wav'); kok.say(txt, 29, p, spec.get('vel', 1.0)); v, sr = sf.read(p); os.remove(p)
        v = np.interp(np.arange(0, len(v), sr / SR), np.arange(len(v)), v); k = int(at * SR)
        voz[k:k + len(v)] += v[:n - k]; duck[max(0, k - int(.1 * SR)):k + len(v) + int(.1 * SR)] = .4
        print(f'{at:5.2f}-{at + len(v) / SR:5.2f} {txt}')
    duck = np.convolve(duck, np.ones(4000) / 4000, 'same')
    mix = mus * duck + sfx + (voz / max(1e-6, np.abs(voz).max()) * .85 if np.abs(voz).max() > 0 else 0)
    mix /= max(1e-6, np.abs(mix).max()) / .92
    sf.write(out, mix, SR)

if __name__ == '__main__':
    c = sys.argv[1]; spec = json.load(open(sys.argv[2])); port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H}); pg.on('pageerror', lambda e: print('ERR', e))
        pg.goto(f'http://127.0.0.1:{port}/tools/blackout/screen.html'); pg.wait_for_function('window.READY===true', timeout=60000)
        if c == 'still':
            *ts, pre = sys.argv[3:]
            for t in ts: Image.fromarray(frame(pg, spec, float(t), 0)).save(f'{pre}-{t}.jpg', quality=88)
        else:
            out = sys.argv[3]; wav = out.replace('.mp4', '.wav'); audio(spec, wav); N = int(spec['dur'] * FPS)
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '9M', '-bufsize', '18M', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(N):
                ff.stdin.write(frame(pg, spec, i / FPS, i).tobytes())
                if i % 90 == 0: print(f'{i}/{N}', flush=True)
            ff.stdin.close(); ff.wait(); print('ok', out)
        b.close()
