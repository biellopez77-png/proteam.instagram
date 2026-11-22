"""Música del u73: pista NUEVA (ElevenLabs music v2.5, si bemol menor, ~136 BPM; sub que late y tic de cronómetro apagado, parón casi
en silencio con dos golpes sueltos y el beat entero con 808 distorsionado, hi-hats con redobles y rimshot; 19 s, una toma). Montaje:
se arranca a 2,59 s de la pista para que el parón caiga bajo el cronómetro rojo («seis minutos con uno menos») y el beat entre de golpe
en «martes»; 2 compases (7,31–10,75 s) en bucle hasta el final, cortados en golpe con 30 ms de fundido; fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
X = int(.03 * SR); DROP = 6.87; OFF = DROP - (T['martes'] - .02)
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
x = S(OFF, 10.75); LOOP = S(7.31, 10.75)
while len(x) < END * SR: x = cat(x, LOOP)
x = x[:int(END * SR)]; t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'desplazamiento', round(OFF, 3))
