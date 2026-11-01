# CARACTERIZACION — The Boss Burger

Obligación 2 del contrato. Identificar necesidades del establecimiento respecto a atención al cliente, gestión de menú, pedidos y reservas. Se hace UNA vez al inicio y sirve como línea base.

Fuente del método: `../../workflows/01_caracterizacion.md`.
Fuente de datos: formulario de caracterización diligenciado por el establecimiento y confirmaciones posteriores de Nicolás (2026-10-11): `../../evidencias/the-boss/caracterizacion-2026-10-11.md`.

**Estado: preliminar** (levantamiento 2026-10-11, pendiente de validación con el establecimiento). Los campos sin respuesta en el formulario se marcan «pendiente por confirmar (2026-10-11)». Las brechas de la sección 6 son propuestas del harness pendientes de validación.

## 1. Operación actual

- Aforo y turnos: aforo máximo 50 personas. Martes a jueves 18:00–22:00; viernes a domingo 17:00–22:00; lunes sin servicio (confirmado por el mensaje de bienvenida del negocio y cargado en el tenant).
- Volumen diario aproximado de pedidos (en sitio / domicilio / recogida): pendiente por confirmar (2026-10-11).
- Ticket promedio: pendiente por confirmar (2026-10-11). Referencia de carta: hamburguesas $28.000–$30.000; combo con papas y gaseosa +$9.000.
- Días y horarios de mayor demanda: pendiente por confirmar (2026-10-11).
- Estacionalidad: pendiente por confirmar (2026-10-11).

## 2. Atención al cliente

- ¿Quién responde WhatsApp hoy?: pendiente por confirmar (2026-10-11). En producción hay una línea «Principal» conectada a AriCRM.
- Tiempo promedio de respuesta actual: pendiente por confirmar (2026-10-11).
- Tipos de mensaje que reciben: pendiente por confirmar (2026-10-11).
- Volumen diario de conversaciones: pendiente por confirmar (2026-10-11).
- Herramientas actuales: WhatsApp con mensaje de bienvenida manual («Hola bienvenidos a the boss burger. En un momento te atenderemos. Los días Lunes no tenemos Servicio»).

## 3. Menú

- ¿Menú digital existente?: carta impresa («Menú The Boss – Impresión.pdf»), transcrita y verificada producto por producto contra las capturas ampliadas: `../../evidencias/the-boss/vertical-restaurantes/menu/carta-the-boss-2026-10-11.md`. Catálogo digital cargado en el tenant el 2026-10-11.
- Nº aproximado de productos / categorías: 23 productos en 6 categorías (Burgers, Sandwich del Boss, Papitas del Boss, Pinchos del Boss, Adiciones, Bebidas).
- Cambia con qué frecuencia: pendiente por confirmar (2026-10-11). El formulario menciona «una promoción de hamburguesa».
- Fotos disponibles: parcial (imágenes de la carta impresa; fotos de producto no entregadas).
- Precios definidos y públicos: sí (COP; verificación 2026-10-11 sin diferencias contra el original).

## 4. Pedidos

- Canales actuales de recepción: WhatsApp (línea «Principal»); recogida en sitio. Otros canales (teléfono, apps): pendiente por confirmar (2026-10-11).
- Métodos de pago aceptados: efectivo y transferencia (Nequi/Daviplata/Bre-B). Sin datáfono: ante otros medios, escalar.
- Cobertura de domicilio: tercerizada — Flash Delivery Manizales. La tarifa por barrio se traslada al cliente sin subsidio ni recargo propio.
- Costo de domicilio: 180 tarifas por barrio cargadas en sede Principal (verificadas contra el JSON: 180 activas, suma COP 1.538.000). Zonas «en rojo» del PDF sin modelar: verificar disponibilidad con el operador antes de prometer despacho.
- Tiempos promedio de preparación y entrega: preparación ~10 minutos (confirmado 2026-10-11); la entrega depende de Flash Delivery (no prometer tiempo de llegada).

## 5. Reservas

- ¿Aceptan reservas?: **no** (confirmado 2026-10-11). El agente lo comunica con amabilidad y ofrece pedido a domicilio o recogida.
- Canal actual / volumen / reglas: no aplica.

## 6. Brechas digitales identificadas

Propuestas del harness (2026-10-31) a partir del formulario y las confirmaciones; pendientes de validación con el establecimiento. Las tres primeras ya tienen mitigación implementada en el tenant:

- Brecha 1 — atención 100 % manual de WhatsApp con horario nocturno y receptores no dedicados → agente IA de domicilios publicado (prompt v2.7) que atiende dentro del horario cargado. Impacto hipotético: pedidos atendidos fuera de la barra, sin espera de respuesta humana.
- Brecha 2 — carta solo en impreso/foto, sin catálogo digital consultable en la conversación → catálogo cargado (23 productos) y expuesto vía `get_catalog`. Impacto hipotético: menos ida y vuelta para precios e ingredientes.
- Brecha 3 — la cotización del domicilio dependía de consulta manual al operador (Flash Delivery) → 180 tarifas por barrio consultables vía `get_delivery_fee`. Impacto hipotético: cotización inmediata con tarifa exacta.
- Brecha 4 (propuesta) — sin registro estructurado de pedidos y clientes → `create_order` con confirmación por token. Pendiente de pruebas formales end-to-end.

## 7. Prioridades de implementación para este cliente

1. Menú digital — hecho: catálogo cargado y verificado (2026-10-11).
2. Pedidos y domicilios — en curso: tarifas cargadas; falta pedido de prueba end-to-end y capturas.
3. Respuestas automáticas / IA — en curso: prompt v2.7 publicado; faltan las 5 conversaciones de prueba formales con clasificación.
4. Plantillas y etiquetas — pendiente.
5. Reservas — no aplica (el establecimiento no acepta reservas).

## 8. Riesgos y bloqueos

- Recurso interno para operar: por confirmar. Usuarios designados: Diego López Benjumea (propietario) y Paola Camacho (mesera); correos y roles de acceso sin respuesta en el formulario.
- Conectividad / dispositivos: sin respuesta en el formulario (bloque 8) — pendiente por confirmar (2026-10-11).
- Resistencias al cambio: sin respuesta en el formulario — pendiente por confirmar (2026-10-11).
- Riesgo operativo identificado: dependencia del propietario como canal único (WhatsApp y Nequi/Daviplata/Bre-B usan el mismo número); la receptora de escalamientos (Paola Camacho) no tiene teléfono registrado.
- Riesgo de cobertura: zonas «en rojo» de Flash Delivery sin modelar en el tenant; festivos sin configurar.

## Fecha, responsable, firma

- Fecha de caracterización: 2026-10-11 (levantamiento preliminar; pendiente validación del establecimiento).
- Responsable MY SEO: Nicolás Navarro Rincón.
- Responsable establecimiento: Diego López Benjumea (propietario) — diligenció el formulario; bloques 8 y 9 (riesgos y confirmaciones/firmas) sin respuesta.
- Evidencia (notas de reunión, grabación, formulario): `../../evidencias/the-boss/caracterizacion-2026-10-11.md` (formulario normalizado + confirmaciones posteriores del 2026-10-11).
