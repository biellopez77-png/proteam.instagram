"""Sonido sencillo para Reels de Trazo, sintetizado (sin música con derechos).
  python3 tools/trazo/sonido.py presentacion out.wav
Para otras escenas: añade una función con la lista de eventos (golpes, avisos, subida, acorde)."""
import sys, wave
import numpy as np

SR = 44100


def env(n, a=0.01, r=0.3):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)


def tone(f, dur, amp, a=0.01, r=0.4, harm=(1, .3, .1)):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(h * np.sin(2 * np.pi * f * (i + 1) * t) for i, h in enumerate(harm))
    return amp * s * env(n, a, r)


def noise_burst(dur, amp, r=0.04, lp=0.15):
    n = int(dur * SR); x = np.random.default_rng(1).standard_normal(n)
    y = np.zeros(n); k = 0.0
    for i in range(n): k += lp * (x[i] - k); y[i] = k
    return amp * y * env(n, 0.001, r) / (np.abs(y).max() + 1e-9)


def pad(freqs, dur, amp, fade=1.5):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .2 * t) * .3) for f in freqs) / len(freqs)
    e = np.minimum(1, t / fade) * np.minimum(1, (dur - t) / fade)
    return amp * s * e


def add(buf, s, at):
    i = int(at * SR); j = min(len(buf), i + len(s)); buf[i:j] += s[:j - i]


def presentacion(dur=25.0):
    b = np.zeros(int(dur * SR))
    add(b, pad([110, 130.8, 164.8], 10.6, .10), 0)              # tensión (la menor)
    for i in range(8): add(b, tone(1318 if i % 2 else 1175, .25, .10, r=.08), .5 + i * .42 + .27)   # avisos de mensaje
    for i, t0 in enumerate([4.6, 5.2, 5.8, 7.2, 7.8, 8.3, 8.8, 9.2]): add(b, noise_burst(.25, .22, r=.05), t0 + .27)
    add(b, tone(220, .5, .10, r=.2), 0.1)                                   # aviso del 40
    n = int(.8 * SR); t = np.arange(n) / SR                                 # subida al levantar el brazo
    sweep = np.sin(2 * np.pi * (200 * t + 900 * t * t)) * np.minimum(1, t / .6) * np.exp(-np.maximum(0, t - .6) / .1)
    add(b, .12 * sweep + noise_burst(.8, .08, r=.5, lp=.05), 10.55)
    add(b, pad([130.8, 196, 261.6, 329.6], 9.4, .11, fade=1.2), 11.4)      # orden (do mayor)
    for i in range(7): add(b, tone([523, 587, 659, 698, 784, 880, 988][i], .4, .07, r=.25), 12.3 + i * .12)
    add(b, tone(65.4, 3.5, .22, a=.005, r=1.2, harm=(1, .5, .2)), 21.4)    # golpe final
    add(b, tone(1046, 2.5, .06, r=1.0), 21.45); add(b, tone(1568, 2.5, .03, r=.8), 21.5)
    add(b, pad([261.6, 329.6, 392], 3.6, .07, fade=.8), 21.4)
    return b


if __name__ == '__main__':
    b = globals()[sys.argv[1]]()
    b = b / (np.abs(b).max() + 1e-9) * .8
    st = np.stack([b, b], 1)
    with wave.open(sys.argv[2], 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype('<i2').tobytes())
    print(sys.argv[2])
