"""Voz del u57 «Balón largo al más rápido» (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c
sigue «disabled» desde el 16/11). UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin cortes, sin acelerar y sin silencios
añadidos (35,6 s, 561 caracteres; la voz entra en 0,10 s). Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion)."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = 0
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
V = A.astype(np.int16); wavfile.write('voz.wav', SR, V)
W = json.load(open('words.json'))
m = lambda s: round(s + O, 3)
K = {'futbol': 0, 'balon': 4, 'rapido': 9, 'gana': 10, 'los': 12, 'cinco': 14, 'ni': 15, 'hoy': 18, 'dos': 21, 'en': 25, 'cadetes': 26, 'demas': 28,
     'corren': 30, 'guar': 31, 'martes': 33, 'diez': 34, 'portero': 39, 'corto': 42, 'balon2': 45, 'cintura': 50, 'correr': 51, 'ahora': 54,
     'jueguen': 56, 'siete': 58, 'preg': 59, 'cuantos': 67, 'goles': 68, 'largo2': 73, 'mismo': 75, 'el28': 76, 'v28': 78, 'pt': 83,
     'apun': 84, 'v27': 92, 'gra': 95, 'gratis': 97}
T = {k: m(W[i]['start']) for k, i in K.items()}
T['camp'] = T['apun']; T['END'] = round(len(V) / SR + .6, 3)
ph = []; a0 = 0
for i, w in enumerate(W):
    if w['text'][-1] in '.:?' or i == len(W) - 1: ph.append((a0, i)); a0 = i + 1
rows = [(m(W[a]['start']), m(W[b]['end']), ' '.join(w['text'] for w in W[a:b + 1])) for a, b in ph]
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
