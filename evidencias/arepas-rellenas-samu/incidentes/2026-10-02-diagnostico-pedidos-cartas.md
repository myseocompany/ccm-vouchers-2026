# Diagnóstico — Cálculos erróneos de pedidos/domicilio, carta repetida y pedidos duplicados (piloto Samu)

**Fecha del diagnóstico**: 2026-10-02 (mismo día del reporte de Nicolás).
**Alcance**: piloto sede San Jorge — tenant `arepas-rellenas-samu-UK5K` (id `01a0ac93-dc1c-73e6-b872-b2c572070661`), línea 313 492 9669 (Evolution), agente IA «Asistente de domicilios — plantilla» (id `01a0f215-6eb7-7028-8cd2-e5dde36c7eec`, modelo `gpt-4o-mini`, `enabled_tools: get_contact, record_detected_intent, create_order`).
**Conversaciones reportadas por Nicolás**: `01a0fa55-27e8-71a7-9d17-4924d52c886f` y `01a0d0bc-cbe2-729e-9ec5-3141d0dfe12f`.
**Método**: consultas de solo lectura a producción (SSH `waterfall`, `php artisan tinker`): mensajes, `automation_runs`, `ai_intent_detections`, `orders`, `automations`, `ai_agents`. Este archivo no contiene datos personales: se citan únicamente identificadores técnicos.

## TL;DR

1. El agente IA **cobra mal**: 3 de 4 grupos de pedido reales tienen precios que no cuadran con el catálogo del propio prompt. Un cliente pagó **$10.000 de más** y Adrián tuvo que reembolsarle por Nequi desde su teléfono.
2. El agente **duplica pedidos**: 2 conversaciones con 2 órdenes cada una para el mismo pedido.
3. El agente **envía la carta repetidamente**: hasta 4 veces en 20 minutos a un mismo cliente, porque la intención `pedir_menu` se detecta con mensajes que no piden la carta y la regla V2 no tiene cooldown ni límite por conversación.
4. **Aclaración**: la conversación `01a0d0bc…` NO la atendió el agente (pausada por `ai_pause_reason=human_phone_takeover` desde que Adrián respondió por teléfono). El total «$31.000» de esa conversación fue cálculo manual de Adrián (la tabla del prompt da $32.000). No es bug del agente — pero evidencia que la tabla de tarifas solo la tiene el agente, no el humano.
5. El problema es **sistémico del piloto**, no puntual de las 2 conversaciones reportadas.

## Radio del problema (desde el arranque del piloto, 2026-09-30 ~16:00 UTC)

- 8 conversaciones nuevas atendidas; 6 pedidos creados por el agente; 19 detecciones de intención `pedir_menu`; 25 runs de automatización.
- Conversaciones con pedidos: `01a0f3cd…` (1 pedido), `01a0f442…` (2 pedidos), `01a0f50d…` (1), `01a0fa55…` (2).

## Hallazgo A — Precios y totales erróneos (agente IA)

Catálogo de referencia (del propio prompt del agente, `prompt-san-jorge-prod-v1.md`): arepa 1 ingrediente $12.000, 2 ingredientes $14.000, 3 $16.000, 4 $18.000, … 8 $22.000, con todo $23.000.

| Pedido | Conv. | Items (precio puesto por el LLM) | Total orden | Problema |
|---|---|---|---|---|
| PED-EGXYTZ (02:13:23) | `01a0fa55…` | 3 arepas de **2 ingredientes** a $16.000/$18.000/$18.000 | $52.000 | Catálogo: $14.000 c/u → productos $42.000. El propio resumen del agente decía «Arepa de 2 ingredientes». |
| PED-FC1OQF (02:16:44) | `01a0fa55…` | ídem | $58.500 | Mismos precios erróneos + domicilio ($6.500) **dentro del total** (semántica inconsistente con el pedido anterior). Total cotizado al cliente: $58.500 vs real $48.500 (42.000+6.500). **El cliente pagó $10.000 de más**; Adrián corrigió por teléfono («Perdón son $48.500», «Ya te envío los 10 mil») y reembolsó por Nequi. |
| PED-YF3GJ2 (10-01 01:29) | `01a0f50d…` | 1 arepa con ~8 ingredientes a $30.000 | $30.000 | Catálogo: 8 ingredientes $22.000 / con todo $23.000. Precio por encima de cualquier precio del catálogo. A verificar con Adrián si hubo acuerdo distinto. |
| PED-8OMVKB / PED-XMCRUT (09-30 21:50/21:54) | `01a0f442…` | «carne desmechada y huevo» (2 ing.) a $16.000 | $38.000 | Catálogo: 2 ingredientes $14.000. Además: pedido duplicado (ver Hallazgo B). |
| PED-SHVCE9 (09-30 20:15) | `01a0f3cd…` | «Arepa con todo» $23.000 ✓ | $27.000 | Item correcto, pero el total no cuadra con domicilio de Milán ($7.000 según tabla → esperado ~$30.000). Desviación a verificar. |

**Causa raíz (código, `velo_wa`)**: `App\Services\AiAgent\Tools\CreateOrderTool` acepta `price` por item y `total` directamente del LLM (`resolveTotal` solo suma lo que le mandan; sin catálogo, sin validación). El modelo `gpt-4o-mini` lee mal la tabla de precios del prompt y hace la aritmética él mismo. La tarifa de domicilio tampoco es un campo: el LLM la mete en `total` o en `notes` según el momento.

## Hallazgo B — Pedidos duplicados (agente IA)

- Conv `01a0f442…`: PED-8OMVKB (21:50:42) y PED-XMCRUT (21:54:38) — items idénticos, mismo pedido, 4 minutos aparte. Ambos quedaron `delivered`.
- Conv `01a0fa55…`: PED-EGXYTZ (02:13:23, sin domicilio) y PED-FC1OQF (02:16:44, con domicilio en el total) — el segundo se creó cuando el cliente preguntó «Cuánto sería con el domicilio».

**Causa raíz**: `create_order` no tiene idempotencia por conversación (nada impide crear N pedidos activos para el mismo pedido real) y el prompt no exige confirmación explícita del resumen final antes de registrar (el flujo definido sí lo exige, paso 7, pero el modelo chico lo salta: registró el pedido apenas recibió el nombre del cliente).

## Hallazgo C — Carta enviada demasiadas veces

En conv `01a0fa55…` el cliente recibió la carta **4 veces en 20 minutos**:

| Hora (UTC) | Origen | Detalle |
|---|---|---|
| 01:57:59 | Secuencia de bienvenida (regla `inicio de conversacion`, trigger `new_conversation`) | La bienvenida incluye la carta como imagen (diseño del piloto). |
| 02:10:38 | Regla `cliente_pide_carta` (trigger `ai_intent_detected`) | Disparada por el mensaje del cliente que pide **marcar** las arepas («Y me las puedes marcar»). Detección: «El cliente pide información sobre una arepa de dos ingredientes». |
| 02:13:21 | Regla `cliente_pide_carta` | Disparada cuando el cliente envió **su nombre**. Detección: «El cliente solicitó la carta». |
| 02:13:40 | Regla `cliente_pide_carta` | Disparada por «Cuánto sería con el domicilio». Detección: «El cliente solicitó el menú para ver los productos». |

Patrón repetido en otras conversaciones: `01a0f442…` 3 runs en 4 min (+ bienvenida); `01a0f3cd…` 4 detecciones en 40 min; `01a0f3ae…` 4 detecciones en 27 min. De las 19 detecciones totales, varias son falsos positivos evidentes («El cliente está iniciando la conversación», «ha manifestado interés en hacer un pedido y ha dado los ingredientes»).

**Causa raíz (doble)**:
1. La intención la reporta el propio LLM con la tool `record_detected_intent` (`App\Services\AiAgent\Tools\RecordDetectedIntentTool`): la descripción ya dice «solo si es clara», pero `gpt-4o-mini` sobre-dispara.
2. La regla V2 `cliente_pide_carta` (definición verificada en `automation_runs.definition_snapshot`) dispara `send_sequence` **sin condiciones, sin cooldown y sin límite por conversación** — el motor V2 hoy no soporta esas guardas (verificado en código: no existe ningún mecanismo de cooldown/once-per-conversation en el engine de automatizaciones; los cooldowns existentes son solo del safety de respuestas IA).

## Hallazgo D — Qué NO es bug del agente

- Conv `01a0d0bc…` (reportada): el agente nunca respondió — la conversación quedó pausada para IA por toma manual de Adrián (`ai_pause_reason=human_phone_takeover`), quien la atendió desde su teléfono WhatsApp (mensajes `is_automated=false`). El «$31.000» (2 arepas: $14.000+$12.000 + domicilio San Rafael $6.000 = $32.000 según tabla) fue error de cálculo manual humano, no del agente.
- Las imágenes/stickers de las 02:17–02:29 en conv `01a0fa55…` (comprobante del reembolso, etc.) también son de Adrián desde el teléfono.
- La pausa por toma humana (`human_phone_takeover`) funcionó correctamente: cuando Adrián respondió, el agente dejó de contestar.

## Riesgo activo

La línea está en producción con clientes reales (pedidos a la 1–2 AM). Mientras no aterricen los fixes, cada pedido tomado por el agente puede repetirse, cobrarse mal o ambos. Ya hubo un reembolso ($10.000). Mitigación inmediata posible sin código: quitar `create_order` de `enabled_tools` del agente (config reversible; el agente sigue con bienvenida, carta y toma de datos, pero el pedido lo crea un humano en el app).

## Tareas derivadas

- Global `TASKS.md`: **P-010** (guardas anti-repetición para reglas V2 por intención) y **P-011** (endurecer `create_order`: total server-side, `delivery_fee` separado, idempotencia, validación contra catálogo).
- `clientes/arepas-rellenas-samu/TASKS.md`: **INC-01** (mitigación), **INC-02** (config: prompt v2 + intención más estricta), **INC-03** (re-test end-to-end), **INC-04** (conciliación de cobros con Adrián).

## Fuente de la consulta

Producción AriCRM (`waterfall`, `~/app.aricrm.co/current`), 2026-10-02, solo lectura: tablas `conversations`, `messages`, `orders`, `automation_runs`, `ai_intent_detections`, `automations`, `ai_agents`; snapshots de reglas en `automation_runs.definition_snapshot`. Captura de salida completa del diagnóstico en poder del agente del harness (no se archivan datos personales).
