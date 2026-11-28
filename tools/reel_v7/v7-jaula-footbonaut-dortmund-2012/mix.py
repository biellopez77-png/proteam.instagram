"""Mezcla v7 · La jaula del primer control (Borussia Dortmund, Footbonaut, 2012) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01», encadenada consigo misma con fundidos de 1,4 s; distinta de las últimas v7, que usaron las «Soft Piano, Strings, Calm, Intro, Logo 01/02/03»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-medianoche-driesell-1971/mix.py.
La voz acaba en 21,62 s; remate quieto; fundido a negro 22,7–23,2 s; outro2 (4 s, con su voz) desde 23,2 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.2; DUR = OUT + 4.0
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
# música: la misma pista cuatro veces, fundidos de 1,4 s (misma tonalidad)
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
for i in range(4):
    put(mus, M, at, 1.0, fi=(.3 if i == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(49) + .1) / .2, 0, 1) * np.clip((T(50) + .3 - tt) / .3, 0, 1)    # casi silencio en «entrena...»
env *= 1 + .3 * np.clip((tt - 20.9) / .5, 0, 1) * np.clip((22.4 - tt) / .5, 0, 1)                  # sube 1 s con el remate
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                        # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); TI = pk(ld('tick.mp3'))
FE = pk(ld('fence.mp3')); KI = pk(ld('kick.mp3')); TO = pk(ld('touch.mp3')); CH = pk(ld('chip.mp3')); BL = pk(ld('block.mp3')); CK = pk(ld('click.mp3'))
for f in [3.72, 12.05, 15.6, 17.68]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)    # aire en cada viaje
put(sfx, WH, 2.8, .05, dur=1.1, fi=.05, fo=.4)                                            # bajada corta a la polaroid
put(sfx, FE, T(8) - .08, .07, dur=1.6, fo=.6)                                             # rejilla metálica en «jaula»
put(sfx, SH, 3.08, .06, off=1.6, dur=.5, fo=.15)                                          # obturador: polaroid del estadio
put(sfx, SL, 3.12, .05)                                                                   # la polaroid se posa
put(sfx, MK, T(10) - .05, .05, off=.6, dur=.45, fi=.03, fo=.15)                           # cota «14 m»
put(sfx, MK, T(12) - .05, .05, off=1.5, dur=.45, fi=.03, fo=.15)                          # cota «14 m»
for i in range(16): put(sfx, CK, T(15) - .05 + i * .065, .035 - .0012 * i)               # las 72 casillas se encienden en cascada
put(sfx, SL, T(18) - .1, .05)                                                             # foto de la máquina
put(sfx, CH, T(19) + .02, .10)                                                            # la máquina dispara el balón
put(sfx, TO, E(21) - .03, .05)                                                            # el balón llega al jugador
put(sfx, CK, T(23), .09)                                                                  # se enciende una casilla
put(sfx, TO, T(26), .13)                                                                  # control
put(sfx, KI, T(28) - .75, .12, off=0.0, dur=1.25, fo=.3)                                  # golpeo (pico del mp3 a 0,8 s)
put(sfx, CK, T(28) + .33, .07)                                                            # la casilla recibe el balón
put(sfx, SL, 12.75, .07)                                                                  # el recorte llega a la pared
put(sfx, MK, E(38) - .05, .06, off=2.5, dur=.4, fi=.03, fo=.15)                           # se tacha el «20»
put(sfx, SL, 16.2, .05)                                                                   # ficha de Götze
for a in [T(42) + .25, T(42) + .62, T(44) + .18]: put(sfx, BL, a, .11)                    # tres bloques que se apilan
put(sfx, TI, T(49) - .02, .08, off=.98, dur=.25, fo=.08)                                  # un tic en la pausa
for i in range(0, 28, 3): put(sfx, CH, T(51) + i * .05 + .1, .03)                         # ráfaga de balones, muy baja
put(sfx, BL, T(54) + .28, .07)                                                            # el reloj de arena cae
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
