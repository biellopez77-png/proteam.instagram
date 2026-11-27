"""Mezcla v7 · «La carta al vecino» (Villas-Boas y Bobby Robson) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Logo, Calm, Piano, Pizzicato» → «Musical, Loop, Logo, Calm, Piano 02», encadenadas con fundido de 1,4 s;
distinta de la de los últimos v7, que usaron «Calm Piano, Dreamy, Intro 01–03» y «Soft Piano, Strings, Calm, Intro, Logo 01/02») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-walkie-luis-enrique-2022/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.64; DUR = OUT + 4.0   # la voz acaba en 21,04 s; a 21,64 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 21,94)
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
# música: dos piezas de la misma serie, encadenadas con fundido de 1,4 s (sin cortes); baja al cierre
put(mus, ld('mus1.mp3'), 0.0, 1.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 10.6, 1.0, fi=1.4, fo=2.0)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 - .35 * np.clip((tt - E(51)) / .15, 0, 1) * np.clip((T(52) + .1 - tt) / .15, 0, 1)   # la música baja en la pausa de «Domingos...»
env *= 1 + .3 * np.clip((tt - E(55)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)     # sube 1 s tras «pregunta» y baja al cierre
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3')); CA = pk(ld('card.mp3'))
PE = pk(ld('pen.mp3')); FO = pk(ld('fold.mp3')); ST = pk(ld('stamp.mp3')); PG = pk(ld('page.mp3')); CO = pk(ld('counter.mp3')); SW = pk(ld('switch.mp3'))
for f in [1.35, 6.95, 9.4, 13.1, 17.2]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
put(sfx, SL, .05, .05)                                                      # postal de Antas
put(sfx, SL, T(1) - .1, .035)                                               # ficha del estadio
put(sfx, MK, T(3) - .25, .025, dur=.7, fi=.05, fo=.2)                       # bloque a rotulador
put(sfx, SW, T(4) - .02, .06, dur=.25, fo=.08)                              # se enciende la ventana
put(sfx, PE, T(8) - .05, .045, dur=1.3, fi=.03, fo=.3)                      # la hoja se escribe sola
put(sfx, FO, T(12) - .15, .05, dur=.6, fo=.2)                               # la hoja se dobla y vuela
put(sfx, CA, T(12) - .2, .05); put(sfx, SH, T(12) + .05, .07)               # ficha de Robson + obturador antiguo
put(sfx, SL, 7.3, .045)                                                     # hoja de la pregunta
put(sfx, PE, T(19), .035, off=1.5, dur=1.0, fi=.03, fo=.25)                 # la pregunta se escribe
put(sfx, MK, E(23) - .1, .035, off=2.0, dur=.45, fi=.02, fo=.12)            # subrayado en azul
put(sfx, CA, T(23), .06)                                                    # ficha de Domingos en el banquillo
put(sfx, CA, 9.75, .05)                                                     # ficha de Robson (escena D)
put(sfx, SL, T(26), .04)                                                    # la ficha se gira
put(sfx, SL, T(30) - .15, .04)                                              # cuaderno
for k, g in [(32, .12), (34, .12), (36, .14)]: put(sfx, ST, T(k) + (.05 if k == 36 else 0), g)   # tres sellos
put(sfx, PG, 13.75, .06)                                                    # página de periódico
put(sfx, CA, T(39) - .15, .045)                                             # ficha de Villas-Boas
put(sfx, CA, T(41), .05)                                                    # marcador de chapa
put(sfx, CO, T(45), .04, dur=1.1, fo=.3)                                    # contador 16 → 33
put(sfx, CA, T(48) - .25, .04)                                              # ficha de Villas-Boas (escena F)
put(sfx, SL, T(51) - .35, .05)                                              # la ficha de Domingos cruza
put(sfx, SL, T(52) - .1, .04)                                               # vuelve la hoja de la pregunta
put(vox, np.repeat(ld(sys.argv[1], 1), 2, 1), 0.0)
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
