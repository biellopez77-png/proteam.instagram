"""Efectos suaves de T01-6-r1 «Nuestro error»: aire en los cambios de zona, papel al destapar la firma y al desplegar el 3-5-2,
lápiz en las flechas, el gol y la libreta. Sin golpes.
python3 sfx_T01-6-r1.py T01-6-r1/sfx.wav T01-6-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('dice')-.35,.8,.16),(at('y')-.3,.9,.2),(at('papel')-.35,.8,.16),(at('y',2)-.25,.8,.16),(at('enero')-.4,1.0,.22),(at('liverpool')-.45,.8,.16),
              (at('klopp',2)-.4,1.0,.22),(at('lucas')-.45,1.0,.22),(at('pero')-.35,.8,.16),(at('y',5)-.3,.8,.16),(at('corre')+.2,1.4,.28),
              (at('ahora')-.4,1.2,.26),(at('y',7)-.35,.8,.16),(at('gol')-.4,.8,.18),(at('contra')+.3,1.2,.26),(at('tres',2)-.4,.8,.16),
              (at('diez',2)-.4,.9,.2),(at('una',2)-.35,1.1,.26),(at('apuntalo')-.35,1.2,.32),(at('para')-.1,1.4,.34)]:
    put(t,air(d),g)
put(at('klopp')-.15,paper(.5),.22)
put(at('cambia'),paper(.6),.22)
a0=at('contarselo'); a1=at('marcha')
for k in range(10): put(a0+(a1-a0)*k/10,pencil(.3),.16)
put(at('gol')-.1,pencil(1.0),.22)
for i,w in enumerate(['quien','quien','quien']): put(at('quien',i+1),pencil(.45),.28)
put(at('diez',2),pencil(.8),.16)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
