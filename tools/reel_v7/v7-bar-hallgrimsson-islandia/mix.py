"""Mezcla v7 · Quien conoce el plan (Heimir Hallgrímsson, Islandia) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo» 01 → 02 → 03, misma serie, encadenadas con fundidos de 1,4 s;
distinta de la del último v7) + SFX reales bajos + voz (ElevenLabs, Mateo). Base: tools/reel_v7/v7-salid-y-disfrutad-cruyff/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 24.10; DUR = OUT + 4.0   # la voz acaba en 24,04 s; el vídeo sigue hasta 24,60 y a 24,10 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s)
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
# música: tres piezas de la misma serie, cada una entra 1,4 s antes de que la anterior se apague (sin cortes)
put(mus, ld('mus1.mp3'), 0.0, 1.0, off=.6, dur=10.4, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 9.0, 1.0, off=1.2, dur=10.4, fi=1.4, fo=1.4)
put(mus, ld('mus3.mp3'), 18.0, 1.0, off=1.2, dur=DUR - 18.0, fi=1.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(59)) / .4, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube en «lo defiende» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); SH = pk(ld('shutter.mp3')); MK = pk(ld('marker.mp3')); CO = pk(ld('counter.mp3'))
TI = pk(ld('tick.mp3')); PC = pk(ld('piece.mp3')); DO = pk(ld('door.mp3')); BO = pk(ld('bolt.mp3')); ST = pk(ld('stamp.mp3'))
PU = pk(ld('pub.mp3')); CR = pk(ld('crowd.mp3'))
for f in [2.15, 4.55, 7.24, 11.21, 15.27, 18.42, 21.5]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, WH, 13.62, .035, dur=1.0, fi=.05, fo=.4)            # empuje hacia el sello
put(sfx, SL, .05, .06)                                      # foto del estadio
put(sfx, TI, .3, .035, off=2.0, dur=1.9, fi=.1, fo=.4)      # el reloj retrocede, muy bajo
put(sfx, DO, T(16) - .2, .06, dur=1.25, fo=.3)              # puerta de madera que se abre
put(sfx, PU, T(16) - .1, .022, off=20.0, dur=2.9, fi=.4, fo=1.0)   # murmullo de bar lejano
put(sfx, SH, 4.95, .07)                                     # foto de Heimir
put(sfx, SL, T(18) + .05, .05); put(sfx, SL, T(20) - .05, .05)    # ficha y tarjeta de la consulta
put(sfx, SL, 7.6, .05)                                      # pizarra
for i in range(5): put(sfx, PC, T(27) - .05 + i * .07, .045)       # el once sobre la mesa
for i in range(3): put(sfx, PC, T(29) + .05 + i * .15, .035)       # se colocan en el sistema
put(sfx, MK, T(32) - .05, .06, dur=.45, fi=.02, fo=.15); put(sfx, MK, T(32) + .15, .06, off=1.0, dur=.45, fi=.02, fo=.15)   # flechas del plan
put(sfx, DO, T(34) - .05, .035, off=.3, dur=.6, fi=.05, fo=.25)    # la puerta se cierra
put(sfx, BO, T(34) + .38, .08, dur=.5, fo=.15)              # cerrojo
put(sfx, SH, T(37) - .1, .04, dur=.12, fo=.05)              # clic de cámara cortado
put(sfx, MK, T(37), .06, off=2.0, dur=.4, fi=.02, fo=.12)   # rotulador que tacha
put(sfx, SL, 13.75, .05)                                    # hoja del plan
put(sfx, ST, T(40) - .03, .13)                              # sello
put(sfx, CO, T(45), .04, dur=1.1, fi=.02, fo=.3)            # contador
put(sfx, SL, 18.75, .05)                                    # marcador
put(sfx, CO, T(49), .04, dur=.3, fi=.02, fo=.1)             # INGLATERRA 1
put(sfx, PC, T(52) - .03, .09)                              # el «2», golpe suave
c = CR[int(3 * SR):].copy()                                 # estadio lejano: sube con el 2 y se va antes de «Quien conoce el plan»
ce = np.interp(np.arange(len(c)) / SR + T(52) - .3, [T(52) - .3, T(52) + .3, 21.0, 21.8], [0, .05, .05, 0])
put(sfx, c * ce[:, None], T(52) - .3, 1.0, dur=21.8 - (T(52) - .3))
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
