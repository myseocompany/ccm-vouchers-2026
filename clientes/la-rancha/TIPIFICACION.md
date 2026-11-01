# La Rancha Parrilla — propuesta de tipificación en AriCRM

**Estado:** propuesta documental del 2026-10-10, derivada de `CARACTERIZACION.md`. No consta carga ni activación en el tenant. Validar con el establecimiento y comprobar las capacidades reales de AriCRM antes de configurar reglas automáticas.

## Categoría principal de conversación

Asignar **una categoría principal** según el motivo que el cliente expresa. Si aparecen varios motivos, priorizar el que requiere atención humana y conservar los demás como temas secundarios cuando AriCRM lo permita.

| Categoría propuesta | Cuándo usarla | Manejo propuesto |
|---|---|---|
| `Consulta · menú y precios` | Pregunta por el menú del día, alternativas, precio o disponibilidad. | Responder solo con el menú vigente y su fecha; si falta, pedir actualización al equipo. |
| `Consulta · ubicación y horario` | Pregunta dónde están o cuándo atienden. | Responder cuando dirección y horario estén confirmados. |
| `Pedido · domicilio` | Solicita comida con entrega. | Recoger producto, cantidad, dirección/zona y pago; validar menú, disponibilidad, tarifa y tiempo antes de confirmar. |
| `Pedido · para llevar` | Pide comida para recoger. | Confirmar si el servicio existe y su precio antes de automatizar. |
| `Reserva` | Solicita mesa o modifica una reserva. | Solicitar fecha, hora y número de personas; confirmar disponibilidad con el equipo hasta definir reglas. |
| `Reclamo · pedido o servicio` | Informa demora, faltante, cambio, comida derramada, plato frío o cobro incorrecto. | Escalar a la responsable del establecimiento con resumen y contexto; no cerrar automáticamente. |
| `Proveedor` | Ofrece productos, consulta compras o coordina pedidos de abastecimiento. | Pasar a atención humana; no tratar como pedido de cliente. |
| `Administrativo` | Cotización especial, contratación u otro asunto administrativo. | Pasar a la responsable; no enviar automáticamente a la línea personal reportada. |
| `Otro / por aclarar` | Intención insuficiente o fuera de las categorías anteriores. | Pedir una aclaración breve y escalar si no se resuelve. |

## Datos y estados útiles

- **Datos de pedido:** fecha del menú consultado, opción, cantidad, consumo en sitio / domicilio / para llevar, zona, tarifa confirmada y medio de pago. Registrar únicamente lo necesario para prestar el servicio.
- **Datos de reserva:** fecha, hora, número de personas y confirmación humana mientras falten reglas de disponibilidad.
- **Estados sugeridos:** `nuevo`, `en atención`, `esperando confirmación del restaurante`, `confirmado`, `resuelto`. Son una propuesta; mapearlos a los estados existentes de AriCRM para evitar duplicar conceptos.
- **Prioridad humana:** reclamos por cobro, pedido no recibido o incorrecto, comida derramada o fría y demoras; además, alergias o seguridad alimentaria si aparecen, aunque la entrevista no definió una política específica.

## Condiciones previas a la publicación

1. Confirmar con el establecimiento la taxonomía y quién recibe cada escalamiento.
2. Confirmar horario, dirección, menú vigente, precios, recogida, zona gratuita y tabla de tarifas externas.
3. Verificar tenant, usuarios, línea conectada y funciones de etiquetas/tipificación en AriCRM.
4. Probar al menos una conversación por categoría y una de reclamo; conservar evidencia en `../../evidencias/la-rancha/`.

**Fuentes:** formulario local `AriCRM_CCMPC - LaRancha.csv` y `../../evidencias/la-rancha/entrevista-caracterizacion-sin-fecha.md`. Las categorías y estados son **propuestas de parametrización**, no decisiones aprobadas ni configuraciones verificadas.
