"""Mezcla v7 · La derrota del Dream Team (San Diego, 1992) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Wind, Reveal, Strings, Dark Piano 02», encadenada consigo misma con fundidos de 1,4 s; no usada en los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-camiseta-gris-ferguson/mix.py.
La voz se abre en tres silencios para que quepan los viajes de cámara: 6,45 (+0,5), 15,87 (+0,8) y 19,8 (+0,35, la pausa del remate);
words.json ya lleva esos desplazamientos.
r2 (28/11, crítica de Andrés 77/100): remate «DERROTA.» quieto hasta 25,35 s; fundido a negro 25,35–25,85 s; outro2 (4 s, con su voz) desde 25,85 s
(«¿Te ha servido? Dale like…» entra a ~26,15 s, 1,9 s después de «derrota»); la música sigue bajando bajo el cierre. La cámara se aleja a toda la pared desde 21,15 s.
La apertura de 15,87 s (voz original) cae entre «Jordan» y «y no hizo» (comprobado con whisper troceando la voz: 15,86–17,4 = «y no hizo ni un ajuste»).
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.35; OUT2 = OUT + .5; DUR = OUT2 + 4.0   # la voz acaba en 24,27 s; remate quieto hasta 25,35; fundido a negro de 0,5 s; outro2 desde 25,85
CUTS = [(6.45, .5), (15.87, .8), (19.8, .35)]
FLY = [2.12, 6.25, 11.12, 16.3, 21.15]   # el último es el alejamiento a toda la pared (1,6 s)
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
def on(x):   # quita el silencio inicial: el golpe cae justo en su tiempo
    i = int(np.argmax(np.abs(x).max(1) > .08 * np.abs(x).max())); return x[max(0, i - 240):]
M = ld('mus.mp3'); LM = len(M) / SR   # 12,3 s
at = 0.0; k = 0
while at < DUR:
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(43) - .3)) / .4, 0, 1) * np.clip((OUT + .4 - tt) / .8, 0, 1)   # sube en el remate y baja en el fundido
env *= 1 - .45 * np.clip((tt - OUT) / 1.0, 0, 1)   # bajo el cierre la música sigue, más baja
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); CA = pk(on(ld('card.mp3')))
CK = pk(on(ld('click.mp3'))); DR = pk(on(ld('drop.mp3'))); CP = pk(on(ld('cap.mp3'))); MK = pk(on(ld('marker.mp3')))
for f in FLY[:-1]: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, FLY[-1] - .2, .05, dur=1.9, fi=.3, fo=.6)            # alejamiento a toda la pared, más largo y suave
put(sfx, SL, 0.05, .07)                                         # el pase baja colgado del cordón
put(sfx, SH, FLY[0] + .45, .07, dur=1.0, fo=.3)                 # portada del Dream Team (obturador)
for k in [7, 8, 10]: put(sfx, CA, T(k), .10)                    # fichas JORDAN, MAGIC, BIRD
put(sfx, DR, T(11), .16)                                        # «pierde»: la portada cae sobre la mesa
put(sfx, SH, T(16) - .3, .06, dur=1.0, fo=.3)                   # Grant Hill en ficha
for a in [.25, .45, .65]: put(sfx, CA, T(16) + a, .08)          # HILL, WEBBER, HURLEY
for a in [T(17), T(17) + .22, T(19), T(19) + .18]: put(sfx, CK, a, .08, dur=.3, fo=.1)   # placas del marcador 6-2 / 5-4
put(sfx, SH, T(20) - .35, .06, dur=1.0, fo=.3)                  # Krzyzewski en ficha
put(sfx, SL, T(24) - .1, .05)                                   # se abre el bocadillo
put(sfx, SH, T(25) - .15, .06, dur=1.0, fo=.3)                  # Chuck Daly en ficha
put(sfx, SL, T(27) - .1, .06)                                   # banquillo
put(sfx, CA, T(30) - .1, .11)                                   # la ficha JORDAN se queda sentada
put(sfx, CP, T(35) - .05, .12)                                  # el rotulador llega con el capuchón puesto
put(sfx, MK, T(41) - .05, .08, dur=1.3, fi=.05, fo=.4)          # «PODÍAN PERDER» a mano, muy suave
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT2)      # audio de outro2.mp4 («¿Te ha servido? Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .84)   # true peak ≤ −1 dBTP
fo = int((DUR - .5) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
