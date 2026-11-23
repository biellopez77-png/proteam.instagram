"""Efectos suaves de T02-1-r2 «La salida de noviembre»: aire en los cambios de zona, borrador y lápiz en la pizarra, papel en las notas y la libreta, lápiz en la lista. Sin golpes.
python3 sfx_T02-1-r2.py T02-1-r2/sfx.wav T02-1-r2/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('en')-.35,.9,.25),(at('hoy')-.35,.9,.25),(at('primer')-.4,1.1,.35),(at('tu')-.35,.9,.25),(at('tres')-.35,.9,.25),(at('pides')-.5,1.3,.4),
              (at('los')-.35,.9,.2),(at('y')-.35,.9,.2),(at('asi')-.35,.9,.2),(at('y',2)-.45,1.2,.35),(at('como')-.35,.9,.25),(at('lo')-.4,.9,.2),(at('tu',2)-.35,.9,.2),
              (at('tres',2)-.35,.9,.25),(at('enero')-.45,1.2,.35),(at('apuntalo')-.4,1.3,.4),(at('porque'),1.5,.4)]:
    put(t,air(d),g)
put(at('queda')-.25,paper(1.1),.22)                      # borrador
put(at('en')-.15,paper(.4),.25); put(at('septiembre')-.25,paper(.45),.28)   # notas
put(at('martes')-.1,pencil(.5),.25)
for w in ['tres','semanas','parado']: put(at(w)-.15,pencil(.4),.22)
put(at('delantero')-.1,pencil(.4),.2)
put(at('abrir')-.15,pencil(.5),.25); put(at('bajar')-.15,pencil(.45),.25)
put(at('no',2)+.05,paper(.6),.22)                         # libreta
put(at('tres',2)+.05,pencil(.9),.24); put(at('cada')-.05,pencil(.9),.24); put(at('ajuste',2)-.2,pencil(.7),.24)
put(at('enero')-.05,paper(.5),.25)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
