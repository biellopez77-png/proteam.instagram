# Reels ProTeam: estilo «unrespiro deportivo»

Referencia: Reel 1 «No eres diferente a ellos» (v8, 30 s, 9:16). Código en `tools/reel1/` (`reel4.html`, `times.js`, `mktimes.py`, `sfx4.py`).
Aprobado por Biel el 14/11/2026 («está perfecto»), con el último ajuste de SISTEMA y la lista de espera.

## Lo que define el estilo (no tocar)

1. **Estructura en 5 bloques** (25–32 s):
   - Gancho (0–2,5 s): frase a máquina sobre negro + collage rápido de referentes reconocibles.
   - Espejo (2,5–7 s): «tú tienes lo mismo que ellos»: franjas con subrayado azul y un gráfico vivo (reloj 24 h).
   - Giro (7–11 s): la diferencia no está en X sino en Y; fondo blanco plano, «?» azul, palabra serif itálica.
   - Contraste (11–19 s): ellos (clips reales de entrenadores) frente a tú (motion graphics del caos que se acelera hasta negro seco).
   - Solución + CTA (19–30 s): palabra clave con impacto (SISTEMA), directo a la lista de espera en la UI oscura de la web, cuenta atrás que cae a 0, fecha y oferta.
2. **Bucle:** empieza y acaba en negro plano, sin logo; el final enlaza con el gancho.
3. **Fondos solo planos:** negro `#000` / tinta `#0d0f14` / blanco `#f5f5f3`. Nada de luces, degradados de color ni brillos.
4. **Tipografía:** Manrope (500/700/800) e Instrument Serif itálica para la palabra emocional en azul `#2f6bff`. Nada más.
5. **Solo palabras destacadas.** Nunca la frase entera. Entrada letra a letra con desenfoque (≈0,3 s), escala lenta +4 %.
6. **Cortes secos.** Sin barridos de luz ni transiciones de plantilla. Las fotos entran con un empujón y luego se mueven despacio (nunca quietas).
7. **Fotos de personas:** referentes reconocibles (entrenadores top) que aporta Biel; recortadas sin cortar cabezas. Objetos y herramientas: motion graphics de la marca, no fotos de stock ni IA.
8. **Voz:** ElevenLabs, voz «Mateo» (`Rie0luvrYhyKLba1lK3c`), eleven_v4. Velocidad ×1,08 en el cuerpo y ×1,0 en el CTA. Nunca quitar silencios automáticamente ni cortar dentro de una palabra: solo insertar pausas sobre silencios reales.
9. **Sonido:** sin música ni campanas. Clics, papel, barridos suaves, golpes graves en las palabras clave; efectos al −10 dB respecto a la voz.
10. **Marcas fuera de márgenes:** sin logos, sin rótulos en bordes.

## Flujo de producción

1. Guion de Biel → locución en ElevenLabs (2 tomas) → elegir.
2. Transcribir con faster-whisper y **ajustar cada palabra al arranque real de la voz** (`mktimes.py`, función `snap`).
3. `times.js` manda todo el montaje: ninguna animación con tiempos fijos a mano.
4. Fotogramas de control antes del render completo (hoja de contacto).
5. Render 30 fps → mezcla (`loudnorm` −15 LUFS en la voz, efectos ×0,32, `alimiter`).
6. Antes de enviar: nivel de audio segundo a segundo (que la voz llegue al final) y búsqueda de fotogramas congelados.

## Variantes del mismo reel

- **Otro gancho, mismo cuerpo:** «Todos los entrenadores top tienen algo en común», «Otra temporada igual…», «Mientras todos miran a los ganadores…».
- **Otra métrica en el espejo:** en vez de 24 h, «90 minutos», «38 jornadas», «3 entrenos por semana».
- **Otro caos:** convocatorias de última hora, lesiones sin registrar, padres preguntando… cada uno con su motion graphic (lista que se tacha, calendario que se llena de avisos, notificaciones que se apilan).
- **Otro deporte en los clips:** baloncesto / balonmano / fútbol según la audiencia del anuncio.

## Evoluciones para otros reels (misma estética, otro tema)

| Reel | Idea | Bloque «ellos» | Bloque «tú» (motion graphic) | Palabra de impacto |
|---|---|---|---|---|
| El lunes | Lo que pasa después del partido | Ruedas de prensa, análisis de vídeo | Notas del partido que se pierden, móvil con 40 mensajes | MEMORIA |
| La convocatoria | 23:47 del viernes, aún sin lista | Pizarras, charlas de vestuario | Lista que se reescribe, chats que vibran | CONTROL |
| Datos | «Lo que no se mide, no mejora» | Staff con tablets, GPS | Excel que se rompe, gráfica a mano | DATOS |
| Temporada | 9 meses en 25 s | Celebraciones, títulos | Calendario que se llena y se colapsa | PLAN |
| El club | Del entrenador al club entero | Clubes grandes, cantera | Carpetas de cada categoría | UNA APP |
| Cuenta atrás | Pieza corta de 12 s solo con la UI | — | Cuenta atrás, registro, «Estás dentro» | 27.11 |

Reglas para cualquier evolución: un solo mensaje por reel, una sola palabra de impacto, 4–6 palabras destacadas en todo el vídeo, CTA siempre a la lista de espera con la fecha y «3 meses gratis» (oferta vigente hasta el 27/11 23:59).

## Actualización 14/11 (Biel): DIRECCION_CREATIVA.md manda
- Cada Reel tiene su propia propuesta visual: la estructura del Reel 1 es una opción, no una plantilla.
- Por cada guion se entrega primero un documento de producción (concepto, guion técnico por bloques, lista de recursos que busca Biel, notas de edición) y después el vídeo.
- Textos: frases o conceptos completos integrados en la composición (nunca subtítulos palabra a palabra).
- Se permiten efectos de luz suaves y zooms si tienen sentido narrativo.
- Sin música en el montaje (voz y efectos). La música, si la hay, la pone Biel desde la biblioteca de Instagram.
- La URL no va en pantalla: «enlace en la bio» en la descripción.
