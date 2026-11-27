"""Mezcla v7 · Solo se juega (Naismith y Phog Allen) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 04», encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-uno-por-ciento-riley/mix.py.
La voz se abre en cinco silencios para que quepan los viajes de cámara: 0,45 s en 2,64 («baloncesto... Y»), 0,4 s en 5,16 («dijo... El»),
0,4 s en 10,58 («caso... Cincuenta»), 0,6 s en 15,46 («victorias... De») y 0,4 s en 18,7 («Smith... El juego», la pausa del remate);
words.json ya lleva esos desplazamientos.
Remontaje 27/11 (crítica de Andrés, 79/100): «enseñarlo» queda 1,05 s solo antes del fundido (OUT 25,4); el cierre es el audio de outro2.mp4 con el sting de piano bajo;
«Dean Smith» con la voz +1,5 dB y la música más hundida (19,4–20,5 s); obturador de Allen y ficha del profesor adelantados a su nueva entrada.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.4; DUR = OUT + 4.0   # la voz acaba en 24,35 s; a 25,4 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 25,7 s)
CUTS = [(2.64, .45), (5.16, .4), (10.58, .4), (15.46, .6), (18.7, .4)]
FLY = [2.42, 5.38, 11.18, 16.56, 20.3]
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
def on(x):   # quita el silencio inicial: el golpe cae justo en su tiempo
    i = int(np.argmax(np.abs(x).max(1) > .08 * np.abs(x).max())); return x[max(0, i - 240):]
M = ld('mus.mp3'); LM = len(M) / SR
at = 0.0; k = 0
while at < DUR:                                     # pasadas encadenadas con fundidos de 1,4 s
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(51) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
MK = pk(on(ld('marker.mp3'))); PE = pk(on(ld('pencil.mp3'))); CH = pk(on(ld('chip.mp3'))); WI = pk(on(ld('whistle.mp3')))
BO = pk(on(ld('bounce.mp3'))); WB = pk(on(ld('board.mp3')))
for f in FLY: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SH, 0.0, .05, dur=1.0, fo=.3)                          # Naismith en ficha (obturador)
put(sfx, SL, T(2) - .1, .08)                                    # el borrador de las reglas se desliza
put(sfx, SL, FLY[0] + .2, .04)                                  # ficha del profesor
put(sfx, MK, T(8) - .05, .04, dur=.45, fo=.15)                  # línea profesor → alumno
put(sfx, SH, FLY[0] + .4, .07, dur=1.0, fo=.3)                  # Phog Allen (obturador)
put(sfx, SL, FLY[1] + .4, .04)                                  # tarjeta de la cita
put(sfx, MK, E(21) - .1, .07, dur=.45, fo=.15)                  # subrayado de SOLO SE JUEGA
put(sfx, ST, T(23) - .06, .10)                                  # sello NO
put(sfx, SL, T(25), .03)                                        # la tarjeta se aparta
put(sfx, PE, T(27), .06, dur=1.9, fo=.3)                        # 50 marcas a lápiz
for i in range(6): put(sfx, CH, T(32) + .1 + i * .2, .05)       # fichas que se apilan (746)
put(sfx, SH, FLY[3] + .35, .06, dur=1.0, fo=.3)                 # foto del equipo de 1924
put(sfx, MK, T(36), .04, dur=.5, fo=.15)                        # círculo sobre el entrenador
put(sfx, SL, T(38) - .05, .04); put(sfx, SL, T(41) - .05, .04)  # fichas de Rupp y Smith
put(sfx, WI, T(38) + .15, .035, dur=.6, fo=.2); put(sfx, WI, T(41) + .15, .03, dur=.6, fo=.2)   # dos silbatos lejanos
bb = T(44) + .45 * (T(46) + .3 - T(44))
put(sfx, BO, bb - .02, .08, dur=.9, fo=.3)                      # el balón bota una vez
put(sfx, WB, T(48) - .05, .06, dur=2.2, fo=.4)                  # rotulador en la pizarra
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
dn = np.clip(np.minimum((tt - 19.5) / .15, (20.35 - tt) / .15), 0, 1)                # «Dean Smith»
vox *= (1 + (10 ** (1.5 / 20) - 1) * dn)[:, None]
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
put(sti, ld(sys.argv[3]), OUT, .22, dur=4.0, fi=.3, fo=1.2)   # sting de piano bajo
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)
dn2 = np.clip(np.minimum((tt - 19.4) / .2, (20.5 - tt) / .2), 0, 1); duck = (duck * (1 - .45 * dn2))[:, None]   # música más hundida bajo «Dean Smith»
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg + sti * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[4]], input=mix.astype(np.float32).tobytes(), check=True)
