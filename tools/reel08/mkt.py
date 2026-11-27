"""times.js del u08 a partir de voz.tsv (ya mapeado) + snap por energía sobre voz.wav."""
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
T = dict(ese=at('ese', s=True), prob=at('problema', s=True), la=at('la', s=True), mur=at('muralla'), agu=at('aguanta'), nadie=at('nadie'), apr=at('aprende'),
         uno1=at('uno'), euno1=at('uno', 2, True), eu=at('en', 2, s=True), inf=at('infantil'), dos=at('dos'), lin=at('lineas'), elin=at('lineas', end=True),
         esta=at('esta', s=True), diez=at('10'), sin=at('sin'), ayu=at('ayudas'), el6=at('el', 2, s=True), cad=at('cadetes'), ecad=at('cadetes', end=True),
         com=at('comenta', s=True), cat=at('categoria'), dias=at('dias'), te=at('te'), sem=at('semana', 2), app=at('app'), pt=at('proteam'),
         lista=at('lista', s=True), n27=at('27'), nov=at('noviembre'), tres=at('tres'), gratis=at('gratis'), preg=at('preguntale', s=True), seg=at('segundo'),
         cuan=at('cuantos'), uno3=at('uno', 5), defe=at('defendieron'), sab=at('sabado'), esab=at('sabado', end=True))
T['END'] = T['esab'] + .7
T = {k: round(v, 3) for k, v in T.items()}
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
