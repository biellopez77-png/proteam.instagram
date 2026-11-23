"""Efectos suaves de T03-2-r2 «Se queda corto»: aire en los cambios de zona, papel en las hojas, lápiz en las marcas, la ficha y la escala. Sin golpes.
python3 sfx_T03-2-r2.py T03-2-r2/sfx.wav T03-2-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('y')-.35,1.1,.3),(at('tu')-.4,.9,.2),(at('piensas')-.45,1.1,.3),(at('sabado')-.4,.9,.2),(at('pero')-.45,1.1,.3),(at('piernas')-.4,.9,.2),
              (at('y',4)-.4,1.1,.3),(at('sobre')-.5,1.3,.35),(at('con',2)-.4,1.0,.25),(at('y',5)-.45,1.0,.25),(at('al')-.4,1.4,.35),(at('uno')-.4,.9,.2),
              (at('si',2)-.45,1.1,.3),(at('tiro',2)-.4,.9,.2),(at('casa')-.2,1.3,.35),(at('apuntalo'),1.3,.4),(at('porque',2),1.5,.4)]:
    put(t,air(d),g)
for i in range(4): put(at('cuatro')-.1+i*.22,pencil(.2),.25)
for i in range(5): put(at('primer')-.2+i*.16,pencil(.16),.18)
for i in range(4): put(at('repite')-.25+i*.15,pencil(.18),.2)
put(at('metes')-.1,paper(.9),.2); put(at('nadie')-.1,pencil(.4),.25)
put(at('duro')-.05,pencil(.4),.3); put(at('por')-.05,pencil(.9),.28)
put(at('acortalo')-.1,paper(.6),.22)
for w,n in [('tiro',2),('ritmo',1),('casa',1)]: put(at(w,n)-.1,pencil(.45),.26)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
