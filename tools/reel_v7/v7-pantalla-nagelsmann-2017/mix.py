"""Mezcla v7 · «Sin mover a nadie» (Nagelsmann y la Videowall, 2017) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Piano, Intro, Tv», 15 s, encadenada consigo misma con un fundido de 1,4 s; distinta de las de los
últimos v7, que usaron «Calm Piano, Dreamy, Intro 01–03» y «Soft Piano, Strings, Calm, Intro, Logo») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-walkie-luis-enrique-2022/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 20.7; DUR = OUT + 4.0   # la voz acaba en 20,10 s; a 20,70 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 21,0)
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
# música: la misma pieza dos veces, encadenada con fundidos de 1,4 s (sin cortes); baja al cierre
M = ld('mus.mp3'); ml = len(M) / SR
put(mus, M, 0.0, 1.0, fi=.3, fo=1.4)
put(mus, M, ml - 1.4, 1.0, fi=1.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(55)) / .15, 0, 1) * np.clip((T(56) + .1 - tt) / .15, 0, 1)   # silencio breve en la pausa de «sitio...»
env *= 1 + .3 * np.clip((tt - E(57)) / .5, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)      # sube tras «lo entiendes» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); ST = pk(ld('stamp.mp3')); SH = pk(ld('shutter.mp3')); WR = pk(ld('wrap.mp3'))
FO = pk(ld('folder.mp3')); TP = pk(ld('tap.mp3')); TU = pk(ld('tube.mp3')); MK = pk(ld('marker.mp3')); CH = pk(ld('chips.mp3'))
for f in [3.42, 5.68, 10.55, 17.15]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .05)                                                      # ficha del jugador
put(sfx, CH, .95, .025, dur=.3, fo=.1); put(sfx, CH, 1.1, .02, dur=.3, fo=.1)   # botas que se apoyan
put(sfx, WR, T(8) + .05, .05, off=5.5, dur=.8, fi=.05, fo=.25)              # venda que se enrolla
put(sfx, ST, T(9) + .12, .12)                                               # sello FIN
put(sfx, SL, T(11) - .4, .045); put(sfx, SH, T(11) - .3, .07)               # ficha de Tuchel + obturador
put(sfx, SH, T(15) - .05, .06)                                              # visor REC
put(sfx, FO, T(16) - .1, .06, dur=1.0, fi=.02, fo=.3)                       # carpeta del rival que se abre
put(sfx, SL, T(17) - .25, .045); put(sfx, SH, T(17) - .15, .07)             # portada «28»
put(sfx, SL, T(22) - .15, .04)                                              # polaroid del estadio
for k, d in enumerate([T(24) - .05, T(25) + .1, E(25) + .3]): put(sfx, CH, d, .025, dur=.3, fo=.1)   # ficha 28 que sube la escalera
put(sfx, TU, T(34) - .05, .045, dur=.45, fo=.15); put(sfx, TU, T(34) + .35, .04, off=.8, dur=.45, fo=.15)   # estructura de la pantalla, dos golpes suaves
put(sfx, TP, T(40), .09)                                                    # toque en la tableta: pausa
put(sfx, CH, T(42) + .05, .018, dur=.3, fo=.1)                              # cámaras que se encienden
put(sfx, MK, T(45), .035, dur=.5, fi=.02, fo=.15)                           # flecha de la solución
v = ld(sys.argv[1], 1)
put(vox, np.repeat(v, 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «Dale like y síguenos…» (su voz empieza a los 0,3 s)
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
