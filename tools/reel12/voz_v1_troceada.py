"""Voz del u12 (Mateo – News & Digital Stories de la biblioteca, única toma: la segunda falló por créditos de ElevenLabs agotados;
la original Rie0luvrYhyKLba1lK3c sigue desactivada). Tiempos de palabra con faster-whisper (sandbox de Higgsfield);
cortes sobre silencios reales. Cuerpo x1.15, reto x1.10. Silencio corto antes de «no el acta». Sin pausa antes del CTA.
Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32); assert sr == SR
B, C = 1.15, 1.10
P = [('qp', 'Quinto periodo.', 0.0, 1.16, B, .06), ('yt', 'Y tú, contando cruces en el acta.', 1.18, 3.40, B, .16),
     ('ext', 'En Extremadura,', 3.82, 4.42, B, .05), ('cada', 'cada jugador de minibasket juega dos periodos completos de los cinco primeros.', 4.80, 9.12, B, .16),
     ('guar', 'Guárdatelo:', 9.44, 9.96, B, .06), ('vie', 'el viernes, seis casillas.', 10.32, 11.78, B, .10),
     ('pri', 'Primero colocas a los que menos juegan.', 12.14, 14.06, B, .18),
     ('sab', 'Y el sábado miras el partido,', 14.46, 16.02, B, .30), ('noel', 'no el acta.', 16.42, 17.06, B, .12),
     ('com', 'Comenta deporte, categoría y días:', 17.40, 19.48, B, .06), ('prep', 'te preparo la semana en la app de ProTeam.', 19.92, 21.76, B, .10),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 22.20, 24.50, B, .04), ('tres', 'tres meses gratis.', 24.84, 26.02, B, .14),
     ('preg', 'Pregúntale a tu segundo:', 26.32, 27.38, C, .06), ('qui', '¿quién llevaba el acta en el quinto periodo?', 27.76, 29.72, C, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.08 * SR), np.float32)]; t = .08; T = {}; rows = []; S = {}
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .06)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); S[key] = (a, k, t); T[key] = round(t + (a - a2) / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
def o(key, src):
    a0, k, t0 = S[key]; return round(t0 + (src - max(0, a0 - .03)) / k, 3)
T['cont'] = o('yt', 1.82); T['acta1'] = o('yt', 3.12); T['dos'] = o('cada', 6.56); T['cinco'] = o('cada', 8.22); T['mini'] = o('cada', 5.56)
T['seis'] = o('vie', 10.78); T['menos'] = o('pri', 13.36); T['partido'] = o('sab', 15.58); T['acta2'] = o('noel', 16.76)
T['app'] = o('prep', 21.12); T['acta3'] = o('qui', 28.46); T['quinto3'] = o('qui', 28.94)
T['END'] = round(len(V) / SR + .5, 3)
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
