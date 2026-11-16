# u30 · Documento de producción (Marta, 02) · «Sábado: presión alta. Martes: rondo.»

- **Guion:** `agencia/guiones/2026-11-16-u30-f11-por-dentro-presion-alta.md` (Dani · Andrés 77) · **Encargo:** t-20261116-crec-02 («ProTeam por dentro», 2 de 3: fútbol).
- **Sale:** mié 18/11 · 9:30 (ver «Hueco» abajo) · **Duración:** 24,3 s · **Montaje:** `tools/reel30/` (parte de reel29 → reel2).
- **Arranque:** 1 ✔ (Bernabéu a sangre con «SÁBADO: PRESIÓN ALTA» en el fotograma 0) · 2 ✔ (voz en 0,13 s; abre con la escena, no con una pérdida — es «por dentro», no variación de u04) · 3 ✔ (24,3 s) · 4 ✔ (ficha «Una frase arriba» 12,8–16,6 s, 3,8 s) · 5 ✔ (sin frase de marca). Experimento abierto de Samuel: ninguno nuevo; cambia respecto a u04 el tipo de pieza (función real paso a paso).

## 1. Concepto audiovisual
**«La frase de arriba».** Una semana que no casa (sábado presión, martes rondo, jueves físico) se tacha; la app enseña la misma semana con su objetivo escrito arriba; la ficha de papel lo convierte en plantilla para el domingo y el martes se enciende en azul con la presión.

## 2. Justificación y diferencia con los cinco anteriores (u29, u28, u27, u09, u08)
Nuevo: días tachados sobre foto (texto como escena, no marcador), zoom en tres pasos sobre una sola captura real (ruta → tarjeta → frase subrayada palabra a palabra), plantilla de semana en papel con una fila que se enciende, cierre con reto sobre Simeone. Cambia ≥ 4 ejes respecto a u29: deporte, función (Planificación, no Partido en directo), apertura (escena de días, no marcador), recurso visual (subrayado y plantilla) y cierre (reto en foto distinta). El bloque CTA «Comenta…» es el del encargo (mismo que u29) por coherencia de serie.

## 3. Guion técnico (marcas reales de `tools/reel30/times.js`)
| tramo | voz | imagen y acción | texto en pantalla | SFX / música |
|---|---|---|---|---|
| 0,00–6,10 | Sábado: presión alta. Martes: rondo. Jueves: físico. ¿Cuándo se entrena la presión? | Calentamiento del Real Madrid en el Bernabéu a sangre; reencuadres en 1,7 (balón), 3,1 (jugador) y 4,4 s (plano cerrado) | EL PARTIDO DEL SÁBADO · Sábado: **PRESIÓN ALTA** · Martes: *rondo.* · Jueves: *físico.* (todo desde el fotograma 0); 4,6 s tachado azul de *rondo* y *físico* · **¿Y la presión?** | golpe grave en 0, barridos en cada reencuadre, dos clics en los tachados; beat desde el inicio |
| 6,10–12,8 | En la app de ProTeam, la semana lleva una frase arriba: preparar el partido del sábado, presión alta y salida por fuera. | Móvil con la captura real de Planificación (Semana 8): sube y se acerca a la ruta (recuadro azul), se abre a la tarjeta (recuadro en la frase) y se acerca a la frase, que se subraya mientras Mateo la lee | PLANIFICACIÓN · CAPTURA REAL · **1 Semana 8** → **2 Una frase arriba** → *presión alta y salida por fuera* | barrido de entrada, clics en los recuadros |
| 12,8–16,6 | Guárdatelo: si la frase está arriba, [silencio 0,3 s] el martes la entrenas. | Papel: plantilla de semana (objetivo del sábado arriba, LUN–VIE); el recuadro del objetivo se activa; en «el martes» la fila MAR se pone azul con «→ presión tras pérdida» y una línea la une al objetivo | GUÁRDALO · PARA EL DOMINGO · **Una frase arriba.** · *El martes, a entrenarla.* | la música se corta (13,3–15,1 de la pista) y **vuelve en «el martes»**; golpe grave ahí |
| 16,6–20,7 | Comenta tu deporte, tu categoría y tus días, y te preparo la primera semana. | Vuelve la foto del principio, oscurecida (bucle) | **Comenta** · chips tu deporte / tu categoría / tus días · *y te preparo la primera semana.* · LISTA DE ESPERA · HASTA EL 27 NOV · *3 meses gratis.* | clic en cada chip |
| 20,7–24,3 | Y a tu segundo: ¿qué frase va arriba de esta semana? | Simeone en la banda del Atlético | RETO PARA TU STAFF · **¿Qué frase va arriba** *de esta semana?* · LISTA DE ESPERA · HASTA EL 27 NOV · *3 meses gratis.* | salida de música de 1,2 s; el vídeo acaba 0,7 s tras la última palabra |

## 4. Voz
Mateo – News & Digital Stories (`gpMzl7dbkfC9dIxAqQZT`, eleven_v4; la original `Rie0…` sigue desactivada: «disabled by the owner»). Toma A. Cuerpo ×1,1, CTA ×1,05, sin pausa antes del CTA (0,16 s). Sin transcripción automática (Hugging Face bloqueado): frases colocadas por silencios reales (`sil.py`) y asignadas al guion por orden y duración.

## 5. Música
Pista nueva (ElevenLabs music v2.5, mi menor, pluck de cristal, rolls de hi-hat; 2 variaciones, elegida la que tiene corte real). Retrasada 0,18 s para que el beat vuelva justo en «el martes la entrenas». Nivel de la mezcla como u29 (música a 0,26 tras loudnorm). Copia sin música en `reels/final/u30-sin-musica.mp4`.

## 6. Material real
Foto `PROTEAM_EQUIPO_ENTRENAMIENTO_REAL_MADRID_FOTO_001` (Ruben Ortega, CC BY-SA 4.0) · `PROTEAM_ENTRENADOR_REFERENTE_FOTO_021` (Simeone; Commons) · captura real `PROTEAM_PRODUCTO_SEMANA_CAPTURA_001`. Personas como ejemplo, nunca como aval; sin nombres de club en rótulos.
## 7. Elementos de edición
Tachados, recuadros y subrayado azules, plantilla de semana en papel, chips del CTA.
## 8. Lo que no se dice
Que la app relacione sesiones con el objetivo o proponga tareas: no se ve en la captura. «→ presión tras pérdida» va en la plantilla de papel (ejemplo nuestro), no en la app.

## 9. Hueco (decisión del turno de las 0:37)
El primer hueco libre era mar 17/11 22:30, justo detrás de u29 (20:30), que es el «por dentro» de balonmano: misma estructura. **Decidido:** u30 va al mié 18/11 9:30 y el 22:30 del martes queda para un Reel de baloncesto con voz de la reserva (encargo en la oficina para el turno de las 3:37), porque dos Reels seguidos no repiten deporte ni estructura.

## 10. Diez preguntas
1. Interesa: todo entrenador de fútbol 11 ha preparado el sábado sin entrenarlo el martes. 2. Concreto: tres días con contenido y una frase real de la app. 3. Para recordar: «si la frase está arriba, el martes la entrenas». 4. Distinta: primera Planificación por dentro. 5. Otra cuenta: no tendría la pantalla. 6. Valor: plantilla para el domingo. 7. Formato: corto con voz y tres zooms. 8. Interés: tachado 4,6 s, móvil 6,1 s, papel 12,8 s, golpe 15,3 s. 9. Realista: todo existe. 10. ProTeam: la semana planificada es lo que el CTA ofrece preparar.
