"""times.js del u03 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
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
T = dict(pi=at('pierdes'), min=at('minuto', s=False), n88=at('88', s=False), e88=at('88', end=True), pero=at('pero'), prob=at('problema', s=False), mar=at('martes', s=False), emar=at('martes', end=True),
         c1=at('cuando'), coche=at('coche', s=False), c2=at('cuando', 2), nadie=at('nadie', s=False), cans=at('cansado', s=False), c3=at('cuando', 3), jue=at('jueves', s=False), rep=at('repetiste', s=False),
         siem=at('siempre', s=False), esiem=at('siempre', end=True), sab=at('el', 7), res=at('resultado', s=False), pero2=at('pero', 2), dec=at('decide', s=False), entre=at('entre', s=False), sem=at('semana', s=False),
         la=at('la'), pt=at('proteam', s=False), plan=at('planificar', s=False), sem2=at('semana', 2, s=False), ses1=at('sesion', s=False), ses2=at('sesion', 2, s=False), eses=at('sesion', 2, end=True),
         une=at('unete'), antes=at('antes', s=False), n28=at('28', s=False), nov=at('noviembre', s=False), cons=at('consigue', s=False), tres=at('tres', s=False), gratis=at('gratis', s=False))
T['END'] = W[-1][1] + 1.6
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
