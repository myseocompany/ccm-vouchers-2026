# CARACTERIZACION — La Rancha Parrilla

**Estado:** borrador consolidado el 2026-10-10 desde el CSV y la entrevista. La fecha de la sesión, la confirmación como beneficiaria y la validación del establecimiento están pendientes. Seguir `../../workflows/01_caracterizacion.md` antes de cerrar C-01.

## 1. Operación actual

- Aforo: aproximadamente 50 personas; turnos internos pendientes de confirmar.
- Servicio al público: inicia a las 11:30 a. m. La entrevista indica cierre a las 3:30 p. m.; el CSV, a las 3:00 p. m. **Horario vigente pendiente de confirmar.**
- Recepción de pedidos: 9:30 a. m.–3:00 p. m., según ambas fuentes.
- Volumen diario de pedidos por canal, ticket promedio, horas pico y estacionalidad: pendientes de medir o confirmar. Los precios del menú no equivalen al ticket promedio.

## 2. Atención al cliente

- La responsable entrevistada operaría AriCRM y recibiría escalamientos; un supervisor apoyaría la operación. Usuarios, roles y acceso efectivo pendientes de verificar en AriCRM.
- Llegan consultas de domicilios, reservas, quejas, recomendaciones y proveedores. Las preguntas frecuentes reportadas son ubicación, menú del día y alternativas al menú.
- Canal principal de pedidos: una línea de WhatsApp. Se reportó otra línea para asuntos administrativos; no se confirmó su integración.
- Herramientas actuales: respuestas rápidas, lista de difusión y estado de WhatsApp para publicar el menú diario. AUNCLICK creó una cuenta/plataforma para el negocio, sin alcance técnico precisado.
- Volumen de conversaciones, horario de respuesta humana y tiempo medio de respuesta: pendientes de confirmar.

## 3. Menú

- Menú del día planificado semanalmente y comunicado cada mañana; los platos y acompañamientos cambian diariamente. La programación se conserva en papel en cocina y se comparte por WhatsApp.
- Precio reportado del menú estándar entre semana: $19.000 en restaurante; $21.000 para domicilio o para llevar según CSV. Res, pollo y cerdo aparecen como opciones estándar.
- Precio reportado de fin de semana, trucha, tilapia y churrasquito: $21.000 en restaurante; $23.000 para domicilio o para llevar según CSV. Confirmar si recogida y domicilio tienen el mismo precio y si hay cobro adicional de envío por zona.
- Se reportó una opción de sopa y una de crema cada día. El CSV indica fríjoles rancheros los domingos; validar composición y disponibilidad.
- Jugos, ensaladas y otras preparaciones rotan con los precios y la disponibilidad de insumos.
- Carta completa vigente, categorías, variantes, condiciones de agotados y fotos: pendientes de recibir. La responsable ofreció la programación semanal y la pieza diaria; indicó que faltan fotos sistemáticas.
- **Regla para IA:** consultar únicamente el menú diario vigente; no inferir el plato de hoy a partir de la programación de otra semana.

## 4. Pedidos, pagos y domicilios

- WhatsApp recibe pedidos; canales adicionales de pedido y recogida en sitio pendientes de confirmar.
- Métodos de pago: efectivo y transferencia con QR. Imagen e instrucciones vigentes pendientes de recibir y validar.
- Cobertura reportada por el CSV: Manizales. La entrevista describe domicilio sin cobro en Alta Suiza, Baja Suiza, Milán, La Sultana, Palermo, La Camelia y El Cable hasta Cable Plaza. **Perímetro exacto y cobertura fuera de él pendientes de validar.** Villamaría fue mencionada en una pregunta, sin respuesta concluyente.
- Fuera de la zona gratuita se usa un grupo de domiciliarios con tabla de tarifas; tabla y condiciones pendientes de recibir. No prometer tarifa sin consultar o confirmar.
- La responsable describió una primera tanda de pedidos recibidos hasta las 11:00 a. m., con despachos aproximados de 11:45 a. m. a 12:30 p. m.; pedidos posteriores tendrían entrega aproximada de 12:30 p. m. a 1:15 p. m. Estos horarios dependen del volumen y **no constituyen un SLA o promesa automática de entrega**.
- Tiempo promedio medido de preparación y entrega: pendiente.

## 5. Reservas

- Acepta reservas por WhatsApp, teléfono y presencialmente.
- La entrevista no indicó anticipación mínima ni restricciones, pero el formulario dejó esos campos vacíos. Confirmar tamaño máximo, disponibilidad por horario, política de ausencia y datos mínimos para reservar antes de automatizar.
- Volumen de reservas: pendiente.

## 6. Brechas digitales identificadas — hipótesis, no decisión aprobada

1. **Menú diario sin fuente estructurada para el CRM.** La planificación está en papel y WhatsApp y cambia cada día. Hipótesis de impacto: reducir respuestas manuales y errores de disponibilidad al publicar una versión diaria validada.
2. **Consultas y pedidos mezclados con proveedores y reclamos en WhatsApp.** Hipótesis de impacto: clasificar cada conversación para que pedidos, reservas y casos administrativos lleguen al responsable adecuado; medir volumen y tiempos.
3. **Tarifas de domicilio fuera de la zona gratuita no documentadas en el material recibido.** Hipótesis de impacto: evitar cotizaciones erróneas y escalar zonas sin tarifa confirmada.
4. **Reclamos sin ruta documentada en el material recibido.** Hipótesis de impacto: escalar con contexto a la responsable y registrar causa y resolución.

## 7. Prioridades propuestas de implementación

1. Recibir y validar programación, menú diario, precios y reglas de agotados.
2. Tipificar consultas, pedidos, reservas, proveedores y reclamos; propuesta en `TIPIFICACION.md`.
3. Definir cobertura, tarifa y confirmación de domicilios por zona.
4. Configurar respuestas de preguntas frecuentes y escalamiento humano, con pruebas controladas.
5. Configurar reservas después de confirmar reglas de capacidad y horario.

## 8. Riesgos y bloqueos

- La Rancha no está en el listado contractual de diez beneficiarios registrado en el harness: confirmar su relación con el programa antes de contabilizar obligaciones.
- Cierre del horario de atención contradictorio entre las dos fuentes.
- Menú, imagen diaria, respuestas rápidas, tabla de tarifas, QR de pago y manual ofrecidos, pero no consta su recepción en esta carpeta.
- Dirección exacta, política de reservas, volumen de operación, conectividad, disponibilidad del equipo y resistencia al cambio: pendientes de confirmar.
- La entrevista describe vinculación de WhatsApp, pero el estado actual del canal y del tenant solo puede verificarse en AriCRM.

## Fecha, responsable y evidencia

- Fecha de entrevista: pendiente de confirmar. Consolidación documental: 2026-10-10.
- Responsable MY SEO: Nicolás, entrevistador según transcripción aportada.
- Responsable establecimiento: responsable entrevistada; firma o aprobación de este contenido pendiente.
- Fuente primaria de respuestas: `/Users/nicolasnavarrorincon/Downloads/AriCRM_CCMPC - LaRancha.csv` y `../../evidencias/la-rancha/entrevista-caracterizacion-sin-fecha.md`.
