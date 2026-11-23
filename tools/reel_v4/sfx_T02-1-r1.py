"""Efectos suaves de T02-1-r1 «La cuarta semana»: aire en los cambios de zona, lápiz en el círculo de la cuarta fila, la tiza, los hilos y los círculos de enero, papel en las fotos, la nota y la ficha. Sin golpes.
python3 sfx_T02-1-r1.py T02-1-r1/sfx.wav T02-1-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
CUT1=at('softly')-.1; CUT2=at('un')-.15
for t,d,g in [(at('no')-.25,.9,.2),(at('dura',2)-.3,1.0,.25),(at('ultimo')-.35,1.2,.3),(at('partidillo')-.25,.9,.2),(at('turron')-.2,.9,.2),
              (at('reyes')-.25,.9,.2),(at('primer')-.35,1.2,.3),(at('rondo')-.25,.9,.2),(at('piensas')-.3,1.1,.3),(at('pero')-.25,1.0,.25),
              (at('si')-.3,1.1,.3),(at('si',2)-.25,.9,.2),(CUT1-.1,1.0,.25),(CUT2-.1,1.1,.3),(at('dos')-.25,.9,.2),(at('y',3)-.2,.9,.2),
              (at('por')-.35,1.2,.3),(at('diez')-.25,.9,.2),(at('y',4)-.25,.9,.2),(at('el',6)-.2,.8,.2),(at('lo')-.2,.8,.2),
              (at('apuntalo')-.15,1.2,.35),(at('porque')-.05,1.3,.3)]:
    put(t,air(d),g)
put(at('cuatro')-.1,pencil(.7),.25); put(at('piensas')+.05,pencil(.9),.22); put(at('cargas')-.1,pencil(1.2),.2); put(at('si',2),pencil(1.2),.2)
for i in range(4): put(CUT1+.3+i*.55,pencil(.5),.16)
put(at('ultimo')-.05,paper(.5),.2); put(at('diez')-.35,paper(.45),.22); put(at('un')+.05,paper(.45),.2); put(at('martes',3)-.1,pencil(.4),.18); put(at('miercoles',2)-.3,paper(.4),.18)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
