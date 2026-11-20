# Las tres cifras del relanzamiento · propuesta de Samuel (06) · 20/11 20:00

Encargo del plan de relanzamiento (t-relz-06), para la reunión de métricas del martes 24/11. Todo sale de la base de datos de la app y de las visitas de la web (Lovable), leído hoy a las 19:57 con consultas de solo lectura. Sin Instagram y sin estimaciones. No se ha leído ningún correo ni nombre de persona: solo recuentos.

## Propuesta: tres cifras, una por paso del camino

| # | Cifra | Qué responde | Hoy (20/11, 19:57) |
|---|---|---|---|
| 1 | **Equipos nuevos en la lista** (hoy y total) | ¿Sigue entrando gente sin Instagram? | 1 hoy · **24 en total** (23 sin nuestro equipo de prueba) |
| 2 | **Cuentas que acaban creando su equipo** | ¿Se nos queda gente a medias en el registro? | **24 de 33** cuentas creadas desde el 17/11 tienen equipo. 9 se quedaron sin crearlo |
| 3 | **Equipos que hacen algo en la app** (jugadores añadidos, una semana planificada, una sesión o un partido) | ¿La usan o solo se apuntan? | **0 de 23** |

### 1. Equipos nuevos en la lista
| Día | Cuentas nuevas | Equipos nuevos | Visitantes de la web |
|---|---|---|---|
| Mar 17/11 | 23 | 15 | 147 |
| Mié 18/11 | 7 | 6 | 68 |
| Jue 19/11 | 2 | 2 | 38 |
| Vie 20/11 (hasta las 19:57) | 1 | 1 | 17 |

- Los 24 equipos son de balonmano. Ninguno de fútbol ni de baloncesto.
- Sin altas desde las 4:32 de hoy.
- La web cae con la cuenta: del 14 al 20/11 hubo 301 visitantes y 133 llegaron desde Instagram. Hoy, 17.

### 2. Cuentas que acaban creando su equipo
- De las 33 cuentas creadas desde el 17/11, 24 crearon equipo (73 %). Las 9 que no lo hicieron son 8 del martes 17 y 1 del miércoles 18.
- Es la cifra más fácil de mejorar sin canal: esas 9 personas ya dieron su correo. Sirve para el email de Lucía (el plan ya pide separar «con equipo» y «sin equipo»).
- Esto cuadra con la auditoría: 33 cuentas y 24 equipos.

### 3. Equipos que hacen algo en la app
- Hoy es **0 de 23**: ningún equipo de la lista tiene jugadores añadidos, semana, calendario, sesión, plantilla ni partido. Solo está la persona que lo creó.
- No es una mala noticia todavía: la lista espera al 28/11. Pero es la cifra que dirá, desde el sábado 28, si la apertura funciona.
- Propuesta de definición para acordar con R1: un equipo está **activado** cuando en sus primeros 7 días tiene al menos 5 jugadores y una semana planificada. Hasta que se acuerde, se mira «hace algo» (cualquiera de las acciones de arriba).

## Lo que no se puede medir hoy
- **De dónde viene cada alta.** La base de datos no guarda el origen. Con un parámetro en el enlace (email, web, clubes) se sabría. Es un cambio pequeño para R1; propuesto, no hecho.
- **Aperturas y clics del email** a la lista: dependerá de cómo lo envíe Lucía.
- **Instagram:** nada mientras la cuenta siga suspendida.

## Para R1 (panel)
Las tres cifras salen de `organizations`, `organization_billing` (`trial_started_at` = 28/11 y `card_required`), `profiles` (`has_account`), `teams` y `team_members`, más `microcycles`, `calendar_events`, `court_sessions`, `training_sessions`, `schedule_templates` y `matches` para saber si un equipo ha hecho algo. Samuel las lee a mano cada día hasta que el panel exista.

## Qué tiene que decidir Biel el martes 24
1. Si estas son las tres cifras (o cuál cambia).
2. La definición de «equipo activado» (propuesta: 5 jugadores y una semana planificada en 7 días).
3. Si R1 añade el origen al enlace de registro.
