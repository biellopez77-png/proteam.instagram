"""times.js del u04 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
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
T = dict(tu=at('tu'), mejor=at('mejor', s=False), rep=at('repetir', s=False), erep=at('repetir', end=True), no2=at('no', 2), apun=at('apuntaste', s=False), eapun=at('apuntaste', end=True),
         aquel=at('aquel'), oct=at('octubre', s=False), todo=at('todo', s=False), enc=at('encajo', s=False), ej=at('el'), ejer=at('ejercicio', s=False), tie=at('tiempos', s=False), par=at('parejas', s=False), epar=at('parejas', end=True),
         hoy=at('hoy'), queda=at('queda', s=False), sens=at('sensacion', s=False), esens=at('sensacion', end=True), y=at('y'), sens2=at('sensaciones', s=False), no3=at('no', 3, s=False), rept=at('repiten', s=False), erept=at('repiten', end=True),
         la=at('la', 2), pt=at('proteam', s=False), guarda=at('guarda', s=False), ses=at('sesiones', s=False), ejs=at('ejercicios', s=False), bib=at('biblioteca', s=False), ebib=at('biblioteca', end=True),
         la2=at('la', 3), abres=at('abres', s=False), repi=at('repites', s=False), erepi=at('repites', end=True),
         une=at('unete'), antes=at('antes', s=False), n28=at('28', s=False), nov=at('noviembre', s=False), cons=at('consigue', s=False), tres=at('tres', s=False), gratis=at('gratis', s=False))
T['END'] = W[-1][1] + 1.6
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
