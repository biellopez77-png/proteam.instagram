"""Efectos suaves de T01-2-r1 «La pizarra que se olvidó de uno»: aire en los movimientos de cámara, lápiz al tachar el 3-0 y al escribir el plan B, papel en la libreta y roce al borrar la pizarra. Sin golpes.
python3 sfx_T01-2-r1.py T01-2-r1/sfx.wav T01-2-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('en')-.15,1.0,.26),(at('y')-.3,.9,.24),(at('tres')-.4,.8,.18),(at('estambul')-.4,1.0,.28),(at('quince')-.35,.8,.2),(at('benitez')-.4,1.1,.3),
              (at('once')-.35,.8,.2),(at('y',3)-.35,.9,.24),(at('tienes',2)-.35,.9,.24),(at('segundo')-.4,.8,.2),(at('doce')-.4,.8,.2),(at('lo')-.4,1.1,.3),
              (at('una',2)-.35,.8,.2),(at('en',3)-.4,1.0,.26),(at('apuntalo')-.4,1.3,.38),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
put(at('cero')+.05,pencil(.5),.3)
put(at('olvida')-.15,paper(.8),.32)
put(at('plan')-.05,pencil(.6),.28); put(at('plan')+.45,pencil(.4),.22); put(at('viernes')-.1,paper(.5),.2)
put(at('si')-.05,pencil(1.4),.26); put(at('sale')-.1,pencil(1.2),.26)
put(at('eliges')-.2,paper(.4),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
