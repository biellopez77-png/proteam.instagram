"""Música del u75: pista NUEVA (ElevenLabs music v2.5, re menor, ~141 BPM, arpegio pulsado de cristal, pad de aire, 808 con
glissandos cortos, hi-hats con tresillos y pabellón lejano; 20 s, una toma). Montaje: la intro escasa (pad y arpegio) bajo el
hook de los dos partidos; SILENCIO de 0,30 s y el beat entra de golpe en «Tú» («Tú no vuelas»). Después la pista sigue y se repite
el tramo 11,58–19,30 s (de golpe a golpe) hasta el final, con 30 ms de fundido cruzado; fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
X = int(.03 * SR); DROP = 6.86; IMP = T['tu'] - .02; GAP = .30
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
lead = IMP - DROP                      # la intro empieza algo después de la voz
intro = S(0, DROP - GAP); f = int(.12 * SR); intro[-f:] *= np.linspace(1, 0, f)[:, None]
fi = int(.25 * SR); intro[:fi] *= np.linspace(0, 1, fi)[:, None]
x = np.concatenate([np.zeros((int(lead * SR), 2), np.float32), intro, np.zeros((int(GAP * SR), 2), np.float32)])
print('golpe en', len(x) / SR, 'objetivo', IMP)
y = S(DROP, 19.30); LOOP = S(11.58, 19.30)
while len(y) < (END - IMP + 1) * SR: y = cat(y, LOOP)
x = np.concatenate([x, y])[:int(END * SR)]; t = np.arange(len(x)) / SR
g = np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
