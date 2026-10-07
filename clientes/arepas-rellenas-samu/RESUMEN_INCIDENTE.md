# Resumen del incidente — Arepas Rellenas Samu

**Corte documental:** 2026-10-04. **Ámbito:** piloto del agente conversacional en la sede San Jorge. Este resumen omite datos personales y mensajes completos de clientes finales.

## Fuentes locales

- `evidencias/arepas-rellenas-samu/incidentes/2026-10-02-diagnostico-pedidos-cartas.md`: consultas de solo lectura a mensajes, pedidos, detecciones de intención y automatizaciones en AriCRM, realizadas el 2026-10-02.
- `clientes/arepas-rellenas-samu/auditoria-caso-2026-10-04.md`: auditoría de producción del 2026-10-04, incluidas las conversaciones y el estado del agente a esa fecha.
- `clientes/arepas-rellenas-samu/forense-conversacion-01a0fe7c-2026-10-04.md` y `clientes/arepas-rellenas-samu/forense-producto-por-producto-2026-10-04.md`: análisis detallados. Estos archivos locales contienen datos de clientes finales y no se incluyen en este commit.

## Hallazgos documentados

- En las primeras conversaciones del piloto se encontraron precios calculados incorrectamente por el agente, pedidos duplicados y envío repetido de la carta. Un cobro excesivo de $10.000 fue reembolsado por el establecimiento. El diagnóstico separa de estos fallos una conversación que atendió un humano y cuyo cálculo incorrecto no fue del agente.
- La conversación `01a0ff15-e42a-705f-9597-f10087dbce4f` documenta una cotización incorrecta, un cambio de ingredientes tras el cual no se repitió la solicitud de confirmación, un pedido creado cuando el restaurante estaba cerrado y una espera cercana a 50 minutos antes de la primera respuesta humana. El agente afirmó que el pedido estaba en proceso sin verificación de atención por el restaurante. En esta conversación la carta se envió una vez.
- La conversación `01a0fe7c-1072-7199-9af0-cec2b091602c` documenta una cotización correcta, seguida de la confirmación de un pedido que el restaurante no atendió oportunamente. La persona esperó alrededor de hora y media. El agente no podía consultar el estado del pedido y prometió contacto humano sin evidencia de una notificación efectiva. En esta conversación la carta se envió una vez.
- Según la auditoría del 2026-10-04, el establecimiento comunicó su retiro voluntario el 2026-10-03. A ese corte el agente figuraba desactivado. La auditoría registra el arreglo del tipo MIME de imágenes como desplegado, pero señala pendientes en validación de precios al crear pedidos, control de duplicados, horario, confirmación humana y escalamiento efectivo. Estos son estados históricos; requieren nueva verificación para afirmarlos como actuales.

## Disponibilidad de conversaciones

Los dos identificadores anteriores tienen cronologías y fragmentos en los análisis locales citados. No se encontró un export íntegro de esos chats en la carpeta del cliente. Antes de responder sobre este caso, revisar los análisis del incidente además de `PROGRESS.md` y distinguir hechos verificados, inferencias y estado actual.
