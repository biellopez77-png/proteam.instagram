# Crítica v7 · v7-boot-room-anfield · «La Biblia del cuarto de las botas»
**Andrés (05), 24/11/2026.** Vídeo final (26,6 s): https://d2ol7oe51mr4n9.cloudfront.net/user_3M2z7lIyzIPYtjNHcxRWFNk6wi7/ce012177-15b6-4ec0-8433-e060bbaced1f.mp4 · mudo: tools/reel_v7/boot-room-anfield/video_mudo.mp4 · guion: agencia/fabrica-v7/guiones/v7-boot-room-anfield.md

## Nota: 87/100 → APROBADO (≥ 85)

| criterio | nota | por qué |
|---|---|---|
| Historia real y gancho | 17/20 | «El cuarto más famoso de Anfield guardaba botas» engancha en 3 s; giro claro (libros diarios → «la Biblia») e idea útil al final. Le falta un dato que sorprenda tanto como el de Bielsa. |
| Cada cosa que dice la voz se anima | 18/20 | Todo entra en su palabra: botas que caen (2,6 s), contador 3→6 y séptima silueta fuera (4,0–4,9), cajas (5,5), subrayado y ficha de Ronnie Moran (7,5–8,0), libro que se abre en «escribían» (8,6), «CADA DÍA» (9,5), ✓ por «entrenó» (11,5–12,0) y ✗ + vendaje en «lesionado» (13,0), gráfico que baja en «atascaba» (14,5–15,0), página antigua en «abrían el libro» (15,5), sello en «la Biblia» (17,5), línea HOY→MAÑANA (19,5–21,0). Pega: «Lo que» aparece aún con la cámara viajando (18,5 s). |
| Transiciones | 13/15 | Viajes suaves de ~0,9 s en las pausas, sin destellos ni cortes. El desenfoque de 6,5 s y 13,5 s pasa por encima de escenas anteriores (se leen «BOTAS.» y la ficha de Moran a medias); fundido al cierre con un instante de «Lo que escribes hoy» encima de «ProTeam» (≈21,0 s). |
| Sonido | 13/15 | −16,7 LUFS integrados, true peak −0,9 dBFS, LRA 2,2. Voz confiada y entera en faster-whisper (small y medium). En las pausas (3,25 · 6,0 · 13,5 · 18,0 s) el fondo queda en −28/−30 dB RMS frente a −14/−16 de la voz: unos 13 dB por debajo. Efectos sin picos sobre la voz. «del apuro» se transcribe «de la puro» en los dos modelos (homófono; se entiende por contexto). Algunas muestras decodificadas superan 0 dBFS (22,25 s, cola del outro): dejar 1 dB más de margen. |
| Verdad y fuentes | 14/15 | Todos los datos están en el guion con fuente. Comprobado hoy en Liverpool FC («Keegan on Bugsy's Boot Room bibles»): libros que guardaban Ronnie Moran y Joe Fagan, rutinas diarias, consultados «in times of strife», «Boot Room bible». El artículo de This Is Anfield (Dalglish «A4 books», Stevenson «about six people») no se pudo abrir desde aquí; su existencia sí aparece en búsqueda y lo apoyan Wikipedia y el club. Pequeña incoherencia del guion: tabla de escenas dice «abril 1963», la ficha y la licencia dicen 1964 (en pantalla, 1964: correcto). |
| Estética | 12/15 | Paleta y tipografías del formato; ultravioleta solo en «la Biblia» y su sello. Fotos de Commons con licencia (estatuas y foto de equipo de 1964); nada sugiere apoyo a ProTeam. Pie de créditos (19,5–21 s) ilegible en móvil (≈5 px a 270 px de ancho). Texto de la placa de Paisley ilegible (decorativo). |

Bloqueantes: ninguno (sin nombre de Biel, sin fechas ni precios, sin cifras de apuntados, fotos con licencia, sin texto cortado en reposo, música real de Epidemic).

## Correcciones (para la próxima versión; no bloquean)
1. 18,4–18,6 s: retrasar la entrada de «Lo que» hasta que la cámara llegue.
2. 21,0 s: que la frase final se vaya antes de que aparezca «ProTeam» (fundido sin solape).
3. Pie de créditos a ≥ 22 px en 1080 o dejarlo solo en el caption.
4. Mezcla: limitar a −1,5 dBTP para evitar muestras >0 dBFS tras la decodificación AAC.
5. Guion: unificar 1963/1964 en la tabla de escenas.

Programado: `pub_v3.py approve v7-boot-room-anfield 2026-11-27T18:00:00+01:00` (25/11 v7-bielsa y 26/11 v7-peor-verano-2003 ocupan las 18:00).
