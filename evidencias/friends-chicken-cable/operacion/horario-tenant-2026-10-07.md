# Verificación del horario general — Friends Chicken

- **Fecha/hora de consulta:** 2026-10-07 13:31 UTC (8:31 a. m. Colombia).
- **Método:** SSH `waterfall`, consulta de solo lectura a `tenants.business_hours` y `tenants.timezone` para Friends Chicken.
- **Zona horaria:** `America/Bogota`.
- **Lunes a sábado:** abierto, 11:00–19:30.
- **Domingo:** abierto, 09:00–17:00.
- **Fuente técnica:** tenant AriCRM Friends Chicken; evidencia de salida de consulta registrada en la sesión de trabajo. No se consultaron mensajes ni credenciales.

## Alcance y discrepancias

- Es el horario general del tenant; no es un horario almacenado por sede. La tabla `branches` aún no tiene columnas de horario ni dirección. La sede activa «Centro» no tiene línea WhatsApp vinculada.
- El borrador del agente (`evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`) indica domingo 11:00–17:00 y contiene referencias distintas para cierre de domicilios. Actualizarlo solo tras confirmar con el establecimiento qué horario aplica a atención comercial, recogida y despacho.
- La consulta confirma el valor guardado en AriCRM al momento del corte; por sí sola no acredita aceptación contractual ni garantiza que el negocio estuviera abierto en tiempo real.
