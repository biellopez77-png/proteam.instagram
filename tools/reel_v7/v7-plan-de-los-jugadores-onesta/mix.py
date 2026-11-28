"""Mezcla v7 · El plan de los jugadores (Onesta, Francia 2001–2016) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-pizarra-o-baggio-ancelotti-1997/mix.py.
La voz acaba en 26,08 s; remate quieto hasta 27,05 s; fundido a negro 27,05–27,55 s; outro2 (4 s, con su voz) desde 27,55 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 27.05; CL = 27.55; DUR = CL + 4.0
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
env *= 1 + .2 * np.clip((tt - 14.2) / .5, 0, 1) * np.clip((16.6 - tt) / .6, 0, 1)             # re-hook: sube un poco
env *= 1 - .2 * np.clip((tt - 22.3) / .6, 0, 1)                                                # remate: baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                  # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')[int(.15 * SR):int(1.3 * SR)]); ST = pk(ld('stamp.mp3')); PI = pk(ld('piece.mp3'))
MK = pk(ld('marker.mp3')); SP = pk(ld('sponge.mp3')); MD = pk(ld('medal.mp3'))
for f in [3.0, 7.6, 14.05, 18.6, 22.0]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)    # aire en cada viaje
for i, o in enumerate([1.45, 3.62, 5.0]): put(sfx, MK, T(7) - .05 + i * .16, .07, off=o, dur=.4, fi=.03, fo=.15)   # gancho: tres trazos cortos
put(sfx, PA, 3.4, .10, fi=.05, fo=.3)                                        # Onesta llega a la pared
put(sfx, PI, T(12) - .05, .05)                                               # ficha de prensa
put(sfx, PA, 7.9, .06, fi=.05, fo=.3)                                        # pizarra de la tríada
put(sfx, MK, T(20) - .02, .07, off=1.45, dur=.45, fi=.03, fo=.15)           # proponían: flecha
put(sfx, SP, T(21) - .05, .08, dur=.3, fo=.1)                                # corregían: borrador
put(sfx, MK, T(21) + .15, .07, off=3.62, dur=.4, fi=.03, fo=.15)            # …y otra flecha
put(sfx, PI, T(23) + .3, .07)                                                # probaban: la ficha se mueve
put(sfx, PA, T(27) - .05, .06, fi=.05, fo=.3)                                # la ficha de Onesta, a un lado
put(sfx, PA, 14.7, .11, fi=.03, fo=.3)                                       # re-hook: Onesta vuelve, firme
for i in range(7): put(sfx, PI, T(41) - .05 + i * .03, .03)                 # las fichas del corro
put(sfx, ST, T(45) + .02, .14)                                               # sello «DECIDE»
for k in (49, 51, 54): put(sfx, MD, T(k) + .02, .06)                         # tres toques metálicos muy bajos
put(sfx, PA, 22.3, .05, fi=.05, fo=.3)                                       # pizarra del remate
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
