"""Efectos suaves de T01-1-r2 «El vestuario te mira»: aire en los movimientos de cámara, papel en la hoja doblada y en el papel de Lehmann, lápiz en las tres líneas. Sin golpes.
python3 sfx_T01-1-r2.py T01-1-r2/sfx.wav T01-1-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('manos')-.3,.9,.25),(at('en')-.4,1.1,.3),(at('lehmann')-.4,.9,.25),(at('penalti')+.2,.9,.22),(at('cambiasso')-.4,1.0,.3),
              (at('miro')-.4,1.1,.3),(at('segun')-.25,.8,.2),(at('lo',2)-.4,1.1,.3),(at('volvemos')-.45,1.4,.38),(at('has')-.35,1.1,.3),
              (at('ni')-.35,.9,.22),(at('asi')-.4,1.3,.32),(at('y',4)-.25,1.0,.25),(at('desde',2)-.4,1.1,.3),(at('tres')-.35,.9,.22),
              (at('leelo')-.4,1.1,.3),(at('apuntalo')-.4,1.3,.38),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
put(at('cambiasso')-.05,paper(.4),.22); put(at('papel',2)-.05,paper(.7),.35); put(at('leelo')-.1,paper(.5),.25)
for w,n in [('que',5),('que',6),('un',3)]: put(at(w,n)-.05,pencil(.7),.3)
put(at('cambio')+.3,pencil(.5),.25); put(at('estaba')-.1,pencil(.45),.2)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
