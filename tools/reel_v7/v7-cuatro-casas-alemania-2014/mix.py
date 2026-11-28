"""Mezcla v7 · «Dortmund y Bayern, misma casa» (Alemania, Campo Bahia, Mundial 2014) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Jazz, Bossanova, Piano», 50,9 s, una sola pista sin cortes; distinta de la de los últimos v7, que usaron
«Calm Piano, Dreamy, Intro» y «Soft Piano, Strings, Calm, Intro, Logo») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/wooden/mix.py y v7-walkie-luis-enrique-2022/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.1; BLK = OUT + .5; DUR = BLK + 4.0   # la voz acaba en 23,08 s; remate quieto ≥ 1 s; fundido a negro 24,1–24,6; cierre outro2.mp4 (4,0 s) desde 24,6
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
# música: una sola pista de bossa al piano, sin cortes; baja al cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, dur=DUR, fi=.3, fo=2.5)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .15 * np.clip((tt - T(50)) / .4, 0, 1) * np.clip((T(54) - tt) / .4, 0, 1)        # sube un poco en «Alemania ganó el Mundial»
env *= 1 - .35 * np.clip((tt - E(57)) / .15, 0, 1) * np.clip((T(58) + .1 - tt) / .15, 0, 1)  # respiro en la pausa de «vestuario...»
env *= 1 + .25 * np.clip((tt - E(60)) / .8, 0, 1) * np.clip((OUT + .3 - tt) / .8, 0, 1)      # respira tras «convivir» y baja al cierre
env *= 1 - .55 * np.clip((tt - OUT) / 1.5, 0, 1)                                              # bajo la voz del cierre, bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); CH = pk(ld('chips.mp3'))
ST = pk(ld('stamp.mp3')); MK = pk(ld('marker.mp3')); WA = pk(ld('water.mp3'))
for f in [4.45, 9.15, 12.85, 15.4, 18.25]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 20.0, .04, dur=1.0, fi=.05, fo=.4)                                      # paso corto al remate
put(sfx, SL, .02, .04)                                                                # ficha de Großkreutz
put(sfx, SL, T(9) - .12, .045); put(sfx, SH, T(9) - .02, .06)                         # Schweinsteiger por la ventana + obturador
put(sfx, SL, T(9) + .08, .035)                                                        # ficha de Müller
put(sfx, CH, T(12) - .05, .05, dur=.35, fo=.1); put(sfx, CH, T(14) - .05, .05, dur=.35, fo=.1)   # dos fichas del Schalke, dos golpes cortos
put(sfx, SL, 5.05, .045)                                                              # tarjeta de hotel
put(sfx, ST, T(24) - .03, .14)                                                        # sello «NO»
put(sfx, SL, 9.75, .035)                                                              # plano
for k in range(3): put(sfx, CH, T(25) + k * .28, .035, dur=.25, fo=.08)               # casas que se van posando (contador)
put(sfx, WA, T(35) - .15, .06, off=2.0, dur=1.6, fi=.25, fo=.7)                       # agua bajo el ferry
put(sfx, SL, 13.55, .035)                                                             # banquillo y lista
put(sfx, MK, T(43) - .05, .05, off=2.4, dur=.32, fi=.02, fo=.08); put(sfx, MK, T(43) + .2, .045, off=3.4, dur=.32, fi=.02, fo=.08)   # la X, dos trazos
for i in range(4): put(sfx, CH, T(46) + .05 + i * .2, .035, dur=.25, fo=.08)           # un veterano en cada casa
put(sfx, CH, T(48), .05, dur=.9, fo=.3)                                               # puntos que se barajan
put(sfx, SL, 18.85, .04); put(sfx, SH, 18.95, .06)                                    # portada de campeones + obturador
put(sfx, SL, T(53) - .1, .035)                                                        # marcador
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
