"""Efectos del u12 (suaves): entrada, corte a los asistentes, acta, columnas, casillas, golpe en «no el acta», CTA y reto.
python3 sfx.py sfx.wav times.js"""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 48000; rng = np.random.default_rng(12)
T = json.loads(open(sys.argv[2]).read().split('=', 1)[1].split(';')[0]); DUR = T['END']; out = np.zeros(int(SR * (DUR + 1)))
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def put(t, x, g):
    i = int(max(0, t) * SR); out[i:i + len(x)] += x[:len(out) - i] * g
def env(n, a, peak=.35):
    t = np.linspace(0, 1, n); return np.where(t < peak, (t / peak) ** a, ((1 - t) / (1 - peak)) ** 1.6)
def whoosh(d=.7, lo=250, hi=3200):
    n = int(d * SR); x = rng.standard_normal(n); y = np.zeros(n); k = 10
    for j in range(k):
        f = lo * (hi / lo) ** (j / (k - 1)); s = bp(x, f * .6, min(f * 1.6, SR / 2 - 100)); y += s * np.exp(-((np.arange(n) / n - j / (k - 1)) ** 2) / (2 * .09 ** 2))
    return y * env(n, 1.6, .55) / (np.abs(y).max() + 1e-9)
def swish(d=.28): n = int(d * SR); y = bp(rng.standard_normal(n), 2500, 9000); return y * env(n, 1.2, .3) / (np.abs(y).max() + 1e-9)
def thump(d=.5):
    n = int(d * SR); t = np.arange(n) / SR; f = 48 + 40 * np.exp(-t * 18)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5); y += lp(rng.standard_normal(n), 400) * np.exp(-t * 40) * .4; return y / np.abs(y).max()
def tick(d=.03, f=3200): n = int(d * SR); y = bp(rng.standard_normal(n), f * .5, f * 1.6) * np.exp(-np.arange(n) / SR * 260); return y / (np.abs(y).max() + 1e-9)
def shimmer(d=.6): n = int(d * SR); y = hp(rng.standard_normal(n), 5000); return y * env(n, 2, .3) / (np.abs(y).max() + 1e-9)
put(0, thump(.45), .3); put(.08, swish(.3), .08)                          # gancho
put(T['yt'] - .1, swish(.25), .08); put(T['acta1'] - .05, tick(.03, 1800), .14)   # corte + sube el acta
for i in range(3): put(T['cont'] + .2 + .3 * i, tick(.025, 2200), .09)   # cruces
put(T['ext'] - .2, whoosh(.45, 300, 2400), .11)                          # tinta: columnas
put(T['dos'], tick(.03, 1500), .14); put(T['cinco'], tick(.03, 1500), .14)
put(T['guar'] - .2, whoosh(.45, 2400, 400), .11)                         # papel: casillas
for i in range(6): put(T['seis'] + .15 + .25 * i, tick(.025, 1700 + 250 * (i % 2)), .1)
put(T['menos'], tick(.03, 1300), .14)
put(T['sab'] - .2, whoosh(.45, 2400, 400), .1)                           # vuelve la foto
put(T['acta2'], thump(.55), .34); put(T['acta2'] + .02, shimmer(.5), .04)   # golpe: no el acta
put(T['com'] - .1, swish(.3), .07)
put(T['prep'] - .05, tick(.03, 1300), .14)
# v2: entra la web de la lista, clic en el campo, toque en el botón, «Estás dentro» y golpe en «tres meses gratis»
put(T['lis'] - .05, whoosh(.45, 300, 2200), .12); put(T['lis'] + .19, tick(.03, 1500), .14); put(T['lis'] + 1.1, tick(.03, 1300), .2); put(T['lis'] + 1.32, shimmer(.6), .05)
put(T['tres'] - .1, thump(.45), .24)
put(T['preg'] - .2, whoosh(.45, 300, 2400), .11); put(T['qui'] + .3, shimmer(.5), .03)
out = out[:int(SR * DUR)]; out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
