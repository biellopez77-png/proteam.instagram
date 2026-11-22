"""u29 v2 (17/11, encargo de Andrés tras la corrección de Biel en u28): cierre con el contador de la lista de espera.
Añade a la voz ya montada (voz.ogg) el cierre de campaña de Mateo, cortado de la toma de u28 v3 (misma voz de la biblioteca,
sin gastar caracteres): «Lista de espera hasta el veintisiete de noviembre: tres meses gratis.» Reescribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
def load(src, dst):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-ac', '1', '-ar', str(SR), dst], check=True); return wavfile.read(dst)[1].astype(np.float32)
V = load('voz.ogg', '_v.wav'); A = load('../reel28/voz_a.mp3', '_a.wav')
rms = lambda x: float(np.sqrt(np.mean(x ** 2)) + 1e-9)
def cut(a, b):
    a2, b2 = a - .03, b + .05; s = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); s[:f] *= np.linspace(0, 1, f); s[-f:] *= np.linspace(1, 0, f); return s, .03
lis, pl = cut(15.67, 18.16); gra, pg = cut(18.47, 19.79)
k = rms(V[np.abs(V) > 300]) / rms(np.concatenate([lis, gra])[np.abs(np.concatenate([lis, gra])) > 300]); lis *= k; gra *= k
T = json.loads(open('times.js').read().split('=', 1)[1].split(';')[0]); T.pop('END', None)
t0 = len(V) / SR; gap = .10; g2 = .05
out = [V, np.zeros(int(gap * SR), np.float32), lis, np.zeros(int(g2 * SR), np.float32), gra]
T['lis'] = round(t0 + gap + pl, 3); T['elis'] = round(t0 + gap + len(lis) / SR, 3)
T['gra'] = round(T['elis'] + g2 + pg, 3); T['egra'] = round(T['elis'] + g2 + len(gra) / SR, 3)
W = np.concatenate(out); T['camp'] = T['lis']; T['END'] = round(len(W) / SR + .5, 3)
wavfile.write('voz.wav', SR, np.clip(W, -32767, 32767).astype(np.int16))
rows = [l for l in open('voz.tsv').read().splitlines() if l and not l.split('\t')[2].startswith(('Lista de espera', 'tres meses'))]
rows += [f"{T['lis']:.3f}\t{T['elis']:.3f}\tLista de espera hasta el veintisiete de noviembre:", f"{T['gra']:.3f}\t{T['egra']:.3f}\ttres meses gratis."]
open('voz.tsv', 'w').write('\n'.join(rows) + '\n'); open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(k, T)
