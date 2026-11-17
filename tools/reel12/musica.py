"""Música del u12: pista nueva (ElevenLabs music v2.5, re menor, 143,5 BPM, pad de campanas con textura de vinilo, rimshot seco).
Tramo contenido de la toma (0–13,75 s) bajo la escena, la norma y la hoja; corte seco ~0,38 s antes de «acta» (en «no el acta»);
el regreso del beat de la toma (30,90 s) cae exactamente en «acta» y sigue hasta el final. Fundido de salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a, _ = librosa.load('m1.mp3', sr=SR, mono=False); a = a.T.astype(np.float32)
HIT = 30.90; IMP = T['acta2']; cut = IMP - .38
A = a[:int(cut * SR)].copy(); f = int(.18 * SR); A[-f:] *= np.linspace(1, 0, f)[:, None]
B = a[int((HIT - .01) * SR):]
x = np.zeros((int(END * SR), 2), np.float32); x[:len(A)] += A[:len(x)]
i0 = int((IMP - .01) * SR); n = min(len(B), len(x) - i0); x[i0:i0 + n] += B[:n]
t = np.arange(len(x)) / SR; g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
x[:i0] *= .8   # el tramo contenido va ~2 dB por debajo para que el golpe crezca
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'corte', round(cut, 2), 'golpe', IMP, 'B disponible', round(len(B)/SR,2), 'necesario', round(END-IMP,2))
