# PROGRESS — Pizzas Beto

Bitácora cronológica de lo que se hizo, con evidencia. No borrar entradas: rectificar con nueva entrada si algo cambia.

## Formato

```
### YYYY-MM-DD — Título corto
- **Qué se hizo**:
- **Obligación asociada**:
- **Responsable**:
- **Evidencia**: ubicación (ruta al archivo, ID de acta, log ID, correo).
- **Notas**:
```

## Entradas

### 2026-10-07 — Checklist de despliegue gradual del agente IA
- **Qué se hizo**: se creó el checklist específico de Beto's Pizza para ejecutar las puertas de preparación, pruebas controladas, activación por fases y vigilancia. Se registraron como bloqueos actuales la línea pendiente de QR, la asignación pendiente del agente a la línea y la falta de validación de las fuentes operativas.
- **Obligación asociada**: 5 y 8 — preparación de C-04/C-06; no constituye activación ni prueba ejecutada.
- **Responsable**: MY SEO, a solicitud de Nicolás.
- **Evidencia**: evidencias/pizzas-beto/ia-conversacional/despliegue-2026-10-07.md.
- **Notas**: el checklist queda pendiente de completar con evidencias de conversaciones controladas, escalamiento efectivo y autorizaciones de producción.

### 2026-10-05 — Publicación de tareas de revisión en AriCRM (producción)
- **Qué se hizo**: a solicitud explícita de Nicolás, se publicaron en el tenant Beto's 7 tareas (modelo `tasks`) de prioridad alta: 6 pedidos sin respuesta (cada una vinculada a su conversación, con descripción del pedido y acción sugerida) y 1 con las 12 validaciones del menú. Objetivo: revisar los casos con el establecimiento y demostrar el funcionamiento del CRM.
- **Obligación asociada**: insumo de auditoría (2/4/5) y preparación de la sesión de validación; no configura automatizaciones.
- **Responsable**: MY SEO (creación), Nicolás (autorización de escritura y creador registrado).
- **Evidencia**: `../../evidencias/pizzas-beto/conversaciones/tareas-auditoria-publicadas-2026-10-05.md` (IDs de tareas y conversaciones).
- **Notas**: escritura limitada a la tabla `tasks`; sin `assigned_to` porque el tenant aún no tiene usuarios (C-02 pendiente). Verificadas por SELECT tras la creación.

### 2026-10-05 — Verificación en producción por SSH (solo lectura)
- **Qué se hizo**: conexión `ssh waterfall` + `tinker` autorizada por Nicolás. SELECT sobre `conversations`/`messages` del tenant Beto's: 363 conversaciones, 6.321 mensajes, 20 nuevos después del corte del export (operación activa). Las 6 conversaciones etiquetadas `pedido_abandonado` siguen `pending` y sin cerrar: nunca fueron tomadas por un humano.
- **Obligación asociada**: insumo de auditoría (obligaciones 2/4/5); no se escribió nada en producción.
- **Responsable**: MY SEO (verificación), Nicolás (autorización).
- **Evidencia**: `../../evidencias/pizzas-beto/conversaciones/verificacion-ssh-waterfall-2026-10-05.md`.
- **Notas**: diferencia pendiente de explicar: export local 6.355 mensajes vs 6.321 por join en BD. Discrepancia de timezone documentada como supuesto.

### 2026-10-05 — Etiquetado de conversaciones para auditoría y borrador de validación con el cliente
- **Qué se hizo**: (1) se extendió `scripts/analisis_conversaciones.py` para etiquetar cada conversación del export (etiquetas de toma, abandono, pedido perdido, nocturnidad y `pregunta:<categoría>`) y emitir `raw/analisis/conversaciones-etiquetadas.json` con IDs reales, que permite filtrar casos para auditoría forense individual; el reporte público incluye la distribución agregada (sección 4). (2) Se redactó el borrador de comunicación al establecimiento con las 12 validaciones pendientes del menú/operación derivadas del análisis.
- **Obligación asociada**: 2, 4 y 5 — insumo de auditoría y de cierre de brechas del menú; no configura producción.
- **Responsable**: MY SEO (análisis y borrador, a solicitud de Nicolás).
- **Evidencia**: `../../evidencias/pizzas-beto/conversaciones/raw/analisis/conversaciones-etiquetadas.json` (local, fuera de git); `borrador-validacion-menu-2026-10-05.md`.
- **Notas**: el borrador NO se ha enviado; el envío al establecimiento requiere aprobación explícita de Nicolás conforme a `POLICIES.md`. Prioridad de auditoría inmediata: las 6 conversaciones con etiqueta `pedido_abandonado`.

### 2026-10-05 — Análisis de conversaciones: oportunidades, tiempos de toma y menú
- **Qué se hizo**: se construyó un script reutilizable (`scripts/analisis_conversaciones.py`) que procesa la exportación de Waterfall y calcula: (1) oportunidades perdidas por falta de respuesta, (2) tiempo hasta la primera respuesta humana descontando la autorrespuesta, y (3) preguntas de clientes categorizadas contra el menú. Se generó el reporte cuantitativo y, con subagente, el análisis cualitativo de fricción del menú (11 elementos a aclarar).
- **Hallazgos principales**: 6 pedidos abandonados sin respuesta (5 de ellos entre 02:35 y 03:31 am); mediana de toma humana de 0 min y p90 de 3 min (operación muy rápida en horario); 28 conversaciones nunca tomadas por un humano; las fricciones de menú dominantes son mitad-y-mitad, combo gaseosa contradictorio entre fuentes, mapeo precio↔tamaño↔porciones y tarifa de domicilio por zona.
- **Obligación asociada**: 2, 4 y 5 — insumo de caracterización, del menú conversacional y del agente IA; no configura producción.
- **Responsable**: MY SEO (análisis, a solicitud de Nicolás).
- **Evidencia**: `../../scripts/analisis_conversaciones.py`; `../../evidencias/pizzas-beto/conversaciones/analisis-conversaciones-2026-10-05.md`; `../../evidencias/pizzas-beto/conversaciones/analisis-menu-cualitativo-2026-10-05.md`. Detalle con identificadores reales y preguntas redactadas solo en `raw/analisis/` (fuera de git).
- **Notas**: heurística documentada en el reporte (ventana de atención 08:00–22:00, autorrespuesta detectada por contenido); la mayoría de los turnos «sin respuesta» son despedidas de cortesía, no pérdidas. Umbrales sujetos a revisión con el establecimiento.

_(vacío inicial)_

### 2026-10-05 — Consolidación documental de caracterización
- **Qué se hizo**: se archivaron y contrastaron el formulario CSV y el documento de implementación recibidos para Beto's Pizza. Se actualizó la caracterización con la línea base disponible, tres brechas priorizadas y los campos faltantes fechados como pendientes de validación. Se detectaron discrepancias en contacto principal, horario/demanda y ticket promedio; no se resolvieron por inferencia.
- **Obligación asociada**: 2 — preparación de C-01. No constituye cierre de caracterización ni autorización para configurar producción.
- **Responsable**: MY SEO (consolidación documental).
- **Evidencia**: `../../evidencias/pizzas-beto/caracterizacion-2026-10-05.md`; fuentes: `../../evidencias/pizzas-beto/caracterizacion/fuentes/AriCRM_CCMPC-Bettos.csv` y `../../evidencias/pizzas-beto/caracterizacion/fuentes/Implementacion-ARI-MY-SEO-COMPANY.docx`.
- **Notas**: pendiente sesión de validación con el establecimiento y confirmación individual de la Cámara conforme a `workflows/01_caracterizacion.md`.

### 2026-10-05 — Transcripción y contraste de fuentes públicas
- **Qué se hizo**: se archivó la transcripción suministrada de la reunión con Alex Humberto Bedoya y se contrastó el catálogo público del sitio web. La caracterización se actualizó con los datos reportados y se registró la discrepancia entre el horario/precios públicos y los informados en reunión.
- **Obligación asociada**: 2 — C-01 queda en revisión; no se cargaron menú, precios, canales ni automatizaciones en producción.
- **Responsable**: MY SEO (organización y verificación de fuentes públicas).
- **Evidencia**: `../../evidencias/pizzas-beto/caracterizacion/transcripcion-reunion-alex-2026-10-05.md`; `../../evidencias/pizzas-beto/caracterizacion/sitio-publico-2026-10-05.md`.
- **Notas**: la transcripción no permite afirmar consentimiento inequívoco de grabación; no usarla como soporte de tal consentimiento.

### 2026-10-05 — CSV consolidado de caracterización
- **Qué se hizo**: se creó una nueva versión consolidada del formulario AriCRM_CCMPC con datos de la reunión y fuentes públicas, manteniendo el CSV recibido sin modificaciones. Cada dato pendiente o que requiere validación quedó señalado.
- **Obligación asociada**: 2 — soporte de C-01 en revisión; no es una autorización de configuración.
- **Responsable**: MY SEO (consolidación documental).
- **Evidencia**: `../../evidencias/pizzas-beto/caracterizacion/AriCRM_CCMPC-Bettos-actualizado-2026-10-05.csv`.

### 2026-10-05 — Archivo de conversación histórica de WhatsApp
- **Qué se hizo**: se archivó una versión minimizada de la conversación suministrada, que documenta la respuesta automática, el flujo de pedido, la solicitud de datos de entrega, la estimación de tiempo y la gestión de factura electrónica. Se redactaron datos personales y financieros.
- **Obligación asociada**: 2 y preparación de 4/5 — evidencia de línea base; no constituye configuración de producción ni confirmación de reglas vigentes.
- **Responsable**: MY SEO (archivo documental).
- **Evidencia**: `../../evidencias/pizzas-beto/operacion/conversacion-whatsapp-2026-08-31-2026-09-21.md`.

### 2026-10-05 — Carta recibida y catálogo estructurado
- **Qué se hizo**: se archivó la carta PDF suministrada y se transcribieron sus tamaños, sabores, otros productos, bebidas y precios en un formato estructurado para preparación del menú conversacional.
- **Obligación asociada**: 4 — preparación de C-03. No se cargó el menú ni se ejecutaron pruebas en producción.
- **Responsable**: MY SEO (archivo y estructuración documental).
- **Evidencia**: `../../evidencias/pizzas-beto/vertical-restaurantes/menu/carta-betos-recibida-2026-10-05.pdf`; `../../evidencias/pizzas-beto/vertical-restaurantes/menu/carta-betos-2026-10-05.jpg`; `../../evidencias/pizzas-beto/vertical-restaurantes/menu/menu-estructurado-carta-2026-10-05.md`.
- **Notas**: confirmar vigencia, disponibilidad por tamaño/sabor y tarifa de domicilio antes de configurar el flujo.

### 2026-10-05 — Borrador de prompt de domicilios
- **Qué se hizo**: se adaptó la plantilla institucional de asistente de domicilios al contexto de Beto's Pizza, incorporando catálogo, preguntas frecuentes, límites para tarifas/horarios y reglas de escalamiento. Se marcó como v0 hasta validación y pruebas controladas.
- **Obligación asociada**: 5 — preparación de C-04. No se activó agente IA ni se ejecutaron pruebas en producción.
- **Responsable**: MY SEO (borrador de parametrización).
- **Evidencia**: `../../evidencias/pizzas-beto/ia-conversacional/prompt-v0-borrador.md`.

### 2026-10-05 — Ajuste de bienvenida con tarifario histórico
- **Qué se hizo**: se incorporó al borrador de la secuencia de bienvenida el texto de respuesta automática suministrado, contrastado con la carta PDF. La tarifa de domicilio permanece identificada como reportada y sujeta a validación de vigencia.
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No se publicó la secuencia ni se modificó producción.
- **Responsable**: MY SEO (borrador documental).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; `../../evidencias/pizzas-beto/operacion/conversacion-whatsapp-2026-08-31-2026-09-21.md`.

### 2026-10-05 — Flags de automatizaciones V2 habilitados
- **Qué se hizo**: se habilitaron en producción, por SSH y con autorización explícita de Nicolás, los flags `automation_rule_builder_v2` y `automation_engine_v2_execute` del tenant Beto's Pizza. La verificación posterior mediante `MessagingFeatureFlags` confirmó ambos valores en `true`.
- **Obligación asociada**: preparación de C-03/C-04. Esto habilita el editor y la ejecución V2; no crea, publica ni activa reglas de automatización, y no activa el agente IA.
- **Responsable**: Nicolás autorizó; MY SEO aplicó y verificó.
- **Evidencia**: `../../evidencias/pizzas-beto/vertical-restaurantes/flags-v2-2026-10-05.md`.

### 2026-10-05 — Carta visual optimizada para WhatsApp
- **Qué se hizo**: se creó una variante móvil de la carta, con bloques de tamaños y categorías más legibles y sin teléfono, web ni redes sociales. La carta original se conserva como fuente; esta variante es un activo de envío propuesto.
- **Obligación asociada**: 4 — preparación de C-03. No se publicó ni se envió al cliente final.
- **Responsable**: MY SEO (activo visual a solicitud de Nicolás).
- **Evidencia**: `../../evidencias/pizzas-beto/vertical-restaurantes/menu/carta-betos-movil-v1-2026-10-05.png`.
- **Notas**: confirmar el diseño y la vigencia del menú con el establecimiento antes de cargarlo en una secuencia V2.

### 2026-10-05 — Exportación controlada de conversaciones de Waterfall
- **Qué se hizo**: se descargaron en modo solo lectura las conversaciones y mensajes del tenant de Beto's Pizza, bajo la excepción autorizada de protección de datos. El archivo bruto quedó local, con permisos restrictivos y excluido de Git.
- **Obligación asociada**: insumo de caracterización y parametrización; no prueba activación, atención ni desempeño del agente.
- **Responsable**: MY SEO, por autorización explícita de Nicolás.
- **Evidencia**: `../../evidencias/pizzas-beto/conversaciones/exportacion-waterfall-2026-10-05.md`.
- **Notas**: 363 conversaciones y 6.355 mensajes; no incluir contenido identificable en informes ni prompts.

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.
