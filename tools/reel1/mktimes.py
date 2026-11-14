"""Genera times.js a partir de las marcas de palabra de la locución (words.tsv: inicio fin palabra) y la pausa insertada tras el gancho."""
import sys, json, unicodedata
W = [l.split('\t') for l in open(sys.argv[1]).read().strip().split('\n')]
W = [(float(a), float(b), unicodedata.normalize('NFD', w.lower()).encode('ascii', 'ignore').decode().strip('.,!?¿¡')) for a, b, w in W]
INS = [tuple(map(float, x.split(':'))) for x in sys.argv[2].split(',')]  # silencios añadidos (en, duración)
import numpy as np
from scipy.io import wavfile
sr_, X = wavfile.read(sys.argv[4]); X = X.astype(float)
def rms(t, w=.015): i = int(t * sr_); return np.sqrt(np.mean(X[max(0, i - int(w * sr_)):i + int(w * sr_)] ** 2) + 1e-9)
def snap(t):  # ajusta el inicio de palabra al arranque real de la voz
    ts = np.arange(max(0, t - .12), t + .4, .005); e = np.array([rms(u) for u in ts]); thr = .2 * e.max()
    quiet = e < .05 * e.max()
    for k in range(1, len(ts)):
        if e[k] > thr and quiet[:k].any(): return float(ts[k])
    return t
def at(word, n=1, end=False):
    k = 0
    for a, b, w in W:
        if w == word:
            k += 1
            if k == n: return (b if end else snap(a))
    raise SystemExit('no encuentro ' + word)
hook_end = at('ellos', end=True)
PAUSE_END = at('tienes')
def S(x): return round(x + sum(d for at_, d in INS if x >= at_), 3)
T = dict(type0=.05, type1=round(hook_end - .05, 3), col0=round(hook_end + .05, 3))
T['s2'] = S(PAUSE_END) - .1; T['colGap'] = round((T['s2'] - T['col0']) / 4, 3)
T['g'] = S(at('ganas')); T['ta'] = S(at('el', 1)); T['s3'] = S(at('y', 1))
T['cnt0'] = T['s3'] + .06; T['hor'] = S(at('horas')); T['cnt1'] = S(at('dia', end=True)) - .2; T['s4'] = S(at('diferencia')) - .25
T['rec'] = S(at('tus')); T['sino'] = S(at('sino')); T['como'] = S(at('como')); T['uti'] = S(at('utilizas'))
T['s6'] = S(at('porque')); T['met'] = S(at('metodologia')); T['her'] = S(at('herramientas')); T['s7'] = S(at('tu'))
T['c7'] = T['exc'] = S(at('excel')); T['wha'] = S(at('whatsapp')); T['lib'] = S(at('libretas')); T['doc'] = S(at('documentos'))
T['cut'] = S(at('documentos', end=True)); T['eso'] = S(at('eso')); T['sis'] = S(at('sistema')); T['s9'] = S(at('sistema', end=True)) + .45
T['web'] = S(at('sistema', end=True)) + .45; T['pt'] = T['web']; T['tap'] = T['web'] + 2.05; T['ok'] = T['tap'] + .45
T['gal'] = S(at('antes')) - .15; T['d28'] = S(at('28')) if any(w == '28' for _, _, w in W) else S(at('del', 1)) + .3
T['s11'] = S(at('y', sum(1 for _, _, w in W if w == 'y'))); T['tres'] = T['s11'] + .12; T['END'] = S(W[-1][1]) + 1.8
T = {k: round(v, 3) for k, v in T.items()}
open(sys.argv[3], 'w').write('window.TIMES = ' + json.dumps(T) + ';\nwindow.DUR = window.TIMES.END;\n')
print(json.dumps(T))
