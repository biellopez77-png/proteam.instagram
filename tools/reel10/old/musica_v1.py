"""Música del u10: pista nueva (ElevenLabs music v2.5, fa menor, 142 BPM, 808 con glide, piano de fieltro frío y ambiente de pabellón).
Intro contenida bajo la escena, la norma y la ficha; silencio de 0,38 s antes de «nadie es especialista» y el golpe de la toma (13,53 s)
cae justo en la frase (T.esp). Fundido de entrada corto y salida de 1,2 s."""
import json, subprocess, numpy as np
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'm1.mp3', '-ar', str(SR), '-ac', '2', '_m1.wav'], check=True)
y = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
HIT = 13.53; d = T['esp'] - HIT
x = np.concatenate([np.zeros((int(d * SR), 2), np.float32), y]) if d > 0 else y[int(-d * SR):]
x = x[:int(END * SR)]
if len(x) < int(END * SR): x = np.concatenate([x, np.zeros((int(END * SR) - len(x), 2), np.float32)])
t = np.arange(len(x)) / SR
gap = np.ones(len(x)); a, b = T['esp'] - .38, T['esp'] - .015
gap[(t >= a) & (t < b)] = 0; f = int(.02 * SR); ia, ib = int(a * SR), int(b * SR)
gap[ia - f:ia] = np.linspace(1, 0, f); gap[ib:ib + f] = np.linspace(0, 1, f)
g = np.clip((t - d) / .3, 0, 1) * np.clip((END - t) / 1.2, 0, 1) * gap
x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'retraso', round(d, 3))
