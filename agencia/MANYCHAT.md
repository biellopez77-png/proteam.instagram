# ManyChat · flujo «Semana» (privados de Instagram)

Desde el 17/11, la conversación para preparar la semana va **siempre por privado**. Los privados los envía ManyChat (Claude no puede mandar mensajes privados de Instagram). Lucía (07) contesta en público y avisa cuando ManyChat ya ha escrito.

## Puesta en marcha (Biel, una sola vez)
1. Crea cuenta en manychat.com con el Instagram @app.proteam (plan gratis vale para empezar) y acepta los permisos de mensajes.
2. Automation → New → plantilla **«Auto-DM links from comments»**.
3. Disparador: **comentario en cualquier publicación o Reel** que contenga alguna de estas palabras: `semana, SEMANA, sub, alevín, alevin, infantil, cadete, juvenil, benjamín, días, entreno, entrenamos`. Activa **«responder también en público»** con: «¡Te acabo de escribir por privado, mira tus mensajes! 💬».
4. Mensajes por privado (cada uno es un bloque; los de pregunta, con «User Input» de texto libre y espera a la respuesta):

> **1.** ¡Hola! 👋 Soy Lucía, de ProTeam. Me encanta que quieras tu semana. Para montártela bien necesito conocer un poco a tu equipo, son 4 preguntas rápidas, ¿vale?
>
> **2.** ¿Qué deporte entrenas y en qué categoría? *(guardar en el campo `deporte_categoria`)*
>
> **3.** ¡Buena edad para crecer mucho! ¿Cuántos días entrenáis a la semana y cuánto dura cada sesión? *(campo `dias`)*
>
> **4.** Perfecto. ¿Qué día jugáis y cómo llega ahora el equipo: bien, cansados, con bajas? *(campo `partido`)*
>
> **5.** Última: ¿qué es lo que más te preocupa ahora mismo de tu equipo? *(campo `preocupacion`)*
>
> **6.** Con esto ya te la puedo montar bien 💪 Una cosa: estamos en plena cuenta atrás. Si te apuntas a la lista de espera antes del 27 de noviembre, el 28 empiezas con **3 meses gratis** de ProTeam y **asesoramiento 1 a 1 gratis** durante esos 3 meses, y te dejamos tu semana montada dentro de la app con tus días y tu partido.
> Botón: **«Apuntarme»** → https://pro-team.app/?auth=register
>
> **7.** *(si no pulsa el botón en 24 h)* ¿Te ha surgido alguna duda? Si prefieres, te paso la semana por aquí igualmente, dime y te la escribo.

5. Activa la automatización. Pruébala comentando «semana» desde otra cuenta.
6. Avisa a Laura en la oficina («ManyChat activado»): pondrá `meta/office.manychat = true` y Lucía empezará a contestar en público remitiendo al privado.

## Después del 27/11
Cambia el mensaje 6 por: «Si quieres, pruébala gratis en https://pro-team.app/?auth=register y te dejamos la semana montada dentro».

## Personas que comentaron antes de activar ManyChat
Lucía las guarda en `meta/comments.waiting`. ManyChat solo escribe a comentarios nuevos: a esas personas, escríbeles tú por privado desde la app de Instagram con el mensaje 1 (o pídeles que comenten «semana» de nuevo).
