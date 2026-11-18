"""Música del u50: pista nueva (ElevenLabs music v2.5, mi menor, ~143 BPM, intro nocturna con reloj y pad tipo Rhodes desafinado, 808 con
glides cortos, hi-hats con tresillos sueltos, rimshot y hiss de vinilo). La intro tranquila de la toma (0–9,9 s) va bajo la escena del domingo;
corte seco 0,35 s antes de «veintiocho» y el beat entero de la toma (desde su entrada, 13,71 s) cae justo en «veintiocho». Fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
DROP = 13.71; IMP = T['v28']; cut = IMP - .35
A = a[:int(cut * SR)].copy(); f = int(.15 * SR); A[-f:] *= np.linspace(1, 0, f)[:, None]
B = a[int((DROP - .01) * SR):]
x = np.zeros((int(END * SR), 2), np.float32); x[:len(A)] += A
i0 = int((IMP - .01) * SR); n = min(len(B), len(x) - i0); x[i0:i0 + n] += B[:n]
t = np.arange(len(x)) / SR; g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
x[:i0] *= 1.25   # la intro es muy suave: que se oiga bajo la voz
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'corte', round(cut, 2), 'golpe', IMP, 'B', round(len(B) / SR, 2), 'necesario', round(END - IMP, 2))
