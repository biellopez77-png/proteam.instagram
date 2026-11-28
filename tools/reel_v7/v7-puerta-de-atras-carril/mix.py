"""Mezcla v7 · Los listos, a los fuertes (Pete Carril) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 02», «… 03» y «… 01», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-red-valvano-1983/mix.py.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)
r2 (28/11, crítica de Andrés 81/100): la voz acaba en 24,8 s; todo quieto de 24,5 a 25,5 s; fundido a NEGRO 25,5–26,0 s;
outro2 (4 s, con su voz desde 0,33 s) a partir de 26,0 s, con su audio en el mismo instante; la música sigue bajando bajo el cierre.
Viaje de 1,2–2,0 s 6 dB más bajo (whoosh y obturador); true peak ≤ −1 dBTP."""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 26.0; DUR = OUT + 4.0   # outro2 desde 26,0 s (fundido a negro 25,5–26,0)
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
M1, M2, M3 = ld('mus1.mp3'), ld('mus2.mp3'), ld('mus3.mp3')
a2 = len(M1) / SR - 1.4; a3 = a2 + len(M2) / SR - 1.4
put(mus, M1, 0.0, 1.0, fi=.3, fo=1.4)
put(mus, M2, a2, 1.0, fi=1.4, fo=1.4)
put(mus, M3, a3, 1.0, fi=1.4, fo=1.4)
if a3 + len(M3) / SR - 1.4 < DUR: put(mus, M1, a3 + len(M3) / SR - 1.4, 1.0, fi=1.4, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(34)) / .25, 0, 1) * np.clip((T(35) + .2 - tt) / .3, 0, 1)   # pausa antes del 43 a 41: solo música
env *= 1 + .3 * np.clip((tt - T(53)) / .5, 0, 1) * np.clip((25.9 - tt) / .6, 0, 1)        # sube en «los listos», quieto, y vuelve al fundido
env *= np.clip(1 - (tt - OUT) / 3.6, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)               # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3'))
TK = pk(ld('tick.mp3')); BO = pk(ld('bounce.mp3')); NT = pk(ld('net.mp3')); CK = pk(ld('click.mp3')); ME = pk(ld('metal.mp3'))
for f, g in [(1.3, .04), (5.25, .08), (10.25, .08), (17.3, .08)]: put(sfx, WH, f - .05, g, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje (el primero, −6 dB)
put(sfx, SL, 0.05, .09)                          # la ficha de prensa
put(sfx, SH, T(1) - .2, .05)                     # foto del Jadwin (obturador, −6 dB)
put(sfx, SL, T(3) - .15, .08)                    # tarjeta de UCLA
put(sfx, MK, T(5) - .1, .05, dur=1.0, fi=.05, fo=.3)    # el trofeo se dibuja
put(sfx, SL, T(8) - .25, .09)                    # la pancarta de Carril
put(sfx, MK, T(19) - .1, .07, dur=1.0, fi=.05, fo=.3)   # rotulador: la flecha del corte
put(sfx, SL, T(22) - .3, .08)                    # foto de archivo
for k in range(4): put(sfx, TK, T(23) + k - .04, .07, dur=.35, fo=.15)   # reloj: 0:07 → 0:04, muy bajo
put(sfx, BO, T(27) - .05, .14, dur=.7, fo=.3)    # el bote del pase picado, uno solo
put(sfx, NT, T(34) - .05, .12, fo=.4)            # tablero y red, discreto
put(sfx, CK, E(35) - .05 - .88, .1, dur=1.0)     # 43
put(sfx, CK, E(37) - .05 - .88, .1, dur=1.0)     # 41
put(sfx, ME, T(45) - .1, .05, fo=1.0)            # metal muy suave y lejano: la viga
put(sfx, MK, T(55) - .1, .05, dur=1.0, fi=.05, fo=.3)   # la flecha final
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
mix /= max(1, np.abs(mix).max() / .78)  # pico de muestra −2,2 dBFS: true peak ≤ −1 dBTP tras el AAC
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
