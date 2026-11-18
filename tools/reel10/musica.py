"""Música del u10 v2 (18/11): pista nueva (ElevenLabs music v2.5, sol menor, ~144 BPM, 808 con slides, hi-hats en tresillo, campana de cristal
sobre pad de cuerdas y ambiente de pabellón). El beat vuelve con fuerza en 12,50 s de la toma: se adelantan 3 compases de la intro (5,0 s, corte en
golpe con 30 ms de fundido) para que ese regreso caiga en «nadie es especialista» (T.esp) y haya música desde el segundo 0.
Silencio de 0,38 s antes de la frase. Fundido de salida de 1,2 s."""
import json, subprocess, numpy as np
from scipy.io import wavfile
SR = 44100
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'm1.mp3', '-ar', str(SR), '-ac', '2', '_m1.wav'], check=True)
y = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
HIT, PRE = 12.50, 5.0; d = T['esp'] - HIT
a = y[:int(PRE * SR)].copy(); f = int(.03 * SR)
x = np.concatenate([a[:-f], a[-f:] * np.linspace(1, 0, f)[:, None] + y[:f] * np.linspace(0, 1, f)[:, None], y[f:]])
x = x[int((PRE - d) * SR):][:int(END * SR)]
if len(x) < int(END * SR): x = np.concatenate([x, np.zeros((int(END * SR) - len(x), 2), np.float32)])
t = np.arange(len(x)) / SR
gap = np.ones(len(x)); ga, gb = T['esp'] - .38, T['esp'] - .015
gap[(t >= ga) & (t < gb)] = 0; g = int(.02 * SR); ia, ib = int(ga * SR), int(gb * SR)
gap[ia - g:ia] = np.linspace(1, 0, g); gap[ib:ib + g] = np.linspace(0, 1, g)
env = np.clip(t / .25, 0, 1) * np.clip((END - t) / 1.2, 0, 1) * gap
x = x * env[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'retraso', round(d, 3))
