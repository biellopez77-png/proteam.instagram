"""Efectos suaves de T03-2-r1 «Tres sábados, el mismo cuarto»: aire en los cambios de zona, papel en la charla y los sellos, lápiz en el círculo, las tachaduras, las flechas, «hambre», la escala y la ficha. Sin golpes.
python3 sfx_T03-2-r1.py T03-2-r1/sfx.wav T03-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('sabados')+.2,.8,.2),(at('tres',2)-.25,1.0,.25),(at('el')-.3,.9,.2),(at('tu')-.35,1.1,.3),(at('asi')-.35,1.1,.3),(at('miras')-.35,1.1,.3),
              (at('y',3)-.35,1.1,.3),(at('y',4)-.35,1.0,.25),(at('hasta')-.4,1.3,.35),(at('jueves')-.35,.9,.25),(at('al',2)-.4,1.4,.35),(at('uno')-.35,.9,.2),
              (at('jueves',2)-.4,1.1,.3),(at('y',6)-.35,1.3,.35),(at('apuntalo'),1.3,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('tercero')-.05,pencil(.6),.28)
for w in ['tocas','acortas','gritas']: put(at(w),pencil(.45),.24)
for w,dt in [('acortas',-.4),('gritas',-.35),('mas',.1)]: put(at(w)+dt,pencil(.3),.22)
put(at('no')-.1,paper(.7),.24); put(at('tampoco')-.1,paper(.7),.24)
for i in range(3): put(at('pides')-.1+i*.35,pencil(.35),.22)
put(at('quinteto'),pencil(.8),.15)
put(at('mundo')-.1,pencil(.5),.2); put(at('falta'),pencil(.6),.28); put(at('hambre'),pencil(.4),.25)
put(at('jueves')+.15,pencil(.5),.18)
put(at('duro')-.05,pencil(.4),.3); put(at('por')-.05,pencil(.9),.28)
put(at('recortalo')-.1,paper(.6),.22); put(at('compara')-.1,pencil(.5),.26)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
