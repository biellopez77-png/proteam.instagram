# Contexto ProTeam — equipo técnico (leer siempre)

## Proyecto
- **App:** ProTeam, hecha en Lovable y sincronizada con GitHub: **biellopez77-png/proteamapp** (rama `main`). Cómo trabajar en el código: `revision/APP_REPO.md`.
- **Project ID de Lovable:** `752a85cb-6281-4373-9da6-8b833b2e0910` · Editor: https://lovable.dev/projects/752a85cb-6281-4373-9da6-8b833b2e0910
- **Qué es:** gestión de equipos de balonmano, fútbol y baloncesto: landing pública, blog y biblioteca de ejercicios; Inicio del entrenador; Planificación (macro/meso/microciclos, plantillas semanales); sesiones de pista, físicas y mixtas; rutinas; partidos en directo con estadística (GF, RPE de partido, modo cuadrícula); informes PDF/Excel (ReportSpec); jugadores, tests físicos, RPE y carga sRPE; facturación con Stripe.
- **Stack:** TanStack Start + React 19 + Tailwind 4 + shadcn, Supabase (RLS, RPCs `match_*`), React Query, recharts, jsPDF. Gestor de paquetes: bun.
- **i18n:** 7 idiomas (es, ca, en, fr, pt, de, it), diccionarios en `src/lib/i18n/dict/*.json`; idioma por defecto es; `bun run build` ejecuta `i18n:check` y falla si falta alguna traducción.
- **Archivo grande:** `src/routes/_authenticated/coach.matches.live.$id.tsx` (~3000 líneas).

## Reglas obligatorias
1. **Código en GitHub, no mensajes a Lovable.** Se lee y se arregla en el repositorio `proteamapp` siguiendo `APP_REPO.md`. `send_message` de Lovable ya no se usa para arreglos (gasta créditos y no hace falta). Con el conector Lovable solo: `query_database` (solo SELECT), `get_project`, `list_messages`/`get_message` y `deploy_project` para publicar arreglos pequeños ya subidos.
2. **Solo lo que pide Biel o un fallo real con evidencia.** Nada de funciones extra: las ideas nuevas van a «Ideas aparcadas» del BACKLOG.
3. **Pequeño en `main`, grande en pull request** (definición en `APP_REPO.md`). Biel revisa los PR; el equipo no los fusiona.
4. **Datos:** nunca borrar ni sobrescribir datos. Prohibido `DELETE`/`UPDATE` desde `query_database`. Migraciones solo aditivas y siempre en PR.
5. **Cambios visuales:** mismos flujos, botones y datos, salvo que se pida lo contrario.
6. **Textos:** todo texto nuevo con `t()` y en los 7 idiomas; ni castellano en catalán ni al revés.
7. **Antes de subir:** `bun run build` sin errores, diff mínimo, `bun.lock` restaurado.
8. **Pagos:** nada de pagos, tarjetas, planes ni Stripe en producción: eso es de Biel.
9. **Con Biel:** en español, breve y al grano.

## Formato de hallazgo
`[ID] · Área · Severidad (Crítica/Alta/Media/Baja) · Qué pasa · Evidencia (archivo:línea o SQL + resultado) · Propuesta · Coste (bajo/medio/alto)`. IDs: `A-###` (análisis), `E-###` (estructura), `L-##` (arreglos).

## Términos de balonmano (para revisar traducciones)
| Término | Significado | Traducción correcta |
|---|---|---|
| Part / Parte | Periodo del partido | Half · Mi-temps · Halbzeit |
| Canvi | Sustitución en el partido | Substitution |
| GF (golpe franco) | — | en FT · fr JF · it TL · de FW · pt LV |
| GF nuestro | Se registra en defensa | — |
| GF del rival | Se registra en ataque | — |
