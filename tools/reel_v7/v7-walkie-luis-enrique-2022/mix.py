"""Mezcla v7 · «La voz del míster» (Luis Enrique, Las Rozas, 2022) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01» → «… Intro 02» → «… Intro 03», encadenadas con fundidos de 1,4 s;
distinta de la de los últimos v7, que usaron «Soft Piano, Strings, Calm, Intro, Logo 01/02») + SFX reales bajos + voz (ElevenLabs, Mateo).
La cita «Vais a oír la voz del míster» pasa por un filtro de radio muy suave (50 % de la señal con paso banda 300–3800 Hz).
Base: tools/reel_v7/v7-lenguaje-corporal-auriemma/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.04; DUR = OUT + 4.0   # la voz acaba en 21,44 s; a 22,04 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 22,34)
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
# música: tres piezas de la misma serie, encadenadas con fundidos de 1,4 s (sin cortes); baja al cierre
put(mus, ld('mus1.mp3'), 0.0, 1.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 8.37, 1.0, fi=1.4, fo=1.4)
put(mus, ld('mus3.mp3'), 16.74, 1.0, fi=1.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(54)) / .15, 0, 1) * np.clip((T(55) + .1 - tt) / .15, 0, 1)   # silencio breve en la pausa de «momento...»
env *= 1 + .3 * np.clip((tt - E(57)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)     # sube 1 s tras «sin gritar» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); CH = pk(ld('chips.mp3'))
TU = pk(ld('tube.mp3')); PT = pk(ld('ptt.mp3')); SC = pk(ld('static.mp3')); TK = pk(ld('tick.mp3')); CO = pk(ld('cone.mp3')); VE = pk(ld('vest.mp3'))
for f in [1.5, 3.55, 7.2, 11.85, 17.6]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .05)                                                      # hoja de calendario que cae
put(sfx, SL, T(2) - .05, .04)                                               # ficha de prensa
put(sfx, SL, 1.9, .04); put(sfx, SH, 2.0, .08)                              # polaroid de Las Rozas + obturador
put(sfx, MK, T(5) - .1, .03, dur=.9, fi=.02, fo=.2)                         # campo a rotulador
for k in range(4): put(sfx, CO, T(7) + .05 + k * .12, .03)                  # conos
put(sfx, SL, T(8) - .2, .045)                                               # ficha de Luis Enrique
put(sfx, TU, T(12), .05, dur=.45, fo=.15); put(sfx, TU, T(14), .045, off=.8, dur=.45, fo=.15)   # tubos del andamio, dos golpes suaves
put(sfx, PT, T(17) - .06, .1); put(sfx, SC, T(17) + .12, .04, dur=.5, fi=.02, fo=.25)           # pulsador del walkie y soplido de estática
for k in range(3): put(sfx, VE, T(18) + k * .22, .035)                      # chalecos que se colocan
for k in range(4): put(sfx, CH, T(22) + k * .2, .02, dur=.3, fo=.1)         # puntos de los altavoces
put(sfx, SL, T(26) - .35, .035)                                             # bocadillo de radio
put(sfx, SC, T(26) - .3, .035, dur=.3, fi=.02, fo=.12); put(sfx, SC, E(32) + .02, .03, dur=.3, fi=.02, fo=.12)   # estática al empezar y acabar la cita
put(sfx, SL, 12.4, .045)                                                    # pizarra
for k, o in [(35, 1.5), (37, 3.4), (39, 5.0)]: put(sfx, MK, T(k) + .05, .035, off=o, dur=.4, fi=.02, fo=.1); put(sfx, CH, T(k) + .25, .02, dur=.3, fo=.1)   # flecha + ficha que desliza
put(sfx, SL, T(43) - .1, .04)                                               # megáfono
put(sfx, MK, T(46) - .05, .05, off=2.4, dur=.45, fi=.02, fo=.12)            # tachón
put(sfx, TK, T(54) + .02, .12, off=.05, dur=.4, fo=.1)                      # un solo tic de reloj
v = ld(sys.argv[1], 1); vr = ld(sys.argv[1], 1, 'highpass=f=300,lowpass=f=3800')
a, b = int((T(26) - .08) * SR), int((E(32) + .08) * SR); r = int(.06 * SR); m = np.zeros(len(v))
m[a:b] = 1; m[a:a + r] = np.linspace(0, 1, r); m[b - r:b] = np.linspace(1, 0, r); m *= .5
v = v * (1 - m[:, None]) + vr[:len(v)] * 1.25 * m[:, None]                  # filtro de radio muy suave solo en la cita
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
