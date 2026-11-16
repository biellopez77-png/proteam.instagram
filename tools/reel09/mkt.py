"""times.js del u09 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
import json, unicodedata, numpy as np
from scipy.io import wavfile
sr, X = wavfile.read('voz.wav'); X = X.astype(float)
W = [l.split('\t') for l in open('voz.tsv').read().strip().split('\n')]
W = [(float(a), float(b), unicodedata.normalize('NFD', w.lower()).encode('ascii', 'ignore').decode().strip('.,¿?:-')) for a, b, w in W]
def rms(t, w=.012): i = int(t * sr); return np.sqrt(np.mean(X[max(0, i - int(w*sr)):i + int(w*sr)] ** 2) + 1e-9)
def snap(t):
    ts = np.arange(max(0, t - .12), t + .45, .005); e = np.array([rms(u) for u in ts]); thr = .2 * e.max(); q = e < .06 * e.max()
    for k in range(1, len(ts)):
        if e[k] > thr and q[:k].any(): return float(ts[k])
    return t
def at(word, n=1, end=False, s=False):
    k = 0
    for a, b, w in W:
        if w == word:
            k += 1
            if k == n: return b if end else (snap(a) if s else a)
    raise SystemExit('falta ' + word)
T = dict(doce=at('doce'), sie=at('siempre', s=True), ult=at('ultimos', s=True), doce2=at('doce', 2), cuando=at('cuando', s=True), decid=at('decidido'),
         nada=at('nada'), cum=at('cumples', s=True), norma=at('norma'), el=at('el', 2, s=True), apr=at('aprende'), cuen=at('cuentan'), ecuen=at('cuentan', end=True),
         este=at('este', s=True), doce3=at('doce', 3), desc=at('descanso'), marc=at('marcador'), vivo=at('vivo'), mand=at('mandaselo', s=True),
         seg=at('segundo'), lleve=at('lleve'), reloj=at('reloj'), com=at('comenta', s=True), cat=at('categoria'), dias=at('dias'), te=at('te', s=True),
         sem=at('semana'), app=at('app'), pt=at('pro'), lista=at('lista', s=True), n27=at('27'), nov=at('noviembre'), tres=at('tres'), gratis=at('gratis'),
         preg=at('preguntale', s=True), cuan=at('cuando', 2), ult2=at('ultimo'), sab2=at('sabado', 2), esab2=at('sabado', 2, True))
T['END'] = T['esab2'] + .7
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
