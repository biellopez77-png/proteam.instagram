"""Efectos de sonido del Reel 1 (sin música). Suaves: barridos, papel, clics, golpes graves.
python3 sfx.py out.wav"""
import sys, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 48000; DUR = 28.4
rng = np.random.default_rng(3)
out = np.zeros(int(SR * (DUR + 1)))

def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def put(t, x, g):
    i = int(t * SR); out[i:i + len(x)] += x[:len(out) - i] * g

def env(n, a, peak=.35):
    t = np.linspace(0, 1, n); e = np.where(t < peak, (t / peak) ** a, ((1 - t) / (1 - peak)) ** 1.6); return e

def whoosh(d=.7, lo=250, hi=3200):
    n = int(d * SR); x = rng.standard_normal(n); y = np.zeros(n); k = 10
    for j in range(k):  # banda que sube
        f = lo * (hi / lo) ** (j / (k - 1)); seg = bp(x, f * .6, min(f * 1.6, SR / 2 - 100))
        w = np.exp(-((np.arange(n) / n - j / (k - 1)) ** 2) / (2 * .09 ** 2)); y += seg * w
    return y * env(n, 1.6, .55) / (np.abs(y).max() + 1e-9)

def swish(d=.28): n = int(d * SR); y = bp(rng.standard_normal(n), 2500, 9000); return y * env(n, 1.2, .3) / (np.abs(y).max() + 1e-9)
def thump(d=.5):
    n = int(d * SR); t = np.arange(n) / SR; f = 48 + 40 * np.exp(-t * 18)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5); y += lp(rng.standard_normal(n), 400) * np.exp(-t * 40) * .4
    return y / np.abs(y).max()
def tick(d=.03, f=3200):
    n = int(d * SR); y = bp(rng.standard_normal(n), f * .5, f * 1.6) * np.exp(-np.arange(n) / SR * 260); return y / (np.abs(y).max() + 1e-9)
def paper(d=.3):
    n = int(d * SR); x = bp(rng.standard_normal(n), 1200, 6000)
    am = np.abs(lp(rng.standard_normal(n), 60)); am /= am.max(); y = x * am * env(n, 1, .2); return y / (np.abs(y).max() + 1e-9)
def shimmer(d=.6): n = int(d * SR); y = hp(rng.standard_normal(n), 5000); return y * env(n, 2, .3) / (np.abs(y).max() + 1e-9)

T = dict(hook=.12, hookOut=2.0, s2=2.2, b2=3.0, b3=3.9, cnt=4.25, s2out=6.2, s3=6.4, q=8.25, b5=8.6, s3out=9.82,
         s4=10.0, b7=11.5, s4out=12.85, s5=12.9, s5out=15.95, sys=16.1, sysW=16.55, s6out=18.6, s7=18.75, pt=19.45,
         pt2=20.1, s7out=21.15, br=21.3, brOut=24.45, b12=24.6, b13=26.0, b13out=27.55)
cards = [13.5, 14.0, 14.5, 15.0]
# barridos de luz entre fases
for a in [T['hookOut'] - .05, T['s2out'] + .05, T['s3out'], T['s4out'], T['s6out'] + .05, T['s7out'] + .05, T['brOut']]:
    put(a - .35, whoosh(.75), .30)
# entradas de frase: roce suave
for a in [T['hook'], T['s2'], T['b2'], T['b3'], T['s3'], T['b5'], T['s4'] + .12, T['b7'], T['s5'] + .05, T['sys'], T['pt'] - .1, T['pt2'], T['b12'], T['b13']]:
    put(a, swish(), .10)
# golpes graves en palabras clave
for a in [T['hook'] + .25, T['cnt'] + 1.35, T['q'] + .3, T['sysW'] + .05, T['pt'] + .05, T['b12'] + .15, T['b13'] + .2]:
    put(a, thump(), .55)
# fotos del collage y tarjetas: papel
for i in range(6): put(T['hook'] + .2 + i * .21, paper(.22), .22)
for i in range(7): put(T['s7'] + i * .12, paper(.2), .2)
for c in cards: put(c, paper(.32), .28); put(c + .02, tick(.03, 1800), .18)
# chips de recursos: clic suave
for i in range(8): put(T['s3'] + .15 + i * .13, tick(.035, 2600), .2)
# contador: un tic por hora
for h in range(24):
    p = h / 24; # tiempo inverso de la curva io
    tt = T['cnt'] + .1 + 1.25 * (np.cbrt(p / 4) if p < .5 else 1 - np.cbrt((1 - p) * 2 / 4 * 1) )
    put(tt, tick(.02, 4200), .14)
# cortes de los planos de acción
for k in range(1, 5): put(T['s4'] + k * .55, tick(.04, 900), .25)
# convergencia + destello
put(T['sys'] + .05, whoosh(.5, 1500, 200), .25); put(T['sysW'] - .05, shimmer(.6), .12)
# navegador: tecleo y clics
for k in range(12): put(T['br'] + .45 + k * .05, tick(.018, 3600), .12)
for k in range(20): put(T['br'] + 1.75 + k * .035, tick(.018, 3800), .11)
for a in [T['br'] + 1.55, T['br'] + 3.0]: put(a, tick(.025, 2200), .3); put(a + .06, tick(.02, 1600), .2)
put(T['br'] + 3.05, swish(.35), .14)

out = out[:int(SR * DUR)]
out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16))
print('ok')
