"""Música del u50 v2: pista nueva (ElevenLabs music v2.5, fa sostenido menor, ~143 BPM; intro de Rhodes apagado de madrugada con ruido de
vinilo y un pulso grave como de móvil vibrando, sin batería; luego el beat entero con 808 de deslizamientos cortos, hi-hats en semicorcheas
con redobles en tresillo y pluck frío). La toma trae 6 s de silencio entre la intro (0–12,6 s) y el golpe (BEAT s): se quitan.
Intro bajo el problema y la nutrición (3,25–12,55 s de la toma, y vuelve a empezar en 3,25 con 30 ms de fundido cruzado); 0,3 s de silencio
y el beat entra en «Tres líneas» (golpe de la ficha). El beat se alarga repitiendo 4 compases cortados en golpe. Fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
BEAT = float(open('.beat').read()); IMP = T['tres']; X = int(.03 * SR); BAR4 = 4 * 4 * 60 / 143
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
need = IMP - .3
intro = cat(S(3.25, 12.55), S(3.25, 3.25 + need - 9.3 + .03 + .5))[:int(need * SR)]
gap = np.zeros((int(.3 * SR), 2), np.float32)
body = cat(S(BEAT, BEAT + BAR4), S(BEAT, 31.2))
f = int(.04 * SR); intro[-f:] *= np.linspace(1, 0, f)[:, None]
x = np.concatenate([intro * 2.0, gap, body])[:int(END * SR)]
if len(x) < int(END * SR): x = np.concatenate([x, np.zeros((int(END * SR) - len(x), 2), np.float32)])
t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'golpe', IMP)
