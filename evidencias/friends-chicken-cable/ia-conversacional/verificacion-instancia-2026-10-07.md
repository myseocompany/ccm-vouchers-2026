# Verificación de la instancia — Friends Chicken — 2026-10-07 (14:05 UTC)

**Hora de corte:** 2026-10-07 14:05 UTC (9:05 a. m. Colombia). **Método:** SSH `waterfall` → `php artisan tinker` sobre `~/app.aricrm.co/current`. Solo `SELECT`, conteos y lectura de flags. Sin escrituras. No se consultaron teléfonos, contactos, conversaciones, mensajes ni credenciales; los UUID se abrevian a 8 caracteres.

## Release

- Release activo: `9585614` (2026-10-06 14:08:27 -0500), sin cambios desde la verificación de las 13:30 UTC.

## Tenant

- `Friends Chicken` (`friends-chicken-uHMR`, id `01a0a5a4…`), activo (sin soft-delete), creado 2026-09-15, onboarding completado 2026-09-15.
- `wa_status=connected`; `max_contacts=10000` (supera el mínimo contractual de 2000); `timezone=America/Bogota`.
- **`business_hours` guardado** (ya no es `null` como en el corte de las 13:30 UTC): lunes a sábado 11:00–19:30, domingo 09:00–17:00. Coincide con `operacion/horario-tenant-2026-10-07.md`.

## Usuarios (C-02)

- `tenant_user_memberships`: **0 usuarios** (0 activos, 0 que hayan iniciado sesión). C-02 exige 3 usuarios por invitación: **no cumplido**.

## Líneas WhatsApp (C-02)

- 1 línea: «Principal», `connected` (evolution), `is_default`, `connected_at` 2026-10-07 10:17:51 UTC, `ai_paused_until=null`, `ai_risk_level=normal`, `updated_at` 13:52:50 UTC. Sin teléfono consultado.
- C-02 exige 3 líneas conectadas: **no cumplido** (1 de 3).

## Agente IA (C-04)

- 1 agente conversacional (`01a0af94…`, «Asistente de domicilios — plantilla»): `is_enabled=true`, `tool_calling_enabled=true`, `llm_model=gpt-4o-mini`, `context_messages=20`, `whatsapp_line_id=null`, `allow_all_lines=false`, sin lista `enabled_tools` en config.
- **Parche de prompt autorizado del 2026-10-07: aplicado y verificado.** `prompt_version=v1-fc-menu-snapshot-2026-10-07`, longitud 12962 chars, `updated_at` 2026-10-07 13:57:51 UTC (8:57 a. m. Colombia). Comprobaciones del parche: bloque «Prioridad operativa» presente exactamente 1 vez; dirección `#19-63` presente y `#19-61` ausente; «domingo, 9:00» presente y «domingo, 11:00» ausente. `config.prompt_sha256` (`adaac15d…e223`) **coincide** con el SHA-256 del texto guardado.
- La config registra además `source_prompt`, `prompt_patch_source`, `prompt_updated_at`, `prompt_updated_from`, `prompt_published_at` y transcripción de audio deshabilitada.
- **Vinculación efectiva a la línea** (lectura de código, `AiAgentService::canUseGlobalAgent`): un agente sin `whatsapp_line_id` y con `allow_all_lines=false` responde mientras el tenant tenga **una sola** línea. Friends Chicken tiene exactamente 1 línea, lo que explica la respuesta del agente en T01. **Riesgo forward-looking:** al conectar la 2.ª línea (exigencia C-02), el agente dejaría de responder en ambas salvo que se vincule la línea o se active `allow_all_lines`.

## Sedes, tarifas y menú (C-03)

- Sede «Centro» activa, sin línea vinculada, **179 tarifas (179 activas)** — coincide con `operacion/tarifas-cargadas-sede-centro-2026-10-07.md`.
- Menú: 7 categorías (7 activas), 31 ítems (31 disponibles) — coincide con la carga verificada el 2026-09-28.

## Intenciones, plantillas, flags y automatizaciones

- Intención `pedir_menu` (`pedir-menu`) activa.
- Plantilla interna «Menú Friends Chicken» (`menu-friends-chicken`) activa, 3 pasos, `usage_count=0` (nunca enviada).
- Flags V2 activos: `automation_rule_builder_v2=true`, `automation_engine_v2_execute=true`.
- Automatizaciones: 4 en total (plantilla V1), **0 activas, 0 reglas V2**. Las secuencias de bienvenida/carta de `PLANTILLAS_WHATSAPP.md` siguen sin registrarse.

## Conclusiones

1. El parche de prompt autorizado está aplicado e íntegro (hash coincidente); falta su entrada en `PROGRESS.md` y la repetición controlada de T01.
2. `business_hours` ya está guardado; el prompt y el horario del tenant coinciden (domingo 09:00).
3. C-02 sigue sin acreditarse: 0 usuarios y 1 de 3 líneas.
4. Antes de conectar líneas adicionales, decidir vinculación del agente (línea específica o `allow_all_lines`) para no romper la atención automática.
5. Esta verificación acredita configuración, no comportamiento conversacional ni cierre de obligaciones.

**Fuente técnica:** `~/app.aricrm.co/current` en `waterfall`, release `9585614`; tablas `tenants`, `tenant_user_memberships`, `whatsapp_lines`, `ai_agents`, `branches`, `delivery_tariffs`, `menu_categories`, `menu_items`, `ai_intents`, `message_templates`, `tenant_messaging_features`, `automations` consultadas con campos minimizados; código `app/Services/AiAgentService.php` (solo lectura en `../velo_wa`).
