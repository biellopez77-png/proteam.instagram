"""Mezcla v7 · Alinea el momento (Ramsey, Hurst y Greaves, Mundial de 1966) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: v7-comba-mikan-1942/mix.py.
La voz acaba en 25,22 s; remate quieto; fundido a negro 26,3–26,8 s; outro2 (4 s, con su voz) desde 26,8 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 26.8; DUR = OUT + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
FL = [1.98, 7.62, 10.12, 14.55, 20.35, 22.28]   # viajes de cámara (reel.html)
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
env *= 1 + .3 * np.clip((tt - 24.3) / .5, 0, 1) * np.clip((25.9 - tt) / .5, 0, 1)             # sube 1 s con el remate
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                   # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
KI = pk(ld('kick.mp3')); CH = pk(ld('chips.mp3')); STP = pk(ld('stamp.mp3')); PL = pk(ld('plate.mp3')); CR = pk(ld('crowd.mp3'))
for f in FL: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)    # aire en cada viaje
put(sfx, KI, .05, .06, dur=.5, fo=.3)                               # el balón de la final rueda un palmo
put(sfx, SH, 2.6, .07, off=1.55, dur=.5, fo=.2)                     # foto de Greaves
put(sfx, CH, T(10) - .18, .07)                                      # 43 fichas caen en la rejilla
put(sfx, STP, T(20) + .0, .14)                                      # sello LESIÓN
put(sfx, SH, 10.7, .06, off=1.55, dur=.5, fo=.2)                    # foto de Hurst
put(sfx, SL, T(27) - .2, .05)                                       # etiqueta del debut
put(sfx, MK, T(31) - .1, .05, off=.1, dur=.6, fi=.03, fo=.2)        # trayectoria del cabezazo
put(sfx, PL, T(34) - .1, .05, dur=.5, fo=.2)                        # marcador 1–0
put(sfx, MK, T(41) - .05, .04, off=.75, dur=.35, fi=.03, fo=.15)    # ✓ de «sano»
put(sfx, SH, 17.3, .06, off=1.55, dur=.5, fo=.2)                    # foto de Ramsey
put(sfx, SL, T(44) - .05, .05)                                      # la ficha de Greaves va al banquillo
for i in range(3): put(sfx, KI, T(47) + i * .3 - .02, .045, dur=.45, fo=.25)   # tres balones
put(sfx, PL, T(49) - .1, .05, dur=.5, fo=.2)                        # marcador 4–2
put(sfx, MK, T(50) + .1, .035, off=1.1, dur=1.2, fi=.1, fo=.4)      # la copa se dibuja
put(sfx, CR, T(50) - .1, .05, off=5.0, dur=2.3, fi=.4, fo=.9)       # murmullo de grada, muy bajo
put(sfx, PL, T(51) + .05, .04, dur=.5, fo=.2)                       # placa de Wembley
put(sfx, MK, T(55) - .05, .06, off=.75, dur=.45, fi=.03, fo=.15)    # «GREAVES» tachado
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
mix /= max(1, np.abs(mix).max() / .8)          # pico ≤ −1,9 dBFS (true peak ≤ −1 dBTP)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
