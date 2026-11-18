"""Voz del u12 v2 (18/11, corrección de Biel del 17/11: «revisa la voz, se corta mucho. falta mucha fluidez»).
Mateo – News & Digital Stories (gpMzl7dbkfC9dIxAqQZT; la original Rie0luvrYhyKLba1lK3c sigue desactivada), eleven_v4, UNA toma nueva ENTERA y SEGUIDA
(484 caracteres), a su velocidad natural: sin trocear, sin acelerar y sin silencios añadidos. La versión anterior (15 frases aceleradas ×1,15/×1,10 y pegadas)
queda en voz_v1_troceada.py. Tiempos de palabra con ElevenLabs Scribe (texto idéntico al guion). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_b.wav'); assert sr == SR
V = np.concatenate([np.zeros((int(O * SR),) + A.shape[1:], A.dtype), A]); wavfile.write('voz.wav', SR, V)
P = [('qp', 'Quinto periodo.', 0.0, 0.88), ('yt', 'Y tú, contando cruces en el acta.', 1.28, 3.60),
     ('ext', 'En Extremadura,', 4.00, 4.88), ('cada', 'cada jugador de minibasket juega dos periodos completos de los cinco primeros.', 4.92, 9.36),
     ('guar', 'Guárdatelo:', 9.52, 10.40), ('vie', 'el viernes, seis casillas.', 10.48, 12.20),
     ('pri', 'Primero colocas a los que menos juegan.', 12.32, 14.40),
     ('sab', 'Y el sábado miras el partido,', 14.56, 16.48), ('noel', 'no el acta.', 16.56, 17.28),
     ('com', 'Comenta deporte, categoría y días:', 17.60, 20.00), ('prep', 'te preparo la semana en la app de ProTeam.', 20.08, 22.32),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 22.48, 24.88), ('tres', 'tres meses gratis.', 25.00, 26.40),
     ('preg', 'Pregúntale a tu segundo:', 26.44, 27.72), ('qui', '¿quién llevaba el acta en el quinto periodo?', 27.84, 30.08)]
T = {}; rows = []
for k, txt, a, b in P: T[k] = round(a + O, 3); T['e' + k] = round(b + O, 3); rows.append((a + O, b + O, txt))
for k, s in [('cont', 1.92), ('acta1', 3.32), ('dos', 6.80), ('cinco', 8.40), ('mini', 5.76), ('seis', 11.28), ('menos', 13.60), ('partido', 15.84),
             ('acta2', 17.00), ('app', 21.28), ('acta3', 28.56), ('quinto3', 29.04)]: T[k] = round(s + O, 3)
T['END'] = round(len(V) / SR + .5, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
