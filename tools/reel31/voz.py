"""Voz del u31 (Mateo – News & Digital Stories de la biblioteca, toma A; la original sigue desactivada). Tiempos de palabra
con faster-whisper (sandbox de Higgsfield) y cortes sobre silencios reales (sil.py). Cuerpo x1.12, reto x1.05.
Silencio corto antes de «no vuelve». Sin pausa antes del reto. Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32); assert sr == SR
B, C = 1.12, 1.05
P = [('oct', 'En octubre tu equipo defendía el bloqueo directo.', .04, 2.69, B, .10), ('hoy', 'Hoy no.', 3.06, 3.50, B, .12),
     ('apu', 'No apuntaste la semana.', 3.97, 5.11, B, .22), ('tres', 'Tres entrenos,', 5.45, 6.25, B, .06),
     ('dos', 'un dos contra dos, diez minutos.', 6.44, 8.27, B, .14), ('pri', '¿Al principio o al final?', 8.60, 10.03, B, .22),
     ('lo', 'Lo que funcionó y no está escrito…', 10.45, 12.46, B, .24), ('vuelve', 'no vuelve.', 12.74, 13.42, B, .20),
     ('app', 'En la app de ProTeam la dejas como plantilla semanal y la aplicas a esta.', 13.83, 17.86, B, .14),
     ('guarda', 'Guárdatelo:', 18.23, 18.84, B, .08), ('dom', 'el domingo,', 19.19, 19.79, B, .03), ('tres2', 'tres apuntes.', 19.94, 20.75, B, .12),
     ('q1', 'Qué hiciste,', 21.04, 21.71, B, .05), ('q2', 'cuánto', 21.94, 22.38, B, .05), ('q3', 'y en qué orden.', 22.54, 23.42, B, .10),
     ('seg', 'Y a tu segundo:', 23.69, 24.46, C, .05), ('que', '¿qué semana de octubre repetiríais mañana?', 24.75, 26.97, C, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.08 * SR), np.float32)]; t = .08; T = {}; rows = []; S = {}
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .05)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); S[key] = (a, k); T[key] = round(t + .03 / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
def o(key, src):
    a0, k = S[key]; return round(T[key] - .03 / k + (src - a0 + .03) / k, 3)
T['bloq'] = o('oct', 1.74); T['diez'] = o('dos', 7.52); T['final'] = o('pri', 9.54); T['plant'] = o('app', 15.62); T['aplic'] = o('app', 16.94)
T['oct2'] = o('que', 25.30); T['man'] = o('que', 26.48)
T['END'] = round(len(V) / SR + .6, 3)
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
