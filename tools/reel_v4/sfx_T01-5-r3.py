"""Efectos suaves de T01-5-r3 «El penalti»: aire en los movimientos de cámara, lápiz en el círculo, el «4», las preguntas y las respuestas, papel en la hoja. Sin golpes.
python3 sfx_T01-5-r3.py T01-5-r3/sfx.wav T01-5-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('tres')-.35,1.0,.3),(at('eso')-.35,.8,.2),(at('ni')-.4,1.1,.3),(at('estan')-.4,.8,.22),(at('infantil')-.4,1.1,.3),(at('once')-.35,.8,.22),
              (at('segundo')-.4,.9,.25),(at('tu',2)-.4,1.0,.28),(at('porque',2)-.4,1.1,.3),(at('ahi')-.45,.9,.25),(at('cuatro',2)-.4,.9,.25),(at('cuando')-.45,1.1,.3),
              (at('nadie')-.4,.9,.25),(at('antes')-.4,.9,.25),(at('donde',2)-.55,.9,.25),(at('quien')-.4,.9,.25),(at('cambiado')-.6,.9,.25),(at('arbitro',2)-.65,1.2,.32),
              (at('apuntalo')-.4,1.4,.4),(at('porque',3),1.6,.4)]:
    put(t,air(d),g)
put(at('antes')-.1,paper(.6),.3)
put(at('cuatro',2)+.15,pencil(.45),.24); put(at('contar')-.35,pencil(.7),.24)
for i in range(3): put(at('tres',3)-.05+i*.2,pencil(.2),.2)
put(at('cambiado')-.2,pencil(.6),.22)
for i in range(3): put(at('arbitro',2)-.05+i*.3,pencil(.3),.2)
put(at('final'),pencil(.45),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
