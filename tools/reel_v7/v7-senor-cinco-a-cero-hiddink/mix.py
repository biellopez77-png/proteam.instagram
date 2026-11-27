"""Mezcla v7 · «Señor Cinco a Cero» (Hiddink y Corea, 2001-2002) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Orchestra, Epic, Dreamy, Suspense», 32 s, una sola pista sin cortes; distinta de las de los
últimos v7: «Logo, Calm, Piano, Pizzicato», «Logo, Calm, Piano 02», «Calm Piano, Dreamy», «Soft Piano, Strings, Calm, Intro, Logo»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/v7-carta-villas-boas-robson/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.0; DUR = OUT + 4.0   # la voz acaba en 21,40 s; a 22,00 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 22,30)
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
# música: una sola pista de 32 s (sin empalmes); baja al cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, dur=DUR, fi=.3, fo=2.2)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(50)) / .15, 0, 1) * np.clip((T(51) + .1 - tt) / .15, 0, 1)   # baja en la pausa de «Mundial...»
env *= 1 + .3 * np.clip((tt - E(54)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)     # sube 1 s tras «juegan» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); CA = pk(ld('card.mp3'))
ST = pk(ld('stamp.mp3')); PG = pk(ld('page.mp3')); CH = pk(ld('chip.mp3')); CR = pk(ld('crowd.mp3')); CL = pk(ld('cloth.mp3')); RU = pk(ld('run.mp3'))
for f in [4.95, 8.45, 13.75, 16.15, 19.45]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .05)                                                      # hoja de calendario
put(sfx, CA, T(1) - .2, .045)                                               # marcador
for i in range(5): put(sfx, CH, T(5) + i * .16, .05, dur=.35, fo=.1)        # cinco fichas (Francia)
put(sfx, PG, T(9) - .05, .06)                                               # persiana del marcador
for i in range(5): put(sfx, CH, T(11) - .1 + i * .11, .04, dur=.35, fo=.1)  # cinco fichas (Chequia)
put(sfx, CA, 5.55, .05); put(sfx, SH, 5.7, .07)                             # ficha de prensa + obturador antiguo
put(sfx, ST, T(19), .13)                                                    # sello «SEÑOR 5-0»
put(sfx, SL, 9.0, .045)                                                     # pizarra
put(sfx, MK, T(25) - .1, .035, dur=.6, fi=.03, fo=.15)                      # «REGLA 1» a rotulador
for i in range(3): put(sfx, CA, T(26) + i * .12, .035)                      # tres etiquetas
for a in [T(28), T(29) - .05, T(30)]: put(sfx, MK, a, .03, off=1.0, dur=.3, fi=.02, fo=.1)   # tres tachones
put(sfx, CA, T(31), .03); put(sfx, CA, T(31) + .3, .025)                    # dorsales
put(sfx, SL, T(38) - .15, .05); put(sfx, RU, T(38) - .1, .03, dur=1.2, fi=.05, fo=.4)   # ficha de Park en carrera
put(sfx, SL, 16.95, .045); put(sfx, SH, 17.0, .06)                          # polaroid de la plaza
put(sfx, CR, 17.6, .035, off=2.0, dur=2.2, fi=.4, fo=.8)                    # multitud muy lejana
put(sfx, CA, T(45) - .2, .04)                                               # cuadro
put(sfx, MK, T(46), .03, off=2.0, dur=.4, fi=.02, fo=.1); put(sfx, MK, T(48) - .1, .03, off=3.0, dur=.35, fi=.02, fo=.1)   # líneas del cuadro
put(sfx, CL, T(52) + .45, .1)                                               # el brazalete cae
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
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
