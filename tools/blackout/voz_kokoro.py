import sherpa_onnx, soundfile as sf, sys
D='/home/claude/tts/kokoro-multi-lang-v1_0/'
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
  model=D+'model.onnx',voices=D+'voices.bin',tokens=D+'tokens.txt',data_dir=D+'espeak-ng-data',lexicon='',lang='es'),num_threads=4))
tts=sherpa_onnx.OfflineTts(cfg)
def say(text,sid,out,speed=1.0):
    a=tts.generate(text,sid=sid,speed=speed); sf.write(out,a.samples,a.sample_rate); return len(a.samples)/a.sample_rate
if False:
    t="Quince días. El veintisiete se va la luz. Y con ella, los excels, los audios de guasap y el caos del lunes. ProTim: seis meses gratis para tu primer equipo. Solo hasta el Black Friday."
    for sid,n in [(28,'dora'),(29,'alex'),(53,'santa')]: print(n, say(t,sid,f'/home/claude/tts/m-{n}.wav'))
