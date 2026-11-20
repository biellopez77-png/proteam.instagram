"""Música del u57: pista NUEVA (ElevenLabs music v2.5, sol menor, ~143 BPM, pad analógico con filtro, 808 con glissando, hi-hats con
tresillos y grada lejana; 20 s, una toma). Montaje: la intro escasa (pad y hats) bajo el hook con Martínez; SILENCIO de 0,30 s antes de
«cinco» y el beat entra de golpe en «cinco» («Los otros cinco ni la tocan»). Luego la pista sigue y se repiten 16 tiempos cortados en
golpe (12,54–19,20 s) hasta el final, con 30 ms de fundido cruzado; fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
X = int(.03 * SR); DROP = 6.69; IMP = T['cinco'] - .02; GAP = .30; SH = DROP - IMP
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
intro = S(SH, DROP - GAP); f = int(.12 * SR); intro[-f:] *= np.linspace(1, 0, f)[:, None]
x = np.concatenate([intro, np.zeros((int(GAP * SR), 2), np.float32)])
print('golpe en', len(x) / SR, 'objetivo', IMP)
y = S(DROP, 19.20); LOOP = S(12.54, 19.20)
while len(y) < (END - IMP + 1) * SR: y = cat(y, LOOP)
x = np.concatenate([x, y])[:int(END * SR)]; t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
