"""Mezcla de v7-cinco-a-la-vez-grinnell-1993 (sandbox de Higgsfield, con los mp3 de Epidemic Sound ya descargados).
Plantilla: tools/reel_v7/wooden/mix.py. python3 mix.py voz11.mp3 outro2.wav out.wav
La voz es la toma de ElevenLabs a 1,12× (atempo, 25,05 s); words.js sale de esa versión.
El cierre (outro2) entra a los 26,2 s: «nivel» acaba a 24,72 s, quieto 1,0 s, fundido a negro de 0,5 s."""
import sys, subprocess, numpy as np
SR = 48000; XF = 26.2; DUR = XF + 4.0
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
# música: Epidemic «Musical, Loop, Calm Piano, Dreamy, Intro» 01 → 02 → 03 → 01, encadenadas con fundidos de 1,4 s (sin cortes)
M = [ld(f) for f in ('m1.mp3', 'm2.mp3', 'm3.mp3', 'm1.mp3')]; at = 0.0
for k, m in enumerate(M):
    put(mus, cut(m, fi=(.8 if k == 0 else 1.4), fo=1.4, norm=False), at); at += len(m) / SR - 1.4
t = np.arange(N) / SR
env = np.ones(N)
env *= 1 + 0.3 * np.clip((t - 22.6) / .5, 0, 1) * np.clip((25.4 - t) / .6, 0, 1)    # sostiene el remate
env *= np.interp(t, [0, XF - .5, XF + 1.5, DUR], [1, 1, .45, .3])                   # baja bajo el cierre
mus *= env[:, None]
# efectos reales, bajos (Epidemic Sound)
WH, TK, CK, TI, PA, MK, ST, SQ, GE = [ld(f) for f in ('whoosh.mp3', 'token.mp3', 'click.mp3', 'tick.mp3', 'paper.mp3', 'marker.mp3', 'stamp.mp3', 'squeak.mp3', 'gear.mp3')]
for f in (3.05, 6.95, 10.25, 13.55, 17.08, 18.85, 22.3): put(sfx, cut(WH, fi=.05, fo=.4), f - .1, .08)   # viajes
put(sfx, cut(WH, fi=.1, fo=.4), 16.05, .045)                            # empuje hacia la canasta
put(sfx, cut(TK, dur=.9, fo=.3), 1.55, .10)                             # salen cinco, entran cinco («vez»)
put(sfx, cut(TK, off=2.0, dur=.8, fo=.3), 2.62, .08)                    # y otra vez («minuto»)
put(sfx, cut(CK), 1.82, .12)                                            # cronómetro
put(sfx, cut(TI, off=1.0, dur=.8, fi=.05, fo=.3), 2.34, .06)            # tic mientras se dibuja la vuelta
put(sfx, cut(PA), 3.35, .10)                                            # postal de Grinnell
put(sfx, cut(PA), 4.70, .08)                                            # ficha de Arseneault
put(sfx, cut(PA), 7.35, .10)                                            # recorte de 1925
put(sfx, cut(MK, off=.1, dur=.95, fo=.25), 8.08, .08)                   # se tachan las 25 casillas
put(sfx, cut(PA), 10.95, .08)                                           # pizarra
put(sfx, cut(TK, off=.2, dur=.7, fo=.3), 12.10, .07)                    # las fichas llenan las columnas
put(sfx, cut(MK, off=2.5, dur=.8, fo=.25), 13.22, .08)                  # flechas de turno
put(sfx, cut(SQ, off=5.0, dur=1.3, fi=.2, fo=.5), 13.98, .05)           # presión: zapatillas lejanas
put(sfx, cut(PA), 15.40, .09)                                           # foto de Taylor
put(sfx, cut(ST), 16.86, .14)                                           # sello «BANDEJA LIBRE»
put(sfx, cut(GE, off=.1, dur=1.0, fo=.3), 17.50, .05)                   # barras de minutos
put(sfx, cut(PA), 17.80, .07)                                           # panel de minutos
put(sfx, cut(PA), 19.55, .07)                                           # clasificación
put(sfx, cut(GE, off=2.0, dur=.9, fo=.3), 19.62, .06)                   # Grinnell sube al 1.º
put(sfx, cut(MK, off=4.0, dur=.7, fo=.25), 21.42, .07)                  # trofeo dibujado
put(sfx, cut(TK, off=.5, dur=.8, fo=.3), 22.75, .07)                    # las quince fichas
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
