"""Música del u31: pista nueva en dos tomas de la misma sesión (ElevenLabs music v2.5, fa# menor, 143,5 BPM, pad de cinta y pluck grave).
m1 (0–10,4 s) lleva el gancho y la escena con el beat contenido; se corta en seco antes de «no vuelve» (silencio de ~0,35 s);
el golpe de m2 (13,42 s) cae exactamente en «no vuelve» y el beat sigue hasta el final. Fundido de salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a, _ = librosa.load('m1.mp3', sr=SR, mono=False); a = a.T.astype(np.float32)
b, _ = librosa.load('m2.mp3', sr=SR, mono=False); b = b.T.astype(np.float32)
HIT = 13.42; cut = T['vuelve'] - .38
A = a[:int(cut * SR)].copy(); f = int(.18 * SR); A[-f:] *= np.linspace(1, 0, f)[:, None]
B = b[int((HIT - .01) * SR):]
x = np.zeros((int(END * SR), 2), np.float32); x[:len(A)] += A[:len(x)]
i0 = int((T['vuelve'] - .01) * SR); n = min(len(B), len(x) - i0); x[i0:i0 + n] += B[:n]
t = np.arange(len(x)) / SR; g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
# el tramo de m1 va 3 dB por debajo para que el golpe crezca
x[:i0] *= .8
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'corte', round(cut, 2), 'golpe', T['vuelve'])
