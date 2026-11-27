"""Mezcla v7 · La cadena del gimnasio (Ken Carter, Richmond High, 1999) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro» 01 → 02 → 03 → 04, misma serie, encadenadas con fundidos de 1,4 s;
distinta de la del último v7, que usó «Soft Piano, Strings, Calm, Intro, Logo») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-bar-hallgrimsson-islandia/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.40; DUR = OUT + 4.0   # la voz acaba en 22,32 s; el vídeo sigue hasta 22,90 y a 22,40 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: cuatro piezas de la misma serie (9 s cada una), cada una entra 1,4 s antes de que la anterior se apague (sin cortes)
put(mus, ld('mus1.mp3'), 0.0, 1.0, off=.2, dur=8.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 6.6, 1.0, off=.2, dur=8.0, fi=1.4, fo=1.4)
put(mus, ld('mus3.mp3'), 13.2, 1.0, off=.2, dur=8.0, fi=1.4, fo=1.4)
put(mus, ld('mus4.mp3'), 19.8, 1.0, off=.2, dur=DUR - 19.8, fi=1.4, fo=2.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(50)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube en «Pero el contrato» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); PG = pk(ld('page.mp3')); CK = pk(ld('chalk.mp3')); C1 = pk(ld('chalk1.mp3'))
CH = pk(ld('chain.mp3')); TA = pk(ld('tape.mp3')); MK = pk(ld('marker.mp3')); BK = pk(ld('books.mp3')); PC = pk(ld('piece.mp3'))
PN = pk(ld('pen.mp3')); TK = pk(ld('tick.mp3')); CL = pk(ld('clock.mp3')); ST = pk(ld('stamp.mp3'))
for f in [3.30, 5.32, 11.08, 18.08, 20.37]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
for f in [9.2, 15.06]: put(sfx, WH, f, .035, dur=1.0, fi=.05, fo=.4)                             # bajadas cortas
put(sfx, SL, .05, .06)                                       # foto del instituto
put(sfx, PG, T(2) - .1, .06)                                 # hoja de calendario
put(sfx, SL, 3.75, .045)                                     # pizarra
put(sfx, CK, T(8) - .08, .06, dur=1.0, fi=.02, fo=.2)        # trece marcas de tiza
put(sfx, C1, T(9) + .02, .05)                                # el 0
put(sfx, SL, 5.95, .05); put(sfx, SL, 6.15, .04)             # Carter y la puerta
put(sfx, CH, T(14) - .1, .08, dur=1.4, fi=.03, fo=.4)        # cadena y candado
put(sfx, TA, T(21) - .05, .05, dur=1.0, fo=.3)               # cinta del cartel
put(sfx, MK, T(23) - .02, .05, dur=E(27) - T(23) + .1, fi=.02, fo=.15)   # rotulador: OS ESPERO EN LA BIBLIOTECA
put(sfx, BK, T(27) + .05, .07)                               # libros
for i in range(5): put(sfx, PC, T(31) - .1 + i * .09, .035)  # 45 fichas
for i in range(4): put(sfx, PC, T(33) + i * .28, .022)       # se apagan
put(sfx, SL, T(36) - .1, .05)                                # contrato
put(sfx, PN, T(37) - .02, .05, dur=.55, fi=.02, fo=.15)      # firma
for k in (38, 39, 40): put(sfx, TK, T(k) - .02, .06, dur=.4, fo=.1)   # tres marcas
put(sfx, CL, T(39), .03, dur=.9, fi=.05, fo=.3)              # tic de reloj suave en «puntualidad»
put(sfx, SL, T(45) - .05, .04)                               # fichas de partido
put(sfx, MK, T(46) + .05, .06, off=1.0, dur=.35, fi=.02, fo=.1); put(sfx, MK, T(46) + .33, .06, off=2.0, dur=.35, fi=.02, fo=.1)   # dos X
put(sfx, C1, T(49), .06)                                     # el 13–0 se agrieta
put(sfx, ST, T(53) - .08, .14)                               # sello SE CUMPLE
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
