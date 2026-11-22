# Lista de espera con 0 altas: dónde se pierde la gente (Samuel, 06 · lunes 16/11/2026)

Datos leídos hoy entre las **12:08 y las 12:12 (hora de Madrid)**. Todo en modo lectura: no he rellenado ningún formulario ni he creado filas de prueba.

## Resumen en cuatro frases
1. **El enlace de la bio está bien**: lleva a pro-team.app, que es la página de la lista de espera.
2. **Estábamos mirando el sitio equivocado.** Apuntarse a la lista **no guarda nada en la tabla `leads`**: apuntarse es **crear una cuenta y después crear un equipo**. Contado bien, el resultado sigue siendo **0 apuntados**, pero ya no hay sospecha de «formulario roto» por ese lado.
3. **La gente se pierde antes de llegar a la web.** Desde que la lista de espera funciona como ahora (viernes 13/11), **nadie ha llegado a la web desde Instagram**. El mensaje de la lista solo lo han visto unas 170 cuentas.
4. El dato de «0 toques en el enlace» de esta mañana **no vale**: la cifra que da Windsor no cuenta los toques en el enlace de la web. Hay que mirarlo en la app de Instagram.

## Qué he comprobado y cómo
| qué | fuente | hora (Madrid) |
|---|---|---|
| Enlace y texto de la bio | Windsor.ai, datos del perfil (cuenta 17841445998297098), leídos al momento | 12:08 |
| Alcance diario y publicaciones del 9 al 16/11 | Windsor.ai | 12:08–12:11 |
| Qué muestra la página pública | Lectura directa de https://pro-team.app/ y captura del proyecto en Lovable | 12:11 |
| Visitas a la web día a día y origen (2–16/11) | Analítica de Lovable, una consulta por día | 12:09–12:10 |
| Tabla `leads`, cuentas, equipos y permisos | Base de datos de Lovable, solo consultas de lectura | 12:08–12:11 |
| Cómo funciona el alta | Código del proyecto de Lovable (página de inicio, formulario de cuenta, creación de equipo, pantalla «ya estás en la lista», reglas de la base de datos) | 12:08–12:11 |

## 1. Qué enlace hay en la bio y a dónde lleva
- **Enlace de la bio: `https://pro-team.app/`** (hecho, Windsor).
- Texto de la bio: «📺 Despierta entrenador, no estamos en 1995. Ya es hora de entrenar a tu manera. • 📢 ¡Cuenta atrás ha empezado! Entra al link👇🏼».
- **Sí lleva a la página de la lista de espera** (hecho, comprobado en la web pública): titular «Blackout Friday», texto «Apúntate a la lista de espera antes del 27 de noviembre y consigue 3 meses gratis», cuenta atrás y botón azul «Apúntate a la lista de espera».
- **Cuántas veces se ha tocado ese enlace: no se puede saber desde aquí.** El dato que usé esta mañana (`profile_links_taps`) solo cuenta los botones de dirección, llamada, correo y mensaje; el dato antiguo de toques en la web ya no lo da Instagram (sale vacío). Tampoco salen las visitas al perfil. **Corrijo el informe de esta mañana: «0 toques en el enlace» no estaba medido.**

## 2. Visitas a la página por día y de dónde vienen
Analítica de la web (Lovable). «Visitantes» son de toda la web, incluida la gente que ya usa la app por dentro; «veces que se abrió la portada» es la página de la lista de espera.

| día | visitantes | veces que se abrió la portada | desde Instagram | resto |
|---|---:|---:|---:|---|
| lun 2/11 | 6 | 1 | 0 | 6 directo |
| mar 3/11 | 10 | 8 | **4** | 6 directo |
| mié 4/11 | 18 | 12 | **4** | 12 directo, 2 Google |
| jue 5/11 | 4 | 3 | **1** | 3 directo |
| vie 6/11 | 6 | 4 | 0 | 5 directo, 1 Google |
| sáb 7/11 | 5 | 1 | **1** | 3 directo, 1 Gmail |
| dom 8/11 | 7 | 4 | 0 | 7 directo |
| lun 9/11 | 8 | 4 | 0 | 6 directo, 2 Google |
| mar 10/11 | 6 | 6 | **1** | 4 directo, 1 Gmail |
| mié 11/11 | 6 | 6 | 0 | 5 directo, 1 Facebook |
| jue 12/11 | 4 | 4 | 0 | 1 directo, 1 Google, 2 Facebook |
| **vie 13/11** | 13 | 6 | **0** | 13 directo |
| **sáb 14/11** | 16 | 8 | **0** | 16 directo |
| **dom 15/11** (Reel u01) | 7 | 5 | **0** | 7 directo |
| **lun 16/11** (hasta las 12:10) | 5 | 4 | **0** | 5 directo |
| **Total** | **121** | **76** | **11** | 99 directo, 6 Google, 3 Facebook, 2 Gmail |

Lo que se ve (hechos):
- En 15 días, **11 visitantes desde Instagram**. El último, el martes 10/11.
- **Desde el viernes 13/11, que es cuando la lista de espera funciona como ahora: 0 visitantes desde Instagram** (41 visitantes en total, todos «directo»).
- Del 2 al 11/11 la cuenta llegaba a entre 1.400 y 2.600 cuentas casi cada día (suma de alcances diarios: 12.902) y eso dio 11 visitas a la web: **menos de 1 visita por cada 1.000 cuentas alcanzadas**. Del 12 al 14/11 el alcance fue 24, 7 y 10; el 15/11, 160.
- **El mensaje de la lista de espera solo ha salido dos veces**: la imagen del sábado 14/11 (10 cuentas alcanzadas) y el Reel u01 del domingo 15/11 (159). En total, unas **170 cuentas**. Con la proporción de arriba, lo esperable de 170 cuentas son 0 visitas. (Esto último es una interpretación mía, no un dato.)

Límites de este dato:
- «Directo» mezcla a quien escribe la dirección, a quien ya usa la app y, seguramente, al propio equipo. No se puede separar.
- La analítica no cruza página con origen, y **no registra cuánta gente pulsa el botón «Apúntate»** (el formulario se abre encima de la portada, no es una página aparte).

## 3. ¿El formulario guarda?
**La lista de espera no es un formulario que guarde en `leads`.** Así funciona, leído en el código y en la web pública:

1. Enlace de la bio → portada con la cuenta atrás.
2. Botón «Apúntate a la lista de espera» → se abre «Crear cuenta»: nombre, apellidos, correo y contraseña (mínimo 8 caracteres).
3. Llega un correo para confirmar la cuenta. Hay que abrirlo.
4. Volver e iniciar sesión.
5. «Crear mi primer equipo»: deporte (en fútbol, además, modalidad), nombre del equipo, categoría y temporada.
6. Solo entonces aparece «Ya estás en la lista de espera» con la cuenta atrás hasta el 28. La web avisa de que ese día habrá que poner la tarjeta (no se cobra hasta pasados los 3 meses).

La propia web lo dice: «Crea tu cuenta y tu equipo. Entras en la lista de espera».

**La tabla `leads` es de otras dos páginas**: la de la plantilla de planificación y la de «Prueba ProTeam» (`/prueba`, la del cartel). Sus 2 filas (5/11 «plantilla» y 10/11 «prueba», con origen «cartel») son de ahí. Sus permisos están bien: cualquiera puede enviar esos dos formularios y solo un administrador puede leerlos. No veo ningún error en esa parte, pero **no tiene nada que ver con la lista de espera**.

**Dónde hay que contar los apuntados de verdad** (base de datos, 12:09):
| qué | cifra |
|---|---:|
| Equipos apuntados a la lista de espera (accesos marcados «Llista d'espera Blackout Friday») | **0** |
| Cuentas creadas desde que la lista funciona así (vie 13/11, 14:08) | **0** |
| Última cuenta creada | mar 10/11 — nunca confirmó el correo ni entró |
| Último equipo creado | mié 4/11 |
| Cuentas creadas en noviembre | 4: una creó equipo, dos confirmaron pero no crearon equipo, una no confirmó |
| Total histórico | 34 cuentas, 8 clubes |

Conclusión del punto 3:
- **Hecho:** 0 apuntados, contados en el sitio correcto.
- **Hecho:** no hay ningún intento a medias desde el 13/11 (ni una cuenta nueva). No es que la gente empiece y el sistema falle: **nadie ha empezado**.
- **Hecho:** en el código no veo ningún error evidente. La regla de la base de datos que da los 3 meses de la lista de espera es la versión vigente y los textos del alta están traducidos al castellano.
- **No comprobado (solo se puede probar a mano):** que el correo de confirmación llega de verdad (y no a la carpeta de spam) y que todo el recorrido funciona en un móvil abriendo el enlace desde Instagram.
- **Interpretación:** el recorrido es largo (cuenta + correo + volver + crear equipo, y aviso de tarjeta). De las 4 cuentas de noviembre, solo 1 llegó a crear equipo. Son muy pocos casos y de antes del cambio del 13/11: es una señal, no una prueba.

Dos detalles más que he visto:
- **La web dice «antes del 27 de noviembre»; el contenido dice «antes del 28 de noviembre» y «HASTA EL 28 NOV».** Es el mismo plazo (cierra el 27 a las 23:59), pero el entrenador ve dos fechas distintas.
- La descripción del Reel u01 lleva escrita la dirección «pro-team.app», que en Instagram no se puede tocar.

## 4. Recomendación para los CTA de esta semana
El problema, con los datos de hoy, no está en el formulario: está en que **casi nadie ve la oferta y quien la ve no llega a la web**. Por eso:

1. **Stories con enlace que se toca, todos los días** (Clara). Es el único sitio, además de la bio, donde se puede poner un enlace pulsable. Pegatina de enlace con el texto «Apúntate» que lleve a `https://pro-team.app/?auth=register` (comprobado en el código: esa dirección abre directamente «Crear cuenta»). No se escribe la dirección en pantalla. Encaja con lo que pidió Biel: la Story enseña algo de la app o de la marca y el enlace es el cierre, no un aviso de Reel.
2. **Un solo CTA por pieza y dicho igual que en la web** (Dani, Marta). Propuesta de frase: «Apúntate antes del 28 de noviembre: creas tu cuenta y tu equipo, y el 28 entras con 3 meses gratis. Enlace en la bio». Decir qué va a pasar al tocar quita sorpresas. Sin dirección escrita en la descripción.
3. **La oferta, antes.** En u01 llegó al final y la media de visionado fue de 6 segundos: no la vio casi nadie. En pantalla («HASTA EL 28 NOV · 3 MESES GRATIS») desde la mitad del Reel, no solo en el cierre.
4. **Prueba de esta semana (hipótesis, una sola variable):** en la mitad de los Reels, cambiar «enlace en la bio» por **«Comenta LISTA y te mando el enlace»**, y responder a mano por mensaje privado con el enlace (ahí sí se puede tocar). Necesita que alguien conteste los comentarios el mismo día; si no hay quien lo haga, no se lanza. Se compara con los Reels de «enlace en la bio» por dos cifras: visitantes a la web desde Instagram y cuentas nuevas por día.
5. **Cambiar cómo medimos**: cada día miro (a) visitantes a la web desde Instagram, (b) cuentas nuevas y (c) equipos apuntados a la lista. Dejo de usar `leads` para esto. `agencia/MARCA.md` y `agencia/agentes/06_PERFORMANCE_LAB.md` dicen que las altas están en `public.leads`: hay que corregirlo (no lo he tocado, solo dejo este informe).

Decisiones que son de Biel (no las tomo yo):
- **Unificar la fecha**: o la web pasa a «antes del 28», o el contenido pasa a «hasta el 27». Cambiar la web requiere Lovable.
- **Acortar el alta.** Existe ya una página con un formulario corto de 5 campos y sin correo de confirmación (`/prueba`, la del cartel), que sí guarda en `leads`. Usar algo así para la lista de espera sería un cambio en la web (Lovable) y cambiaría lo que significa «estar apuntado». Lo dejo como opción, no como recomendación, porque todavía no hay datos de que la gente abandone en el alta: no ha llegado nadie.

## Qué queda sin poder comprobar y quién debe hacerlo
| qué | por qué no se puede desde aquí | quién |
|---|---|---|
| Toques reales en el enlace de la bio y visitas al perfil | Instagram ya no da ese dato a Windsor | **Biel**, en la app de Instagram: Panel profesional → Estadísticas → actividad del perfil («toques en el enlace externo»), últimos 14 días |
| Que el alta funciona de principio a fin | Hay que hacerla a mano | **Biel**, desde el móvil y tocando el enlace de la bio dentro de Instagram: crear cuenta con un correo real que no haya usado, comprobar que llega el correo (mirar spam) y cuánto tarda, confirmar, entrar, crear equipo y ver la pantalla «Ya estás en la lista de espera». Que me diga el correo usado para descontarlo de las cifras |
| Cuánta gente pulsa «Apúntate» y no termina | La analítica de la web no lo registra | Nadie, hoy. Haría falta un cambio en la web (Lovable) |
| Cuánto del tráfico «directo» es del propio equipo | La analítica no lo separa | Nadie, hoy |
| Datos de u02, u03 y c08 | A las 12:11 todavía no aparecían publicados en Windsor | Samuel, en el informe diario de esta noche |
