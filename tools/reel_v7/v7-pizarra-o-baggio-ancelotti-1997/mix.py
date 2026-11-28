"""Mezcla v7 · La pizarra o Baggio (Ancelotti, Parma 1997) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», encadenada consigo misma con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-servilleta-rexach-2000/mix.py.
La voz acaba en 25,94 s; remate quieto hasta 26,9 s; fundido a negro 26,9–27,4 s; outro2 (4 s, con su voz) desde 27,4 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 26.9; CL = 27.4; DUR = CL + 4.0
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
env *= 1 + .2 * np.clip((tt - 14.0) / .5, 0, 1) * np.clip((16.9 - tt) / .6, 0, 1)             # re-hook: sube un poco
env *= 1 - .2 * np.clip((tt - 23.3) / .5, 0, 1)                                                # remate: baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                  # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3', 2)[int(5.0 * SR):int(6.4 * SR)]); ST = pk(ld('stamp.mp3')); PI = pk(ld('piece.mp3'))
MK = pk(ld('marker.mp3')); CK = pk(ld('click.mp3')[:int(.3 * SR)]); SH = pk(ld('shutter.mp3')); CL_ = pk(ld('cloth.mp3'))
for f in [2.5, 5.55, 11.02, 14.0, 18.62, 20.95, 22.95]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, ST, T(3) - .02, .14)                                                # sello «NO» (gancho)
put(sfx, SH, T(7) - .25 - 1.55, .08, off=0, dur=2.3, fo=.3)                 # polaroid del Tardini (el clic cae en 3,0 s)
for k, n in [(15, 5), (16, 4), (17, 2)]:                                     # fichas que se colocan, fila a fila
    for i in range(n): put(sfx, PI, T(k) - .05 + i * .04 + .12, .045)
put(sfx, PI, T(26) + .1, .08)                                                # la ficha 10 rebota y se queda fuera
put(sfx, PA, T(28) - .1, .09, dur=1.0, fi=.05, fo=.3)                        # foto de Baggio en Bolonia
for i in range(11): put(sfx, CK, T(32) + (E(33) + .05 - T(32)) * (2 * i + 1) / 22, .035)   # contador (uno de cada dos goles)
put(sfx, PA, T(37) - .35, .09, dur=1.0, fi=.05, fo=.3)                       # Ancelotti grande
put(sfx, CL_, T(44) - .12, .08, off=.05, dur=.8, fo=.3)                      # la camiseta se posa
for i in range(3): put(sfx, PI, T(50) + .1 + i * .12, .06)                   # las fichas se reordenan
put(sfx, MK, T(50) + .1, .06, off=1.2, dur=.5, fi=.03, fo=.15)              # flechas de rotulador
put(sfx, MK, T(51), .06, off=3.0, dur=.45, fi=.03, fo=.15)
put(sfx, ST, T(56) + .02, .12)                                               # sello «NO» otra vez
put(sfx, MK, T(60) - .05, .08, off=4.4, dur=.45, fi=.03, fo=.15)             # tachón
put(sfx, MK, T(66) - .05, .05, off=2.0, dur=.4, fi=.03, fo=.15)              # la pizarra se vuelve a dibujar
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
