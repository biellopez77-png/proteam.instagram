"""Música del u30: pista nueva m2 (ElevenLabs music v2.5, mi menor, pluck de cristal, rolls de hi-hat). Su corte (13,3–15,1 s)
cae bajo «Guárdatelo: si la frase está arriba» y el beat vuelve justo en «el martes la entrenas» (retraso de la pista).
Fundido de entrada corto y salida de 1,2 s.
v2 (17/11): el cierre con el contador alarga el Reel a 28,3 s; la pista dura 33 s y llega sin bucle."""
import json, subprocess, numpy as np
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'm2.mp3', '-ar', str(SR), '-ac', '2', '_m2.wav'], check=True)
y = wavfile.read('_m2.wav')[1].astype(np.float32) / 32768
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
RET = 15.09; d = T['martes'] - RET                       # retraso (>0) o avance (<0)
x = np.concatenate([np.zeros((int(d * SR), 2), np.float32), y]) if d > 0 else y[int(-d * SR):]
x = x[:int(END * SR)]; n = len(x); t = np.arange(n) / SR
g = np.clip((t - max(d, 0)) / .25, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', n / SR, 'retraso', round(d, 3))
