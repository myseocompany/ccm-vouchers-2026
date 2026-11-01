# PLANTILLAS DE RESPUESTA (SECUENCIAS) — Formato del vertical restaurantes

Formato canónico de las "plantillas de respuesta" del programa: **secuencias de mensajes de WhatsApp** que el sistema envía automáticamente al cumplirse una condición. Las definiciones concretas de cada establecimiento viven en `clientes/<slug>/PLANTILLAS_WHATSAPP.md`.

> Decisión del programa (2026-09-30, Nicolás): el flujo usa la acción **`send_sequence`**, no `send_template`. Las secuencias funcionan en **cualquier línea (Evolution y Cloud API)** y no requieren aprobación de Meta.

## Mecanismo (verificado en código AriCRM, 2026-09-30)

Dos condiciones, dos reglas V2, una misma acción:

| Condición | Disparador V2 | Acción |
|---|---|---|
| Inicio de conversación (primer mensaje del cliente) | `NewConversation` | `send_sequence` → secuencia de bienvenida |
| El cliente pide la carta (detección semántica) | `AiIntentDetected` (intención `pedir_menu`) | `send_sequence` → secuencia de la carta |

- **Acción `send_sequence`** (motor V2): publicada en `main` (PR #19, commit squash `396ea59`, 2026-09-30) y **deploy verificado en producción 2026-09-30** (release activo `396ea59`, salud 200, 0 migraciones pendientes — `MEMORY.md`). Cada paso es `{type: text|image|video|audio|document, body, media_url, delay_seconds}` con pausas acumuladas (0 a 24 h por paso).
- **Detección de la intención "pedir la carta"**: el agente IA llama a la tool `record_detected_intent`; la instrucción se inyecta automáticamente al prompt desde la tabla de intenciones del tenant (PR #13). No depende de palabras clave literales.
- **Inicio de conversación**: `HandleInboundMessage` detecta `$isNewConversation` y dispara `NewConversation`; el motor V2 deduplica por conversación + contador de reaperturas.
- **Placeholders en los textos**: `{{name}}` (nombre del contacto, por defecto "Cliente"), `{{tenant}}`, `{{phone}}`, `{{company}}`, entre otros (`SequenceTemplateRenderer`). Un placeholder sin dato no rompe el envío: cae al valor por defecto.

## Guardas del envío (por paso, en `SendAutomationSequenceStep`)

La secuencia se corta o se salta si:

1. El contacto hizo opt-out.
2. La conversación está cerrada.
3. **El cliente respondió después de iniciada la secuencia** (los pasos pendientes no se envían — no se spamea sobre la respuesta del cliente).
4. El safety de volumen outbound (`reserveOutboundSlot`) deniega el paso.

## Estructura de cada secuencia

| Secuencia | Pasos típicos |
|---|---|
| Bienvenida | 1) texto de bienvenida (delay 0s) · 2) imagen opcional: logo o foto del local (delay ~2s) |
| Carta | 1) texto "con mucho gusto" (delay 0s) · 2) la carta como texto o imagen (delay ~3s) |

- El link al menú digital (cuando exista) va dentro del texto; las secuencias no tienen botones.
- Si la carta es larga, dividirla en varios pasos de texto (p. ej. por categoría) en lugar de un solo mensaje gigante.

## Puntos abiertos (definir al activar cada cliente)

- **Doble mensaje en la bienvenida**: si la regla no silencia al agente, el cliente puede recibir secuencia + respuesta libre del agente en el mismo turno. `suppresses_ai_reply` existe hoy en automatizaciones V1; verificar paridad V2 antes de activar.
- **Carta una sola vez por conversación**: el dedupe V2 por intención es por mensaje (`ai_intent:<intent>:<message>`), no por conversación. Si el cliente pide la carta dos veces en mensajes distintos, la secuencia se enviaría dos veces. Configurar condición o acordar el comportamiento con el establecimiento.
- **Contenido de la carta**: la secuencia lleva contenido estático; la fuente de verdad del menú es el catálogo estructurado del tenant. Definir quién actualiza la secuencia cuando cambie la carta (evitar divergencia carta–catálogo–secuencia).

## Relación con `send_template`

La acción `send_template` (plantilla Meta aprobada) también quedó publicada en el mismo PR, pero **solo sale por líneas Cloud API** y exige aprobación de Meta por plantilla. Queda como opción futura para locales que migren a Cloud API y quieran botones/estructura aprobada. El flujo del programa es `send_sequence`.

## Checklist de configuración por cliente (workflow 03)

- [ ] Copy validado con el establecimiento
- [ ] Contenido de la carta definido (texto o imagen) y cargado en la secuencia
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia archivada en `evidencias/<slug>/vertical-restaurantes/secuencias/`
