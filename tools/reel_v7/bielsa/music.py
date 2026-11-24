"""Pista original sintetizada (sin licencias de terceros) + SFX + mezcla con la voz.
python3 music.py voice.wav out.wav  → 17.4 s de reel + cola de 5.6 s para el outro."""
import sys, numpy as np, wave
from scipy.signal import butter, sosfilt, fftconvolve
SR = 48000; BPM = 120; B = 60 / BPM; DUR = 17.05 + 5.61
N = int(DUR * SR); t = np.arange(N) / SR
rng = np.random.default_rng(7)
FLY = [1.6, 4.18, 7.18, 9.32, 11.92, 13.86]; LOCO = 13.28
def rd(p):
    w = wave.open(p); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    if w.getnchannels() == 2: a = a.reshape(-1, 2).mean(1)
    assert w.getframerate() == SR, w.getframerate(); return a
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], 'band', fs=SR, output='sos'), x)
def add(buf, x, at, g=1.0):
    i = int(at * SR); j = min(len(buf), i + len(x))
    if i < len(buf): buf[i:j] += g * x[:j - i]
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
# --- sonidos
def kick():
    n = int(.45 * SR); tt = np.arange(n) / SR; f = 45 + 110 * np.exp(-tt * 28)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 7)
    x += .25 * lp(rng.standard_normal(n), 3000) * np.exp(-tt * 120); return np.tanh(1.6 * x)
def clap():
    n = int(.35 * SR); tt = np.arange(n) / SR; e = np.zeros(n)
    for d in (0, .011, .022): e += np.exp(-np.clip(tt - d, 0, None) * 60) * (tt >= d)
    e += .5 * np.exp(-tt * 12); return bp(rng.standard_normal(n), 900, 5000) * e * .7
def hat(op=False):
    n = int((.25 if op else .06) * SR); tt = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000, 4) * np.exp(-tt * (14 if op else 70)) * .35
def saw(f, n, det=(0, -.08, .07)):
    tt = np.arange(n) / SR; return sum(2 * ((f * 2 ** (d / 12) * tt + rng.random()) % 1) - 1 for d in det) / len(det)
def pluck(m, dur=.5):
    n = int(dur * SR); tt = np.arange(n) / SR; x = saw(hz(m), n)
    env = np.exp(-tt * 9); out = np.zeros(n); fc = 400 + 4200 * np.exp(-tt * 14)
    # filtro de barrido aproximado por bloques
    for k in range(0, n, 512):
        seg = x[max(0, k - 512):k + 512]; y = lp(seg, max(200, fc[k]))
        out[k:k + 512] = y[-len(out[k:k + 512]):] if k else y[:512]
    return out * env * .5
def pad(ms, dur):
    n = int(dur * SR); tt = np.arange(n) / SR
    x = sum(saw(hz(m), n, (0, -.12, .11, .05)) for m in ms) / len(ms)
    a = np.minimum(1, tt / .35) * np.minimum(1, (dur - tt) / .4)
    return lp(x, 1400) * a * .35
def sub(m, dur):
    n = int(dur * SR); tt = np.arange(n) / SR
    return np.tanh(1.3 * np.sin(2 * np.pi * hz(m) * tt)) * np.minimum(1, tt / .01) * np.exp(-tt * 1.2) * .55
def riser(dur):
    n = int(dur * SR); tt = np.arange(n) / SR; x = rng.standard_normal(n); out = np.zeros(n)
    for k in range(0, n, 1024):
        f = 300 + 7000 * (k / n) ** 2; out[k:k + 1024] = bp(x[k:k + 1024], f * .7, min(f * 1.4, 18000))
    return out * (tt / dur) ** 2 * .35
def whoosh(dur=.55):
    n = int(dur * SR); tt = np.arange(n) / SR; x = rng.standard_normal(n); out = np.zeros(n)
    for k in range(0, n, 512):
        p = k / n; f = 400 + 3000 * np.sin(np.pi * p); out[k:k + 512] = bp(x[k:k + 512], f * .6, f * 1.6)
    return out * np.sin(np.pi * tt / dur) ** 2 * .45
def impact():
    n = int(1.6 * SR); tt = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(30 + 60 * np.exp(-tt * 9)) / SR) * np.exp(-tt * 3)
    x += .35 * lp(rng.standard_normal(n), 1500) * np.exp(-tt * 10); return np.tanh(1.4 * x) * .8
def tick(f=2400):
    n = int(.03 * SR); tt = np.arange(n) / SR; return np.sin(2 * np.pi * f * tt) * np.exp(-tt * 220) * .25
def thud():
    n = int(.6 * SR); tt = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(70 + 120 * np.exp(-tt * 40)) / SR) * np.exp(-tt * 12)
    x += .6 * bp(rng.standard_normal(n), 200, 2500) * np.exp(-tt * 35); return np.tanh(2 * x) * .9
# --- arreglo
drums = np.zeros(N); bass = np.zeros(N); harm = np.zeros(N); fx = np.zeros(N)
PROG = [(57, [69, 72, 76]), (53, [65, 69, 72]), (48, [67, 72, 76]), (55, [67, 71, 74])]  # Am F C G
END = 17.4
def section(t): return 'intro' if t < 1.6 else 'break' if 9.32 <= t < 11.92 else 'out' if t >= 16.6 else 'full'
K, C = kick(), clap()
beat = 0.0; i = 0
while beat < END + 2:
    s = section(beat)
    if s == 'full' or (s == 'out' and beat < 17.4):
        add(drums, K, beat, .9)
        if i % 4 in (1, 3): add(drums, C, beat, .55)
    if s in ('full', 'intro', 'break'):
        for k in range(4):
            sw = .03 if k % 2 else 0; add(drums, hat(k == 2 and s == 'full'), beat + k * B / 4 + sw, (.5 if k % 2 else .8) * (.5 if s != 'full' else 1))
    beat += B; i += 1
bar = 0
while bar * 4 * B < DUR:
    t0 = bar * 4 * B; root, ch = PROG[bar % 4]; s = section(t0)
    add(harm, pad(ch, 4 * B + .3), t0, .55 if s == 'break' else .35)
    if s != 'intro' and t0 < END:
        for k, off in enumerate([0, .75, 1.5, 2.0, 2.75, 3.5]):
            add(bass, sub(root - 12, .45), t0 + off * B, .9 if s == 'full' else .4)
    arp = [ch[0], ch[1], ch[2], ch[1] + 12, ch[2], ch[1]]
    if t0 < END + 4:
        for k in range(8):
            add(harm, pluck(arp[k % 6] + (12 if s == 'break' else 0)), t0 + k * B / 2, .3 if s != 'intro' else .2)
    bar += 1
# filtro de intro: abre de 400 Hz a pleno en 1.6 s
cut = int(1.6 * SR); m = harm[:cut].copy(); harm[:cut] = 0
for k in range(0, cut, 2048):
    f = 350 + 6000 * (k / cut) ** 2; seg = lp(m[k:k + 2048], f); harm[k:k + len(seg)] = seg
# FX: riser antes de cada viaje, whoosh en el viaje, impacto en la llegada
for f in FLY:
    add(fx, riser(.9), f - .9 + .28, .6); add(fx, whoosh(.6), f, .9)
for f in (1.6, 4.18, 11.92, 13.86): add(fx, impact(), f + .28, .7)
add(fx, thud(), LOCO, 1.1)
W = [float(l.split(',')[1]) for l in open('words.js').read().split('[')[2:] if ',' in l] if False else []
for k in range(51): add(fx, tick(2400 + 20 * k), 4.47 + k * (1.0 / 51) * (1.15), .7)  # contador 01→51
for k in range(8): add(fx, tick(1800), 6.33 + k * .1, .5)  # pasada del escáner
for k in range(4): add(fx, tick(1200), 7.46 + k * .16, .8)  # reloj
# reverb
ir_n = int(2.2 * SR); ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 3.2); ir = lp(ir, 6000); ir /= np.abs(ir).sum() ** .5 * 6
music = drums * .9 + bass + harm + .35 * fftconvolve(harm + .3 * C.sum() * 0 + .4 * drums * 0, ir)[:N] + .25 * fftconvolve(fx, ir)[:N]
fx_dry = fx
# voz y sidechain
v = rd(sys.argv[1]); voice = np.zeros(N); voice[:min(N, len(v))] = v[:N]
env = np.convolve(np.abs(voice), np.ones(int(.05 * SR)) / int(.05 * SR), 'same'); env = np.minimum(1, env / (env.max() * .25))
env = np.maximum.accumulate(env[::-1])[::-1] * 0 + env
duck = 1 - .45 * lp(env, 8)
# cola: la música baja bajo el outro (que trae su propia voz)
tail = np.ones(N); a = int(17.0 * SR); tail[a:] = np.maximum(.35, 1 - (t[a:] - 17.0) / .8 * .65)
fo = int((DUR - 1.2) * SR); tail[fo:] *= np.linspace(1, 0, N - fo)
tl_ = np.zeros(N); add(tl_, rd('/tmp/tail.wav'), 17.35)
voice = voice + tl_
env2 = np.convolve(np.abs(voice), np.ones(2400)/2400, 'same'); env2 = np.minimum(1, env2/(env2.max()*.25)); duck = 1 - .45*lp(env2, 8)
mix = music * duck * tail * .17 + fx_dry * .32 + voice * 1.0
R=lambda x:round(20*np.log10(np.sqrt((x[:int(17*SR)]**2).mean())+1e-12),1); print("bed",R(music*duck*tail*.17),"fx",R(fx_dry*.32),"voz",R(voice))
mix = np.tanh(mix * 1.1) / np.tanh(1.1); mix /= np.abs(mix).max() / .92
out = np.stack([mix, mix], 1)
w = wave.open(sys.argv[2], 'w'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close(); print('ok', DUR)
