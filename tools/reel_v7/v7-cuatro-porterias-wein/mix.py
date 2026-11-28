"""Mezcla v7 · Cuatro porterías (Horst Wein) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 01», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-salon-de-bingo-hurley/mix.py.
La voz acaba en 24,44 s; remate quieto hasta 25,6 s; fundido a negro 25,6–26,1 s; outro2 (4 s, con su voz) desde 26,1 s;
la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.6; CL = 26.1; DUR = CL + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
FL = [4.15, 10.12, 13.05, 17.0, 21.12]
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
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
while at < DUR:
    put(mus, M, at, 1.0, fi=(.3 if at == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .2 * np.clip((tt - 13.1) / .5, 0, 1) * np.clip((16.9 - tt) / .6, 0, 1)             # re-hook: sube un poco
env *= 1 + .25 * np.clip((tt - 22.6) / .4, 0, 1) * np.clip((24.6 - tt) / .8, 0, 1)            # remate: sube y baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                  # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); GO = pk(ld('goal.mp3')); BA = pk(ld('ball.mp3'))
ME = pk(ld('medal.mp3')); ST = pk(ld('stamp.mp3')); CH = pk(ld('chip.mp3')); MK = pk(ld('marker.mp3'))
for f in FL: put(sfx, WH, f - .05, .06, dur=1.3, fi=.05, fo=.4)                                 # aire en cada viaje
for i in range(4): put(sfx, GO, T(10) + .12 + i * .2, .07, dur=.5, fo=.1)                       # caen las cuatro miniporterías
put(sfx, PA, T(8) - .1, .05, fo=.2)                                                              # entra el stick
put(sfx, PA, FL[0] + .35, .08, fo=.2)                                                            # Wein llega a la pared
put(sfx, CH, T(13), .03)                                                                         # ficha de prensa
put(sfx, ME, T(19) - .05, .08, fo=.2)                                                            # la medalla
put(sfx, BA, T(28) - .05, .08, off=.5, dur=.6, fo=.2)                                           # el balón bota una vez
put(sfx, PA, FL[1] + .35, .06, fo=.2)                                                            # el campo
for i in range(3): put(sfx, CH, T(29) + i * .08, .035)                                           # tres fichas azules
for i in range(3): put(sfx, CH, T(31) + i * .08, .035)                                           # tres blancas
put(sfx, MK, T(35) - .05, .07, fo=.1)                                                            # la zona de tiro
put(sfx, PA, FL[2] + .3, .07, fo=.2)                                                             # re-hook: la banda
for i in range(3): put(sfx, PA, T(45) + i * .2, .035, fo=.2)                                     # tres preguntas
put(sfx, PA, T(49) - .25, .07, fo=.2)                                                            # foto de los niños
put(sfx, PA, T(50) - .1, .06, fo=.2)                                                             # ficha DFB
put(sfx, ST, T(54), .12)                                                                         # sello OBLIGATORIO
put(sfx, PA, FL[4] + .35, .05, fo=.2)                                                            # el campo del remate
put(sfx, MK, T(57), .05, fo=.1)                                                                  # se redibuja la zona
for i in range(3): put(sfx, CH, T(63) + .5 + i * .09, .03)                                       # las fichas se abren
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
