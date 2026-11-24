"""Mezcla v7 · El peor verano (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental») + SFX reales bajos + voz (ElevenLabs, Mateo).
python3 mix.py voz.mp3 tail.mp3 out.wav"""
import sys, subprocess, numpy as np
SR = 48000; DUR = 26.7; OUT = 21.1   # la voz acaba en 21,1 s; ahí entra el cierre (xfade 0,6 s)
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(at * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: una sola pista, sin cortes; se apaga con 1,4 s mientras entra el cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, off=1.6, dur=OUT + 1.6, fi=0.4, fo=1.4)
W = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); PB = pk(ld('paper2.mp3')); MK = pk(ld('marker.mp3'))
BD = pk(ld('board.mp3')); ST = pk(ld('stamp.mp3')); NT = pk(ld('net.mp3')); GR = pk(ld('gear.mp3'))
for f in [2.36, 8.28, 11.22, 15.42, 17.78]: put(sfx, W, f - .1, .09, dur=1.2, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, PA, 0.0, .08)                              # pista y semanas
put(sfx, MK, 1.42, .08, dur=1.0, fo=.3)             # cruces fuera de la zona
put(sfx, GR, 3.1, .08, dur=1.0, fi=.05, fo=.3)      # el año rueda hasta 2003
put(sfx, BD, 4.55, .07, dur=1.2, fi=.1, fo=.4)      # la silueta se dibuja
put(sfx, MK, 7.85, .08, dur=.7, fo=.2)              # «catapulta»
put(sfx, PA, 8.85, .14)                             # foto NBA
put(sfx, PB, 9.26, .10)                             # ficha de Dell Curry
put(sfx, MK, 10.5, .08, dur=.6, fo=.2)              # el punto sube
put(sfx, MK, 11.1, .07, dur=.7, fo=.2)              # arco alto
put(sfx, BD, 12.0, .07, off=1.5, dur=1.1, fi=.05, fo=.3)   # tiros cortos
put(sfx, BD, 13.35, .07, off=3.0, dur=1.0, fi=.05, fo=.3)  # calendario tachado
put(sfx, ST, 16.36, .22)                            # sello «Nº 1»
put(sfx, NT, 16.8, .10, dur=1.4, fi=.1, fo=.5)      # triples que entran
put(sfx, PA, 18.45, .14)                            # foto del entrenamiento
put(sfx, PB, 19.73, .08)                            # bocadillo
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; env = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
env = np.minimum(1, env / (np.percentile(env[env > 0], 90) + 1e-9)); sm = np.zeros_like(env)
for i in range(1, len(env)): a = .45 if env[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (env[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
