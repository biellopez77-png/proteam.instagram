"""u30 v2 (17/11, encargo de Andrés tras la corrección de Biel en u28): cierre con el contador de la lista de espera.
Añade a la voz montada (voz.wav de voz.py) el cierre de campaña de Mateo, cortado de la toma de u28 v3 (misma voz de la biblioteca,
sin gastar caracteres): «Lista de espera hasta el veintisiete de noviembre: tres meses gratis.» Reescribe voz.wav, voz.tsv y times.js.
Orden: ffmpeg voz_a.mp3 → voz_a.wav · python3 voz.py · python3 cierre_contador.py"""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
def load(src, dst):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-ac', '1', '-ar', str(SR), dst], check=True); return wavfile.read(dst)[1].astype(np.float32)
V = wavfile.read('voz.wav')[1].astype(np.float32); A = load('../reel28/voz_a.mp3', '_a.wav')
rms = lambda x: float(np.sqrt(np.mean(x[np.abs(x) > 300] ** 2)) + 1e-9)
def cut(a, b):
    s = A[int((a - .03) * SR):int((b + .05) * SR)].copy(); f = int(.008 * SR); s[:f] *= np.linspace(0, 1, f); s[-f:] *= np.linspace(1, 0, f); return s
lis, gra = cut(15.67, 18.16), cut(18.47, 19.79); k = rms(V) / rms(np.concatenate([lis, gra])); lis *= k; gra *= k
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); T.pop('END', None)
t0 = T['eque']; V = V[:int(t0 * SR)]; gap, g2 = .12, .05
W = np.concatenate([V, np.zeros(int(gap * SR), np.float32), lis, np.zeros(int(g2 * SR), np.float32), gra])
T['lis'] = round(t0 + gap + .03, 3); T['elis'] = round(t0 + gap + len(lis) / SR, 3)
T['gra'] = round(T['elis'] + g2 + .03, 3); T['egra'] = round(T['elis'] + g2 + len(gra) / SR, 3); T['camp'] = T['lis']; T['END'] = round(len(W) / SR + .5, 3)
wavfile.write('voz.wav', SR, np.clip(W, -32767, 32767).astype(np.int16))
rows = [l for l in open('voz.tsv').read().splitlines() if l]
rows += [f"{T['lis']:.3f}\t{T['elis']:.3f}\tLista de espera hasta el veintisiete de noviembre:", f"{T['gra']:.3f}\t{T['egra']:.3f}\ttres meses gratis."]
open('voz.tsv', 'w').write('\n'.join(rows) + '\n'); open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(round(k, 3), T['lis'], T['gra'], T['END'])
