"""Voz del u72 (Reel de datos corto; Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT). UNA toma entera y seguida, sin cortes,
sin acelerar y sin silencios añadidos. Tiempos de palabra con ElevenLabs Scribe (idéntica al guion; coste 0)."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
m = lambda s: round(s + O, 3)
P = [('once', 'Once en el campo.', 0, 1.04), ('cinco', 'Cinco en la pista.', 1.36, 2.56), ('siete', 'Siete en la de balonmano.', 2.72, 4.0),
     ('tres', 'Tres deportes, y el mismo lunes:', 4.32, 6.48), ('sem', 'la semana, la convocatoria, los minutos.', 6.52, 9.44),
     ('por', 'Por eso la app de ProTeam es para los tres.', 9.52, 12.32), ('camp', 'Lista de espera hasta el veintisiete de noviembre:', 12.48, 14.96),
     ('gra', 'tres meses gratis.', 15.08, 16.48)]
T = {}; rows = []
for k, txt, s, e in P: T[k] = m(s); T['e' + k] = m(e); rows.append((m(s), m(e), txt))
for k, s in [('mismo', 5.6), ('lunes', 5.88), ('semana', 6.64), ('conv', 7.44), ('min', 8.64), ('pt', 10.4), ('tres2', 11.76), ('v27', 13.44)]: T[k] = m(s)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
