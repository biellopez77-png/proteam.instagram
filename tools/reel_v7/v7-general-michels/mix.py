"""Mezcla v7 · Ningún hueco vacío (Rinus Michels, Ajax) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 01», «… 02» y «… 03», encadenadas con fundidos de 1,4 s; distintas a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-sistema-lobanovski/mix.py.
La voz se abre 0,4 s en el silencio de «Europa... Cuando» (19,2 s) para que la pausa del guion respire; words.json ya lleva ese desplazamiento.
python3 mix.py voz.mp3 tail.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.3; DUR = OUT + 5.61; CUT = 19.2; GAP = 0.4   # la voz acaba en 23,26 s; a 23,3 empieza el fundido de 0,6 s al cierre
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
M1 = ld('mus1.mp3'); M2 = ld('mus2.mp3'); M3 = ld('mus3.mp3')
put(mus, M1, 0.0, 1.0, fo=1.4)                     # 01
put(mus, M2, 8.35, 1.0, fi=1.4, fo=1.4)            # 02 entra mientras 01 se apaga
put(mus, M3, 16.7, 1.0, fi=1.4)                    # 03: remate y cola hacia el cierre
put(mus, M1, 26.0, .8, fi=1.0, fo=1.5)             # 01 otra vez, bajo el cierre (se funde con el final)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(56) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); CH = pk(ld('chain.mp3')); CK = pk(ld('chalk.mp3')); PG = pk(ld('pages.mp3'))
SH = pk(ld('shutter.mp3')); ST = pk(ld('stamp.mp3')); CP = pk(ld('cap.mp3')); TK = pk(ld('token.mp3')); TI = pk(ld('tick.mp3')); CL = pk(ld('click.mp3'))
for f in [4.65, 11.05, 15.25, 19.0]: put(sfx, WH, f - .3, .08, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, 0.0, .06)                                          # retrato de 1966
put(sfx, SL, T(5) - .1, .05)                                    # ficha de prensa
put(sfx, CH, T(8) - .1, .06, off=2.15, dur=1.2, fi=.03, fo=.5)  # cordón y silbato que se mecen (sin pitar)
put(sfx, CK, T(11) - .1, .07, dur=1.1, fo=.3)                   # tiza: la mano en la pizarra del aula
put(sfx, SL, T(13) - .15, .05)                                  # rótulo del colegio
put(sfx, PG, T(15) - .5, .08)                                   # hojas del calendario
put(sfx, SH, T(17) - .5, .07, off=2.8, dur=1.0, fo=.3)          # foto del banquillo, 1965
put(sfx, SL, T(19) - .25, .04)                                  # tabla de clasificación
put(sfx, ST, T(28) + .06, .09)                                  # sello «EL GENERAL»
put(sfx, SH, T(29) - .55, .06, off=2.8, dur=1.0, fo=.3)         # foto del entrenamiento, 1969
put(sfx, CP, T(31) - .05, .08)                                  # rotulador que se destapa
put(sfx, TK, T(34) - .05, .06, dur=1.0, fo=.3)                  # fichas que se deslizan
put(sfx, TK, T(37) - .1, .05, off=1.4, dur=1.0, fo=.3)          # y vuelven a cambiar
for k in range(4): put(sfx, TI, T(41) + k * .25, .07, dur=.25, fo=.05)   # cuatro tics: 1965 → 1971
put(sfx, SH, T(44) - .55, .07, off=2.8, dur=1.0, fo=.3)         # portada de 1971
put(sfx, TK, T(56) - .05, .05, dur=.7, fo=.25)                  # una ficha sale de su sitio
put(sfx, CL, T(57) + .3, .1)                                    # otra encaja en el hueco
put(sfx, CL, T(58) + .45, .06)                                  # y la primera ocupa el sitio libre
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
put(vox, V[:int(CUT * SR)], 0.0); put(vox, V[int(CUT * SR):], CUT + GAP)
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
