"""Mezcla de v7-alfombra-bennett-umbc-2018 (sandbox de Higgsfield, con los mp3 de Epidemic Sound ya descargados).
Plantilla: tools/reel_v7/wooden/mix.py. python3 mix.py voz11.mp3 outro2.wav out.wav
La voz es la toma de ElevenLabs a 1,1× (atempo, 25,3 s); words.js sale de esa versión."""
import sys, subprocess, numpy as np
SR = 48000; XF = 26.1; DUR = XF + 4.0
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); out = np.zeros((N, 2))
def cut(x, off=0, dur=None, fi=0.0, fo=0.0, norm=True):
    x = x[int(off * SR):]; x = (x[:int(dur * SR)] if dur else x).copy()
    if norm: x /= np.abs(x).max() + 1e-9
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    return x
def put(buf, x, at, g=1.0):
    i = int(at * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
# música: Epidemic «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde 9 s, sin cortes
put(mus, cut(ld('music.mp3'), off=9.0, dur=DUR, fi=.8, fo=2.0, norm=False), 0.0)
t = np.arange(N) / SR
env = np.ones(N)
env *= 1 + 0.4 * np.clip((t - 24.4) / .4, 0, 1) * np.clip((25.6 - t) / .5, 0, 1)   # sube 1 s con «Se usa»
env *= np.interp(t, [0, XF, XF + 1.5, DUR], [1, 1, .45, .3])                       # baja bajo el cierre
mus *= env[:, None]
# efectos reales, bajos (Epidemic Sound)
W, RP, PA, GE, CL, CU, MK, SW, PG, NE = [ld(f) for f in ('whoosh.mp3', 'rip.mp3', 'paper.mp3', 'gear.mp3', 'cloth.mp3', 'cutlery.mp3', 'marker.mp3', 'switch.mp3', 'page.mp3', 'net.mp3')]
for f in (2.72, 8.38, 11.32, 14.50, 19.32, 22.14): put(sfx, cut(W, fi=.05, fo=.4), f - .1, .08)   # viajes
put(sfx, cut(RP), 1.37, .12)                                            # el «1» se raja en «perdido»
put(sfx, cut(PA), 2.95, .10)                                            # postal de Charlotte
put(sfx, cut(GE, off=.1, dur=.6, fo=.2), 6.82, .06)                     # marcador 74
put(sfx, cut(GE, off=1.5, dur=.45, fo=.15), 7.90, .05)                  # marcador 54
put(sfx, cut(PA), 8.85, .10)                                            # ficha de Bennett
put(sfx, cut(CL, dur=.4, fi=.05, fo=.2), 10.50, .08)                    # la ficha va hacia la alfombra (corto: no tapa «alfombra»)
put(sfx, cut(CL, off=.3, dur=.6, fo=.3), 11.35, .06)                    # y vuelve a la vista
put(sfx, cut(PA), 12.0, .09); put(sfx, cut(PA), 12.19, .07)             # fichas de Jerome y Bennett
put(sfx, cut(CU), 12.34, .08)                                           # mesa
put(sfx, cut(MK, off=.1, dur=.45, fo=.15), 13.68, .09)                  # flecha 1
put(sfx, cut(MK, off=2.5, dur=.45, fo=.15), 14.26, .09)                 # flecha 2
put(sfx, cut(SW, off=.75, dur=.6, fo=.2), 15.14, .10)                   # la pantalla se enciende
put(sfx, cut(PA), 15.78, .09)                                           # foto del banquillo
put(sfx, cut(PG), 19.99, .10)                                           # 2018 → 2019
put(sfx, cut(GE, off=2.8, dur=.6, fo=.2), 20.98, .06)                   # marcador 85–77
put(sfx, cut(NE), 21.78, .10)                                           # la red cae
put(sfx, cut(CL, dur=.8, fo=.3), 22.70, .07)                            # la ficha sobre la alfombra (una vez)
# voz y cierre (outro2.mp4 trae su voz: «¿Te ha servido? Dale like…»)
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
o2 = ld(sys.argv[2]); o2 *= 10 ** ((-20 - 20 * np.log10(np.sqrt((o2 ** 2).mean()) + 1e-12)) / 20)   # el cierre, a la sonoridad de la voz
put(out, o2, XF)
put(out, cut(ld('sting.mp3'), dur=4.0, fi=.05, fo=1.2), XF, .22)
e = np.abs(vox[:, 0]); hop = 480; en = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
en = np.minimum(1, en / (np.percentile(en[en > 0], 90) + 1e-9)); sm = np.zeros_like(en)
for i in range(1, len(en)): a = .45 if en[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (en[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(25 * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg + out
mix /= max(1, np.abs(mix).max() / .9)
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
