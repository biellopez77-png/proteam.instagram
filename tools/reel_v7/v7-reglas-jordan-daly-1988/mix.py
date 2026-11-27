"""Mezcla v7 · Las reglas para Jordan (Chuck Daly, 1988) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo» 01 → 02 → 03, encadenadas con fundidos de 1,4 s;
distinta de la del último v7, que usó «Orchestra, Piano, Choir, Sentimental») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-libreta-reep-1950/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 23.36; DUR = OUT + 4.0   # la voz acaba en 22,76 s; a 23,36 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 23,66)
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
# música: tres partes de la misma serie, encadenadas sin cortes; sube en el remate y baja al cierre
put(mus, ld('m1.mp3'), 0.0, 1.0, fi=.4, fo=1.4)
put(mus, ld('m2.mp3'), 12.5, 1.0, fi=1.4, fo=1.4)
put(mus, ld('m3.mp3'), 25.0, 1.0, fi=1.4, fo=1.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(53)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)
env *= np.clip((DUR - tt) / 2.4, 0, 1) * .5 + .5 * np.clip((DUR - .3 - tt) / 2.4, 0, 1)   # la música va bajando bajo el cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); PN = pk(ld('pen.mp3'))
ST = pk(ld('stamp.mp3')); BO = pk(ld('bounce.mp3')); TK = pk(ld('token.mp3')); PW = pk(ld('pawn.mp3'))
for f in [1.92, 6.12, 10.3, 17.58, 19.62]: put(sfx, WH, f - .2, .07, dur=1.4, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .06, off=3.0, dur=1.0, fi=.05, fo=.3)                          # polaroid del Silverdome
put(sfx, SL, T(2) - .05, .05, off=3.6, dur=.6, fi=.03, fo=.2)                     # hoja de calendario que cae
put(sfx, SH, 2.7 - .4, .07, dur=1.0, fo=.3)                                       # obturador: ficha de Jordan
for i in range(7): put(sfx, PW, T(9) + i * .1, .03, off=.9, dur=.25, fo=.1)       # marcador que cuenta hasta 59
put(sfx, SL, T(13) - .1, .045, off=5.0, dur=.8, fi=.03, fo=.3)                    # marcador final
put(sfx, SH, 6.9 - .4, .07, dur=1.0, fo=.3)                                       # obturador: ficha de Daly
put(sfx, TK, T(20) - .2, .05, dur=1.0, fo=.3)                                     # fichas del uno contra uno
put(sfx, MK, T(27) - .1, .07, off=1.2, dur=.35, fo=.1); put(sfx, MK, T(27) + .05, .07, off=1.55, dur=.35, fo=.1)   # tachado
put(sfx, SL, T(28) - .25, .06, off=7.8, dur=.9, fi=.03, fo=.3)                    # la libreta entra
put(sfx, PN, T(29) - .05, .05, off=1.6, dur=.9, fi=.02, fo=.2)                    # «Jordan Rules» a mano
put(sfx, MK, E(29) + .1, .05, off=3.1, dur=.4, fo=.1)                             # subrayado
put(sfx, SL, E(29) + .1, .035, off=9.6, dur=.7, fi=.03, fo=.3)                    # pizarra
put(sfx, BO, T(31) - .05, .05, off=2.45, dur=.6, fo=.2)                           # un bote en el parqué
put(sfx, PN, T(31), .045, off=2.85, dur=E(36) - T(31), fi=.02, fo=.2)             # regla 1
put(sfx, TK, T(34) - .1, .045, off=1.25, dur=1.0, fo=.3)                          # el 23 va a su izquierda
put(sfx, TK, T(37) - .1, .04, off=2.6, dur=1.0, fo=.3)                            # el 23 al ala
put(sfx, PN, T(39) - .1, .045, off=5.05, dur=E(41) - T(39), fi=.02, fo=.2)        # regla 2
put(sfx, TK, T(40) - .1, .05, dur=.8, fo=.3); put(sfx, TK, T(40) + .05, .045, off=1.25, dur=.8, fo=.3)   # dos encima
put(sfx, TK, T(42) - .1, .04, off=2.6, dur=1.0, fo=.3)                            # el 23 al poste
put(sfx, PN, T(44) - .1, .045, off=1.6, dur=E(47) - T(44), fi=.02, fo=.2)         # regla 3
put(sfx, SH, T(44) + .1 - .4, .05, dur=1.0, fo=.3)                                # polaroid de Detroit
put(sfx, TK, T(45) - .1, .055, dur=1.0, fo=.3)                                    # llega el grande
for k in (50, 51, 52): put(sfx, ST, T(k) - .02, .12)                              # tres sellos
put(sfx, SL, 20.3, .04, off=12.6, dur=.8, fi=.03, fo=.3)                          # pista final
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
