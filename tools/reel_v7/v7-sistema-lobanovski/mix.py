"""Mezcla v7 · Veintidós piezas (Lobanovski y Zelentsov) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02» y «… Logo 03», encadenadas con fundidos de 1,4 s; distintas a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-sexto-hombre-auerbach/mix.py.
La voz se abre 0,5 s en el silencio de «Recopas... Porque» (19,25 s) para que la pausa del guion respire; words.json ya lleva ese desplazamiento.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.45; DUR = OUT + 5.61; CUT = 19.25; GAP = 0.5   # la voz acaba en 22,44 s; a 22,45 empieza el fundido de 0,6 s al cierre
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
M2 = ld('mus2.mp3'); M3 = ld('mus3.mp3')
put(mus, M2, 0.0, 1.0, dur=9.4, fo=1.4)            # 02: sube y sostiene
put(mus, M3, 6.6, 1.0, dur=9.6, fi=1.4, fo=1.4)    # 03: entra mientras 02 se apaga
put(mus, M2, 14.2, 1.0, fi=1.4, fo=1.0)            # 02 otra vez: sostiene la pausa y el remate, cola hacia el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(47) - .2)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); PC = pk(ld('pencil.mp3')); CL = pk(ld('clink.mp3'))
CD = pk(ld('card.mp3')); PN = pk(ld('pen.mp3')); SC = pk(ld('scrib.mp3')); PI = pk(ld('piece.mp3')); MK = pk(ld('marker.mp3'))
ST = pk(ld('stamp.mp3')); WB = pk(ld('wb.mp3'))
for f in [2.5, 6.55, 11.1, 15.35, 19.05]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06)                                          # retrato de 1985
put(sfx, SL, T(1) - .05, .05)                                   # ficha de prensa
put(sfx, PC, T(3) - .2, .08, off=1.0, dur=1.4, fi=.05, fo=.4)   # lápiz: el plano del radiador
put(sfx, CL, T(7) + .26, .09, dur=1.5, fo=.6)                   # dos copas que brindan
put(sfx, SL, T(11) - .15, .06)                                  # la tarjeta se desliza
put(sfx, CD, T(11) + .2, .05)                                   # y se posa
put(sfx, SH, T(14) - .45, .07)                                  # foto de la tribuna, 1975
put(sfx, SL, T(15) - .1, .05)                                   # la hoja de registro
for k in [17, 19, 22]: put(sfx, PN, T(k) - .02, .09, dur=.45, fo=.15)   # un trazo de bolígrafo por palabra
put(sfx, SC, T(25) - .1, .1, off=.5, dur=1.1, fi=.05, fo=.35)  # la hoja se llena
for k in range(22): put(sfx, PI, T(31) - .05 + k * .038 + .18, .05 - .0012 * k)   # 22 fichas sobre el tablero
put(sfx, MK, T(35) - .1, .05, off=.2, dur=1.2, fi=.05, fo=.35)  # rotulador: la red de los once
put(sfx, SH, T(37) - .45, .07)                                  # foto del Dinamo de Kiev, 1975
put(sfx, ST, T(41), .09)                                        # sello ARCHIVO · 1975
put(sfx, MK, T(45) - .1, .04, off=1.6, dur=.9, fi=.05, fo=.3)   # las copas se dibujan
put(sfx, ST, T(46), .08); put(sfx, ST, T(46) + .35, .08)         # dos sellos: 1975 · 3-0 y 1986 · 3-0
put(sfx, WB, T(49) + .1, .05, dur=1.0, fi=.05, fo=.3)           # pizarra: la red
put(sfx, WB, T(51) - .05, .06, off=1.5, dur=.45, fi=.03, fo=.15)  # el signo «>»
put(sfx, WB, T(53), .05, off=2.5, dur=1.0, fi=.05, fo=.3)       # los once unos
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
put(vox, V[:int(CUT * SR)], 0.0); put(vox, V[int(CUT * SR):], CUT + GAP)
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
