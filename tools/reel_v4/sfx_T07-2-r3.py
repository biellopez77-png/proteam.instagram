"""Efectos suaves de T07-2-r3 «Nunca pasó del medio»: aire en los cambios de zona, papel en el calendario y el marcador, lápiz en el rótulo, «central», las flechas, la palabra sobre negro y el aro de la pizarra. Sin golpes.
python3 sfx_T07-2-r3.py T07-2-r3/sfx.wav T07-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('cuatro')-.35,.8,.14),(at('temporada')-.4,.9,.16),(at('ni')-.3,.8,.14),(at('benjamin')-.4,1.1,.2),(at('es')-.35,.9,.16),
              (at('funciono')-.35,.8,.14),(at('pero')-.3,.8,.14),(at('nunca')-.3,.7,.12),(at('y',2)-.4,1.1,.2),(at('esta')-.35,.9,.16),
              (at('en',4)-.35,.9,.16),(at('si')-.35,.8,.14),(at('atacan')-.4,.9,.16),(at('apuntalo')-.45,1.2,.3),(at('para')-.2,1.4,.3)]:
    put(t,air(d),g)
put(at('ni')+.05,paper(.5),.2)
put(at('benjamin')+.35,pencil(.8),.25)
put(at('central')-.05,pencil(.5),.22)
put(at('funciono')-.05,paper(.4),.18)
for i in range(3): put(at('defender')-.2+i*.18,pencil(.5),.2)
for w in [1,2,3]: put(at('nunca',w)-.05,pencil(.2),.18)
for i in range(5): put(at('aprendiendo')-.05+i*.12,pencil(.4),.16)
put(at('y',3)+.1,pencil(.8),.25)
put(at('pizarra'),pencil(.6),.22)
put(at('cruzado',2)-.1,pencil(.6),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
