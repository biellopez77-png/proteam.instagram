"""Mezcla v7 · Siete segundos (Mike D'Antoni, Phoenix Suns 2004-05) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01», encadenada consigo misma con fundidos de 1,4 s; distinta de la del último v7)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-techo-forest-clough/mix.py.
La voz acaba en 23,86 s; remate quieto hasta 24,7 s; fundido de 0,5 s; outro2 (4 s, con su voz) desde 24,7 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.7; DUR = OUT + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vn', '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: la misma pista tres veces, fundidos de 1,4 s (misma tonalidad)
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
for i in range(3):
    put(mus, M, at, 1.0, fi=(.3 if i == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .15 * np.clip((tt - 19.0) / .4, 0, 1) * np.clip((20.9 - tt) / .4, 0, 1)            # baja un poco en «Ni ellos se lo esperaban»
env *= 1 + .3 * np.clip((tt - 20.9) / .5, 0, 1) * np.clip((21.9 - tt) / .5, 0, 1)             # sube 1 s con el «7»
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); ST = pk(ld('stamp.mp3'))
TO = pk(ld('token.mp3')); TI = pk(ld('tick.mp3')); PA = pk(ld('pass.mp3')); NE = pk(ld('net.mp3')); SQ = pk(ld('squeak.mp3'))
for f in [3.52, 7.2, 13.47, 16.25, 18.5, 20.32]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
for i in range(4): put(sfx, TI, T(7) - .05 + i * .2, .07, off=.95, dur=.25, fo=.1)               # el reloj baja de 24 a 17
put(sfx, SL, 4.3, .07)                                   # tabla 2003-04
put(sfx, TO, T(16) - .05, .06, off=.1, dur=1.0, fo=.3)  # 29 fichas
put(sfx, SL, T(18) - .15, .1)                            # hoja del calendario
put(sfx, SH, T(21) - .25, .09, dur=1.0, fo=.3)           # foto de D'Antoni
put(sfx, SL, T(22) - .05, .05)                           # ficha de prensa
put(sfx, MK, T(26), .04, dur=1.2, fi=.05, fo=.3)         # pizarra: las X corren, las O atacan
put(sfx, MK, T(30), .06, off=3.0, dur=.5, fi=.02, fo=.2) # flecha a canasta
put(sfx, SQ, T(33) - .1, .05, off=4.35, dur=.6, fi=.03, fo=.25)   # Nash corre: un chirrido
for x in [T(36), T(37), T(38), T(38) + .32]: put(sfx, PA, x + .05, .08, dur=.5, fo=.2)   # tres pases y tiro
put(sfx, NE, T(38) + .6, .09, dur=1.5, fo=.5)            # red
put(sfx, TO, T(40) - .05, .06, off=.1, dur=1.0, fo=.3)   # 62 fichas
put(sfx, ST, E(42) - .1, .12, off=.75, dur=.6, fo=.2)    # sello
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT)      # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(OUT * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(OUT * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
