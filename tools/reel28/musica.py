"""Música del u28: pista nueva m1 (ElevenLabs music v2.5, la menor, pad de campana, fondo tranquilo). El beat suena desde el
fotograma 0; el pequeño hueco de la pista (≈2 s) queda antes del corte al dato; salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
y, _ = librosa.load('m1.mp3', sr=SR, mono=False); y = y.T.astype(np.float32)
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
n = int(END * SR); x = y[:n].copy(); t = np.arange(n) / SR
x *= np.clip((END - t) / 1.2, 0, 1)[:, None]; x[:int(.01 * SR)] *= np.linspace(0, 1, int(.01 * SR))[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
