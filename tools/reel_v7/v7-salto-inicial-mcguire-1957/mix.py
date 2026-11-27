"""Mezcla v7 · El salto perdido (Frank McGuire, North Carolina, final NCAA 1957) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s; distinta de la del último v7, que usó la «Logo 01»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-siete-segundos-dantoni/mix.py.
La voz acaba en 26,9 s; remate quieto; fundido a negro 27,8–28,3 s; outro2 (4 s, con su voz) desde 28,3 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 28.3; DUR = OUT + 4.0
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
env *= 1 - .45 * np.clip((tt - 3.3) / .3, 0, 1) * np.clip((4.9 - tt) / .4, 0, 1)             # casi silencio en «uno ochenta»
env *= 1 + .3 * np.clip((tt - 26.2) / .5, 0, 1) * np.clip((27.4 - tt) / .5, 0, 1)             # sube 1 s con el remate
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); ST = pk(ld('stamp.mp3'))
TI = pk(ld('tick.mp3')); BO = pk(ld('bounce.mp3')); TA = pk(ld('tape.mp3'))
for f in [4.62, 8.3, 10.98, 13.62, 17.15, 20.4, 23.75]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, MK, T(6) - .05, .05, dur=.7, fi=.05, fo=.25)        # la columna de Chamberlain sube
put(sfx, SH, T(12) - .3, .07, off=1.55, dur=.5, fo=.2)       # Kearns entra
put(sfx, TA, E(15) - .4, .12)                                # la columna de Kearns se para en 1,80: cinta métrica
put(sfx, SL, 5.15, .09)                                      # programa de la NCAA
put(sfx, SL, T(20) - .15, .06)                               # rótulo Kansas City
put(sfx, SH, 8.85, .09, off=1.55, dur=.6, fo=.25)            # foto de Chamberlain
put(sfx, SH, 11.25, .07, off=1.55, dur=.5, fo=.2)            # foto de McGuire
put(sfx, MK, 11.7, .04, dur=.7, fi=.05, fo=.25)              # el círculo central se dibuja
put(sfx, BO, 12.0, .08, off=2.42, dur=.6, fo=.25)            # el balón en el centro
put(sfx, MK, T(28), .05, off=1.0, dur=.5, fi=.03, fo=.2)     # flecha de McGuire al círculo
put(sfx, SH, T(30) - .2, .06, off=3.1, dur=.5, fo=.2)        # Kearns cae en el círculo
put(sfx, SL, 13.95, .06)                                     # pista
put(sfx, ST, T(37) + .1, .13, off=.75, dur=.6, fo=.2)       # sello PERDIDO (golpe a T(37)+0,2)
put(sfx, MK, 16.4, .04, off=2.4, dur=.6, fi=.03, fo=.25)     # la cita, subrayado corto
put(sfx, SL, 17.55, .06)                                     # pizarra
for x in [T(41), T(42) + .05, T(43) + .05]: put(sfx, MK, x - .05, .05, off=.05, dur=.35, fi=.02, fo=.12)   # tres X
put(sfx, MK, T(44) - .05, .05, off=1.6, dur=.7, fi=.03, fo=.25)                                              # se cierran
put(sfx, SL, 20.9, .06)                                      # marcador
for x in [T(51), T(52), T(52) + .35]: put(sfx, TI, x - .05, .07, off=.95, dur=.25, fo=.1)                   # tres prórrogas
put(sfx, SL, 24.25, .05)                                     # remate: el círculo vuelve
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
