"""Mezcla v7 · Un equipo no se ficha (Guy Roux y el Auxerre) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01», encadenada consigo misma con fundidos de 1,4 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-ubuntu-rivers-2008/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json con los tiempos de wt.py; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.42; DUR = OUT + 4.0   # la voz acaba en 21,82 s; a 22,42 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s, sin app)
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
put(mus, M, 0.0, 1.0, dur=11.6, fi=.4, fo=1.4)                    # primera vuelta (la pista decae a partir de ~11,5 s)
put(mus, M, 10.2, 1.0, off=1.0, dur=11.6, fi=1.4, fo=1.4)         # se encadena consigo misma (misma tonalidad), fundido de 1,4 s
put(mus, M, 20.4, 1.0, off=1.0, dur=OUT + 1.8 - 20.4, fi=1.4, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(48)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube en «se construye» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
TO = pk(ld('token.mp3')); CO = pk(ld('cone.mp3')); CU = pk(ld('cup.mp3')); PG = pk(ld('pages.mp3'))
for f in [3.25, 6.18, 8.85, 12.27, 15.3, 18.08]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, T(3) - .45, .07)                             # foto del estadio
put(sfx, SL, T(4) - .05, .06)                             # ficha «AUXERRE · 1961»
put(sfx, TO, T(6) + .2, .07, dur=1.0, fo=.4)              # la ficha cae en «Regional»
put(sfx, SH, T(8) - .35, .09)                             # polaroid de Guy Roux (obturador)
put(sfx, MK, T(10), .045, dur=.9, fi=.03, fo=.3)          # se dibujan el silbato y las botas
put(sfx, SL, T(12) - .15, .06)                            # ficha «GUY ROUX»
for k in [16, 17]: put(sfx, TO, T(k) + .26, .06, dur=.7, fo=.3)   # la ficha sube peldaño a peldaño
put(sfx, TO, T(19) + .2, .07, dur=.9, fo=.4)              # llega a Primera
put(sfx, CO, T(21), .05)                                  # conos en la pizarra
for i in range(3): put(sfx, TO, T(22) + .35 + i * .18, .035, dur=.5, fo=.2)   # chapas
put(sfx, SH, T(27) - .3, .08)                             # foto de Cantona
put(sfx, SL, T(28) - .05, .06)                            # ficha «ERIC CANTONA»
put(sfx, CU, T(32) - .05, .05, dur=1.1, fi=.02, fo=.5)    # trofeo: Liga
put(sfx, CU, T(34) - .05, .05, off=1.5, dur=1.1, fi=.02, fo=.5)   # trofeo: Copa
put(sfx, PG, T(35), .07, dur=1.0, fi=.05, fo=.3)          # el calendario pasa de 1961 a 2005
put(sfx, SH, T(35) - .2, .06)                             # foto de Guy Roux en 2008
put(sfx, MK, T(39), .04, dur=1.0, fi=.05, fo=.3)          # se dibuja el banquillo
put(sfx, MK, E(47) - .12, .07, dur=.5, fi=.02, fo=.2)     # se tacha «FICHA»
for i in range(4): put(sfx, TO, T(48) + i * .22, .04, dur=.5, fo=.2)   # los peldaños se marcan uno a uno
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
