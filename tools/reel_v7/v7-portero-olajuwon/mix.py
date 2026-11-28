"""Mezcla v7 · Portero hasta los quince (Hakeem Olajuwon) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01» y «… Intro 02», misma serie y tonalidad, alternadas con fundidos de 1,4 s;
distintas de las últimas v7, que usaron «Soft Piano, Strings, Calm, Intro, Logo 01/02/03»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-medianoche-driesell-1971/mix.py.
La voz acaba en 36,46 s; remate quieto (≥ 1 s); fundido a negro 37,5–38,0 s; outro2 (4 s, con su voz) desde 38,0 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py, ya con los índices de words.js)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 38.0; DUR = OUT + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vn', '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: Intro 01 / Intro 02 alternadas, fundidos de 1,4 s
M = [ld('m1.mp3'), ld('m2.mp3')]; at = 0.0; i = 0
while at < DUR:
    m = M[i % 2]; put(mus, m, at, 1.0, fi=(.3 if i == 0 else 1.4), fo=1.4); at += len(m) / SR - 1.4; i += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .25 * np.clip((tt - E(98)) / .4, 0, 1) * np.clip((OUT - tt) / .5, 0, 1)                   # sube un poco con el remate quieto
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                         # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); MK = pk(ld('marker.mp3')); SQ = pk(ld('squeak.mp3')); TI = pk(ld('tick.mp3')); CA = pk(ld('card.mp3'))
for f in [6.24, 10.42, 13.5, 20.24, 21.78, 24.36, 33.86]: put(sfx, WH, f - .25, .08, dur=1.4, fi=.05, fo=.45)   # aire en cada viaje
put(sfx, PA, 0.0, .07, off=.4, fo=.3)                                                                    # la ficha ya en la pared
put(sfx, PA, 2.0 - .4, .07)                                                                              # mapa
put(sfx, MK, 2.6, .045, dur=2.6, fi=.1, fo=.5)                                                           # la costa se dibuja
put(sfx, CA, T(14) - .05, .07)                                                                           # punto en Lagos
put(sfx, PA, 7.0 - .4, .10)                                                                              # guantes y cono
put(sfx, PA, T(24) - .15 - .4, .10)                                                                      # portera de balonmano
put(sfx, CA, 10.95, .06); put(sfx, CA, 11.15, .06)                                                       # las dos fotos se apilan
put(sfx, MK, 11.35, .045, off=3.0, dur=1.8, fi=.05, fo=.4)                                               # silueta de pies a cabeza
for i, o in enumerate([4.5, 6.2, 7.85, 9.15]): put(sfx, SQ, T(36) + i * .12 - .03, .06, off=o - .03, dur=.3, fo=.12)   # huellas del pívot
put(sfx, CA, T(42) - .05, .07); put(sfx, CA, T(43) - .05, .07)                                           # dos anillos
for i in range(8): put(sfx, TI, T(46) + i * .18, .05 - .004 * i, off=1.08, dur=.2, fo=.08)               # el contador sube
put(sfx, CA, T(47) - .03, .06)                                                                           # 3.830 · tapones
put(sfx, PA, 20.55 - .4, .10)                                                                            # carro de balones
put(sfx, PA, 22.05 - .4, .10)                                                                            # penetración
put(sfx, MK, T(62), .06, off=.75, dur=.5, fi=.03, fo=.2)                                                 # círculo al balón
put(sfx, MK, T(64), .07, off=1.62, dur=.3, fi=.02, fo=.12)                                               # se tacha: sin botar
put(sfx, PA, 24.7 - .4, .08)                                                                             # pizarra
for i in range(2): put(sfx, TI, T(68) + i * .5 - .02, .09, off=2.05, dur=.25, fo=.1)                     # reloj de 10′
put(sfx, CA, T(74), .05)                                                                                 # balón en la mano
for i, o in enumerate([10.45, 12.15, 13.85]): put(sfx, SQ, T(78) + i * .24, .10, off=o - .03, dur=.35, fo=.15)   # tres pasos
put(sfx, MK, T(80), .06, off=3.4, dur=.45, fi=.03, fo=.15)                                               # finta
put(sfx, MK, T(82) - .1, .05, off=4.05, dur=.5, fi=.03, fo=.2)                                           # pase
put(sfx, CA, T(84) - .05, .07)                                                                           # nadie bota
put(sfx, CA, T(86) + .05, .05)                                                                           # halo en el 11
for i, o in enumerate([19.0, 20.7, 21.85]): put(sfx, SQ, T(92) + i * .32, .05, off=o - .03, dur=.3, fo=.12)   # huellas del remate, bajas
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT)      # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(OUT * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(OUT * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
