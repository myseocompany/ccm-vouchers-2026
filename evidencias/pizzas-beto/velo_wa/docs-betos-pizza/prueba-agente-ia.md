# Plan de pruebas — Agente IA de Beto's Pizza

**Fecha:** 2026-10-25
**Estado:** Borrador
**Alcance:** Validación funcional y operativa del agente IA de Beto's Pizza (playground + smoke test por WhatsApp) antes de darlo por operativo en producción.

---

## 1. Datos del agente

| Campo | Valor |
|---|---|
| Tenant | Beto's Pizza — `<!-- tenant_id (UUID) -->` |
| Línea WhatsApp | `line_01a0c56b6af9` (instancia Evolution, webhook vía gateway `hooks.aricrm.co`) |
| Número de la línea | `<!-- +57 ... -->` |
| Agente IA | `<!-- nombre + UUID del agente -->` |
| Modelo / provider | `<!-- ej. gpt-4o-mini / OpenAI -->` |
| System prompt (fuente versionada) | `docs/betos-pizza/prompts/<agente>/v1-<descripcion>.md` |
| KB vinculada | `<!-- nombre de la KB publicada, o "ninguna" -->` |

> **Completar antes de ejecutar.** Los IDs se consultan en Waterfall (`ssh waterfall`) con `php artisan tinker` desde la release activa, o en la UI de superadmin.

## 2. Prerrequisitos

- [ ] Línea `line_01a0c56b6af9` conectada (estado `open` en Evolution).
- [ ] Agente IA creado, habilitado y `is_default` en la línea.
- [ ] System prompt publicado y snapshot versionado en `docs/betos-pizza/prompts/` (regla de versionado de `AGENTS.md`).
- [ ] API key del provider configurada y con cuota.
- [ ] (Si aplica) KB publicada y vinculada al agente.
- [ ] Número de prueba disponible (teléfono personal, nunca un cliente real).
- [ ] Acceso a la inbox del tenant para observar conversaciones en vivo.

## 3. Cómo ejecutar las pruebas

### 3.1 Playground (sin WhatsApp real) — primera pasada

**Settings → Agente IA → panel "Probar agente".**

- No crea `Conversation` ni `Message`, no envía nada por WhatsApp, no toca el flujo productivo.
- **Sin fallback de provider**: si falta la API key o hay un 429, se ve el error real (no una respuesta silenciosa de otro provider).
- El historial vive solo en el navegador; el botón "Limpiar" lo vacía.
- Cada envío consume tokens del LLM (limiter de 20/min por tenant).

Ejecutar aquí los casos **F1–F10** de la sección 4 antes de tocar WhatsApp.

### 3.2 WhatsApp real (smoke test) — segunda pasada

Desde el número de prueba, escribir al número de la línea y ejecutar de nuevo **F1–F10** más los casos **S1–S6** de la sección 5.

Advertencias específicas de esta línea:

- **Alto volumen**: la línea de Beto's es una de las que más mensajes genera (~392/h en hora pico, muchos de grupos). Probar fuera del pico para no competir con tráfico real.
- **Backlog de cola serial**: la cola de la instancia drena ~1 lote/min; si la línea se reconectó hace poco puede haber backlog de 15–20 min. Un mensaje de prueba puede tardar en llegar a AriCRM — eso no es un bug del agente.
- **Warmup**: si el agente acaba de habilitarse, el daily cap del día 1 es bajo (~20–40 respuestas IA) y puede abortar con `daily_cap_exceeded`. No forzar respuestas manuales en bucle (lección Botanazo).

## 4. Casos de prueba funcionales

| # | Escenario | Mensaje de ejemplo | Resultado esperado | OK |
|---|---|---|---|---|
| F1 | Saludo inicial | "Hola" | Saluda, se presenta como Beto's Pizza y ofrece ayuda (menú/pedidos) | ☐ |
| F2 | Menú | "¿Qué pizzas tienen?" | Lista solo productos reales del menú; no inventa sabores | ☐ |
| F3 | Precios | "¿Cuánto cuesta la pizza hawaiana grande?" | Precio exacto según menú/KB; no estima | ☐ |
| F4 | Pedido completo | "Quiero una pepperoni mediana a la calle 123 #45-67, pago contra entrega" | Recopila producto, tamaño, dirección, teléfono y pago; confirma resumiendo el pedido | ☐ |
| F5 | Pedido incompleto | "Quiero una pizza" | Pregunta por lo que falta (tamaño, dirección) en vez de confirmar a ciegas | ☐ |
| F6 | Horario | "¿Abren hoy? ¿A qué hora?" | Horario real del negocio; **día de la semana correcto** (ver S1) | ☐ |
| F7 | Domicilio | "¿Llegan a mi barrio? ¿Cuánto vale el envío?" | Cobertura y costo de envío reales; si no tiene el dato, dice que va a confirmar | ☐ |
| F8 | Promociones | "¿Tienen promociones hoy?" | Solo promos vigentes; no inventa descuentos | ☐ |
| F9 | Fuera de alcance | "¿Venden hamburguesas?" (si no venden) | Dice que no, sin alucinar; redirige a lo que sí ofrece | ☐ |
| F10 | Escalamiento humano | "Quiero hablar con una persona" | Cede la conversación, avisa que atiende un humano; deja la conv marcada para revisión | ☐ |

## 5. Casos de comportamiento y seguridad (lecciones Botanazo)

Fuente: incidentes reales del agente de Botanazo (`docs/specs/AI_AGENT_BOTANAZO_ONBOARDING_SPEC.md`).

| # | Escenario | Cómo probar | Resultado esperado | OK |
|---|---|---|---|---|
| S1 | Fecha/hora correcta | Preguntar "¿qué día y hora es?" | Día de la semana, fecha y hora correctos (COT). El prompt estático hace que el LLM invente la fecha — si falla, falta inyección de `now()` en el prompt | ☐ |
| S2 | Takeover humano | Responder a mano desde la inbox | La conv queda con IA desactivada (`human_phone_takeover`); el bot no vuelve a responder ahí | ☐ |
| S3 | Réplicas consecutivas | Enviar 5+ mensajes seguidos sin respuesta humana | A las 5 réplicas aparece `consecutive_threshold_reached` y `needs_human_review = true` (es un flag, no un kill switch — comportamiento correcto) | ☐ |
| S4 | Daily cap / warmup | Observar durante una sesión de pruebas larga | Si se excede el cap: `flush_aborted abort_reason=daily_cap_exceeded` y el bot calla (sin crash). No forzar respuestas en bucle | ☐ |
| S5 | Duplicados | Forzar una respuesta manual justo después de una del bot | `reply_skipped reason=duplicate_auto_reply` — no se envía dos veces el mismo mensaje | ☐ |
| S6 | Conv preexistente | Escribir desde un número que ya tenía conversación abierta antes de habilitar el agente | En convs preexistentes el bot puede arrancar apagado — verificar el toggle y prender a mano si aplica | ☐ |

## 6. Verificación técnica post-prueba

Desde Waterfall (release activa):

```bash
# Eventos del agente en la ventana de pruebas
grep -E "ai_safety|ai_takeover" storage/logs/laravel.log | tail -50

# Errores de provider (429, timeouts, keys)
grep -iE "provider|openai|anthropic|gemini" storage/logs/laravel.log | grep -i error | tail -20
```

En la inbox del tenant:

- [ ] Las conversaciones de prueba aparecen con las respuestas del bot en tiempo razonable (< 30 s en condiciones normales).
- [ ] Ninguna conversación de cliente real recibió contenido de las pruebas.
- [ ] El toggle de IA por conversación refleja el estado esperado (apagado tras takeover).

## 7. Criterios de aprobación

El agente se da por **aprobado** cuando:

1. F1–F10 pasan en playground y en WhatsApp real.
2. S1 pasa sin alucinación de fecha (o el hallazgo queda documentado con ticket).
3. S2–S5 se comportan según lo esperado (sin dobles envíos, sin respuestas tras takeover).
4. No hay errores de provider ni aborts inesperados en `laravel.log` durante la ventana de pruebas.

Cualquier fallo se registra en la sección 8 con evidencia (captura del chat + líneas de log).

## 8. Registro de ejecución

| Fecha | Ejecutado por | Ambiente (playground / WhatsApp) | Casos ejecutados | Resultado | Hallazgos |
|---|---|---|---|---|---|
| | | | | | |

---

## Referencias

- `docs/specs/AI_AGENT_BOTANAZO_ONBOARDING_SPEC.md` — lecciones de onboarding del agente de Botanazo (fuente de S1–S6).
- `docs/AI_AGENT_PLAYGROUND_PLAN.md` — diseño del playground (sin fallback, sin persistencia).
- `docs/incidents/LLM/ACTIVE-INCIDENT.md` — riesgos conocidos de la línea `line_01a0c56b6af9` (backlog de cola serial, reconexiones).
- `AGENTS.md` — regla de versionado de prompts (`docs/<tenant>/prompts/<agente>/v<N>-<descripcion>.md`).
