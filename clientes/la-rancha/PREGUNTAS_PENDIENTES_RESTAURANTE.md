# La Rancha Parrilla — preguntas de clientes para FAQ y agente IA

**Estado:** inventario inicial extraído de la entrevista de caracterización, 2026-10-10. No son conversaciones reales de clientes ni pruebas ejecutadas.

**Fuente:** `../../evidencias/la-rancha/entrevista-caracterizacion-sin-fecha.md`, especialmente las preguntas frecuentes reportadas por la responsable. No se recibió un FAQ o export de conversaciones del establecimiento; cuando exista, debe contrastarse con este inventario sin copiar datos personales.

## Preguntas frecuentes identificadas

| Tema | Pregunta que podría hacer un cliente | Respuesta o tratamiento actual | Estado para el agente |
|---|---|---|---|
| Menú | ¿Cuál es el menú de hoy? | Consultar exclusivamente el menú vigente publicado ese día. | Puede resolver si existe menú vigente. |
| Menú | ¿Qué sopa y crema tienen hoy? | Depende del menú diario. | Puede resolver si existe menú vigente. |
| Proteínas | ¿Puedo escoger res, pollo o cerdo? | Sí: son las proteínas estándar reportadas; confirmar agotados del día. | Puede resolver con menú/agotados vigentes. |
| Proteínas especiales | ¿Tienen trucha, tilapia o churrasquito? | Son opciones reportadas con precio fijo, pero su disponibilidad depende del día. | Confirmar en menú vigente; escalar si falta. |
| Domingo | ¿Hoy hay fríjoles rancheros? | Se reportan los domingos; confirmar el menú del domingo. | Puede resolver con menú vigente. |
| Precio | ¿Cuánto vale el almuerzo en el restaurante? | Entre semana $19.000; fin de semana $21.000. | Puede resolver con fecha local. |
| Precio | ¿Cuánto vale a domicilio? | Entre semana $21.000; fin de semana $23.000. | Puede resolver con fecha local; no incluye una tarifa externa no verificada. |
| Ubicación | ¿Dónde quedan? | La dirección exacta no está en la fuente actual. | Escalar hasta confirmarla. |
| Horario | ¿A qué hora atienden / hasta qué hora reciben pedidos? | Servicio público reportado 11:30 a. m.–3:30 p. m.; otra fuente indica cierre 3:00 p. m. Pedidos reportados 9:30 a. m.–3:00 p. m. | Escalar hasta confirmar horario vigente. |
| Pedido | Quiero pedir almuerzo a domicilio. | Identificar menú, proteína/cantidad, zona, dirección y pago; aceptación final por el equipo. | Recoger solicitud solo cuando menú, cobertura y flujo estén verificados; no confirmar automáticamente. |
| Domicilio | ¿Llegan a mi barrio? | Zonas gratuitas reportadas: Alta Suiza, Baja Suiza, Milán, La Sultana, Palermo, La Camelia y El Cable hasta Cable Plaza. | Requiere validar fuente vigente y perímetro; otras zonas escalan. |
| Domicilio | ¿Cuánto cuesta el domicilio? | En la zona reportada no tiene costo; fuera de ella hay tabla externa no recibida. | Escalar si no existe tabla vigente disponible. |
| Domicilio | ¿Atienden Villamaría? | No quedó confirmado en la entrevista. | Escalar. |
| Entrega | ¿A qué hora llega mi pedido? | Depende del flujo; no hay SLA para prometer automáticamente. | Escalar o comunicar solo un tiempo confirmado por el equipo. |
| Pago | ¿Cómo puedo pagar? | Efectivo o transferencia con QR; QR no está disponible como fuente autorizada del agente. | Responder medios; compartir QR solo mediante fuente autorizada. |
| Reserva | Quiero reservar una mesa. | Reciben reservas por WhatsApp, teléfono y presencialmente. | Recoger fecha, hora y personas; escalar para disponibilidad. |
| Reserva | ¿Con cuánta anticipación puedo reservar / para cuántas personas? | No hay reglas recibidas. | Escalar. |
| Reclamo | Mi pedido se demoró / llegó frío / llegó incompleto / me cobraron mal. | Debe llegar a la responsable del establecimiento. | Escalamiento prioritario, con resumen y sin prometer compensación. |
| Alternativas | ¿Tienen algo diferente al menú del día? | La responsable la identifica como pregunta frecuente; no hay carta alternativa confirmada. | Escalar o responder solo si la carta vigente está disponible. |

## Preguntas que debe contestar la fuente de menú diaria

La pieza o texto diario debe permitir resolver, como mínimo:

1. ¿Qué sopa, crema, proteínas, acompañamientos y jugo hay hoy?
2. ¿Qué opción está agotada o no se ofrece hoy?
3. ¿Hay alternativas adicionales al menú estándar?
4. ¿Hay alguna excepción explícita a la regla fija de precios?

## Próximo enriquecimiento

Cuando el restaurante entregue su FAQ, respuestas rápidas o una muestra autorizada y anonimizada de consultas, agregar cada pregunta recurrente, su respuesta aprobada, la fuente y la regla de escalamiento correspondiente.
