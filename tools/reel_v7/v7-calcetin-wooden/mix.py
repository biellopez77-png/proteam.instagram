"""Mezcla v7 · Primero, el calcetín (John Wooden, UCLA) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s;
distinta a las de los v7 anteriores, que usaron la 01 y la 02) + SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-general-michels/mix.py.
La voz se abre en tres silencios para que quepan los viajes de cámara: 0,4 s en 3,37 («UCLA... Y»), 0,4 s en 12,77 («ampolla... Kareem»)
y 0,5 s en 18,7 («calcetines... Lo pequeño», la pausa del remate); words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.2; DUR = OUT + 5.61   # la voz acaba en 21,9 s; a 22,2 empieza el fundido de 0,6 s al cierre
CUTS = [(3.37, .4), (12.77, .4), (18.7, .5)]
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
put(mus, M, 11.6, 1.0, fi=1.4, fo=1.4)             # entra mientras la primera se apaga
put(mus, M, 23.0, .8, fi=1.0, fo=1.5)              # bajo el cierre (se funde con el final)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(46) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); TP = pk(on(ld('tap.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
MK = pk(on(ld('marker.mp3'))); TI = pk(on(ld('tick.mp3'))); SK = pk(on(ld('sock.mp3')))
for f, g in [(3.1, .08), (5.3, .05), (12.95, .08), (19.3, .08)]: put(sfx, WH, f - .3, g, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06)                                          # ficha de 1960
put(sfx, SL, T(1) - .05, .04)                                   # ficha de prensa
for i in range(10): put(sfx, TP, T(3) - .08 + i * .115 + .12, .035, dur=.35, fo=.1)   # diez banderines
put(sfx, SH, T(7) - .5, .07, dur=1.0, fo=.3)                    # foto de 1965
put(sfx, ST, T(10) - .04, .09)                                  # sello «DÍA 1»
put(sfx, MK, T(17) - .12, .07, dur=.75, fo=.2)                  # el calcetín se dibuja
put(sfx, TI, T(18), .06, dur=1.05, fo=.25)                      # media hora en el reloj
put(sfx, SK, T(20) - .05, .1, dur=1.7, fo=.5)                   # el calcetín se estira
put(sfx, MK, T(30) - .05, .06, dur=.5, fo=.15)                  # círculo de la ampolla
put(sfx, SL, T(31) - .55, .06)                                  # foto de Alcindor
put(sfx, SL, T(33) - .1, .04)                                   # ficha
put(sfx, SH, T(37) - .1, .04, dur=.8, fo=.3)                    # la cita (obturador muy suave)
put(sfx, SL, T(45) - .6, .04)                                   # el calcetín estirado del final
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
