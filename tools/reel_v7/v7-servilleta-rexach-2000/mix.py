"""Mezcla v7 · La servilleta (Rexach y Messi, 2000) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01», encadenada consigo misma con fundidos de 1,4 s; distinta de la del último v7)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: ../v7-siete-segundos-dantoni/mix.py.
La voz acaba en 25,38 s; remate quieto hasta 26,2 s; fundido a negro 26,2–26,7 s; outro2 (4 s, con su voz) desde 26,7 s; la música sigue bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json con los tiempos de wt.py)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 26.2; CL = 26.7; DUR = CL + 4.0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vn', '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: la misma pista encadenada (misma tonalidad), fundidos de 1,4 s
M = ld('mus.mp3'); L = len(M) / SR; at = 0.0
while at < DUR:
    put(mus, M, at, 1.0, fi=(.3 if at == 0 else 1.4), fo=1.4); at += L - 1.4
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .2 * np.clip((tt - 10.4) / .5, 0, 1) * np.clip((13.2 - tt) / .6, 0, 1)             # re-hook: sube un poco
env *= 1 + .25 * np.clip((tt - 19.3) / .5, 0, 1) * np.clip((21.7 - tt) / .6, 0, 1)            # 2004: sube un poco
env *= 1 - .2 * np.clip((tt - 21.7) / .5, 0, 1)                                                # remate: baja
env *= np.clip(1 - (tt - OUT) / 4.0, 0, 1) ** 1.5 * (tt >= OUT) + (tt < OUT)                  # baja bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); PA = pk(ld('paper.mp3')); PE = pk(ld('pen.mp3')); FL = pk(ld('flip.mp3')); TE = pk(ld('tennis.mp3'))
CA = pk(ld('cafe.mp3')); SH = pk(ld('shutter.mp3')); CD = pk(ld('card.mp3'))
for f in [2.78, 6.6, 10.44, 13.12, 18.94, 21.62]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, PA, T(7) - .1, .12, off=.2, dur=.9, fi=.05, fo=.3)                 # la servilleta se despliega
put(sfx, CD, 3.25, .08)                                                      # ficha de jugador
for x in [T(17) + .05, T(18) + .1, T(19) + .1]: put(sfx, FL, x - .2, .07, dur=.6, fo=.2)   # hojas del calendario
for i in range(3): put(sfx, CD, T(20) - .05 + i * .22, .07)                # tres fichas «?»
put(sfx, SH, T(26) - .15, .08, dur=1.0, fo=.3)                              # foto de Rexach
put(sfx, CA, T(29) - .3, .05, off=20, dur=4.6, fi=.6, fo=1.2)               # murmullo de restaurante, muy bajo
put(sfx, TE, T(33), .05, dur=1.6, fi=.02, fo=.6)                            # bote de pelota de tenis lejano
put(sfx, PA, T(36) - .1, .09, off=1.5, dur=1.0, fi=.05, fo=.3)              # la servilleta desliza sobre el mantel
put(sfx, PE, T(38), .07, off=.5, dur=E(44) - T(38) + .2, fi=.08, fo=.3)     # bolígrafo
put(sfx, PE, T(45), .08, off=4.0, dur=1.4, fi=.05, fo=.3)                   # tres firmas cortas
for i in range(3): put(sfx, CD, T(48) + i * .08, .05)                       # las fichas se apartan
put(sfx, SH, T(50) - .25, .08, dur=1.0, fo=.3)                              # portada
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), CL)       # audio de outro2.mp4 («Dale like y síguenos…»)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20)
ov = vox[int(CL * SR):].copy(); vox *= vg
o_r = 20 * np.log10(np.sqrt((ov ** 2).mean()) + 1e-12); vox[int(CL * SR):] = ov * 10 ** ((-19.5 - o_r) / 20)   # el cierre al nivel de la voz
mus *= 10 ** ((-31 - R(mus)) / 20)
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .3) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
