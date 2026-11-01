# Perfil de baja latencia — agente Sushi Fusion

Fecha de aplicación: 2026-10-29 10:09 UTC<br>
Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)<br>
Línea: `principal` (`01a140ba-7d7a-7256-8e40-97a6c6cc5e4f`, instancia `line_01a140ba7d7a`)<br>
Agente observado: `01a18263-c04e-73c3-95a4-d3395049c907`

## Configuración aplicada

El override vive en `whatsapp_lines.ai_safety_config` y afecta únicamente esta línea:

- `message_buffer_seconds`: `0`
- `conversation_cooldown_seconds`: `0`
- `max_reply_jitter_seconds`: `0`
- `min_reply_delay_seconds`: `0`
- `max_reply_delay_seconds`: `0`
- `max_per_minute_per_line`: `30`
- `per_minute_refill_rate`: `30`
- `hourly_auto_limit`: `200`
- `max_parallel_ai_conversations`: `10`

El token bucket se reinicializó con 30 tokens. No se cambiaron el prompt, modelo, tools, takeover humano, deduplicación, opt-out ni las comprobaciones de riesgo.

## Verificación real

Línea emisora controlada: My SEO Company. Conversación: `01a18462-7479-72fc-ab0f-f507adce6fb3`.

- Primer smoke: todavía heredó una reserva futura creada antes del cambio; 44 s entre inbound y outbound. No representa el perfil nuevo.
- Segundo smoke limpio: enviado a Evolution a las `10:10:49`, inbound persistido `10:10:50`, webhook recibido `10:10:52`, generación iniciada tras encolar `10:10:55` y outbound persistido `10:10:57`.
- Latencia observada: 8 s envío→respuesta y 7 s inbound→respuesta.
- Log de seguridad: `line_delay_seconds=0`, `conversation_delay_seconds=0`, `effective_jitter_seconds=0`, `final_delay_seconds=0`; generación OpenAI `2.14 s`.

La latencia restante corresponde al tránsito Evolution/webhook y al procesamiento/generación real, no a esperas artificiales configuradas por AriCRM.

## Rollback

Para volver a los defaults, dejar `whatsapp_lines.ai_safety_config` en `null` para esta línea. Los defaults actuales son buffer 15 s, cooldown 60 s, jitter máximo 15 s, bucket 3/min y límite horario 20.
