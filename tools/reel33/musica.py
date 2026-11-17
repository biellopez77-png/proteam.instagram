"""Música del u33 (17/11, con voz: realineada a los nuevos tiempos; misma pista nueva que no sale en otro Reel): pista nueva (ElevenLabs music v2.5, do menor, 143 BPM, 808 distorsionado, arpegio frío y tic de reloj).
Toma m1: intro tensa con silencio; el golpe (6,705 s de la pista) cae en el 6 que pasa a 4 (T.drop). Como la pista acaba en ~14 s, se repiten dos compases desde el golpe (corte en beat, 30 ms). Fundido de salida de 1,2 s."""
import json, subprocess, numpy as np
from scipy.io import wavfile
SR = 44100
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END = T['END']
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', 'm1.mp3', '-ar', str(SR), '-ac', '2', '_m1.wav'], check=True)
y = wavfile.read('_m1.wav')[1].astype(np.float32) / 32768
off = 6.705 - T['drop']; BAR = 60 / 143.55 * 4
# la pista acaba en ~14,0 s: se repiten 2 compases (cortando en golpe de beat, 30 ms de fundido cruzado) hasta el final
L0 = 6.705 + 2 * BAR; seg = y[int(L0 * SR):int((L0 + 2 * BAR) * SR)]
x = y[int(off * SR):int((L0 + 2 * BAR) * SR)]; cf = int(.03 * SR); r = np.linspace(0, 1, cf)[:, None]
while len(x) < int(END * SR):
    x = np.concatenate([x[:-cf], x[-cf:] * (1 - r) + seg[:cf] * r, seg[cf:]])
x = x[:int(END * SR)]
t = np.arange(len(x)) / SR; g = np.clip(t / .05, 0, 1) * np.clip((END - t) / 1.2, 0, 1); x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', len(x) / SR, 'desplazamiento', round(off, 3))
