"""Voz del u08 (Mateo, toma B + reto toma A). Corta solo en silencios reales, cuerpo x1.1, CTA x1.0,
reto x1.05; pausa antes del CTA 0,15 s. Escribe voz.wav y voz.tsv (mapeado)."""
import numpy as np, subprocess
from scipy.io import wavfile
SR = 44100
def load(f):
    sr, X = wavfile.read(f); return X.astype(np.float32)
B, R = load('voz_b.wav'), load('reto.wav')
WB = [(float(a), float(b), w) for a, b, w in (l.split('\t') for l in open('voz_b.tsv').read().strip().split('\n'))]
WR = [(float(a), float(b), w) for a, b, w in (l.split('\t') for l in open('reto.tsv').read().strip().split('\n'))]
# (fuente, ini, fin, tempo, hueco_despues)
P = [('B', 0.00, 2.00, 1.1, .30), ('B', 2.24, 3.33, 1.1, .25), ('B', 3.55, 7.10, 1.1, .25), ('B', 7.45, 8.11, 1.1, .15),
     ('B', 8.24, 10.70, 1.1, .25), ('B', 11.00, 11.74, 1.1, .15), ('B', 11.88, 14.76, 1.1, .25), ('B', 15.01, 17.04, 1.1, .15),
     ('B', 17.33, 19.06, 1.0, .22), ('B', 19.25, 21.42, 1.0, .25), ('B', 21.70, 24.11, 1.0, .22), ('B', 24.37, 25.80, 1.0, .30),
     ('R', 0.00, 1.34, 1.05, .28), ('R', 1.87, 4.78, 1.05, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return load('_t2.wav')
out = [np.zeros(int(.12 * SR), np.float32)]; t = .12; maps = []
for src, a, b, k, g in P:
    X = B if src == 'B' else R; seg = X[int(a * SR):int(b * SR)].copy(); f = int(.006 * SR)
    seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); maps.append((src, a, b, k, t)); out.append(y); t += len(y) / SR
    out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
lines = []
for W, s in ((WB, 'B'), (WR, 'R')):
    for a, b, w in W:
        for src, pa, pb, k, t0 in maps:
            if src == s and pa - .05 <= a < pb:
                lines.append((t0 + (max(a, pa) - pa) / k, t0 + (min(b, pb) - pa) / k, w)); break
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in lines))
print('dur', round(len(V) / SR, 2), 'palabras', len(lines))
