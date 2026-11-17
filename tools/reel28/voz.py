"""Voz del u28 (17/11): Mateo – News & Digital Stories de la biblioteca (la original Rie0luvrYhyKLba1lK3c sigue desactivada), una toma.
Frases cortadas sobre silencios reales (silencedetect -38 dB) — el contenedor no llega a Hugging Face para faster-whisper.
Cuerpo x1.10, campaña x1.0, sin pausa antes del cierre. Escribe voz.wav, voz.tsv y times.js (mismas claves que el montaje)."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'voz_a.mp3', '-ac', '1', '-ar', str(SR), 'voz_a.wav'], check=True)
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32)
B, C = 1.10, 1.0
P = [('les', 'Lesión número uno en baloncesto:', .0, 1.97, B, .06), ('tob', 'el tobillo.', 2.31, 2.98, B, .14),
     ('sem', '¿Está en tu semana?', 3.42, 4.24, B, .16), ('dic', 'Dieciséis temporadas universitarias en Estados Unidos:', 4.82, 7.83, B, .06),
     ('esg', 'el esguince de tobillo,', 8.13, 9.26, B, .04), ('pri', 'el primero de la lista.', 9.47, 10.73, B, .14),
     ('app', 'En la app de Pro Team tienes tu rutina de tobillo.', 11.13, 13.74, B, .12),
     ('cua', '¿Cuándo lo entrenasteis por última vez?', 14.12, 15.81, B, .14),
     ('lis', 'Lista de espera hasta el veintisiete de noviembre:', 16.29, 18.81, C, .05), ('gra', 'tres meses gratis.', 19.12, 20.40, C, 0)]
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
# claves del montaje
M = {'b1': T['tob'], 'q1': T['sem'], 's2': round(T['dic'] - .12, 3), 'd3': T['pri'], 's3': round(T['app'] - .12, 3),
     'h1': round(T['app'] + 1.0, 3), 'jug': round(T['app'] + 1.5, 3), 's4': round(T['cua'] - .12, 3), 'r1': T['cua'], 'r2': round(T['cua'] + .55, 3),
     'camp': T['lis'], 'END': round(len(V) / SR + .5, 3)}
M.update({k: v for k, v in T.items() if k not in M})
open('times.js', 'w').write('window.TIMES = ' + json.dumps(M) + ';\n'); print(M)
