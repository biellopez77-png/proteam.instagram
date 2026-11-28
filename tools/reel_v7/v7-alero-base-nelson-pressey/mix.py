"""Mezcla v7 · Le dio el balón a un alero (Don Nelson y Paul Pressey) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 03», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-cuatro-porterias-wein/mix.py.
La voz acaba en 21,70 s; remate quieto hasta 22,9 s; fundido a negro 22,9–23,4 s; outro2 (4 s, con su voz) desde 23,4 s;
la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.9; CL = 23.4; DUR = CL + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
FL = [2.92, 6.28, 8.76, 12.62, 16.80]
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
def hits(x, th=.35, gap=.12):
    """Inicios (s) de los golpes de un archivo con varios (botes, recepciones)."""
    e = np.abs(x).max(1); m = e.max(); out = []; i = 0
    while i < len(e):
        if e[i] > th * m: out.append(max(0, i / SR - .01)); i += int(gap * SR)
        else: i += 1
    return out
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
while at < DUR:
    put(mus, M, at, 1.0, fi=(.3 if at == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .2 * np.clip((tt - 12.7) / .5, 0, 1) * np.clip((16.8 - tt) / .6, 0, 1)              # re-hook: sube un poco
env *= 1 + .25 * np.clip((tt - 19.3) / .4, 0, 1) * np.clip((21.9 - tt) / .8, 0, 1)             # remate: sube y baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
BO = pk(ld('bounce.mp3')); CA = pk(ld('catch.mp3')); SW = pk(ld('swish.mp3')); TA = pk(ld('tape.mp3'))
PE = pk(ld('pencil.mp3')); HO = pk(ld('sheet.mp3'))
b0 = hits(BO)[0]; c0 = hits(CA)[0]; p0 = hits(PE, .3)[0]
for f in FL: put(sfx, WH, f - .05, .06, dur=1.3, fi=.05, fo=.4)                                   # aire en cada viaje
put(sfx, BO, 0.02, .07, off=b0, dur=.35, fo=.15)                                                  # el balón bota junto al «1»
put(sfx, MK, T(1), .07, fo=.1)                                                                    # la flecha de rotulador
put(sfx, CA, T(13) - .03, .08, off=c0, dur=.4, fo=.15)                                            # el alero recibe el balón
put(sfx, SH, FL[0] + .35, .06)                                                                    # Nelson llega a la pared
put(sfx, PA, T(15) - .05, .05, fo=.2)                                                             # ficha de prensa
put(sfx, PA, T(19) - .1, .06, fo=.2)                                                              # el pabellón
put(sfx, PA, FL[1] + .35, .07, fo=.2)                                                             # Pressey
put(sfx, PA, T(26) - .05, .05, fo=.2)                                                             # ficha «ALERO»
put(sfx, TA, T(27), .08, fo=.2)                                                                   # la regla sube
put(sfx, PA, FL[2] + .3, .05, fo=.2)                                                              # la pizarra
for i in range(3): put(sfx, BO, T(33) + .05 + i * .33, .045, off=b0, dur=.3, fo=.12)              # tres botes bajos
put(sfx, MK, T(38), .05, fo=.1)                                                                   # cortes de los bases
put(sfx, SW, T(39) + .02, .07, fo=.3)                                                             # red: +2
put(sfx, HO, FL[3] + .3, .08, fo=.2)                                                              # re-hook: la hoja real
put(sfx, PA, T(44) - .1, .05, fo=.2)                                                              # tarjeta del contador
for i in range(7): put(sfx, PE, T(49) + i * .1, .04, off=p0, dur=.14, fo=.05)                     # siete marcas de lápiz
put(sfx, SH, T(54) - .1, .05)                                                                     # Pippen
put(sfx, MK, T(55), .045, fo=.1)                                                                  # la misma flecha
put(sfx, SH, T(56) - .1, .05)                                                                     # Giannis
put(sfx, PA, T(57) - .1, .05, fo=.2)                                                              # vuelve la pizarra
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), CL)       # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
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
