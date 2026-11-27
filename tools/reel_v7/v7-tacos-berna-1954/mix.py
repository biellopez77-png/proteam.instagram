"""Mezcla v7 · Los tacos de Berna (final del Mundial 1954) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Orchestra, Epic, Dreamy, Suspense», una sola pista de 32,7 s, sin empalmes; distinta a las de los v7 anteriores)
+ SFX reales bajos + lluvia suave + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-tres-filas-summitt/mix.py.
La voz se abre en cinco silencios para que quepan los viajes de cámara: 0,4 s en 2,42 («perder... En»), 0,4 s en 6,76 («tres... En la final»),
0,5 s en 8,85 («llovió... Fritz»), 0,4 s en 13,11 («campo... Y sus botas») y 0,5 s en 17,61 («largos... Alemania»); words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.1; DUR = OUT + 5.61   # la voz acaba en 24,9 s; a 25,1 empieza el fundido de 0,6 s al cierre
CUTS = [(2.42, .4), (6.76, .4), (8.85, .5), (13.11, .4), (17.61, .5)]
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
def on(x):   # quita el silencio inicial: el golpe cae justo en su tiempo
    i = int(np.argmax(np.abs(x).max(1) > .08 * np.abs(x).max())); return x[max(0, i - 240):]
put(mus, ld('mus.mp3'), 0.0, 1.0, fi=.3, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(51) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); PG = pk(on(ld('page.mp3'))); FL = pk(on(ld('flip.mp3'))); CP = pk(on(ld('chip.mp3')))
SH = pk(on(ld('shutter.mp3'))); MK = pk(on(ld('marker.mp3'))); MD = pk(on(ld('mud.mp3'))); RT = pk(on(ld('ratchet.mp3'))); WR = pk(on(ld('wrench.mp3')))
RA = pk(ld('rain.mp3')[int(10 * SR):int(40 * SR)])
for f in (2.2, 6.92, 9.46, 14.18, 19.14): put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06); put(sfx, SL, .2, .04)                       # los húngaros recortados y su ficha
for k in range(4): put(sfx, PG, T(2) + (E(3) + .1 - T(2)) * k / 4, .05, dur=.5, fo=.15)   # el calendario pasa cuatro hojas
put(sfx, SL, T(4) - .1, .03)                                         # «0 derrotas»
put(sfx, SL, 2.9, .04)                                               # marcador
put(sfx, FL, T(15) - .12, .08, dur=.5, fo=.15); put(sfx, FL, T(16) + .05, .08, dur=.5, fo=.15)   # tablillas 8 y 3
for i in range(8): put(sfx, CP, T(15) - .05 + i * .04 + .2, .03, dur=.35, fo=.1)   # ocho fichas
for i in range(3): put(sfx, CP, T(16) + .12 + i * .07 + .2, .035, dur=.35, fo=.1)  # tres fichas
put(sfx, SH, 7.3, .07, dur=1.0, fo=.3)                               # el reloj de la final en polaroid
r0, r1 = T(22) - .2, T(51) + .9                                      # lluvia: entra en «llovió» y se apaga en el remate
rv = np.interp(tt, [r0, T(22) + .4, E(22) + .5, 10.4, 19.14, 20.0, T(51) - .1, r1], [0, 1, 1, .45, .45, .75, .75, 0], left=0, right=0)
rain = np.zeros((N, 2)); put(rain, RA, 0.0, .09, dur=DUR); sfx += rain * rv[:, None]
put(sfx, SL, 9.9, .05)                                               # jugada de la final
put(sfx, MK, T(23) + .05, .06, dur=.9, fo=.25)                       # círculo sobre Walter
put(sfx, SL, T(25), .035); put(sfx, SL, T(27) - .4, .03)             # ficha y barras
put(sfx, MD, T(30), .09)                                             # «peor»: pisada en barro
put(sfx, SL, 14.6, .04); put(sfx, MK, 14.7, .04, dur=1.0, fo=.3)     # la suela se dibuja
for i in range(6): put(sfx, RT, T(38) + i * .13, .05, dur=.22, fo=.08)   # seis tacos de rosca
for i in range(6): put(sfx, RT, T(42) + i * .09, .035, dur=.18, fo=.06)  # salen los cortos
put(sfx, WR, T(42) - .05, .05, dur=.8, fo=.3)                        # herramienta
for i in range(6): put(sfx, RT, T(45) + i * .08, .05, dur=.22, fo=.08)   # entran los largos
put(sfx, SL, 19.6, .04)                                              # el marcador vuelve
put(sfx, FL, T(49) - .1, .08, dur=.5, fo=.15); put(sfx, FL, T(50) - .02, .08, dur=.5, fo=.15)   # 3 y 2
put(sfx, SL, T(51) + .1, .04); put(sfx, MK, T(55) - .1, .05, dur=.6, fo=.2)   # bota, campo y flecha
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
