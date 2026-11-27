"""Mezcla v7 · Tienen hambre (Wenger y el chocolate, 1996) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 01», 25,7 s; se encadena consigo misma con un fundido de 1,4 s; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-tacos-berna-1954/mix.py.
La voz se abre 0,3 s en 5,6 («Arsenal... En»), 13,42 («partido... Ganan»), 18,56 («chocolatinas... Y») y 21,8 («agua... El») para que quepan los viajes;
words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.4; DUR = OUT + 5.61
CUTS = [(5.6, .3), (13.42, .3), (18.56, .3), (21.8, .3)]
FLY = (5.3, 10.88, 13.5, 18.95, 22.45)
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
M = ld('mus.mp3'); ML = len(M) / SR
put(mus, M, 0.0, 1.0, fi=.3, fo=1.4); put(mus, M, ML - 1.4, 1.0, fi=1.4, fo=2.0)   # se encadena consigo misma (fundido de 1,4 s)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(53) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); FL = pk(ld('flip.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(on(ld('marker.mp3')))
ST = pk(ld('stamp.mp3')); RM = pk(ld('room.mp3')[int(20 * SR):int(32 * SR)]); CR = pk(ld('creak.mp3')); LA = pk(ld('latch.mp3'))
WR = pk(ld('wrap.mp3')); BU = pk(ld('bus.mp3')); PL = pk(ld('plate.mp3')); PO = pk(ld('pour.mp3'))
for f in FLY: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)              # aire en cada viaje
put(sfx, SL, 0.0, .05)                                                       # el estadio en ficha
put(sfx, SL, T(1) - .3, .04); put(sfx, SL, T(1) - .1, .03)                   # Wenger y su ficha
put(sfx, ST, T(5) - .05, .09, off=7.30, dur=.5, fo=.15)                      # sello «PARTIDO 1»
put(sfx, RM, 5.9, .06, dur=5.2, fi=.6, fo=.8)                                # vestuario casi en silencio
put(sfx, CR, T(13), .06, off=3.5, dur=1.1, fi=.1, fo=.4)                     # el banco cruje en «nadie»
put(sfx, SL, T(15) - .45, .03)                                               # maletín
put(sfx, LA, T(16) - .05, .07, off=1.05, dur=.8, fo=.3)                      # el cierre del maletín
put(sfx, SL, T(18) - .25, .025); put(sfx, SL, T(20) - .25, .025)             # bocadillos
put(sfx, SL, 11.2, .04)                                                      # bandeja
put(sfx, MK, T(26), .07, dur=.45, fo=.15); put(sfx, MK, T(26) + .2, .06, off=2.05, dur=.45, fo=.15)   # la cruz de rotulador
put(sfx, WR, T(28) - .05, .05, off=.15, dur=1.0, fo=.35)                     # la chocolatina sale (envoltorio)
put(sfx, SL, 13.95, .04)                                                     # marcador
put(sfx, FL, T(32) - .08, .08, off=.33, dur=.5, fo=.15); put(sfx, FL, T(34) - .08, .08, off=.33, dur=.5, fo=.15)   # tablillas 2 y 0
put(sfx, BU, T(35) - .6, .07, off=8.6, dur=4.4, fi=.5, fo=1.4)               # el autocar pasa, bajo
put(sfx, SH, 19.4, .06, off=3.15, dur=.6, fo=.2)                             # polaroid de Wenger en la banda
put(sfx, PL, T(48) - .3, .07, off=.85, dur=.7, fo=.25)                       # el plato en la mesa
put(sfx, SL, T(49), .03); put(sfx, SL, T(50), .03)                           # pescado y brócoli
put(sfx, PO, T(52) - .15, .07, off=.25, dur=1.3, fi=.05, fo=.4)              # agua en el vaso
put(sfx, SL, 22.95, .035); put(sfx, MK, T(55), .04, dur=.5, fo=.2)           # plato → campo y flecha
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
