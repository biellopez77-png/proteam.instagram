"""Efectos suaves de T06-1-r2 «Dos palabras»: aire en los cambios de zona, papel en la foto y el recorte, lápiz en el hilo, la carrera, las flechas, «Bien hecho» y la libreta. Sin golpes.
python3 sfx_T06-1-r2.py T06-1-r2/sfx.wav T06-1-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('ferguson')-.35,.8,.18),(at('mejores')-.35,.7,.14),(at('casi')-.35,.7,.14),(at('sir')-.35,.9,.2),(at('harvard')-.35,.7,.14),
              (at('cadete')-.5,1.1,.3),(at('nadie',2)-.4,1.0,.25),(at('vestuario')-.4,1.0,.25),(at('carrera')-.4,.8,.18),(at('aprende')-.35,1.0,.25),
              (at('sabado')-.35,.9,.2),(at('queda')-.35,.7,.15),(at('contraataque',2)-.35,.8,.16),
              (at('banda',2)-.4,1.1,.28),(at('acabar')-.35,.8,.18),(at('apuntalo')-.4,1.3,.38),(at('porque')+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('ferguson')-.3,paper(.5),.2); put(at('sir')-.3,paper(.5),.18)
put(at('sir'),pencil(.6),.16); put(at('dos',2),pencil(.5),.18)
put(at('corre'),pencil(1.2),.12)
for w in ('gol','penalti','cambio'): put(at(w)-.15,pencil(.45),.2)
a,b=at('bien')-.05,at('hecho')+.45
for i in range(8): put(a+i*(b-a)/8,pencil(.12),.18)
put(at('superlativos')-.1,pencil(.5),.2)
a,b=at('apunta')-.1,at('minuto',3)+.5
for i in range(16): put(a+i*(b-a)/16,pencil(.12),.16)
put(at('minuto',4)-.1,pencil(.6),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
