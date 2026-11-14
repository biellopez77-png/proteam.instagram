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
# gancho
put(0, thump(.4), .3); put(0, swish(.3), .1); put(1.05, whoosh(.45, 400, 2500), .14)
put(1.1, paper(.2), .2); put(1.22, paper(.2), .18); put(T['tu'] - .15, whoosh(.5, 2500, 400), .14); put(T['tu'], thump(.35), .2)
put(T['no'] - .2, whoosh(.25, 300, 3000), .2)
# desmontando
for k in ['no', 'ni1', 'ni2']: put(T[k], swish(.3), .14); put(T[k] + .02, thump(.25), .15); put(T[k] + .14, paper(.18), .16)
for i in range(7): put(T['y1'] + i * .22, paper(.16), .14); put(T['y1'] + i * .22, tick(.03, 1300), .14)
put(T['veinte'] - .4, thump(.3), .18); put(T['per'], whoosh(.5, 3000, 250), .2)
# sistema
for k in range(13): put(T['los2'] + .5 + k * .2, tick(.025, 2400 + 80 * k), .12)
put(T['sis'] - .4, whoosh(.4, 300, 2600), .2); put(T['sis'], thump(.6), .45); put(T['sis'] + .02, shimmer(.4), .05)
# método
put(T['pla'], swish(.28), .12)
for i in range(9): put(T['pla'] + .15 + i * .05, tick(.02, 3000), .1)
put(T['reg'], swish(.28), .12)
for i in range(7): put(T['reg'] + .05 + i * .07, tick(.025, 1800), .16)
put(T['ana'], swish(.28), .12)
for i in range(16): put(T['ana'] + .15 + i * .037, tick(.012, 3500 + 60 * i), .07)
put(T['y2'] + .25, thump(.35), .2)
for g in range(3): put(T['dec'] + g * .12 + .35, tick(.03, 1200), .2)
# producto
put(T['pt'] - .1, whoosh(.45, 300, 2200), .16); put(T['pt'] + .3, thump(.35), .18)
for k in ['herr', 'sis2']: put(T[k] + .1, swish(.25), .1)
put(T['herr'] + .75, swish(.25), .1); put(T['solo'] - .3, paper(.2), .14)
# CTA
put(T['une'] - .05, whoosh(.4, 2500, 400), .14); put(T['une'], tick(.03, 1500), .18)
put(T['n28'] - .1, thump(.4), .3); put(T['n28'] + .05, tick(.03, 2000), .18); put(T['nov'], swish(.25), .1)
put(T['cons'], whoosh(.4, 300, 2500), .14); put(T['tres'] - .2, thump(.5), .42); put(T['tres'] - .15, shimmer(.6), .05)
out = out[:int(SR * DUR)]
out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
