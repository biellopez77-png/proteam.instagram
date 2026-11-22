"""Voces (Piper, gratis), efectos sintetizados y línea de tiempo del vídeo «Edu y Clara» (estilo bill wurtz).
  python3 tools/wurtz/audio.py   -> tools/wurtz/out/timeline.json y tools/wurtz/out/audio.wav
Cada plano dura lo que diga el guion o lo que necesiten sus frases (lo que sea mayor)."""
import json, os, sys
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'trazo'))
import voz  # motor de voz del repositorio

D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, 'out'); os.makedirs(OUT, exist_ok=True)
SR = 44100
E = ('davefx', 0, 1.06)      # Edu: voz masculina, algo rápida
C = ('sharvard', 1, 0.94)    # Clara: voz femenina, pausada

# (id, duración mínima, [(quién, texto hablado, texto en pantalla o None)], [(segundo, texto en pantalla)], [(segundo, efecto)])
SHOTS = [
 (1, 2.5, [(E, 'tengo cuarenta y tres excels.', '43 excels')], [], [(0, 'room')]),
 (2, 2.3, [(C, 'por qué.', 'por qué')], [], [(0.1, 'squeak')]),
 (3, 3.0, [(E, 'uno por jugador.', 'uno por jugador'), (E, 'uno por semana.', 'uno por semana'), (E, 'y uno que se llama, final final dos.', 'final_final_2')], [], []),
 (4, 2.6, [], [], [(0, 'paper'), (0, 'rain')]),
 (5, 2.5, [(E, 'y el grupo de guasap de los padres.', 'grupo de padres')], [], [(0.1, 'notif')]),
 (6, 2.6, [], [(0.25, '¿mañana a qué hora?'), (0.6, '¿mañana a qué hora?'), (0.9, '¿mañana a qué hora?'), (1.15, '¿mañana a qué hora?'), (1.4, '¿mañana a qué hora?')], [(0.25, 'notif'), (0.6, 'notif'), (0.9, 'notif'), (1.15, 'notif'), (1.4, 'notif')]),
 (7, 2.5, [(E, 'el sábado perdimos.', None), (C, 'lo sé.', None)], [], []),
 (8, 2.8, [(E, 'no sé por qué perdimos.', 'no sé')], [], [(0.9, 'thud')]),
 (9, 2.0, [], [(0.2, '…')], [(0, 'crickets')]),
 (10, 2.2, [(C, 'has probado a no hacer eso.', 'no hacer eso')], [], []),
 (11, 2.6, [(C, 'esto es ProTim.', 'proteam')], [], [(0, 'chime')]),
 (12, 3.0, [(C, 'aquí planifico la semana.', 'la semana'), (C, 'toda. en un sitio.', 'en un sitio')], [], [(0.3, 'click')]),
 (13, 3.0, [(E, 'y los excels.', None), (C, 'se fueron.', 'se fueron')], [], [(0.8, 'flap')]),
 (14, 3.0, [(C, 'en el partido apunto cada acción.', None), (C, 'tiro.', 'tiro'), (C, 'parada.', 'parada'), (C, 'pérdida.', 'pérdida')], [], [(0, 'crowd')]),
 (15, 2.4, [], [(0.2, 'en directo')], [(0.3, 'tick'), (0.8, 'tick'), (1.3, 'tick')]),
 (16, 3.0, [(C, 'y luego me dice por qué perdimos.', None), (E, 'te lo dice.', None)], [], []),
 (17, 3.0, [(C, 'con números.', 'con números')], [(1.3, 'del 10 al 15')], [(1.0, 'marker')]),
 (18, 3.0, [(E, 'y si están cansados.', None), (C, 'también.', 'también')], [], [(1.2, 'lowbat')]),
 (19, 2.6, [], [(0.2, 'rpe'), (1.1, 'quién está cansado')], []),
 (20, 3.0, [(E, 'necesito un momento.', None)], [(1.9, '(un momento)')], [(1.4, 'steps')]),
 (21, 2.4, [(E, 'vale.', 'vale')], [], [(0, 'pop')]),
 (22, 2.8, [], [(0.35, 'lunes.'), (1.0, 'martes.'), (1.65, 'hecho.')], [(0.35, 'click'), (1.0, 'click'), (1.65, 'bell')]),
 (23, 2.6, [(E, 'ganamos.', 'ganamos')], [], [(0, 'buzzer')]),
 (24, 2.8, [], [], [(0, 'choir')]),
 (25, 2.8, [], [(0.4, '8 horas')], [(0.2, 'snore')]),
 (26, 2.8, [], [(0.4, 'hasta los padres')], [(0, 'applause')]),
 (27, 2.6, [(E, 'ahora me sobran cuarenta y tres excels.', None), (C, 'bórralos.', 'bórralos')], [], []),
 (28, 2.6, [(E, 'y qué hago con mi vida.', None), (C, 'entrenar.', 'entrenar')], [], [(0, 'hit')]),
 (29, 4.2, [], [(0.1, 'pruébala con tu equipo'), (0.9, 'pro-team.app')], [(0, 'sting')]),
 (30, 3.2, [], [(1.0, 'adiós final_final_2')], [(0.5, 'whoosh')]),
]

# ---------- efectos (sintetizados)
rng = np.random.default_rng(7)
def mix(parts, d):
    b = np.zeros(int(d * SR))
    for at, x in parts: i = int(at * SR); j = min(len(b), i + len(x)); b[i:j] += x[:j - i]
    return b
def env(n, a, r): t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
def tone(f, d, amp, a=.005, r=.2): n = int(d * SR); t = np.arange(n) / SR; return amp * np.sin(2 * np.pi * f * t) * env(n, a, r)
def noise(d, amp, lp=.2, a=.002, r=.1):
    n = int(d * SR); x = rng.standard_normal(n); y = np.zeros(n); k = 0.
    for i in range(n): k += lp * (x[i] - k); y[i] = k
    return amp * y / (np.abs(y).max() + 1e-9) * env(n, a, r)
def sfx(name):
    if name == 'room': return noise(2.4, .03, .02, .3, 3)
    if name == 'squeak': n = int(.18 * SR); t = np.arange(n) / SR; return .12 * np.sin(2 * np.pi * (1800 + 900 * t / .18) * t) * env(n, .005, .06)
    if name == 'paper': return np.concatenate([noise(.12, .18, .5, .002, .04) for _ in range(8)])
    if name == 'rain': return np.concatenate([np.pad(tone(rng.uniform(1600, 2600), .05, .05, r=.015), (0, int(.12 * SR))) for _ in range(18)])
    if name == 'notif': return np.concatenate([tone(988, .09, .12, r=.05), tone(1319, .14, .12, r=.07)])
    if name == 'thud': return tone(55, .5, .5, a=.002, r=.15)
    if name == 'crickets':
        n = int(2 * SR); t = np.arange(n) / SR; ch = (np.sin(2 * np.pi * 30 * t) > .6) * (np.sin(2 * np.pi * 1.2 * t) > 0)
        return .05 * np.sin(2 * np.pi * 4400 * t) * ch
    if name == 'chime': return mix([(i * .07, tone(f, 1.2, .08, r=.4)) for i, f in enumerate([784, 988, 1175, 1568])], 1.5)
    if name == 'click': return noise(.03, .25, .8, .0005, .008)
    if name == 'flap': return np.concatenate([noise(.08, .15, .1, .01, .03) for _ in range(6)])
    if name == 'crowd': return noise(3.0, .05, .03, .3, 5)
    if name == 'tick': return tone(2400, .04, .15, a=.0005, r=.01)
    if name == 'marker': return noise(.6, .07, .35, .02, 10)[:int(.6 * SR)] * np.minimum(1, (.6 - np.arange(int(.6 * SR)) / SR) / .05)
    if name == 'lowbat': return np.concatenate([tone(660, .12, .1, r=.08), np.zeros(int(.05 * SR)), tone(440, .2, .1, r=.12)])
    if name == 'steps': return np.concatenate([np.pad(noise(.06, .2, .1, .001, .02), (0, int(.3 * SR))) for _ in range(4)])
    if name == 'pop': n = int(.15 * SR); t = np.arange(n) / SR; return .25 * np.sin(2 * np.pi * (300 + 900 * t / .15) * t) * env(n, .002, .05)
    if name == 'bell': return mix([(0, tone(2093, 1.0, .12, r=.35)), (0, tone(3136, .8, .05, r=.25))], 1.0)
    if name == 'buzzer': n = int(1.0 * SR); t = np.arange(n) / SR; return .15 * np.sign(np.sin(2 * np.pi * 220 * t)) * np.minimum(1, (1 - t) / .05)
    if name == 'choir':
        n = int(2.6 * SR); t = np.arange(n) / SR; s = sum(np.sin(2 * np.pi * f * t + .3 * np.sin(2 * np.pi * 5 * t)) for f in [523, 659, 784, 1047])
        return .05 * s * np.minimum(1, t / .3) * np.minimum(1, (2.6 - t) / .5)
    if name == 'snore': n = int(2.4 * SR); t = np.arange(n) / SR; return noise(2.4, .08, .05, .3, 9)[:n] * (.5 + .5 * np.sin(2 * np.pi * .8 * t)) ** 2
    if name == 'applause': return np.concatenate([noise(.04, rng.uniform(.05, .12), .6, .001, .01) for _ in range(60)])
    if name == 'hit': return tone(80, .4, .4, a=.002, r=.1)
    if name == 'sting': return mix([(i * .05, tone(f, 2.0, .07, r=.7)) for i, f in enumerate([523, 659, 784, 1047, 1319])], 2.5)
    if name == 'whoosh': n = int(1.0 * SR); return noise(1.0, .12, .15, .3, .4)[:n] * np.sin(np.linspace(0, np.pi, n))
    raise KeyError(name)

def mix(parts, d):
    b = np.zeros(int(d * SR))
    for at, x in parts: i = int(at * SR); j = min(len(b), i + len(x)); b[i:j] += x[:j - i]
    return b

def add(buf, x, at):
    i = int(at * SR); j = min(len(buf), i + len(x)); buf[i:j] += x[:j - i]

# ---------- voces
engines = {}
def speak(who, text):
    v, sid, vel = who
    if v not in engines: engines[v] = voz.motor(v)
    a = engines[v].generate(text, sid=sid, speed=vel)
    x = voz.resample(np.asarray(a.samples, dtype=np.float64), a.sample_rate)
    nz = np.where(np.abs(x) > .01)[0]; x = x[max(0, nz[0] - 300): nz[-1] + 1500]
    return x / (np.abs(x).max() + 1e-9) * .85

clips = []; t = 0.0; timeline = []
for sid_, dmin, lines, texts, fx in SHOTS:
    cur = 0.25 if lines else 0; L = []
    for who, said, shown in lines:
        x = speak(who, said); d = len(x) / SR
        L.append({'who': 'E' if who is E else 'C', 'said': said, 'text': shown, 'at': round(cur, 3), 'end': round(cur + d, 3)})
        clips.append((t + cur, x)); cur += d + .18
    dur = max(dmin, cur + .25)
    timeline.append({'id': sid_, 'start': round(t, 3), 'dur': round(dur, 3), 'lines': L,
                     'texts': [{'at': a, 'text': s} for a, s in texts], 'fx': [{'at': a, 'name': n} for a, n in fx]})
    for a, n in fx: clips.append((t + a, sfx(n) * .9))
    t += dur
total = t
buf = np.zeros(int((total + .5) * SR))
for at, x in clips: add(buf, np.asarray(x, dtype=np.float64), at)
# música de fondo muy baja (jazz de ascensor sintetizado), sube en el cierre
n = len(buf); tt = np.arange(n) / SR
bass = sum(.02 * np.sin(2 * np.pi * f * tt) * (np.sin(2 * np.pi * .5 * tt) > 0) for f in [110])
buf += bass
buf = buf / (np.abs(buf).max() + 1e-9) * .9
sf.write(os.path.join(OUT, 'audio.wav'), np.stack([buf, buf], 1), SR)
json.dump({'total': round(total, 3), 'shots': timeline}, open(os.path.join(OUT, 'timeline.json'), 'w'), ensure_ascii=False, indent=1)
print('total', round(total, 2), 's ·', len(timeline), 'planos')
