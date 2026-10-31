# SECUENCIAS WHATSAPP — Indecente

Borrador de las "plantillas de respuesta" del programa para este establecimiento: dos secuencias de mensajes (bienvenida y carta) que las automatizaciones V2 envían al cumplirse su condición. Mecanismo, guardas y formato: `../../templates/PLANTILLAS_WHATSAPP.md`. **No configurar en producción sin aprobación** (`../../POLICIES.md`).

## Estado

- **Bloqueado**: la Cámara no ha entregado los datos de este beneficiario (ver tarea global P-002 y decisión 2026-09-12 en `../../DECISIONS.md`). Este borrador usa placeholders; no se puede validar copy ni definir contenido hasta tener nombre comercial, propuesta y canales confirmados.

## Secuencia 1 — Bienvenida (inicio de conversación)

**Regla V2**: disparador `Nueva conversación` → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | Hola {{name}} 👋 ¡Bienvenido a {NOMBRE_COMERCIAL}! {PROPUESTA}. Pide a domicilio o recoge en tienda. Escríbenos por aquí y te atendemos de una. |
| 2 | imagen (opcional) | 2s | Logo o foto del local — pendiente assets del establecimiento |

## Secuencia 2 — Carta (cuando el cliente la pide)

**Regla V2**: intención `pedir_menu` detectada por el agente IA → acción `Enviar secuencia`.

| Paso | Tipo | Delay | Contenido |
|---|---|---|---|
| 1 | texto | 0s | ¡Con mucho gusto! 🍽️ Aquí tienes la carta completa de {NOMBRE_COMERCIAL}. Para pedir, escríbenos por aquí lo que se te antoja y te confirmamos disponibilidad, precio y tiempo de entrega. |
| 2 | texto o imagen | 3s | La carta vigente — contenido pendiente (datos del beneficiario + caracterización) |

## Notas específicas del cliente

- Todos los campos de `CLIENTE.md` están vacíos a la espera de los datos de la Cámara. Completar este archivo junto con la caracterización (C-01).

## Checklist de configuración (workflow 03)

- [ ] Datos del beneficiario recibidos de la Cámara
- [ ] Copy validado con el establecimiento
- [ ] Contenido de la carta definido (texto o imagen) y cargado
- [ ] (Opcional) URL del menú digital en el texto de bienvenida
- [ ] Flags V2 (editor + ejecución) activos en el tenant
- [ ] Intención `pedir_menu` creada y activa
- [ ] Reglas V2 creadas (bienvenida + carta) y probadas con teléfonos controlados
- [ ] Evidencia en `evidencias/indecente/vertical-restaurantes/secuencias/`
