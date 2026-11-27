"""Efectos suaves de C3 «El parón que dura cuatro semanas»: aire en los movimientos de cámara, lápiz en los tachones, el círculo, el subrayado y la lista; papel al cambiar de foto. Sin golpes.
python3 sfx_c3.py c3-paron/sfx.wav c3-paron/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('tres')-.45,1.1,.3),(at('dura',2)-.4,1.1,.3),(at('ultimo')-.45,1.3,.4),(at('partidillo')-.4,1.0,.3),(at('hasta')-.3,1.0,.25),
              (at('reyes')-.45,1.3,.4),(at('piernas')-.4,1.0,.3),(at('y',2)-.4,1.3,.4),(at('ya')-.4,.9,.25),(at('cargas')-.45,1.2,.35),
              (at('segundo')-.4,1.0,.3),(at('esa',2)-.4,1.6,.45),(at('diez')-.4,1.0,.3),(at('primera')-.45,1.0,.3),(at('apunta')-.4,1.0,.3),
              (at('la',3)-.45,1.6,.4),(at('guardalo')-.4,1.0,.3),(at('apuntalo')-.45,1.6,.4),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
for k,s in enumerate([at('tres')-.05,at('tres')+.3,at('semanas')+.1]): put(s,pencil(.45),.3)
put(at('cuatro')-.1,pencil(.7),.35)
put(at('ultimo')-.2,paper(.45),.25); put(at('reyes')-.2,paper(.45),.25)
put(at('cuenta')-.1,pencil(.6),.3); put(at('tiron')-.15,pencil(.5),.35)
put(at('cuarta')-.05,pencil(.6),.25)
for w in ['diez','primera','apunta']: put(at(w)-.15,pencil(.5),.3)
put(at('ultimo',2)-.2,pencil(.6),.3)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
