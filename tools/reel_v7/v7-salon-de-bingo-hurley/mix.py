"""Mezcla v7 · Un salón de bingo (Bob Hurley, St. Anthony) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-plan-de-los-jugadores-onesta/mix.py.
La voz acaba en 22,88 s; remate quieto hasta 23,95 s; fundido a negro 23,95–24,45 s; outro2 (4 s, con su voz) desde 24,45 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.95; CL = 24.45; DUR = CL + 4.0
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
# música: la misma pista encadenada (misma tonalidad), fundidos de 1,4 s
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
while at < DUR:
    put(mus, M, at, 1.0, fi=(.3 if at == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .2 * np.clip((tt - 14.4) / .5, 0, 1) * np.clip((17.8 - tt) / .6, 0, 1)             # re-hook: sube un poco
env *= 1 + .25 * np.clip((tt - 21.2) / .4, 0, 1) * np.clip((22.6 - tt) / .8, 0, 1)            # remate: sube 1 s y baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                  # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); TR = pk(ld('trophy.mp3')); MK = pk(ld('marker.mp3'))
CH = pk(ld('chip.mp3')); TP = pk(ld('tape.mp3')); FD = pk(ld('folder.mp3')); CK = pk(ld('clock.mp3'))
for f in [4.22, 8.0, 14.45, 17.76, 20.72]: put(sfx, WH, f - .05, .06, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
for i, at in enumerate([.45, 1.1, 1.75]): put(sfx, TR, at, .06)                                  # trofeos: tres toques
put(sfx, MK, T(9) - .05, .08, fo=.1); put(sfx, MK, T(9) + .2, .07, fo=.1)                        # la cruz sobre el pabellón
put(sfx, PA, 4.7, .10, fo=.2)                                                                    # Hurley llega a la pared
put(sfx, CH, T(13) - .05, .035)                                                                  # ficha de prensa
put(sfx, PA, T(15) - .15, .06, fo=.2)                                                            # polaroid del instituto
put(sfx, PA, 8.65, .08, fo=.2)                                                                   # el salón
put(sfx, PA, T(25) - .1, .07, fo=.2)                                                             # cae el cartón de bingo
for i in range(2): put(sfx, CH, T(25) + .3 + i * .22, .07)                                       # dos fichas sobre el cartón
put(sfx, PA, T(26) - .25, .05, fo=.2)                                                            # la pista
put(sfx, TP, T(30), .09)                                                                         # cinta métrica que se recoge
put(sfx, CH, T(34), .03)                                                                         # el marcador, apagado
put(sfx, FD, T(38) - .1, .14)                                                                    # re-hook: el expediente cae
put(sfx, CK, T(40) - .1, .05, off=1.0, dur=1.9, fi=.05, fo=.4)                                  # reloj de oficina
put(sfx, PA, T(43) - .1, .06, fo=.2)                                                             # Hurley junto al expediente
put(sfx, PA, 18.4, .08, fo=.2)                                                                   # portada del Salón de la Fama
put(sfx, PA, 20.95, .05, fo=.2)                                                                  # la pista corta del remate
for i in range(5): put(sfx, CH, T(57) + i * .07, .03)                                            # las cinco fichas
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), CL)       # audio de outro2.mp4 («Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(CL * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(CL * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
