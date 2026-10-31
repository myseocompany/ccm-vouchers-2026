# Parche de prompt — tarifas de domicilio incrustadas — 2026-10-08

**Origen:** instrucción de Nicolás «Parcha el JSON» (2026-10-08), sobre el hallazgo de que el prompt referenciaba `../operacion/domicilios/tarifas-flash-delivery-2026.json` — un archivo que el agente no puede leer durante la conversación, por lo que no podía cotizar domicilios y escalaba todo.

**Alcance autorizado:** cambiar solo el `system_prompt` del agente de Friends Chicken (`01a0af94…`) y sus metadatos de versión, vía SSH en `waterfall`. Sin tocar ítems, tarifas de la DB, pedidos, líneas ni automatizaciones.

## Cambios exactos sobre el prompt vigente

1. **Conservado sin modificar** el bloque «Datos para Transferencia» (titular Mónica Carolina Araujo Portillo, Bancolombia, Llave Bre-B) — editado directamente en producción el 2026-10-07 22:55 UTC **sin bump de versión** (hallazgo del guard de precondiciones: el hash del prompt ya no era el de la v1 documentada). Este parche lo recupera como parte del estado versionado.
2. Bullet «Zonas de cobertura y costo de domicilio»: la referencia al archivo externo se sustituye por la sección incrustada; se elimina el contraste obsoleto para `Conjunto La Estación`, `Cuchilla de los Santa` y `Santa Helena` (nombres confirmados por Nicolás el 2026-10-07 según las notas del propio JSON).
3. Se añade al final la sección «## Tarifas de domicilio — Flash Delivery Manizales (2026)» con el **JSON íntegro** de `tarifas-flash-delivery-2026.json` (179 zonas, COP, reglas de verificación y notas) en un bloque de código.

## Metadatos aplicados

- `prompt_version`: `v2-fc-tarifas-domicilio-2026-10-08`
- `prompt_sha256`: `01e32185cb29c1517ed55f4dbcf1fd20bf8aeb486a005dc179d1f577fd7ca13d` (19.593 chars)
- `prompt_updated_from`: `tarifas_flash_delivery_json_2026-10-08`
- Snapshot versionado en el repo AriCRM: `docs/friends-chicken/prompts/agente-domicilios/v2-fc-tarifas-domicilio-2026-10-08.md` (junto con la línea base v1 recuperada).

## Verificación (10/10 OK, 2026-10-08)

- Precondición 1: prompt actual = v1 + datos de transferencia (hash `0a2f28a1…` coincidente).
- Precondición 2: las 179 tarifas del JSON son **idénticas** a las activas de la sede Centro en `delivery_tariffs` (sin diferencias de nombre ni precio).
- Post: hash v2 coincidente; sección de tarifas presente exactamente 1 vez; sin referencia al archivo externo; secciones «Menú Friends Chicken» y «Prioridad operativa» intactas; datos de transferencia conservados; 179 zonas en el prompt; `config.prompt_sha256` y `config.prompt_version` actualizados; agente sigue `is_enabled=false` (borrador pendiente de activación).

## Rollback

Restaurar el prompt desde el snapshot v1 (`docs/friends-chicken/prompts/agente-domicilios/v1-fc-menu-snapshot-2026-10-07.md`) o desde la línea base v1 + datos de transferencia (hash `0a2f28a1…`), actualizando `prompt_sha256`/`prompt_version` en la misma operación.
