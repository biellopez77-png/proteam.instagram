# Scene Plan · Wooden y los calcetines (ejemplo v7)

**Datos del proyecto**
- **Formato y FPS:** 1080×1920, 30 fps.
- **Duración:** 19,6 s de historia y 5,6 s del cierre de ProTeam (25,2 s en total).
- **Presets:** `photo-storytelling-red`, adaptado a la paleta ProTeam: el beige pasa a la pared azul noche y el rojo, al azul #6AA8FF. El ultravioleta #8B5CF6 sale una sola vez, en el recuadro de los pies.
- **Pipeline:** HTML + GSAP con Chrome headless (`tools/blackout/htmlreel.py`), y FFmpeg y Python para el audio, en el sandbox de Higgsfield.
- **Transiciones (agencia/sistema-v7/FORMATO.md):**
  - un solo plano;
  - viajes de 0,9 s `power2.inOut`, que empiezan en la pausa de la voz;
  - zoom de respiración ×0,9;
  - desenfoque de 4 px como máximo, solo a alta velocidad;
  - sin destellos;
  - empujes dentro de una escena de 1,1 s;
  - fundido de 0,6 s al cierre.

| Escena | Inicio–fin | Voz | Visual principal | Texto en pantalla (palabra a palabra) | Movimiento | Entrada | Audio |
|---|---|---|---|---|---|---|---|
| 01 | 0,00–2,38 | Primer día de entrenamiento en UCLA | Retrato de Wooden, anuario de 1960, enmarcado | «Primer día de entrenamiento» / «en **UCLA**.» | Acercamiento lento ×1,08 | La foto sube y se endereza (0,6 s) | Papel sobre la pared |
| 02 | 2,38–7,62 | Los mejores jugadores del país… y John Wooden les enseña a ponerse los calcetines | Foto de grupo de 1965 (LA Times, CC BY 4.0) | «Los mejores jugadores del país…» / «y John Wooden les enseña» / «a ponerse los **calcetines**.» | Viaje de 0,9 s; en «ponerse», empuje de 1,1 s hacia los pies | Recuadro UV a trazos sobre los pies en «calcetines» | Aire suave, papel y carta |
| 03 | 7,62–11,02 | Sin una arruga. Los cordones, bien apretados | Calcetín y zapatilla dibujados | «Sin una **arruga**.» / «Los cordones,» / «bien **apretados**.» | Viaje y bajada lenta del calcetín a la zapatilla | En «arruga», las arrugas se alisan con un barrido de luz; los cordones se dibujan y en «apretados» se cierran | Tela y cordones |
| 04 | 11,02–15,06 | Una arruga es una ampolla. Y una ampolla, un entreno perdido | Tres tarjetas encadenadas y la semana | Rótulos de las tarjetas | Viaje y deriva | Cada tarjeta entra en su palabra, las flechas se dibujan en «es» e «Y» y la X tacha el martes en «perdido» | Tarjetas y rotulador |
| 05 | 15,06–17,02 | Diez títulos en doce años | Vitrina de los 12 años (1964–1975) | Contador 0→10 / «títulos en 12 años» | Viaje y deriva | Los 10 años con título se encienden uno a uno; 1966 y 1974 se quedan apagados | Clics suaves |
| 06 | 17,02–19,60 | Todo empezaba por los pies | Retrato recortado (anuario de UCLA, dominio público) | «Todo empezaba» / «por los **pies**.» y «John Wooden» letra a letra | Viaje y acercamiento ×1,1 | Retrato que sube | Papel |
| Cierre | 19,60–25,20 | Estamos terminando la app de ProTeam… | `tools/reel_v6/outro/outro.mp4` | — | Fundido de 0,6 s | — | Cola de la voz del cierre |

**Mezcla**
- Voz a −19 dB RMS.
- Música real de Epidemic Sound («Orchestra, Piano, Choir, Sentimental», desde los 2 s) a −31 dB, que baja suavemente bajo la voz.
- Efectos reales de Epidemic Sound con ganancias entre 0,035 y 0,13.
