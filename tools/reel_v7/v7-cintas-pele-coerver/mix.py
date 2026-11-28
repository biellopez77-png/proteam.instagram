"""Mezcla v7 · Las cintas de Pelé (Wiel Coerver) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s;
distinta de la del último v7, que usó la «Logo 01») + SFX reales bajos + voz (ElevenLabs, Mateo). Base: v7-siete-segundos-dantoni/mix.py.
La voz acaba en 22,4 s; remate quieto hasta 23,4 s; fundido a negro 23,4–23,9 s; outro2 (4 s, con su voz) desde 23,9 s,
con el sting «Logo, Calm, Piano 01» bajo; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.9; DUR = OUT + 4.0
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
env *= 1 - .15 * np.clip((tt - 19.1) / .4, 0, 1) * np.clip((21.5 - tt) / .4, 0, 1)            # baja un poco en «El regate no es solo un don»
env *= 1 + .3 * np.clip((tt - 21.6) / .5, 0, 1) * np.clip((22.9 - tt) / .5, 0, 1)             # sube 1 s con «se enseña»
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); TI = pk(ld('tick.mp3'))
VH = pk(ld('vhs.mp3')); CA = pk(ld('card.mp3')); BK = pk(ld('book.mp3')); STG = pk(ld('sting.mp3'))
for f in [8.05, 13.42, 19.12]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)              # aire en cada viaje
put(sfx, SL, T(6) - .15, .07)                                   # la foto de Coerver se aparta
put(sfx, SL, T(9) - .2, .05)                                    # entra el televisor
put(sfx, VH, T(12) - .85, .12, fo=.2)                           # la cinta entra en el vídeo (golpe en T(12)+0,1)
put(sfx, SH, T(15) - .15, .07, off=1.6, dur=.8, fo=.3)          # ficha de prensa
put(sfx, SL, T(18) - .2, .1)                                    # hoja del calendario 1974
put(sfx, SL, T(17) - .2, .05)                                   # marcador
for i in range(7): put(sfx, CA, T(19) - .05 + i * .2 - .23, .045, fo=.1)   # la pila de cintas
put(sfx, TI, T(19), .05, off=.3, dur=1.5, fi=.05, fo=.4)       # reloj
for i in range(4): put(sfx, CA, T(28) - .15 + i * .16 - .2, .07, fo=.1)    # cuatro fotogramas, como cartas
put(sfx, SH, 14.05, .08, off=1.6, dur=.8, fo=.3)               # polaroid del libro
put(sfx, BK, T(36) + .02, .1)                                   # la portada se posa
for i, t0 in enumerate([T(38), T(40), T(43), T(44)]): put(sfx, MK, t0 - .05, .035, off=.4 + i * .8, dur=.4, fi=.03, fo=.15)   # rotulador: la pirámide se llena
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
sr = np.sqrt((STG[:int(3 * SR)] ** 2).mean()); put(mus, STG * (10 ** (-33 / 20) / sr), OUT, 1.0, dur=4.0, fi=.05, fo=1.2)   # sting del cierre, bajo (≈ −33 dB, bajo la música)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .89)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
