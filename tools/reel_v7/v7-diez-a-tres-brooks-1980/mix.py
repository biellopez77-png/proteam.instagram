"""Mezcla v7 · Lo que haces después (Herb Brooks, 10-3 en el Madison Square Garden y 4-3 en Lake Placid, 1980) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 02», encadenada consigo misma con fundido de 1,4 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-ubuntu-rivers-2008/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json con los tiempos de wt.py; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.62; DUR = OUT + 4.0   # la voz acaba en 24,52 s; el vídeo sigue hasta 25,12 (0,6 s) y a 24,62 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s, sin app)
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
put(mus, M, 0.0, 1.0, dur=24.5, fi=.4, fo=1.4)                     # primera vuelta (24,7 s)
put(mus, M, 23.1, 1.0, off=2.0, dur=DUR - 23.1, fi=1.4, fo=1.4)    # se encadena consigo misma (misma tonalidad), fundido de 1,4 s
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(55)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube 1 s en «después» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); PG = pk(ld('page.mp3'))
MD = pk(ld('medal.mp3')); CO = pk(ld('counter.mp3')); LI = pk(ld('light.mp3')); PU = pk(ld('puck.mp3'))
for f in [3.48, 10.62, 16.5, 20.42]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 9.0, .04, dur=1.1, fi=.1, fo=.4)              # bajada corta al marcador
put(sfx, PG, .3, .06); put(sfx, PG, 1.15, .05)            # hojas del calendario hasta el 9
put(sfx, LI, T(3) - .25, .04, dur=1.6, fi=.02, fo=.6)     # la marquesina se enciende
put(sfx, SL, T(6) - .15, .07)                             # ficha de EE. UU.
put(sfx, SL, T(12) - .25, .06)                            # ficha de la URSS
for k in [13, 14, 15, 16]: put(sfx, MD, T(k) + .12, .09)  # cuatro medallas sobre la mesa
put(sfx, CO, T(18) - .05, .06, dur=1.0, fi=.02, fo=.3)    # marcador mecánico 0 → 10
put(sfx, PU, T(18), .035, off=1.35, dur=1.0, fi=.02, fo=.4)   # discos sobre el hielo, muy bajos
put(sfx, CO, T(20) - .08, .05, dur=.4, fi=.02, fo=.15)    # el 3
put(sfx, SH, T(22) - .2, .09)                             # foto de Herb Brooks (obturador)
put(sfx, SL, T(23) - .05, .06)                            # ficha de prensa
put(sfx, SL, T(26) - .15, .08)                            # el recorte se desliza
put(sfx, MK, T(29), .05, dur=2.4, fi=.03, fo=.4)          # rotulador que subraya la cita
put(sfx, PG, T(37), .05); put(sfx, PG, T(38) + .25, .04); put(sfx, PG, T(39) + .2, .04)   # hojas del 9 al 22
put(sfx, SH, T(41) - .35, .07)                            # foto del pabellón
put(sfx, SL, T(43) - .35, .08)                            # la portada se desliza
put(sfx, CO, T(44) - .05, .05, dur=.35, fi=.02, fo=.15); put(sfx, CO, T(46) - .05, .05, dur=.35, fi=.02, fo=.15)   # 4 a 3, un clic cada uno
put(sfx, MK, T(51) - .05, .07, dur=.6, fi=.02, fo=.2)     # rotulador que tacha el 10-3
put(sfx, SL, T(52) - .3, .05)                             # Jim Craig detrás
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
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
