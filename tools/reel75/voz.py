"""Voz del u75 «Un entreno y un avión» (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c
sigue «disabled»; se probó otra vez el 20/11 9:41 y falló sin coste). UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural:
sin cortes, sin acelerar y sin silencios añadidos (35,7 s, 564 caracteres). La voz entra en 0,10 s (0,1 s de cola delante).
Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion, coste 0)."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = 0.10
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
V = np.concatenate([np.zeros(int(O * SR), np.int16), A.astype(np.int16)]); wavfile.write('voz.wav', SR, V)
W = json.load(open('words.json'))
m = lambda s: round(s + O, 3)
K = {'jueves': 0, 'gana': 1, 'polonia': 5, 'hoy': 6, 'irun': 10, 'lider': 13, 'medio': 15, 'entreno': 17, 'avion': 20, 'tu': 21,
     'vuelas': 23, 'lunes': 26, 'pegado': 29, 'partido': 31, 'escribes': 34, 'domingo': 36, 'sin': 37, 'cada': 41, 'guar': 43,
     'acabar': 45, 'jugador': 47, 'uno': 51, 'diez': 53, 'costado': 57, 'con': 58, 'lunes2': 62, 'poco': 66, 'mas': 67,
     'todo': 71, 'menos': 72, 'preg': 73, 'segundo': 76, 'quien': 77, 'cargado': 80, 'sinmirar': 84, 'el28': 86, 'v28': 88,
     'pt': 93, 'lista': 95, 'v27': 100, 'tres': 101, 'gratis': 103}
T = {k: m(W[i]['start']) for k, i in K.items()}
T['camp'] = round(T['pt'] - .26, 3); T['gra'] = T['tres']; T['END'] = round(len(V) / SR + .6, 3)
ph = []; a0 = 0
for i, w in enumerate(W):
    if w['text'][-1] in '.:?' or i == len(W) - 1: ph.append((a0, i)); a0 = i + 1
rows = [(m(W[a]['start']), m(W[b]['end']), ' '.join(w['text'] for w in W[a:b + 1])) for a, b in ph]
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
