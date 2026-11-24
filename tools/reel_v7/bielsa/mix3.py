"""Mezcla v3 (se ejecuta donde estén los mp3 de Epidemic Sound, vía Higgsfield).
Música real suave (Epidemic: Soft Piano, Strings, Calm 01 y 02, en Do mayor) + SFX reales bajos + voz.
python3 mix3.py voz.mp3 tail.mp3 out.wav"""
import sys, subprocess, numpy as np
SR = 48000; DUR = 22.7
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
# música: 01 hasta el «No era una manía», 02 después, sin cortes (fundido de 1,4 s)
m1, m2 = ld('m01.mp3'), ld('m02.mp3')
put(mus, m1, 0.0, 1.0, off=0.6, dur=10.4, fi=0.4, fo=1.4)
put(mus, m2, 9.0, 1.0, off=1.0, fi=1.4)
# SFX reales, discretos
W = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); ST = pk(ld('stamp.mp3')); SH = pk(ld('shutter.mp3'))
CL = pk(ld('clock.mp3')); MK = pk(ld('marker.mp3')); CA = pk(ld('cards.mp3'))
for f in [1.3, 4.05, 7.0, 9.2, 11.85, 13.85]: put(sfx, W, f - .1, .10, fi=.05, fo=.4)
put(sfx, SH, 0.95, .10, dur=.6, fo=.2)          # visor REC en «espiar»
put(sfx, PA, 1.75, .14)                          # aparece la diapositiva
put(sfx, CA, 4.62, .09, dur=1.3, fi=.05, fo=.4)  # 51 fichas sobre la mesa
put(sfx, CL, 7.62, .07, dur=1.8, fi=.2, fo=.5)   # reloj de las 4 horas
put(sfx, MK, 10.9, .08, dur=1.5, fi=.1, fo=.4)   # flechas en la pizarra
put(sfx, ST, 13.46, .22)                         # sello «EL LOCO»
put(sfx, PA, 14.2, .12)                          # portada sobre la pila
# voz (más segura, ElevenLabs) y cola del outro
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), 17.4)
# ducking suave de la música con la voz (ataque 80 ms, suelta 400 ms)
e = np.abs(vox[:, 0]); hop = 480; env = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
env = np.minimum(1, env / (np.percentile(env[env > 0], 90) + 1e-9)); sm = np.zeros_like(env)
for i in range(1, len(env)): a = .45 if env[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (env[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(17 * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg      # música ~12 dB bajo la voz
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
