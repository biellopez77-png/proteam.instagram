"""Efectos de sonido del u09 (sin música). Suaves: barridos, papel, clics, golpes graves.
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
# gancho: entrada suave y golpe grave en «últimos» (entra el beat)
put(0, thump(.45), .22); put(.1, swish(.3), .07)
put(T['ult'] + .02, thump(.4), .3)
# partido decidido: la barra corre (clics de reloj), el 9 entra al final
put(T['cuando'] - .1, whoosh(.45, 2500, 400), .12)
for i in range(10): put(T['cuando'] + .2 + i * .22, tick(.02, 2600), .07)
put(T['nada'] - .25, swish(.3), .1); put(T['nada'] + .15, tick(.03, 1500), .16)
# consecuencia: foto + check
put(T['cum'] - .1, whoosh(.5, 400, 2600), .12); put(T['norma'], tick(.03, 1800), .16)
# ficha: papel, el 9 se mueve antes del descanso, filas
put(T['este'] - .1, whoosh(.4, 300, 2500), .12); put(T['este'] + .1, paper(.3), .2)
put(T['doce3'] - .1, swish(.3), .1); put(T['marc'] - .1, tick(.03, 1800), .16); put(T['vivo'] + .15, tick(.03, 1800), .16)
# app: directo → informe → semana
put(T['mand'] - .1, whoosh(.45, 300, 2200), .13); put(T['seg'] - .05, tick(.03, 1300), .18)
put(T['lleve'] - .12, swish(.28), .1); put(T['lleve'] + .25, tick(.03, 1300), .16)
put(T['com'] - .1, swish(.28), .1); put(T['sem'] - .05, tick(.03, 1300), .16)
# CTA de campaña (igual que u08)
web = T['lista'] - .05; tap = web + .62
put(web - .05, whoosh(.4, 2500, 400), .12); put(web + .24, tick(.03, 1500), .16)
for i in range(8): put(web + .27 + i * .03, tick(.012, 3000), .05)
put(tap, tick(.03, 1300), .2); put(tap + .22, shimmer(.4), .04)
put(T['n27'] + .3, thump(.4), .26)
put(T['tres'] - .2, thump(.5), .3); put(T['tres'] - .15, shimmer(.6), .04)
# reto
put(T['preg'] - .1, whoosh(.45, 300, 2200), .12); put(T['ult2'] - .1, swish(.3), .09); put(T['sab2'], tick(.03, 1500), .14)
out = out[:int(SR * DUR)]
out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
