"""Mezcla v7 · Cansados de mi voz (Steve Kerr, 2018) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde los 2 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-balon-del-sabado-hogan/mix.py.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)
La voz acaba en 20,04 s; remate quieto hasta 20,64 s; fundido a negro de 0,5 s; outro2 (4 s, con su voz) desde 21,14 s; la música sigue bajando bajo el cierre."""
import sys, json, subprocess, numpy as np
SR = 48000
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
OUT = E(51) + 0.6; OC = OUT + 0.5; DUR = OC + 4.0
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
put(mus, ld('mus.mp3'), 0.0, 1.0, off=2.0, dur=DUR, fi=.4, fo=3.2)   # la música sigue bajando bajo el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .25 * np.clip((tt - E(46)) / .2, 0, 1) * np.clip((T(47) + .2 - tt) / .3, 0, 1)   # pausa «...»: solo música
env *= 1 - .15 * np.clip((tt - T(40)) / .6, 0, 1) * np.clip((T(51) - tt) / .4, 0, 1)        # «Kerr lo explicó así»: la música baja un poco
env *= 1 + .3 * np.clip((tt - T(51)) / .5, 0, 1) * np.clip((OC - tt) / .8, 0, 1)            # sube en «suyo» y baja al cierre
env *= 1 - .45 * np.clip((tt - OUT) / .5, 0, 1)                                               # bajo el cierre, más baja
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
ST = pk(ld('stamp.mp3')); CL = pk(ld('clip.mp3')); CN = pk(ld('counter.mp3')); TK = pk(ld('token.mp3'))
for f in [1.26, 7.08, 11.0, 13.6, 15.42]: put(sfx, WH, f - .25, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.05, .1)                                   # la hoja del calendario cae
put(sfx, SL, T(2) + .05, .06)                            # ficha del equipo
put(sfx, SH, T(3) - .25, .1); put(sfx, SL, T(4) + .05, .06)   # foto de Kerr y su ficha
put(sfx, MK, T(8) - .05, .06, dur=.7, fi=.05, fo=.3)     # ondas de voz (trazo de rotulador)
put(sfx, SL, T(16), .05)                                 # «y yo también»
put(sfx, SL, T(21) - .25, .07)                           # marcador TIEMPO MUERTO
put(sfx, TK, T(21) + .05, .1, dur=1.1, fo=.3)            # las fichas hacen corro
put(sfx, CL, T(26) + .2, .14)                            # la pizarra se apoya en el centro
put(sfx, MK, T(28), .1, dur=.8, fi=.05, fo=.3)           # flecha sobre la pizarra
put(sfx, SH, T(28) - .15, .08)                           # recorte de Iguodala
put(sfx, SL, T(30) - .4, .07); put(sfx, SH, T(30) - .2, .08)   # polaroid de Green
put(sfx, MK, T(32), .14, dur=1.5, fi=.05, fo=.3)         # X y O y flecha
put(sfx, MK, T(33), .12, dur=.35, fo=.1); put(sfx, MK, T(34), .12, off=1.0, dur=.35, fo=.1); put(sfx, MK, T(36), .12, off=2.0, dur=.35, fo=.1)   # tres TM tachados
put(sfx, SL, T(37) - .5, .08); put(sfx, SH, T(37) - .3, .08)   # foto del corro
put(sfx, CN, T(37), .05, dur=E(39) - T(37), fi=.05, fo=.15)    # contador 129–83, muy bajo
put(sfx, ST, T(39) + .2, .2)                             # sello +46
put(sfx, SL, T(40) - .45, .06)                           # ficha pequeña de Kerr
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OC)   # audio de outro2.mp4
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
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f  dur %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max(), DUR))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
