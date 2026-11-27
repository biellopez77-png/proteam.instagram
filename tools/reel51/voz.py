"""Voz del u51 (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue «disabled by the owner» el 19/11 0:45).
UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin acelerar y sin silencios añadidos. Un único corte sobre silencio real
(4,12 → 5,62 s de la toma) para quitar la frase «Los jugadores ya se van» (recomendación de Andrés: la toma pasaba de 36 s).
Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion; coste 0). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06; C0, C1 = 4.12, 5.62; SH = C1 - C0
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
a, b = A[:int(C0 * SR)].copy(), A[int(C1 * SR):].copy(); x = int(.01 * SR)
a[-x:] *= np.linspace(1, 0, x)[:, None]; b[:x] *= np.linspace(0, 1, x)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), a, b]).astype(np.int16); wavfile.write('voz.wav', SR, V)
m = lambda s: round((s if s < C0 else s - SH) + O, 3)
P = [('sab', 'Sábado, una y diez.', 0, 1.64), ('acabo', 'El partido acabó hace diez minutos.', 1.84, 4.0),
     ('ent', 'Y el entrenador sigue con él:', 5.76, 7.52), ('quien', 'quién jugó cuánto,', 7.56, 8.8), ('falla', 'qué falló,', 8.88, 9.6),
     ('toca', 'qué toca el martes.', 9.64, 10.88), ('ese', 'Ese problema no lo vimos desde una oficina.', 11.04, 13.6),
     ('lo', 'Lo vivimos en el banquillo.', 13.76, 15.2), ('busc', 'Buscábamos cómo resolverlo.', 15.44, 17.28),
     ('nac', 'Y así nació la app de ProTeam,', 17.44, 19.68), ('para', 'para entrenadores de fútbol, baloncesto y balonmano.', 19.76, 22.68),
     ('hecha', 'Hecha en el banquillo,', 22.8, 24.16), ('noofi', 'no en una oficina.', 24.32, 25.56),
     ('preg', 'Pregunta para tu staff:', 25.76, 27.2), ('cuando', 'cuando acaba el partido, ¿quién de vosotros sigue con él?', 27.24, 30.4),
     ('abre', 'Abre el sábado veintiocho.', 30.48, 32.24), ('camp', 'Lista de espera hasta el veintisiete de noviembre,', 32.4, 34.8),
     ('gra', 'con tres meses gratis.', 34.92, 36.48)]
T = {}; rows = []
for k, txt, s, e in P: T[k] = m(s); T['e' + k] = m(e); rows.append((m(s), m(e), txt))
for k, s in [('diez', 1.12), ('min', 3.12), ('jugo', 7.88), ('martes', 10.16), ('ofi', 12.96), ('banq', 14.64), ('nacio', 17.8), ('pt', 18.88),
             ('fut', 20.72), ('bal', 21.28), ('bm', 22.0), ('banq2', 23.48), ('ofi2', 24.88), ('quien2', 28.507), ('sigue2', 29.36),
             ('v28', 31.32), ('v27', 33.44), ('tres', 35.16)]: T[k] = m(s)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
