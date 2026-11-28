"""Mezcla v7 · «Con una mano» (Hank Luisetti, Stanford, 1936) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Jazz, Soft, Piano» → «Musical, Loop, Jazz, Soft, Piano, Bass» → «… Jazz, Soft, Piano» otra vez,
encadenadas con fundidos de 1,4 s; distinta de la del último v7, «Calm Piano, Dreamy, Intro 01–03») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-walkie-luis-enrique-2022/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 27.15; DUR = OUT + 4.0   # la voz acaba en 26,04 s; remate quieto > 1 s; a 27,15 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 27,45)
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
# música: tres tramos de la misma serie de jazz suave, encadenados con fundidos de 1,4 s (sin cortes); baja al cierre
put(mus, ld('mus1.mp3'), 0.0, 1.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 12.6, 1.0, fi=1.4, fo=1.4)
put(mus, ld('mus1.mp3'), 25.2, 1.0, fi=1.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .45 * np.clip((tt - E(45)) / .1, 0, 1) * np.clip((E(45) + .4 - tt) / .1, 0, 1)   # silencio breve tras «entran»
env *= 1 + .25 * np.clip((tt - E(49)) / .4, 0, 1) * np.clip((T(50) + .3 - tt) / .3, 0, 1)    # la música sostiene la pausa del «...»
env *= 1 - .4 * np.clip((tt - OUT) / 1.5, 0, 1)                                              # baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); CH = pk(ld('chips.mp3'))
BO = pk(ld('bounce.mp3')); RU = pk(ld('run.mp3')); CR = pk(ld('crowd.mp3')); NE = pk(ld('net.mp3')); ST = pk(ld('stamp.mp3'))
for f in [3.95, 7.85, 12.3, 15.0, 20.2]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, BO, .02, .09, dur=.9, fo=.3)                                       # un bote de balón en parqué (primer fotograma)
put(sfx, SH, T(6) - .15, .08); put(sfx, SL, T(6) - .2, .04)                  # ficha de prensa (1944) + obturador
put(sfx, RU, T(9) - .1, .035, dur=1.1, fi=.1, fo=.4)                        # zapatillas en carrera, lejanas
put(sfx, SL, T(11) - .35, .045)                                             # ficha de 1943
put(sfx, MK, T(21), .03, dur=.8, fi=.02, fo=.2)                             # rotulador: parábola corta
put(sfx, MK, T(26) + .3, .03, off=1.2, dur=.7, fi=.02, fo=.2)               # rotulador: parábola que llega
put(sfx, SL, T(27) - .3, .04); put(sfx, SH, T(27) - .2, .07)                # postal del Garden + obturador
put(sfx, ST, T(28) + .1, .05, dur=.5, fo=.15)                               # matasellos
put(sfx, CR, 13.1, .025, dur=2.4, fi=.5, fo=.8)                             # murmullo de pabellón, muy bajo
for k in range(6): put(sfx, CH, T(39) + k * .27, .02, dur=.35, fo=.1)       # fichas que caen
for x in [T(43) + .4, T(44) + .6, T(45) + .7]: put(sfx, NE, x - .05, .06, dur=.9, fo=.3)   # red, tres veces
put(sfx, SL, T(46) - .15, .04)                                              # marcador
put(sfx, ST, E(49) - .1, .07, dur=.5, fo=.15)                               # sello «FIN DE LA RACHA»
v = ld(sys.argv[1], 1)
put(vox, np.repeat(v, 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
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
