# Verificación en producción: prompt del agente vs. lo pactado — 2026-10-05

> **Uso interno del harness.** No incluye credenciales ni contenido de conversaciones de clientes finales.

- **Fecha**: 2026-10-05 (lectura).
- **Método**: SSH `waterfall` → `php artisan tinker` sobre `~/app.aricrm.co/current`. **Solo SELECT / lectura**; cero escrituras.
- **Alcance**: verificar que la configuración del agente IA en producción corresponde a lo pactado en la reunión con el establecimiento (transcripción: `../reunion-revision-bot-2026-10-03.md`).
- **Tenant**: `01a0c5d9-0f5c-73ba-b0ae-0e663da0507f` · slug `trattorias-y-pastificios-sas-q1Vz`.

## 1. Agente IA (`ai_agents` `01a101af-1bf1-737b-a4bc-d8d03a883e83`)

| Campo | Valor en producción | ¿Corresponde a lo pactado? |
|---|---|---|
| `is_enabled` | `true` | ✅ |
| Línea | `whatsapp_line_id=null` + `config.allow_all_lines=true` | ✅ «que esté en todas las líneas» (reunión) |
| `llm_model` | `gpt-4o-mini` | ✅ «GPT 4 mini» (reunión; subible) |
| `context_messages` | `20` | ✅ «20 hacia atrás» (reunión) |
| `system_prompt` | 7945 chars, actualizado `2026-10-03 16:04:03` (hora del servidor) | ver §2 |
| `config.prompt_version` | `v1-trattorias-doyo-ono` | ⚠️ desactualizado: el contenido ya es solo-ONO (v1.1); versionar |
| `config.source_prompt` | `evidencias/.../prompt-v1.md` | ⚠️ la evidencia v1 quedó atrás del contenido en producción |

## 2. Prompt (`system_prompt`) vs. lo pactado — texto exacto en `prompt-v1.1-solo-ono-2026-10-03.md`

**Corresponde (✅):**

1. «Eres el asistente virtual de *Ono*» — **solo ONO**; DOYO eliminado del encabezado y del catálogo (pactado: omitir DOYO, dejar solo ONO).
2. Catálogo ONO completo y validado en reunión: 9 pokes (Caribe $34, Acevichado $30, Bahía $40, Orange $39, Paisa $30, Teriyaki $30, Veggie $28, Honolulu $36, Kraskí $34) + «Arma tu Poke» (bases / 13 proteínas / toppings hasta 4 / salsas hasta 5) + Poke Pork Belly marcado no disponible (confirmado por Paulo: sin producción).
3. Link de la carta = **link específico de ONO** (`menupp.co/doyoyono/venue/HL0hbbttgdQVfSFhSfnf/menu/tsFpduQ47fZCV6LkKkzn`, coincide con el link ONO registrado en `../menu-menupp-2026-10-03.md`).
4. Escalamiento general a **Ángela Bedoya** (mismo chat); **Eventos/catering escala a Steven** (pactado: Steven para órdenes especiales/muy grandes).
5. Pagos: Bold, Datáfono Bancolombia, transferencia y Bre-B; sin efectivo a domicilio; el agente no cobra.
6. Horarios L-V 11:30–15:00 y 18:00–22:00; sáb 11:30–22:00; dom 11:30–20:40; festivos cerrado.
7. Cobertura Manizales/Villamaría; flota tercerizada; tarifas pendientes → no inventar valores, pedir barrio y escalar.
8. Entrega ~30 min (sin prometer exacto); sin reservas.
9. Flujo pactado íntegro: intención → link → armado (incluye arma tu poke) → producto/variante → alergias («sin maní») → resumen → datos/barrio/dirección → cobertura → **no cobra ni pide método de pago** → pasa a Ángela.
10. Tono/formato: español colombiano, neutro-jovial, de tú; bloques cortos; 1–2 preguntas; emojis definidos; asteriscos simples; sin tablas/JSON/Markdown/rutas.

**Residuos a corregir (⚠️, no cambian el comportamiento esencial):**

1. Texto interno desactualizado: «Link **general** (una sola línea atiende **ambas marcas**):» precede al link de ONO — el link ya es el específico de ONO; corregir la etiqueta.
2. Contradicción menor en catering: la sección «Eventos/catering» escala a **Steven**, pero la lista de «Escalamiento obligatorio» incluye «eventos o catering» bajo **Ángela**. En la reunión Paulo dijo catering→Ángela y Steven para órdenes especiales muy grandes; unificar criterio.
3. Sección «Puntos abiertos (a resolver antes de producción)» sigue DENTRO del prompt del LLM — es nota interna (doble mensaje, tarifas, discrepancias, marca por línea); retirarla del prompt y dejarla en evidencia.
4. Artefactos de sanitización: secuencias escapadas (`\$`, `\+`, `\*\*`) y el fragmento roto «\*\* escala\*\*» en el paso 4 del flujo.
5. `config.prompt_version` sigue `v1-trattorias-doyo-ono` y `source_prompt` apunta al v1 — versionar como v1.1/v2-solo-ono al próxima edición.

## 3. Reglas V2 (bienvenida y carta)

| Regla | Trigger | Activa | Contenido (acción `send_sequence`, 1 paso, `delay_seconds=0`) | Verificado |
|---|---|---|---|---|
| `0b8ce31d-…` «Bienvenida — DOYO & Ono» (acción `01a10283-…`, upd. 2026-10-03 16:06:05) | `new_conversation` | ✅ | Sismo + carta + **solo link ONO** (🥗) + domicilio Manizales/Villamaría | ✅ corresponde (nombre de la regla residual, ver residuos) |
| `518c6f82-…` «Carta — DOYO & Ono» (acción `01a10284-…`, upd. 2026-10-03 16:06:34) | `ai_intent_detected` | ✅ | Carta + **solo link ONO** | ✅ corresponde (nombre residual) |

- Ambas con `suppresses_ai_reply=false` — el punto abierto del doble mensaje sigue vigente (vigilar en la re-prueba).
- Las 4 automatizaciones «Plantilla - …» siguen inactivas (esperando decisión).

## 4. Línea e intención

- `whatsapp_lines` `01a0c5dc-…`: `status=connected`, `provider=evolution`, `ai_risk_level=normal`, sin pausa IA (upd. 2026-10-03 16:09:31). ✅
- `label=Dojo` ⚠️ residual (typo de DOYO y además ya debería decir ONO). El **icono/foto de perfil** de WhatsApp no se gestiona desde AriCRM: se cambia desde el teléfono, como se pactó con Steven.
- `ai_intents`: `pedir-menu` activa (upd. 2026-10-03 12:47:02). ✅ dispara la secuencia de carta.

## 5. Conclusión

**El prompt y las secuencias en producción SÍ corresponden a lo pactado en lo esencial** (solo ONO, link ONO, flujo, catálogo validado, escalamiento Ángela+Steven, configuración 20 mensajes / gpt-4o-mini / todas las líneas). Quedan residuos cosméticos/de higiene (nombres de reglas «DOYO & Ono», label «Dojo», etiqueta «Link general… ambas marcas», contradicción menor de catering, «Puntos abiertos» y escapes dentro del prompt, versionado de config) que conviene limpiar en la próxima edición con aprobación. Esta verificación es de **configuración almacenada**, no de entrega de mensajes: la re-prueba con teléfono controlado y las 5 conversaciones de C-04 siguen pendientes.

## 6. Nota sobre la fecha de la reunión

Los cambios pactados (prompt solo-ONO 16:04:03; acciones de bienvenida/carta 16:06:05 y 16:06:34; línea 16:09:31 — hora del servidor, 2026-10-03) contienen decisiones que solo pudieron originarse en la reunión (escalamiento a Steven, omisión de DOYO). Por ello la reunión se fechó como **2026-10-03 por la tarde**; la transcripción se recibió y registró el 2026-10-05.
