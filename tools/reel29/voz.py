"""Voz del u29 (Mateo de la biblioteca, toma A). Sin transcripción (Hugging Face bloqueado en el turno): las frases se
localizan por silencios reales y se asignan al guion por orden y duración. Cuerpo x1.1, CTA x1.05–1.06. Escribe voz.wav, voz.tsv y times.js."""
import numpy as np, subprocess, json
from scipy.io import wavfile
SR = 44100
sr, A = wavfile.read('voz_a.wav'); A = A.astype(np.float32); assert sr == SR
# (clave, texto, ini, fin, tempo, hueco_despues)
P = [('v26', 'Veintiséis a diecisiete.', 0.00, 1.69, 1.1, .26), ('tira', 'Tira tu lateral.', 2.02, 2.87, 1.1, .30),
     ('cinco', 'Cinco toques:', 3.22, 4.00, 1.1, .22), ('quien', 'quién,', 4.28, 4.64, 1.1, .26), ('tiro', 'tiro,', 4.95, 5.28, 1.1, .24),
     ('desde', 'desde dónde,', 5.48, 6.28, 1.1, .22), ('adonde', 'adónde va,', 6.52, 7.12, 1.1, .22), ('gol', 'y gol o parada.', 7.33, 8.80, 1.1, .34),
     ('v27', 'Veintisiete.', 9.30, 10.08, 1.1, .30), ('acabar', 'Al acabar,', 10.43, 10.96, 1.1, .10),
     ('sabes', 'ya sabes quién tiró diez veces', 11.08, 13.00, 1.1, .09), ('seis', 'y metió seis.', 13.11, 13.96, 1.1, .30),
     ('banq', '¿En tu banquillo,', 14.30, 15.04, 1.1, .16), ('apunta', 'quién apunta los tiros?', 15.23, 16.34, 1.1, .30),
     ('asi', 'Así se registra un partido en la app de ProTeam.', 16.77, 19.46, 1.05, .18),
     ('com', 'Comenta tu deporte,', 19.72, 20.73, 1.06, .12), ('cat', 'tu categoría y tus días,', 20.87, 22.23, 1.06, .09),
     ('prep', 'y te preparo la primera semana.', 22.32, 24.03, 1.06, 0)]
def tempo(x, k):
    if k == 1.0: return x
    wavfile.write('_t.wav', SR, x.astype(np.int16)); subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '_t.wav', '-af', f'atempo={k}', '_t2.wav'], check=True)
    return wavfile.read('_t2.wav')[1].astype(np.float32)
out = [np.zeros(int(.10 * SR), np.float32)]; t = .10; T = {}; rows = []
for key, txt, a, b, k, g in P:
    a2, b2 = max(0, a - .03), min(len(A) / SR, b + .04)
    seg = A[int(a2 * SR):int(b2 * SR)].copy(); f = int(.008 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    y = tempo(seg, k); T[key] = round(t + .03 / k, 3); T['e' + key] = round(t + len(y) / SR, 3); rows.append((T[key], T['e' + key], txt))
    out.append(y); t += len(y) / SR; out.append(np.zeros(int(g * SR), np.float32)); t += g
V = np.concatenate(out); wavfile.write('voz.wav', SR, V.astype(np.int16))
open('voz.tsv', 'w').write(''.join(f'{a:.3f}\t{b:.3f}\t{w}\n' for a, b, w in rows))
T['END'] = round(len(V) / SR + .7, 3)
open('times.js', 'w').write('window.TIMES = ' + json.dumps(T) + ';\n'); print(T)
