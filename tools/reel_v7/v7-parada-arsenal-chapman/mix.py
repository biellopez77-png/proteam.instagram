"""Mezcla v7 · La parada se llama Arsenal (Chapman) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», una sola pista, primeros 29 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-red-valvano-1983/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.3; DUR = OUT + 5.61   # la voz acaba en 22,98 s; a 23,3 empieza el fundido de 0,6 s al cierre
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
put(mus, ld('mus.mp3'), 0.0, 1.0, dur=OUT + 1.6, fi=.3, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(44)) / .25, 0, 1) * np.clip((T(47) + .2 - tt) / .3, 0, 1)   # «La lección...»: casi solo música
env *= 1 + .3 * np.clip((tt - T(54)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)    # sube 1 s en «campo» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); TR = pk(ld('train.mp3'))
LE = pk(ld('letter.mp3')); FL = pk(ld('flip.mp3')); ST = pk(ld('stamp.mp3')); MT = pk(ld('metal.mp3'))
for f in [1.9, 5.6, 9.25, 10.95, 12.7, 16.8, 19.2]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .09)                                   # ficha de Chapman
put(sfx, MK, T(7) - .05, .06, dur=.6, fi=.05, fo=.25)    # rotulador: estadio
put(sfx, MK, T(10) - .05, .06, off=1.0, dur=.8, fi=.05, fo=.3)   # rotulador: círculo del metro
put(sfx, TR, T(13) - .4, .07, off=8, dur=2.6, fi=.5, fo=1.0)     # metro lejano
put(sfx, SL, T(13) - .2, .1)                             # foto de los azulejos
put(sfx, SL, T(15) - .6, .07)                            # ficha de Chapman, más cerca
put(sfx, SL, T(16) - .1, .06)                            # bocadillo
put(sfx, MK, T(25), .08, off=2.0, dur=.5, fi=.03, fo=.2) # tacha GILLESPIE ROAD
put(sfx, MK, T(27) - .1, .07, off=3.0, dur=.6, fi=.05, fo=.25)   # escribe ARSENAL
for i in range(6): put(sfx, LE, T(28) - .15 + i * .2 + .4, .09 - .006 * i)   # cartas que caen
for i in range(5): put(sfx, FL, T(29) + i * .16, .05)    # hojas de calendario
put(sfx, ST, T(34) - .05, .11)                           # billete sellado
put(sfx, SL, T(35) - .15, .08)                           # mapa
put(sfx, MT, T(37) - .05, .07, dur=1.2, fo=.5)           # cartel del andén
put(sfx, SL, T(38) - .55, .09)                           # foto del andén (2017)
put(sfx, TR, T(38) - .5, .045, off=15, dur=2.4, fi=.6, fo=1.0)   # eco de andén, muy bajo
put(sfx, SL, T(41) - .15, .07)                           # la entrada hoy
put(sfx, MK, T(49), .05, off=4.0, dur=1.5, fi=.1, fo=.5) # línea de puntos hasta el estadio
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
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
