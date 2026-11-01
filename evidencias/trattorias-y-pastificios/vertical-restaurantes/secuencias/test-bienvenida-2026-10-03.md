# Pruebas con teléfono controlado — secuencia de bienvenida (regla 1)

- **Fecha**: 2026-10-03 (pruebas ~08:26 y ~08:38 hora local, Colombia UTC-5).
- **Tenant**: `01a0c5d9-0f5c-73ba-b0ae-0e663da0507f` · slug `trattorias-y-pastificios-sas-q1Vz`.
- **Línea**: 310 482 3232 (se muestra en el chat del tester como `~Doyo-Milan`).
- **Teléfono controlado**: "My SEO Company".
- **Regla 1 — Bienvenida** (`new_conversation` → `send_sequence`, id `0b8ce31d-f838-4acf-9eb7-2bde3636a9e4`): paso 1 texto 0s (bienvenida/sismo, sin link), paso 2 texto 2s (link `https://menupp.co/doyoyono`).

## Hallazgo — prueba 08:38 (definitiva)

```
[3/10/26, 8:38:08] My SEO Company: hola
[3/10/26, 8:38:16] ~Doyo-Milan: Hola My SEO Company 👋 Gracias por escribirnos. Como bien sabes, nuestros locales sufrieron por el terremoto y por ahora estamos a domicilio exclusivamente, hasta nuevo aviso. Te compartimos nuestra carta y te ayudamos a armar tu pedido.   ← paso 1
[3/10/26, 8:39:34] ~Doyo-Milan: Aquí tienes la carta: https://menupp.co/doyoyono — Para pedir, escríbenos por aquí lo que se te antoja (incluido el «arma tu poke» 🥗) y te confirmamos disponibilidad, precio y tiempo de entrega. Domicilios en Manizales y Villamaría.   ← paso 2
```

- **Ambos pasos se entregaron.** `NewConversation` → `send_sequence` **funciona** sobre la línea Evolution. (Rectifica las lecturas previas de este documento.)
- **Issue 1 — retardo del paso 2:** llegó ~78 s después del paso 1 (08:38:16 → 08:39:34), no los 2 s configurados. El paso 1 (delay 0s) salió ~8 s tras el `hola`; el paso 2 (delay 2s) salió ~86 s tras el `hola`.
- **Issue 2 — doble mensaje:** en este run **no** llegó respuesta libre del agente (sin doble mensaje). Queda como riesgo abierto (`suppresses_ai_reply` sin paridad V2).

### Prueba 08:26 (anterior, descartada como ruido)
- En la primera prueba (~08:26) se reportó "solo el primero" y se observó una respuesta genérica del agente. La prueba 08:38 muestra que la secuencia entrega ambos pasos; el 08:26 pudo ser conversación no-nueva o un run interrumpido. Se conserva como antecedente.

## Chat de prueba del agente (UI `app.aricrm.co/settings/ai-agent`)

- El usuario reporta que **en el chat de prueba del agente (UI de AriCRM) las secuencias no funcionan** (no aparece la bienvenida ni el link).
- **Inferencia**: ese chat de prueba ejercita el **prompt/intenciones/tools del agente**, no el **motor de automatizaciones V2**. Los disparadores `NewConversation` y `AiIntentDetected` se emiten sobre mensajes inbound reales en `HandleInboundMessage`, no en el sandbox de UI → las secuencias no disparan ahí. **Para probar secuencias hay que usar la línea real** (como se hizo a las 08:38). A confirmar leyendo el código en `velo_wa` (referencia solo lectura, permitida por POLICIES).

## Causa del retardo del paso 2 (confirmada en código `velo_wa`, 2026-10-03)

**No es un cron ni el `delay_seconds` (2 s).** Es el **cooldown de seguridad entre mensajes automatizados** de `AiAgentSafetyService::reserveOutboundSlot`:

- Cada paso, al ejecutarse, llama a `reserveOutboundSlot($conversation, …)`. Esta calcula `conversationDelay = conversation_cooldown_seconds - segundosDesdeUltimaRespuesta` cuando la conversación tiene `ai_last_reply_at` reciente, con `conversation_cooldown_seconds` = **60** (default) y le suma `random_int(0, max_reply_jitter_seconds)` con jitter default **0-15 s**. El resultado se aplica como `->delay()` al `SendWhatsAppMessage` (`SendAutomationSequenceStep` líneas 76/114-117).
- Paso 1 (primera respuesta, sin `ai_last_reply_at` previo): `conversationDelay=0` + jitter 0-15 → sale rápido (~8 s observado). Fija `ai_last_reply_at`.
- Paso 2 (segunda respuesta, `ai_last_reply_at` acaba de fijarse): `conversationDelay ≈ 60` + jitter 0-15 → **~60-75 s** de retardo adicional. Sumado al `delay_seconds=2` → ~78 s observados. Encaja.
- Es protección anti-burst (heurística de baneo de WhatsApp): espacia los mensajes automatizados de una conversación.

**Implicación para el arreglo:**
- Poner el paso 2 a `delay_seconds=0` **no arregla nada**: el cooldown (60 s) domina, no el delay del paso.
- **Fusionar los dos pasos en un solo mensaje** (un solo outbound) sí arregla: no hay segundo `reserveOutboundSlot` → sin cooldown entre mensajes. **Recomendado.**
- Alternativa: bajar `conversation_cooldown_seconds` en `ai_safety_config` de la línea, pero afecta **todo** el comportamiento del bot (no solo secuencias) → riesgoso, no recomendado.

## Descartado

- **No es deploy de `send_sequence`**: verificado en producción 2026-09-30 (release `396ea59`, salud 200, 0 migraciones pendientes — `MEMORY.md`). El stale "pendiente deploy" de `templates/PLANTILLAS_WHATSAPP.md` ya se corrigió.
- **No son los flags V2**: activos desde 2026-10-03.
- **No es que `NewConversation` no dispare**: la prueba 08:38 confirma que dispara y entrega ambos pasos.

## Lectura a producción (SSH `waterfall`, solo lectura, 2026-10-03)

`automation_runs` de la regla 1 (id `0b8ce31d-…`): 2 runs, ambos `success`, trigger `new_conversation`.

Run más reciente `01a10201-…` (13:43 UTC = 08:43 local), conversación `01a10201-9b4c-…`:
- `2026-10-03 13:43:38` in (HUMAN) `hola`
- `2026-10-03 13:43:42` out (AUTO) — **un solo mensaje automatizado** (no dos)

Cuerpo del mensaje automatizado en producción (texto plano):
```
Hola My SEO Company 👋 Gracias por escribirnos.
Por ahora estamos a domicilio exclusivamente, hasta nuevo aviso ya que nuestros locales sufrieron por el terremoto.
Te compartimos nuestra carta y te ayudamos a armar tu pedido.
https://menupp.co/doyoyono
Para pedir, escríbenos por aquí lo que se te antoja (incluido el «arma tu poke» 🥗) y te confirmamos disponibilidad, precio y tiempo de entrega.
Domicilios en Manizales y Villamaría.
```

**Conclusiones confirmadas:**
- El usuario **fusionó los dos pasos en un solo mensaje** (un outbound). Ya no hay segundo `reserveOutboundSlot` → sin cooldown. El mensaje llega en **~4 s** (13:43:38 → 13:43:42). Retardo resuelto. ✅
- El copy fue reescrito (sismo condensado). Usa el **link general** `https://menupp.co/doyoyono` (no los específicos de DOYO/ONO).
- Run status `success`. `NewConversation` → `send_sequence` confirmado end-to-end en producción.

## Pendiente (siguientes pasos)

1. ~~Cambiar el link general por los dos links etiquetados~~ **Hecho (2026-10-03, con aprobación)**: swap ejecutado en la acción `send_sequence` `01a10201-3061-73ff-bc71-381479e530f4`, verificado por relectura del `config`. Pendiente: re-probar con teléfono controlado y validar el copy con Paulo/Ángela.
2. Validar el copy completo (sismo + carta + cobertura) con Paulo/Ángela antes de abrir a clientes.
3. (Cierre) archivar captura del chat como evidencia en `evidencias/trattorias-y-pastificios/assets/`.
