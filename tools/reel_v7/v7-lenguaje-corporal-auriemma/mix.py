"""Mezcla v7 · «Da igual lo bueno que seas» (Geno Auriemma, UConn) (se ejecuta en el sandbox de Higgsfield, donde están los mp3 de Epidemic Sound).
Música real (Epidemic: «Musical, Loop, Soft Piano, Strings, Calm, Intro, Logo 01» → «… Logo 02», encadenadas con fundido de 1,4 s;
distinta de la del último v7, que usó «Orchestra, Piano, Choir, Sentimental») + SFX reales bajos + voz (ElevenLabs, Mateo).
Base: tools/reel_v7/v7-libreta-reep-1950/mix.py.
python3 mix.py voz.mp3 outro2.mp4 sting.mp3 out.wav   (necesita words.json; sting = Epidemic «Musical, Loop, Logo, Calm, Piano 01»)"""
import sys, json, subprocess, numpy as np
SR = 48000; OUT = 21.38; DUR = OUT + 4.0   # la voz acaba en 20,78 s; a 21,38 empieza el fundido de 0,5 s al cierre (outro2.mp4, 4,0 s; su voz entra a 21,68)
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
# música: dos piezas de la misma serie, encadenadas con fundido de 1,4 s (sin cortes); baja al cierre
put(mus, ld('mus1.mp3'), 0.0, 1.0, dur=13.0, fi=.3, fo=1.4)
put(mus, ld('mus2.mp3'), 11.6, 1.0, off=.8, fi=1.4, fo=2.4)
tt = np.arange(N) / SR; env = np.ones(N)
env *= 1 + .3 * np.clip((tt - T(48)) / 1.0, 0, 1) * np.clip((OUT + .6 - tt) / .8, 0, 1)   # sube en «El talento» y baja al cierre
env *= 1 - .25 * np.clip((tt - E(47)) / .2, 0, 1) * np.clip((T(48) + .2 - tt) / .2, 0, 1)  # se recoge en la pausa de «seas...»
mus *= env[:, None]
WH = pk(ld('whoosh.mp3')); SL = pk(ld('slide.mp3')); MK = pk(ld('marker.mp3')); SH = pk(ld('shutter.mp3'))
CH = pk(ld('chips.mp3')); ST = pk(ld('stamp.mp3')); WO = pk(ld('wood.mp3'))
for f in [2.3, 4.8, 8.7, 11.95, 15.25]: put(sfx, WH, f - .05, .07, dur=1.3, fi=.05, fo=.4)   # aire en cada viaje
for k in range(4): put(sfx, CH, T(2) + k * .45, .035)                       # fichas W que caen
put(sfx, SL, T(9) - .15, .05)                                               # postal del pabellón
put(sfx, SL, T(12) - .2, .045); put(sfx, SH, T(12) - .02, .08)              # ficha de Auriemma + obturador
put(sfx, MK, T(16) - .05, .04, dur=1.1, fi=.02, fo=.2)                      # banquillo dibujado
put(sfx, SL, T(21) - .1, .05)                                               # tarjeta de la estrella
put(sfx, MK, T(22), .035, off=1.5, dur=.4, fi=.02, fo=.1)                   # estrella a rotulador
put(sfx, WO, E(24) + .35, .07, dur=.8, fo=.3)                               # se sienta en el banquillo: golpe suave de madera
put(sfx, SL, 9.15, .04)                                                     # bocadillo de la cita
put(sfx, MK, T(33) - .05, .06, off=2.4, dur=.5, fi=.02, fo=.12)             # «12» a rotulador
put(sfx, MK, E(34) - .1, .04, off=3.4, dur=.4, fi=.02, fo=.1)               # subrayado
put(sfx, SL, 12.45, .04)                                                    # pizarra
put(sfx, MK, T(38), .05, off=4.0, dur=.5, fi=.02, fo=.12)                   # círculo azul
put(sfx, MK, T(39) - .05, .05, off=5.0, dur=.6, fi=.02, fo=.12)             # tachón
put(sfx, ST, T(41) - .03, .12)                                              # sello NUNCA
put(sfx, SL, 15.6, .045)                                                    # foto del banquillo de UConn
put(sfx, SL, T(49) - .2, .04); put(sfx, SL, T(55) - .25, .035)             # lista y pista
put(sfx, SL, T(56), .035)                                                   # la ficha pasa a la pista
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
