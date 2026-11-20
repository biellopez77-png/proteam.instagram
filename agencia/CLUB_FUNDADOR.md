# Club Fundador (Biel, 20/11)

**Qué es.** No es un descuento ni un regalo por apuntarse a la lista: es formar parte de los comienzos de ProTeam. Debe transmitir reconocimiento, pertenencia, participación y cercanía.

## Ventajas y su estado
| # | Ventaja | Estado | Qué se puede decir en público |
|---|---|---|---|
| 1 | Insignia verificada y numerada | Implementada en el PR #1 de proteamapp. Falta aplicar la migración y fusionar (necesita a Biel) | «Insignia de fundador con tu número» |
| 2 | 3 meses gratis | Activo para la lista de espera hasta el 27/11 23:59 | Sí, tal cual |
| 3 | Precio fundador congelado | **Pendiente:** importe, duración y condiciones sin definir. No existe en Stripe | Solo «precio fundador», sin importe y sin decir que el precio general subirá. Mejor no publicarlo hasta tener condiciones |
| 4 | Soporte individual de tú a tú | Activo: Lucía por Gmail durante los 3 meses | «Una persona del equipo te acompaña» |
| 5 | Participación y votaciones exclusivas | Diseñado. Primera tanda: las 5 encuestas del miércoles 25 (públicas) | «Votas en lo que construimos». Nunca prometer que cada voto cambia la app |
| 6 | 3 tickets regalo para amigos | **Pendiente:** recompensas y condiciones | «3 invitaciones para tus amigos. Pronto, más». Sin detalles |
| 7 | Carta de bienvenida personalizada | Implementada en el PR #1 (nombre, número y firma animada de Biel) | Puede aparecer en el Reel P4 |

## Numeración
- Los números del 1 al 10 están reservados. El 1 es de Biel; los demás, para quien él diga. Solo se asignan a mano desde `/admin` → Club Fundador.
- Desde el 11, «Siguiente número» asigna el primero libre, con bloqueo y `UNIQUE`: no puede haber duplicados.
- **Nadie tiene número todavía.** Biel dice cuándo empezar y a quién van los del 1 al 10.

## Cómo se consigue la insignia (verificación)
1. En la pantalla de la lista de espera: «Consigue tu insignia del Club Fundador».
2. Se abre una ventana con la explicación, los 3 pasos, la imagen para compartir (`stories/cocreacion1120/share.jpg`; en la app es `public/club-fundador/compartir.jpg`), los botones de compartir y descargar, y el recordatorio de mencionar a @app.proteam.
3. El usuario escribe su @ y pulsa «Ya la he compartido» → solicitud «en revisión».
4. **La verificación es manual:** un admin abre su Instagram desde `/admin`, comprueba la historia con la mención y pulsa Verificar (o Rechazar). Pulsar «Compartir» nunca verifica nada.
5. Al verificarse se abre una vez la carta de bienvenida; después puede volver a verla desde el mismo bloque.

**Quién verifica:** Biel, o la persona que él designe. Lucía no puede ver las menciones en historias desde Windsor (la API no da menciones de historias), así que la comprobación se hace a mano.

## Comunicación
- **Stories** (`stories/cocreacion1120/`): `anuncio.jpg` («¡Ya estás dentro…!» + insignia) y `club.jpg` (las 6 ventajas; necesita el OK de Biel).
- **Reel** P4 «Te cuento con los dedos» (POV): `agencia/guiones/2026-11-20-pov-serie-camara-en-mano.md`.
- **Web:** propuesta de sección en el lienzo «Club Fundador · propuesta» (https://claude.ai/artifact/XY22WySA7SwwAyf3ztpkuF). No está implementada.
- **Reglas:** nada de plazas limitadas ni escasez inventada; nunca el importe del precio fundador; nunca detalles de los tickets hasta que estén aprobados.
