# CARACTERIZACION — Sushi Fusion (Compañía de Restaurantes Sushi S.A.S.)

Obligación 2 del contrato. Identificar necesidades del establecimiento respecto a atención al cliente, gestión de menú, pedidos y reservas. Se hace UNA vez al inicio y sirve como línea base.

Fuente del método: `../../workflows/01_caracterizacion.md`.

Fuente de datos: formulario de caracterización (9 bloques) respondido por el establecimiento (`../../evidencias/sushi-fusion/formulario-caracterizacion-2026-10-20.csv`) y reunión de caracterización/onboarding del 2026-10-20 (transcripción en `../../evidencias/sushi-fusion/reunion-caracterizacion-2026-10-20.md`).

Estado: levantamiento preliminar 2026-10-20; los campos no reportados se marcan «pendiente por confirmar (2026-10-20)».

## 1. Operación actual

- Aforo y turnos: horario de atención al público lunes a sábado 12:00 m – 9:30 pm; domingo 12:00 m – 9:00 pm. Se maneja **aforo para reservas**.
- Volumen diario aproximado de pedidos (sitio / domicilio / recogida): pendiente por confirmar (2026-10-20).
- Ticket promedio y estacionalidad: pendiente por confirmar (2026-10-20).
- Días y horarios de mayor demanda: pendiente por confirmar (2026-10-20).
- Tiempo promedio de respuesta actual y volumen de conversaciones/día: pendiente por confirmar (2026-10-20).

## 2. Atención al cliente

- ¿Quién responde WhatsApp hoy? El equipo del punto; el responsable operativo y receptor de escalamientos es Carlos Mauricio Villa Sánchez (está capacitando al equipo).
- Herramientas actuales: **WhatsApp Business** (una sola línea; tenía ~4 dispositivos vinculados), página web con cartas, cartas en PDF por marca.
- Tipos de mensaje que reciben (pedido, reserva, queja, información): pedidos, información (cartas/domicilio/horarios) y reservas. Detalle y volumen pendiente por confirmar (2026-10-20).
- Lógica de venta actual (clave para el agente): **asesoría por componentes / "psicología de consumo"**. El vendedor guía al cliente porque muchas veces no racionaliza lo que busca. Flujo observado:
  1. Definir **tipo de plato**: ¿sushi / ceviche / arroz / pasta / hamburguesa / perro?
  2. **¿Con mariscos o sin mariscos?** (predomina pescado/mariscos, pero hay alternativas pollo/res/cerdo/chicharrón en todas las cartas).
  3. **Proteína**: camarón, pescado, mariscos, pollo, res, cerdo.
  4. **Preparación / sabor**: colombiana / japonesa / peruana; agridulce / ácido / cremoso / picante, según gusto.
  - Ejemplos de la carta usados en la reunión: ceviches (primavera cremoso peruano, suero costeño colombiano, tradicional leche de tigre peruano); arroces Tepán (Japón, "todo aparte", múltiples sabores) vs Thai (mezclado, un sabor); arroces al queso peruanos (parmesano/mozzarella/holandés); chaufa; arroces colombianos (marinero).

## 3. Menú

- ¿Menú digital existente? Formato: sí — **PDF por marca** (4 marcas) + carta de **bebidas**; también publicado en **página web** y enviado por link. Decisión: el agente enviará cartas (PDF o link) y/o asesorará sobre ellas.
- Nº aproximado de productos / categorías: **~400 productos** en total entre las 4 marcas (reto grande de cobertura declarado por el establecimiento).
- Cambia con qué frecuencia: pendiente por confirmar (2026-10-20). Productos agotados/rotativos y cómo se marcan: pendiente por confirmar (2026-10-20).
- Fotos disponibles: sí (dentro de los PDF).
- Precios definidos y públicos: sí.
- **Problema de los PDF**: pesan ~12 MB (están en resolución de impresión) → lentos para WhatsApp. **Acción**: el establecimiento generará versión de **baja resolución / menor tamaño** manteniendo buena visualización (lo hace el propio establecimiento, no la agencia).
- **Dualidad mesa vs domicilio** (riesgo para el agente): existen cartas y precios distintos para mesa y para domicilio (ej. línea de domicilio "Sushi House" con combos promocionales 30k–100k; arroces familiares/medianos ~3 personas/personales). Hay productos con el **mismo nombre y distinto precio** (p. ej. chaufa personal vs familiar; una es Inca Fusion, otra de otra marca) → el agente podría mezclarlos.
  - Opciones discutidas: (a) cargar **solo** familiares + personales de la línea de domicilio (no los personales de mesa, que casi no se mueven), dejando la opción de responder si el cliente pregunta explícitamente por un personal; (b) diferenciar por **gramajes/nombres**. Decisión final pendiente por confirmar (2026-10-20).

## 4. Pedidos

- Canales actuales de recepción: WhatsApp (una línea), presencial, página web.
- **Datos a capturar al inicio del pedido** (acordado): Nombre, Dirección, Barrio, Teléfono, Medio de pago.
- Métodos de pago aceptados: efectivo (domicilio), **QR Multibanca / llave Bre-B**; **tarjeta de crédito** mediante **link de pago del datáfono** (lo emite un humano, **no** el agente). Contexto: hay fraude con tarjeta → se prefiere QR/llave.
- Cobertura de domicilio: validación por **barrio contra tabla**; costo por zona; sectores ambiguos o no listados → **escalar** (nunca responder "no te despacho" en seco). Flota: entrega ~30 min promedio (variable).
- Recogida en sitio: pendiente por confirmar (2026-10-20).

## 5. Reservas

- ¿Aceptan reservas? **Sí.** Sin costo (no se cobra la reserva).
- Datos a capturar: **ocasión, fecha, número de personas**.
- Valor agregado: detalle de cumpleaños (decoración sencilla / postre con vela) — alcance exacto pendiente por confirmar (2026-10-20).
- Anticipación mínima, tamaño máximo de grupo, política de no-show, canal y volumen: pendiente por confirmar (2026-10-20).

## 6. Brechas digitales identificadas

- Brecha 1 — **Catálogo enorme y no estructurado en el canal**: ~400 productos en 4 marcas, hoy se envían como PDF pesados (~12 MB) de forma manual. Hipótesis: catálogo estructurado + flujo de asesoría por componentes acelera la respuesta y reduce fricción.
- Brecha 2 — **El diferencial del negocio (asesoría/armado por proteína+preparación) no está en el canal**: el autoservicio por PDF pierde la "psicología de consumo" del vendedor. Hipótesis: la IA replica ese flujo (tipo de plato → mariscos sí/no → proteína → preparación/sabor) y mejora conversión.
- Brecha 3 — **Dualidad mesa/domicilio con productos duplicados**: precios y nombres que se solapan confunden al cliente y al bot. Hipótesis: estructurar solo la línea de domicilio (o diferenciar por gramaje/nombre) ordena el pedido.
- Brecha 4 — **Fuera de horario sin respuesta**: hipótesis: el agente envía cartas 24/7 y permite programar, capturando demanda nocturna sin tomar pedido fuera de horario.
- Brecha 5 — **Validación manual de zonas de domicilio**: hoy se consulta una tabla de barrios a mano. Hipótesis: el agente valida el barrio y escala los sectores ambiguos, sin rechazar en seco.

## 7. Prioridades de implementación para este cliente

1. Secuencia de bienvenida + **envío de cartas** (4 marcas + bebidas) en PDF liviano / link de la página.
2. **IA de asesoría de carta por componentes** (tipo de plato → ¿mariscos? → proteína → preparación/sabor), replicando la venta consultiva del punto.
3. **Toma de pedido cuando el cliente ya lo tiene claro** (captura Nombre/Dirección/Barrio/Teléfono/Pago), con **confirmación final por humano**.
4. **Validación de zona de domicilio** contra tabla de barrios + **escalamiento** de sectores ambiguos/no cubiertos.
5. **Reservas** (ocasión/fecha/#personas), sin cobro.

Alcance del agente acordado (2026-10-20): **dos funciones** — (a) explicar/asesorar la carta; (b) si el cliente ya tiene claro el pedido, tomarlo. Si requiere asesoría profunda, **escala a asesor humano**. Siempre escalan: pago con tarjeta de crédito (link del datáfono), quejas, cobro doble, "no llegó", sectores no cubiertos.

## 8. Riesgos y bloqueos

- Recurso interno para operar: sí — Carlos Mauricio Villa Sánchez (operador; capacitando al equipo). Usuario adicional: Ana María Sepúlveda (por invitar).
- Conectividad / dispositivos: hay WhatsApp Business (una línea, ~4 dispositivos); en la sesión se vinculó AriCRM por QR en una tablet, en **modo escucha**. Dependencia operativa concentrada en Carlos Mauricio (mitigación: capacitación al equipo en curso).
- Catálogo de ~400 productos: reto de cobertura → mitigación acordada: arrancar con asesoría de carta + toma de pedido solo cuando el cliente tiene claro qué quiere.
- PDF de ~12 MB: bloqueante de UX → el establecimiento entregará versión liviana.
- Dualidad mesa/domicilio y productos duplicados: riesgo de que el agente mezcle precios/porciones → decidir estructura de catálogo antes de activar.
- Alcance de líneas: por ahora **una sola línea** de WhatsApp (las 3 del alcance quedan disponibles).

## Fecha, responsable, firma

- Fecha de caracterización: 2026-10-20 (levantamiento preliminar; pendiente validación del establecimiento).
- Responsable MY SEO: Nicolás Navarro Rincón — MY SEO.
- Responsable establecimiento: Carlos Mauricio Villa Sánchez — Compañía de Restaurantes Sushi S.A.S.
- Evidencia: reunión `../../evidencias/sushi-fusion/reunion-caracterizacion-2026-10-20.md` y formulario `../../evidencias/sushi-fusion/formulario-caracterizacion-2026-10-20.csv`.
