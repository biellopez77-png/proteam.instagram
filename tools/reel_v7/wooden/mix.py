"""Mezcla del ejemplo Wooden (sandbox de Higgsfield, con los mp3 de Epidemic Sound ya descargados).
python3 mix.py voz.mp3 tail.mp3 out.wav"""
import sys, subprocess, numpy as np
SR = 48000; DUR = 25.2
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def cut(x, off=0, dur=None, fi=0.0, fo=0.0, norm=True):
    x = x[int(off * SR):]; x = (x[:int(dur * SR)] if dur else x).copy()
    if norm: x /= np.abs(x).max() + 1e-9
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    return x
def put(buf, x, at, g=1.0):
    i = int(at * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
T = dict(fly=[2.38, 7.62, 11.02, 15.06, 17.02])
# música: Epidemic «Orchestra, Piano, Choir, Sentimental», desde 2 s, sin cortes
put(mus, cut(ld('music.mp3'), off=2.0, dur=DUR, fi=.8, fo=1.6, norm=False), 0.0)
# efectos reales, bajos
W, PA, SO, LA, MK, CA = ld('whoosh.mp3'), ld('paper.mp3'), ld('socks.mp3'), ld('laces.mp3'), ld('marker.mp3'), ld('card.mp3')
for f in T['fly']: put(sfx, cut(W, fi=.05, fo=.4), f - .1, .08)
put(sfx, cut(PA), 0.05, .12); put(sfx, cut(PA), 2.75, .12)          # fotos que llegan a la pared
put(sfx, cut(CA), 7.02, .06)                                          # recuadro sobre los pies
put(sfx, cut(SO, off=1.6, dur=1.3, fi=.1, fo=.4), 8.45, .10)          # el calcetín se alisa
for i in range(5): put(sfx, cut(LA), 9.62 + i * .14, .05)            # cordones pasando
put(sfx, cut(LA), 10.44, .13)                                         # apretados
for t0 in (11.52, 12.17, 13.99): put(sfx, cut(CA), t0, .07)          # tarjetas
put(sfx, cut(MK, off=1.85, dur=.45, fo=.15), 11.96, .09)              # flecha 1
put(sfx, cut(MK, off=3.25, dur=.45, fo=.15), 13.04, .09)              # flecha 2
put(sfx, cut(MK, off=4.65, dur=.5, fo=.15), 14.62, .10)               # la X del martes
for i in range(10): put(sfx, cut(CA), 15.48 + i * .1, .035)          # títulos que se encienden
put(sfx, cut(PA), 17.4, .10)                                          # retrato final
# voz y cola del outro
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), 19.9)
e = np.abs(vox[:, 0]); hop = 480; env = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
env = np.minimum(1, env / (np.percentile(env[env > 0], 90) + 1e-9)); sm = np.zeros_like(env)
for i in range(1, len(env)): a = .45 if env[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (env[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(19 * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
