# Audio v7 en el sandbox de Higgsfield

Tiempos por palabra (`wt.py`):

```python
import sys,json
from faster_whisper import WhisperModel
m=WhisperModel('small',compute_type='int8')
for f in sys.argv[1:]:
    segs,_=m.transcribe(f,language='es',word_timestamps=True)
    print(json.dumps([(w.word.strip(' ,.'),round(w.start,2),round(w.end,2)) for s in segs for w in s.words],ensure_ascii=False))
```

Mezcla: `tools/reel_v7/bielsa/mix3.py` como plantilla (adapta tiempos, pistas y efectos; desde el 27/11 la cola de voz del cierre es el audio de `tools/reel_v6/outro/outro2.mp4`, «Dale like y síguenos para más vídeos como este», no tail.mp3), luego
`ffmpeg -i video_mudo.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart final.mp4`.
Subida: `media_upload` (filename final.mp4) → `curl -X PUT -H "Content-Type: video/mp4" --data-binary @final.mp4 '<upload_url>'` en el MISMO comando → `media_confirm` type video. URL pública: la de d2ol7oe51mr4n9.cloudfront.net que devuelve media_upload.
Los mp3 de Epidemic caducan en ~1 h: descárgalos en el sandbox justo después de `download_sound_effect`.
