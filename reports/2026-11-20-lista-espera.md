# Lista de espera: estado real y altas por día · Samuel (06) · 20/11 9:05

Fuente: base de datos de la app (Lovable, solo consultas de lectura), leída hoy a las 9:00. Un equipo está en la lista cuando tiene la prueba fijada para el 28/11 y la tarjeta pendiente (`organization_billing`: `trial_started_at` = 28/11, `card_required` = sí).

## La cifra real: 24 equipos
| Día | Equipos nuevos | Acumulado |
|---|---|---|
| Mar 17/11 | 15 | 15 |
| Mié 18/11 | 6 | 21 |
| Jue 19/11 | 2 | 23 |
| Vie 20/11 (hasta las 9:00) | 1 | 24 |

- 24 equipos, 24 cuentas distintas (un equipo por cuenta).
- Uno de los 24 se llama «Equipo ProTeam» (17/11 22:47): parece una prueba nuestra. Sin él, **23**.
- Antes del 17/11 no hay ninguno: las 5 cuentas anteriores (del 30/9 al 4/11) son pruebas previas, no lista.

## Por qué había dos cifras (15 y 9)
No se contradicen: **15** son los equipos que entraron el martes 17 (la foto de ese día, la que quedó en `agencia/ESTRATEGIA.md`) y **9** son los que han entrado después (6 + 2 + 1). Sumadas dan la real: 24.

## Lo que dicen los datos
- **Los 24 son de balonmano.** Ninguno de fútbol ni de baloncesto. Los nombres lo confirman en varios casos (clubes de balonmano de España y de fuera). Categorías: sobre todo infantil, cadete y sénior.
- **Hay equipos de fuera de España** (por el nombre, al menos tres de Latinoamérica y uno centroeuropeo).
- **El ritmo baja:** 15 → 6 → 2 → 1. El pico del 17 coincide con el Reel u08 (balonmano, 19.000 vistas).
- **Origen:** la base de datos no guarda de dónde viene cada alta (no hay campo de origen en la cuenta ni en el equipo). No se puede decir cuántos llegan de Instagram; solo que el pico coincide con u08.

## Qué haría con esto
1. Para el fin de semana, al menos un Reel de balonmano al día en buena hora (u75 el sábado, u71 el domingo): es el único deporte que está convirtiendo.
2. Fútbol y baloncesto llevan cuatro días con piezas y cero altas: mirar el lunes si llegan visitas a la web desde esas piezas o si se pierden antes.
3. Guardar el origen en el alta (un parámetro en el enlace de la bio) es un cambio pequeño en la app: propuesta para el equipo técnico, no hecha.

Consultas: recuento por `trial_started_at`, `card_required` y día de creación de la organización; listado de las 24 con deporte, categoría y hora de alta. No se ha leído ni guardado ningún correo ni nombre de persona.
