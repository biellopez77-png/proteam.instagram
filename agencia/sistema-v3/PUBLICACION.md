# Publicación v3 · Instagram y TikTok (Biel, 23/11)

**Cuentas:** Instagram **@proteam.oficial** (Windsor, cuenta 17841477624464717) y TikTok **proteam.oficial**.
**Qué va a cada sitio:** todos los vídeos a TikTok y a Instagram (Reels); los carruseles, a Instagram y algunos a TikTok (modo foto) cuando se valore; las Stories, a Instagram.

## Interruptor
`publicar/ESTADO.json` → `"publicar": false`. **No se publica nada hasta que Biel dé la orden** (después de la estrategia de relanzamiento). Solo Biel lo enciende.

## La cola: `publicar/cola.json` (`python3 tools/pub_v3.py`)
1. Cuando Marta o Clara terminan una pieza, la añaden: `pub_v3.py add <id> reel|carrusel|story <caption.txt> <archivos>`. Queda en «revisión».
2. Biel la aprueba en el feed simulado; el turno la pasa a «aprobada» con `approve` (fecha en el siguiente hueco libre).
3. El turno de publicación (cada hora, hoy apagado) hace `due`: si el interruptor está encendido y toca, publica UNA pieza en Instagram con Windsor (`execute_action`: create_video_post, create_carousel_post o create_story; URL de jsDelivr y, si falla, la de raw.githubusercontent) y la marca con `done`/`fail`.
4. TikTok: Windsor **no** puede publicar en TikTok (tiktok_organic solo lee). La vía es Higgsfield (`tiktok_*`), que pide que Biel conecte la cuenta y revise cada publicación en su formulario. Mientras tanto, `pub_v3.py tiktok` deja un kit por vídeo en `publicar/tiktok/<id>/` (vídeo + texto) para subirlo a mano o desde el formulario.

## Formatos
- Reel: MP4 9:16, 3 s-15 min. Portada: el primer fotograma (que en v3 es el gancho).
- Carrusel: JPEG (no PNG), de 2 a 10 láminas, 4:5 (1080×1350). **Ojo:** los carruseles de Clara son de 1080×1440 (3:4), que Instagram no acepta por la API: hay que exportarlos también a 1080×1350.
- Story: JPEG o MP4 de 3-60 s, 9:16.
- Texto: máximo 2.200 caracteres; la primera línea promete algo y al final, una pregunta fácil; créditos de las fotos si los hay.
