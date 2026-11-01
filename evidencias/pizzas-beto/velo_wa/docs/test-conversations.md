# Set de conversaciones de prueba — Beto's Pizza

Propuesta de datos sintéticos para pruebas del tenant **BETO'S PIZZA** en Waterfall/producción. Este documento **no ejecuta nada**: define los contactos, conversaciones y mensajes sugeridos, con los valores técnicos de cada campo para quien los quiera sembrar o simular.

## Contexto

| Dato | Valor |
|---|---|
| Tenant | BETO'S PIZZA (`01a0c569-e7a1-70f8-9ee8-c187f35b37ff`, slug `betos-pizza-2Ggr`) |
| Línea WhatsApp | Principal (`01a0c56b-6af9-73e1-bb71-ab57501739cb`, instancia `line_01a0c56b6af9`, teléfono `573122113446`) |
| Estado de la línea | `disconnected` desde 2026-10-07 ~04:04 UTC. No impide crear datos a nivel DB: los mensajes quedan como registros históricos, sin tráfico real de WhatsApp |
| Agente IA | Asistente de domicilios — plantilla (`01a10c00-ae04-7307-8e09-33b3b53088c7`) |
| Usuarios del tenant | Ninguno (sin membresías) → los outbound van con `sent_by = null` |

## Marcadores del set de prueba

Para que el set sea identificable, aislable y limpiable sin tocar datos reales:

- **Teléfonos**: rango ficticio `573001000011` … `573001000018` (prefijo no asignado a operadores reales).
- **`wa_id`**: `{teléfono}@s.whatsapp.net`.
- **`tags` del contacto**: `["test-data"]`.
- **`provider_conversation_id`**: `test-betos-01` … `test-betos-08`.
- **`provider_message_id` / `wa_message_id`**: `TESTBETOS0001`, `TESTBETOS0002`, … (nunca colisiona con IDs reales de WA, que son hex mayúscula).
- **`provider`**: `evolution` (igual que los mensajes reales del tenant).

## Resumen de escenarios

| # | Contacto | Escenario | Status final | Última actividad |
|---|---|---|---|---|
| 1 | Camila Torres | Pedido en curso, confirmado por asesor | `open` | hoy, hace ~1 h 30 min |
| 2 | Andrés Gómez | Cliente escribió y nadie ha respondido | `pending` | hoy, hace ~10 min |
| 3 | Marcela Ruiz | Reclamo por demora, resuelto | `closed` | ayer |
| 4 | Jorge Peña | Consulta de menú y horarios | `closed` | hace 2 días |
| 5 | Laura Méndez | Cliente frecuente pregunta por promoción | `closed` | hace 3 días |
| 6 | Daniel Vargas | Atendida por agente IA (automatizada) | `open` | hoy, hace ~41 min |
| 7 | Sofía Cardona | Nota de voz entrante con transcripción | `pending` | hoy, hace ~1 h |
| 8 | Felipe Castro | Conversación cerrada y reabierta por el cliente | `pending`, `reopen_count = 1` | hoy, hace ~20 min |

---

## Conversación 1 — Pedido en curso (`test-betos-01`)

**Contacto**: Camila Torres · `573001000011` · push_name "Camila"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hoy −2 h 00 | in | Buenas tardes 🍕 ¿Tienen domicilio en el barrio Los Alpes? |
| hoy −1 h 55 | out | ¡Hola Camila! Sí, llegamos a Los Alpes sin costo adicional. ¿Qué te apetece hoy? |
| hoy −1 h 50 | in | Una pizza pepperoni familiar y una gaseosa de 1.5 litros |
| hoy −1 h 45 | out | ¡Excelente elección! Pepperoni familiar $58.000 + gaseosa $8.500 = $66.500. Entrega en 35-40 minutos. ¿Confirmo a la dirección guardada (Cra 45 #12-30)? |
| hoy −1 h 40 | in | Sí, esa misma. A nombre de Camila Torres |
| hoy −1 h 30 | out | ¡Listo! Pedido #1042 confirmado ✅ Tu pizza sale en unos minutos. Te avisamos cuando el domiciliario esté en camino. |

**Campos de conversación**: `status = open` · `message_count = 6` · `first_message_at` = primer in · `first_response_at` = primer out · `last_message_at` = último out · `last_customer_inbound_at` = hoy −1 h 40 · `ai_agent_enabled = false`

---

## Conversación 2 — Sin responder (`test-betos-02`)

**Contacto**: Andrés Gómez · `573001000012` · push_name "Andrés"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hoy −25 min | in | Buenas noches, ¿hasta qué hora están abiertos hoy? |
| hoy −10 min | in | ¿Hola? |

**Campos de conversación**: `status = pending` · `pending_reason = "Esperando primera respuesta del asesor"` · `pending_since` = hoy −25 min · `message_count = 2` · `first_response_at = null` (nadie ha contestado) · `last_customer_inbound_at` = hoy −10 min

---

## Conversación 3 — Reclamo por demora (`test-betos-03`)

**Contacto**: Marcela Ruiz · `573001000013` · push_name "Marcela"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| ayer −6 h | in | Llevo casi una hora esperando mi pedido #1038 y nada. ¿Qué pasó? |
| ayer −6 h +4 min | out | Hola Marcela, disculpa la demora. Estoy verificando el estado de tu pedido con la tienda. |
| ayer −6 h +12 min | out | Tu pedido salió hace 10 minutos; el domiciliario tuvo un problema con la moto. Llega en máximo 15 minutos y te enviamos un 15% de descuento para tu próximo pedido 🙏 |
| ayer −6 h +50 min | in | Ok, gracias por la información |

**Campos de conversación**: `status = closed` · `closed_at` = ayer −4 h (auto-cierre, `closed_by = null`) · `message_count = 4` · `last_customer_inbound_at` = ayer −6 h +50 min

---

## Conversación 4 — Consulta de menú y horarios (`test-betos-04`)

**Contacto**: Jorge Peña · `573001000014` · push_name "Jorge"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hace 2 días | in | Buenas, ¿manejan pizza vegetariana? |
| hace 2 días +6 min | out | ¡Hola! Sí, tenemos la Vegetariana Suprema: champiñones, pimentón, cebolla, aceitunas y maíz. Personal $32.000, Mediana $45.000, Familiar $58.000. |
| hace 2 días +8 min | in | Perfecto, y ¿a qué hora abren los domingos? |
| hace 2 días +10 min | out | Los domingos abrimos de 12:00 m. a 9:00 p. m. 🍕 |
| hace 2 días +12 min | in | Gracias, más tarde les escribo para pedir |

**Campos de conversación**: `status = closed` · `closed_at` = hace 2 días +2 h · `message_count = 5`

---

## Conversación 5 — Cliente frecuente / promoción (`test-betos-05`)

**Contacto**: Laura Méndez · `573001000015` · push_name "Laura"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hace 3 días | in | ¡Hola! Vi que tienen promoción 2x1, ¿aún está vigente? |
| hace 3 días +3 min | out | ¡Hola Laura! Sí, el 2x1 en pizzas grandes aplica de martes a jueves hasta el final del mes. Solo domicilios y pedidos por este chat 🍕🍕 |
| hace 3 días +5 min | in | ¡Genial! Mañana jueves pido dos de pepperoni 🤤 |
| hace 3 días +7 min | out | ¡Te esperamos! Recuerda mencionar el código BETO2X1 al confirmar tu pedido. |

**Campos de conversación**: `status = closed` · `closed_at` = hace 3 días +3 h · `message_count = 4`

---

## Conversación 6 — Atendida por agente IA (`test-betos-06`)

**Contacto**: Daniel Vargas · `573001000016` · push_name "Daniel"

| Hora (relativa) | Dir | Mensaje | `is_automated` |
|---|---|---|---|
| hoy −45 min | in | Hola, quiero pedir una pizza mexicana familiar para la carrera 15 con 87 | — |
| hoy −44 min | out | ¡Hola! Soy el asistente de Beto's Pizza 🍕 La Mexicana familiar está en $62.000 y el domicilio a la Cra 15 con 87 tarda entre 30 y 40 minutos. ¿Te la confirmo? | `true` |
| hoy −42 min | in | Sí, confírmala. Pago contra entrega en efectivo | — |
| hoy −41 min | out | ¡Listo! Pedido confirmado ✅ Total: $62.000 + $4.000 de domicilio = $66.000, efectivo contra entrega. Llega en 30-40 minutos. | `true` |

**Campos de conversación**: `status = open` · `ai_agent_enabled = true` · `message_count = 4`
**Campos de mensajes out**: `is_automated = true` · `ai_agent_id = 01a10c00-ae04-7307-8e09-33b3b53088c7` · `sent_by = null`

---

## Conversación 7 — Nota de voz entrante (`test-betos-07`)

**Contacto**: Sofía Cardona · `573001000017` · push_name "Sofía"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hoy −1 h | in | 🎤 nota de voz (sin `body`) |

**Campos del mensaje in**: `media_type = "audio"` · `is_voice_note = true` · `body = null` · `transcription_status = "completed"` · `transcript = "Hola, buenas tardes. Quería saber si hacen pizzas mitad y mitad, una mitad hawaiana y la otra de pollo con champiñones, familiar. Y si me la pueden enviar a la calle 80 con 23."` · `media_url` puede quedar en `null` (no hay archivo real que descargar).

**Campos de conversación**: `status = pending` · `pending_reason = "Transcripción lista, esperando respuesta del asesor"` · `pending_since` = hoy −1 h · `message_count = 1` · `first_response_at = null`

---

## Conversación 8 — Cerrada y reabierta (`test-betos-08`)

**Contacto**: Felipe Castro · `573001000018` · push_name "Felipe"

| Hora (relativa) | Dir | Mensaje |
|---|---|---|
| hace 5 días | in | ¿Me mandan el menú? |
| hace 5 días +5 min | out | ¡Claro! Aquí va nuestro menú de hoy 🍕 (puedes usar `media_type = "document"` con `body = null` si quieres probar adjuntos) |
| hoy −20 min | in | Hola, ya revisé el menú. Quiero una pizza de la casa mediana, pero ¿pueden ser sin cebolla? |

**Campos de conversación**: `status = pending` · `reopen_count = 1` · `closed_at = null` (la reapertura la limpia) · `pending_reason = "Esperando respuesta del asesor"` · `pending_since` = hoy −20 min · `message_count = 3`

---

## Anexo técnico (para siembra)

Si alguien siembra este set en DB, tener en cuenta el comportamiento del modelo `Message`:

1. **Hook `Message::created`**: cada mensaje creado mueve el status de la conversación (`in` → `pending`, `out` → `open`; si estaba cerrada y entra un `in`, reabre con `reopen_count + 1`). Por eso el **status final y las métricas se fijan después del último mensaje**, no al crear la conversación.
2. **Índice único parcial**: solo puede existir una conversación `open`/`pending` por `(tenant_id, contact_id, whatsapp_line_id)`. Como cada contacto del set es nuevo y distinto, no hay conflicto.
3. **Índice único de mensajes**: `(tenant_id, provider, provider_message_id)` donde `provider_message_id IS NOT NULL`. Los IDs `TESTBETOS…` no colisionan con los reales (hex WA).
4. **Métricas manuales**: el hook no actualiza `message_count`, `first_message_at`, `first_response_at`, `last_message_at` ni `last_customer_inbound_at`; se setean a mano al final.
5. **Timestamps**: `created_at` es fillable en `Message` (permite backdate); `updated_at` se ajusta aparte si se quiere coherente.
6. **Estados de mensaje sugeridos**: in → `read` (o `delivered`); out → `delivered` o `read`. Evitar `pending` en outbound para que ningún job de reintentos los tome.
7. **Sin usuarios en el tenant**: `sent_by = null` en todos los out; el campo `last_advisor_response_at` de la conversación no se llena (solo aplica para out con autor humano).

### Criterios de limpieza

Todo el set se identifica con:

```sql
-- mensajes
DELETE FROM messages WHERE tenant_id = '01a0c569-e7a1-70f8-9ee8-c187f35b37ff'
  AND provider_message_id LIKE 'TESTBETOS%';
-- conversaciones
DELETE FROM conversations WHERE tenant_id = '01a0c569-e7a1-70f8-9ee8-c187f35b37ff'
  AND provider_conversation_id LIKE 'test-betos-%';
-- contactos
DELETE FROM contacts WHERE tenant_id = '01a0c569-e7a1-70f8-9ee8-c187f35b37ff'
  AND phone LIKE '57300100001%';
```
