"""Mezcla v7 · La libreta de Swindon (Charles Reep, County Ground, 1950) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Orchestra, Piano, Choir, Sentimental», una sola pista sin costuras, desde el principio;
distinta de la del último v7, que usó «Calm Piano, Dreamy, Intro» 01–04) + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-cadena-gimnasio-carter/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 22.65; DUR = OUT + 4.0   # la voz acaba en 22,05 s; a 22,65 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 22,95)
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
# música: una pista continua (sin cortes); baja al cierre
put(mus, ld('mus.mp3'), 0.0, 1.0, off=.5, dur=DUR, fi=.4, fo=2.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(48)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube en «La memoria» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); TY = pk(ld('type.mp3')); MK = pk(ld('marker.mp3')); WI = pk(ld('whistle.mp3'))
PG = pk(ld('page.mp3')); PN = pk(ld('pencil.mp3')); SH = pk(ld('shutter.mp3')); PI = pk(ld('pile.mp3')); MG = pk(ld('mag.mp3'))
for f in [2.35, 6.05, 9.55, 16.42, 19.08]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 14.68, .035, dur=1.0, fi=.05, fo=.4)                                               # bajada corta a la ficha
put(sfx, SL, .05, .06)                                       # postal del County Ground
put(sfx, SL, 2.85, .04)                                      # grada
put(sfx, TY, T(6) - .05, .05, dur=E(9) - T(6) + .1, fo=.15)  # ficha a máquina: CONTABLE · RAF
put(sfx, MK, T(14) - .05, .045, dur=1.2, fi=.02, fo=.2)      # flechas de ataque en la pizarra
put(sfx, MK, T(18) - .04, .06, off=2.0, dur=.3, fi=.02, fo=.1); put(sfx, MK, T(20) - .04, .06, off=3.0, dur=.3, fi=.02, fo=.1)   # dos cruces
put(sfx, WI, T(21) - .1, .035, dur=1.6, fi=.05, fo=.6)       # silbato lejano del descanso, muy bajo
put(sfx, PG, T(24) - .05, .06)                               # la libreta entra
put(sfx, SL, T(29) - .15, .045)                              # hoja de notas
put(sfx, PN, T(31) - .05, .06, off=1.0, dur=E(36) - T(31) + .1, fi=.03, fo=.2)   # lápiz que apunta
put(sfx, SH, T(39) - .03, .08)                               # obturador: CHARLES REEP
for i in range(0, 16, 3): put(sfx, PI, T(42) + i * .13, .035 + .004 * i)   # libretas que se apilan
put(sfx, MG, E(47) - .1, .05)                                # la pila se asienta
put(sfx, SL, 19.5, .045); put(sfx, PG, 19.75, .05)           # foto de hoy y libreta abierta
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
