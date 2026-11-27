"""Efectos suaves de T01-3-r2 «El portero lo sabía»: aire en los cambios de zona, papel en la foto y la hoja, rotulador en la pizarra, lápiz en las flechas y la pregunta. Sin golpes.
python3 sfx_T01-3-r2.py T01-3-r2/sfx.wav T01-3-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('extremo')-.3,.9,.2),(at('tu')-.35,1.1,.35),(at('pero')-.4,1.2,.3),(at('descanso',2)-.45,1.2,.3),(at('diez')-.4,.9,.2),
              (at('entras')-.35,1.2,.3),(at('ataque')-.3,.9,.2),(at('no')-.25,1.0,.25),(at('del')-.3,.9,.2),(at('mientras')-.3,.9,.2),
              (at('salis')-.45,1.2,.3),(at('y',2)-.25,1.2,.3),(at('tu',5)-.35,1.1,.3),(at('y',3)-.25,1.0,.25),(at('despues')-.35,1.0,.25),
              (at('una',2)-.3,.9,.2),(at('con',2)-.25,1.2,.35),(at('apuntalo')-.15,1.2,.35),(at('porque',2)-.08,1.2,.3),(at('donde',2)-.4,1.3,.35)]:
    put(t,air(d),g)
put(at('tu')-.2,paper(.4),.22); put(at('diez')-.4,paper(.5),.25)
for w,n,d in [('ataque',2,.75),('perdidas',1,.55),('pivote',1,.5)]:
    s=at(w,n)-.1; k=int(d/.13)
    for i in range(k): put(s+i*.13,pencil(.14),.22)
put(at('area')-.2,pencil(.6),.2); put(at('sexto')-.15,pencil(1.0),.3); put(at('decides')-.1,pencil(.55),.3)
put(at('por',2)-.05,pencil(.9),.25); put(at('agua')-.15,pencil(.5),.22); put(at('cosa')-.1,paper(.3),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
