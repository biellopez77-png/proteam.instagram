"""Música del u59: pista nueva (ElevenLabs music v2.5, fa menor, ~143 BPM, intro tensa con tic de reloj y pad frío de cristal, 808 con
deslizamientos cortos, hi-hats en tresillos y palmada seca). La intro (0–13,4 s de la toma) va bajo la tira de los diez días; silencio de
0,3 s antes de «veintiocho» y el beat entero (entrada de la toma en 13,425 s) cae justo en «veintiocho». Fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
DROP = 13.425; IMP = T['v28']; OFF = IMP - DROP
x = np.zeros((int(END * SR), 2), np.float32)
i0 = int(OFF * SR); n = min(len(a), len(x) - i0); x[i0:i0 + n] += a[:n]
t = np.arange(len(x)) / SR
gap = np.ones(len(x), np.float32); c0, c1 = IMP - .3, IMP - .01
gap[(t > c0) & (t < c1)] = 0; f = int(.04 * SR); j = int(c0 * SR); gap[j - f:j] = np.linspace(1, 0, f)
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1) * gap; x *= g[:, None]
x[:int(IMP * SR)] *= 1.6   # la intro es muy suave: que se oiga bajo la voz
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'golpe', IMP, 'desplazamiento', round(OFF, 3))
