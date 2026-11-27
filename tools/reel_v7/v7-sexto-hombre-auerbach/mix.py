"""Mezcla v7 · El sexto no es el sexto mejor (Auerbach, Ramsey y Havlicek) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Sentimental, Fast 02», entra a 0,55 s para que su silencio caiga en el remate y su acorde final justo en «mejor»)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-libros-phil-jackson/mix.py.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json con los tiempos de words.js)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.45; DUR = OUT + 5.61   # la voz acaba en 21,16 s; a 21,45 empieza el fundido de 0,6 s al cierre
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
put(mus, ld('mus.mp3'), 0.55, 1.0, fi=.5, fo=1.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (E(58) - .2)) / .3, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # el acorde final sube 1 s y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); CR = pk(ld('creak.mp3'))
CD = pk(ld('card.mp3')); CK = pk(ld('clock.mp3')); SQ = pk(ld('squeak.mp3')); WS = pk(ld('whistle.mp3')); CL = pk(ld('clink.mp3')); ST = pk(ld('stamp.mp3'))
for f in [3.5, 9.95, 13.08]: put(sfx, WH, f - .05, .08, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, -.3, .08, off=.3)                                  # foto del banquillo de 1956
put(sfx, SL, T(1) - .05, .06)                                   # ficha RED AUERBACH
put(sfx, SH, T(4) - .2, .07)                                    # foto de Ramsey
put(sfx, SL, T(7) - .05, .06)                                   # ficha FRANK RAMSEY
put(sfx, CD, T(8) - .05, .05)                                   # estrella
put(sfx, MK, T(9) - .2, .06, off=.4, dur=1.0, fi=.03, fo=.3)    # el banco se dibuja
put(sfx, CR, T(11) - .05, .07, dur=1.4, fo=.4)                  # madera que cruje, muy suave
put(sfx, SL, T(12) - .5, .07)                                   # la pizarra
for i in range(5): put(sfx, CD, T(16) - .3 + i * .09 + .25, .05)   # cinco fichas, una a una
put(sfx, CK, T(18) - .1, .06, off=1.0, dur=T(23) - T(18) + .2, fi=.2, fo=.5)   # reloj de partido, discreto
put(sfx, WS, T(23) - .25, .04)                                  # silbato lejano: cambio
put(sfx, SQ, T(23) + .1, .09, off=11.9, dur=1.9, fi=.05, fo=.5)   # zapatillas sobre parqué
put(sfx, MK, T(26) - .15, .05, off=1.2, dur=.8, fi=.03, fo=.25)   # flechas de carrera
put(sfx, SH, T(28) - .45, .07)                                  # foto de los Celtics campeones
put(sfx, MK, T(29) - .05, .05, off=2.0, dur=.5, fi=.03, fo=.2)    # círculo sobre Ramsey
for i in range(7): put(sfx, CL, T(32) + i * .14 + .25, .07 - .004 * i, dur=.45, fo=.15)   # siete anillos
put(sfx, MK, T(36) - .1, .06, off=3.0, dur=2.0, fi=.05, fo=.4)  # el trofeo se dibuja
put(sfx, SL, T(43) - .1, .06)                                   # la placa
put(sfx, SH, T(47) - .3, .07)                                   # foto de Havlicek
put(sfx, ST, T(49) + .1, .1)                                    # nombre en la placa
put(sfx, WH, T(51) - .4, .06, dur=1.0, fi=.05, fo=.4)           # las fotos se apartan
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, np.repeat(ld(sys.argv[2], 1), 2, 1), OUT + 0.3)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .8) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
