"""Mezcla v7 · Después de perder, primero el equipo (Popovich, 2013) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Calm, Piano 02», encadenada consigo misma con fundidos de 1,4 s; distinta a la de los últimos v7)
+ SFX reales bajos + voz (ElevenLabs eleven_v4, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-derrota-dream-team-1992/mix.py.
La voz se abre en cuatro silencios para que quepan los viajes de cámara: 11,12 (+0,58), 14,84 (+0,58), 19,15 (+0,58) y 21,54 (+0,25, la pausa del remate);
words.json ya lleva esos desplazamientos. La voz acaba en 26,24 s; remate quieto hasta 27,3; fundido a negro de 0,5 s; outro2 (4 s, con su voz) desde 27,8.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 27.3; OUT2 = OUT + .5; DUR = OUT2 + 4.0
CUTS = [(11.12, .58), (14.84, .58), (19.15, .58), (21.54, .25)]
FLY = [5.1, 10.98, 15.27, 20.12, 23.06]   # el último es el alejamiento a toda la pared (1,6 s)
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
M = ld('mus.mp3'); LM = len(M) / SR   # 12,1 s
at = 0.0; k = 0
while at < DUR:
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(57) - .3)) / .4, 0, 1) * np.clip((OUT + .4 - tt) / .8, 0, 1)   # sube en el remate y baja en el fundido
env *= 1 - .45 * np.clip((tt - OUT) / 1.0, 0, 1)   # bajo el cierre la música sigue, más baja
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
SW = pk(on(ld('swish.mp3'))); PL = pk(on(ld('plate.mp3'))); FS = pk(on(ld('steps.mp3'))); AP = pk(ld('applause.mp3'))
for f in FLY[:-1]: put(sfx, WH, f - .2, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, FLY[-1] - .1, .05, dur=1.9, fi=.3, fo=.6)            # alejamiento a toda la pared, más largo y suave
put(sfx, ST, T(5) + .05, .14, dur=.6, fo=.2)                    # «perdieron»: sello PERDIDO
put(sfx, SH, T(9) - .35, .06, dur=.5, fo=.2)                    # Popovich en ficha (obturador)
put(sfx, PL, T(14), .08, dur=1.2, fo=.3)                        # «cenar»: plato
put(sfx, SL, FLY[0] + .55, .08)                                 # cae la hoja del calendario
put(sfx, SW, T(22) + .45, .10, dur=1.6, fo=.4)                  # triple: red
put(sfx, SH, FLY[1] + .5, .06, dur=.5, fo=.2)                   # Popovich en la banda
put(sfx, SL, T(40) - .1, .06)                                   # la tarjeta «celebración» gira
for i in range(0, 12, 3): put(sfx, PL, T(41) + i * .07, .05, dur=.6, fo=.2)   # platos que se apoyan
put(sfx, FS, T(45) - .1, .06, dur=2.0, fi=.1, fo=.5)            # pasos al entrar por la puerta
put(sfx, SH, T(48) - .2, .05, dur=.5, fo=.2)                    # banquillo de los Spurs
put(sfx, SL, FLY[3] + .55, .07)                                 # hoja de 2014
put(sfx, AP, T(55) - .3, .05, dur=2.6, fi=.4, fo=1.2)           # aplauso lejano en «campeones»
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT2)      # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .84)   # true peak ≤ −1 dBTP
fo = int((DUR - .5) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
