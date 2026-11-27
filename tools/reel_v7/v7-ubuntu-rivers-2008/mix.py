"""Mezcla v7 · Cambió el grito (Doc Rivers y el «Ubuntu», Celtics 2007-08) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 01», encadenada consigo misma con fundido de 1,4 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/bielsa/mix3.py y v7-techo-forest-clough/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json con los tiempos de wt.py; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.95; DUR = OUT + 4.0   # la voz acaba en 24,66 s; a 24,95 empieza el fundido de 0,5 s al cierre nuevo (outro2.mp4, 4,0 s, sin app)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
M = ld('mus1.mp3')
put(mus, M, 0.0, 1.0, dur=19.0, fi=.4, fo=1.4)                 # primera vuelta (la pista decae a partir de 19 s)
put(mus, M, 17.6, 1.0, dur=OUT + 1.8 - 17.6, fi=1.4, fo=1.4)   # se encadena consigo misma (misma tonalidad), fundido de 1,4 s
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(54)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube 1 s en «cambió el equipo» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); PA = pk(ld('paper.mp3'))
BK = pk(ld('book.mp3')); TO = pk(ld('token.mp3')); SQ = pk(ld('shoe.mp3')); GY = pk(ld('gym.mp3')); CO = pk(ld('counter.mp3')); CF = pk(ld('confetti.mp3'))
for f in [4.92, 13.32, 19.02, 22.08]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, TO, T(7) - .05, .06, dur=1.0, fo=.4)            # las 24 fichas azules caen
put(sfx, TO, T(10) - .05, .05, dur=1.2, fo=.5)           # las 58 apagadas
put(sfx, SH, T(14) - .4, .09)                            # foto de Doc Rivers (obturador)
put(sfx, SL, T(15) - .08, .08)                           # ficha de prensa
put(sfx, BK, T(16) - .1, .12, dur=1.6, fo=.4)            # el libro se abre
put(sfx, SL, T(18) - .15, .06)                           # retrato de Tutu en la página
put(sfx, PA, T(25) - .08, .07, dur=.6, fi=.03, fo=.2)    # rotulador: «UBUNTU»
put(sfx, PA, T(28), .05, dur=1.2, fi=.03, fo=.3)         # rotulador: flecha y círculo
put(sfx, SQ, T(32) - .25, .07, off=2.0, dur=1.6, fi=.1, fo=.6)   # zapatillas en el parqué
put(sfx, MK, E(41) - .1, .07, dur=.5, fi=.02, fo=.2)     # se tacha «CELTICS!»
put(sfx, GY, T(42) - .3, .10, off=10.0, dur=1.9, fi=.4, fo=.8)   # pabellón vacío, sin voces
put(sfx, CO, T(45) - .05, .06, dur=1.3, fi=.03, fo=.4)   # marcador mecánico 24 → 66
put(sfx, SH, T(48) - .35, .08)                           # foto de Pierce
put(sfx, CF, T(49) - .1, .05, off=1.0, dur=1.4, fi=.1, fo=.6)    # confeti, discreto
put(sfx, SL, T(52) - .1, .06)                            # vuelve el bocadillo pequeño
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo, como en tools/recut/recut.py
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
