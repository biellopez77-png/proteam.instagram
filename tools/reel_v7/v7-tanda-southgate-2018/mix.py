"""Mezcla v7 · El que falló el penalti (Southgate) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01», «… 02» y «… 03», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: v7-puerta-de-atras-carril/mix.py y tools/reel_v7/wooden/mix.py.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)
La voz acaba en 22,4 s; todo quieto de 22,5 a 23,5 s; fundido a NEGRO 23,5–24,0 s; outro2 (4 s, con su voz) desde 24,0 s,
con su audio en el mismo instante; la música sigue bajando bajo el cierre. True peak ≤ −1 dBTP."""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.0; DUR = OUT + 4.0
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
M = [ld('mus1.mp3'), ld('mus2.mp3'), ld('mus3.mp3')]
at = 0.0; k = 0
while at < DUR:
    m = M[k % 3]; put(mus, m, at, 1.0, fi=(.3 if k == 0 else 1.4), fo=1.4); at += len(m) / SR - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .25 * np.clip((tt - T(49)) / .4, 0, 1) * np.clip((T(54) - tt) / .4, 0, 1)        # sube un poco en «primera»
env *= 1 - .25 * np.clip((tt - T(54)) / .3, 0, 1) * np.clip((T(61) - tt) / .3, 0, 1)        # baja en «lo que se entrena...»
env *= 1 + .3 * np.clip((tt - T(61)) / .3, 0, 1) * np.clip((23.9 - tt) / .8, 0, 1)          # sube 1 s en «lotería» y vuelve al fundido
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                 # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
TK = pk(ld('tick.mp3')); ST = pk(ld('stamp.mp3')); KI = pk(ld('kick.mp3')); TE = pk(ld('tear.mp3'))
for f, g in [(3.12, .06), (6.98, .08), (9.9, .07), (12.92, .08), (15.04, .08), (19.64, .07)]: put(sfx, WH, f - .05, g, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, KI, 0.0, .10, dur=.8, fo=.3)              # golpe del penalti, muy bajo (ya en el primer fotograma)
put(sfx, ST, T(4) - .06, .12, dur=.8, fo=.3)       # sello «FUERA»
put(sfx, SL, T(9) - .3, .09)                       # el recorte de periódico
for k in range(5): put(sfx, TK, T(11) + k * .22, .04, dur=.3, fo=.15)   # contador 1996 → 2018, mecánico y bajo
put(sfx, SH, T(14) - .3, .06)                      # foto de Southgate (obturador)
for k in range(4): put(sfx, TK, T(19) + .1 + k * .55, .05, dur=.35, fo=.15)   # reloj de la sesión hasta el 90'
put(sfx, KI, T(21) + .05, .05, dur=.6, fo=.3)      # los balones en el punto, muy bajo
for i in range(5): put(sfx, MK, T(28) + i * .17, .06, off=.4, dur=.24, fi=.02, fo=.08)   # cinco trazos de rotulador
put(sfx, SH, T(36) - .3, .06)                      # polaroid de Pickford y Dier
put(sfx, SL, T(44) - .3, .08)                      # foto de Moscú
put(sfx, SL, T(45) - .05, .05)                     # hoja de calendario
for i in range(3): put(sfx, MK, T(46) + i * .24 + .12, .05, off=.4, dur=.28, fi=.02, fo=.1)   # tres cruces: 1990, 1998, 2006
put(sfx, MK, T(49) - .03, .06, off=1.2, dur=.35, fi=.02, fo=.12)   # el círculo de 2018
put(sfx, ST, T(50) - .1, .06, dur=.6, fo=.3)       # marcador 4-3, sello suave
put(sfx, TE, T(61) - .02, .10, fo=.2)              # el boleto se rompe
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT)   # audio de outro2.mp4, sincronizado con su imagen
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(OUT * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(OUT * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .78)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
