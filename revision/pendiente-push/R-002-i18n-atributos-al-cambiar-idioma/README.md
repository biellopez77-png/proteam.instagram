# R-002 — Al cambiar de idioma, los textos de ayuda se quedaban en el idioma anterior

**Qué pasa hoy.** `src/lib/i18n/index.tsx` (commit fb80d88): `translateAttrs` traduce `title`, `placeholder`, `aria-label`, `alt` con `setAttribute`. El `MutationObserver` (bloque «Re-translate nodes React adds or updates later», `attributeFilter: ATTRS`) recibe también ese cambio propio, borra el original guardado (`delete store[r.attributeName]`) y vuelve a traducir: guarda como «original» el texto ya traducido.

Consecuencias:
1. **Error**: el entrenador cambia el idioma en Configuración (sin recargar) y los placeholders, tooltips y etiquetas de lectores de pantalla escritos como literales se quedan en el idioma anterior (el diccionario nuevo no reconoce el texto ya traducido). Se arregla solo al recargar.
2. **Rendimiento**: cada atributo traducido se procesa dos veces (búsqueda en el diccionario de 5.266 claves incluida) en cada pantalla que se monta.

**Qué cambia.** Se apunta el valor que escribe la propia capa (`appliedAttr`) y el observador ignora los registros cuyo valor coincide con él. Cuando React escribe un valor nuevo, se traduce igual que antes.

**Prueba** (`prueba-jsdom.mjs`, misma lógica con jsdom): castellano → inglés.
- Sin parche: `placeholder` y `aria-label` se quedan en «Buscar jugador» / «Cerrar menú»; 8 llamadas a `translateAttrs`.
- Con parche: «Search player» / «Close menu»; 5 llamadas. Si React vuelve a escribir el original catalán, se traduce bien en los dos casos.

**Aplicar** (en proteamapp): `python3 <esta carpeta>/aplicar.py` → `bun run build` → commit en `main`, push y `deploy_project`. Probar: Configuración → idioma English → el buscador de jugadores y el botón del menú móvil deben salir en inglés sin recargar. Una segunda ejecución del script no toca nada.
