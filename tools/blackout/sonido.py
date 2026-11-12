"""Audio de los Reels de Blackout Friday: voz Kokoro (gratis, local) + ambiente sintetizado.
  python3 sonido.py reels/r01.json  -> reels/r01.wav  (json: {dur, voz_sid, lineas:[[t, texto]], clunks:[t], dark_at})"""
import sys, json, numpy as np, soundfile as sf
sys.path.insert(0, '/home/claude/tts'); import kok
SR = 24000
def lp(x, a):  # paso bajo de un polo
    y = np.zeros_like(x); acc = 0.
    for i in range(len(x)): acc += a * (x[i] - acc); y[i] = acc
    return y
spec = json.load(open(sys.argv[1])); dur = spec['dur']; n = int(dur * SR); mix = np.zeros(n)
t = np.arange(n) / SR; rng = np.random.default_rng(1)
dark = spec.get('dark_at', 99)
# zumbido de pabellón con luces encendidas (50 Hz + armónicos + aire)
hum = (np.sin(2 * np.pi * 100 * t) * .5 + np.sin(2 * np.pi * 150 * t) * .2) * .02 + lp(rng.normal(0, 1, n), .02) * .05
mix += hum * np.clip((dark - t) / .2, 0, 1)
# golpe de interruptor por cada fila
for c in spec.get('clunks', []):
    k = int(c * SR); L = int(.5 * SR); e = np.exp(-np.arange(L) / (SR * .06))
    s = (np.sin(2 * np.pi * 55 * np.arange(L) / SR) * .8 + lp(rng.normal(0, 1, L), .2) * .6) * e * .55
    mix[k:k + L] += s[:n - k]
# dron grave tras el apagón
dr = (np.sin(2 * np.pi * 41 * t) + .5 * np.sin(2 * np.pi * 61.5 * t + .3) + .3 * lp(rng.normal(0, 1, n), .004) * 8) * .05
mix += dr * np.clip((t - dark) / 3, 0, 1) * np.clip((dur - t) / .8, 0, 1)
# voz
import tempfile, os
for at, txt in spec['lineas']:
    tmp = tempfile.mktemp(suffix='.wav'); kok.say(txt, spec.get('voz_sid', 29), tmp, spec.get('vel', .95))
    v, sr = sf.read(tmp); os.remove(tmp)
    if sr != SR: v = np.interp(np.arange(0, len(v), sr / SR), np.arange(len(v)), v)
    k = int(at * SR); mix[k:k + len(v)] += v[:n - k] * .9
    print(f'{at:5.2f}-{at + len(v) / SR:5.2f} {txt}')
mix /= max(1e-6, np.abs(mix).max()) / .89
sf.write(sys.argv[1].replace('.json', '.wav'), mix, SR)
