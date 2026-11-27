"""Voz del u10 (17/11): Mateo – News & Digital Stories de la biblioteca (la original Rie0luvrYhyKLba1lK3c da «disabled by the owner»), una toma.
Frases cortadas sobre silencios reales (silencedetect -38 dB). Cuerpo x1.10, campaña x1.0, sin pausa antes del cierre.
Silencio corto antes de «doce años» (golpe de música). Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'voz_a.mp3', '-ac', '1', '-ar', str(SR), 'voz_a.wav'], check=True)
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32)
B, C = 1.10, 1.0
P = [('ent', 'Entra a defender.', .0, 1.10, B, .06), ('sal', 'Sale a atacar.', 1.42, 2.43, B, .22), ('doc', 'Tiene doce años.', 2.84, 4.01, B, .12),
     ('gan', 'Tú ganas una defensa.', 4.33, 5.49, B, .06), ('med', 'Él se queda sin medio balonmano.', 5.77, 7.55, B, .14),
     ('eus', 'En los Juegos Escolares de Euskadi,', 8.01, 9.64, B, .04), ('per', 'ese cambio no se permite.', 9.79, 11.35, B, .14),
     ('sem', 'Esta semana,', 11.73, 12.43, B, .04), ('par', 'en el partidillo:', 12.57, 13.49, B, .06), ('qui', 'quien defiende,', 13.69, 14.43, B, .04),
     ('ata', 'ataca la siguiente.', 14.57, 15.67, B, .14), ('ald', 'A los doce,', 16.08, 16.69, B, .04), ('esp', 'nadie es especialista.', 16.80, 18.17, B, .12),
     ('seg', 'Pregúntale a tu segundo:', 18.42, 19.59, B, .05), ('que', '¿quién no ha atacado en todo el año?', 19.85, 21.66, B, .10),
     ('com', 'Comenta tu categoría y tus días:', 22.00, 23.73, B, .04), ('pre', 'te preparo la semana en la app de Pro Team.', 23.93, 26.16, B, .10),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 26.46, 28.93, C, .05), ('gra', 'tres meses gratis.', 29.13, 30.39, C, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.08 * SR), np.float32)]; t = .08; T = {}; rows = []
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .05)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); T[key] = round(t + (a - a2) / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
T['camp'] = T['lis']; T['END'] = round(len(V) / SR + .5, 3)
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T['doc'], T['camp'], T['gra'], T['END'])
