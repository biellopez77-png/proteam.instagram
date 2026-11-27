"""Mezcla v7 · Cuatro minutos sin tirar (Milan, Indiana, 1954) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», una sola pista sin cortes; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-general-michels/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.4; DUR = OUT + 5.6   # la voz acaba en 24,26 s; a 24,4 empieza el fundido de 0,6 s al cierre
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
put(mus, ld('mus.mp3'), 0.0, 1.0, off=2.0, fi=.8)  # la pista empieza a sonar a los 2 s
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(50) - .3)) / .4, 0, 1) * np.clip((OUT + 1.0 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); ST = pk(ld('stamp.mp3')); TK = pk(ld('tokens.mp3')); TH = pk(ld('thud.mp3'))
CL = pk(ld('click.mp3')); BO = pk(ld('bounce.mp3')); NE = pk(ld('net.mp3')); CR = pk(ld('crowd.mp3')); TI = pk(ld('tick.mp3'))
for f in [2.15, 9.6, 13.3, 17.85, 21.35]: put(sfx, WH, f - .2, .08, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06)                                   # ficha de Milan (hoy)
put(sfx, SL, T(0) + .15, .04)                            # rótulo MILAN · INDIANA
put(sfx, ST, T(1) + .02, .12)                            # sello «1954»
put(sfx, TK, T(5) + .1, .07, dur=1.2, fo=.3)             # 161 puntos que se rellenan
put(sfx, TI, T(5), .05, dur=1.0, fi=.05, fo=.3)          # tic suave del contador
put(sfx, TH, T(13) + .38, .12)                           # el bloque ×10 cae de golpe
put(sfx, CL, T(21) + .1, .10, dur=.5, fo=.1)             # se enciende «4.º CUARTO»
put(sfx, SL, T(23) - .45, .05)                           # foto de Plump
put(sfx, BO, T(25) + .23, .10, dur=.6, fo=.3)            # un solo bote del balón, y silencio
put(sfx, TI, T(34), .07, dur=1.9, fi=.2, fo=.5)          # el cronómetro del balón retenido
put(sfx, CR, T(38) - .2, .08, off=5.0, dur=2.3, fi=.4, fo=.9)   # público lejano, muy bajo
put(sfx, NE, T(46) + .78, .12, dur=1.6, fo=.5)           # red
put(sfx, CL, T(47), .09, dur=.5, fo=.1)                  # 32
put(sfx, SL, T(47) + .2, .05)                            # postal del equipo campeón
put(sfx, CL, T(49), .08, dur=.5, fo=.1)                  # 30
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
