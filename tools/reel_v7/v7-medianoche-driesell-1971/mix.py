"""Mezcla v7 · El primer minuto (Lefty Driesell, Maryland, 15/10/1971) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», encadenada consigo misma con fundidos de 1,4 s; distinta de las dos últimas v7, que usaron la «Logo 01» y la «Logo 03»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-salto-inicial-mcguire-1957/mix.py.
La voz acaba en 24,58 s; remate quieto; fundido a negro 25,18–25,68 s; outro2 (4 s, con su voz) desde 25,68 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.68; DUR = OUT + 4.0
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
# música: la misma pista tres veces, fundidos de 1,4 s (misma tonalidad)
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
for i in range(3):
    put(mus, M, at, 1.0, fi=(.3 if i == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .45 * np.clip((tt - E(40) + .05) / .2, 0, 1) * np.clip((T(41) + .2 - tt) / .3, 0, 1)   # casi silencio tras «sin focos»
env *= 1 + .3 * np.clip((tt - 22.9) / .5, 0, 1) * np.clip((24.4 - tt) / .5, 0, 1)                  # sube 1 s con el remate
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                        # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); TI = pk(ld('tick.mp3'))
PA = pk(ld('paper.mp3')); SW = pk(ld('switch.mp3')); CA = pk(ld('car.mp3')); CR = pk(ld('crowd.mp3')); CK = pk(ld('click.mp3')); RU = pk(ld('run.mp3'))
for f in [3.2, 9.3, 11.8, 19.1, 21.2]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
TK = TI[:int(.25 * SR)]                                                                  # un tic del reloj
for x in [T(7), T(9)]: put(sfx, TK, x - .02, .10, fo=.08)                                # las agujas llegan a las 00:03
put(sfx, PA, T(13) + .3, .10)                                                            # la hoja del calendario cae
put(sfx, SL, T(19) - .12, .06)                                                           # reglamento
put(sfx, MK, T(22) - .05, .05, dur=.6, fi=.05, fo=.25)                                   # el rotulador rodea el 15
put(sfx, SH, 10.05 - 1.55, .07, dur=2.2, fo=.2)                                          # foto de Driesell (obturador a 10,05)
put(sfx, SL, T(25), .05)                                                                 # ficha de prensa
put(sfx, MK, T(30), .05, off=1.0, dur=.4, fi=.03, fo=.15)                                # se tacha la mañana
put(sfx, SL, 12.55, .07)                                                                 # postal del estadio
put(sfx, RU, T(33), .045, off=.75, dur=19.0 - T(33), fi=.4, fo=.8)                       # pasos de carrera, lejanos
put(sfx, CK, T(35) - .1, .16)                                                            # clic del cronómetro
for i in range(4): put(sfx, SW, T(39) + .12 * i + .05, .07 - .01 * i)                    # las torres se apagan una a una
put(sfx, CA, T(41) + .1, .06, dur=2.4, fi=.1, fo=.8)                                     # coche que arranca, lejos y bajo
put(sfx, CR, T(47) - .2, .07, off=10, dur=19.2 - T(47) + .2, fi=.5, fo=.6)               # murmullo de estudiantes al aire libre
put(sfx, SL, 19.9, .06)                                                                  # portada
put(sfx, TK, T(60) - .02, .12, fo=.08)                                                   # remate: un solo tic
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
