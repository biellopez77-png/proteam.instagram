"""Voz del u59 (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue «disabled by the owner» el 18/11 6:50).
UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin trocear, sin acelerar y sin silencios añadidos.
Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion; coste 0). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
S = O
P = [('diez', 'Diez días.', 0, 1.16), ('equipo', 'En tu equipo de balonmano,', 1.36, 2.72), ('si', 'si entrenáis tres días por semana,', 2.8, 4.72),
     ('son', 'son cinco entrenos y dos partidos.', 4.8, 7.24), ('ses', 'Cinco sesiones que vas a preparar de memoria.', 7.44, 9.96),
     ('par', 'Dos partidos que vas a analizar de cabeza.', 10.16, 12.64), ('sab', 'El sábado veintiocho de noviembre', 12.88, 14.56),
     ('abre', 'abre la app de ProTeam,', 14.72, 16.16), ('para', 'para entrenadores de fútbol, baloncesto y balonmano.', 16.24, 19.28),
     ('mand', 'Mándaselo a tu segundo:', 19.36, 20.8), ('cuan', '¿cuántos de esos cinco entrenos tenéis ya escritos?', 20.83, 23.88),
     ('camp', 'Lista de espera hasta el veintisiete de noviembre:', 24.08, 26.8), ('gra', 'tres meses gratis.', 26.92, 28.32)]
T = {}; rows = []
for k, txt, a, b in P: T[k] = round(a + S, 3); T['e' + k] = round(b + S, 3); rows.append((a + S, b + S, txt))
for k, s in [('dias', .48), ('bm', 2.08), ('cinco', 5.12), ('dos', 6.24), ('memoria', 9.4), ('cabeza', 12.0), ('v28', 13.4),
             ('fut', 17.2), ('bal', 17.76), ('bm2', 18.48), ('cinco2', 21.68), ('escritos', 23.16), ('v27', 25.28)]: T[k] = round(s + S, 3)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
