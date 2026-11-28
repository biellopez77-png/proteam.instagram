"""Mezcla v7 · «Las estrellas barren» (All Blacks: McCaw y Carter barren su vestuario) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», desde el inicio, una sola pista sin cortes; distinta de la del último v7,
que usó «Musical, Loop, Jazz, Bossanova, Piano») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-cuatro-casas-alemania-2014/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.5; BLK = OUT + .5; DUR = BLK + 4.0   # la voz acaba en 24,46 s; remate quieto ≥ 1 s; fundido a negro 25,5–26,0; cierre outro2.mp4 (4,0 s) desde 26,0
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2, af=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', f] + (['-af', af] if af else []) + ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); sti = np.zeros((N, 2))
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: una sola pista (piano, cuerdas y coro suaves), sin cortes; baja al cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, dur=DUR, fi=.3, fo=2.5)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .15 * np.clip((tt - T(41)) / .4, 0, 1) * np.clip((T(54) - tt) / .4, 0, 1)        # sube un poco en «Ganaron el Mundial»
env *= 1 - .35 * np.clip((tt - E(57)) / .15, 0, 1) * np.clip((T(58) + .1 - tt) / .15, 0, 1)  # respiro en la pausa de «grande...»
env *= 1 + .25 * np.clip((tt - E(59)) / .8, 0, 1) * np.clip((OUT + .3 - tt) / .8, 0, 1)      # respira tras «barrer» y baja al cierre
env *= 1 - .55 * np.clip((tt - OUT) / 1.5, 0, 1)                                              # bajo la voz del cierre, bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); ST = pk(ld('stamp.mp3'))
MK = pk(ld('marker.mp3')); BR = pk(ld('broom.mp3')); CR = pk(ld('crowd.mp3'))
for f in [4.15, 10.45, 13.15, 16.55, 21.5]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, CR, 0.0, .05, off=6.0, dur=4.6, fi=.2, fo=1.4)                               # murmullo de grada muy bajo bajo la portada
put(sfx, SL, .03, .04)                                                                # portada
put(sfx, BR, T(11) - .15, .06, dur=.55, fi=.02, fo=.2)                                # la escoba cae: un barrido corto
put(sfx, SL, 4.7, .04); put(sfx, SH, 4.8, .06)                                        # foto de la haka + obturador
put(sfx, SL, T(18) - .12, .04); put(sfx, SL, T(21) - .12, .04)                        # fichas de McCaw y Carter en las perchas
put(sfx, SL, 10.95, .03)                                                              # suelo del vestuario
put(sfx, BR, T(28) - .1, .09, dur=.8, fi=.02, fo=.25)                                 # primer barrido de las vendas
put(sfx, BR, T(30) - .05, .09, off=1.4, dur=.8, fi=.02, fo=.25)                       # segundo barrido, a la esquina
put(sfx, SL, 13.75, .035)                                                             # fichas de novato
put(sfx, MK, T(36) - .05, .05, off=2.4, dur=.32, fi=.02, fo=.08); put(sfx, MK, T(36) + .2, .045, off=3.4, dur=.32, fi=.02, fo=.08)   # la X, dos trazos
put(sfx, SL, 14.0, .035)                                                              # fichas de McCaw y Carter
put(sfx, ST, T(40) - .03, .14)                                                        # sello «VETERANOS»
put(sfx, SL, 17.2, .04); put(sfx, SH, 17.3, .06)                                      # foto de la final de 2011 + obturador
put(sfx, SL, T(45) - .1, .035); put(sfx, SL, T(49) - .1, .035)                        # marcadores
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), BLK, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (desde negro)
put(sti, ld(sys.argv[3]), BLK, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a2 = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a2 * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
