"""Efectos de sonido del Reel 2 (sin música). Suaves: barridos, papel, clics, golpes graves.
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


import json
T = json.loads(open(sys.argv[2]).read().split('=',1)[1].split(';')[0])
DUR = T['END']; out = np.zeros(int(SR * (DUR + 1)))
def rewind(d=1.1):  # cinta hacia atrás: ruido filtrado con barrido descendente y trémolo
    n = int(d * SR); t = np.arange(n) / SR; x = rng.standard_normal(n); y = np.zeros(n); k = 12
    for j in range(k):
        f = 4000 * (300 / 4000) ** (j / (k - 1)); w = np.exp(-((t / d - j / (k - 1)) ** 2) / (2 * .07 ** 2)); y += bp(x, f * .6, min(f * 1.5, SR / 2 - 100)) * w
    y *= (.6 + .4 * np.sin(2 * np.pi * 28 * t)); return y * env(n, 1.2, .5) / (np.abs(y).max() + 1e-9)
# gancho
put(0, thump(.4), .32); put(.25, swish(.3), .1)
put(T['min'] - .1, swish(.25), .1)
for i in range(3): put(T['min'] + i * 1.0, tick(.03, 2200), .2)
put(T['n88'] + .03, thump(.45), .3)
# rebobinado
put(T['pero'] - .1, rewind(T['mar'] - T['pero'] + .1), .22)
for i in range(18): put(T['pero'] + i * (T['mar'] - T['pero']) / 18, tick(.02, 2600 + 50 * i), .08)
put(T['mar'], thump(.5), .36); put(T['mar'] + .02, shimmer(.4), .04)
# semana en papel
put(T['c1'] - .1, whoosh(.45, 300, 2500), .14); put(T['c1'] + .05, paper(.3), .2)
for i in range(3): s = T['c1'] + .2 + i * .42; put(s, paper(.15), .14); put(s + .27, paper(.12) * np.linspace(1, .3, int(.12 * SR)), .2)
put(T['coche'] - .2, swish(.25), .1)
put(T['c2'] - .1, whoosh(.4, 400, 2800), .14); put(T['c2'], paper(.25), .18)
for i in range(6): put(T['c2'] + .1 + i * .07, tick(.02, 1500), .14)
k0 = T['nadie'] + .1; n6 = (T['c3'] - .2 - k0) / 7
for i in range(6): put(k0 + i * n6, tick(.03, 3200), .1)
put(T['nadie'], swish(.25), .1)
put(T['c3'] - .1, whoosh(.4, 400, 2800), .14); put(T['c3'], paper(.25), .18)
for i in range(3): put(T['rep'] + i * .2, tick(.03, 1300), .2); put(T['rep'] + i * .2 + .02, thump(.2), .1)
put(T['siem'] - .25, swish(.3), .12)
# sábado
put(T['sab'] - .08, whoosh(.4, 2500, 300), .16); put(T['sab'] + .08, thump(.5), .34)
put(T['res'] - .3, swish(.25), .1)
put(T['pero2'] - .05, whoosh(.5, 3000, 250), .14)
for i in range(5): put(T['dec'] - .1 + i * .1, tick(.03, 1800 + 200 * i), .18)
put(T['sem'], thump(.7), .5); put(T['sem'] + .01, shimmer(.5), .05)
# app
put(T['la'] - .1, whoosh(.45, 300, 2200), .15); put(T['sem2'] - .15, swish(.3), .12); put(T['sem2'], tick(.03, 1600), .14); put(T['ses1'] - .1, swish(.25), .08)
# CTA (como u02, tiempos comprimidos)
web = T['une'] - .05; tap = web + .62
put(web - .05, whoosh(.4, 2500, 400), .14); put(web + .24, tick(.03, 1500), .18)
for i in range(8): put(web + .27 + i * .03, tick(.012, 3000), .06)
put(tap, tick(.03, 1300), .22); put(tap + .22, shimmer(.4), .05)
put(T['n28'] - .3, thump(.4), .3); put(T['n28'] - .2, tick(.03, 2000), .18); put(T['nov'], swish(.25), .1)
put(T['cons'], whoosh(.4, 300, 2500), .14); put(T['tres'] - .2, thump(.5), .42); put(T['tres'] - .15, shimmer(.6), .05)
out = out[:int(SR * DUR)]
out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
