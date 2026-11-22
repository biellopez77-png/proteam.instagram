"""Música del u29 (v2, 17/11): la misma pista m2 (ElevenLabs music v2.5, fondo tranquilo). Desplazada para que un tiempo
caiga en «Veintisiete» (el gol), hueco corto justo antes. Como el cierre con el contador alarga el Reel a 27,6 s y la pista dura 26 s,
se repiten 16 tiempos cortando en golpe de beat con 30 ms de fundido cruzado. Salida de 1,2 s."""
import json, subprocess, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'm2.ogg', '-ar', str(SR), '-ac', '2', '_m2.wav'], check=True)
y = wavfile.read('_m2.wav')[1].astype(np.float32) / 32768
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END, G = T['END'], T['v27']
ym = librosa.resample(y.mean(1), orig_sr=SR, target_sr=22050); _, b = librosa.beat.beat_track(y=ym, sr=22050); bt = librosa.frames_to_time(b, sr=22050)
off = min(x - G for x in bt if x - G >= 0)
# bucle: corta en el último tiempo con margen y vuelve 16 tiempos atrás
ci = max(i for i, x in enumerate(bt) if x <= len(y) / SR - 1.6); c, r = bt[ci], bt[ci - 16]; f = int(.03 * SR)
A = y[:int(c * SR) + f].copy(); B = y[int(r * SR):].copy(); w = np.linspace(0, 1, f)[:, None]
A[-f:] = A[-f:] * (1 - w) + B[:f] * w; z = np.concatenate([A, B[f:]])
x = z[int(off * SR):][:int(END * SR)]; n = len(x); assert n >= int(END * SR) - 2, n / SR
t = np.arange(n) / SR; g = np.ones(n, np.float32)
g *= 1 - .8 * np.clip((t - (G - .3)) / .06, 0, 1) * np.clip((G - .02 - t) / .02, 0, 1)
g *= np.clip((END - t) / 1.2, 0, 1); x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', n / SR, 'offset', round(off, 3), 'bucle', round(c, 2), '->', round(r, 2))
