# TAREA: Auditoría de estado real de las correcciones del incidente Samu

**ID propuesto**: P-999 (auditoría)
**Fecha**: 2026-10-04
**Repo destino**: `../velo_wa/` (agente que ejecuta las correcciones)
**Ejecutor**: agente de código en `velo_wa`
**Tipo**: auditoría de solo lectura — no modificar nada

---

## Contexto

En el marco del programa Vouchers Digitales 2026 (contrato CT-239-26-3), el piloto del agente conversacional en Arepas Rellenas Samu (tenant `arepas-rellenas-samu-UK5K`) presentó un incidente: cobros erróneos, pedidos duplicados y envío repetido de la carta. El establecimiento se retiró y la Cámara de Comercio pidió garantías de que no se repita.

Se hicieron afirmaciones sobre correcciones ya "deployadas". Necesito que verifiques, **con evidencia**, cuáles de esas afirmaciones son ciertas HOY en el código y en producción. No asumas: si no lo ves en el archivo o en la DB, no está.

## Objetivo

Para cada afirmación listada abajo, determina el estado real (HECHO / PARCIAL / NO HECHO) y adjunta evidencia verificable: ruta de archivo + número de línea, hash de commit, o salida de consulta. Refuta cualquier afirmación que no se sostenga.

## Afirmaciones a verificar

| # | Afirmación hecha a la Cámara | Qué verificar |
|---|---|---|
| 1 | "El bot ya no calcula precios (usa el catálogo)" | ¿`CreateOrderTool` delega en `OrderPricingService::quote()`? ¿O sigue aceptando `price`/`total` del LLM y sumando en `resolveTotal()`? |
| 2 | "No puede duplicar pedidos" | ¿Existe idempotencia por conversación (un guard que impida crear N pedidos activos para el mismo pedido)? |
| 3 | "No puede repetir la carta" | (a) ¿Cuál es el `condition_text` real de la intención `pedir-menu` en producción? (b) ¿Existe cooldown/límite por conversación en el motor V2? |
| 4 | "Endurecimos la detección de intenciones" | ¿Está la instrucción endurecida (reglas 1-5) en `AiAgentService::appendIntentContext`? |
| 5 | "Todo está deployado" | ¿Qué release corre en producción? ¿Incluye los fixes 1-4? |
| 6 | Fix P-009 (imagen no renderizaba) | ¿`SendAutomationSequenceStep` fija `media_mime_type`/`media_filename`? |
| 7 | Gate de horario | ¿Existe algún control para que el bot no tome pedidos fuera del horario del restaurante? |
| 8 | Flujo de confirmación por humano | ¿Existe algún mecanismo donde el restaurante acepte el pedido antes de que el bot confirme al cliente? |
| 9 | Timeout de confirmación | ¿Existe algún timeout que avise al cliente si el restaurante no responde? |

## Método

**Código (repo `velo_wa`)**
- Inspecciona los archivos directamente; cita ruta y línea.
- Busca los archivos: `app/Services/AiAgent/Tools/CreateOrderTool.php`, `app/Services/Pricing/OrderPricingService.php`, `app/Jobs/SendAutomationSequenceStep.php`, `app/Services/AiAgentService.php`, `app/Services/Automations/AutomationV2Engine.php`, `app/Services/AiAgent/Tools/RecordDetectedIntentTool.php`.
- Revisa `git log` y `git branch --contains` para saber qué está en `main`.

**Producción (SSH `waterfall`, solo lectura)**
- Release: `cd ~/app.aricrm.co/current && git log -1 --oneline`
- Verifica que el código deployado coincida con `main` (no asumas que el push a main implica deploy — el deploy es manual vía Waterfall).
- Intención en producción:
  ```sql
  SELECT slug, condition_text, is_active FROM ai_intents
  WHERE tenant_id = '01a0ac93-dc1c-73e6-b872-b2c572070661';
  ```
- Corre el mismo grep sobre los archivos deployados para confirmar que el fix está en el servidor, no solo en el repo local.

## Formato de salida

Una tabla:

| # | Afirmación | Estado real | Evidencia | Acción necesaria |
|---|---|---|---|---|

Después de la tabla:
1. **Lista de afirmaciones NO sostenidas** — las que se hicieron pero no son ciertas.
2. **Riesgo de credibilidad** — qué pasa si la Cámara verifica y no es cierto.
3. **Tareas faltantes** — qué hay que implementar y deployar para que cada afirmación sea verdadera.

## Reglas

- Si no lo ves en el archivo o en la DB, **NO está hecho**. No infieras por nombres de archivos ni por commits locales.
- Distingue **repo local** de **producción deployada**. Un fix en `main` sin deploy no protege al cliente.
- Cita siempre: `ruta:línea`, hash de commit, o resultado de query.
- No modifiques nada. Solo lectura y reporte.
- No "arregles" nada en esta tarea — es auditoría.

## Contexto adicional

El diagnóstico del incidente está en el repo del programa: `evidencias/arepas-rellenas-samu/incidentes/2026-10-02-diagnostico-pedidos-cartas.md`.

Las tareas derivadas (P-010 a P-014) podrían no existir en `TASKS.md`.

---

## Resultado esperado (referencia interna — no incluir en el prompt enviado al agente)

Estado verificado por el harness el 2026-10-04 (SSH waterfall), como punto de contraste para validar el reporte del agente:

| # | Afirmación | Estado esperado |
|---|---|---|
| 1 | Bot no calcula precios | ❌ NO HECHO — `CreateOrderTool` sigue con `resolveTotal` sobre input del LLM |
| 2 | No duplica pedidos | ❌ NO HECHO — sin idempotencia |
| 3 | No repite la carta | ⚠️ PARCIAL — condiciones endurecidas pero `condition_text` = "El cliente manifiesta querer conocer la carta, menú, productos" |
| 4 | Detección endurecida | ✅ HECHO — reglas 1-5 en `AiAgentService::appendIntentContext` |
| 5 | Todo deployado | ⚠️ PARCIAL — release `5499016`; P-009 y pricing service presentes, pero `CreateOrderTool` sin wirear |
| 6 | Fix P-009 | ✅ HECHO — `SendAutomationSequenceStep` con `MediaAttributes::guessMimeType` |
| 7 | Gate de horario | ❌ NO HECHO |
| 8 | Confirmación por humano | ❌ NO HECHO |
| 9 | Timeout | ❌ NO HECHO |
