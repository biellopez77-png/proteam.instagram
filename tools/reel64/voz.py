"""Voz del u64 «Cinco jugadores fuera» (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue
«disabled by the owner» el 20/11 3:45). UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin cortes, sin acelerar y sin
silencios añadidos (35,1 s, 572 caracteres). Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion; coste 0)."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
W = json.load(open('words.json'))
m = lambda s: round(s + O, 3)
K = {'cinco': 'Cinco', 'cuatro': 'cuatro', 'ult': 'último', 'es': 'Es', 'depor': 'Deportivo,', 'sab': 'sábado.', 'tu': 'Tú', 'inter': 'internacionales.',
     'tienes': 'Tienes', 'examen': 'examen', 'martes': 'martes', 'solo': 'solo', 'viernes': 'viernes.', 'escr': 'escribes', 'como': 'como', 'todos1': 'todos.',
     'guar': 'Guárdatelo:', 'antes': 'antes', 'apunta': 'apunta', 'necesita': 'necesita', 'mas': 'más', 'preg': 'Pregúntale', 'que2': '¿qué',
     'entr': 'entrenáis', 'todos2': 'todos?', 'el28': 'El', 'v28': 'veintiocho', 'pt': 'Pro', 'apun': 'Apúntate', 'v27': 'veintisiete', 'gra': 'tres', 'gratis': 'gratis.'}
IX = {}
for k, w in K.items():
    IX[k] = next(i for i, x in enumerate(W) if x['text'] == w and i not in IX.values() and (k != 'el28' or i > 70))
T = {k: m(W[i]['start']) for k, i in IX.items()}
T['camp'] = T['apun']; T['END'] = round(len(V) / SR + .75, 3)
ph = []; a0 = 0
for i, w in enumerate(W):
    if w['text'][-1] in '.:?,' and (w['text'][-1] != ',' or w['text'] in ('todos,',)) or i == len(W) - 1: ph.append((a0, i)); a0 = i + 1
rows = [(m(W[a]['start']), m(W[b]['end']), ' '.join(w['text'] for w in W[a:b + 1])) for a, b in ph]
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
