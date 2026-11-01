# Spec velo_wa — retiro de `get_daily_menu` en Calamar Azul y prompt v9 (P-016 del programa CCM Vouchers)

**Solicitado por**: harness `ccm-vouchers-2026` (tarea P-016 en `../TASKS.md`) · 2026-10-31
**Prioridad**: alta — el agente de Calamar Azul está a un despliegue de quedar coherente con las reglas confirmadas por el establecimiento el mismo día; mientras tanto, la tool de menú del día sigue en el flujo pese a la decisión de no usarla y el ejecutivo se describe sin la bebida confirmada.
**Diagnóstico y evidencia completa**: `../clientes/mar-azul/PROGRESS.md` (entradas del 2026-10-31) y `../evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md` (rondas 1–4 y addendum) en el repo `ccm-vouchers-2026`.

## 01 — User story

Como operador del tenant Calamar Azul (menú **fijo**, sin variación diaria),
quiero que el agente IA describa el almuerzo ejecutivo y los acompañantes desde su `system_prompt` (definiciones confirmadas por el establecimiento) y que la herramienta `get_daily_menu` quede fuera de su flujo,
para que el bot no declare «no disponible» el plato más vendido cuando no hay menú del día publicado, no contradiga las reglas del restaurante y no dependa de una publicación diaria que nadie va a hacer.

## 02 — Contexto (verificado)

**Tenant y agente** (verificación de solo lectura 2026-10-30, release `d4e3cf55`):

- Tenant `01a0fcc8-7908-71e0-ac67-c8aca5e05bf2` (Grupo D Mar Azul SAS). Agente único: `Asistente Calamar Azul` (`01a14570-da52-70b4-b234-ba7b128d642a`), `is_enabled = false`, `pilot_mode_enabled = true`, modelo `gpt-4.1` desde la publicación de la v7 (2026-10-31).
- `enabled_tools` (12): `get_catalog`, `quote_order`, `create_order`, `get_delivery_fee`, **`get_daily_menu`**, `handoff_to_human`, **`is_holiday`** (herramienta muerta: `IsHolidayTool` no existe en el release), `record_detected_intent`, `get_contact`, `update_contact`, `create_task`, `schedule_follow_up`. Además **`daily_menu_tool_enabled: true`** en config.
- Metadatos de versión falsos: `config.prompt_version = v2-produccion-2026-10-16` y `config.prompt_sha256 = 9144893d…` no corresponden al prompt vivo.

**La tool y el bloque de código**:

- En la ruta productiva, `AiAgentService::appendDailyMenuToolContext()` agrega al prompt efectivo un bloque «Menú del día (herramienta obligatoria)». El sandbox del harness pasa el prompt crudo y no lo reproduce, así que el bloque solo se manifiesta en producción.
- Con el menú del día vacío, `get_daily_menu` devuelve `available:false` (67 B). En la ronda 1 del guion MA (2026-10-31), eso produjo que el bot declarara el almuerzo ejecutivo «no disponible hoy» (caso MA-02, falla reproducible) aunque el catálogo lo vende a $26.000 — la venta más frecuente del corpus. La v7 lo corrigió por disciplina de prompt, pero la tool y el bloque siguen en el flujo.
- `GetDailyMenuTool` no implementa el marker `ReadOnlyTool` aunque su `execute()` solo lee: `playgroundToolsFor()` la excluye del playground de la UI y no se puede probar desde `/settings/ai-agent` (el harness la admite vía `playgroundToolsOverride()`).

**Decisiones y confirmaciones del 2026-10-31** (fuentes canónicas en el harness):

- **Decisión de Nicolás**: `get_daily_menu` **no se debe usar en este tenant**. El establecimiento tiene menú fijo.
- **Definición confirmada del ejecutivo** (`../evidencias/mar-azul/vertical-restaurantes/almuerzo-ejecutivo-2026-10-31.md`): filete apanado, bagre, mojarra, sierra o trucha, con sopa de pescado, arroz de coco, patacón, ensalada y **bebida de agua de panela con limón** — $26.000, solo hasta las 3:00 p. m., sujeto a agotados; las opciones disponibles del día las confirma caja.
- **Menú fijo confirmado**: el establecimiento no cambia el menú a diario; el agente nunca responde con un menú variable ni dice que no sabe qué hay hoy.
- **Acompañantes confirmados** (`../evidencias/mar-azul/vertical-restaurantes/acompanantes-carta-2026-10-31.md`): platos de carta sin sopa ni bebida; cazuelas, sancocho, pescados de carta y especialidades con arroz, patacón y ensalada; excepciones — ensalada Brisa del Mar y mix de mariscos solo arroz y patacón, paella con patacón con queso, ceviches con galletas de soda, **Cayana Mar Azul con arroz y ensalada** (la base es patacón con trucha), **patacón marinero con ensalada**, **pasta marinera con patacón**. Cambios de acompañamiento: solicitud sujeta a caja, sin cobrarla por cuenta del bot.
- Ninguna versión del prompt hasta la v8 incluye estas confirmaciones (llegaron después de las rondas 1–4). Estado de versiones: v5 (línea base, SHA `4c21a851…`), v6 `v6-domicilios-y-reservas-2026-10-30` (SHA `b0ad4822…`), **v7 `v7-disciplina-tools-y-escalamiento-2026-10-31` publicada** (SHA `8ab67ca2…`), v8 `v8-cobertura-y-promesas-2026-10-31` en preview sin publicar (SHA `45bf0f89…`).

**Restricción importante**: otros tenants **sí** usan menús del día variables (p. ej. La Rancha, cuyo agente gira por completo alrededor del menú del día). La funcionalidad **no** se retira del producto: se desactiva para este tenant y el bloque de contexto queda condicionado.

## 03 — Criterios de aceptación

- **AC1 — Config del tenant**: `enabled_tools` del agente de Calamar Azul queda **sin** `get_daily_menu` y **sin** `is_holiday`, con `daily_menu_tool_enabled: false`; las demás nueve tools se conservan intactas.
- **AC2 — Gate de código**: la ruta productiva **no** agrega el bloque «Menú del día (herramienta obligatoria)» a un agente cuya config no tiene la tool habilitada. El gate se prueba con test de código (unit/feature sobre `appendDailyMenuContext`), no solo en producción.
- **AC3 — Sin regresión global**: un agente con `get_daily_menu` habilitada (p. ej. La Rancha) sigue recibiendo el bloque y la tool funciona igual que hoy.
- **AC4 — Ejecutivo desde el prompt**: re-corrida de MA-01 y MA-02 con las expectativas del addendum del guion MA: el bot describe el ejecutivo con la definición confirmada (incluida la bebida **agua de panela con limón**), cotiza $26.000, deja las opciones del día a caja, nunca dice «no disponible hoy» ni menciona «limonada de la casa».
- **AC5 — Acompañantes**: los casos de acompañantes pasan (MA-03 y MA-08 del guion MA; T12–T22 del guion derivado `../clientes/mar-azul/PRUEBAS_CONVERSACIONALES.md`), incluidas las excepciones y correcciones por plato.
- **AC6 — Ronda limpia**: la suite MA de 32 casos queda en verde con las expectativas del addendum, con cero `ok=false` y **sin ninguna llamada a `get_daily_menu`** en los logs de la ronda.
- **AC7 — Versionado**: la v9 se publica como snapshot nuevo con hash (convención de `docs/mar-azul/prompts/asistente-whatsapp/`, sin sobrescribir v5–v8) y `config.prompt_version`/`config.prompt_sha256` quedan correctos al publicar.

## 04 — Propuesta técnica

**A. Config del tenant (producción, con autorización)** — quitar del agente `01a14570-da52-70b4-b234-ba7b128d642a`: `get_daily_menu` de `enabled_tools`, `is_holiday` (herramienta muerta, ya señalada en la verificación del 2026-10-30) y pasar `daily_menu_tool_enabled` a `false`. No tocar `is_enabled` (sigue `false`), `pilot_mode_enabled`, ni los teléfonos autorizados.

**B. Gate de código (evolución del producto)** — en `AiAgentService::appendDailyMenuToolContext()`: solo agregar el bloque «Menú del día (herramienta obligatoria)» cuando el agente tenga la tool habilitada (`get_daily_menu` en `enabled_tools` y/o `daily_menu_tool_enabled`, según la fuente canónica de esa config en el código). Encuadre de producto, no parche por tenant: cualquier cliente con menú fijo se beneficia; los de menú variable (La Rancha) no cambian en nada. Recomendado en la misma pasada: agregar el marker `ReadOnlyTool` a `GetDailyMenuTool` para que sea probable desde el playground de la UI (`playgroundToolsFor()` hoy la excluye).

**C. Prompt v9 (Calamar Azul)** — nuevo snapshot ramificado de la última versión versionada (v8 en preview, SHA `45bf0f89…`; si para entonces se publicó, de la última publicada), que:

1. Incorpore la definición confirmada del ejecutivo (con la bebida), el menú fijo y las reglas de acompañantes con sus excepciones y correcciones — texto fuente: las dos páginas canónicas citadas en la sección 02.
2. Elimine toda instrucción de consultar menú del día / `get_daily_menu`.
3. Conserve las ganancias de v7/v8 verificadas en las rondas: disparo de `quote_order` sin aritmética propia, sustituciones como cambio (no adición) sujetas a caja, escalamiento obligatorio (tiempo de entrega, estado del pedido, gramaje ausente), franja de reservas 2:00–4:30 p. m. con retención de 30 minutos y evento empresarial como excepción, sin promesas de cobertura ni de tiempo, moneda colombiana (`$6.000`), asterisco simple de WhatsApp.
4. Se publique con `calamar:configure-agent` conservando `gpt-4.1`, corrigiendo `config.prompt_version`/`config.prompt_sha256` en la misma operación.

**Notas**:
- El prompt v9 solo lleva lo **confirmado**; los puntos abiertos (si el patacón marinero también lleva arroz, si la pasta marinera también lleva ensalada, el tipo de arroz estándar y el caso de la langosta) no se inventan y quedan fuera hasta confirmación del establecimiento.
- El catálogo (92 ítems, 9 categorías) ya contiene el ejecutivo a $26.000; el prompt no debe duplicar precios de carta que el bot debe tomar de `get_catalog`/`quote_order` — la definición del ejecutivo y los acompañantes son reglas de composición, no una segunda lista de precios.

## 05 — Testing

- **Unit/feature (nuevo)**: agente sin `get_daily_menu` en `enabled_tools` → `appendDailyMenuToolContext()` no agrega el bloque; agente con la tool → lo agrega (AC2/AC3).
- **Feature existente**: suite de regresión del agente en verde.
- **Ronda sandbox**: re-corrida del guion MA (`../evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md`) con las expectativas del addendum del 2026-10-31, por el método del spec de regresión sandbox (docs/AI_AGENT_SANDBOX_REGRESSION_SPEC.md, en el repo `velo_wa`). Verificar en los logs: cero llamadas a `get_daily_menu`.
- **Consulta de solo lectura post-cambio**: `enabled_tools`, `daily_menu_tool_enabled`, `config.prompt_version`/`prompt_sha256` del agente en DB.

## 06 — Fuera de alcance

- Campo de notas para `quote_order` (las sustituciones siguen yendo en el texto a caja): deuda de producto separada.
- Aliases de barrios, conflicto de tarifas (Arenillo, La Castellana, Santos) y bloqueos del camino WhatsApp real (teléfono remitente fuera del pilot, conversación con dueño humano): ya registrados en el guion MA.
- Prompts de otros tenants, imágenes del catálogo y capa conversacional (plantillas/etiquetas) de Calamar Azul.

## Verificación post-deploy (producción)

1. Consulta de solo lectura: `enabled_tools` sin `get_daily_menu` ni `is_holiday`, `daily_menu_tool_enabled = false`, metadatos de versión correctos.
2. Re-corrida de la suite MA con expectativas del addendum: 32/32, cero `ok=false`, sin `get_daily_menu` en logs; casos de ejecutivo y acompañantes con las definiciones confirmadas.
3. Verificar que el prompt efectivo de la ruta productiva no contiene el bloque «Menú del día» (captura o log del prompt armado).
4. Registrar la evidencia en `../clientes/mar-azul/PROGRESS.md` del repo `ccm-vouchers-2026` y cerrar P-016 en `../TASKS.md`.
