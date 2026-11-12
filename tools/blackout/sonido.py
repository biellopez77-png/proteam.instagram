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
# música: bombo, charles y un bajo, sintetizados (sin derechos)
mu = spec.get('musica')
if mu:
    bpm = mu.get('bpm', 100); beat = 60 / bpm; vol = mu.get('vol', .5); m = np.zeros(n); t0m = mu.get('desde', 0)
    k_ = np.arange(int(.25 * SR)) / SR; kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-k_ * 30)) * k_) * np.exp(-k_ * 9)
    h_ = np.arange(int(.05 * SR)); hat = rng.normal(0, 1, len(h_)) * np.exp(-h_ / (SR * .008)); hat = hat - lp(hat, .3)
    bass_notes = [41.2, 41.2, 49.0, 36.7]
    b_i = 0; tt = t0m
    while tt < mu.get('hasta', dur):
        k = int(tt * SR); L = min(len(kick), n - k)
        if L > 0: m[k:k + L] += kick[:L] * .9
        k2 = int((tt + beat / 2) * SR); L2 = min(len(hat), n - k2)
        if L2 > 0: m[k2:k2 + L2] += hat[:L2] * .25
        if b_i % 4 == 0:
            f = bass_notes[(b_i // 4) % 4]; Lb = int(beat * 4 * SR); kb = int(tt * SR); xb = np.arange(min(Lb, n - kb)) / SR
            if len(xb): m[kb:kb + len(xb)] += (np.sin(2 * np.pi * f * xb) + .3 * np.sin(2 * np.pi * 2 * f * xb)) * np.exp(-xb * .6) * .35
        tt += beat; b_i += 1
    for w in mu.get('golpes', []):
        k = int(w * SR); L = min(int(.4 * SR), n - k); x = np.arange(L) / SR
        m[k:k + L] += (rng.normal(0, 1, L) * np.exp(-x * 12) * .5 + np.sin(2 * np.pi * 60 * x) * np.exp(-x * 8))
    duck = np.ones(n)
    for at, txt in spec['lineas']: duck[int(at * SR):int((at + .25 * len(txt.split()) + .8) * SR)] = mu.get('duck', .45)
    duck = lp(duck, .0005)
    mix += m * vol * duck
# tele: ruido de canal sin señal y chasquido de apagado
for a0, a1 in spec.get('estatica', []):
    k0, k1 = int(a0 * SR), min(n, int(a1 * SR)); nz = rng.normal(0, 1, k1 - k0); nz = nz - lp(nz, .05)
    mix[k0:k1] += nz * .18 * np.clip(np.minimum(np.arange(k1 - k0), np.arange(k1 - k0)[::-1]) / (SR * .02), 0, 1)
for a0 in spec.get('apagado', []):
    k = int(a0 * SR); L = min(int(.6 * SR), n - k); x = np.arange(L) / SR
    mix[k:k + L] += np.sin(2 * np.pi * (900 * np.exp(-x * 9) + 40) * x) * np.exp(-x * 7) * .35 + rng.normal(0, 1, L) * np.exp(-x * 30) * .3
zz = spec.get('zumbido')
if zz:  # zumbido de tubo de 15,7 kHz suavizado y hum de 50 Hz mientras la tele está encendida
    m = np.zeros(n); k0, k1 = int(zz[0] * SR), min(n, int(zz[1] * SR)); x = np.arange(k1 - k0) / SR
    m[k0:k1] = np.sin(2 * np.pi * 100 * x) * .025 + np.sin(2 * np.pi * 7850 * x) * .006
    mix += m
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
