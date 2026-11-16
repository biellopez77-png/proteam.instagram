"""Música del u29: pista nueva m2 (ElevenLabs music v2.5, fondo tranquilo, sin subidones). Desplazada para que un tiempo
caiga en «Veintisiete» (el gol), hueco corto justo antes y salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
y, _ = librosa.load('m2.mp3', sr=SR, mono=False); y = y.T.astype(np.float32)
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); END, G = T['END'], T['v27']
ym, sr = librosa.load('m2.mp3', sr=22050); _, b = librosa.beat.beat_track(y=ym, sr=sr); bt = librosa.frames_to_time(b, sr=sr)
cands = [x - G for x in bt if 0 <= x - G <= len(y) / SR - END - .05]; off = min(cands)
x = y[int(off * SR):][:int(END * SR)]; n = len(x); t = np.arange(n) / SR; g = np.ones(n, np.float32)
g *= 1 - .8 * np.clip((t - (G - .3)) / .06, 0, 1) * np.clip((G - .02 - t) / .02, 0, 1)
g *= np.clip((END - t) / 1.2, 0, 1); x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16)); print('ok', n / SR, 'offset', round(off, 3))
