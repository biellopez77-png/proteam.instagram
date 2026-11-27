"""Mezcla v7 · ¿Trece? ¿Catorce? (Rangnick y el Dinamo de Kiev de Lobanovski) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Calm Piano, Dreamy, Intro 03», encadenada consigo misma con fundidos de 1,4 s; distinta a las de los v7 anteriores)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/bielsa/mix3.py y v7-uno-por-ciento-riley/mix.py.
Remontaje 27/11 (crítica de Andrés, 78/100): «A LA VEZ» queda ≥1 s quieto tras «vez» (OUT 21,3); fundido a negro de 0,5 s y el cierre es el audio de outro2.mp4 (su voz entra a 21,6 s); la música va bajando bajo el cierre.
La voz se abre 0,5 s en tres silencios para que quepan los viajes de cámara: 4,6 («Backnang... Un»), 7,5 («Lobanovski... En») y 16,3 («respirar... No», la pausa del remate);
words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.3; DUR = OUT + 4.0   # la voz acaba en 20,16 s; a 21,3 empieza el fundido a negro de 0,5 s al cierre (outro2.mp4, 4,0 s)
CUTS = [(4.6, .5), (7.5, .5), (16.3, .5)]
FLY = [4.45, 7.85, 17.12]
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
def on(x):   # quita el silencio inicial: el golpe cae justo en su tiempo
    i = int(np.argmax(np.abs(x).max(1) > .08 * np.abs(x).max())); return x[max(0, i - 240):]
M = ld('mus.mp3'); LM = len(M) / SR   # 9,74 s
at = 0.0; k = 0
while at < DUR:                                     # pasadas encadenadas con fundidos de 1,4 s
    put(mus, M, at, 1.0, fi=0 if k == 0 else 1.4, fo=1.4); at += LM - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .35 * np.clip((tt - (T(51) - .3)) / .4, 0, 1) * np.clip((OUT + .3 - tt) / .6, 0, 1)   # sube en el remate y baja al cierre
env *= 1 - .6 * np.clip((tt - OUT) / 2.5, 0, 1)   # bajo el cierre la música va bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); PA = pk(on(ld('paper.mp3'))); SH = pk(on(ld('shutter.mp3'))); ST = pk(on(ld('stamp.mp3')))
MK = pk(on(ld('marker.mp3'))); WB = pk(on(ld('wb.mp3'))); CH = pk(on(ld('chip.mp3'))); CK = pk(on(ld('click.mp3'))); BO = pk(on(ld('bounce.mp3')))
for f in FLY: put(sfx, WH, f - .3, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, -.1, .07)                                          # ficha de Rangnick
put(sfx, ST, T(2) - .04, .08)                                   # sello JUGADOR
put(sfx, ST, T(4) - .04, .08)                                   # sello ENTRENADOR
put(sfx, SL, T(7) - .3, .07)                                    # foto de Backnang
put(sfx, CH, T(12) + .25, .07)                                  # el alfiler se clava
put(sfx, ST, T(15) - .04, .08)                                  # sello AMISTOSO
put(sfx, PA, T(18) - .35, .07, dur=.9, fo=.3)                   # recorte de periódico del Dinamo
put(sfx, SH, T(21) - .25, .07, dur=1.0, fo=.3)                  # Lobanovski en ficha (obturador)
put(sfx, BO, T(25) + .1, .07, dur=1.2, fo=.4)                   # el balón sale por la banda
for i in range(10): put(sfx, CH, T(31) + i * (E(34) + .1 - T(31)) / 10, .07)   # una ficha por número
put(sfx, CH, T(35), .07); put(sfx, CH, T(36), .07)              # ¿trece? ¿catorce?, más secos
put(sfx, CK, T(38) + .05, .07)                                  # el contador se fija en 11
put(sfx, WB, T(42), .07, dur=1.4, fi=.05, fo=.3)                # rotulador que cierra el círculo
put(sfx, MK, T(49), .07, dur=.5, fo=.15)                        # once flechas a la vez
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
put(vox, ld(sys.argv[2]), OUT, dur=4.0)   # audio del cierre outro2 («¿Te ha servido? Dale like y síguenos…», su voz entra a los 0,3 s)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
