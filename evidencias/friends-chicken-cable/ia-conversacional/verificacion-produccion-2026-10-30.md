# Verificación de producción — Friends Chicken, 2026-10-30

Consulta de **solo lectura** por SSH a `waterfall` (`quaint-waterfall`), release desplegado `d4e3cf55`, Laravel 12.53. No se modificó ningún registro. Los scripts de consulta se borraron del servidor al terminar.

Esta verificación se hizo junto con la de Calamar Azul para comparar ambos tenants: `../../mar-azul/ia-conversacional/verificacion-produccion-2026-10-30.md`.

El tenant_id fue aportado por Nicolás en sesión; **no estaba registrado en ningún archivo del repositorio** antes de esta verificación.

## Tenant

| Campo | Valor |
|---|---|
| id | `01a0a5a4-1cda-7099-bfe7-c993e6f1352b` |
| name / slug | Friends Chicken · `friends-chicken-uHMR` |
| creado / onboarding | 2026-09-15 15:16:31 · completado 2026-09-15 15:24:07 |
| vertical | `restaurant` |
| `wa_status` | `connected` |
| `business_hours` | lun–sáb 11:00–19:30; dom 09:00–17:00 — coincide con la evidencia del 2026-10-07 |
| `max_contacts` | **10.000** (el alcance contractual asigna hasta 2.000) |

## Sedes y tarifas

Una sola sede: `Centro` (`01a11688-80dd-708f-ab11-a51086d72b5b`), activa, sort 1, sin `whatsapp_line_id`, **179/179 tarifas activas**. No existe una sede Cable en producción, consistente con el cierre físico de esa sede.

## Línea de WhatsApp

Una sola: `Principal` (`01a0a5aa-35d7-73ee-a0c9-29cb248d40b2`), `status=connected`, provider `evolution`, `is_default=true`, `connected_at=2026-10-30 00:44:50`, `ai_risk_level=normal`.

## Agente IA

`Asistente de domicilios — plantilla` (`01a0af94-108c-7296-ab4a-534b85acac4e`), único agente del tenant.

| Campo | Valor |
|---|---|
| `is_enabled` | **`true`** |
| `updated_at` | 2026-10-28 23:23:37 |
| `is_default` | **false** |
| modelo | `gpt-4.1` |
| `tool_calling_enabled` | true |
| `whatsapp_line_id` | NULL, con `allow_all_lines = true` |
| `purpose` | `restaurant_delivery_reference` |
| `source_prompt` | evidencias/tenant-patron/prompts/agente-domicilios/v1-prompt-generico.md (ruta literal del `config`, resuelve en `velo_wa`, no en este repo) |
| `prompt_version` | `v5-fc-cobertura-escala-2026-10-25` (desde `v4-fc-tono-whatsapp-2026-10-09`) |
| `prompt_published_at` | 2026-10-25T17:51:26Z |
| `system_prompt` | 13.140 bytes · SHA-256 `5224eb33…`, **coincide** con `config.prompt_sha256` |
| audio / imagen | ambos **activados** |

**No existe la clave `enabled_tools`.** Según `AiAgentService::effectiveEnabledTools()` (comentario en la línea 1255 del release desplegado), un `enabled_tools` nulo significa «todas las herramientas del registry», salvo `get_daily_menu`, que es opt-in y aquí no está activado. El agente tiene por tanto más herramientas disponibles que el de Calamar Azul, no menos.

## Hallazgos

1. **La bitácora está tres semanas atrasada.** `../../../clientes/friends-chicken-cable/PROGRESS.md` documenta hasta `v1-fc-menu-snapshot-2026-10-07`. Producción corre `v5-fc-cobertura-escala-2026-10-25`, y el `config` registra el linaje intermedio `v4-fc-tono-whatsapp-2026-10-09`. Dos versiones de prompt sin entrada.
2. **El prompt ya referencia las herramientas**: `get_delivery_fee`, `get_catalog`, `quote_order` y `create_order` aparecen en el texto. La conclusión de la evidencia del 2026-10-07 —«el agente no cuenta con herramienta de consulta de menú ni base de conocimiento vinculada»— quedó obsoleta. **T01 debe repetirse**: pudo haberse corregido y nadie lo ha vuelto a probar.
3. **El prompt dice «Friends Chicken no acepta reservas».** La entrada de `../../../clientes/friends-chicken-cable/PROGRESS.md` del 2026-09-30 registra lo contrario: reservas con abono de $50.000 no reembolsable, consumible en tres meses. Una de las dos afirmaciones es falsa y hay que resolverlo con el establecimiento.
4. **El agente en producción se identifica como plantilla de referencia** (`purpose: restaurant_delivery_reference`, `source_prompt` apuntando al prompt genérico del tenant patrón) y tiene `is_default = false`. Confirmar si operar sobre el agente genérico parchado es intencional.
5. **El riesgo de la segunda línea está mitigado.** La evidencia del 2026-10-07 advertía que al conectar la 2.ª línea el agente dejaría de responder, por `whatsapp_line_id` nulo con `allow_all_lines=false`. Hoy `allow_all_lines = true`: el riesgo ya no aplica.
6. **El prompt nombra una responsable operativa y dos números de escalamiento** que no corresponden al contacto principal de `../../../clientes/friends-chicken-cable/CLIENTE.md`, donde los contactos técnico y administrativo siguen en «pendiente». Los datos no se transcriben acá (POLICIES). La ficha del cliente está incompleta frente a lo que ya opera.
7. **0 pedidos.** `orders = 0`: el criterio de C-03 «al menos un pedido y una reserva de prueba completados end-to-end» está incumplido.
8. **0 usuarios.** `tenant_user_memberships = 0`. C-02 exige 3 por invitación: incumplido.
9. **Capa conversacional parcial**: 1 `ai_intent` activa, 1 `message_template` activa, 10 `tags`, 5 `automations` de las cuales **solo 1 está activa**.
10. **Catálogo sin imágenes.** 7 categorías activas y 31 ítems disponibles; ningún ítem tiene `image_url`, lo que confirma que las 16 fotografías archivadas nunca se mapearon.
11. **Volumen**: 856 contactos y 726 conversaciones — 43% del tope contractual de 2.000 contactos.
