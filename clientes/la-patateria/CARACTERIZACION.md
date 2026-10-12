# CARACTERIZACION — La Patateria

Obligación 2 del contrato. Identificar necesidades del establecimiento respecto a atención al cliente, gestión de menú, pedidos y reservas. Se hace UNA vez al inicio y sirve como línea base.

Fuente del método: `../../workflows/01_caracterizacion.md`.

**Estado de la información**: caracterización en progreso. Datos reportados en el formulario `evidencias/la-patateria/caracterizacion/AriCRM_CCMPC-patateria-2026-10-12.csv`; los vacíos requieren confirmación del establecimiento. No equivale todavía a aceptación ni cierre de C-01.

## 1. Operación actual

- Aforo y turnos: pendiente por confirmar al 2026-10-12.
- Volumen diario aproximado de pedidos en sitio / domicilio / recogida: pendiente por confirmar al 2026-10-12.
- Ticket promedio: pendiente por confirmar al 2026-10-12.
- Horario reportado: lunes a jueves, 12:00–21:00; viernes y sábado, 12:00–22:00; domingo, 12:00–20:00.
- Días de mayor demanda y estacionalidad: pendiente por confirmar al 2026-10-12.
- Apertura reportada: 14 de octubre; año, sede y alcance de esa apertura pendientes por confirmar al 2026-10-12.

## 2. Atención al cliente

- Responsable operativo reportado para AriCRM: líder de Servicio al Cliente identificado en `CLIENTE.md`.
- Quién responde WhatsApp hoy y en qué horario: pendiente por confirmar al 2026-10-12.
- Tiempo promedio de respuesta actual: pendiente por confirmar al 2026-10-12.
- Tipos de mensajes reportados: pedidos, reservas, explicación de platos, quejas y PQR.
- Preguntas frecuentes reportadas: ubicación, promociones, domicilios, ingredientes o composición de platos, cotizaciones, cobro de reservas, horario de apertura y disponibilidad de mesas.
- Volumen diario de conversaciones: pendiente por confirmar al 2026-10-12.
- Herramientas actuales: WhatsApp; se reportan Instagram, Facebook y sitio web, pero faltan URLs y verificación al 2026-10-12.
- Prioridad expresada en el formulario: el CRM es lo más importante.

## 3. Menú

- Menú digital vigente: existe carta digital publicada en `https://patateria.bibisoft.co/tienda/productos` (plataforma bibisoft; store_id=63, menu_id=12). Catálogo extraído el 2026-10-12 a `carta/` (`productos.json` crudo + `carta.md` + `carta.csv`). Pendiente: confirmar con el establecimiento si este catálogo publicado es la "carta nueva"/definitiva y su fecha de vigencia.
- Número de productos y categorías: **8 categorías y 46 productos** (todos activos y visibles en menú), según extracción del 2026-10-12 — ver `carta/carta.md`.
- Frecuencia de cambio reportada: anual.
- Fotos disponibles: sí; cada producto trae `url_image` en el catálogo publicado (verificado 2026-10-12).
- Precios definidos y públicos: sí; precio por producto (`unit_value`, COP) presente en el catálogo publicado (verificado 2026-10-12). Pendiente: validar vigencia de precios con el establecimiento.
- Productos agotados o rotativos y mecanismo para marcarlos: pendiente por confirmar al 2026-10-12.

## 4. Pedidos

- Canales actuales de recepción: WhatsApp y atención en local; uso de teléfono, web u otros canales pendiente por confirmar al 2026-10-12.
- Métodos de pago reportados para domicilio: enlace de pago y efectivo.
- Métodos de pago reportados en local: datáfono, efectivo y QR.
- Cobertura de domicilio: tercerizada mediante plataforma con tabla de tarifas. Se reporta que en Pereira no hay domicilios; sedes, zonas, proveedor y tabla vigentes pendientes por confirmar al 2026-10-12.
- Recogida en sitio e instrucciones: pendiente por confirmar al 2026-10-12.
- Horarios de recepción de pedidos: pendiente por confirmar al 2026-10-12.
- Tiempos reportados: preparación de 1,5 minutos y entrega de 10 minutos; alcance y condiciones de estos tiempos pendientes por validar al 2026-10-12.

## 5. Reservas

- Aceptan reservas: sí, reportado en el formulario.
- Canales actuales: WhatsApp, teléfono y presencial.
- Volumen aproximado: pendiente por confirmar al 2026-10-12.
- Reglas reportadas: aceptación según ocupación; mesas de hasta 15 personas; grupos mayores requieren llamada.
- Anticipación mínima, cobro o garantía y política de no-show: pendientes por confirmar al 2026-10-12.
- Se menciona un enlace para pedidos/reservas y disponibilidad de mesas mediante “Cluvi”; URL, flujo y vigencia pendientes por confirmar al 2026-10-12.

## 6. Brechas digitales identificadas

Las siguientes son hipótesis de trabajo priorizadas a partir del formulario; deben validarse con el establecimiento antes de configurar producción.

1. **Información operativa y catálogo dispersos o sin validar**: todavía no se cuenta con la carta nueva, URLs verificadas, reglas completas de pedidos/reservas ni cobertura de domicilios por sede. Impacto esperado: evitar respuestas contradictorias y permitir que menú, horarios y condiciones se consulten desde una fuente vigente.
2. **Atención de WhatsApp sin línea base medible**: faltan volumen de conversaciones, responsable y horario actual, y tiempo promedio de respuesta. Impacto esperado: centralizar la atención en AriCRM y establecer métricas base para medir tiempos y demanda.
3. **Escalamiento y automatización aún no parametrizados**: existen criterios iniciales para quejas y novedades, pero falta confirmar responsables, disponibilidad y flujo completo. Impacto esperado: automatizar preguntas frecuentes sin dejar desatendidos reclamos, cambios ni incidencias de pago o servicio.
4. **Operación multicanal y posiblemente multisede sin delimitación confirmada**: se reportan WhatsApp, Instagram, Facebook, sitio web y diferencias de domicilio en Pereira. Impacto esperado: evitar publicar información de una sede en otra y enrutar correctamente cada solicitud.

## 7. Prioridades de implementación para este cliente

Orden propuesto, sujeto a validación del establecimiento:

1. CRM y bandeja centralizada de atención.
2. Respuestas automáticas e IA para horarios, ubicación, promociones, composición de platos e información general.
3. Escalamiento humano de quejas, reclamos, cambios, cobros incorrectos y novedades del servicio.
4. Menú digital, una vez recibida y validada la carta nueva.
5. Integración o enlace de pedidos y reservas, con reglas confirmadas por sede.

Tono solicitado: muy cercano, informal y natural, con registro paisa, evitando caricaturizar el habla local.

La IA podría informar sobre decoración, ubicación y cortesía de cumpleaños cuando las reglas estén verificadas. Los pedidos y reservas se orientarían mediante enlace. Quejas, reclamos, cambios, cobros incorrectos y novedades del servicio deben escalar a una persona.

## 8. Riesgos y bloqueos

- Recurso interno para operar: se identificó un líder de Servicio al Cliente como responsable operativo; disponibilidad y suplencia pendientes por confirmar al 2026-10-12.
- Escalamiento: se reportan dos responsables; falta definir orden, horarios y canal de notificación al 2026-10-12.
- Conectividad, computador y dispositivos disponibles el día D: pendiente por confirmar al 2026-10-12.
- Disponibilidad de una persona durante cuatro horas continuas: pendiente por confirmar al 2026-10-12.
- Resistencia al cambio: pendiente por confirmar al 2026-10-12.
- Dependencia crítica de una sola persona: pendiente por confirmar al 2026-10-12.
- Solo se reportó una línea de WhatsApp para conexión; las líneas 2 y 3 y sus titulares están pendientes.
- La carta nueva, sus precios y su vigencia bloquean la carga definitiva del menú.
- La información de sedes y la referencia a Pereira deben aclararse antes de publicar ubicaciones, domicilios o tiempos.
- Las autorizaciones y confirmaciones finales del formulario están vacías; no configurar canales en producción sin aprobación explícita y presencia del titular.

## Fecha, responsable, firma

- Fecha de caracterización: pendiente; CSV incorporado y analizado el 2026-10-12.
- Responsable MY SEO: Nicolás Navarro Rincón.
- Responsable establecimiento: fundador identificado en `CLIENTE.md`; confirmación/firma pendiente al 2026-10-12.
- Responsable operativo reportado: líder de Servicio al Cliente identificado en `CLIENTE.md`.
- Evidencia: `../../evidencias/la-patateria/caracterizacion/AriCRM_CCMPC-patateria-2026-10-12.csv` y `../../evidencias/la-patateria/caracterizacion/extraccion-2026-10-12.md`.
