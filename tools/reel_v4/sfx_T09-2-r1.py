"""Efectos suaves de T09-2-r1 «Siete minutos»: aire en los cambios de zona, papel en el peto y la nota, lápiz en el 7, los «10′», los círculos y la flecha. Sin golpes.
python3 sfx_T09-2-r1.py T09-2-r1/sfx.wav T09-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('sale')-.35,.8,.18),(at('le')-.35,.9,.2),(at('sabado')-.35,1.1,.3),(at('banquillo')-.45,1.1,.3),(at('peto')-.35,.8,.18),(at('nadie')-.35,.8,.18),
              (at('ibas')-.35,1.1,.28),(at('reloj')-.35,1.1,.28),(at('eso')-.35,1.1,.28),(at('peor',2)-.4,1.1,.3),(at('pregunta')-.35,.8,.18),(at('tampoco')-.3,.8,.15),
              (at('apunta')-.3,.8,.18),(at('descanso')-.35,.8,.18),(at('ese')-.35,.9,.22),(at('apuntalo')+.1,1.3,.38),(at('porque')+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('sale')-.05,paper(.6),.22)
put(at('siete')+.05,pencil(.55),.28)
put(at('ese')-.1,paper(.4),.2)
a,b=at('apunta')-.05,at('jugar',2)+.2
for i in range(18): put(a+i*(b-a)/18,pencil(.12),.17)
put(at('rodea')-.05,pencil(.4),.22); put(at('rodea')+.25,pencil(.4),.22)
put(at('entra'),pencil(.6),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
