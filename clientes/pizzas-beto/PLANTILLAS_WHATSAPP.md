# SECUENCIAS WHATSAPP — Pizzas Beto

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v2 (2026-10-05). La carta PDF recibida confirma los precios de productos de la respuesta histórica. Pendiente: validación de vigencia de horario, disponibilidad y tarifa de domicilio antes de activar.

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | Gracias por comunicarte con Beto's Pizza. ¿Cómo podemos ayudarte? |
| 2 | texto | 1s | Porción: $10.000 (hawaiana o carnes) · Personal: $20.000 (4 porciones pequeñas) · Pizza S: $28.000 (6 porciones pequeñas) · Mediana: $55.000 (8 porciones pequeñas + gaseosa) · Familiar: $80.000 (8 porciones grandes + gaseosa). |
| 3 | texto | 1s | Maicitos: S $14.000 / M $18.000 · Lasaña mixta: S $15.000 / M $19.000. Domicilio reportado: $5.000; confirmaremos valor, disponibilidad y tiempo según tu zona. |
| 4 | imagen (opcional) | 2s | Carta visual móvil: `evidencias/pizzas-beto/vertical-restaurantes/menu/carta-betos-movil-v1-2026-10-05.png` |

Nota: los pasos 2 y 3 se basan en la conversación histórica y la carta PDF recibida. Antes de activar, confirmar que los precios y el domicilio siguen vigentes; si cambian por zona o disponibilidad, usar una herramienta de catálogo/tarifas vigente en vez de este texto fijo.

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes la carta de Beto's Pizza. Para pedir, escríbenos por aquí la pizza que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | imagen | 3s | Carta visual móvil: `evidencias/pizzas-beto/vertical-restaurantes/menu/carta-betos-movil-v1-2026-10-05.png` — usar solo tras confirmar vigencia con el establecimiento |

## Notas específicas del cliente

- (Sin notas por ahora.)

## Checklist de configuración (workflow 03)

- [ ] Copy validado con el establecimiento
- [ ] Contenido de la carta definido (texto o imagen) y cargado
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [x] Flags V2 (editor + ejecución) activos en el tenant — ver `PROGRESS.md`, 2026-10-05
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/pizzas-beto/vertical-restaurantes/secuencias/`
