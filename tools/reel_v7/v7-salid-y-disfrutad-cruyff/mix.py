"""Mezcla v7 · Salid y disfrutad (Johan Cruyff antes de la final de Wembley, 1992) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», 139 s, sin encadenar; distinta de la del último v7) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-diez-a-tres-brooks-1980/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.85; DUR = OUT + 4.0   # la voz acaba en 22,75 s; el vídeo sigue hasta 23,35 (0,6 s) y a 22,85 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s, sin app)
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
put(mus, ld('mus1.mp3'), 0.0, 1.0, off=1.9, dur=DUR, fi=.3, fo=1.4)   # la pista empieza con 2,1 s de silencio
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .25 * np.clip((tt - T(32)) / .4, 0, 1) * np.clip((T(32) + 1.4 - tt) / .4, 0, 1)   # la música abre 1 s en «disfrutad»
env *= 1 + .3 * np.clip((tt - T(49)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)      # sube en «Se sale a disfrutar» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); CO = pk(ld('counter.mp3'))
CR = pk(ld('crowd.mp3')); KI = pk(ld('kick.mp3')); TI = pk(ld('tick.mp3'))
for f in [2.45, 5.85, 8.65, 15.0, 16.85, 18.98]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SH, .05, .08)                                     # polaroid de Wembley (obturador)
put(sfx, SL, E(1) - .25, .05)                              # ficha del partido
put(sfx, SL, T(6) - .15, .06); put(sfx, SL, T(7) - .05, .05)   # tarjetas 1961 y 1986
put(sfx, MK, T(8), .06, dur=.45, fi=.02, fo=.15); put(sfx, MK, T(9), .06, off=1.0, dur=.5, fi=.02, fo=.15)   # dos cruces de rotulador
put(sfx, MK, T(10) - .1, .035, off=2.0, dur=1.0, fi=.05, fo=.3)   # copa de contorno
put(sfx, SH, T(13) - .35, .08)                             # foto de Cruyff
put(sfx, SL, T(16) - .1, .05)                              # ficha J. CRUYFF
put(sfx, MK, T(18) - .25, .05, off=3.0, dur=.9, fi=.03, fo=.25)   # flecha y «stop»
put(sfx, SL, T(20) - .45, .05)                             # vuelve la polaroid de Wembley
c = CR[int(10 * SR):].copy()                               # murmullo de estadio, muy lejano: entra en la cita, sube en «lleno» y baja en «disfrutad»
ce = np.interp(np.arange(len(c)) / SR + T(20) - .4, [T(20) - .4, T(20) + .4, T(28), T(29), T(32), T(32) + 1.2], [0, .03, .03, .055, .055, 0])
put(sfx, c * ce[:, None], T(20) - .4, 1.0, dur=T(32) + 1.2 - (T(20) - .4))
put(sfx, MK, T(24) - .05, .04, off=4.0, dur=1.2, fi=.05, fo=.3)   # líneas del campo
put(sfx, SL, T(30) - .4, .06)                              # tarjeta de la cita
put(sfx, TI, T(33) - .4, .035, off=2.0, dur=1.7, fi=.1, fo=.4)    # tic de reloj, muy bajo
put(sfx, SH, T(35) - .4, .06); put(sfx, SL, T(35) - .2, .04)      # foto de Koeman y pizarra
put(sfx, CO, T(36), .04, dur=.35, fi=.02, fo=.12)          # fichas de la barrera
put(sfx, KI, T(37) + .05, .12, dur=.6, fo=.2)              # un solo golpeo de balón
put(sfx, MK, T(37) + .1, .04, off=5.0, dur=.5, fi=.02, fo=.15)    # trayectoria en la pizarra
put(sfx, CO, T(38) - .05, .05, dur=.35, fi=.02, fo=.12)    # el marcador pasa a 1
put(sfx, SL, T(41) - .5, .04)                              # tarjeta de la cita, ya en azul
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
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
