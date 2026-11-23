"""Efectos suaves de T04-2-r1 «Dos paradas en un minuto»: aire en los cambios de zona, lápiz en el «1», las flechas, el hilo y la libreta, papel en las fichas y la nota. Sin golpes.
python3 sfx_T04-2-r1.py T04-2-r1/sfx.wav T04-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('y')-.35,.9,.2),(at('un')-.35,.8,.18),(at('mundial')-.4,1.1,.28),(at('cuartos')-.3,.8,.18),(at('y',2)-.35,1.1,.3),(at('entra')-.3,.9,.2),
              (at('solo')-.35,1.1,.3),(at('cinco')-.35,1.1,.3),(at('si')-.35,1.1,.3),(at('sin')-.3,.9,.2),(at('es',2)-.35,1.1,.3),(at('pitan')-.3,.8,.18),
              (at('acerto')-.35,1.1,.3),(at('paises',2)-.3,.9,.2),(at('tu',2)-.35,1.1,.3),(at('cada',3)-.3,.9,.2),(at('vuelta')-.35,.9,.2),(at('nombre')-.3,.8,.2),
              (at('apuntalo')+.1,1.3,.38),(at('porque')+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('uno')-.1,pencil(.45),.25)
put(at('cambia')-.05,paper(.5),.22); put(at('cambia')+.15,paper(.5),.2)
put(at('elegir')-.1,pencil(.4),.2); put(at('lado')-.1,pencil(.4),.2)
put(at('error')-.1,pencil(.45),.28); put(at('sin')-.1,pencil(1.4),.18)
put(at('estudiado')-.2,pencil(.6),.2); put(at('grecia')-.2,paper(.4),.2)
a,b=at('acerto'),at('todos')
for i in range(5): put(a+i*(b-a)/5,pencil(.3),.2)
put(at('ida')-.1,pencil(.45),.22)
a,b=at('cada',3)-.05,at('lado',3)+.2
for i in range(18): put(a+i*(b-a)/18,pencil(.12),.17)
put(at('bolsa')-.3,paper(.7),.25); put(at('nombre')-.25,paper(.4),.22); put(at('lado',4)-.1,pencil(.4),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
