"""Mezcla v7 · La guerra (Tom Izzo, Michigan State 1999-2000) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 01», 25,7 s; distinta de la del último v7) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-salid-y-disfrutad-cruyff/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
HOLD = E(50) + 1.0; OUT = HOLD + .5; DUR = OUT + 4.0   # remate quieto 1 s tras «entrena», fundido a negro de 0,5 s y outro2.mp4 (4,0 s, sin app)
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
put(mus, ld('mus1.mp3'), 0.0, 1.0, dur=OUT + 2.2, fi=.25, fo=2.0)   # la música baja durante el cierre
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(49)) / .4, 0, 1) * np.clip((OUT + .2 - tt) / .9, 0, 1)   # sube 1 s en «se entrena» y baja al cierre
env *= np.interp(tt, [0, OUT, OUT + 1.0, DUR], [1, 1, .55, .3])
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); CH = pk(ld('chips.mp3'))
HE = pk(ld('helmet.mp3')); TH = pk(ld('thud.mp3')); BO = pk(ld('bounce.mp3')); SQ = pk(ld('squeak.mp3')); ST = pk(ld('stamp.mp3'))
TA = pk(ld('tape.mp3')); AP = pk(ld('applause.mp3'))
for f in [2.32, 6.66, 10.9, 13.86, 16.98]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 8.62, .04, dur=1.0, fi=.1, fo=.4)              # empuje hacia la libreta
put(sfx, SL, .02, .04)                                      # foto de Izzo (ya en pantalla)
put(sfx, SL, T(3) - .15, .05)                               # ficha TOM IZZO
put(sfx, SH, T(7) - .2, .08)                                # polaroid del entreno
put(sfx, HE, T(10) + .15, .14); put(sfx, TH, T(10) + .17, .07)   # el casco cae en el banco
put(sfx, HE, T(12) + .15, .08); put(sfx, TH, T(12) + .17, .06)   # las hombreras
put(sfx, BO, T(17) - .05, .10, dur=.5, fo=.2)               # un bote en el parqué («baloncesto»)
put(sfx, SL, T(17) + .2, .035)                              # rótulo Michigan State · 1999-2000
put(sfx, CH, T(18) - .05, .05, dur=1.0, fo=.3)              # diez fichas
put(sfx, SL, T(22) - .1, .05)                               # libreta
put(sfx, MK, T(24) - .05, .06, dur=.45, fi=.02, fo=.15)     # «1.»
put(sfx, MK, T(27) - .05, .06, off=2.4, dur=.45, fi=.02, fo=.15)   # se tacha
put(sfx, ST, T(27) + .42, .12)                              # sello «SIN REGLAS»
put(sfx, SH, 11.15, .07)                                    # foto del rebote
put(sfx, SQ, T(31) - .15, .07, off=4.4, dur=1.0, fi=.05, fo=.4)   # zapatillas en el parqué, corto
put(sfx, MK, T(34) - .1, .035, off=3.25, dur=.8, fi=.05, fo=.2)   # marcas del calendario
put(sfx, SL, 14.2, .06)                                     # periódico
put(sfx, AP, T(42) + .1, .035, dur=2.2, fi=.3, fo=.9)       # aplauso lejano y corto
put(sfx, TA, T(45) - .1, .05, fo=.3)                        # cinta métrica
put(sfx, MK, T(48) + .3, .03, off=5.0, dur=.35, fi=.02, fo=.1)    # marca de lo que falta
put(sfx, SL, T(49) - .3, .03)                               # pista en calma
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                     # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2) # sting de piano bajo
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
print('OUT %.2f DUR %.2f  voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (OUT, DUR, R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
