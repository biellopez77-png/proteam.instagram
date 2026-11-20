# Informe de la noche · viernes 20/11

**Leyenda:**
- **Implementado:** está en el código.
- **Probado:** se ha comprobado que funciona.
- **Publicado:** está en producción.
- **Diseñado:** existe como propuesta o archivo, todavía no en la app.

## Por qué estaba todo parado
Desde el jueves a las 8:40, **todas las tareas programadas fallan con «límite de uso alcanzado»** (USAGE_LIMIT_REACHED).
- Son unas 20 tareas, muchas cada hora: más de 100 ejecuciones al día que gastan del mismo límite que tu suscripción.
- **Consecuencia:** el jueves no se publicó nada. El contexto (u51, u72, u68), c17s3 y c18 siguen pendientes. El publicador los moverá solo al siguiente hueco libre (`pub.py late`) cuando vuelva a funcionar.
- **Solución:** decisión abierta en el panel de Álex. Activar créditos extra en claude.ai/settings/usage, aplicar el horario ligero, o las dos cosas (recomendado).

## Qué está hecho

| # | Entregable | Estado | Dónde |
|---|---|---|---|
| 1 | Planning actualizado (dónde estamos de verdad, fin de semana problema → nutrición → solución, nueva distribución, «menos ruido») | Hecho | `agencia/LANZAMIENTO.md` (bloque ACTUALIZACIÓN 20/11) y panel de Álex |
| 2 | Encargos para todos los agentes | Hecho (9 tareas) | Oficina: tareas `t-mis20-*` (00, 01, 02, 03, 04, 05, 06, 07, R1) + 2 reglas nuevas |
| 3 | Informe de cada agente | Ninguno ha podido trabajar (límite de uso). Lo he hecho yo directamente | Este documento |
| 4 | Stories de cocreación (2 de entrada) | Diseñadas y renderizadas | `stories/cocreacion1120/s1.jpg`, `s2.jpg` |
| 5 | 5 encuestas con hueco para la encuesta nativa | Diseñadas y renderizadas | `stories/cocreacion1120/p1–p5.jpg` + `LEEME.md` |
| 6 | Propuesta visual del Club Fundador | Diseñada | Lienzo «Club Fundador · propuesta» (8 pantallas) + `agencia/CLUB_FUNDADOR.md` |
| 7 | Conseguir la insignia (lista de espera, verificación manual, numeración 1–10 reservada) | **Implementado y probado en local, en PR #1.** Sin publicar | github.com/biellopez77-png/proteamapp/pull/1 |
| 8 | Imagen para compartir en Instagram | Diseñada; también dentro de la app | `stories/cocreacion1120/share.jpg`, `anuncio.jpg`, `club.jpg` |
| 9 | Carta de bienvenida con firma animada | **Implementada en el PR #1**. La firma es una recreación gráfica | PR #1 y lienzo (pantalla «Carta») |
| 10 | Onboarding (4 pasos) y «Tu primera semana» | Diseñado (propuesta). Solo usa funciones que ya existen | Lienzo. La implementación queda como encargo a R1 (PR aparte) |
| 11 | Guiones de los próximos vídeos | 4 guiones POV con hook, tiempos y gráfico de cada momento | `agencia/guiones/2026-11-20-pov-serie-camara-en-mano.md` |
| 12 | Gráficos y animaciones para los POV | 14 gráficos en PNG transparente + WebM con alfa (entrada animada) | `agencia/recursos/pov/` (fuentes en `tools/pov/`) |
| 13 | Mejoras de la web y la app | **Publicado:** entrada «Facturació» en el menú, para cancelar sin pedírselo a nadie. **Publicado:** antes de poner la tarjeta se explica la fecha de fin de la prueba, la renovación y cómo cancelar | Commit 32ecd1f, deploy 0439cbfb |
| 14 | Revisión de la suscripción | Hecha (resumen abajo) | — |

## Revisión de la suscripción, tarjeta y cancelación (lo que hay de verdad)
- **No se cobra durante la prueba:** el checkout de Stripe se crea con `trial_end` = fin real de la prueba (lista de espera: 28/02/2027; desde el 28/11, 1 mes). Antes de pagar, Stripe muestra el precio y la renovación.
- **Cancelación:** se hacía desde el portal de Stripe en «Facturación», pero **esa página no estaba enlazada en ningún menú**. Ahora está en el menú secundario. En el portal se ven las facturas, el método de pago y la cancelación; si se cancela durante la prueba, no se cobra.
- **Precio fundador:** **no existe en Stripe**. Hace falta que definas el importe y las condiciones antes de comunicarlo.

## Lo que necesita tu aprobación
1. **El límite de uso:** créditos extra, horario ligero o las dos cosas (panel de Álex).
2. **El PR #1 (Club Fundador):** revisarlo, aplicar la migración `20261120010000_club_fundador.sql` y fusionar. Sin esto no hay insignia en la web.
3. **El texto de la carta de bienvenida** (está en el PR y en el lienzo).
4. **Precio fundador y tickets:** sus condiciones, o decidir no comunicarlos hasta después del 28 (recomendado).
5. **Quién verifica las historias:** recomiendo que lo hagas tú, 5 minutos al día en `/admin` › Club Fundador.
6. **Publicar la Story `club.jpg`**, que nombra el «precio fundador»; si decides esperar, sale sin esa línea.
7. **Subir a mano** las 5 encuestas del miércoles 25.

## Lo que me tienes que dar
- **Las grabaciones POV (P1–P4).** Cómo grabar, en el documento de los guiones.
- **El prototipo de la insignia.** Cambia el color y la forma en las Stories, la app y los gráficos.
- **Tu firma real**, si la quieres en lugar de la recreación.
- **Quién lleva los números del 1 al 10.**

## Pendiente (prioridad 2 y 3, no bloquea el lanzamiento)
- Perfil general fuera del equipo y onboarding interactivo: encargados a R1 como PR, partiendo del lienzo.
- Sistema completo de tickets regalo: espera a tener las condiciones.
- Sección del Club Fundador en la web: diseñada en el lienzo, se implementa cuando apruebes el PR #1.
