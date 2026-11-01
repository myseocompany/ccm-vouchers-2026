# Minuta operativa de entrevista — El Efecto Barbacoa

**Fecha de registro**: 2026-09-29  
**Fuente**: transcripción compartida directamente por Nicolás en esta conversación.  
**Estado**: levantamiento operativo preliminar; pendiente de validación formal del establecimiento.  
**Protección de datos**: la transcripción de origen contenía datos personales de integrantes del establecimiento. No se archiva aquí; esta minuta conserva únicamente información operativa mínima.

## Operación y oportunidad

- Capacidad estimada: entre 150 y 200 personas; ocupación semanal aproximada: hasta 100 personas.
- Horas de mayor carga: mediodía y noche. En esos momentos el equipo puede tardar entre 10 y 15 minutos en responder WhatsApp, con riesgo de perder pedidos o reservas de último momento.
- El resultado esperado de la automatización es una primera respuesta constante y más rápida para consultas frecuentes, pedidos y reservas.

## Canales y atención

- Hay una línea de WhatsApp principal para atención. La atiende el equipo de caja; las notificaciones o conversaciones que requieran intervención humana deben permanecer en ese canal de negocio, no en teléfonos personales.
- Las consultas habituales son reservas, domicilios y cotizaciones. Proveedores no se gestionan por ese WhatsApp.
- El menú vigente comunicado por el establecimiento es el PDF enlazado en [`mensaje-bienvenida-2026-09-29.md`](ia-conversacional/mensaje-bienvenida-2026-09-29.md).

## Pedidos y domicilios

- Los domicilios se reciben después de las 12:00. La hora límite, tiempos de preparación/entrega y medios de pago requieren confirmación antes de automatizar compromisos.
- Cobertura reportada: Manizales. El costo depende del sector y debe consultarse por barrio en el JSON de tarifas; no se debe enviar la tabla completa al cliente cuando basta responder su zona.
- El agente debe solicitar la zona, responder el valor solo cuando lo encuentre en la fuente vigente y escalar zonas ambiguas, no listadas o condiciones de pago especiales.

## Reservas

- Las reservas se gestionan solo por WhatsApp para mantener la confirmación escrita; actualmente se registran de forma manual, sin agenda digital.
- Horario habitual de reserva: hasta las 19:30 entre semana y hasta las 19:00 los fines de semana. Se admite una tolerancia de 20 minutos.
- No se toman reservas en Día de la Madre, Día del Padre y Amor y Amistad. Pueden existir cierres o excepciones adicionales que requieren confirmación vigente.
- La reserva sin decoración no tiene costo. La decoración opcional cuesta $50.000 COP y no es reembolsable. Pagos anticipados de consumo no son reembolsables, pero quedan como saldo consumible.
- La disponibilidad siempre debe ser validada por el equipo humano antes de confirmar una reserva.

## Escalamiento y tono

- Escalar al equipo humano: quejas, reclamos, devoluciones, problemas de pago, cotizaciones o eventos, solicitudes de hablar con administración, dudas específicas de productos o ingredientes que el catálogo no resuelva, y cualquier excepción de domicilio o reserva.
- El humano puede tomar el control de una conversación y el agente no debe continuar interviniendo sin una señal/herramienta que lo habilite.
- Tono esperado: humano, cercano y respetuoso; saludo contextual (buenos días/tardes/noches) y presentación como El Efecto Barbacoa, sin un personaje o acento impuesto.

## Marca y propuesta gastronómica

- Restaurante especializado en cortes de carne, barbacoa texana y asado a las brasas.
- Su propuesta se centra en el manejo experto de leña, carbón y fuego para obtener sabores y aromas distintivos sin ocultar el sabor de la carne.
- Esta información sirve para describir la marca de forma general; no sustituye las fichas vigentes de productos, ingredientes o restricciones alimentarias.

## Pendientes antes de activar

1. Validar formalmente horarios, políticas de reservas, cobertura, tarifas y fecha de vigencia.
2. Cargar catálogo estructurado con productos, precios, variantes, disponibilidad e información verificable de ingredientes.
3. Confirmar medios de pago, recargo de datafono, tiempos de servicio y hora límite de pedidos.
4. Configurar el destinatario/grupo humano y la regla técnica para detener el agente cuando un humano interviene.
5. Ejecutar y documentar las pruebas del workflow 04.
