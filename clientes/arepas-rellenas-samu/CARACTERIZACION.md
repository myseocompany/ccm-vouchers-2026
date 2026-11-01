# CARACTERIZACION — Arepas Rellenas Samu

Obligación 2 del contrato. Identificar necesidades del establecimiento respecto a atención al cliente, gestión de menú, pedidos y reservas. Se hace UNA vez al inicio y sirve como línea base.

Fuente del método: `../../workflows/01_caracterizacion.md`.

- **Fecha de caracterización**: 2026-09-30
- **Responsable MY SEO**: Nicolás Navarro Rincón
- **Responsable establecimiento**: Adrián Sepúlveda
- **Evidencia**: `evidencias/arepas-rellenas-samu/caracterizacion-2026-09-30.md`

---

## 1. Operación actual

- **Sedes**: 2
  - Sede Chipre — sede principal, antigüedad mayor
  - Sede San Jorge — nueva, menos de 1 mes (abierta sept 2026)
- **Aforo**: consumo rápido en sitio (no hay salón gestionado); alta rotación de mesas; clientes llegan, piden y consumen sin reserva previa
- **Horario**: lunes a domingo 4:00 PM – 10:30 PM (ambas sedes)
- **Modelo de negocio**: domicilios + consumo en sitio espontáneo. Sin reservas.
- **Volumen diario de pedidos**: no cuantificado en la reunión — _pendiente levantar métrica_
- **Ticket promedio**: _pendiente_
- **Días de mayor demanda**: _pendiente confirmar_, presumiblemente fines de semana
- **Estacionalidad**: _pendiente_
- **Producción**: manual con moldes y rodillos. Evalúan mecanizar (máquina de arepas)
- **Bodega/producción**: bodega anterior colapsó por derrumbe; ya cuentan con bodega nueva — costos incrementados

## 2. Atención al cliente

- **Quién responde WhatsApp hoy**: Adrián Sepúlveda y su mamá Heny Johana Castillo (Chipre). En San Jorge: Adrián coordina.
- **Tiempo promedio de respuesta actual**: _pendiente cuantificar_
- **Tipos de mensaje recibidos**: 100% pedidos. Proveedores se manejan en líneas personales separadas.
- **Volumen diario de conversaciones**: _pendiente_
- **Herramientas actuales**: WhatsApp Business. Usan respuestas rápidas: al primer mensaje envían imagen del menú + solicitud de datos (dirección, teléfono, método de pago).
- **Práctica actual de contactos**: agregan manualmente todos los que escriben para que vean los estados de WA.

## 3. Menú

- **Menú digital existente**: sí — imagen/foto enviada por WhatsApp como respuesta rápida
- **Producto base**: arepa rellena combinable. ~10 ingredientes opcionales → combinaciones prácticamente ilimitadas
- **Ingredientes confirmados**: carne, jamón, queso, tocineta (esta última solo en San Jorge por ahora)
- **Diferencias entre sedes**: San Jorge tiene tocineta + precios levemente distintos. Plan: unificar en semana del 2026-10-06
- **Bebidas**: no se incluyen en domicilios (se derraman/enfrían)
- **Fotos disponibles**: parcial — hay fotos de combinaciones representativas, no de cada variante
- **Frecuencia de cambio**: relativamente fijo; cambios puntuales de ingredientes/precios
- **Carta entrenamiento IA**: usar carta actualizada de San Jorge (con tocineta), corrección del número en el diseño pendiente por Adrián

## 4. Pedidos

- **Canales de recepción**: WhatsApp (principal), presencial espontáneo
- **Flujo del pedido**: cliente escribe → recibe carta automática → confirma pedido con dirección, teléfono y método de pago → se prepara → se envía con emoji de confirmación → cliente paga (antes, durante o después de la llegada — nunca han tenido impago)
- **Métodos de pago**:
  - Efectivo (ambas sedes)
  - Transferencia / Nequi 314 337 1048 (Chipre)
  - Llave 316 668 7367 (San Jorge)
- **Política de pago**: no es pago estricto primero; se confía en el cliente; cero impagos históricos
- **Cobertura de domicilio**: Manizales y Villamaría — flota propia
- **Costo de domicilio**: variable por barrio/zona. Tabla diferente por sede (imágenes compartidas en reunión — adjuntar a evidencia)
- **Tiempos**: 30-50 minutos promedio según distancia. Comunicación al cliente: "entre 30 y 40 min, puede ser antes"

## 5. Reservas

- **Aceptan reservas**: NO
- **Razón**: negocio de rotación continua; espacio no permite gestionar llegadas programadas; clientes llegan directamente

## 6. Brechas digitales identificadas

1. **Sin base de datos organizada de clientes**: los contactos están dispersos en los teléfonos; no hay lista exportable para campañas. Impacto hipotético: imposibilidad de fidelización activa.
2. **Flujo de pedido manual**: respuestas rápidas funcionan pero no automatizan la captura de datos ni la confirmación estructurada. Tiempo ahorrado con automatización: ~2-3 min por conversación.
3. **Dos líneas desconectadas operativamente**: Chipre y San Jorge se responden de forma independiente; no hay vista unificada. Riesgo de inconsistencia en respuestas.
4. **Menús inconsistentes entre sedes**: carta diferente genera confusión y dificulta entrenamiento de IA. Bloquea lanzamiento unificado hasta que Adrián iguale cartas (~semana 2026-10-06).
5. **Sin capacidad de campaña masiva**: WhatsApp Business tiene límite ~200 mensajes/día; sin línea Cloud API no pueden hacer difusión a toda la base. Brecha de fidelización directa.

## 7. Prioridades de implementación para este cliente

1. **Menú digital unificado** — prerequisito para todo lo demás; esperar unificación de carta
2. **Pedidos automatizados** — captura de datos (dirección, teléfono, método de pago) sin intervención humana
3. **Respuestas automáticas + IA** — FAQs (tiempo de entrega, ubicación, tarifas de domicilio), escalamiento para PQR/reclamos
4. **Base de datos de contactos** — captura estructurada desde conversaciones para habilitar campañas futuras
5. **Reservas** — no aplica

## 8. Riesgos y bloqueos

- **Dependencia crítica en Adrián**: es el único operador tecnológico; si no está disponible, la operación queda sin soporte. La mamá no maneja tecnología.
- **Menús aún no unificados**: bloqueo parcial para entrenamiento de IA hasta semana del 2026-10-06
- **Dos razones sociales/cuentas separadas**: Chipre (Heny Johana) y San Jorge (familiar); no son sociedad; requiere coordinar permisos y pagos por separado
- **Conectividad/dispositivos**: Adrián tiene los dos teléfonos; el de San Jorge no siempre está en el local → riesgo de desconexión de WA
- **Resistencia al cambio**: no detectada en Adrián; mamá puede necesitar acompañamiento adicional si se le asigna un rol
- **Alcance de dos sedes**: confirmado con Sandra (Cámara) que aplica para las dos; documentar esta autorización formalmente
