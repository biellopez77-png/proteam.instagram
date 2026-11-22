"""Efectos de sonido del Reel 1 (sin música). Suaves: barridos, papel, clics, golpes graves.
python3 sfx.py out.wav"""
import sys, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 48000; DUR = 33.6
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


T = dict(col0=1.45, s2=1.96, g=2.84, ta=3.82, s3=5.06, cnt0=5.35, cnt1=6.6, s4=7.30, rec=8.78, sino=9.74, como=10.26,
         s6=11.96, met=13.48, her=14.48, s7=17.06, cut=21.22, sis0=22.30, sis=23.28, s9=24.26, pt=24.46, web=25.40,
         tap=27.30, ok=27.95, s10=28.55, d28=29.14, s11=30.60, tres=31.16)
for k in range(26): put(.05 + k * 1.3 / 26, tick(.016, 3600), .09)          # máquina de escribir
for i in range(6): put(T['col0'] + i * .085, paper(.14), .2)
for a in [T['s2'], T['g'], T['ta']]: put(a, swish(.3), .12); put(a + .02, tick(.03, 1500), .18)
put(T['s3'], tick(.03, 1200), .2)
for h in range(24):
    p = (h + .5) / 24; tt = T['cnt0'] + (T['cnt1'] - T['cnt0']) * (np.cbrt(p / 4) if p < .5 else 1 - np.cbrt((1 - p) / 4))
    put(tt, tick(.02, 4200), .12)
put(T['cnt1'], thump(), .35)
put(T['s4'] + .05, swish(.3), .12)
put(T['sino'] - .05, whoosh(.45, 2500, 300), .22); put(T['sino'] + .2, thump(), .35)
put(T['como'], swish(.3), .12); put(10.80, swish(.3), .12)
for i in range(8): put(T['s6'] + i * (T['s7'] - T['s6']) / 8, tick(.04, 900), .25)
for w in [T['met'], T['her']]: put(w, swish(.28), .1)
tt, gap = T['s7'], .5
while tt < T['cut']:
    put(tt, paper(min(.25, gap)), .2 + (.5 - gap) * .3); tt += gap; gap = max(.045, gap * .88)
put(T['sis'], thump(), .6); put(T['sis'] - .03, shimmer(.4), .08)
put(T['pt'], swish(.4), .14); put(T['pt'] + .3, thump(.4), .3)
for k in range(20): put(T['web'] + .35 + k * .05, tick(.018, 3800), .1)
put(T['web'] + .97, tick(.025, 2200), .25); put(T['tap'], tick(.025, 2200), .35); put(T['tap'] + .06, tick(.02, 1500), .22); put(T['ok'], swish(.3), .14)
[put(28.46 + i * .52, tick(.04, 900), .25) for i in range(4)]; put(T['d28'], thump(), .45); put(T['tres'], thump(), .5); put(T['tres'] + .05, shimmer(.6), .06)
out = out[:int(SR * DUR)]
out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
