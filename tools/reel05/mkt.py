"""times.js del u05 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
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
T = dict(un=at('un'), h3=at('3', s=False), cero=at('0', s=False), esc=at('esconder', s=False), prob=at('problemas', s=False), cero2=at('0', 2, s=False), uno=at('1', s=False), euno=at('1', end=True),
         ganas=at('ganas'), lunes=at('lunes', s=False), nadie=at('nadie', s=False), rev=at('revisa', s=False), nada=at('nada', s=False), enada=at('nada', end=True),
         pero=at('pero'), ocas=at('ocasiones', s=False), conc=at('concediste', s=False), siguen=at('siguen', s=False), ahi=at('ahi', s=False), tap=at('tapadas', s=False), marc=at('marcador', s=False), emarc=at('marcador', end=True),
         apunta=at('apunta'), tres2=at('tres', s=False), cada=at('cada', s=False), part=at('partido', s=False), q1=at('que', 3), hic=at('hicieron', s=False), q2=at('que', 4), hiz=at('hiciste', s=False), q3=at('que', 5, s=False), camb=at('cambias', s=False), ecamb=at('cambias', end=True),
         la=at('la', 1), pt=at('proteam', s=False), reg=at('registra', s=False), part2=at('partido', 2, s=False), dir=at('directo', s=False), edir=at('directo', end=True),
         une=at('unete'), antes=at('antes', s=False), n28=at('28', s=False), nov=at('noviembre', s=False), cons=at('consigue', s=False), tresm=at('tres', 2, s=False), gratis=at('gratis', s=False))
T['tres'] = T['tresm']
T['END'] = W[-1][1] + 1.6
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
