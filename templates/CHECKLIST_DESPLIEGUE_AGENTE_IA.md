# Checklist de despliegue gradual del agente IA

**Uso:** copiar este archivo a `evidencias/<slug>/ia-conversacional/despliegue-<YYYY-MM-DD>.md` para cada establecimiento. Registrar responsable, fecha y evidencia concreta en cada punto. Un ítem sin evidencia queda pendiente. Este control complementa los criterios de los workflows 04 y 06; no los sustituye.

**Cliente / tenant / línea:** pendiente de completar

**Responsable MY SEO / responsable del establecimiento:** pendiente de completar

**Fecha y ventana de activación:** pendiente de completar

**Versión del prompt / release de AriCRM verificado en producción:** pendiente de completar

## Puerta 1 — Preparación y alcance

- [ ] Alcance aprobado con el establecimiento por escrito: qué resuelve el agente, qué escala y qué funciones se activarán primero. Guardar el soporte.
- [ ] Menú, precios, cargos adicionales, tarifas de domicilio, zonas, horarios y excepciones tienen fuente vigente confirmada por el establecimiento. Registrar fecha y archivo.
- [ ] Responsable humano está disponible durante la ventana de activación, sabe usar AriCRM y puede asumir una conversación. Registrar usuario/grupo y canal de aviso, sin credenciales.
- [ ] Existe un procedimiento de desactivación inmediata y una persona con acceso para ejecutarlo. Ensayar el procedimiento en un entorno controlado y registrar resultado.
- [ ] La versión del código y la configuración que se probaron coinciden con el release y la configuración verificados en producción. No usar un merge o un archivo local como prueba de despliegue.

## Puerta 2 — Pruebas con teléfonos controlados

Registrar por escenario: fecha, resultado esperado, resultado observado, ID técnico de conversación y captura o log sin datos personales. Las cinco conversaciones del workflow 04 deben tener clasificación correcta y escalamiento efectivo.

- [ ] Saludo y carta: la imagen se ve en el teléfono; una solicitud explícita de carta la envía una vez. Preguntar por un producto, precio o ingrediente **no** vuelve a enviar la carta.
- [ ] Pedido normal: ingredientes, cantidades y domicilio producen el total del catálogo, calculado por lógica determinista verificada en el código desplegado. El agente no inventa precios.
- [ ] Corrección posterior al resumen: el agente actualiza el pedido, muestra el nuevo total y solicita de nuevo confirmación explícita.
- [ ] Repetición o reintento: no crea dos pedidos activos para la misma intención de compra. Verificar registros en AriCRM.
- [ ] Fuera de horario o zona: no promete preparación ni entrega; comunica la limitación y ofrece el siguiente paso definido con el establecimiento.
- [ ] Queja, demora y solicitud de estado: el aviso llega realmente al humano designado con contexto; registrar la recepción. El agente no promete que alguien fue notificado si no existe confirmación técnica.
- [ ] Toma humana: cuando una persona del establecimiento responde, el agente deja de contestar esa conversación.
- [ ] Medios: validar visualmente carta y otros archivos en el teléfono controlado; `delivered` por sí solo no demuestra que se rendericen.

## Puerta 3 — Activación por fases

**Fase A — atención informativa:** bienvenida, carta y preguntas frecuentes. Mantener deshabilitada la creación y confirmación automática de pedidos hasta aprobar la fase B.

- [ ] Nicolás autoriza explícitamente cualquier cambio de configuración en producción, conforme a `POLICIES.md`.
- [ ] El establecimiento valida el contenido y conoce la hora de activación, el canal de soporte y cómo pedir desactivación.
- [ ] Activar en una sola línea y registrar hora, responsable, release, configuración y capturas o logs.
- [ ] Revisar cada conversación de la primera ventana con el responsable del establecimiento presente; registrar hallazgos y ajustes.

**Fase B — pedidos:** solo después de superar la fase A y repetir las pruebas de la Puerta 2 con la configuración exacta de producción.

- [ ] Precio calculado y validado por el sistema, no por el modelo; tarifa de domicilio separada y visible.
- [ ] Control de duplicados verificado en la herramienta de creación de pedidos.
- [ ] El restaurante recibe y acepta el pedido antes de que el agente diga «confirmado» o «en proceso» al cliente.
- [ ] Si no hay aceptación en el plazo acordado, el cliente recibe una respuesta veraz y el caso escala al humano. Probar el timeout.
- [ ] El horario y la disponibilidad del restaurante bloquean la toma de pedidos cuando no puede atenderlos.
- [ ] Nicolás autoriza la activación de la función de pedidos en producción; el establecimiento confirma la ventana operativa.

## Puerta 4 — Vigilancia y parada

- [ ] Durante las primeras 2 horas, revisar todas las conversaciones y pedidos al menos cada 15 minutos con el establecimiento; después acordar frecuencia para las siguientes 24–48 horas. Registrar quién monitorea y dónde deja evidencia.
- [ ] Desactivar el agente o la función de pedidos de inmediato ante precio incorrecto, pedido duplicado, confirmación sin aceptación del restaurante, operación fuera de horario, carta repetida, escalamiento fallido o solicitud del establecimiento. Registrar hora de solicitud y hora de desactivación efectiva.
- [ ] Revisar pedidos y conversaciones afectados, coordinar la atención humana y documentar correcciones o reembolsos sin copiar datos personales al repo.
- [ ] Reanudar solo tras identificar causa, aplicar corrección, repetir las pruebas relacionadas y obtener nueva autorización para la configuración en producción.

## Cierre de la ventana

**Resultado:** aprobado / detenido / pendiente

**Evidencias por puerta:** pendientes de completar

**Incidentes y acciones:** pendientes de completar

**Confirmación del establecimiento:** pendiente de completar

**Aprobación de Nicolás para la siguiente fase:** pendiente de completar

No marcar C-04 ni C-06 como completas por superar este checklist: aplicar además los criterios contractuales de sus workflows y archivar su evidencia específica.
