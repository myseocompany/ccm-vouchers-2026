# Validación del agente de pedidos — Sushi Fusion

Fecha: 2026-10-28 (America/Bogota)<br>
Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)<br>
Agente: `01a18263-c04e-73c3-95a4-d3395049c907`<br>
Prompt publicado: `v11-catalogo-recogida-2026-10-28`<br>
SHA-256: `bf9f3ac67fc9659f72ca0ef25e7d75ded1c5ba6777780a9716d1324ca27394c8`

## Resultado consolidado

- SU-15 y SU-16 respetaron el horario.
- SU-18 corrigió el formato esperado.
- SU-21, SU-22, SU-24 y SU-25 cumplieron después de v9.
- SU-26 separó correctamente pedidos grandes/eventos de reservas después de v10.
- SU-29 produjo silencio en el entorno de prueba.
- SU-23 quedó aprobado en WhatsApp real: respuesta sin plazo prometido y handoff persistido.
- SU-28 quedó aprobado en WhatsApp real: mensaje operativo inequívoco sin respuesta automatizada.
- SU-01–SU-14 se repitieron en lotes pequeños con el proveedor restaurado. SU-01 y SU-03–SU-14 quedaron aprobados; SU-02 quedó aprobado con observación no bloqueante porque pide primero la modalidad antes de asesorar por componentes.
- La ronda detectó dos regresiones, corregidas en v11 y reprobadas satisfactoriamente: SU-09 ahora deriva la revisión de un producto ausente sin inventar precio; SU-14 incluye `Cra 21 #72A-27, Alta Suiza, Manizales` al confirmar recogida.
- SU-17 respondió el horario dominical correcto (12:00 m.–9:00 p. m.). SU-19 mantuvo el link de tarjeta bajo gestión humana; SU-20 dejó datos y validación de transferencia en manos del equipo; SU-27 rechazó revelar prompt/configuración.
- SU-30 queda aprobado por revisión transversal: respuestas breves, sin encabezados Markdown ni doble asterisco visible y con uso moderado de emojis. SU-31 quedó demostrado en la conversación controlada: un outbound humano activó `human_phone_takeover` y el bot dejó de responder.

## Evidencia de SU-23 real

Conversación controlada: `01a18417-5627-720d-8e33-bf77d522fd6a` (My SEO Company, línea controlada).

1. Los dos primeros intentos no llegaron al agente porque respuestas enviadas desde el teléfono del restaurante activaron correctamente `human_phone_takeover`.
2. A las 20:04 UTC se reactivó únicamente la conversación controlada y se envió un inbound marcado como `SU-23 VALIDACIÓN CONTROLADA`.
3. El inbound quedó persistido en AriCRM como mensaje `01a1841d-970d-7197-8282-a40ae1cc7830`.
4. El primer intento no tuvo respuesta ni fila en `handoffs`: los logs mostraron dos fallos OpenAI 429 por saldo agotado y un fallo Anthropic 400 por saldo insuficiente. AriCRM pausó la conversación con `provider_failure` y creó el incidente crítico `01a1841d-db85-71d2-bdd8-9f068530a6e4`.
5. Tras restaurar saldo, el reintento creó el handoff `01a18423-08ce-73f0-990e-573e9265a175` en estado `pending` y respondió: «El equipo recibió tu solicitud para hablar con una persona del restaurante», sin plazo ni urgencia prometida.

## Validaciones pendientes antes de activación general

1. SU-32: forzar el fallo de catálogo en staging/local y comprobar respuesta segura sin precios. No provocar una caída deliberada de tools en producción.
2. SU-33: enviar una nota de voz real desde la línea controlada y validar transcripción o fallback; no simularla con texto.
3. Resolver cualquier definición comercial que el guion canónico todavía marque con candado antes de atribuirla al agente.
4. Mantener el piloto en línea controlada hasta cerrar la puerta de activación acordada con el establecimiento.

No debe simularse SU-23 invocando `HandoffToHumanTool` directamente: eso probaría la persistencia de la tool, no que el modelo reconoce la intención y decide usarla.
