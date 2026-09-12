# Workflow 03 — Plantilla vertical restaurantes

**Obligación contractual**: Cláusula Quinta, numeral 4.
**Objetivo**: activar la plantilla vertical restaurantes en el tenant del cliente, con menú digital, pedidos, reservas, etiquetas y plantillas de respuesta.

## Precondiciones

- Tenant creado (workflow 02).
- Menú del cliente disponible (PDF, foto o listado). Si no hay, coordinar con el cliente para levantarlo.
- Reglas del cliente sobre domicilios y reservas (cobertura, costos, anticipación).

## Pasos

1. Aplicar plantilla vertical restaurantes al tenant. Verificar categorías base cargadas.
2. Cargar catálogo del cliente (productos + precios + variantes + fotos). Fuente: entregada por el cliente.
3. Configurar reglas de pedido: métodos de pago, costo/cobertura de domicilio, tiempos, horarios.
4. Configurar módulo de reservas: horarios, tamaño de grupo, política de no-show, anticipación mínima.
5. Cargar etiquetas base (nuevo, recurrente, VIP, queja, pedido, reserva) y personalizar con lo detectado en la caracterización.
6. Cargar plantillas de respuesta base + adaptaciones específicas del cliente (tono, saludo).
7. Prueba end-to-end: enviar mensaje desde un WhatsApp externo, generar un pedido y una reserva de prueba, verificar en el panel.
8. Evidencia en `evidencias/<c>/vertical-restaurantes/`.
9. Cerrar `C-04` en `TASKS.md` del cliente.

## Criterio de aceptación

- Menú completo cargado y visible desde el flujo conversacional.
- Al menos un pedido y una reserva de prueba completados end-to-end.
- Plantillas y etiquetas activas.
