"""Efectos suaves de T01-5-r2 «Diez baja»: aire en los movimientos de cámara, papel al doblar la hoja y al meterla en el bolsillo, lápiz en las preguntas, las respuestas y los hilos. Sin golpes.
python3 sfx_T01-5-r2.py T01-5-r2/sfx.wav T01-5-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('dos')-.3,.9,.25),(at('hoja')-.35,.9,.22),(at('escritas')-.4,1.0,.3),(at('sesenta')-.35,.8,.2),(at('perdiendo')-.45,.9,.22),(at('futbol')-.45,1.1,.3),
              (at('su')-.4,.9,.25),(at('tu')-.4,.9,.25),(at('pero')-.4,1.0,.28),(at('solo')-.45,.9,.2),(at('hoja',2)-.45,1.0,.28),(at('dentro')-.55,.9,.22),
              (at('llego')-.45,1.1,.3),(at('antes')-.35,.9,.25),(at('otras')-.4,.9,.25),(at('una',2)-.45,1.2,.32),(at('apuntalo')-.4,1.4,.4),(at('porque'),1.6,.4)]:
    put(t,air(d),g)
put(at('doblada')-.15,paper(.5),.3); put(at('bolsillo')-.1,paper(.7),.28); put(at('nadie',3)-.1,paper(.5),.22)
put(at('metro')-.2,pencil(1.0),.2)
for i in range(3): put(at('tres')-.05+i*.2,pencil(.2),.2)
put(at('cambiado')-.1,pencil(.55),.22); put(at('donde',2)-.25,pencil(.4),.2); put(at('quien')-.2,pencil(.4),.2)
for i in range(3): put(at('linea')-.1+i*.35,pencil(.3),.2)
put(at('respuesta',2)-.45,pencil(.7),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
