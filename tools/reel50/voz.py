"""Voz del u50 v2 (19/11 3:45, corrección de Biel: problema → nutrición → CTA + solución). Mateo – News & Digital Stories
(gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue «disabled by the owner» el 19/11 3:40). UNA toma entera y seguida,
a su velocidad natural, sin cortes ni silencios añadidos (27,5 s, 453 caracteres). Tiempos de palabra con ElevenLabs Scribe (coste 0,
transcripción idéntica al guion). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
m = lambda s: round(s + O, 3)
P = [('dom', 'Domingo, once de la noche.', 0, 1.76), ('sem', 'La semana, sin preparar.', 2.08, 3.52),
     ('seg', 'Y tu segundo te escribe:', 3.84, 5.12), ('que', '¿qué hacemos el martes?', 5.36, 6.64),
     ('entre', 'Entre el partido y el lunes', 6.72, 8.0), ('nohay', 'no hay otro hueco.', 8.16, 9.36),
     ('hazlo', 'Hazlo el sábado, al recoger:', 9.44, 11.2), ('falla', 'qué falló,', 11.28, 11.92), ('toca', 'qué toca el martes', 11.96, 12.8),
     ('rep', 'y qué repites el jueves.', 12.96, 14.72), ('tres', 'Tres líneas.', 14.8, 15.76),
     ('ysi', 'Y si la quieres montada:', 15.92, 17.28), ('app', 'la app de ProTeam,', 17.32, 18.48),
     ('para', 'para planificar la semana y cada sesión.', 18.56, 20.88),
     ('mand', 'Mándaselo al que te escribe los domingos a las once.', 20.933, 23.52),
     ('camp', 'Lista de espera hasta el veintisiete de noviembre:', 23.68, 26.08), ('gra', 'tres meses gratis.', 26.2, 27.52)]
T = {}; rows = []
for k, txt, s, e in P: T[k] = m(s); T['e' + k] = m(e); rows.append((m(s), m(e), txt))
for k, s in [('once', .8), ('noche', 1.36), ('martes', 5.92), ('hueco', 8.72), ('sab', 9.76), ('recoger', 10.48), ('martes2', 12.4),
             ('jueves', 13.92), ('lineas', 15.12), ('montada', 16.56), ('pt', 17.84), ('planif', 18.72), ('semana2', 19.36), ('sesion', 20.16),
             ('domingos', 22.32), ('once2', 23.04), ('v27', 24.64), ('meses', 26.48)]: T[k] = m(s)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
