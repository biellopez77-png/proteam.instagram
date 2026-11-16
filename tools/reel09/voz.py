"""Voz del u09 (Mateo de la biblioteca, toma A). Corta solo en los silencios entre frases (60 ms antes de la primera palabra, 80 ms después de la última),
cuerpo x1.1, CTA x1.0, reto x1.05; pausa antes del CTA 0,15 s. Escribe voz.wav y voz.tsv (mapeado)."""
import json, numpy as np, subprocess
from scipy.io import wavfile
SR = 44100
def load(f):
    sr, X = wavfile.read(f); assert sr == SR; return X.astype(np.float32)
A = load('voz_a.wav')
W = [(float(a), float(b), w) for a, b, w in (l.split('\t') for l in open('voz_a.tsv').read().strip().split('\n'))]
# frases: (índice de la primera palabra, tempo, hueco después)
CUTS = [('Juega', 1.1, .22), ('siempre', 1.1, .26), ('cuando', 1.1, .24), ('Cumples', 1.1, .18), ('Él', 1.1, .26),
        ('Este', 1.1, .22), ('Mándaselo', 1.1, .14), ('que', 1.1, .15),
        ('Comenta', 1.0, .14), ('Te', 1.0, .16), ('Lista', 1.0, .12), ('Tres', 1.0, .18), ('Pregúntale', 1.05, .18), ('¿cuándo', 1.05, 0)]
idx = []; k = 0
for name, *_ in CUTS:
    while W[k][2] != name: k += 1
    idx.append(k); k += 1
bounds = []
for j, i in enumerate(idx):
    last = (idx[j + 1] - 1) if j < len(idx) - 1 else len(W) - 1
    a = max(0, W[i][0] - .06); e = W[last][1] + (.25 if j == len(idx) - 1 else .08)
    bounds.append((a, e))
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return load('_t2.wav')
out = [np.zeros(int(.10 * SR), np.float32)]; t = .10; maps = []
for (a, b), (_, k, g) in zip(bounds, CUTS):
    seg = A[int(a * SR):int(b * SR)].copy(); f = int(.008 * SR)
    seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); maps.append((a, b, k, t)); out.append(y); t += len(y) / SR
    out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
lines = []
for a, b, w in W:
    for pa, pb, k, t0 in maps:
        if pa <= a < pb:
            lines.append((t0 + (a - pa) / k, t0 + (min(b, pb) - pa) / k, w)); break
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in lines))
print('dur', round(len(V) / SR, 2), 'palabras', len(lines), [round(x, 2) for x in sum(bounds, ())])
