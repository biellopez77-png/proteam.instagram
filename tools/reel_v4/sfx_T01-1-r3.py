"""Efectos suaves de T01-1-r3 «Trece mil para siete»: aire en los movimientos de cámara, papel en el papel de Lehmann, en la hoja vacía y en la ficha que se pega en enero, lápiz en «Cambiasso», en las tachaduras y en las tres líneas. Sin golpes.
python3 sfx_T01-1-r3.py T01-1-r3/sfx.wav T01-1-r3/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('penaltis')-.1,.8,.2),(at('para')-.25,1.1,.3),(at('siete')-.3,.8,.2),(at('lehmann')-.4,1.2,.35),(at('argentina')-.35,.8,.2),(at('dos')-.35,.8,.2),
              (at('el')-.4,1.0,.28),(at('falta')-.3,.8,.2),(at('no')-.35,.8,.2),(at('lo')-.4,1.1,.3),(at('inter')-.35,.8,.2),(at('ahora')-.45,1.3,.36),
              (at('que',4)-.35,1.0,.28),(at('acuerdas')-.4,1.2,.32),(at('llovia')-.35,.8,.2),(at('arbitro')-.35,.8,.2),(at('pero')-.3,1.0,.26),
              (at('viste')-.4,1.1,.3),(at('extremo')-.35,.8,.2),(at('al')-.4,1.0,.28),(at('leelas')-.4,1.3,.32),(at('apuntalo')-.4,1.3,.38),(at('porque')+.05,1.6,.4)]:
    put(t,air(d),g)
put(at('para')+.3,paper(.5),.22); put(at('ni')-.25,paper(.6),.3); put(at('leelas')+.3,paper(.5),.28); put(at('primera')-.05,paper(.7),.3)
put(at('falta')-.05,pencil(.9),.28)
for i in range(4): put(at('ahora')-.1+i*.14,pencil(.25),.2)
put(at('enero')-.05,pencil(.8),.18)
for w,n in [('peligroso',1),('banda',2),('balon',1)]: put(at(w,n)-.05,pencil(.7),.3)
put(at('parado')+.3,pencil(.5),.22)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
