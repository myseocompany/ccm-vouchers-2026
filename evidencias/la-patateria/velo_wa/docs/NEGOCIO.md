# La Patatería — el negocio y su bot

Perfil consolidado del tenant y del agente IA. Referencia operativa completa (IDs, runbook, pendientes): [`README.md`](./README.md). Actualizado: 2026-10-12.

## Quién es La Patatería

Restaurante de **papas rellenas y snacks** de Manizales, Caldas (NIT 1088011076). Su carta mezcla lo criollo con lo mexicano y lo texano: entradas para picar (molcajete guacamole, nachos, papas de la casa), sopas, pollo y lomo "alrededor del mundo", **hamburguesas en pan de papa**, pizzas grandes, picadas para compartir y bebidas — 46 productos en 8 categorías, vendidos también por su tienda en línea (`https://patateria.bibisoft.co/tienda`).

**Historia reciente que define su operación:** la sede histórica de Manizales (Cra 23 # 75-75) quedó **en ruinas por el sismo**, con pérdida total de infraestructura. El negocio operó desde un punto temporal en la zona Milán/Circunvalar (Tv 72 #16-54) y mantiene un segundo punto en **Pereira**. La **reapertura del local de Manizales** (Cra 23 # 75-48) fue reportada para el **14 de octubre de 2026**.

**Sedes actuales:**

| Sede | Ubicación | Notas |
|---|---|---|
| Manizales | Cra 23 # 75-48 | Local de la reapertura (confirmado 2026-10-12) |
| Pereira | Avenida Circunvalar #5-83, frente al Parque Arboleda | Confirmada 2026-10-12 (edición en línea) |

**Gente:**

- **Propietario:** Jorge Eduar Zapata de los Ríos (Eduar) — `eduarzapatadelosrios@gmail.com`, 318 209 9420. Usuario AriCRM del tenant.
- **Segundo usuario del equipo:** **Otman David Hernandez Zea** — `ohernandez@unal.edu.co` (creado y verificado en producción el 12-oct 13:14, durante la reunión). Junto con Eduar, destino de las notificaciones de escalamiento ("responde el que esté en turno").
- **Líder de Servicio al Cliente reportado en la caracterización:** Javier Quinchía (sin usuario; su rol operativo lo asume David).

**Contrato:** beneficiario del programa de vouchers digitales 2026 (gestión MY SEO para la Cámara de Comercio). Alcance contratado: hasta 3 usuarios AriCRM, 3 líneas WhatsApp, 2.000 contactos.

**Operación conocida** (fuentes: caracterización 2026-10-12, corpus de 250 conversaciones y **respuestas del dueño al cuestionario 2026-10-12** — integradas en el prompt v7):

- **Apertura del local de Manizales** (Cra 23 # 75-48): martes 13 de octubre de 2026 desde las 6:00 p. m. La ubicación afectada por el sismo ya no se menciona.
- **Horario:** L-J 12:00–21:00, V-S 12:00–22:00 (cierre 10 p. m. confirmado), D 12:00–20:00. Tabla por sede sin respuesta.
- **Reservas:** sin costo. Mismo día sí, si se piden *antes del mediodía* (después → walk-in u otro día). Última hora: L-J y domingo 7:30 p. m., V-S 8:00 p. m. La mesa se retiene 10 minutos. Grupos hasta 15 (mayores → equipo). El bot registra *solicitud recibida* — nunca dice "reserva confirmada"; el equipo confirma cuando está abierto.
- **Cumpleaños son el motor:** 84 menciones en 9 días. Decoración gratis en todas las sedes para cumpleaños, grados, aniversarios y eventos empresariales: centro de mesa con bombas + postre de cortesía al homenajeado. Torta propia permitida; alcohol solo el del restaurante.
- **Menú del día:** L-V sin festivos, 12:00–2:00 p. m., solo consumo en el punto, $25.500 con bebida (pendiente reconfirmar). Rotación de 15 menús que avanzan solo L-J sin festivos; el viernes es siempre cazuela de frijoles; reinicia tras el 15. El dueño enviará los 15 menús para cargarlos en el menú digital.
- **Domicilios:** Pereira solo por Rappi (enlace oficial `rappi.com.co/restaurantes/900074543-la-patateria`); Manizales sin domicilio. Recogida en ambas sedes; preparación ~30 minutos.
- **Promociones:** promo de hamburguesas (el cliente la llama 2x1; precio especial: dos hamburguesas + dos bebidas + una porción) en la categoría hamburguesas clásicas, ambas sedes, martes y jueves de 3:00 p. m. al cierre. Bono de reconstrucción ya no se vende (los existentes se redimen sin condiciones → equipo). Convenio corporativo → humano. Sin otras promos (festival de hamburguesas la próxima semana).
- **Pagos:** en punto: efectivo, datáfono, tarjetas y QR (transferencias no); domicilios/recogidas: en línea o efectivo. Facturación: actualizar datos en `app.bibisoft.co/register-clients?company_id=55` y solicitar de nuevo.
- **Mascotas** permitidas sin condiciones. **Contactos:** quejas/cobros → Eduard y David · CVs/proveedores/prensa → 318 426 72 02.
- **Volumen del canal:** ~27 conversaciones nuevas/día con picos de almuerzo (11:00–14:00) y noche (17:00–21:00). Antes del bot, la primera respuesta sustantiva tardaba una mediana de 39 minutos y ~14 hilos morían sin respuesta.

## Qué hace el bot: "Reservas La Patatería"

Agente conversacional (**gpt-4.1-mini**) que atiende el WhatsApp del negocio (+57 324 688 7353, línea "Principal"). Su personalidad es ***buena papa con picardía*** 🥔 — la regla de oro del marcaje: *"Somos buena papa con la gente y nos tomamos muy en serio las papas"*. Cercano e informal paisa (sin caricaturizar), con un juego de palabras de papas como máximo cada cuatro mensajes y **cero humor** en quejas, cobros, errores o situaciones delicadas. Mensajes cortos y formato WhatsApp.

**Su trabajo, en orden de prioridad:**

1. **Reservas de mesa, de punta a punta.** Pregunta la ciudad cuando importa (puerta de ciudad, como hacía el equipo), recopila los datos (ciudad, nombre, celular, correo opcional, día, hora, personas, ocasión), resume, pide confirmación explícita y **crea la reserva en el sistema** — queda confirmada con código y el cliente recibe el QR por el mismo chat. La reserva queda asociada a la sede correcta (una unidad reservable por ciudad) con "Sede: …" en las notas. Reglas: sin costo, solo días futuros (mismo día → atención por orden de llegada), última hora 7:30 p. m., grupos de hasta 15.
2. **Carta y platos.** Explica qué lleva cada plato y su precio desde su base de conocimiento (la carta versionada del 2026-10-12, 46 fuentes por producto), identifica platos en fotos, informa el menú del día y las bases disponibles (papa en cascos, puré, francesa y criolla). **No arma pedidos ni cotiza**: para pedir siempre envía el link de domicilios (`https://linktr.ee/LaPatateriaDomicilios`).
3. **Cumpleaños.** Registra la ocasión y las preferencias en la reserva; confirma decoración gratis (globos), brownie de cortesía y torta propia.
4. **Información por sede.** Ubicación (Manizales Cra 23 # 75-48 / Pereira Av. Circunvalar #5-83 frente al Parque Arboleda), horarios, domicilios (solo Pereira por Rappi), mascotas, 2x1 solo Pereira (martes y jueves).

**Lo que NO hace — siempre pasa al equipo humano** (con contexto): quejas y PQR, pagos/cobros/facturación electrónica, cambios y cancelaciones de reservas (las ubica con `find_reservation` y deriva), alergias sin ficha confirmada, grupos de más de 15, eventos y cotizaciones, promociones/bonos/convenios, empleo, proveedores y prensa, y cualquier dato que no tenga confirmado — nunca inventa.

**Cómo está construido** (detalle técnico en el README):

- Tools: `create_appointment`, `find_reservation`, `update_contact`, `handoff_to_human` (+ `record_detected_intent` automático).
- Base de conocimiento "Carta La Patatería" (46 productos, versión 1 publicada, 3 chunks embebidos).
- 22 intenciones sembradas para analítica y futuras automatizaciones.
- Prompt versionado con SHA-256: activa **v5-precision-carta-2026-10-12** (`prompts/reservas/`); configuración idempotente vía `php artisan patateria:configure-agent`.
- El sistema le inyecta fecha/hora actual y calendario de 14 días (no alucina fechas) y las sedes activas por turno.

## Fuentes

- Ficha y caracterización del establecimiento: `ccm-vouchers-2026/clientes/la-patateria/` (`CLIENTE.md`, `CARACTERIZACION.md`).
- Análisis del canal: `exports/patateria-01a0cb62/` (`analisis-faq-agente-ia-2026-10-12.md`, `analisis-opencode.md`, `PREGUNTAS_PENDIENTES_DUENO.md`).
- Carta versionada: `docs/patateria/carta/carta-2026-10-12.md` (extracción bibisoft store_id=63, menu_id=12).
