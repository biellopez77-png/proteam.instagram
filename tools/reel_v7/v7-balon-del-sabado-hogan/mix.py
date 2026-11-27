"""Mezcla v7 · El balón del sábado (Jimmy Hogan) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» y «… Logo 03», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-partido-secreto-mclendon/mix.py.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)
r2 (27/11, Marta A): remate quieto hasta 23,95 s, fundido a negro 23,95–24,45 y cierre común outro2 desde 24,45 s (su audio entra ahí); la música sigue bajando bajo el cierre."""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.95; OC = OUT + 0.5; DUR = OC + 4.0   # la voz acaba en 22,86 s; remate quieto hasta 23,95; fundido de 0,5 s; outro2 (4 s) desde 24,45
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
M1, M2 = ld('mus1.mp3'), ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, fi=.3, fo=1.4)
put(mus, M2, len(M1) / SR - 1.4, 1.0, dur=DUR - (len(M1) / SR - 1.4), fi=1.4, fo=3.2)   # la música sigue bajando bajo el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .25 * np.clip((tt - E(43)) / .2, 0, 1) * np.clip((T(44) + .2 - tt) / .3, 0, 1)  # pausa «...»: solo música
env *= 1 + .3 * np.clip((tt - T(51)) / .5, 0, 1) * np.clip((OC - tt) / .8, 0, 1)   # sube en el remate y baja al cierre
env *= 1 - .45 * np.clip((tt - OUT) / .5, 0, 1)   # bajo el cierre, más baja
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); FL = pk(ld('flip.mp3')); SH = pk(ld('shutter.mp3')); NW = pk(ld('news.mp3'))
MK = pk(ld('marker.mp3')); ST = pk(ld('stamp.mp3')); LK = pk(ld('locker.mp3')); PL = pk(ld('padlock.mp3')); KK = pk(ld('kick.mp3')); SP = pk(ld('steps.mp3'))
for f in [1.15, 5.2, 8.15, 12.3, 15.68, 19.45]: put(sfx, WH, f - .25, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .09)                                   # el sello
put(sfx, FL, T(3) - .1, .11, off=.3, dur=.45, fo=.1)     # tablilla HUNGRÍA 6
put(sfx, FL, T(4) - .05, .11, off=.3, dur=.45, fo=.1)    # tablilla INGLATERRA 3
put(sfx, SL, T(7) - .3, .08); put(sfx, SH, T(7) - .15, .1)   # polaroid de Wembley
put(sfx, NW, T(9) - .6, .1, off=.2, dur=1.2, fi=.1, fo=.4)   # recorte del equipo húngaro
put(sfx, SL, T(11) - .15, .07)                           # tarjeta de prensa
put(sfx, MK, T(22) - .3, .18, dur=1.0, fo=.3)            # flecha de rotulador
put(sfx, SL, E(22) + .05, .08)                           # recorte de Hogan
put(sfx, ST, T(24) + .12, .2)                            # sello INGLÉS
put(sfx, KK, T(28) - .15 - .8, .08, dur=1.2, fo=.2)      # el balón entra en el armario
put(sfx, LK, T(30) + .1, .14, dur=1.5, fo=.5)            # la puerta del armario se cierra
put(sfx, PL, T(31) + .15, .12)                           # candado
put(sfx, SL, T(33) - .1, .07)                            # tarjeta SOLO EL SÁBADO
put(sfx, SL, T(36) - .5, .08); put(sfx, SH, T(36) - .2, .09)   # foto de 1910
put(sfx, MK, T(36) - .2, .16, dur=1.0, fo=.3)            # círculo de rotulador
put(sfx, KK, T(38) - .2 - .8, .08, dur=1.2, fo=.2)       # el balón rueda hacia él
put(sfx, KK, T(40) + .3 - .8, .12, dur=1.2, fo=.2)       # control
put(sfx, KK, T(41) - .8, .12, dur=1.2, fo=.2)            # pase
put(sfx, SP, T(43) - 1.1, .1, dur=1.9, fi=.2, fo=.3)     # moverse
put(sfx, KK, T(44) - .5 - .8, .07, dur=1.2, fo=.2)       # balón final
put(sfx, SL, T(46) - .1, .07)                            # tarjeta otra vez
put(sfx, MK, T(50) - .35, .2, dur=1.0, fo=.3)            # tachón
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
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
