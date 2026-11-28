"""Mezcla v7 · La comba de Mikan (Ray Meyer y George Mikan, DePaul, 1942) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», encadenada consigo misma con fundidos de 1,4 s;
distinta de la del último v7, que usó la «Logo 03») + SFX reales bajos + voz (ElevenLabs, Mateo). Base: v7-salto-inicial-mcguire-1957/mix.py.
La voz acaba en 24,24 s; remate quieto; fundido a negro 25,3–25,8 s; outro2 (4 s, con su voz) desde 25,8 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.8; DUR = OUT + 4.0
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
env *= 1 + .3 * np.clip((tt - 23.3) / .5, 0, 1) * np.clip((24.9 - tt) / .5, 0, 1)             # sube 1 s con el remate
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
BO = pk(ld('bounce.mp3')); CH = pk(ld('chip.mp3')); RO = pk(ld('rope.mp3')); SW = pk(ld('swish.mp3')); ST = pk(ld('steps.mp3'))
for f in [6.25, 9.0, 11.55, 16.85, 18.55, 21.1]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, BO, .55 - .02, .10, off=2.48, dur=.9, fo=.4)            # «torpe»: el balón se le escapa y bota
put(sfx, MK, T(2), .04, off=.05, dur=1.2, fi=.05, fo=.3)         # la regla sube
put(sfx, MK, T(9) - .05, .05, off=.75, dur=.6, fi=.03, fo=.2)    # las gafas se dibujan
for x in [5.725, 6.175, 6.625]: put(sfx, RO, x - .05, .12, off=.40, dur=.3, fo=.12)   # la comba golpea el suelo, tres veces
put(sfx, SH, 7.0, .07, off=1.55, dur=.5, fo=.2)                  # foto de DePaul
put(sfx, SL, T(21) + .1 - .3, .06)                               # rótulo DePaul · Chicago
put(sfx, SH, 9.75, .07, off=1.55, dur=.5, fo=.2)                 # foto de Meyer
put(sfx, SL, T(23) - .3, .05)                                    # ficha de Meyer
for i, o in enumerate([5.5, 9.45, 5.5]): put(sfx, ST, T(27) + i * .16 - .1, .05, off=o, dur=.4, fi=.02, fo=.15)   # pasos de baile, muy bajos
put(sfx, SL, 12.3, .05)                                          # el aro
for k in [34, 35, 36, 37]: put(sfx, SW, T(k) + .25, .10, off=.02, dur=1.0, fo=.4)   # red: uno por palabra
put(sfx, SH, 17.3, .08, off=1.55, dur=.5, fo=.2)                 # foto de Mikan
put(sfx, SL, T(41) - .3, .05)                                    # ficha de Mikan
put(sfx, SL, 18.95, .05)                                         # foto de los Lakers
for i in range(7): put(sfx, CH, T(43) + i * .12 + .23 - .68, .06, off=0, dur=.95, fo=.2)   # siete fichas sobre la mesa
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
