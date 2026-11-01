# Preguntas de aclaración — agente IA de Mercado Gastronómico Fusión

**Fecha:** 28 de octubre de 2026  
**Objetivo:** controlar las definiciones comerciales y operativas pendientes antes de cargar definitivamente el catálogo y ejecutar las pruebas del asistente.  
**Estado:** los ocho puntos prioritarios de la sección 1 ya fueron enviados por WhatsApp a Mauro; están pendientes de respuesta.

> Este es un documento interno de seguimiento. No reenviar completa la sección 1: esas preguntas ya fueron formuladas al establecimiento.

## 1. Preguntas prioritarias ya enviadas por WhatsApp

Fuente del estado: Nicolás informó que envió el mensaje a Mauro. Falta archivar una captura o export del mensaje y las respuestas para contar con evidencia verificable.

| N.º | Tema consultado | Pregunta o decisión solicitada | Estado | Respuesta validada | Evidencia |
|---:|---|---|---|---|---|
| 1 | Bebidas con precios diferentes | Precio de domicilio para Agua Manantial ($12.000/$10.000), Fuze Tea ($10.000/$11.000) y sodas saborizadas ($16.000/$14.000), incluyendo si depende de la marca | Enviada; pendiente de respuesta | — | — |
| 2 | Rolls de Sushi Fusión | Si los rolls que no aparecen en The Sushi House también se venden a domicilio y qué precio aplica | Enviada; pendiente de respuesta | — | — |
| 3 | Rolls básicos a domicilio | Confirmar The Sushi House: Filadelfia $36.000, California $35.000 y Ojo de Tigre $42.000 | Enviada; pendiente de respuesta | — | — |
| 4 | Combos de sushi | Confirmar que los combos de mesa de Sushi Fusión y los combos por bocados de The Sushi House son líneas diferentes que deben conservarse; solicitar la posible página faltante | Enviada; pendiente de respuesta | — | — |
| 5 | Productos de temporada | Vigencia de Krabb Gari, Krabb Dijon y Krabb Cream y si deben ocultarse cuando no estén confirmados | Enviada; pendiente de respuesta | — | — |
| 6 | Horarios por marca | Confirmar si las seis marcas están disponibles durante todo el horario o tienen días/franjas diferentes | Enviada; pendiente de respuesta | — | — |
| 7 | Escalamiento | Identificar la segunda persona receptora y el usuario o número que debe asociarse, además de Carlos Mauricio | Enviada; pendiente de respuesta | — | — |
| 8 | Alcance inicial | Aprobar inicio gradual: información, cartas, horarios y asesoría; toma de pedidos después de pruebas, con confirmación humana de disponibilidad, total, domicilio y pago | Enviada; pendiente de respuesta | — | — |

### Efecto de las respuestas sobre las pruebas

- Puntos 1–4: desbloquean pruebas de precios, canal, homónimos y combos (SU-01, SU-06, SU-07 y SU-08).
- Puntos 5–6: desbloquean pruebas de disponibilidad y horario.
- Punto 7: permite verificar que el escalamiento llegue al humano designado, exigencia del workflow 04.
- Punto 8: fija el límite funcional del prompt v1 y confirma que el bot no cierre total, domicilio ni pago.

## 2. Aclaraciones adicionales detectadas

Estas preguntas **no estaban incluidas** en el WhatsApp ya enviado. No todas bloquean la primera ronda: pueden agruparse en una llamada corta o resolverse durante la revisión de las pruebas.

### Prioridad alta — necesarias antes de activar

1. **Pedidos para recoger:** ¿están habilitados en la sede de Alta Suiza? Si sí, ¿tienen el mismo horario que los domicilios?
2. **Último pedido y programación:** ¿hasta qué hora se recibe el último pedido? ¿Se pueden dejar pedidos programados fuera del horario de atención?
3. **Barrios que requieren consulta:** para las zonas marcadas “en rojo”, ¿se aprueba esta respuesta?: “Voy a confirmar con el equipo si tenemos disponibilidad para tu zona; mientras tanto puedo ayudarte a armar el pedido”.
4. **Conversaciones internas:** ¿los contactos del equipo, proveedores y plataformas se identificarán mediante una lista controlada o una etiqueta en AriCRM? No registrar teléfonos en este documento.
5. **Alergias:** ¿el asistente puede orientar sin garantizar ausencia de contaminación cruzada y escalar, o debe escalar desde el primer mensaje sin recomendar productos?

### Prioridad media — necesarias para completar reservas y catálogo

6. **Reservas:** ¿cuál es la anticipación mínima y el número máximo de personas sin autorización especial? ¿Toda reserva requiere confirmación humana?
7. **Cumpleaños:** ¿sigue vigente el detalle de cortesía? Si sí, ¿qué incluye y bajo qué condiciones?
8. **Niguiris:** ¿deben ofrecerse como bundle de mesa en Sushi Fusión y como producto de The Sushi House para domicilio, o desean otra presentación?
9. **Rice To Go — papa:** ¿“Papas a la francesa 150 g” ($15.000) y “Trozos de papa frita 150 g” ($16.000) son productos diferentes o un duplicado?
10. **Entrega de cartas:** cuando el cliente pida el menú, ¿el asistente debe enviar PDF liviano, enlace web o ambos? ¿Ya están disponibles las versiones livianas definitivas de las seis cartas?

## 3. Decisiones provisionales mientras llegan las respuestas

- No publicar ni inventar precios para los puntos 1–4.
- No ofrecer como disponibles los productos de temporada del punto 5.
- Si la disponibilidad por marca no está confirmada, consultar o escalar antes de prometer un producto.
- Mantener el alcance conservador del prompt v1: el asistente asesora y arma el pedido, pero una persona confirma disponibilidad, total, domicilio y pago.
- No afirmar que existe recogida, cortesía de cumpleaños o una presentación específica de niguiri hasta recibir confirmación.
- Ante barrio incierto, alergia o conversación posiblemente interna, escalar sin inventar una respuesta operativa.

## 4. Registro de respuestas y cierre

Cuando Mauro responda:

1. Archivar captura o export de la respuesta en `evidencias/sushi-fusion/` sin exponerla fuera del expediente del cliente.
2. Completar la columna “Respuesta validada” de la sección 1.
3. Actualizar `evidencias/sushi-fusion/ia-conversacional/catalogo-skus-v1.md` y el prompt solo en los puntos confirmados.
4. Retirar el estado `🔒` únicamente de los casos de prueba que hayan quedado definidos.
5. Registrar la actualización en `PROGRESS.md`. La respuesta no autoriza por sí sola la activación en producción.

