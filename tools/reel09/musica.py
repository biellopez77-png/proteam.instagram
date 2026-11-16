"""Música del u09: pista nueva m2 (ElevenLabs music v2.5, fondo tranquilo, intro de pad de 13,4 s). El beat entra justo en
«últimos» (palabra de impacto) tras el pad; +4 compases insertados en tiempo fuerte (fundido 30 ms) y salida de 1,2 s."""
import json, numpy as np, librosa
from scipy.io import wavfile
SR = 44100
y, _ = librosa.load('m2.mp3', sr=SR, mono=False); y = y.T.astype(np.float32)
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0])
END, HIT = T['END'], T['ult']
yb, _ = librosa.load('m2.mp3', sr=22050); _, bf = librosa.beat.beat_track(y=yb, sr=22050); BT = librosa.frames_to_time(bf, sr=22050)
DB = BT[0]; BEAT = float(np.median(np.diff(BT[:40])))
off = DB - HIT; x = y[int(off * SR):]
a_src = DB + 16 * BEAT                      # compás 5 del beat (tiempo fuerte)
a = int((a_src - off) * SR); L = int(16 * BEAT * SR); f = int(.03 * SR)
blk = x[a:a + L].copy(); w = np.linspace(0, 1, f)[:, None]
head, tail = x[:a + L].copy(), x[a + L:].copy()
blk2 = x[a:a + L].copy()
blk2[:f] = head[-f:] * (1 - w) + blk2[:f] * w; tail[:f] = blk2[-f:] * (1 - w) + tail[:f] * w
x = np.concatenate([head[:-f], blk2[:-f], tail])
n = int(END * SR); assert len(x) >= n, (len(x) / SR, END); x = x[:n]
t = np.arange(n) / SR; g = np.ones(n, np.float32)
g *= np.clip((END - t) / 1.2, 0, 1)
x = x * g[:, None]
wavfile.write('musica_alineada.wav', SR, (np.clip(x, -1, 1) * 32767).astype(np.int16))
print('ok', round(len(x) / SR, 2), 'offset', round(off, 3), 'beat', round(BEAT, 4), 'primer golpe', round(DB, 3))
