"""Mezcla v7 · «Estoy cansado» (Dean Smith) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 03» → «… Logo 02», misma serie, encadenadas con fundido de 1,4 s;
distinta de la del último v7, que usó «Logo, Calm, Piano, Pizzicato» → «Logo, Calm, Piano 02») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-carta-villas-boas-robson/mix.py. Sin sting de piano al cierre (la descarga de Epidemic falló): la música va bajando bajo el cierre.
python3 mix.py voz.mp3 outro2.mp4 out.wav   (necesita words.json)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 20.9; DUR = OUT + 4.0   # la voz acaba en 20,30 s; a 20,90 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 21,20)
W = json.load(open('words.json')); T = lambda k: W[k][1]; E = lambda k: W[k][2]
def ld(f, ch=2, af=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', f] + (['-af', af] if af else []) + ['-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32).reshape(-1, ch).copy()
N = int(DUR * SR); mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); vox = np.zeros((N, 2)); 
def put(buf, x, at, g=1.0, off=0.0, dur=None, fi=0.0, fo=0.0):
    x = x[int(off * SR):]; x = x[:int(dur * SR)] if dur else x; x = x.copy()
    if fi: n = min(len(x), int(fi * SR)); x[:n] *= np.linspace(0, 1, n)[:, None]
    if fo: n = min(len(x), int(fo * SR)); x[-n:] *= np.linspace(1, 0, n)[:, None]
    i = int(max(0, at) * SR); j = min(N, i + len(x))
    if i < N: buf[i:j] += g * x[:j - i]
pk = lambda x: x / (np.abs(x).max() + 1e-9)
# música: dos piezas de la misma serie, encadenadas con fundido de 1,4 s (sin cortes); baja bajo el cierre
put(mus, ld('mus1.mp3'), 0.0, 1.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 12.4, 1.0, fi=1.4, fo=3.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(43)) / .15, 0, 1) * np.clip((T(44) + .1 - tt) / .15, 0, 1)   # la música baja en la pausa de «cansado...»
env *= 1 + .3 * np.clip((tt - E(47)) / .6, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)      # sube tras «esconderlo» y baja al cierre
env *= np.clip(1 - .55 * (tt - OUT) / 2.0, .45, 1)                                            # bajo el cierre, la música va bajando
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); CA = pk(ld('card.mp3'))
ST = pk(ld('stamp.mp3')); CO = pk(ld('counter.mp3')); BO = pk(ld('bounce.mp3')); CK = pk(ld('clock.mp3')); AP = pk(ld('applause.mp3'))
for f in [3.62, 8.92, 11.22, 13.48, 15.68]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, CA, .05, .05)                                                      # ficha de Dean Smith
put(sfx, CO, T(3), .04, dur=1.2, fo=.3)                                     # contador 0 → 879
put(sfx, SL, T(5) - .3, .04); put(sfx, SH, T(5) - .05, .07)                 # polaroid del pabellón + obturador
put(sfx, CA, T(7), .05)                                                     # ficha de las temporadas
put(sfx, MK, 3.9, .025, dur=.9, fi=.05, fo=.25)                             # pista a rotulador
put(sfx, CA, T(12), .04)                                                    # fichas en la pista
put(sfx, MK, T(15) - .05, .03, off=1.0, dur=.5, fi=.02, fo=.15)             # flecha de cambio
put(sfx, BO, T(16) - .1, .05, dur=.45, fo=.15)                              # un bote en parqué, muy bajo
put(sfx, MK, T(16), .03, off=2.0, dur=.8, fi=.03, fo=.25)                   # la mano se dibuja
put(sfx, SL, E(18) - .05, .035)                                             # bocadillo
put(sfx, SL, T(21) + .05, .045)                                             # la ficha sale al banquillo
put(sfx, SL, T(24) - .45, .04); put(sfx, MK, T(24) - .05, .03, off=3.0, dur=.5, fi=.02, fo=.15)   # libreta + tachones
put(sfx, ST, T(25), .12)                                                    # sello SIN CASTIGO
put(sfx, CA, 11.7, .05)                                                     # foto de 1967
put(sfx, CK, T(26), .06, off=2.0, dur=1.6, fi=.1, fo=.4)                    # tic de reloj suave
put(sfx, SL, T(30) - .05, .04)                                              # la ficha vuelve a la pista
put(sfx, MK, 13.9, .025, off=4.0, dur=.6, fi=.05, fo=.2)                    # banquillo a rotulador
put(sfx, AP, T(36) - .05, .10, dur=1.9, fi=.05, fo=.7)                      # aplausos de pocas personas, cortos y bajos
put(sfx, SL, T(42) + .4, .03)                                               # la pista en calma
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
put(vox, ld(sys.argv[2]), OUT, dur=4.0)                       # audio del cierre «¿Te ha servido? Dale like y síguenos…» (su voz empieza a los 0,3 s)
e = np.abs(vox[:, 0]); hop = 480; ev = np.array([e[i:i + hop].max() for i in range(0, N, hop)])
ev = np.minimum(1, ev / (np.percentile(ev[ev > 0], 90) + 1e-9)); sm = np.zeros_like(ev)
for i in range(1, len(ev)): a2 = .45 if ev[i] > sm[i - 1] else .05; sm[i] = sm[i - 1] + a2 * (ev[i] - sm[i - 1])
duck = np.interp(np.arange(N), np.arange(len(sm)) * hop, 1 - .42 * sm)[:, None]
R = lambda x: 20 * np.log10(np.sqrt((x[:int(OUT * SR)] ** 2).mean()) + 1e-12)
vg = 10 ** ((-19 - R(vox)) / 20); vox *= vg
mg = 10 ** ((-31 - R(mus)) / 20); mus *= mg
mix = vox + mus * duck + sfx * vg
mix /= max(1, np.abs(mix).max() / .9)
fo = int((DUR - .6) * SR); mix[fo:] *= np.linspace(1, 0, N - fo)[:, None]
print('voz %.1f  música %.1f  sfx %.1f  pico %.2f' % (R(vox), R(mus * duck), R(sfx * vg), np.abs(mix).max()))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', sys.argv[3]], input=mix.astype(np.float32).tobytes(), check=True)
