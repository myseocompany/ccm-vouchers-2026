# MEMORY

Índice de conocimiento persistente del programa. Entradas cortas, con fuente y fecha. El contenido detallado va en el archivo que se referencia.

## Convenciones

- Toda entrada debe tener: título, fuente, fecha y utilidad futura.
- No duplicar información que ya esté en `PROGRAMA.md`, `POLICIES.md` o el contrato.
- Actualizar o eliminar entradas obsoletas; no acumular.

## Entradas

### 2026-10-07 — Caso Arepas Rellenas Samu: conversaciones e incidente del piloto
- **Fuente**: `clientes/arepas-rellenas-samu/RESUMEN_INCIDENTE.md` (síntesis sin datos personales del diagnóstico del 2026-10-02 y las auditorías del 2026-10-04; allí constan las rutas de los análisis detallados locales).
- **Utilidad futura**: antes de responder sobre Samu, leer el resumen del incidente y consultar los análisis detallados locales cuando hagan falta. Incluye las conversaciones `01a0ff15-e42a-705f-9597-f10087dbce4f` y `01a0fe7c-1072-7199-9af0-cec2b091602c`, los problemas reportados y el retiro voluntario comunicado el 2026-10-03. Para futuras activaciones usar `templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` desde los workflows 04 y 06. Distinguir el estado histórico verificado el 2026-10-04 del estado actual de producción y evitar reproducir datos personales de los clientes finales.

### 2026-09-30 — Envío de "plantillas de respuesta" por condición (bienvenida + carta), vía secuencias
- **Fuente**: verificación y publicación en `../velo_wa`: acciones `send_sequence` y `send_template` fusionadas a `main` (PR #19, commit squash `396ea59`) y **deploy verificado en producción 2026-09-30** (release activo `396ea59` en Waterfall/Forge; salud 200; 0 migraciones pendientes). **El flujo del programa usa `send_sequence`** (decisión de Nicolás, 2026-09-30): funciona en cualquier línea, incluidas las Evolution, y no requiere aprobación de Meta. `send_template` queda como opción futura para líneas Cloud API.
- **Utilidad futura**: bienvenida con el disparador `NewConversation` y carta con la intención `pedir_menu` detectada por el agente IA, ambas como reglas V2 con acción `Enviar secuencia`. **Piloto: sede San Jorge de Arepas Rellenas Samu** (decisión de Nicolás, 2026-09-30) — la bienvenida envía el menú, réplica automatizada de su práctica actual. Definiciones por cliente en `clientes/<slug>/PLANTILLAS_WHATSAPP.md`; mecanismo, guardas y checklist en `templates/PLANTILLAS_WHATSAPP.md`.

### 2026-09-14 — Sistema de gestión de tareas: AriStudio
- **Fuente**: instrucción directa de Nicolás en conversación, 2026-09-14.
- **Utilidad futura**: gestionar las tareas operativas del programa en `/Volumes/ExternoMS/projects/aristudio` (AriStudio). Mantener en este harness las evidencias, los entregables contractuales y los registros exigidos por `TASKS.md`, `PROGRESS.md` y los workflows; AriStudio no sustituye dichos soportes.
