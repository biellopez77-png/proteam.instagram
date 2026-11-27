"""Voz del u30 (Mateo – News & Digital Stories de la biblioteca, toma A; la original está desactivada). Sin transcripción
(Hugging Face bloqueado en el turno): las frases se localizan por silencios reales (sil.py) y se asignan al guion por orden
y duración. Cuerpo x1.1, CTA x1.05. Silencio corto antes de «el martes la entrenas». Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32); assert sr == SR
B, C = 1.1, 1.05
P = [('sab', 'Sábado:', .02, .48, B, .10), ('pres', 'presión alta.', .84, 1.67, B, .20), ('mar', 'Martes:', 2.15, 2.72, B, .08),
     ('rondo', 'rondo.', 2.97, 3.44, B, .20), ('jue', 'Jueves:', 3.94, 4.41, B, .08), ('fis', 'físico.', 4.70, 5.19, B, .26),
     ('cuando', '¿Cuándo se entrena la presión?', 5.81, 7.26, B, .28),
     ('app', 'En la app de ProTeam, la semana lleva una frase arriba:', 7.68, 10.61, B, .14),
     ('obj', 'preparar el partido del sábado,', 10.92, 12.59, B, .10), ('obj2', 'presión alta y salida por fuera.', 12.84, 14.85, B, .28),
     ('guarda', 'Guárdatelo:', 15.24, 15.83, B, .14), ('si', 'si la frase está arriba,', 16.18, 17.50, B, .30),
     ('martes', 'el martes la entrenas.', 17.65, 18.95, B, .16),
     ('com', 'Comenta tu deporte, tu categoría y tus días, y te preparo la primera semana.', 19.27, 23.47, C, .14),
     ('seg', 'Y a tu segundo:', 23.77, 24.61, C, .08), ('que', '¿qué frase va arriba de esta semana?', 24.89, 26.68, C, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.10 * SR), np.float32)]; t = .10; T = {}; rows = []
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .05)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); T[key] = round(t + .03 / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
o = lambda key, src, a0, k: round(T[key] - .03 / k + (src - a0 + .03) / k, 3)
T['semana'] = o('app', 8.84, 7.68, B); T['cat'] = o('com', 20.44, 19.27, C); T['dias'] = o('com', 21.23, 19.27, C); T['prep'] = o('com', 21.82, 19.27, C)
T['END'] = round(len(V) / SR + .7, 3)
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
