# Exportación controlada de conversaciones — Beto's Pizza

**Fecha/hora de exportación:** 2026-10-05 12:37 UTC  
**Origen:** Waterfall / AriCRM, consulta de solo lectura.  
**Alcance:** tenant de Beto's Pizza únicamente.

## Resultado

- Conversaciones exportadas: 363.
- Mensajes exportados: 6.355.
- Rango de conversaciones: 2026-09-21 19:33:16 a 2026-10-05 03:53:42 (según timestamps almacenados en Waterfall).
- Archivo local: `raw/waterfall-conversaciones-2026-10-05.json`.

## Protección de datos

El archivo de conversaciones contiene datos personales y contenido de mensajes. Está almacenado con permisos locales restrictivos (`600`) dentro del directorio `raw/` (permisos `700`), que está excluido de Git. No se debe copiar, publicar, usar como ejemplo identificable de prompt ni mezclar con otros clientes.

La exportación fue autorizada de forma explícita para caracterización, parametrización, pruebas y mejora del agente de este establecimiento. Ver excepción vigente en `SOURCES.md` y decisión de 2026-10-05 en `DECISIONS.md`.
