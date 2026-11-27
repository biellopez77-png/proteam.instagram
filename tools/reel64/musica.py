"""Música del u64: pista NUEVA (ElevenLabs music v2.5, re menor, ~143 BPM, percusión de reloj apagada, dron de cuerda frío, 808 y hi-hats
con tresillos, campana de cristal; 25 s, una toma). Montaje: la pista desde su inicio bajo el hook y la semana del Deportivo; SILENCIO de
0,33 s antes de «Tú no tienes internacionales» (la vuelta) y el beat entra de golpe en «Tú» con 2 compases cortados en golpe
(2,58–5,97 s, 8 tiempos) en bucle hasta el final, con 30 ms de fundido cruzado; fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
X = int(.03 * SR); IMP = T['tu'] - .02; GAP = .33
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
intro = S(0, IMP - GAP); f = int(.12 * SR); intro[-f:] *= np.linspace(1, 0, f)[:, None]
x = np.concatenate([intro, np.zeros((int(GAP * SR), 2), np.float32)])
print('golpe en', len(x) / SR, 'objetivo', IMP)
L0, L1 = 2.58, 5.97; LOOP = S(L0, L1); y = LOOP.copy()
while len(y) < (END - IMP + 1) * SR: y = cat(y, LOOP)
x = np.concatenate([x, y])[:int(END * SR)]; t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
