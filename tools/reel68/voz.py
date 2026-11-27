"""Voz del u68 «Cuatro sitios» (Mateo – News & Digital Stories, gpMzl7dbkfC9dIxAqQZT: la original Rie0luvrYhyKLba1lK3c sigue
«disabled by the owner» el 19/11 6:45). UNA sola toma, ENTERA y SEGUIDA, a su velocidad natural: sin cortes, sin acelerar y sin
silencios añadidos (42,8 s, 640 caracteres). Tiempos de palabra con ElevenLabs Scribe (transcripción idéntica al guion; coste 0)."""
import numpy as np, json
from scipy.io import wavfile
SR = 44100; O = .06
sr, A = wavfile.read('voz_a.wav'); assert sr == SR
A = A.astype(np.float32); f = int(.01 * SR); A[:f] *= np.linspace(0, 1, f)[:, None]
V = np.concatenate([np.zeros((int(O * SR), 2), np.float32), A]).astype(np.int16); wavfile.write('voz.wav', SR, V)
W = json.load(open('words.json'))
m = lambda s: round(s + O, 3)
K = {'lib': 'Libreta.', 'piz': 'Pizarra.', 'exc': 'Excel.', 'wa': 'WhatsApp.', 'cua': 'Cuatro', 'equ': 'equipo.', 'si': 'Si', 'hab': 'hablamos.',
     'nos': 'nosotros', 'entr': 'entrenamos.', 'cada': 'cada', 'apu': 'apuntar', 'bus': 'buscar', 'avi': 'avisar', 'perd': 'perdiera',
     'buscab': 'Buscábamos', 'arr': 'arreglarlo.', 'para': 'Para', 'todos': 'todos', 'hasta': 'Hasta', 'decid': 'decidimos', 'crear': 'crearlo.',
     'pt': 'Pro', 'app': 'app', 'sem': 'semana,', 'conv': 'convocatoria', 'jug': 'jugador,', 'mismo': 'mismo', 'llev': 'Llevamos',
     'seis': 'seis', 'v28': 'veintiocho', 'abre': 'abre.', 'pero': 'Pero', 'lista': 'lista', 'cierra': 'cierra', 'v27': 'veintisiete.',
     'quien': 'Quien', 'tres': 'tres', 'gra': 'gratis.', 'enl': 'Enlace'}
IX = {}
for k, w in K.items():
    IX[k] = next(i for i, x in enumerate(W) if x['text'] == w and i not in IX.values())
T = {k: m(W[i]['start']) for k, i in IX.items()}
T['camp'] = T['pero']; T['END'] = round(len(V) / SR + .75, 3)
ph = []; a0 = 0
for i, w in enumerate(W):
    if w['text'][-1] in '.…:' and w['text'] != 'Team:': ph.append((a0, i)); a0 = i + 1
rows = [(m(W[a]['start']), m(W[b]['end']), ' '.join(w['text'] for w in W[a:b + 1])) for a, b in ph]
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
