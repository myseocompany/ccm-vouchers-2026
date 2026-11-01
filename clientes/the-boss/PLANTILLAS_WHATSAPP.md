# SECUENCIAS WHATSAPP — The Boss Burger

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v1 (2026-10-31). Pendientes: validación del copy con el establecimiento (Diego) y activación de flags V2 en el tenant. El contenido de la carta ya existe y está verificado.
- **Ya activa en producción (verificado 31-oct):** la automatización `enviar_menu` (disparador `new_conversation`) envía la bienvenida con la carta en cada conversación nueva — pre-check del guion de pruebas (`../../evidencias/the-boss/ia-conversacional/MENSAJES_PRUEBA_2026-10-31.md`). Las secuencias V2 de este borrador son evolución pendiente de aprobar; al configurarlas, no duplicar la bienvenida ya activa.

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Qué más! 👋🍔 ¡Bienvenido a *The Boss Burger*! Hamburguesas al horno de brasa, hechas con calma y actitud. Pide a domicilio o recoge en Alta Suiza. Escríbenos por aquí y te atendemos de una. |
| 2 | imagen (opcional) | 2s | Logo o foto del local — pendiente assets del establecimiento |

Nota: cuando exista menú digital, añadir el link al final del paso 1. El catálogo ya vive en el tenant (`get_catalog`); definir con el establecimiento si la bienvenida incluye el link o solo el ofrecimiento.

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con gusto! 🍔🔥 Aquí va la carta completa de *The Boss Burger*. Para pedir, escríbenos por aquí lo que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | texto o imagen | 3s | La carta vigente: 6 categorías, 23 productos (`../../evidencias/the-boss/vertical-restaurantes/menu/carta-the-boss-2026-10-11.md`). Si va como texto, dividirla por categoría (Burgers, Sandwich del Boss, Papitas del Boss, Pinchos del Boss, Adiciones, Bebidas) |

## Notas específicas del cliente

- Voz de marca «Street Boss»: urbana, directa, cercana; «¡Qué más!» como saludo; 1–2 emojis por mensaje (🍔 🔥 🛵 📍). Fuente: `../../evidencias/the-boss/ia-conversacional/prompt-v2.md` (sección «Tono y estilo de marca») y destilado completo en `../../evidencias/the-boss/ia-conversacional/street-boss-ai-v1-voz-copy.md`.
- No usar términos de promoción no verificados (sold out, best seller, VIP, gratis) ni prometer rapidez; el tiempo de entrega del domicilio depende de Flash Delivery.
- Los lunes no hay servicio: la bienvenida no debe prometer atención inmediata fuera del horario (mar–jue 18:00–22:00; vie–dom 17:00–22:00).
- El agente IA del tenant ya atiende pedidos con el prompt v2.7; estas secuencias V2 son complementarias y no deben duplicar ni contradecir las respuestas del agente.

## Checklist de configuración (workflow 03)

- [ ] Copy validado con el establecimiento
- [x] Contenido de la carta definido (texto o imagen) y cargado — catálogo en producción (31 ítems al 31-oct) y bienvenida con carta activa vía `enviar_menu`
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/the-boss/vertical-restaurantes/secuencias/`
