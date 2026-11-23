"""Efectos suaves de T05-1-r3 «Ciento tres y fuera»: aire en los cambios de zona, lápiz en las casillas, las rayas y las columnas, papel en las fichas y la libreta. Sin golpes.
python3 sfx_T05-1-r3.py T05-1-r3/sfx.wav T05-1-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('y')-.35,.9,.22),(at('partidos')+.4,1.1,.25),(at('oakland')-.4,1.1,.3),(at('equipo')-.35,.9,.2),(at('pocos')-.4,1.1,.3),(at('muchos')-.35,.9,.2),
              (at('ganaron')-.4,1.1,.3),(at('pero')-.4,1.1,.3),(at('minnesota')-.35,.9,.2),(at('pregunta')-.35,.9,.2),(at('tu')-.4,1.2,.3),
              (at('no',4)-.4,1.2,.35),(at('solo')-.4,1.0,.25),(at('apuntalo',2)+.1,1.3,.4),(at('como')+.0,1.5,.4)]:
    put(t,air(d),g)
for i in range(5): put(at('y')+.05+i*.28,pencil(.2),.2)
put(at('dos',2)-.15,paper(.5),.22); put(at('moneyball')-.1,pencil(.6),.22)
for i in range(12): put(at('muchos')-.1+i*.07,pencil(.1),.15)
put(at('mercado')-.1,pencil(.7),.22)
a,b=at('ganaron'),at('seguidas')+.3
for i in range(20): put(a+i*(b-a)/20,pencil(.14),.22)
put(at('record')-.15,paper(.45),.22)
for w in [('gana',1),('gana',1),('tres',2)]: pass
put(at('gana')-.1,pencil(.3),.22); put(at('gana')+.2,pencil(.3),.22); put(at('tres',2),pencil(.3),.25)
put(at('entonces')-.1,paper(.6),.28)
put(at('pierdes')-.1,pencil(.6),.2)
put(at('mal')-.1,pencil(.5),.3)
put(at('partido')-.1,pencil(.4),.25); put(at('ciento',2)-.15,pencil(.8),.25)
put(at('no',4)-.05,paper(.7),.3)
a,b=at('apuntalo')-.1,at('sabado',2)+.3
for i in range(22): put(a+i*(b-a)/22,pencil(.12),.18)
put(at('decide')-.1,pencil(.5),.25); put(at('quien')-.1,paper(.4),.2); put(at('martes')-.1,paper(.4),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
