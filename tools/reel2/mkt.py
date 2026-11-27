"""times.js del Reel 2 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
import json, unicodedata, numpy as np
from scipy.io import wavfile
sr, X = wavfile.read('voz.wav'); X = X.astype(float)
W = [l.split('\t') for l in open('voz.tsv').read().strip().split('\n')]
W = [(float(a), float(b), unicodedata.normalize('NFD', w.lower()).encode('ascii', 'ignore').decode().strip('.,')) for a, b, w in W]
def rms(t, w=.012): i = int(t * sr); return np.sqrt(np.mean(X[max(0, i - int(w*sr)):i + int(w*sr)] ** 2) + 1e-9)
def snap(t):
    ts = np.arange(max(0, t - .12), t + .45, .005); e = np.array([rms(u) for u in ts]); thr = .2 * e.max(); q = e < .06 * e.max()
    for k in range(1, len(ts)):
        if e[k] > thr and q[:k].any(): return float(ts[k])
    return t
def at(word, n=1, end=False, s=True):
    k = 0
    for a, b, w in W:
        if w == word:
            k += 1
            if k == n: return b if end else (snap(a) if s else a)
    raise SystemExit('falta ' + word)
T = dict(los=at('los'), tu=at('tu', s=False), con=at('construir', s=False), no=at('no'), tal=at('talento', s=False), ni1=at('ni'), ni2=at('ni', 2),
         y1=at('y'), veinte=at('20', s=False), per=at('personas', end=True), los2=at('los', 2), forma=at('forma', s=False), llama=at('llama', s=False),
         sis=at('sistema', s=False), pla=at('planifican'), reg=at('registran'), ana=at('analizan'), y2=at('y', 3), dec=at('decisiones', s=False),
         obj=at('objetivo', s=False), pt=at('la', 1), herr=at('herramientas', s=False), sis2=at('sistema', 2, s=False), solo=at('solo', 2, s=False),
         une=0, lug=at('lugar', end=True), ptw=at('proteam', s=False), antes=at('antes', s=False), n28=at('28', s=False), nov=at('noviembre', s=False), cons=at('consigue', s=False),
         tres=at('3', s=False), gratis=at('gratis', s=False))
def onset(t0, t1):
    for u in np.arange(t0, t1, .005):
        if rms(u) > .2 * max(rms(v) for v in np.arange(t0, t1, .02)): return float(u)
T['une'] = onset(at('lugar', end=True) + .1, at('a', 1, s=False) + .2)
T['END'] = W[-1][1] + 1.6
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
