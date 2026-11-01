# SECUENCIAS WHATSAPP — DOYO & ONO (Trattorias y Pastificios S.A.S.)

Borrador de las "plantillas de respuesta" del programa para este establecimiento: secuencias de mensajes de WhatsApp que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v2 (2026-10-03), redactado para las marcas **DOYO & ONO** a partir del formulario, la entrevista y la carta extraída de MenuApp (`../../evidencias/trattorias-y-pastificios/carta-menupp-2026-10-03.md`). Sustituye al borrador v1 (KOMO, 2026-09-30).
- **Reglas V2 configuradas en producción el 2026-10-03** (bienvenida + carta), con el agente IA habilitado. Ver `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/reglas-v2-2026-10-03.md`. Pendiente: prueba con teléfonos controlados y validación del copy.
- **Por ahora se trabaja con una sola línea** (decisión operativa 2026-10-03); las 3 del alcance quedan disponibles.
- Pendientes: validar el copy con el establecimiento, decidir qué link de carta envía la secuencia según la marca (ver notas) y confirmar la dirección (discrepancia Cámara vs. MenuApp).

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`. Tono neutro/jovial. Incluye contexto del sismo (el cliente opera a domicilio por reapertura parcial).

> **Estado en producción (2026-10-03, verificado por SSH)**: la regla está **fusionada en un solo paso** (un mensaje) — el usuario lo cambió tras la prueba 08:38. Esto resuelve el retardo: dos pasos separados disparaban el cooldown de seguridad entre mensajes automatizados (`conversation_cooldown_seconds`=60 + jitter 0-15 → ~60-75 s en el segundo, confirmado en código `AiAgentSafetyService::reserveOutboundSlot`). Con un solo mensaje llega en ~4 s. El copy envía **ambos links etiquetados** (DOYO + ONO).

| Paso | Tipo | Delay | Contenido (en producción) |
|---|---|---|---|
| 1 | texto | 0s | Hola {{name}} 👋 Gracias por escribirnos.\n\nPor ahora estamos a domicilio exclusivamente, hasta nuevo aviso ya que nuestros locales sufrieron por el terremoto.\n\nTe compartimos nuestra carta y te ayudamos a armar tu pedido.\n\n🍜 DOYO: https://menupp.co/doyoyono/venue/EXcbqaaTTqnFRvHrnN4p/menu/bPE7JKxW9DcspjFnDPPL\n🥗 ONO: https://menupp.co/doyoyono/venue/HL0hbbttgdQVfSFhSfnf/menu/tsFpduQ47fZCV6LkKkzn\n\nPara pedir, escríbenos por aquí lo que se te antoja (incluido el «arma tu poke» 🥗) y te confirmamos disponibilidad, precio y tiempo de entrega.\n\nDomicilios en Manizales y Villamaría. |

> **Swap ejecutado en producción (2026-10-03, con aprobación)**: link general `doyoyono` reemplazado por los dos links etiquetados (DOYO + ONO) en la acción `send_sequence` `01a10201-3061-73ff-bc71-381479e530f4` de la regla de bienvenida. Verificado por relectura del `config`. Pendiente: re-probar con teléfono controlado y validar el copy con Paulo/Ángela.

Notas:
- Links específicos por marca (fuente: `../../evidencias/trattorias-y-pastificios/menu-menupp-2026-10-03.md`). El general `doyoyono` queda como fallback.
- **Validar el copy con Paulo/Ángela** antes de abrir a clientes (copy nuevo + links por marca).
- La **promoción/bono** (ej. $2.000 en el primer pedido) queda **pendiente**: el cliente quiere primero que el bot funcione antes de promocionar (no hacer promesas falsas).
- Si se vuelven a separar en 2 pasos, el segundo llegará con ~60-75 s de retardo por el cooldown de seguridad (no por el `delay_seconds`); poner el delay a 0 no lo evita.

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes nuestra carta. Para pedir a domicilio, escríbenos por aquí lo que se te antoja (incluido el «arma tu poke» 🥗) y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | texto | 2s | https://menupp.co/doyoyono |

Notas:
- Si la carta es por marca, usar el link específico de DOYO o de ONO según la línea/conversación.
- La secuencia solo entrega la carta; la **captura del pedido (armado, dirección, teléfono, método de pago) y el cierre (cobro y domicilio)** son conversacionales y terminan en **humano (Ángela)**.

## Qué hace el agente vs. qué escala (resumen)

- **Agente IA**: presentar la carta, resolver FAQs (¿tienen domicilio?, ¿a partir de qué hora?, ubicación, horarios), orientar el armado del poke y tomar **pedido + dirección**.
- **Escala a Ángela Bedoya (mismo chat)**: quejas, alergias, pagos, cambios, reclamos, eventos/catering, y el **cierre del pedido** (cobro y domicilio).
- **Eventos**: el agente ofrece «Pregúntanos aquí por nuestros eventos» y escala.
- **Reservas**: no se ofrecen en el beneficio (aunque MenuApp las tenga habilitadas).

## Notas específicas del cliente

- **Decisión de marca abierta**: el beneficiario es el grupo Trattorias y Pastificios S.A.S. (KOMO, ONO, DOYO). El formulario y la entrevista son para **ONO/DOYO** con la línea 310 482 3232. Si la línea atiende varias marcas, se replica este par de secuencias por marca y cada regla se dispara según la línea de la conversación.
- **Tono**: neutro, jovial. No usar un tono temático «oriental».
- **Pagos** (fuente entrevista): Bold, Datáfono Bancolombia, transferencia y Bre-B; **no** efectivo a domicilio. (MenuApp muestra efectivo: config desactualizada — ver discrepancias en la carta.)
- Probar las reglas con teléfonos controlados antes de abrir el flujo a clientes reales.

## Checklist de configuración (workflow 03)

- [ ] Marca(s) de la línea WhatsApp decidida(s) con el establecimiento
- [ ] Copy validado con el establecimiento (Paulo / Ángela)
- [ ] Link de carta confirmado por marca (general por ahora)
- [x] Flags V2 (editor + ejecución) activos en el tenant — 2026-10-03
- [x] Intención `pedir_menu` creada y activa — 2026-10-03
- [x] Agente IA habilitado (requerido por el disparador `AiIntentDetected` de la carta) — 2026-10-03
- [x] Reglas V2 creadas (bienvenida + carta) en producción — 2026-10-03 (falta probar con teléfonos controlados)
- [x] Evidencia en `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/`
