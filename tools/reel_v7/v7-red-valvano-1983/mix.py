"""Mezcla v7 · Cortar la red antes de tiempo (Valvano) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» y «… 03», encadenadas con 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-jinete-sacchi/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.3; DUR = OUT + 5.61   # la voz acaba en 22,0 s; a 22,3 empieza el fundido de 0,6 s al cierre
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
M1, M2 = ld('mus1.mp3'), ld('mus2.mp3')
put(mus, M1, 0.0, 1.0, fi=.3, fo=1.4)
put(mus, M2, len(M1) / SR - 1.4, 1.0, dur=OUT + 1.6 - (len(M1) / SR - 1.4), fi=1.4, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(49)) / .25, 0, 1) * np.clip((T(50) + .2 - tt) / .3, 0, 1)  # pausa antes del remate: solo música
env *= 1 + .3 * np.clip((tt - T(52)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube 1 s en «de verdad» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); FL = pk(ld('flip.mp3')); SL = pk(ld('slide.mp3')); SC = pk(ld('scissors.mp3')); LA = pk(ld('ladder.mp3'))
MK = pk(ld('marker.mp3')); NW = pk(ld('news.mp3')); CK = pk(ld('click.mp3')); BZ = pk(ld('buzzer.mp3'))
for f in [1.15, 4.15, 7.65, 10.15, 13.45, 18.25]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .09)                          # foto del pabellón
put(sfx, FL, T(3) - .15, .1)                    # la hoja del calendario
put(sfx, SL, T(5) - .2, .1)                     # ficha de Valvano
put(sfx, SC, T(11) + .38, .12)                  # las tijeras, una vez
put(sfx, LA, T(17) - .05, .12)                  # la escalera se apoya
for f in [T(19), T(19) + .28, T(20) + .05, T(21) + .05]: put(sfx, SC, f, .08)   # cuatro cortes
put(sfx, SL, T(22) - .15, .08)                  # marcador vacío
put(sfx, MK, T(26) - .05, .06, dur=.9, fi=.05, fo=.3)   # rotulador sobre TÍTULO
put(sfx, NW, T(28) - .25, .13, dur=1.2, fo=.4)  # el periódico
put(sfx, SL, T(30) - .05, .07)                  # cartel de la final
put(sfx, SL, T(35) - .3, .09)                   # foto de Valvano en la banda
put(sfx, BZ, T(40) + .1, .05, fo=.3)            # bocina, lejana y corta
put(sfx, CK, E(41) - .05, .1)                   # 54
put(sfx, CK, E(43) - .05, .1)                   # 52
for f in [T(47), T(47) + .3, T(49), T(50) - .05]: put(sfx, SC, f, .08)   # vuelven a cortar la red
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
