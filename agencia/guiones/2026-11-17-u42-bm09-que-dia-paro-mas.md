# u42 · bm-09 · «Sábado: le meten 28. Domingo: le meten 20. ¿Qué día paró más?» (balonmano)

- **fase: solución (mar 24 tarde – mié 25; enseña la app)** (lanzamiento, `agencia/LANZAMIENTO.md`; marcado por Dani el 17/11 21:10)
- **Estado: listo para producir** · **Crítica de Andrés: 81/100** (guion, escala 16/11) · riesgo de salto bajo · crítica en `agencia/criticas/2026-11-17-u42-guion.md`
- **Deporte:** balonmano · **Encargo:** t-20261117-01-guiones-23-24 (horizonte de 15 días).
- **Cuándo:** semana del 23/11 (lunes 23 a viernes 27), cierre de campaña con la **animación del contador de la lista de espera** (como u28 v3) y «HASTA EL 27 NOV». Desde el 28/11, cierre A de `CIERRE_DESDE_28N.md`. No el mismo día que u23 (también va de portero) ni que u29 (mismo registro «gol o parada»).
- **Insight:** I-030 (`intel/insights/INSIGHTS.md`) · **Territorio:** errores normalizados (u37 en las últimas 10; 2 de 10).
- **Idea en una frase:** al portero de base se le juzga por los goles que encaja, y los goles dependen de cuántos tiros recibe: el día que más le metieron puede ser el día que más paró.

## 1. Objetivo estratégico
Envíos al segundo y al entrenador de porteros con un acertijo que se resuelve con una división, y guardados con un método de tres pasos. Presenta el resumen del partido con el porcentaje del portero.

## 2. Público y escena
Entrenador de balonmano de base (infantil, cadete, juvenil). Fin de semana con dos partidos. Lunes: «el sábado, veintiocho goles; tenemos que hablar».

## 3. Insight y procedencia
En base se cuenta lo que se ve en el marcador (goles encajados) y no lo que no se ve (tiros recibidos), así que el portero recibe la bronca el día que su defensa le deja tirar más. Inferido (sin cita ni cifra). Los números del ejemplo son una escena con cuentas exactas, no estadística:
- Sábado: 47 tiros a puerta, 28 goles → 19 paradas → 19/47 = **40 %**.
- Domingo: 30 tiros a puerta, 20 goles → 10 paradas → 10/30 = **33 %**.
(Cuenta comprobada el 17/11; se redondea a entero.)

## 4. Lo que es verdad y de dónde sale
- **Captura real** `PROTEAM_PRODUCTO_RESULTADOS_CAPTURA_001` (mirada el 17/11): pestaña Resumen del partido, «Nosotros y rival» con **«% portero 50 % · 21 %»**, Lanzamientos 39 · 34, Eficacia 67 % · 50 %. **Sin usar hasta hoy.**
- **Captura real** `PROTEAM_PRODUCTO_REGISTRO_ACCION_CAPTURA_005` (paso «¿Gol o parada?», ya mirada para u29): de apoyo, 1 s.
- **Se dice:** que en la app cada tiro se apunta como gol o parada y que el resumen del partido da el porcentaje del portero. **No se dice:** que la app compare partidos ni dé el porcentaje de la temporada (no lo hemos visto).
- En pantalla, las cifras de la captura (50 % · 21 %) son del partido de demostración y no se mezclan con las del ejemplo (28 y 20).

## 5. Voz (voz Mateo · 106 palabras · ≈ 35 s (más el contador))
| # | Bloque | Texto | Qué añade |
|---|---|---|---|
| 1 | H | Sábado: le meten veintiocho. Domingo: le meten veinte. ¿Qué día paró más tu portero? | dos números y una pregunta en el segundo 0 |
| 2 | Giro | El sábado. Le tiraron cuarenta y siete y paró diecinueve: un cuarenta por ciento. El domingo le tiraron treinta y paró diez: un treinta y tres. | la cuenta que cambia la respuesta |
| 3 | Consecuencia | Si solo cuentas goles, el lunes le riñes el día que mejor estuvo. | el coste |
| 4 | Guardable | Guárdatelo: apunta cada tiro a puerta, no solo los goles. Paradas entre tiros. Y el lunes, a tu portero, el porcentaje. | el método en tres pasos |
| 5 | Producto | En la app de ProTeam cada tiro es gol o parada, y el resumen del partido te da el porcentaje del portero. | la app lo hace (captura real) |
| 6 | Reto | Pregúntale a tu segundo: ¿qué día paró más el vuestro? | reto; repite la pregunta del hook |

Silencio de 0,4 s antes de «El sábado». Sin pausa antes del reto.

## 6. Pantallas (máx. 5 palabras por golpe; recortadas el 18/11, encargo de Biel de menos texto)
| s | pantalla |
|---|---|
| 0–3,8 | Foto a sangre: portero de primer nivel en estirada (Asobal, EHF o selección; Pau) · desde el fotograma 0, a dos columnas: **SÁB 28 · DOM 20** · en el 2,5: **¿QUÉ DÍA PARÓ MÁS?** |
| 3,8–11,0 | las dos columnas se rellenan en motion graphics (no es la app): **SÁB 47 tiros · 19 paradas → 40 %** / **DOM 30 tiros · 10 paradas → 33 %**; el 40 % se enciende en azul |
| 11,0–14,0 | foto del portero, más oscura · **LE RIÑES EL MEJOR DÍA** |
| 14,0–20,5 | ficha guardable: **PORTERO, EL LUNES** · 1 Cada tiro, apuntado · 2 Paradas ÷ tiros · 3 Dile el porcentaje · abajo, serif azul: *porcentaje, no goles* |
| 20,5–26,5 | móvil: captura real REGISTRO_ACCION_005 («¿Gol o parada?») 1 s → captura real RESULTADOS_001 con «% portero» recuadrado ≥ 2,5 s |
| 26,5–30,0 | vuelve la foto del principio (bucle) · RETO PARA TU STAFF · **¿Y el vuestro?** |
| 30,0–33,0 | **cierre de campaña con la animación del contador de la lista de espera** (la de u28 v3 / u09: contador que corre, correo, toque, «Estás dentro») → «3 meses gratis · HASTA EL 27 NOV» |

## 7. Descripción
Sábado le meten 28. Domingo le meten 20. ¿Qué día paró más tu portero? 🤾
El sábado: 19 paradas de 47 tiros (40 %). El domingo: 10 de 30 (33 %).
Guárdalo: 1) apunta cada tiro a puerta, no solo los goles; 2) paradas entre tiros; 3) el lunes, a tu portero, el porcentaje. En la app de ProTeam cada tiro es gol o parada y el resumen del partido te da el porcentaje del portero.
Envíaselo a tu segundo entrenador: ¿qué día paró más el vuestro?
Comenta tu deporte, tu categoría y tus días y te preparo la primera semana en la app de ProTeam. Lista de espera hasta el 27 de noviembre: 3 meses gratis. Enlace en la bio.

Foto: (crédito de Pau). Las cifras son un ejemplo con las cuentas hechas.

#balonmano #balonmanobase #entrenadordebalonmano #porterobalonmano #proteam

**Desde el 28/11:** cierre A de `CIERRE_DESDE_28N.md` («Pruébalo en la app de ProTeam.»), sin fecha ni oferta.

## 8. Hooks (0–3 en curiosidad · relevancia · tensión · claridad · coherencia; ≥ 11 pasa)
| # | tipo | hook | total |
|---|---|---|---|
| 1 | acertijo con números | **Sábado: le meten 28. Domingo: le meten 20. ¿Qué día paró más?** (elegido) | **14** (3·3·3·3·2) |
| 2 | contraintuitivo | El día que más goles encajó tu portero fue su mejor partido. | 12 (3·3·2·2·2) |
| 3 | número | 28 goles encajados. 40 % de paradas. | 12 (2·3·2·3·2) |
| 4 | frase oída | «Veintiocho goles, tenemos que hablar.» Y paró diecinueve. | 12 (3·2·3·2·2) |
| 5 | pregunta directa | ¿Cuántos tiros recibió tu portero el sábado? | 11 (2·3·1·3·2) |
| 6 | error | Juzgas a tu portero por el marcador. | 10 |
| 7 | comparación | 28 goles con 47 tiros. 20 goles con 30. | 10 (se entiende tarde) |
| 8 | escena | Lunes, vídeo: tu portero, mirando los 28 goles. | 9 (no se cuenta qué pasa) |

## 9. Diferenciación (frente a los cinco últimos Reels publicados o programados y la reserva)
| pieza | qué comparte | ejes distintos |
|---|---|---|
| u29 «26–17. Tira tu lateral.» (programado hoy) | registro «gol o parada» | 4: problema (cómo se juzga al portero, no quién apunta), captura principal distinta (RESULTADOS_001), acertijo, ficha |
| u23 «Tu portero, solo, contra la pared» | el portero | 4: medir, no entrenar; números en el hook; producto distinto; reto |
| u37 «Siete metros. Minuto 58.» | balonmano, «apunta cada…» | 3: otro jugador, otra métrica (porcentaje), estructura del hook (acertijo con respuesta) |
| u34 «Minuto 45: 0-1» (fútbol) | goles encajados | 4: deporte, minuto frente a porcentaje, sin actualidad |
| u33 «Brazo arriba: 4 pases» (programado) | balonmano, número en 0 s | 4: regla frente a medición, producto, reto |

## 10. Riesgos de ejecución
- **Recurso que falta:** portero de balonmano de primer nivel en estirada con licencia (Pau). Hay porteros en el banco de balonmano (`agencia/recursos/2026-11-16-banco-balonmano.md`).
- Las dos columnas del principio son motion graphics: estilo distinto de la app, para que no parezca una pantalla de ProTeam.
- La voz dice cuatro cifras seguidas en el bloque 2: los rótulos tienen que ir a la vez que la voz, nunca antes.
- No mezclar el 50 % de la captura con el 40 % del ejemplo: la captura sale después de la ficha y con el recuadro solo en «% portero».

## 11. Por qué merece publicarse
Es un acertijo que se contesta en tres segundos y deja mal la costumbre de todos los banquillos: dan ganas de mandárselo al entrenador de porteros. Y la app hace exactamente la cuenta que pide el método.

## Diez preguntas de control
1. ¿Le interesa? Sí: todos los lunes se habla del portero. 2. ¿Algo concreto? 28/20, 47/30, 40 %/33 %. 3. ¿Idea para recordar? «Los goles dicen cuánto le tiraron.» 4. ¿Distinta? Primer Reel con el porcentaje del portero y primera vez de RESULTADOS_001. 5. ¿Prueba de la otra cuenta? La cuenta la podría hacer otra; el resumen con «% portero» de la app, no. 6. ¿Valor? Método de tres pasos y una división. 7. ¿Formato? Reel con voz, ≈ 35 s. 8. ¿Interés? Respuesta a los 3,8 s, ficha a los 14, app a los 20,5. 9. ¿Realista? Una foto, motion graphics, dos capturas reales y la animación del contador ya hecha. 10. ¿Representa a ProTeam? Sí: partido en directo y resumen.

## Debilidades que conozco
- Los números son un ejemplo, no un partido real: se dice en la descripción.
- El porcentaje también depende de la defensa (de dónde le tiran): el guion no lo niega, pero no entra.
