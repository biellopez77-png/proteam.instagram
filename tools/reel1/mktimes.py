"""Genera times.js a partir de las marcas de palabra de la locución (words.tsv: inicio fin palabra) y la pausa insertada tras el gancho."""
import sys, json, unicodedata
W = [l.split('\t') for l in open(sys.argv[1]).read().strip().split('\n')]
W = [(float(a), float(b), unicodedata.normalize('NFD', w.lower()).encode('ascii', 'ignore').decode().strip('.,!?¿¡')) for a, b, w in W]
INS = [tuple(map(float, x.split(':'))) for x in sys.argv[2].split(',')]  # silencios añadidos (en, duración)
def at(word, n=1, end=False):
    k = 0
    for a, b, w in W:
        if w == word:
            k += 1
            if k == n: return (b if end else a)
    raise SystemExit('no encuentro ' + word)
hook_end = at('ellos', end=True)
def S(x): return round(x + sum(d for at_, d in INS if x >= at_), 3)
T = dict(type0=.05, type1=round(hook_end - .05, 3), col0=round(hook_end + .05, 3))
T['s2'] = S(at('tienes')); T['colGap'] = round((T['s2'] - T['col0']) / 4, 3)
T['g'] = S(at('ganas')); T['ta'] = S(at('el', 1)); T['s3'] = S(at('y', 1))
T['cnt0'] = T['s3'] + .06; T['hor'] = S(at('horas')); T['cnt1'] = S(at('dia', end=True)) - .2; T['s4'] = S(at('diferencia')) - .25
T['rec'] = S(at('tus')); T['sino'] = S(at('sino')); T['como'] = S(at('como')); T['uti'] = S(at('utilizas'))
T['s6'] = S(at('porque')); T['met'] = S(at('metodologia')); T['her'] = S(at('herramientas')); T['s7'] = S(at('tu'))
T['c7'] = T['exc'] = S(at('excel')); T['wha'] = S(at('whatsapp')); T['lib'] = S(at('libretas')); T['doc'] = S(at('documentos'))
T['cut'] = S(at('documentos', end=True)); T['eso'] = S(at('eso')); T['sis'] = S(at('sistema')); T['s9'] = S(at('con', 2)) if False else S(at('sistema', end=True)) + .35
T['pt'] = T['s9'] + .15; T['web'] = S(at('puedes')) + .1; T['tap'] = T['web'] + 1.0; T['ok'] = T['tap'] + .45
T['gal'] = S(at('antes')) - .3; T['d28'] = S(at('28')) if any(w == '28' for _, _, w in W) else S(at('del', 1)) + .3
T['s11'] = S(at('y', sum(1 for _, _, w in W if w == 'y'))); T['tres'] = T['s11'] + .12; T['END'] = S(W[-1][1]) + 1.8
T = {k: round(v, 3) for k, v in T.items()}
open(sys.argv[3], 'w').write('window.TIMES = ' + json.dumps(T) + ';\nwindow.DUR = window.TIMES.END;\n')
print(json.dumps(T))
