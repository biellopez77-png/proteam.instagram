"""Efectos de los Reels v2 (22/11) (suaves): golpe de entrada, golpe por número (11 · 5 · 7), golpe del lunes, tres casillas que se marcan, ProTeam y cierre de la lista de espera.
python3 sfx.py sfx.wav times.js"""

import sys, json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 48000; rng = np.random.default_rng(10)
js=open(sys.argv[2]).read(); WORDS=json.loads(js.split('WORDS=')[1].split(';')[0]); DUR=float(js.split('VEND=')[1].split(';')[0])+.7; out = np.zeros(int(SR * (DUR + 1)))
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

def at(w, n=1):
    c = 0
    for x in WORDS:
        if x[0] == w:
            c += 1
            if c == n: return x[1]
    raise SystemExit('falta ' + w)
CUES = {'bq': [('sin',1,'thump',.24),('jordan',1,'shimmer',.05),('cincuenta',1,'whoosh',.08),('cincuenta',1,'thump',.18),('cincuenta',2,'thump',.18),
  ('como',1,'whoosh',.08),('sabado',1,'tick',.14),('martes',1,'thump',.16),('ahora',1,'whoosh',.09),('presionan',1,'thump',.14),('base',1,'shimmer',.06),
  ('haz',1,'whoosh',.09),('base',2,'thump',.18),('cambia',1,'tick',.14),('los',2,'whoosh',.09),('base',3,'thump',.2),('proteam',1,'thump',.14),('lista',1,'whoosh',.12),('tres',1,'thump',.22)],
 'bm': [('este',1,'thump',.24),('euros',1,'thump',.2),('euros',1,'shimmer',.06),('portero',1,'whoosh',.07),('mundial',1,'whoosh',.09),('miraba',1,'whoosh',.08),
  ('apuntado',1,'tick',.12),('alemania',1,'thump',.24),('ahora',1,'whoosh',.09),('paro',1,'tick',.14),('marcaron',1,'thump',.2),('desde',1,'whoosh',.08),
  ('nueve',1,'tick',.14),('extremos',1,'tick',.14),('contraataque',1,'whoosh',.09),('nadie',1,'thump',.2),('hoja',1,'whoosh',.09),('raya',1,'tick',.12),
  ('descanso',1,'shimmer',.06),('papel',3,'whoosh',.08),('partido',1,'thump',.2),('proteam',1,'thump',.14),('lista',1,'whoosh',.12),('tres',1,'thump',.22)]}
F = {'thump': lambda: thump(.45), 'shimmer': lambda: shimmer(.6), 'whoosh': lambda: whoosh(.4, 300, 2400), 'tick': lambda: tick(.03, 1600)}
for w, n, k, g in CUES[sys.argv[3]]:
    t = at(w, n); put(t - (.3 if k == 'whoosh' else .05), F[k](), g)
lt = at('lista'); put(lt + .19, tick(.03, 1500), .14); put(lt + 1.1, tick(.03, 1300), .2); put(lt + 1.32, shimmer(.6), .05)
out = out[:int(SR * DUR)]; out = out / max(1e-9, np.abs(out).max()) * .85
wavfile.write(sys.argv[1], SR, (out * 32767).astype(np.int16)); print('ok')
