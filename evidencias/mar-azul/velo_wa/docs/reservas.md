# Calamar Azul — reglas de reserva

Reglas de negocio de reservas de mesa, reportadas por el cliente el **2026-10-30**. Esta página es la fuente canónica; el `system_prompt` del agente debe derivarse de aquí, no al contrario.

## Ventana de reserva

| Regla | Valor |
|---|---|
| Días | Lunes a sábado |
| Franja | **2:00 p. m. – 4:30 p. m.** |
| Retención de la mesa | 30 minutos |
| Excepciones por fecha | Fechas especiales como el Día de la Madre: no se reserva |
| Eventos empresariales | **Sí se pueden pactar en otros horarios**, fuera de la franja de 2:00–4:30 p. m. |
| Costo | $20.000 la reserva · $30.000 la reserva con decoración |

La franja encaja con la operación: atención al público de 11:00 a. m. a 5:00 p. m., así que 4:30 p. m. es el último acomodo antes del cierre.

## Por qué la franja arranca a las 2:00 p. m.

Por el **alto flujo del restaurante** en el almuerzo. Antes de las 2:00 p. m. la ocupación la absorbe la demanda de mesa por orden de llegada, así que comprometer mesas en ese pico le quita puestos a gente que ya está en el local.

El problema que esto gestiona es el **no-show**: la mesa se separa, el cliente no llega, y el restaurante queda con una mesa bloqueada que necesitaba agendar. De ahí los 30 minutos de retención y el costo de la reserva: ambos existen para que la reserva tenga respaldo y no se pierda el puesto.

## Qué hace el agente IA

El agente **no confirma** reservas. Toma la solicitud (fecha, hora, número de personas, ocasión) y la escala a la cajera en turno, que es quien confirma valor, decoración y pago. `reserva` y `decoración` están en la lista de escalamiento obligatorio del prompt.

## Diferencias con el prompt vivo (pendiente de corregir)

El `system_prompt` en producción (capturado el 2026-10-30, SHA-256 `4c21a851…`) dice:

> «Se aceptan de lunes a sábado después de las 2:00 p. m., excepto fechas especiales como Día de la Madre, y se conservan 30 minutos.»

Dos vacíos frente a lo reportado por el cliente:

1. **Falta el tope de 4:30 p. m.** El prompt dice «después de las 2:00 p. m.», abierto. Tal como está, el bot podría tomar una solicitud para las 4:45 p. m. o para una hora posterior al cierre.
2. **No menciona los eventos empresariales.** Hoy el bot no sabe que un evento corporativo puede pactarse fuera de la franja, así que trataría esa petición como fuera de horario en vez de escalarla como la excepción que es.

Ambos se arreglan en la próxima versión del prompt (`docs/mar-azul/prompts/asistente-whatsapp/`), siguiendo la convención de versionado de AGENTS.md: nuevo snapshot con hash, sin sobrescribir el anterior.
