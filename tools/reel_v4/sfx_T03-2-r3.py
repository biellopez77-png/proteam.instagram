"""Efectos suaves de T03-2-r3 «El castigo del jueves»: aire en los cambios de zona, lápiz en las carreras, la pizarra y la escala, papel en las notas. Sin golpes.
python3 sfx_T03-2-r3.py T03-2-r3/sfx.wav T03-2-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('por')-.35,.9,.25),(at('y')-.35,.9,.2),(at('perdiste')-.35,.9,.2),(at('jueves')-.45,1.2,.35),(at('ultimo')-.3,.9,.2),(at('partido')-.35,.9,.2),
              (at('lo',2)-.4,1.1,.3),(at('tercer')-.35,.9,.2),(at('problema')-.4,1.1,.3),(at('piernas')-.35,.9,.2),(at('jueves',2)-.35,.9,.2),(at('y',2)-.4,1.1,.3),
              (at('y',3)-.4,1.1,.3),(at('un',3)-.45,1.5,.4),(at('al',2)-.35,.9,.2),(at('lo',4)-.4,1.1,.3),(at('jueves',4)-.35,1.3,.35),(at('apuntalo')+.1,1.3,.4),(at('porque',2),1.5,.4)]:
    put(t,air(d),g)
for i in range(10): put(.05+i*.15,pencil(.22),.22)
for i in range(10): put(at('y',3)-.1+i*.1,pencil(.18),.18)
put(at('castigo')-.15,pencil(1.0),.3); put(at('corran')-.1,pencil(.5),.28); put(at('tercer')-.1,pencil(.4),.25)
put(at('siguiente')-.15,paper(.45),.22); put(at('perder',2)-.15,paper(.45),.22)
put(at('nadie')-.1,paper(.4),.2)
put(at('un',3)-.2,pencil(1.2),.22)
put(at('diez',2)-.05,pencil(.4),.3); put(at('minutos')-.1,pencil(.8),.28)
put(at('martes')-.15,paper(.7),.25); put(at('jueves',4)-.05,paper(.5),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
