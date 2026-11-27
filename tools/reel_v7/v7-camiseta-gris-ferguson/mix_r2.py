"""r2 (27/11, Marta B): el remate «verlo» respira hasta 24,9 s, fundido a negro de 0,5 s y outro2 (cierre común, con su voz) a 25,4 s;
la música sigue bajando bajo el cierre. Antes: tail.mp3 (cierre retirado) a 24,4 s.
python3 mix_r2.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)

Mezcla v7 · La camiseta gris (Ferguson, The Dell 1996) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Intro, Tv», encadenada consigo misma con fundidos de 1,4 s; no usada en los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-contar-rivales-rangnick/mix.py.
La voz se abre en cuatro silencios para que quepan los viajes de cámara: 5,65 (+0,4), 10,63 (+0,5), 15,15 (+0,4) y 19,19 (+0,6, la pausa del remate);
words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.9; OUT2 = OUT + 0.5; DUR = OUT2 + 4.0   # la voz acaba en 23,86 s; quieto hasta 24,9; negro 24,9–25,4; outro2 desde 25,4
CUTS = [(5.65, .4), (10.63, .5), (15.15, .4), (19.19, .6)]
FLY = [5.4, 10.84, 15.8, 20.34]
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
M = ld('mus.mp3'); LM = len(M) / SR   # 15,1 s
at = 0.0; k = 0
while at < DUR:
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(59) - .3)) / .4, 0, 1) * np.clip((OUT + .5 - tt) / .6, 0, 1)   # sube en el remate y vuelve a su nivel en el negro
env *= np.interp(tt, [OUT2 + .1, OUT2 + .5, DUR - 1.2, DUR], [1, .5, .5, 0])   # bajo la voz del cierre sigue bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); CR = pk(ld('crowd.mp3'))
DO = pk(on(ld('door.mp3'))); CL = pk(on(ld('cloth.mp3'))); CK = pk(on(ld('click.mp3'))); ST = pk(ld('steps.mp3')); KI = pk(on(ld('kick.mp3'))); MK = pk(on(ld('marker.mp3')))
for f in FLY: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, CR, 0, .10, off=12, dur=5.6, fi=.3, fo=1.2)            # grada lejana en The Dell, muy baja
put(sfx, SL, -.05, .07)                                         # ficha de prensa de The Dell
for a in [T(8), T(8) + .3, T(9)]: put(sfx, CK, a, .08, dur=.3, fo=.1)   # tres clics del marcador
put(sfx, SH, T(12) - .3, .07, dur=1.0, fo=.3)                   # Ferguson en ficha (obturador)
put(sfx, DO, T(14) - .05, .10, dur=1.6, fo=.5)                  # la puerta del vestuario se abre (sala con eco)
put(sfx, CL, T(21) + .1, .14)                                   # la camiseta cae en el banco
put(sfx, SL, T(22) + .05, .06)                                  # muestra de color GRIS
put(sfx, SL, T(25) - .2, .07)                                   # tarjeta de visión
put(sfx, SH, T(27), .06, dur=1.0, fo=.3)                        # ficha de la experta
put(sfx, CR, T(30) - .3, .10, off=40, dur=3.6, fi=.4, fo=1.0)   # murmullo de grada
put(sfx, CL, T(38) + .1, .10)                                   # sale la gris
put(sfx, ST, T(40) - .2, .08, off=3.0, dur=1.6, fi=.1, fo=.5)   # tacos sobre cemento
put(sfx, CK, T(46) + .1, .06, dur=.3, fo=.1)                    # marcador de la segunda parte
put(sfx, MK, T(45) + .1, .06, dur=.6, fo=.2)                    # tachón de la primera parte
put(sfx, CK, T(49), .08, dur=.3, fo=.1)                         # 0–1
put(sfx, KI, E(59) + .02, .12, dur=1.2, fo=.4)                  # el pase sale por la línea de mirada
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(24.0 * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
O = ld(sys.argv[2]); act = lambda x: np.sqrt(np.mean(x[np.abs(x[:, 0]) > .02] ** 2))
og = act(vox[:int(24.0 * SR)]) / act(O) * .95; ob = np.zeros((N, 2)); put(ob, O, OUT2, og)   # cierre común al nivel de la voz
mix = vox + mus * duck + sfx * vg + ob
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .25) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
