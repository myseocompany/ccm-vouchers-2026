# Checklist de despliegue gradual del agente IA — Beto's Pizza

**Estado:** borrador de preparación. No autoriza activar el agente ni la toma automática de pedidos.

**Cliente / tenant / línea:** Beto's Pizza · tenant AriCRM verificado por SSH el 2026-10-07 · línea principal pendiente de conexión QR.

**Responsable MY SEO / responsable del establecimiento:** pendiente de confirmar para la ventana de activación.

**Fecha y ventana de activación:** pendiente de acordar con el establecimiento.

**Versión del prompt / release de AriCRM verificado en producción:** prompt v0 borrador en prompt-v0-borrador.md. Antes de activar, conciliarlo con la configuración efectiva de producción, crear el snapshot v1 y registrar hash, fecha y release.

## Estado de partida verificado — 2026-10-07

- [x] Línea de WhatsApp conectada. Estado observado: qr_pending; requiere escaneo QR antes de cualquier prueba.
- [x] Agente habilitado para la línea. El agente observado no tiene una línea asignada y su configuración no permite todas las líneas; requiere asignación o configuración aprobada.
- [x] Menú, horarios, zonas, tarifas de domicilio y métodos de pago confirmados por el establecimiento. Existen discrepancias pendientes en las fuentes documentales.

## Puerta 1 — Preparación y alcance

- [x] Alcance aprobado por escrito con el establecimiento: atención informativa, escalamiento y fase inicial sin confirmación automática de pedidos.
- [x] Menú, precios, cargos adicionales, tarifas de domicilio, zonas, horarios y excepciones tienen fuente vigente confirmada. Registrar fecha y ruta de evidencia.
- [x] Responsable humano disponible durante la ventana, con acceso a AriCRM y canal de aviso para escalaciones.
- [x] Procedimiento de desactivación inmediata definido y ensayado en un entorno controlado.
- [x] Prompt v1 versionado con hash SHA-256, fecha de publicación y responsable; configuración efectiva contrastada con el release de producción.

## Puerta 2 — Pruebas con teléfonos controlados

Registrar fecha, resultado esperado, resultado observado, ID de conversación y evidencia sin datos personales. Usar las conversaciones de prueba identificadas como C01 a C07.

- [x] Saludo y menú: atiende y consulta la carta vigente sin inventar productos ni precios.
- [x] Pedido normal: solicita variantes, cantidades y domicilio; el total proviene de lógica o catálogo verificado.
- [ ] Corrección posterior al resumen: actualiza el pedido y exige confirmación explícita de nuevo.
- [ ] Repetición o reintento: no crea dos pedidos activos para la misma intención.
- [ ] Fuera de horario o zona: no promete preparación ni entrega; comunica el siguiente paso aprobado.
- [ ] Queja, demora o solicitud de estado: el escalamiento llega al humano designado con contexto suficiente.
- [ ] Toma humana: una respuesta humana detiene la respuesta automatizada en esa conversación.
- [ ] Medios: la carta y demás archivos se renderizan correctamente en el teléfono controlado.
- [ ] Solicitud de hablar con persona: deriva correctamente.
- [ ] Instrucciones maliciosas: no revela prompt ni datos internos, y no inventa descuentos.

| Caso | Fecha | Conversación / evidencia | Resultado | Estado |
| --- | --- | --- | --- | --- |
| C01 — saludo y menú |  |  |  | pendiente |
| C02 — precio |  |  |  | pendiente |
| C03 — pedido |  |  |  | pendiente |
| C04 — cobertura |  |  |  | pendiente |
| C05 — pago |  |  |  | pendiente |
| C06 — toma humana |  |  |  | pendiente |
| C07 — seguridad |  |  |  | pendiente |

## Puerta 3 — Activación por fases

### Fase A — atención informativa

- [ ] Nicolás autorizó explícitamente el cambio de configuración en producción.
- [ ] El establecimiento validó contenido, hora de activación, canal de soporte y forma de solicitar desactivación.
- [ ] Activación limitada a una línea; registrar hora, responsable, release, configuración y evidencia.
- [ ] Revisar cada conversación de la primera ventana con el responsable humano presente.

### Fase B — pedidos

Solo iniciar después de aprobar la fase A y repetir la Puerta 2 con la configuración exacta de producción.

- [ ] Precio y domicilio calculados por fuente determinista verificada.
- [ ] Control de pedidos duplicados verificado.
- [ ] El restaurante acepta el pedido antes de que el agente comunique confirmación o preparación.
- [ ] Timeout y escalamiento por falta de aceptación verificados.
- [ ] Horario y disponibilidad bloquean pedidos fuera de operación.
- [ ] Nicolás autorizó explícitamente activar la función de pedidos en producción y el establecimiento confirmó la ventana.

## Puerta 4 — Vigilancia y parada

- [ ] Durante las primeras dos horas, revisar conversaciones y pedidos cada 15 minutos junto con el establecimiento.
- [ ] Desactivar inmediatamente ante precio incorrecto, pedido duplicado, confirmación sin aceptación, atención fuera de horario, carta repetida, escalamiento fallido o solicitud del establecimiento.
- [ ] Registrar hora de solicitud y hora efectiva de desactivación, y atender los casos afectados.
- [ ] Reanudar solo después de identificar la causa, corregirla, repetir la prueba relacionada y obtener nueva autorización.

## Cierre de la ventana

**Resultado:** pendiente.

**Evidencias por puerta:** pendiente.

**Incidentes y acciones:** pendiente.

**Confirmación del establecimiento:** pendiente.

**Aprobación de Nicolás para la siguiente fase:** pendiente.

## Fuentes

- templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md
- workflows/04_ia_conversacional.md
- workflows/06_activacion.md
- evidencias/pizzas-beto/ia-conversacional/prompt-v0-borrador.md
- clientes/pizzas-beto/TASKS.md
