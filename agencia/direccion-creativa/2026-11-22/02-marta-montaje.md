# Tres estilos de montaje · Marta (02) · 22/11/2026

**Estado:** propuesta para revisar. No se monta, no se genera voz ni música y no se renderiza nada (pausa total del 20/11).
**Base:** documento de dirección creativa (D1, D2, D3), `agencia/MARCA.md`, `REEL_ESTILO.md`, `DIRECCION_CREATIVA.md`, `agencia/APRENDIZAJES.md` y los guiones de Dani en `01-dani-reels.md`.

## Lo que comparten los tres (no cambia)
- **Lienzo:** 1080 × 1920, 30 fps. Tinta `#0d0f14`, negro, papel `#f2f1ec`, azul `#2f6bff`. Manrope 500/700/800 e Instrument Serif itálica en azul para la palabra emocional. Nada más.
- **Zona segura 9:16:** todo texto entre **y = 260 y y = 1600**, con **≥ 90 px a cada lado** y la columna derecha (x > 930) libre entre y = 1150 y y = 1750, donde Instagram pone los botones. Nada pegado a los márgenes, sin logos ni marcas de agua, sin URL en pantalla.
- **Texto:** frases o conceptos destacados, **máximo 5 palabras por golpe**, nunca subtítulos palabra a palabra. Cada golpe dura al menos el tiempo de leerlo dos veces (≈ 0,4 s por palabra, mínimo 1,2 s). Las fichas guardables, ≥ 2 s quietas.
- **Primer fotograma (dato del 17/11):** situación concreta, con deporte o categoría legible en el fotograma 0. Nunca negro, nunca texto a máquina, nunca frase de marca. Una cara sola tampoco basta (u02).
- **Voz:** ElevenLabs, voz **Mateo** (`Rie0luvrYhyKLba1lK3c`), `eleven_v4`. ×1,08 en el cuerpo y ×1,0 en el cierre. Dos tomas, se elige una. Tiempos de montaje anclados al arranque real de cada palabra (`mktimes.py`, función `snap`); nunca se quitan silencios en automático ni se corta dentro de una palabra.
- **Mezcla:** voz `loudnorm` −15 LUFS; efectos a −10 dB respecto a la voz (×0,32), `alimiter`. Antes de entregar: nivel segundo a segundo (que la voz llegue al final), búsqueda de fotogramas congelados, cola ≤ 0,8 s tras la última palabra (hipótesis de u04) y ninguna pantalla de producto menos de 1,5 s.
- **Producto:** solo capturas o grabaciones reales; R4 confirma que son la versión publicada.

### Música: punto que tiene que decidir Biel
Hay dos reglas que chocan. `MARCA.md` (15/11, «fijo») y el documento de dirección creativa piden **música nueva en cada Reel, del estilo de referencia** (trap oscuro ~143 BPM, silencio antes de la palabra de impacto). `DIRECCION_CREATIVA.md` y la actualización del 14/11 en `REEL_ESTILO.md` dicen **sin música**.
**Propuesta:** seguir como se ha hecho desde u02: **dos másteres por Reel**, con música (generada y alineada) y sin música. Biel elige cuál sube. Los tres estilos de abajo funcionan con y sin música; donde la música cambia el montaje, lo indico.

---

## M1 · «Plano secuencia» (para D1, el tablero)
**Idea:** la cámara nunca corta dentro de un bloque; viaja por un espacio en 2,5D. El corte se reserva para cambiar de bloque narrativo.
- **Ritmo:** 5–7 bloques por Reel. Dentro de cada bloque, travelling lateral de 2–4 s y un **zoom rápido (0,25 s, ease-out)** al detalle cuando la voz lo nombra. **Un solo corte seco a negro** (0,3–0,5 s) antes de la revelación. Planos medios de 3–5 s: el ritmo lo da el movimiento, no el número de cortes.
- **Primer fotograma:** el objeto central del caso ya clavado y legible (la conclusión de D1-A, el «12 PARADAS · 20 GOLES» de D1-B, la carpeta EXPEDIENTE de D1-C), con la cámara ya moviéndose 2 % por segundo. Foto del referente o del deporte detrás, a media luz, para que el deporte se lea sin texto.
- **Texto:** vive en el tablero (etiqueta, nota, recorte), no flota encima. Etiquetas en Manrope 800 de 64–96 px; la palabra clave en Instrument Serif 110–140 px, escrita como a mano (trazo que se dibuja en 0,4 s). Al acercarse la cámara, el texto que se lee siempre cae dentro de la zona segura: se compone el tablero pensando en el encuadre final, no al revés.
- **Movimiento:** pistas que se clavan con un empujón de 4 % y sombra que se asienta; sellos DESCARTADO que caen fuera de plano; el **hilo azul** hace de transición (la cámara lo sigue hasta la pista siguiente).
- **Sonido:** chincheta seca al clavar, papel al girar una nota, tensión suave del hilo, sello con golpe grave, un «whoosh» corto en cada zoom. Silencio total de 1 s en la pausa del reto (D1-B). Con música: el corte a negro cae en el silencio previo al golpe.
- **Voz:** sin pausas añadidas salvo la marcada en el guion; el retroceso de cámara sincroniza con la primera frase.
- **Riesgo y antídoto:** si todo es tablero, cansa. Cada caso cambia de pared (corcho, pizarra de vestuario, mesa del cuerpo técnico) y de luz (lateral fría, cenital, contraluz de ventana).
- **Producción:** motor HTML con cámara 3D CSS (o `tools/kit3d/engine.js`) y render con Playwright, como los reels de `tools/reel*`; `times.js` manda toda la animación.

## M2 · «Documental respirado» (para D2, a pie de pista)
**Idea:** cámara real en mano, cortes con la respiración de la voz y silencios con sonido ambiente. Los gráficos acompañan a la persona y nunca la tapan.
- **Ritmo:** un plano por frase (1,5–3 s), con **jump cuts** dentro del mismo plano en vez de transiciones. Uno o dos silencios de 0,6–1 s con sonido ambiente antes de la frase importante. Transiciones «de objeto a objeto»: la mano tapa el objetivo, se gira el móvil o se cierra la libreta.
- **Primer fotograma:** el objeto que sitúa la escena en primer plano y nítido, con la hora o el lugar legibles (el móvil a las 8:15, el escritorio con la semana abierta, la libreta en la banda de un pabellón). Rótulo corto encima del objeto (**LUNES · 8:15**), nunca un título.
- **Texto:** muy poco y pegado a un objeto del plano (sobre la libreta, encima del móvil, en un pósit real). Gráficos POV ya hechos (`agencia/recursos/pov/`, g01–g10): entran con su WebM de 0,5 s cuando se nombra la cosa, salen en el corte siguiente y **nunca dos a la vez**. Tarjetas al 86 % de opacidad solo en el fondo del gráfico.
- **Imagen:** luz natural, grano ligero, desenfoque real; ningún efecto que simule cámara si la cámara es real. Corrección de color fría y contrastada, igual en todos los planos.
- **Sonido:** el ambiente es protagonista: taza en la mesa, páginas, zapatillas en el parquet, balón al fondo, silbato lejano. Efectos de interfaz solo cuando se ve el móvil. Con música: entra baja (−40 % bajo la voz) y se corta en los silencios de ambiente.
- **Voz:** Mateo a ×1,04 en vez de ×1,08 en D2 (más cercana); el «yo» es un personaje, nunca un testimonio de usuario.
- **Riesgo y antídoto:** imperfección sin control parece descuido. Regla: el temblor y el foco van solo en los cortes; el plano que se lee está estable al menos 1 s.
- **Producción:** depende de grabaciones reales (móvil vertical, 1080p o 4K a 30 fps, luz de ventana lateral, 1 s de margen por toma), como en la serie POV.

## M3 · «Pulso táctico» (para D3, la pista viva)
**Idea:** el suelo es la pizarra. La cámara vuela sobre la pista y cada idea se dibuja en el parquet o el césped; el corte cae en el pulso.
- **Ritmo:** movimientos de cámara largos (vuelo cenital → caída a ras de suelo en 1,5–2 s) y **cambio de escena en el golpe**. Con música, a ~143 BPM: los cambios caen cada 2 o 4 tiempos (≈ 0,84 s o 1,68 s). Sin música, en el arranque de la palabra clave. Líneas tácticas que se dibujan en 0,5–0,8 s.
- **Primer fotograma:** la pista o el campo ya reconocibles (líneas del deporte, porterías o canastas) con la situación dibujada: el balón robado (D3-A), los 14 dorsales cayendo (D3-B), la presión con el balón en el 1 (D3-C). La categoría en un rótulo pequeño en el suelo.
- **Texto:** en perspectiva, «pintado» en el suelo o de pie como un objeto que la cámara rodea. Cifras en Manrope 800 grandes (la cuenta de D3-B ocupa el círculo central). La palabra emocional en Instrument Serif, de pie. Comprobar que la proyección en perspectiva no saca ninguna letra de la zona segura en el fotograma final de cada plano.
- **Color:** dibujo táctico en blanco y azul; lo que está mal, en gris (nunca rojo). Lo que es **EJEMPLO**, rotulado como tal.
- **Sonido:** trazo de rotulador al dibujar, silbato corto en el cambio de escena, bote de balón o golpe de pie en el golpe de cámara, reloj en los conteos (D3-A). Con música: silencio de un compás antes de la regla o de la cuenta.
- **Riesgo y antídoto:** si se abusa, parece un videojuego. Máximo un vuelo largo por bloque; el resto, planos fijos con el dibujo animándose.
- **Producción:** `tools/kit3d/engine.js` (three.js) para la pista en 3D; fondo de pabellón o campo real. Fondos con IA solo si Biel aprueba la propuesta del documento (fondos sin personas).

---

## Qué estilo encaja con cada versión de Dani

| versión | estilo | por qué | ajuste propio |
|---|---|---|---|
| D1-A «Era el jueves» | **M1** | La conclusión clavada y el retroceso son un plano secuencia natural. | Retroceso continuo de 0 a 8 s sin cortes; los sellos DESCARTADO caen en el golpe de la palabra «Descartada». |
| D1-B «Desde dónde» | **M1** | El reto necesita ver las cuatro notas a la vez en un mismo espacio. | El único corte a negro es la pausa «Elige una» (2 s con contador); silencio total. |
| D1-C «Expediente: Estambul» | **M1** con un inserto **M3** | El expediente es tablero; los tres goles se entienden mejor dibujados. | 3–7 s: línea de tiempo del partido en el suelo (M3) y vuelta a la carpeta. |
| D2-A «Lunes, 8:15» | **M2** | Escena en tiempo real: cuanto menos montaje, más verdad. | Sin jump cuts entre 0 y 12 s (tiempo continuo); el silencio de la taza en 12 s. |
| D2-B «Empieza por el final» | **M2** con cierre **M1** | Documental para el antes; el producto pide pantallas estables. | El rebobinado es real (vídeo invertido 0,6 s, no un efecto); capturas ≥ 1,5 s cada una, en el móvil 3D (`tools/blackout/phone3d.html`) o grabadas. |
| D2-C «Nadie me enseñó» | **M2** | Confesión: manos, objetos y ambiente de pabellón. | Cada lección escrita en un objeto real (pósit, libreta, móvil); la nota final, ≥ 2,5 s quieta para guardar. |
| D3-A «Robas y nadie sale» | **M3** | Es una jugada: se dibuja, se rebobina y se redibuja. | El rebobinado recoge las líneas al revés, en 0,8 s, con sonido de cinta. |
| D3-B «Haz la cuenta» | **M3** | La cuenta pintada en el césped es el gancho visual. | Plano cenital fijo mientras se escribe la cuenta; vuelo solo al pasar a las barras. Se entiende sin sonido. |
| D3-C «Una regla» | **M3** | La comparación funciona en el mismo encuadre: misma jugada, una cruz. | Dos pasadas idénticas de cámara (antes y después) para que el ojo compare. |

## Orden de prueba que propongo (cuando se levante la pausa)
1. **M1 con D1-B**: no depende de grabación ni de datos externos y prueba el reto con pausa.
2. **M3 con D3-B**: prueba el motor de pista con la pieza más simple (plano cenital, una cuenta).
3. **M2** solo cuando haya grabaciones reales; mientras, no se simula.

Se mide como siempre (visita llena): saltos en 3 s, tiempo medio frente a duración, y guardados y compartidos por 1.000 vistas.
