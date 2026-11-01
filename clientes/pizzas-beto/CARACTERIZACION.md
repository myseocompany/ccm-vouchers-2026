# CARACTERIZACION — Pizzas Beto

Obligación 2 del contrato. Identificar necesidades del establecimiento respecto a atención al cliente, gestión de menú, pedidos y reservas. Se hace UNA vez al inicio y sirve como línea base.

Fuente del método: `../../workflows/01_caracterizacion.md`.

## 1. Operación actual

- Aforo y turnos: capacidad instalada reportada para aproximadamente el doble de la operación actual; aforo físico y turnos de cocina pendientes de cuantificar.
- Volumen diario aproximado de pedidos: cerca de 20 en total; falta desagregar entre sitio, domicilio y recogida.
- Ticket promedio: no se reportó un promedio consolidado. Se indicó que una pizza grande con domicilio es el pedido más habitual y cuesta $85.000. Validar la matriz vigente, pues el sitio público muestra pizzas entre $9.000 y $76.000 sin que sea posible determinar si incluyen domicilio.
- Días y horarios de mayor demanda: lunes a domingo de 11:00 a. m. a 9:45 p. m.; fines de semana con mayor demanda. El sitio público anuncia 11:00 a. m.–8:00 p. m.; confirmar el horario vigente por canal antes de automatizarlo.
- Estacionalidad: mayor demanda en fines de semana; cuantificación pendiente por confirmar.

## 2. Atención al cliente

- ¿Quién responde WhatsApp hoy? Leidy Johana Gaviria Martínez, cajera y responsable operativa propuesta de AriCRM; atiende de 8:00 a. m. a 10:00 p. m. para pedidos programados.
- Tiempo promedio de respuesta actual: inmediato si no hay otros chats activos; máximo reportado de 2 a 5 minutos en horas pico.
- Tipos de mensaje que reciben: principalmente pedidos; también consultas y quejas.
- Volumen diario de conversaciones: cercano al volumen de pedidos; dato exacto pendiente por confirmar.
- Herramientas actuales: WhatsApp con autorrespuesta, carta y catálogo de fotos; sitio web transaccional; Instagram y Facebook. TikTok está proyectado. Falta identificar cuentas y autorizaciones para integraciones.

## 3. Menú

- Menú digital existente y formato: catálogo de WhatsApp, sitio web y carta recibida en PDF. Referencia pública: `https://betospizza.com.co/tienda/`; la carta estructurada está en `evidencias/pizzas-beto/vertical-restaurantes/menu/menu-estructurado-carta-2026-10-05.md`. Vigencia pendiente de confirmación del establecimiento.
- Nº aproximado de productos / categorías: la carta PDF identifica 14 sabores de pizza, lasaña, maicitos, bowl de nachos y 6 bebidas; el sitio público muestra 5 categorías y 17 ítems. Validar catálogo operativo, SKUs, variantes y disponibilidad ante la discrepancia de presentación.
- Frecuencia de cambio: pendiente por confirmar.
- Fotos disponibles: sí, en el catálogo de WhatsApp y reportadas por el establecimiento; deben entregarse los originales para no perder resolución.
- Precios definidos y públicos: sí, en carta/catálogo y sitio web; la matriz completa vigente por tamaño, sabor, adición y domicilio requiere validación antes de cargarla en AriCRM.

## 4. Pedidos

- Canales actuales de recepción: WhatsApp, sitio web con carrito/compra y recogida en la sede centro. El sitio web genera entre uno y cinco pedidos diarios, y alrededor de diez semanales según el establecimiento.
- Métodos de pago aceptados: contraentrega, transferencia, datáfono, efectivo y llave; confirmar instrucciones vigentes y datos de recaudo antes de automatizarlos.
- Cobertura de domicilio: toda Manizales y Villamaría; Neira se gestiona programado. Modalidad propia/tercerizada pendiente por confirmar.
- Costo de domicilio: tarifa única actual, cuyo monto debe confirmarse; una conversación de agosto-septiembre de 2026 registra $5.000, pero es evidencia histórica y no una tarifa vigente aprobada. El establecimiento quiere variar la tarifa por zona.
- Recogida en sitio: sí, únicamente sede centro (Calle 20 #20-32).
- Tiempos promedio de preparación y entrega: varían según el sector y demanda; una conversación de septiembre de 2026 registró una estimación de 45 minutos. Falta definir reglas/valores vigentes para automatización.

## 5. Reservas

- ¿Aceptan reservas? No.
- Canal actual y volumen: no aplica mientras no se acepten reservas; confirmar si hay excepciones para grupos o eventos (2026-10-05).
- Reglas: no aplica; pendiente confirmar excepciones (2026-10-05).

## 6. Brechas digitales identificadas

Lista priorizada de brechas que AriCRM Plan Crecer + vertical restaurantes va a cerrar. Cada brecha con hipótesis de impacto (tiempo ahorrado, mensajes atendidos, pedidos capturados, reservas gestionadas).

- Brecha 1 — La carta existe en WhatsApp y web, pero falta recibir y validar la matriz vigente de SKUs, precios, variantes, disponibilidad y tarifas de domicilio para atención conversacional. **Impacto esperado**: responder consultas de producto/precio de forma consistente y habilitar pedidos guiados. Prioridad 1.
- Brecha 2 — Atención de consultas y pedidos depende de una sola operadora, con demoras de hasta 2–5 minutos en horas pico. **Impacto esperado**: resolver automáticamente horarios, ubicación, cobertura, tamaños y tiempos, reduciendo la carga inicial. Prioridad 2.
- Brecha 3 — No hay reglas documentadas para clasificar pedidos, consultas y quejas ni para escalar estas últimas al gerente. **Impacto esperado**: atención trazable y escalamiento oportuno de quejas/casos no resueltos. Prioridad 3.

## 7. Prioridades de implementación para este cliente

1. Validar y estructurar menú/catálogo vigente y pedidos conversacionales.
2. Respuestas automáticas para preguntas frecuentes (cobertura, tamaños, tiempos, ubicación) y clasificación inicial.
3. Agente IA con escalamiento al gerente para quejas, cambios y casos no resueltos.
4. Reservas: no prioritaria, pues el establecimiento reporta que no las acepta; reevaluar solo si el cliente cambia esa regla.

## 8. Riesgos y bloqueos

- Recurso interno para operar: sí, Leidy Johana Gaviria Martínez fue identificada como responsable operativa; existe dependencia operativa de esta persona que debe mitigarse con al menos un usuario adicional.
- Conectividad / dispositivos: el cliente prevé operar mediante enlace en computador y también desde WhatsApp; validar conectividad y disponibilidad el día de configuración.
- Resistencias al cambio identificadas: no reportadas en la reunión; validar en el seguimiento.
- Bloqueos de implementación: faltan matriz de menú/precios vigente, tarifas/tiempos de domicilio por zona, número y titular de la línea, usuarios adicionales, permisos de canales sociales y confirmación del horario que se automatizará.

## Fecha, responsable, firma

- Fecha de caracterización: reunión transcrita, fecha efectiva pendiente de confirmar; consolidación documental 2026-10-05.
- Responsable MY SEO: pendiente de asignación.
- Responsable establecimiento: Alex Humberto Bedoya, gerente general (formulario suministrado; firma/validación pendiente).
- Evidencia: `evidencias/pizzas-beto/caracterizacion-2026-10-05.md`, `evidencias/pizzas-beto/caracterizacion/transcripcion-reunion-alex-2026-10-05.md`, `evidencias/pizzas-beto/caracterizacion/sitio-publico-2026-10-05.md`, `evidencias/pizzas-beto/operacion/conversacion-whatsapp-2026-08-31-2026-09-21.md` y `evidencias/pizzas-beto/vertical-restaurantes/menu/menu-estructurado-carta-2026-10-05.md`; fuentes originales en `evidencias/pizzas-beto/caracterizacion/fuentes/`.
