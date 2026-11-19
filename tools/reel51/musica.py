"""Música del u51: pista nueva (ElevenLabs music v2.5, re menor, ~143 BPM, intro de piano apagado con ambiente de estadio vacío y pad
cálido, sin batería; luego el beat entero con 808 de deslizamientos cortos y hi-hats en tresillos). El beat entra en la toma a los 13,40 s
y se coloca en «nació» (golpe de «ProTeam.»), con 0,3 s de silencio antes. Los 2,96 s iniciales del vídeo llevan una frase de piano de la
propia intro (6,7–9,66 s de la toma). El beat se alarga repitiendo 4 compases (20,12–26,0 s) cortados en golpe, con 30 ms de fundido
cruzado. Fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
DROP = 13.40; IMP = T['nacio']; OFF = IMP - DROP; X = int(.03 * SR)
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
pre = S(6.7, 6.7 + OFF)
body = cat(S(0, 26.83), S(20.12, 26.83)); body = cat(body, S(20.12, 26.83))
x = cat(pre, body)[:int(END * SR)]
if len(x) < int(END * SR): x = np.concatenate([x, np.zeros((int(END * SR) - len(x), 2), np.float32)])
t = np.arange(len(x)) / SR
gap = np.ones(len(x), np.float32); c0, c1 = IMP - .3, IMP - .01
gap[(t > c0) & (t < c1)] = 0; f = int(.04 * SR); j = int(c0 * SR); gap[j - f:j] = np.linspace(1, 0, f)
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1) * gap; x *= g[:, None]
x[:int(IMP * SR)] *= 2.2   # la intro es muy suave: que se oiga bajo la voz
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'golpe', IMP, 'desplazamiento', round(OFF, 3))
