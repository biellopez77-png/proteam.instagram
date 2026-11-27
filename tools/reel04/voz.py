"""Voz del u04: sin quitar silencios; cuerpo x1.1, CTA x1.0, pausa antes del CTA <= 0,2 s. Escribe voz.wav y voz.tsv (mapeado)."""
import numpy as np, subprocess
from scipy.io import wavfile
SRC, TSV, K = 'voz_b.ogg', 'voz_b.tsv', 1.1
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',SRC,'-ac','1','-ar','44100','orig.wav'],check=True)
sr, X = wavfile.read('orig.wav'); X = X.astype(np.float32)
W = [l.split('\t') for l in open(TSV).read().strip().split('\n')]; W = [(float(a), float(b), w) for a, b, w in W]
def rms(t): i = int(t*sr); return np.sqrt(np.mean(X[max(0,i-220):i+220]**2))
def quiet(a, b): ts = np.arange(a, b, .005); return float(ts[int(np.argmin([rms(t) for t in ts]))])
def w(word, n=1, end=False):
    k = 0
    for a, b, x in W:
        if x.lower().strip('.,') == word:
            k += 1
            if k == n: return b if end else a
une = w('únete'); ses_end = w('repites', 1, True)
cut = quiet(ses_end + .02, min(une - .05, ses_end + .14))
cut2 = quiet(max(cut, une - .12), une - .02)
body = X[:int(cut*sr)]
wavfile.write('body.wav', sr, body.astype(np.int16))
subprocess.run(['ffmpeg','-loglevel','error','-y','-i','body.wav','-af',f'atempo={K}','body_f.wav'],check=True)
_, B = wavfile.read('body_f.wav')
cta = X[int(cut2*sr):].astype(np.int16)
lead = np.zeros(int(.12*sr), np.int16)
out = np.concatenate([lead, B, cta]); wavfile.write('voz.wav', sr, out)
def m(t): return .12 + t / K if t < cut else .12 + len(B)/sr + (t - cut2)
open('voz.tsv','w').write(''.join(f'{m(a):.3f}\t{m(b):.3f}\t{x}\n' for a, b, x in W))
print('dur', round(len(out)/sr, 2), 'cut', round(cut, 3), 'cut2', round(cut2, 3), 'pausa CTA', round((cut-ses_end)/K + (une-cut2), 3))
