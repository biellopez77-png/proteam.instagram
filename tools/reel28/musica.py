"""Música del u28 con voz (17/11): la misma pista nueva del u28 (m1, la menor, 143,5 BPM), que no sale en ningún otro Reel.
La pista acaba en ~14 s: desde 13,84 s se repiten 4 compases desde el golpe de 7,15 s (corte en beat, 30 ms de fundido cruzado).
Hueco de 0,3 s antes de «el primero de la lista» (T.d3) y el beat vuelve en esa palabra. Fundido de salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
y, _ = librosa.load('m1.ogg', sr=SR, mono=False); y = y.T.astype(np.float32)
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
BAR = 60 / 143.55 * 4; L0 = 7.15; L1 = L0 + 4 * BAR
seg = y[int(L0 * SR):int(L1 * SR)]; x = y[:int(L1 * SR)].copy(); cf = int(.03 * SR); r = np.linspace(0, 1, cf)[:, None]
while len(x) < int(END * SR):
    x = np.concatenate([x[:-cf], x[-cf:] * (1 - r) + seg[:cf] * r, seg[cf:]])
n = int(END * SR); x = x[:n]; t = np.arange(n) / SR
gap = 1 - np.clip((t - (T['d3'] - .38)) / .08, 0, 1) * np.clip((T['d3'] - t) / .02, 0, 1)  # hueco antes del impacto
x *= gap[:, None]
x *= np.clip((END - t) / 1.2, 0, 1)[:, None]; x[:int(.01 * SR)] *= np.linspace(0, 1, int(.01 * SR))[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
