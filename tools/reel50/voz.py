"""Voz del u50 (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c devolvió «disabled by the owner» el 18/11 0:40).
UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin trocear, sin acelerar y sin silencios añadidos. La toma empieza con la voz en 0,0 s: no se recorta nada.
Tiempos de palabra con ElevenLabs Scribe (texto idéntico al guion; coste 0). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06; TRIM = 0
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A[int(TRIM * SR):].astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None] if A.ndim > 1 else np.linspace(0, 1, f)
V = np.concatenate([np.zeros((int(O * SR),) + A.shape[1:], np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
S = O - TRIM
P = [('dom', 'Domingo, once de la noche.', 0, 1.84), ('sem', 'La semana, sin preparar.', 2.16, 3.88), ('seg', 'Y tu segundo te escribe:', 4.08, 5.36),
     ('que', '¿qué hacemos el martes?', 5.68, 7.12), ('ult', 'Este puede ser el último domingo así.', 7.28, 9.28),
     ('sab', 'El sábado veintiocho de noviembre', 9.68, 11.44), ('abre', 'abre la app de ProTeam,', 11.6, 13.28),
     ('para', 'para entrenadores de fútbol, baloncesto y balonmano.', 13.36, 16.08), ('qued', 'Quedan diez días.', 16.32, 17.84),
     ('mand', 'Mándaselo al que te escribe los domingos a las once.', 17.88, 20.64), ('camp', 'Lista de espera hasta el veintisiete de noviembre:', 20.8, 23.28),
     ('gra', 'tres meses gratis.', 23.36, 24.88)]
T = {}; rows = []
for k, txt, a, b in P: T[k] = round(a + S, 3); T['e' + k] = round(b + S, 3); rows.append((a + S, b + S, txt))
for k, s in [('once', .88), ('noche', 1.44), ('martes', 6.24), ('ultimo', 8.24), ('v28', 10.28), ('fut', 14.32), ('bal', 14.8), ('bm', 15.52), ('diez', 16.8), ('once2', 20.0), ('v27', 21.8)]: T[k] = round(s + S, 3)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
