# SECUENCIAS WHATSAPP — La Patateria

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v1 (2026-09-30). Pendientes: validación del copy con el establecimiento y contenido de la carta (caracterización).

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | Hola {{name}} 👋 ¡Bienvenido a La Patateria! Papas rellenas y snacks para todo el antojo: pide a domicilio o recoge tu orden. Cuéntanos qué quieres por aquí y te confirmamos disponibilidad y tiempo de entrega. |
| 2 | imagen (opcional) | 2s | Logo o foto del local — pendiente assets del establecimiento |

Nota: cuando exista menú digital, añadir el link al final del paso 1.

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes la carta completa de La Patateria. Para pedir, escríbenos por aquí la papa o el snack que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | texto o imagen | 3s | La carta vigente — contenido pendiente (caracterización); si es larga, dividirla en varios pasos por categoría |

## Notas específicas del cliente

- Sede de Manizales (Cra 23 # 75-75) en ruinas por el sismo. Verificar punto de operación actual en la caracterización antes de mencionar ubicaciones en el copy.

## Checklist de configuración (workflow 03)

- [ ] Copy validado con el establecimiento
- [ ] Contenido de la carta definido (texto o imagen) y cargado
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/la-patateria/vertical-restaurantes/secuencias/`
