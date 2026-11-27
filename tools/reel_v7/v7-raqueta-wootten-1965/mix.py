"""Mezcla v7 · La raqueta de Wootten (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Wind, Reveal, Strings, Dark Piano 01» y «… 02», encadenadas una y otra vez con fundidos de 1,4 s)
+ SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/wooden/mix.py y v7-no-se-entrena-phog-allen/mix.py.
La voz se abre en tres silencios para que quepan los viajes de cámara: 0,5 s en 11,35 («DeMatha... preparó»), 0,5 s en 13,82 («tenis... en el»)
y 0,4 s en 17,45 («alto... Ganaron»); words.json ya lleva esos desplazamientos.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 25.38; DUR = OUT + 4.0   # la voz acaba en 24,78 s; a 25,38 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 25,68 s)
CUTS = [(11.35, .5), (13.82, .5), (17.45, .4)]
FLY = [5.16, 8.42, 11.25, 14.2, 18.24, 21.08]
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
MS = [ld('mus1.mp3'), ld('mus2.mp3')]
at = 0.0; k = 0
while at < DUR:                                     # pasadas encadenadas con fundidos de 1,4 s
    M = MS[k % 2]; put(mus, M, at, 1.0, fi=.4 if k == 0 else 1.4, fo=1.4); at += len(M) / SR - 1.4; k += 1
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - E(44)) / .25, 0, 1) * np.clip((T(45) + .2 - tt) / .3, 0, 1)        # pausa antes del remate: la música sostiene
env *= 1 + .35 * np.clip((tt - (T(51) - .3)) / .4, 0, 1) * np.clip((OUT + 1.3 - tt) / .8, 0, 1)   # sube 1 s en el remate y baja al cierre
env *= np.clip(1 - (tt - (OUT + .5)) / 3.0, .25, 1)                                                # en el cierre, la música va bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(on(ld('slide.mp3'))); SH = pk(on(ld('shutter.mp3'))); TY = pk(on(ld('type.mp3')))
TA = pk(on(ld('tape.mp3'))); MK = pk(on(ld('marker.mp3'))); RA = pk(on(ld('racket.mp3'))); BO = pk(on(ld('bounce.mp3')))
BZ = pk(on(ld('buzzer.mp3'))); CK = pk(on(ld('click.mp3')))
for f in FLY: put(sfx, WH, f - .1, .07, dur=1.3, fi=.05, fo=.4)    # aire en cada viaje
put(sfx, SL, T(2) - .25, .08)                                       # ficha de Power Memorial
put(sfx, TY, T(2) + .05, .06, dur=.95, fo=.25)                      # máquina de escribir
for i in range(0, 71, 6): put(sfx, CK, T(5) - .05 + i * .017, .03)  # fichas que se encienden, muy bajas
put(sfx, SH, T(9) - .3, .08)                                        # obturador: Alcindor
put(sfx, TA, T(13) - .05, .10)                                      # la regla se despliega
put(sfx, SL, T(16) - .4, .08)                                       # polaroid del gimnasio
put(sfx, SH, T(18) - .15, .06)                                      # ficha sin foto
put(sfx, MK, T(26) - .15, .06, dur=.8, fi=.03, fo=.25)              # la raqueta se traza
put(sfx, RA, T(28) + .1, .07, dur=.6, fo=.2)                        # golpe seco de raqueta, muy bajo
put(sfx, BO, T(29) - .2, .07, dur=.9, fo=.3)                        # bote de balón en parqué
put(sfx, MK, T(40) - .05, .05, dur=.5, fo=.15)                      # línea de altura
put(sfx, SH, T(41) - .45, .07)                                      # foto del pabellón
put(sfx, CK, E(42) - .1, .08); put(sfx, CK, E(44) - .1, .08)        # 46 y 43
put(sfx, BZ, E(44) + .02, .035, fo=.4)                              # bocina, lejana y corta
put(sfx, SL, T(45) - .2, .05)                                       # la regla del final
V = np.repeat(ld(sys.argv[1], 1), 2, 1)
cuts = [0.0] + [c for c, _ in CUTS] + [len(V) / SR]; sh = 0.0
for k in range(len(cuts) - 1):
    put(vox, V[int(cuts[k] * SR):int(cuts[k + 1] * SR)], cuts[k] + sh)
    if k < len(CUTS): sh += CUTS[k][1]
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
