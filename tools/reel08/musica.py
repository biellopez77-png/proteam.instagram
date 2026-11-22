"""Música del u08: pista nueva m1 (ElevenLabs music v2.5, fondo tranquilo). Desplazada para que un tiempo fuerte caiga en
«problema», hueco de 0,3 s antes de esa palabra, +1 compás insertado en tiempo fuerte (fundido 30 ms) y salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
y, _ = librosa.load('m1.mp3', sr=SR, mono=False); y = y.T.astype(np.float32)
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0])
END = T['END']; PROB = T['prob']
DB, BEAT = 4.300, 0.41835   # tiempo fuerte del compás en la pista y duración de un tiempo
off = DB - PROB             # segundo de la pista que suena en t=0
x = y[int(off * SR):]
# compás duplicado a partir del tiempo fuerte de 9,45 s de la pista
a = int((9.451 - off) * SR); L = int(4 * BEAT * SR); f = int(.03 * SR)
bar = x[a:a + L].copy(); w = np.linspace(0, 1, f)[:, None]
head, tail = x[:a + L].copy(), x[a:].copy()
bar[:f] = head[-f:] * (1 - w) + bar[:f] * w; tail[:f] = bar[-f:] * (1 - w) + tail[:f] * w
x = np.concatenate([head[:-f], bar[:-f], tail])
n = int(END * SR); assert len(x) >= n, (len(x) / SR, END); x = x[:n]
t = np.arange(n) / SR
g = np.ones(n, np.float32)
g *= 1 - .88 * np.clip((t - (PROB - .34)) / .06, 0, 1) * np.clip((PROB - .02 - t) / .02, 0, 1)   # hueco antes de «problema»
g *= np.clip((END - t) / 1.2, 0, 1)                                                        # salida suave
x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'offset', round(off, 3))
