# Métrica de diciembre: equipos que crean su primera semana de entrenos (Samuel, 06 · mié 18/11/2026)

Encargo de Biel (panel de dirección, 17/11). Datos leídos hoy a las **8:53 (Madrid)** en la base de datos de la app (Lovable, proyecto 752a85cb…, solo consultas de lectura). No se ha escrito nada en la base de datos.

## 1. De dónde sale el dato
- **Hoy no sale del apartado «Análisis» del admin.** Ese apartado (publicado el 17/11) enseña cuentas, cuentas activas, lista de espera y facturación; no tiene ninguna tarjeta de semanas creadas.
- **Mientras no la tenga, el número se lee cada noche con la consulta de abajo** (bucle de las 22:41). Es el mismo dato que enseñaría la tarjeta.
- Propuesta para el equipo técnico (no bloquea nada): una tarjeta «Equipos con primera semana» en «Análisis», con el filtro de fechas que ya existe y la misma separación lista de espera / cuentas nuevas. Hasta que exista, vale la consulta.

## 2. Qué cuenta como «primera semana creada»
**Un equipo cuenta el día en que, por primera vez, tiene una semana (microciclo) con al menos una sesión de entreno dentro.**
En la base de datos: la primera fila de `microcycle_links` de ese equipo con `item_type` «court» o «live» (una sesión enlazada a una semana). La fecha es el `created_at` de esa fila.

Por qué así y no «tiene un microciclo»:
- Las semanas vacías se crean en bloque al montar la temporada: hoy hay 140 microciclos de solo 4 equipos (uno tiene 105, creados en 2 momentos). Una semana vacía no es una semana preparada.
- Un partido o un evento enlazado no es un entreno: no cuentan (hoy hay 15 enlaces de partido, 3 de evento y 1 de test).

Dos avisos para leer bien el número desde el 28:
- **La semana que montamos nosotros también deja esa fila.** Para la lista de espera se promete «tu semana montada»: si la monta el equipo de ProTeam, el equipo aparecerá con primera semana sin haberla hecho él. Cada noche se dan las dos cifras: con primera semana (cualquiera) y **creada por alguien del propio equipo** (`created_by` es miembro del equipo y no un administrador). La métrica de Biel es la segunda.
- Cada equipo cuenta una vez, el día de su primera semana.

## 3. Cómo se separa lista de espera y cuentas nuevas
- **Lista de espera:** la organización tiene un acceso con la nota «Llista d'espera Blackout Friday: 3 mesos» en `organization_access_grants`.
- **Cuenta nueva:** equipo creado desde el sáb 28/11 a las 00:00 (Madrid) sin ese acceso.
- **Anteriores a la campaña:** el resto (los que ya estaban en prueba o con acceso manual). No entran en la métrica de diciembre.

## 4. Foto de hoy (mié 18/11, 8:53)
| grupo | equipos | con primera semana | última |
|---|---:|---:|---|
| Lista de espera | **15** | **0** | — |
| Cuentas nuevas (desde el 28/11) | 0 | 0 | — |
| Anteriores a la campaña | 8 | 3 | 14/11 |

Es lo esperado: la lista no entra en la app hasta el 28. El punto de partida de diciembre es **0 de 15**.
Dato aparte, leído en la misma consulta: los 15 equipos de la lista son de **balonmano** y los 15 se crearon el **martes 17/11**.

## 5. Las dos cifras de la lista (15 y 9): cuál es la buena
**La buena es 15.** Las dos son la misma cuenta (accesos «Llista d'espera Blackout Friday») leída a horas distintas del martes 17/11:
- El 17/11 entraron 15 equipos, uno a uno: 3:xx, 4:xx, 12:xx, dos a las 13:xx, dos a las 16:xx, 18:xx, 20:xx (van 9), 22:00, 22:16, 22:33 (dos), 22:47 y 23:15 (van 15).
- La revisión técnica leyó **9**: es la cifra que había entre las 20 h y las 22:00. La estrategia dice **15**: es la cifra desde las 23:15.
- Hoy a las 8:53 siguen siendo 15 (ninguna alta el 18 todavía).
No hay dos formas de contar ni un error: es una foto antes y otra después de las altas de la noche.

## 6. Qué se entrega cada noche desde el sáb 28
Una línea en el diario (`reports/diario-AAAA-MM-DD.md`) y en el parte:
«Primera semana: lista de espera N de M (hoy +n) · cuentas nuevas N de M (hoy +n) · montadas por nosotros: N».
Si una cifra no se puede leer esa noche, se escribe «sin dato» y el motivo. No se estima.

## Consulta (solo lectura)
```sql
with wl as (select distinct organization_id from organization_access_grants
            where note ilike 'Llista d''espera%'),
fw as (select l.team_id, min(l.created_at) first_at,
              bool_or(exists(select 1 from team_members tm
                             where tm.team_id = l.team_id and tm.user_id = l.created_by)) propia
       from microcycle_links l where l.item_type in ('court','live') group by l.team_id)
select case when wl.organization_id is not null then 'lista de espera'
            when t.created_at >= '2026-11-28 00:00+01' then 'cuenta nueva'
            else 'anterior' end grupo,
       count(*) equipos, count(fw.team_id) con_primera_semana,
       count(*) filter (where fw.propia) creada_por_el_equipo,
       count(*) filter (where (fw.first_at at time zone 'Europe/Madrid')::date
                              = (now() at time zone 'Europe/Madrid')::date) hoy
from teams t left join wl on wl.organization_id = t.organization_id
left join fw on fw.team_id = t.id where not t.archived group by 1;
```
Límite conocido: «creada por el equipo» se decide por quién enlazó la sesión; si un administrador de ProTeam es además miembro del equipo, contaría como propia. Se revisará a mano el 28 con los primeros casos.
