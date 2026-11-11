"""Voz en off gratis y sin conexión a servicios de pago (motor Piper vía sherpa-onnx; voces alojadas en GitHub).
Funciona en las tareas programadas de la nube: no gasta créditos de ElevenLabs.

  python3 tools/trazo/voz.py guion.json voz.wav [--dur 31] [--voz davefx|sharvard] [--vel 1.0]
  python3 tools/trazo/voz.py --mezclar voz.wav sonido.wav mezcla.wav     (baja la música bajo la voz)

guion.json = [[segundo_de_inicio, "frase"], ...]. Cada frase empieza en su segundo; si no cabe antes de la
siguiente, el programa avisa con «SOLAPA» y hay que acortar la frase o mover el tiempo en la escena.
Escribe los números con letras («diecinueve», «minuto cuarenta y cinco») y los nombres como se pronuncian.
"""
import json, os, subprocess, sys, tarfile, urllib.request
import numpy as np, soundfile as sf

SR = 44100
CACHE = os.path.expanduser('~/.cache/proteam-voz')
VOCES = {'davefx': 'vits-piper-es_ES-davefx-medium', 'sharvard': 'vits-piper-es_ES-sharvard-medium'}


def modelo(voz):
    name = VOCES[voz]; d = os.path.join(CACHE, name)
    if not os.path.isdir(d):
        os.makedirs(CACHE, exist_ok=True); tb = d + '.tar.bz2'
        urllib.request.urlretrieve(f'https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/{name}.tar.bz2', tb)
        tarfile.open(tb).extractall(CACHE); os.remove(tb)
    onnx = next(os.path.join(d, f) for f in os.listdir(d) if f.endswith('.onnx'))
    return onnx, os.path.join(d, 'tokens.txt'), os.path.join(d, 'espeak-ng-data')


def motor(voz):
    try:
        import sherpa_onnx
        if int(sherpa_onnx.__version__.split('.')[0]) >= 2: raise ImportError   # la v2 ya no trae el fonemizador
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--break-system-packages', '-q', 'sherpa-onnx<2'], check=True); import sherpa_onnx
    onnx, tokens, data = modelo(voz)
    cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=onnx, tokens=tokens, data_dir=data, noise_scale=0.5, noise_scale_w=0.7), num_threads=4))
    return sherpa_onnx.OfflineTts(cfg)


def resample(x, sr):
    if sr == SR: return x
    n = int(len(x) * SR / sr); return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x)


def hablar(guion, out, dur=None, voz='davefx', vel=1.0, sid=0):
    tts = motor(voz); clips = []
    for t0, txt in guion:
        a = tts.generate(txt, sid=sid, speed=vel); x = resample(np.asarray(a.samples, dtype=np.float64), a.sample_rate)
        nz = np.where(np.abs(x) > 0.01)[0]; x = x[max(0, nz[0] - 400): nz[-1] + 2000] if len(nz) else x
        clips.append((float(t0), x))
    total = dur or max(t + len(x) / SR for t, x in clips) + .5
    b = np.zeros(int(total * SR)); ok = True
    for i, (t0, x) in enumerate(clips):
        fin = t0 + len(x) / SR; nxt = clips[i + 1][0] if i + 1 < len(clips) else total
        print(f'{t0:6.2f}–{fin:6.2f}  {"SOLAPA" if fin > nxt - .15 else "ok    "}  {guion[i][1][:60]}')
        ok &= fin <= nxt - .15
        s = int(t0 * SR); e = min(len(b), s + len(x)); b[s:e] += x[:e - s]
    b = b / (np.abs(b).max() + 1e-9) * .9
    sf.write(out, b, SR); print(out, 'OK' if ok else 'HAY SOLAPES: ajusta el guion o los tiempos'); return ok


def mezclar(voz, musica, out):
    v, sr1 = sf.read(voz); m, sr2 = sf.read(musica)
    if v.ndim > 1: v = v.mean(1)
    if m.ndim > 1: m = m.mean(1)
    v = resample(v, sr1); m = resample(m, sr2); n = max(len(v), len(m)); v = np.pad(v, (0, n - len(v))); m = np.pad(m, (0, n - len(m)))
    w = int(.25 * SR); env = np.convolve(np.abs(v), np.ones(w) / w, 'same'); duck = 1 - .72 * np.clip(env / .04, 0, 1)   # la música baja cuando hay voz
    x = v * 1.0 + m * duck * .8; x = x / (np.abs(x).max() + 1e-9) * .92
    sf.write(out, np.stack([x, x], 1), SR); print(out)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == '--mezclar': mezclar(a[1], a[2], a[3])
    else:
        opt = {a[i][2:]: a[i + 1] for i in range(2, len(a), 2)}
        hablar(json.load(open(a[0])), a[1], float(opt['dur']) if 'dur' in opt else None, opt.get('voz', 'davefx'), float(opt.get('vel', 1.0)))
