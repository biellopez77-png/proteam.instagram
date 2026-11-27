"""Efectos del u73 (suaves): golpe de entrada, cronómetro que corre, martes, pregunta y cierre. Antes: u64 (suaves): golpe de entrada, 4 DÍAS, puntos que caen en la semana, golpe en «Tú», puntos que se apagan, todos encendidos, ficha, Riazor, 28 NOV y cierre.
Antes: u68 (suaves): golpe de entrada, cuatro fichas, 2×2, tres verbos, caída de las fichas (SE PIERDE), banquillos, fichas que vuelan, golpe en «ProTeam.», tres pantallas, 6 MESES, 28 NOV y cierre de la lista de espera.
python3 sfx.py sfx.wav times.js"""

import sys, json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 48000; rng = np.random.default_rng(10)
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
def vib(d=.42):
    n = int(d * SR); t = np.arange(n) / SR; y = np.sign(np.sin(2 * np.pi * 150 * t)) * (np.sin(2 * np.pi * 9 * t) > -.2)
    y = lp(y, 900) * np.minimum(1, t / .02) * np.minimum(1, (d - t) / .05); return y / (np.abs(y).max() + 1e-9)
put(0, thump(.45), .22)
put(T['seis'] - .1, swish(.25), .06)
for k in range(12): put(T['seis'] - .1 + k * .14, tick(.025, 2600), .05)
put(T['menos'], thump(.35), .12)
put(T['martes'] - .06, whoosh(.4, 2400, 400), .07); put(T['ni'] - .1, tick(.03, 900), .14)
put(T['cuan'] - .06, whoosh(.45, 300, 2400), .08)
put(T['camp'] - .05, whoosh(.45, 300, 2200), .12); put(T['camp'] + .19, tick(.03, 1500), .14); put(T['camp'] + 1.1, tick(.03, 1300), .2); put(T['camp'] + 1.32, shimmer(.6), .05)
put(T['gra'] - .1, thump(.45), .24)
out = out[:int(SR * DUR)]; out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
