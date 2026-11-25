"""Mezcla v7 · Un libro para cada jugador (Phil Jackson y Shaq) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 01», desde 0,65 s para que su acorde final caiga justo después de «jugador»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-carteles-herrera/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de wt.py, con «O'Neal» unido como en words.js)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 20.5; DUR = OUT + 5.61   # la voz acaba en 20,22 s; a 20,5 empieza el fundido de 0,6 s al cierre
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
put(mus, ld('mus.mp3'), 0.0, 1.0, off=.65, dur=OUT + 2.2, fi=.4, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(49)) / .2, 0, 1) * np.clip((T(50) + .2 - tt) / .2, 0, 1)   # pausa antes del remate: solo música
env *= 1 + .35 * np.clip((tt - (E(53) - .1)) / .3, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # el acorde final sube 1 s y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); CA = pk(ld('cabin.mp3')); BK = pk(ld('book.mp3')); FL = pk(ld('flip.mp3')); TU = pk(ld('turn.mp3'))
BU = pk(ld('bus.mp3')); WS = pk(ld('whistle.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
ST = pk(ld('stamp.mp3')); CD = pk(ld('card.mp3'))
for f in [1.28, 3.98, 6.2, 8.4, 10.36, 14.58, 16.74]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, CA, 0.0, .07, off=20, dur=2.4, fi=.3, fo=.9)          # cabina del avión, lejana
put(sfx, SL, T(3) - .1, .08)                                   # tarjeta de embarque
put(sfx, SH, T(5) - .35, .07)                                  # foto de Phil Jackson
put(sfx, SL, T(6) - .05, .06)                                  # ficha PHIL JACKSON
for i in range(5): put(sfx, BK, T(8) + i * .13 + .3, .07 - .006 * i)   # un libro en cada asiento
put(sfx, BK, T(12) - .35, .08)                                 # la balda
for i in range(7): put(sfx, CD, T(13) + i * .09, .045)        # fichas con dorsal
put(sfx, SL, T(15) - .05, .06)                                 # 1 LIBRO = 1 JUGADOR
put(sfx, SH, T(17) - .35, .07)                                 # foto de Shaq
put(sfx, SL, T(19) - .05, .06)                                 # ficha SHAQUILLE O'NEAL
put(sfx, FL, T(22) - .15, .09, dur=1.2, fo=.3)                 # Ecce Homo: páginas
put(sfx, CD, T(22) + .35, .05)                                 # etiqueta «para Shaq»
put(sfx, TU, T(25) - .08, .09)                                 # hoja del calendario
put(sfx, SL, T(26) - .3, .08); put(sfx, CD, T(26) + .3, .05)  # Siddhartha y su etiqueta
put(sfx, BU, T(27) - .3, .06, dur=2.4, fi=.05, fo=.6)          # puerta del autobús, suave
put(sfx, WS, T(33) + .2, .05)                                  # silbato corto y lejano
put(sfx, ST, T(35) + .05, .1)                                  # EXPULSADO
put(sfx, SL, T(36) - .2, .08)                                  # la hoja del resumen
put(sfx, MK, T(38) - .1, .07, off=.4, dur=2.0, fi=.03, fo=.3)  # rotulador, renglón a renglón
put(sfx, ST, T(42) + .15, .14)                                 # sello N.º 1 · EL ÚNICO
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
