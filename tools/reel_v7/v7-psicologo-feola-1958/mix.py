"""Mezcla v7 · El informe que decía que Pelé no jugara (Feola, Suecia 1958) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», encadenada consigo misma con fundidos de 1,4 s; distinta a la del último v7)
+ SFX reales bajos + voz (ElevenLabs eleven_v4, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-cena-popovich-2013/mix.py.
La voz se abre en seis silencios para que quepan los viajes de cámara de 0,9 s (ver CUTS); words.json ya lleva esos desplazamientos.
La voz acaba en 28,79 s; remate quieto hasta 29,85; fundido a negro de 0,5 s; outro2 (4 s, con su voz) desde 30,35.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 29.85; OUT2 = OUT + .5; DUR = OUT2 + 4.0
CUTS = [(3.4, .2), (8.45, .55), (13.2, .4), (19.5, .45), (20.7, .6), (22.5, .45)]
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
FLY = [E(9), E(17), E(26), E(41), E(44), E(48)]
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
M = ld('mus.mp3'); LM = len(M) / SR   # 13,9 s
at = 0.0; k = 0
while at < DUR:
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(58) - .3)) / .4, 0, 1) * np.clip((OUT + .4 - tt) / .8, 0, 1)   # sube en el remate y baja en el fundido
env *= 1 - .45 * np.clip((tt - OUT) / 1.0, 0, 1)   # bajo el cierre la música sigue, más baja
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
PE = pk(on(ld('pencil.mp3'))); TY = pk(on(ld('type.mp3'))); MK = pk(on(ld('marker.mp3'))); CR = pk(ld('crowd.mp3')); CK = pk(on(ld('clock.mp3')))
for f in FLY: put(sfx, WH, f - .2, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SH, 0.05, .05, dur=.5, fo=.2)                          # Pelé en ficha (primer fotograma)
put(sfx, SH, FLY[0] + .55, .06, dur=.5, fo=.2)                  # polaroid de Feola
put(sfx, SL, T(11) + .2, .07)                                   # carpeta
put(sfx, SL, T(13) + .15, .06)                                  # fichas en abanico
for j in range(3): put(sfx, PE, T(14) + .1 + j * .2, .05, dur=.4, fo=.1)   # tics de lápiz
put(sfx, SL, T(15), .05)                                        # fichas de la plantilla
put(sfx, SL, T(19) - .1, .08)                                   # cae el informe
put(sfx, TY, T(22) - .25, .06, dur=.25, fo=.08); put(sfx, TY, T(22) - .05, .05, dur=.25, fo=.08)   # máquina de escribir, dos teclas
put(sfx, ST, E(22) - .1, .14, dur=.6, fo=.2)                    # sello NO JUEGA (Pelé)
put(sfx, SH, T(23) - .25, .05, dur=.5, fo=.2)                   # Garrincha en ficha
put(sfx, ST, T(26) + .05, .09, dur=.6, fo=.2)                   # segundo sello, más bajo
put(sfx, SH, FLY[2] + .5, .05, dur=.5, fo=.2)                   # Feola en ficha
put(sfx, MK, T(32) - .1, .05, dur=.6, fo=.2)                    # rotulador en el bocadillo
put(sfx, MK, T(43) - .1, .07, dur=.5, fo=.2); put(sfx, MK, T(43) + .1, .06, dur=.5, fo=.2)   # los sellos se tachan
put(sfx, SL, FLY[4] + .5, .07)                                  # portada de revista
put(sfx, CR, T(48) - .3, .035, dur=1.4, fi=.3, fo=.6)           # grada muy baja
put(sfx, CK, T(53), .07, dur=.35, fo=.15)                       # tic de reloj
put(sfx, SL, T(54) - .15, .06)                                  # calendario
for j in range(5): put(sfx, PE, T(56) + j * .18, .035, dur=.3, fo=.1)   # casillas que se marcan
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT2)      # audio de outro2.mp4 («Dale like y síguenos…»)
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
