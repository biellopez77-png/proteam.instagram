"""Música del u72: pista nueva (ElevenLabs music v2.5, sol menor, ~143 BPM; arranca ya con pulso de pluck apagado y bombo suave, parón
con silencio y el beat entero con 808, hi-hats con redobles y un golpe de sintetizador de cristal). El beat de la toma entra a los 6,70 s y
cae en «lunes» (5,94 s del vídeo); el silencio de antes es el de la propia pista. Se alarga repitiendo 2 compases (6,70–10,057 s) cortados en
golpe, con 30 ms de fundido. Fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
DROP = 6.70; IMP = T['lunes']; OFF = IMP - DROP; X = int(.03 * SR); L = 10.057
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
x = cat(cat(S(-OFF, L), S(DROP, L)), S(DROP, 13.45))[:int(END * SR)]
t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'golpe', IMP, 'desplazamiento', round(OFF, 3))
