"""Música original para «Hola, ProTeam» (120 ppm, 34 s), sintetizada: sin derechos de terceros."""
import sys, wave, numpy as np
SR = 44100; DUR = 34.0; BEAT = .5
b = np.zeros(int(DUR * SR))
def add(s, t):
    i = int(t * SR); j = min(len(b), i + len(s)); b[i:j] += s[:j - i]
def env(n, a, r): t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
def kick():
    n = int(.4 * SR); t = np.arange(n) / SR; f = 50 + 110 * np.exp(-t * 30); return .9 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7)
def clap():
    n = int(.25 * SR); x = np.random.default_rng(3).standard_normal(n); return .35 * np.diff(np.r_[0, x]) * env(n, .001, .05)
def hat(o=.12):
    n = int(.08 * SR); x = np.random.default_rng(5).standard_normal(n); return o * np.diff(np.r_[0, x]) * env(n, .0005, .015)
def note(f, d, amp=.18, a=.005, r=.25, saw=True):
    n = int(d * SR); t = np.arange(n) / SR
    w = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 7)) if saw else np.sin(2 * np.pi * f * t)
    return amp * w * env(n, a, r)
def pad(fs, d, amp=.07):
    n = int(d * SR); t = np.arange(n) / SR; s = sum(np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * f * 2.003 * t) for f in fs) / len(fs)
    return amp * s * np.minimum(1, t / .4) * np.minimum(1, (d - t) / .4)
# acordes por compás (2 s): La m – Fa – Do – Sol, brillante
CH = [[220, 261.6, 329.6], [174.6, 220, 261.6], [261.6, 329.6, 392], [196, 246.9, 293.7]]
BASS = [110, 87.3, 130.8, 98]
for bar in range(17):
    t0 = bar * 2.0; c = CH[bar % 4]
    full = 2.5 <= t0 < 29.5
    if t0 >= 2.0: add(pad(c, 2.0, .06 if full else .09), t0)
    if full:
        for k in range(4):
            add(kick(), t0 + k * BEAT)
            if k % 2: add(clap(), t0 + k * BEAT)
            add(hat(), t0 + k * BEAT + .25)
            add(note(BASS[bar % 4], .22, .16, r=.12, saw=False) + note(BASS[bar % 4] * 2, .22, .05, r=.1), t0 + k * BEAT + .25)
        for k in range(8):   # arpegio
            add(note(c[k % 3] * 2, .2, .045, r=.09), t0 + k * .25)
# intro (0–2.5): notas sueltas tipo «hola»
for i, (f, t) in enumerate([(659.3, .25), (784, .7), (988, 1.2), (1318.5, 1.7)]): add(note(f, 1.2, .09, r=.5, saw=False), t)
# subidas en los cambios de bloque
for t in (5.9, 9.9, 14.9, 19.4, 22.9, 25.9):
    n = int(.5 * SR); x = np.random.default_rng(int(t)).standard_normal(n) * np.linspace(0, .12, n); add(x, t - .45)
# golpes de los tres deportes
for t in (23, 24, 25): add(kick() * 1.2, t); add(note(130.8, .6, .2, r=.3, saw=False), t)
# cierre
add(note(65.4, 4, .35, a=.003, r=1.5, saw=False), 29.6); add(pad([261.6, 329.6, 392, 523.3], 4.4, .1), 29.6)
add(note(1046.5, 3, .07, r=1.2, saw=False), 29.65)
b = b / np.abs(b).max() * .85
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.stack([b, b], 1) * 32767).astype('<i2').tobytes())
print(sys.argv[1])
