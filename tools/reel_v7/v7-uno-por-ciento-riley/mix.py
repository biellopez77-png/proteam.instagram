"""Mezcla v7 · Un uno por ciento (Pat Riley, Lakers 1986-87) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 02», encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-tres-filas-summitt/mix.py.
La voz se abre en cinco silencios para que quepan los viajes de cámara: 0,4 s en 4,98 («Oeste... Pat»), 9,83 («más... Y»), 14,44 («arriba... Tirarse»)
y 16,97 («cuenta... Ocho»), y 0,45 s en 19,22 («campeones... Lo pequeño», la pausa del remate); words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.9; DUR = OUT + 5.61   # la voz acaba en 23,73 s; a 23,9 empieza el fundido de 0,6 s al cierre
CUTS = [(4.98, .4), (9.83, .4), (14.44, .4), (16.97, .4), (19.22, .45)]
FLY = [4.66, 9.92, 14.9, 17.84, 20.61]
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
M = ld('mus.mp3'); LM = len(M) / SR   # 9,77 s
at = 0.0; k = 0
while at < DUR:                                     # pasadas encadenadas con fundidos de 1,4 s
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(55) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); PG = pk(on(ld('page.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
MK = pk(on(ld('marker.mp3'))); PE = pk(on(ld('pencil.mp3'))); CH = pk(on(ld('chip.mp3'))); TK = pk(on(ld('tick.mp3')))
SQ = pk(ld('squeak.mp3')[int(20.5 * SR):int(21.2 * SR)]); BO = pk(on(ld('bounce.mp3')))
for f in FLY: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, PG, T(2) - .1, .10)                                    # la hoja del calendario se pasa
put(sfx, SH, T(3) - .55, .07, dur=1.0, fo=.3)                   # Kareem en ficha (obturador)
put(sfx, SL, T(5) - .45, .05)                                   # marcador
put(sfx, MK, T(5) - .05, .05, dur=.4, fo=.12)                   # LAKERS tachado
put(sfx, ST, T(8) - .04, .09)                                   # sello ELIMINADOS
put(sfx, SL, T(11) - .55, .06)                                  # portada de Riley
put(sfx, MK, E(16) - .05, .07, dur=.45, fo=.15)                 # «GANAR MÁS» tachado
put(sfx, SL, T(17) - .4, .04)                                   # libreta
put(sfx, PE, T(19), .07, dur=1.6, fo=.3)                        # cinco jugadores apuntados a lápiz
put(sfx, PE, T(22) - .05, .06, off=1.6, dur=.7, fo=.2)          # +1 %
put(sfx, SH, T(25) - .55, .06, dur=1.0, fo=.3)                  # Magic en ficha
for i in range(3): put(sfx, CH, T(31) - .05 + i * .16, .05)     # fichas: su número
for i in range(4): put(sfx, TK, T(35) + i * .1, .035, dur=.12, fo=.05)   # tic del contador hasta 800
put(sfx, BO, T(39) + .05, .08, dur=1.2, fo=.4)                  # balón suelto que bota una vez
put(sfx, SQ, T(43), .06, fo=.2)                                 # chirrido de zapatilla en la estirada
put(sfx, CH, T(45) + .1, .05)                                   # +1 a la libreta
put(sfx, SH, T(47) - .55, .06, dur=1.0, fo=.3)                  # desfile en polaroid
put(sfx, SL, T(51) - .6, .04)                                   # libreta del final
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
