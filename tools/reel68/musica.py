"""Música del u68: pista NUEVA (ElevenLabs music v2.5, fa menor, ~140 BPM, intro de marimba apagada con pad de cinta, beat a los 6,8 s,
corte a 8,2 s y vuelta del beat a los 8,97 s; 15 s, una toma). Pista corta a propósito para no pasar del tope diario de voz (19/11).
Montaje: intro (0,38–6,8 s) bajo «Libreta. Pizarra. Excel. WhatsApp…»; 5 vueltas de 2 compases (8,97–12,40 s, cortadas en golpe,
30 ms de fundido cruzado); el tramo 6,8–8,97 (beat + corte) termina justo en «Pro Team», donde vuelve el beat (golpe de «ProTeam.»);
después 2 compases en bucle hasta el final con fundido de salida de 1,2 s."""
import json, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
S = lambda t0, t1: a[int(t0 * SR):int(t1 * SR)].copy()
DROP, BEAT, L1 = 8.97, 6.8, 12.40; IMP = T['pt'] - .04; X = int(.03 * SR)
def cat(p, q):
    p, q = p.copy(), q.copy(); p[-X:] *= np.linspace(1, 0, X)[:, None]; q[:X] *= np.linspace(0, 1, X)[:, None]
    return np.concatenate([p[:-X], p[-X:] + q[:X], q[X:]])
LOOP = S(DROP, L1); pre_len = IMP - (DROP - BEAT) - 5 * (L1 - DROP) + 6 * .03
x = S(BEAT - pre_len, BEAT)
for _ in range(5): x = cat(x, LOOP)
x = cat(x, S(BEAT, DROP))
print('golpe en', len(x) / SR, 'objetivo', IMP)
x = cat(x, S(DROP, L1))
while len(x) < END * SR: x = cat(x, LOOP)
x = x[:int(END * SR)]; t = np.arange(len(x)) / SR
g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
x[:int(pre_len * SR)] *= 1.8   # la intro de marimba es suave: que se oiga bajo la voz
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR)
