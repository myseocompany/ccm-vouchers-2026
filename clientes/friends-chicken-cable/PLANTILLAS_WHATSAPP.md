# SECUENCIAS WHATSAPP — Friends Chicken

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v1 (2026-09-30). Pendientes: validación del copy con el establecimiento y contenido de la carta (catálogo en carga, C-03 en progreso).

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | Hola {{name}} 👋 ¡Bienvenido a Friends Chicken! El pollo crujiente de siempre, listo para domicilio o recoger. Escríbenos tu pedido por aquí y te confirmamos disponibilidad y tiempo de entrega. |
| 2 | imagen (opcional) | 2s | Logo o foto del local — pendiente assets del establecimiento |

Nota: cuando exista menú digital, añadir el link al final del paso 1.

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes la carta completa de Friends Chicken. Para pedir, escríbenos por aquí lo que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | texto o imagen | 3s | La carta vigente (septiembre 2026) — catálogo estructurado en carga; si es larga, dividirla en varios pasos por categoría |

## Notas específicas del cliente

- **Referencia para la réplica**: el tenant de producción de Friends Chicken ya tiene la intención `pedir_menu` activa y los flags V2 (editor + ejecución) habilitados. El piloto del flujo se hace en Arepas Rellenas Samu (decisión 2026-09-30); este cliente es el siguiente candidato natural.
- La carta vigente está en `evidencias/friends-chicken-cable/vertical-restaurantes/menu/menu-friends-chicken-2026-09.pdf`; el catálogo estructurado se está cargando (C-03 en progreso, ítems sin activar hasta completar el catálogo).
- Sede Cable cerrada por el sismo; operación consolidada en la sede del centro. No incluir direcciones en el copy mientras la operación esté en transición.

## Checklist de configuración (workflow 03)

- [ ] Copy validado con el establecimiento
- [ ] Contenido de la carta definido (texto o imagen) y cargado
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/friends-chicken-cable/vertical-restaurantes/secuencias/`
