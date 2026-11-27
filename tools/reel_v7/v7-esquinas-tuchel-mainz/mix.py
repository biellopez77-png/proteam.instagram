"""Mezcla v7 · «Le cortó las esquinas» (Tuchel en el Mainz) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», 139 s, desde 2,0 s y sin cortes; distinta de las de los
últimos v7: «Musical, Loop, Piano, Intro, Tv», «Calm Piano, Dreamy, Intro 01–03», «Soft Piano, Strings, Calm, Intro, Logo») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-pantalla-nagelsmann-2017/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 19.88; DUR = OUT + 4.0   # la voz acaba en 19,28 s; a 19,88 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 20,18)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2, af=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', f] + (['-af', af] if af else []) + ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: una sola pieza larga (sin bucles ni cortes), desde 2,0 s (antes hay silencio); baja al cierre
M = ld('mus.mp3')
put(mus, M, 0.0, 1.0, off=2.0, dur=DUR, fi=.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(53)) / .15, 0, 1) * np.clip((T(54) + .1 - tt) / .15, 0, 1)   # baja un poco en la pausa de «hábito...»
env *= 1 + .3 * np.clip((tt - E(56)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)      # sube tras «el campo» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); SC = pk(ld('scissors.mp3'))
TN = pk(ld('tennis.mp3')); CL = pk(ld('cloth.mp3')); MK = pk(ld('marker.mp3')); CH = pk(ld('chips.mp3'))
for f in [3.22, 6.86, 12.12, 16.2]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .05); put(sfx, SL, .3, .035)                               # ficha de Tuchel y campo
for k in range(4):
    c0 = T(3) - .05 + k * .55
    put(sfx, SC, c0 + .05, .08, dur=.45, fo=.12)                             # tijeras: un corte por esquina
    put(sfx, SL, c0 + .5, .02)                                               # la esquina cae como papel
put(sfx, SL, T(11) - .35, .045); put(sfx, SH, T(11) - .25, .07)              # polaroid del campo del Mainz + obturador
put(sfx, SL, T(14) - .1, .035)                                               # ficha de la balanza
put(sfx, CH, E(21) - .05, .02, dur=.3, fo=.1)                                # la balanza se asienta
put(sfx, SL, T(22) - .45, .04)                                               # rombo
put(sfx, MK, T(25), .03, dur=.6, fi=.02, fo=.15)                             # carrera hacia el banderín
put(sfx, MK, T(28) + .1, .035, off=1.0, dur=.35, fi=.02, fo=.1)              # tachadura del banderín
put(sfx, CH, T(29), .022, dur=.35, fo=.1)                                    # fichas azules
put(sfx, MK, T(33) - .05, .035, off=2.0, dur=.55, fi=.02, fo=.15)            # flechas en diagonal
put(sfx, MK, T(34) - .05, .03, off=3.0, dur=.9, fi=.02, fo=.2)               # flechas hasta la portería
put(sfx, CH, T(39) - .1, .02, dur=.3, fo=.1)                                 # fichas de los defensas
for k in range(4): put(sfx, TN, T(43) + k * .12 + .3, .05, dur=.45, fo=.2)   # pelotas de tenis que botan
put(sfx, MK, T(46) - .2, .025, off=4.0, dur=.5, fi=.02, fo=.15)              # camiseta dibujada
put(sfx, CL, T(48) - .15, .07, off=5.5, dur=.9, fi=.05, fo=.3)               # mano que no agarra: tela
put(sfx, SL, 16.75, .035)                                                    # ficha pequeña y rombo final
put(sfx, MK, T(55), .025, off=1.5, dur=.6, fi=.02, fo=.15)                   # flechas finales
v = ld(sys.argv[1], 1)
put(vox, np.repeat(v, 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a2 = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a2 * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
