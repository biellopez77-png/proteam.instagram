"""Mezcla v7 · Antes, caballo (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Wind, Reveal, Strings, Dark Piano 01» y «… 02», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-golpe-ciento-uno-spurs/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.75; DUR = OUT + 5.61   # la voz acaba en 21,68 s; a 21,75 empieza el fundido de 0,6 s al cierre
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
M1, M2 = ld('mus1.mp3'), ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, fi=.3, fo=1.4)
put(mus, M2, len(M1) / SR - 1.4, 1.0, dur=OUT + 1.6 - (len(M1) / SR - 1.4), fi=1.4, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .25 * np.clip((tt - T(33)) / .5, 0, 1) * np.clip((T(40) - tt) / .6, 0, 1)   # la prensa duda: baja un poco
env *= 1 + .3 * np.clip((tt - E(47)) / .3, 0, 1) * np.clip((T(48) + .2 - tt) / .3, 0, 1)  # pausa antes del remate: solo música
env *= 1 + .3 * np.clip((tt - T(52)) / .6, 0, 1) * np.clip((OUT + .5 - tt) / .8, 0, 1)   # sube 1 s en «caballo» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); LD = pk(ld('lid.mp3')); CA = pk(ld('card.mp3')); ST = pk(ld('stamp.mp3'))
MK = pk(ld('marker.mp3')); SG = pk(ld('sign.mp3')); NW = pk(ld('news.mp3')); SH = pk(ld('shutter.mp3')); HO = pk(ld('horse.mp3'))
for f in [2.95, 4.77, 9.4, 12.95, 16.08, 17.56]: put(sfx, WH, f - .1, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, PA, 0.02, .09)                         # ficha de Sacchi
put(sfx, PA, T(2) - .1, .12)                    # postal de Fusignano
put(sfx, LD, T(3) - .12, .14)                   # la caja de zapatos se abre
put(sfx, CA, T(10) - .05, .1)                   # ficha de jugador
put(sfx, ST, T(13) + .08, .2)                   # sello AMATEUR
put(sfx, MK, T(19), .06, dur=1.4, fi=.1, fo=.4) # cuadro de la Copa
put(sfx, CA, T(23) + .2, .14)                   # 1-0 grupos
put(sfx, CA, T(24) + .45, .14)                  # 1-0 eliminatoria
put(sfx, PA, T(29) - .15, .1)                   # San Siro
put(sfx, PA, T(30) - .2, .1)                    # contrato
put(sfx, SG, T(30) + .3, .13)                   # firma
for i, k in enumerate([33, 34, 35]): put(sfx, NW, T(k) + (-.0 if i == 0 else .2), .15)   # periódicos
put(sfx, CA, T(35) + .25, .08)                  # ficha pequeña
put(sfx, SH, T(40) - .12, .08)                  # «Sacchi respondió»: clic suave
put(sfx, MK, T(42), .05, off=2.0, dur=1.6, fi=.2, fo=.5)   # dibujo del jinete
put(sfx, HO, T(52) + .3, .06, fo=.2)            # el caballo, muy bajo
put(sfx, PA, T(52) + .15, .06)                  # la Copa
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
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
