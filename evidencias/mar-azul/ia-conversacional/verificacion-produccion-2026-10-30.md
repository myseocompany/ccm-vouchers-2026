# Verificación de producción — Calamar Azul, 2026-10-30

Consulta de **solo lectura** por SSH a `waterfall` (`quaint-waterfall`), release desplegado `d4e3cf55`, Laravel 12.53. No se modificó ningún registro. Los scripts de consulta se borraron del servidor al terminar. Tablas consultadas con campos minimizados: `tenants`, `branches`, `delivery_tariffs`, `whatsapp_lines`, `ai_agents`, `tenant_user_memberships`, `menu_categories`, `menu_items`, `ai_intents`, `message_templates`, `automations`, `tags`, `contacts`, `conversations`, `orders`.

Los teléfonos autorizados del pilot mode no se transcriben (POLICIES: datos personales del cliente).

## Tenant

| Campo | Valor |
|---|---|
| id | `01a0fcc8-7908-71e0-ac67-c8aca5e05bf2` |
| name / slug | Grupo D Mar Azul SAS · `grupo-d-mar-azul-sas-LQ3L` |
| creado / onboarding | 2026-10-02 13:23:11 · completado 2026-10-02 13:24:26 |
| vertical | `restaurant` |
| `wa_status` | `connected` |
| timezone | `America/Bogota` |
| `business_hours` | los 7 días, 11:00–17:00 — coincide con `../../../clientes/mar-azul/CLIENTE.md` |
| `max_contacts` | **10.000** (el alcance contractual asigna hasta 2.000) |
| `max_agents` | 5 |

## Sedes y tarifas

| Sede | id | Activa | Tarifas |
|---|---|---|---|
| Sede Cable (`cable`, sort 1) | `01a14579-4916-7150-af8f-6f805542d8b1` | sí | 133/133 activas |
| Sede Centro (`centro`, sort 2) | `01a18e9a-26a8-7136-a92f-bd81bec466bd` | **no** | 133/133 activas |

Total 266, ninguna huérfana (`branch_id` nulo = 0). Ninguna sede tiene `whatsapp_line_id`.

El motivo de mantener Centro inactiva **sigue vigente** en el código desplegado: `GetDeliveryFeeTool` declara `branch_id` en `required` (línea 66) y `AiAgentService::injectBranchContext()` (línea 888 en producción, no 862 como citaba la evidencia del 2026-10-16) inyecta las sedes activas en cada turno.

## Línea de WhatsApp

Una sola: `Principal - Cable` (`01a0fcc8-ee74-71c9-af2c-53c385d2cf97`), `status=connected`, provider `evolution`, `is_default=true`, `connected_at=2026-10-30 02:53:30`, `ai_risk_level=normal`, sin pausa. **Corrige a `../../../clientes/mar-azul/CLIENTE.md`**, que declara las líneas «pendientes de titularidad y autorización»: hay una línea conectada y el agente está vinculado a ella.

## Agente IA

`Asistente Calamar Azul` (`01a14570-da52-70b4-b234-ba7b128d642a`), único agente del tenant.

| Campo | Valor |
|---|---|
| `is_enabled` | **`false`** |
| `updated_at` | 2026-10-30 21:29:32 |
| `is_default` | true |
| modelo | `gpt-4o-mini` |
| `tool_calling_enabled` | true |
| `whatsapp_line_id` | vinculado a `Principal - Cable` |
| `allow_all_lines` | false |
| `pilot_mode_enabled` | **true**, 3 teléfonos autorizados (6 entradas, dos formatos) |
| `enabled_channels` | `["whatsapp"]` |
| audio / imagen | ambos desactivados |
| `system_prompt` | 5.000 bytes · SHA-256 `4c21a8513155d9b8b1c0df3ba8f8b5c4789998d5a692b72a16bee5f0d3111f34` |

`enabled_tools` (12): `get_catalog`, `quote_order`, `create_order`, `get_delivery_fee`, `get_daily_menu`, `handoff_to_human`, `is_holiday`, `record_detected_intent`, `get_contact`, `update_contact`, `create_task`, `schedule_follow_up`. Más `daily_menu_tool_enabled: true`.

## Hallazgos

1. **`is_enabled = false`.** El agente no está respondiendo. La línea base `prompt-v5-recuperada-produccion-2026-10-30.md` registró `is_enabled = true` al momento de su captura; la desactivación ocurrió a las 21:29:32, después. El pilot mode nunca se abrió.
2. **Las herramientas sí están habilitadas.** El desfase de las 266 tarifas es exclusivamente del texto del prompt, que no nombra ninguna herramienta y sigue declarando las bandas placeholder de $5.000/$8.000/$12.000 más la frase «falta la tabla que asigna cada barrio a una banda».
3. **`is_holiday` es una herramienta muerta.** `IsHolidayTool` no existe en el release desplegado y el identificador no aparece en el código del agente. Hay que quitarlo de `enabled_tools`.
4. **Los metadatos de versión del prompt son falsos.** `config.prompt_version = v2-produccion-2026-10-16` y `config.prompt_sha256 = 9144893d…`, contra un prompt vivo cuyo SHA real es `4c21a851…`. Un lector que confíe en el metadato concluye que corre el v2.
5. **El tope de 4:30 p. m. no está en reservas.** El prompt sí contiene «4:30», pero es el corte de recepción de domicilios. La sección de reservas dice «se aceptan de lunes a sábado después de las 2:00 p. m.», sin tope, y no menciona eventos empresariales.
6. **La capa conversacional está vacía**: 0 `message_templates`, 0 `tags`, 0 `ai_intents`, 0 `automations`. El criterio de C-03 exige «plantillas y etiquetas activas».
7. **0 pedidos.** `orders = 0`: el criterio de C-03 «al menos un pedido y una reserva de prueba completados end-to-end» está incumplido, no solo pendiente de documentar.
8. **0 usuarios.** `tenant_user_memberships = 0`. C-02 exige 3 por invitación: incumplido.
9. **Catálogo completo pero sin imágenes.** 9 categorías activas y 92 ítems, todos disponibles; las 9 categorías coinciden una a una con `../../../clientes/mar-azul/carta/carta-whatsapp-2026-10-16.md`. Ningún ítem tiene `image_url`, pese a las 26 capturas archivadas.
10. **Hay tráfico real**: 179 contactos y 179 conversaciones, atendidos por personas (el agente está apagado).
