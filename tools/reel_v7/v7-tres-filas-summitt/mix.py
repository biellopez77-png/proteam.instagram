"""Mezcla v7 · Las tres primeras filas (Pat Summitt, Tennessee) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Calm, Piano 02», encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-calcetin-wooden/mix.py.
La voz se abre en cuatro silencios para que quepan los viajes de cámara: 0,5 s en 3,40 («Tennessee... Y»), 0,4 s en 5,94 («pista... Era»),
0,45 s en 11,95 («banquillo... Todas») y 0,55 s en 14,57 («graduaron... Lo que exiges», la pausa del remate); words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 19.4; DUR = OUT + 5.61   # la voz acaba en 19,2 s; a 19,4 empieza el fundido de 0,6 s al cierre
CUTS = [(3.40, .5), (5.94, .4), (11.95, .45), (14.57, .55)]
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
M = ld('mus.mp3')
put(mus, M, 0.0, 1.0, fo=1.4)                      # primera pasada
put(mus, M, 10.4, 1.0, fi=1.4, fo=1.4)             # entra mientras la primera se apaga
put(mus, M, 20.4, .8, fi=1.0, fo=1.5)              # bajo el cierre (se funde con el final)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(45) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); TP = pk(on(ld('tap.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
MK = pk(on(ld('marker.mp3'))); CH = pk(on(ld('chalk.mp3'))); CR = pk(on(ld('chair.mp3')))
for f, g in [(3.2, .08), (6.1, .06), (12.48, .08), (15.74, .08)]: put(sfx, WH, f - .3, g, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06)                                          # Summitt recortada
put(sfx, SL, T(1) - .05, .04)                                   # ficha de prensa
for i in range(8): put(sfx, TP, T(3) - .05 + i * .12 + .1, .035, dur=.4, fo=.12)   # ocho trofeos en la balda
put(sfx, SH, T(8) - .5, .07, dur=1.0, fo=.3)                    # el pabellón en polaroid
put(sfx, MK, T(13) - .05, .05, dur=.8, fo=.25)                  # la línea de banda se traza
put(sfx, MK, E(17) - .2, .07, dur=.45, fo=.15)                  # «PISTA» tachada
put(sfx, CH, T(20) - .05, .07, dur=.8, fo=.2)                   # tiza en la pizarra
for k in (25, 26, 27): put(sfx, CR, T(k) - .03, .07, dur=.6, fo=.15)   # fila 1, 2 y 3 (golpe seco de silla)
put(sfx, ST, T(33) - .04, .09)                                  # sello «BANQUILLO»
put(sfx, SL, T(34) - .55, .06)                                  # foto de 2008
put(sfx, SL, T(42) - .55, .04)                                  # aula y pista del final
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
