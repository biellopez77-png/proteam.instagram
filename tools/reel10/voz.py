"""Voz del u10 v2 (18/11, corrección de Biel: la norma es de toda España hasta juvenil). Mateo – News & Digital Stories (gpMzl7dbkfC9dIxAqQZT; la
original Rie0luvrYhyKLba1lK3c sigue «disabled by the owner»). UNA toma ENTERA y SEGUIDA a su velocidad natural: sin trocear, sin atempo, sin silencios
añadidos (modelo tools/reel50/voz.py). Tiempos de frase con ElevenLabs Scribe (texto idéntico al guion; coste 0). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json, subprocess
from scipy.io import wavfile
SR = 44100; O = .08
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'voz_a.mp3', '-ac', '1', '-ar', str(SR), 'voz_a.wav'], check=True)
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)
V = np.concatenate([np.zeros(int(O * SR), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
P = [('ent', 'Entra a defender.', 0, 1.12), ('sal', 'Sale a atacar.', 1.32, 2.64), ('doc', 'Tiene doce años.', 2.8, 4.08),
     ('gan', 'Tú ganas una defensa.', 4.24, 5.6), ('med', 'Él se queda sin medio balonmano.', 5.76, 7.52),
     ('eus', 'En España, hasta juvenil,', 7.84, 9.44), ('per', 'ese cambio no se permite.', 9.56, 11.04),
     ('sem', 'Esta semana,', 11.36, 12.16), ('par', 'en el partidillo:', 12.24, 13.28), ('qui', 'quien defiende,', 13.32, 14.16),
     ('ata', 'ataca la siguiente.', 14.32, 15.44), ('ald', 'A los doce,', 15.6, 16.4), ('esp', 'nadie es especialista.', 16.48, 17.8),
     ('seg', 'Pregúntale a tu segundo:', 17.92, 19.12), ('que', '¿quién no ha atacado en todo el año?', 19.36, 21.12),
     ('com', 'Comenta tu categoría y tus días:', 21.44, 23.36), ('pre', 'te preparo la semana en la app de Pro Team.', 23.44, 25.84),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 26.0, 28.56), ('gra', 'tres meses gratis.', 28.68, 30.16)]
T = {}; rows = []
for k, txt, a, b in P: T[k] = round(a + O, 3); T['e' + k] = round(b + O, 3); rows.append((a + O, b + O, txt))
T['camp'] = T['lis']; T['END'] = round(len(V) / SR + .5, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T['esp'], T['camp'], T['END'])
