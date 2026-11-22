"""Voz del u33 (17/11): Mateo – News & Digital Stories de la biblioteca (la original Rie0luvrYhyKLba1lK3c sigue desactivada), una toma.
Frases cortadas sobre silencios reales (silencedetect -38 dB). Cuerpo x1.10, campaña x1.0, sin pausa antes del cierre.
Escribe voz.wav, voz.tsv y times.js con las claves del montaje (tir, s2, drop, s3, m, s4, camp, END)."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'voz_a.mp3', '-ac', '1', '-ar', str(SR), 'voz_a.wav'], check=True)
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32)
B, C = 1.10, 1.0
P = [('bra', 'Brazo arriba:', .0, .76, B, .08), ('cua', 'cuatro pases,', 1.09, 1.89, B, .05), ('tir', 'y a tirar.', 2.12, 2.72, B, .16),
     ('has', 'Hasta dos mil veintidós', 3.13, 4.25, B, .04), ('sei', 'eran seis.', 4.38, 5.08, B, .14), ('aho', 'Ahora,', 5.41, 5.81, B, .10),
     ('cu2', 'cuatro.', 6.06, 6.44, B, .30), ('pas', 'Pasivo pitado,', 6.99, 7.82, B, .05), ('bal', 'balón perdido:', 8.03, 8.85, B, .10),
     ('app', 'en la app de Pro Team lo apuntas en directo,', 9.16, 11.39, B, .04), ('lun', 'y el lunes está en la cronología.', 11.56, 13.37, B, .14),
     ('cus', '¿Cuántos perdisteis por pasivo el sábado?', 13.73, 15.60, B, .14),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 16.10, 18.46, C, .05), ('gra', 'tres meses gratis.', 18.73, 20.01, C, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.08 * SR), np.float32)]; t = .08; T = {}; rows = []; S = {}
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .05)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); S[key] = (a2, k); T[key] = round(t + (a - a2) / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
M = {'tir': T['tir'], 's2': round(T['has'] - .12, 3), 'drop': T['cu2'], 's3': round(T['app'] - .12, 3), 'm': round(T['lun'] - .05, 3),
     's4': round(T['cus'] - .12, 3), 'camp': T['lis'], 'gra': T['gra'], 'END': round(len(V) / SR + .5, 3)}
M.update({k: v for k, v in T.items() if k not in M})
open('times.js', 'w').write('window.TIMES = ' + json.dumps(M) + ';\n'); print(M)
