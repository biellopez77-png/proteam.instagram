"""Voz del Reel 2: pausas solo en silencios reales, cuerpo x1.1, CTA x1.0. Escribe voz.wav y voz.tsv (tiempos de palabra ya mapeados)."""
import numpy as np, subprocess, sys
from scipy.io import wavfile
SRC, TSV, K = 'voz_b.ogg', 'voz_b.tsv', 1.1
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',SRC,'-ac','1','-ar','44100','orig.wav'],check=True)
sr, X = wavfile.read('orig.wav'); X = X.astype(np.float32)
W = [l.split('\t') for l in open(TSV).read().strip().split('\n')]; W = [(float(a), float(b), w) for a, b, w in W]
def quiet(a, b):  # punto más silencioso entre a y b
    ts = np.arange(a, b, .005); e = [np.sqrt(np.mean(X[int(t*sr)-220:int(t*sr)+220]**2)) for t in ts]; return float(ts[int(np.argmin(e))])
def wend(word): return next(b for a, b, w in W if w.lower().strip('.,') == word)
def wstart(word): return next(a for a, b, w in W if w.lower().strip('.,') == word)
cut = quiet(wend('lugar') - .05, wstart('únete') + .12)   # final del cuerpo
ins = [(quiet(wend('construir') - .02, wstart('no') + .1), .30), (quiet(wend('sistema') - .02, wstart('planifican') + .1), .30)]
def seg(a, b): return X[int(a*sr):int(b*sr)]
parts, t0 = [], 0.
for p, d in ins: parts += [seg(t0, p), np.zeros(int(d*sr), np.float32)]; t0 = p
parts.append(seg(t0, cut)); body = np.concatenate(parts)
wavfile.write('body.wav', sr, body.astype(np.int16))
subprocess.run(['ffmpeg','-loglevel','error','-y','-i','body.wav','-af',f'atempo={K}','body_f.wav'],check=True)
_, B = wavfile.read('body_f.wav'); gap = np.zeros(int(.25*sr), np.int16)
cta = seg(cut, len(X)/sr).astype(np.int16)
lead = np.zeros(int(.15*sr), np.int16)
out = np.concatenate([lead, B, gap, cta]); wavfile.write('voz.wav', sr, out)
def m(t):
    if t >= cut: return .15 + len(B)/sr + .25 + (t - cut)
    return .15 + (t + sum(d for p, d in ins if t >= p)) / K
open('voz.tsv','w').write(''.join(f'{m(a):.3f}\t{m(b):.3f}\t{w}\n' for a, b, w in W))
print('dur', round(len(out)/sr, 2), 'cut', round(cut, 2), [round(p, 2) for p, _ in ins])
