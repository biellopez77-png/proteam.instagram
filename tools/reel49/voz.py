"""Voz del u49 (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue desactivada).
UNA sola toma, ENTERA y SEGUIDA (menos la frase quitada por Biel el 17/11), a su velocidad natural: sin trocear, sin acelerar y sin silencios añadidos (queja de Biel en u12).
Tiempos de frase por silencios reales (silencedetect -38 dB, 0,12 s) y de palabra clave con la transcripción de ElevenLabs Scribe (texto idéntico al guion). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
# Corrección de Biel (17/11): fuera la frase «Hoy no te contamos más.» Un único corte sobre silencios reales (22,39–23,91 s de la toma), con 12 ms de fundido a cada lado.
C0, C1 = 22.39, 23.91; CUT = C1 - C0; f = int(.012 * SR)
A1 = A[:int(C0 * SR)].astype(np.float32); A2 = A[int(C1 * SR):].astype(np.float32)
r = np.linspace(1, 0, f); r = r[:, None] if A.ndim > 1 else r
A1[-f:] *= r; A2[:f] *= r[::-1]
A = np.concatenate([A1, A2]).astype(A.dtype)
V = np.concatenate([np.zeros(int(O * SR), A.dtype), A]); wavfile.write('voz.wav', SR, V)
P = [('min', 'Minuto setenta.', 0.02, 1.05), ('cuan', '¿Cuántos minutos lleva tu nueve?', 1.49, 2.96), ('nolo', 'No lo sabes.', 3.40, 4.21),
     ('ult', 'Último cuarto.', 4.62, 5.49), ('base', 'Tu base no se ha sentado en todo el partido.', 5.80, 8.03), ('cuenta', 'Te das cuenta ahora.', 8.38, 9.36),
     ('desc', 'Descanso.', 9.77, 10.49), ('port', 'Tu portero lleva catorce goles.', 10.82, 12.72), ('par', '¿Y paradas?', 12.98, 13.70),
     ('nadie', 'Nadie las ha contado.', 14.00, 15.05), ('tres', 'Tres banquillos.', 15.44, 16.32), ('mismo', 'El mismo sábado.', 16.63, 17.60),
     ('apu', 'Apunta otro:', 17.88, 18.57), ('sab', 'sábado veintiocho de noviembre.', 18.86, 20.57), ('abre', 'Abre la app de ProTeam.', 20.87, 22.23),
     ('qued', 'Quedan diez días.', 24.07, 25.24), ('mand', 'Mándaselo a tu segundo:', 25.52, 26.73),
     ('cual', '¿cuál de los tres sois?', 26.98, 28.05), ('camp', 'Lista de espera hasta el veintisiete de noviembre:', 28.34, 30.67), ('gra', 'tres meses gratis.', 30.91, 32.16)]
T = {}; rows = []
P = [(k, x, a - (CUT if a > C0 else 0), b - (CUT if a > C0 else 0)) for k, x, a, b in P]
for k, txt, a, b in P: T[k] = round(a + O, 3); T['e' + k] = round(b + O, 3); rows.append((a + O, b + O, txt))
for k, s in [('setenta', .40), ('nueve', 2.64), ('cat', 11.68), ('v28', 19.36), ('diez', 24.48 - CUT), ('v27', 29.44 - CUT)]: T[k] = round(s + O, 3)
T['END'] = round(len(V) / SR + .7, 3)
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
