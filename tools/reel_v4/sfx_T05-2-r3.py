"""Efectos suaves de T05-2-r3 «Los tres empiezan en tu área»: aire en los cambios de zona, lápiz en las flechas, el acta, las columnas y las rayas, papel en las hojas. Sin golpes.
python3 sfx_T05-2-r3.py T05-2-r3/sfx.wav T05-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('y')-.35,1.0,.25),(at('tu')-.35,.9,.2),(at('cadete')-.4,1.1,.3),(at('campo')-.35,.9,.2),(at('tu',2)-.4,1.1,.3),
              (at('primer')-.35,.8,.18),(at('segundo')-.35,.8,.18),(at('y',3)-.35,.8,.18),(at('en')-.4,1.1,.3),(at('y',4)-.35,.9,.22),(at('como')-.4,1.1,.28),
              (at('tu',3)-.35,1.0,.2),(at('una')-.35,.9,.2),(at('si',3)-.35,1.0,.25),(at('apuntalo')+.1,1.3,.4),(at('porque',2)-.1,1.3,.35),(at('el',8)-.05,1.4,.35)]:
    put(t,air(d),g)
for i in range(3): put(at('flechas')-.1+i*.3,pencil(.5),.18)
put(at('perdido'),pencil(.6),.22); put(at('segundo')+.35,pencil(.6),.2); put(at('tercero'),pencil(1.2),.18)
put(at('acta')-.1,pencil(.8),.22); put(at('martes')-.1,pencil(.6),.2)
for w in ['tiros','perdidas','balones']: put(at(w,2 if w=='tiros' else 1)-.15,pencil(.55),.2)
for k in range(3): put(at('contra')+.05+k*.12,pencil(.12),.2)
put(at('contra',2)+.05,pencil(.15),.2)
a,b=at('una')-.05,at('accion')+.35
for k in range(6): put(a+k*(b-a)/6,pencil(.14),.22)
put(at('gana')-.1,pencil(.6),.22); put(at('martes',2)-.1,pencil(.45),.25); put(at('salida')-.1,pencil(.8),.2)
put(at('si',3)-.3,paper(.5),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
