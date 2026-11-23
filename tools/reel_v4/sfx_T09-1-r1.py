"""Efectos suaves de T09-1-r1 «La banda del minuto ocho»: aire en los cambios de zona, papel en el cartel y la libreta, lápiz en las carreras, el 0-1 y las tres líneas. Sin golpes.
python3 sfx_T09-1-r1.py T09-1-r1/sfx.wav T09-1-r1/times.js"""
import sys, json, numpy as np
exec(open('sfx_a1.py').read().split("for t,d,g in")[0].split('"""',2)[2])
for t,d,g in [(at('cambias')-.35,.8,.18),(at('marcador')-.35,.9,.2),(at('cero')-.35,.7,.15),(at('cadete')-.45,1.1,.28),(at('los')-.35,1.0,.25),
              (at('banda')-.35,.8,.18),(at('en')-.4,1.1,.28),(at('tres')-.35,.9,.22),(at('banquillo')-.4,1.0,.25),(at('y',4)-.35,.8,.15),
              (at('asi')-.4,1.0,.25),(at('duelo')-.5,.8,.15),(at('quien')-.35,.8,.15),(at('es')-.4,1.0,.22),(at('apuntalo')-.4,1.3,.38),(at('porque',2)+.0,1.5,.38)]:
    put(t,air(d),g)
put(at('cambias')-.1,paper(.5),.22); put(at('banquillo')-.1,paper(.6),.2)
for w,n in [('tres',1),('carreras',1),('banda',2)]: put(at(w,n)-.1,pencil(.6),.24)
put(at('gol')-.45,pencil(.8),.28)
for a,b in [(at('primeros')-.1,at('minutos')+.35),(at('donde')-.1,at('atacan')+.4),(at('duelo')-.15,at('pierdes')+.4),(at('quien')-.05,at('piernas')+.4)]:
    for i in range(8): put(a+i*(b-a)/8,pencil(.12),.16)
put(at('ese')-.1,pencil(.5),.24)
wavfile.write(sys.argv[1],SR,(np.clip(out,-1,1)*32767*.9).astype(np.int16)); print('ok')
