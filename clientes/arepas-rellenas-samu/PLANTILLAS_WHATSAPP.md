# SECUENCIAS WHATSAPP — Arepas Rellenas Samu

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- Borrador v1 (2026-09-30). Pendientes: confirmar cuál línea es la de San Jorge, carta corregida por Adrián y validación del copy.
- **Piloto del programa, acotado a la sede San Jorge** (decisión de Nicolás, 2026-09-30): el primer agente envía el menú como bienvenida — réplica automatizada de la práctica actual del negocio («al primer mensaje envían imagen del menú»). El aprendizaje se replica a los demás locales.

## Prerrequisitos del piloto (estado al 2026-09-30)

| # | Prerrequisito | Estado |
|---|---|---|
| 1 | Acción `send_sequence` en producción | ✓ Deploy verificado 2026-09-30: release activo `396ea59`, `/up` y `/login` en 200, manifest de assets OK, 0 migraciones pendientes |
| 2 | Línea WhatsApp de San Jorge operativa | ✓ Confirmada en la práctica: 313 492 9669 se muestra como «~Arepas Rellenas Samu San Jorge» (etiqueta «Principal», conectada, Evolution, agente asignado). Pendiente formalizar con Adrián |
| 3 | Flags V2 (editor + ejecución) activos en el tenant | ✓ Activos en el tenant de **prueba** `restaurante-domicilios-v1` y en el tenant **real** de Samu (`arepas-rellenas-samu-UK5K`) — verificados 2026-09-30 (`editor_v2=1 engine_v2_execute=1`) |
| 4 | Intención `pedir_menu` creada y activa | ✓ Ya existía activa en el tenant de Samu (slug `pedir-menu`, verificada 2026-09-30); creada también en el tenant de prueba con la misma condición («el cliente solicita conocer el menú o la carta») |
| 5 | Carta de San Jorge (imagen) | ✓ `carta-san-jorge-2026-09-30.png` montada en el CDN público de AriCRM y cableada en la secuencia `enviar_carta`. Pendiente: diseño corregido por Adrián (número) |
| 6 | Copy validado con el establecimiento (Adrián) | Pendiente |
| 7 | Agente IA habilitado (requerido por el disparador `AiIntentDetected` de la carta) | ✓ Habilitado por Nicolás, asignado a la línea San Jorge, tool calling activo; prompt de producción limpio (`prompt-san-jorge-prod-v1.md`) instalado 2026-09-30 |

## Secuencia 1 — Bienvenida = envío del menú (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`. Réplica automatizada de la práctica actual (carta automática al primer mensaje); el cliente confirma después su pedido con dirección, teléfono y método de pago (flujo que ya manejan).

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | Hola {{name}} 👋 ¡Bienvenido a Arepas Rellenas Samu — sede San Jorge! Te compartimos nuestra carta. Para pedir a domicilio, escríbenos por aquí lo que se te antoja. |
| 2 | imagen | 2s | Carta vigente de San Jorge (con tocineta) — pendiente el diseño corregido por Adrián |

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes nuestra carta. Para pedir, escríbenos por aquí la arepa que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega (30–50 min según zona; domicilios en Manizales y Villamaría). |
| 2 | imagen | 2s | Carta vigente de San Jorge (con tocineta) — mismo asset del paso 2 de la bienvenida |

## Notas específicas del cliente

- Dirección aún por confirmar (dato inicial Cámara: Cr 10 # 9-30): no incluir dirección en el copy hasta verificarla.
- Dos sedes en el alcance (confirmado por Sandra de la Cámara en la caracterización; formalizar por escrito). El piloto es **solo San Jorge**; Chipre se configura después con el mismo aprendizaje.
- La caracterización definió: «Carta entrenamiento IA: usar carta actualizada de San Jorge (con tocineta)» — el piloto no espera la unificación de menús de la semana del 2026-10-06.
- Bebidas no se incluyen en domicilios (se derraman/enfrían): no promoverlas en el copy.
- La secuencia solo entrega la carta; la captura de datos del pedido (dirección, teléfono, método de pago) sigue siendo conversacional (agente/humano), como en su flujo actual.
- Probar las reglas con teléfonos controlados antes de abrir el flujo a clientes reales.

## Checklist de configuración (workflow 03)

- [ ] Línea de San Jorge confirmada con Adrián
- [ ] Copy validado con el establecimiento
- [ ] Carta de San Jorge (imagen corregida por Adrián) cargada en ambas secuencias
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/arepas-rellenas-samu/vertical-restaurantes/secuencias/`
