"""Mezcla v7 · Cinco dedos, un puño (Krzyzewski) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde 1,5 s) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/bielsa/mix3.py y v7-red-valvano-1983/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.8; DUR = OUT + 5.61   # la voz acaba en 21,6 s; a 21,8 empieza el fundido de 0,6 s al cierre
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
put(mus, ld('mus.mp3'), 0.0, 1.0, off=1.5, dur=OUT + 1.6, fi=.3, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(43)) / .25, 0, 1) * np.clip((T(44) + .2 - tt) / .3, 0, 1)   # pausa antes del remate: solo música
env *= 1 + .3 * np.clip((tt - T(51)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)    # sube 1 s en «puño» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); CP = pk(ld('chip.mp3')); PI = pk(ld('pick.mp3'))
MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); GL = pk(ld('glove.mp3'))
for f in [2.72, 13.25, 18.27]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 5.37, .05, dur=1.1, fi=.1, fo=.4)                                         # la cámara se acerca a la mano
put(sfx, SL, 0.0, .09)                                       # ficha de Krzyzewski
for i in range(5): put(sfx, CP, T(4) - .08 + i * .12 + .34, .1, dur=.35, fo=.1)       # cinco fichas caen en la pista
put(sfx, PI, T(9) - .55, .08)                                # las fichas se levantan
put(sfx, MK, T(9), .06, dur=1.0, fi=.05, fo=.35)             # se dibuja la mano
put(sfx, CP, T(12) + .45, .07, dur=.35, fo=.1)               # las fichas llegan a las yemas
put(sfx, SH, T(18) - .25, .08, dur=.45, fo=.1)               # foto de la charla
for k in [22, 23, 24, 26, 28]: put(sfx, MK, T(k) - .03, .06, off=1.0 + k % 3, dur=.45, fi=.03, fo=.15)   # cada palabra en su dedo
put(sfx, SL, T(29) - .25, .07)                               # panel del talento
for d in [0, .16, .3]: put(sfx, CP, T(31) + d, .06, dur=.35, fo=.1)                   # estrellas que se dispersan
put(sfx, SL, T(39) - .25, .07)                               # panel del equipo
put(sfx, MK, T(41) - .05, .05, off=4.0, dur=.7, fi=.05, fo=.25)   # pases
put(sfx, SL, T(44) - .3, .09)                                # foto de archivo, 1986
put(sfx, GL, T(49) - .05, .14, off=.15, dur=1.0, fi=.05, fo=.3)   # la mano se cierra
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
