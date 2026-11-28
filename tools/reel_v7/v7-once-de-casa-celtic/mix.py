"""Mezcla v7 · Los once de casa · r2 (28/11, Marta A). Se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound.
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», distinta a la de la r1) + SFX reales bajos + voz (ElevenLabs, Mateo, eleven_v4).
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (words.json con los tiempos ya desplazados; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)
La voz lleva 0,35 s de silencio añadido en 17,50 s (pausa antes del remate «Antes de buscar lejos…»).
El vídeo: remate quieto hasta «cerca»+1,1 s, fundido a negro hasta «cerca»+1,6 s (OUT) y outro2.mp4 desde negro; su voz entra 0,3 s después (≥ 1,2 s tras «cerca»)."""
import sys, json, subprocess, numpy as np
SR = 48000
PAUSE_AT, PAUSE = 17.50, 0.35
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
OUT = E(50) + 1.6; DUR = OUT + 4.0
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
put(mus, ld('mus1.mp3'), 0.0, 1.0, dur=DUR, fi=.25, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(47)) / .6, 0, 1) * np.clip((OUT - .2 - tt) / .8, 0, 1)   # sube en «mira quién juega cerca»
env *= np.clip(1 - .55 * (tt - OUT + .5) / 2.0, .45, 1)                                     # y va bajando durante el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); ST = pk(ld('stamp.mp3')); CA = pk(ld('card.mp3')); CK = pk(ld('click.mp3'))
SH = pk(ld('shutter.mp3')); PE = pk(ld('pencil.mp3'))
F1, F2, F3, F4, F5 = E(10) - .08, E(16) + .12, T(23) - .1, E(34) + .02, E(42) + .06
for f in [F1, F2, F3, F4, F5]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, PE, T(6) - .05, .06, dur=E(7) - T(6) + .25, fi=.03, fo=.25)   # compás: círculo de 50 km
put(sfx, SL, T(10) - .1, .05)                            # foto pequeña de Celtic Park
put(sfx, PE, T(12) - .1, .05, dur=1.3, fi=.03, fo=.3)    # la copa se dibuja
put(sfx, SL, F2 + .5, .07)                               # la postal desliza
put(sfx, ST, T(18) - .02, .12)                           # matasellos
put(sfx, SH, T(19) - .35, .08)                           # foto de Jock Stein
put(sfx, SL, T(20) - .05, .05)                           # ficha de prensa
put(sfx, SL, F3 + .15, .05)                              # marcador
put(sfx, CK, T(24) - .05, .06, dur=.5, fo=.2)            # placas 0-1
put(sfx, CK, T(33) - .1, .07, dur=.5, fo=.2)             # 1-1
put(sfx, CK, T(34) - .1, .08, dur=.5, fo=.2)             # 2-1
put(sfx, CA, T(37) - .1, .09)                            # ficha CELTIC
put(sfx, ST, T(39) - .02, .11)                           # sello 1.º
put(sfx, PE, T(41), .05, dur=.7, fi=.03, fo=.2)          # subrayado
put(sfx, SH, F5 + .4, .06)                               # foto final
V = np.repeat(ld(sys.argv[1], 1), 2, 1); cut = int(PAUSE_AT * SR)
put(vox, V[:cut], 0.0); put(vox, V[cut:], PAUSE_AT + PAUSE)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…»
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .85)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('OUT %.2f  voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (OUT, R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
