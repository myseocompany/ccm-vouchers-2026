# Evidencia de conversación WhatsApp — Beto's Pizza

**Período de la conversación:** 2026-08-31 a 2026-09-21  
**Origen:** transcripción suministrada por el usuario.  
**Tratamiento de datos:** se redactaron dirección, teléfonos, correo y datos bancarios; no son necesarios para la parametrización.  
**Alcance:** evidencia histórica de la operación y del flujo conversacional. No acredita precios, horarios ni métodos de pago vigentes para producción.

## 2026-08-31 — Respuesta automática observada

Ante la consulta “pizza”, el establecimiento respondió:

> Gracias por comunicarte con Beto's Pizza. ¿Cómo podemos ayudarte?

La respuesta automática listaba esta oferta y precios en ese corte:

| Producto / tamaño | Precio informado | Nota |
|---|---:|---|
| Porción (hawaiana o carnes) | $10.000 | — |
| Personal (cuatro porciones pequeñas) | $20.000 | — |
| Pizza S (seis porciones pequeñas) | $28.000 | — |
| Mediana (ocho porciones pequeñas) | $55.000 | Incluye gaseosa |
| Familiar (ocho porciones grandes) | $80.000 | Incluye gaseosa |
| Maiz S / M | $14.000 / $18.000 | — |
| Lasaña S / M | $15.000 / $19.000 | Mixtas: pollo, boloñesa, champiñones |
| Domicilio | $5.000 | Tarifa histórica publicada |

También se envió un mensaje de ausencia: “En este momento no podemos responder, pero lo haremos lo antes posible.”

## 2026-09-21 — Flujo de pedido observado

1. Ante “Dame un Small”, el establecimiento pidió el sabor.
2. Para una pizza S de carnes, solicitó dirección y luego envió una plantilla para diligenciar: producto, dirección, barrio, nombre, teléfono y devolución/cambio.
3. Ante consulta por medios de pago, compartió instrucciones de transferencia y pagos digitales. **Los números de cuenta, llave y teléfonos fueron redactados.**
4. Informó un tiempo estimado de entrega de aproximadamente 45 minutos.
5. Informó un total de $33.000, incluido domicilio, para el pedido de pizza S de carnes; coincide con $28.000 + $5.000 del tarifario histórico.
6. Confirmó que emite factura electrónica y solicitó correo electrónico y teléfono para gestionarla.

## Implicaciones para el bot

- Puede orientar sobre tamaños, sabores, carta y flujo de toma de pedido, pero debe pedir los datos de entrega solo cuando el cliente decida ordenar.
- No debe enviar números de cuenta, llaves, teléfonos ni instrucciones de pago desde conocimiento no validado. Debe escalar o usar una fuente de pagos vigente aprobada por el establecimiento.
- El tiempo de “45 minutos”, el domicilio de $5.000 y los precios son una **referencia histórica**; el bot debe verificar zona, demanda y tarifario vigente antes de confirmarlos.
- Las solicitudes de factura electrónica deben escalar a una persona humana para el manejo seguro de datos de facturación.
