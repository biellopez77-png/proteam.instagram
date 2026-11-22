"""Música del u49: pista nueva (ElevenLabs music v2.5, si bemol menor, ~144 BPM, 808 con slides, hi-hats en tresillo, pad granular frío,
percusión de reloj en la intro y ambiente de pabellón). Intro de la toma (0–6,68 s) bajo el hook; desde ahí el beat suena FILTRADO
(paso bajo, «tras la puerta del vestuario») bajo los tres banquillos y el calendario; corte seco 0,38 s antes de «veintiocho»
y el beat de la toma vuelve sin filtro (desde su entrada, 6,68 s) justo en «veintiocho». Fundido de salida de 1,2 s."""
import json, subprocess, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
a = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
HIT = 6.68; IMP = T['v28']; cut = IMP - .38
A = a[:int(cut * SR)].copy()
k = int(HIT * SR); lp = sosfilt(butter(4, 420, 'low', fs=SR, output='sos'), A[k - SR:], axis=0)[SR:]
xf = np.clip((np.arange(len(lp)) / SR) / .25, 0, 1)[:, None]   # el filtro entra en 0,25 s
A[k:] = A[k:] * (1 - xf) * .0 + lp * 1.15 * xf + A[k:] * (1 - xf)
f = int(.15 * SR); A[-f:] *= np.linspace(1, 0, f)[:, None]
B = a[int((HIT - .01) * SR):]
x = np.zeros((int(END * SR), 2), np.float32); x[:len(A)] += A
i0 = int((IMP - .01) * SR); n = min(len(B), len(x) - i0); x[i0:i0 + n] += B[:n]
t = np.arange(len(x)) / SR; g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x *= g[:, None]
x[:i0] *= .85
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'corte', round(cut, 2), 'golpe', IMP, 'B', round(len(B) / SR, 2), 'necesario', round(END - IMP, 2))
