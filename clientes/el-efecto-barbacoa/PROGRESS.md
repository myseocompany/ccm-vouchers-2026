# PROGRESS — El Efecto Barbacoa S.A.S.

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

_(vacío inicial)_

### 2026-09-30 — Prompt de agente consolidado en un solo archivo
- **Qué se hizo**: se integraron en el prompt de trabajo las reglas de formato WhatsApp, bienvenida, respuesta de menú y tarifa de domicilio que habían quedado en un complemento separado. El complemento se conserva solo como historial.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v3.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v3.md).
- **Notas**: este es el único archivo para parametrización; no se activó ni modificó el agente en producción. Siguen pendientes las pruebas y la validación operativa del workflow 04.

### 2026-09-30 — Pieza de felicitación para el grupo preparada
- **Qué se hizo**: se preparó una imagen vertical 9:16 (936 × 1664 px) para felicitar a El Efecto Barbacoa por el lanzamiento de su agente IA, según la indicación de Nicolás. Se usó como referencia la fotografía del menú aportada por el establecimiento y el logo blanco de Ari. La pieza quedó lista para revisión y envío por Nicolás.
- **Obligación asociada**: comunicación de acompañamiento; esta pieza no acredita por sí sola activación ni cierre de C-04/C-06.
- **Responsable**: MY SEO.
- **Evidencia**: `evidencias/el-efecto-barbacoa/materiales/felicitacion-lanzamiento-agente-ia-2026-09-30.png`.
- **Notas**: no se envió al grupo desde el harness.

### 2026-09-29 — Borrador v1 de agente IA preparado
- **Qué se hizo**: se redactó un prompt de parametrización para atención por WhatsApp, pedidos, domicilios y reservas, con escalamiento conservador a humano. Se incorporaron las reglas operativas aportadas en el formulario. No se activó ninguna configuración ni se afirmó disponibilidad de datos aún no confirmados.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v1.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v1.md).
- **Notas**: falta el menú/catálogo con precios, costo y tiempos de domicilio, medios de pago, disponibilidad de reservas, asignación técnica del responsable humano y cinco pruebas antes de que C-04 pueda cerrarse.

### 2026-09-29 — Mensaje de bienvenida recibido y archivado
- **Qué se hizo**: se archivó el texto compartido por el establecimiento para su bienvenida de WhatsApp, con enlace de menú y horarios comunicados.
- **Obligación asociada**: 2 y 5 — caracterización y referencia para parametrización del agente IA.
- **Responsable**: MY SEO (registro documental).
- **Evidencia**: [`mensaje-bienvenida-2026-09-29.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/mensaje-bienvenida-2026-09-29.md).
- **Notas**: no se configuró ni activó respuesta automática. El enlace de menú no valida por sí solo catálogo, precios ni disponibilidad para pedidos.

### 2026-09-29 — Tabla de tarifas de domicilio archivada
- **Qué se hizo**: se archivó la imagen con las tarifas de domicilio de RAPIDOMIS por zona/barrio, recibida como insumo para la operación de pedidos.
- **Obligación asociada**: 2 y 4 — caracterización y parametrización del vertical restaurantes.
- **Responsable**: MY SEO (registro documental).
- **Evidencia**: [`tarifas-domicilio-2026-09-29.md`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.md) y su imagen adjunta.
- **Notas**: pendiente confirmar vigencia, cobertura y valores con el establecimiento antes de configurarlos o comunicarlos automáticamente.

### 2026-09-29 — Tarifas de domicilio convertidas a JSON de referencia
- **Qué se hizo**: se transcribieron las tarifas por zona de la imagen a un JSON consumible por un agente IA, incluyendo la restricción de escalar valores no confirmados, zonas no listadas y el recargo de datafono cuyo monto no es legible.
- **Obligación asociada**: 4 — parametrización del vertical restaurantes.
- **Responsable**: MY SEO (preparación documental).
- **Evidencia**: [`tarifas-domicilio-2026-09-29.json`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.json).
- **Notas**: estado `pendiente_validacion_establecimiento`; no se cargó ni activó en AriCRM.

### 2026-09-29 — Prompt v2 adaptado con fuente JSON de domicilios
- **Qué se hizo**: se creó una versión de prompt específica para El Efecto Barbacoa que integra menú comunicado, horarios, reservas, flujo de pedido y reglas de consumo del JSON de tarifas.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v2.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v2.md) y [`tarifas-domicilio-2026-09-29.json`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.json).
- **Notas**: no activado. Requiere validar vigencia del menú y tarifas, configurar destinatario humano y ejecutar las pruebas antes de cerrar C-04.

### 2026-09-29 — Entrevista operativa depurada y archivada
- **Qué se hizo**: se registraron los hallazgos operativos de una entrevista de caracterización sobre atención, pedidos, domicilios, reservas, escalamiento y tono de marca.
- **Obligación asociada**: 2 y 5 — caracterización y parametrización del agente IA.
- **Responsable**: MY SEO (registro documental).
- **Evidencia**: [`caracterizacion-entrevista-2026-09-29.md`](../../evidencias/el-efecto-barbacoa/caracterizacion-entrevista-2026-09-29.md).
- **Notas**: la transcripción original contenía datos personales y no se archivó; se preservó únicamente la información operativa mínima. Sigue pendiente la validación formal del establecimiento.

### 2026-09-29 — Prompt v3 ajustado con hallazgos de entrevista
- **Qué se hizo**: se ajustó el borrador del agente para priorizar menú, tarifa por barrio, domicilios y solicitudes de reserva; se definieron escalamiento de cotizaciones y excepciones, y pausa del agente ante toma humana.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v3.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v3.md).
- **Notas**: no activado. Aún requiere validar datos operativos, configurar el grupo humano y realizar pruebas documentadas.

### 2026-09-29 — Formato visual de WhatsApp documentado para el agente
- **Qué se hizo**: se creó un complemento de prompt con el mensaje inicial diagramado, reglas de formato compatibles con WhatsApp y una respuesta estructurada para el envío de menú.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v4-formato-whatsapp.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v4-formato-whatsapp.md).
- **Notas**: no activado; requiere prueba real de renderizado en el canal antes de uso.

### 2026-09-29 — Tarifas por barrio confirmadas como fuente vigente
- **Qué se hizo**: se actualizó el estado del JSON de tarifas tras confirmación directa de Nicolás de que representa las tarifas por barrio para el agente.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA.
- **Responsable**: Nicolás (confirmación de fuente) + MY SEO (registro documental).
- **Evidencia**: [`tarifas-domicilio-2026-09-29.json`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.json).
- **Notas**: zonas no listadas y recargo de datafono continúan como casos de escalamiento.

### 2026-09-29 — JSON de tarifas incrustado en el prompt
- **Qué se hizo**: se incorporó la tabla completa de tarifas por barrio dentro del prompt v3, con la instrucción de buscar el barrio indicado y responder únicamente su valor de domicilio en COP.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v3.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v3.md).
- **Notas**: no activado; la tabla no se muestra al cliente y las zonas ambiguas/no listadas se escalan.

### 2026-09-29 — Menú recibido convertido a imágenes
- **Qué se hizo**: se convirtió el menú PDF compartido por el establecimiento en 23 imágenes PNG para preservarlo como evidencia y facilitar su estructuración posterior.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA.
- **Responsable**: MY SEO (preparación documental).
- **Evidencia**: [`menu-2026.md`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/menu-2026.md).
- **Notas**: falta estructurar y validar el catálogo antes de que el agente pueda responder detalles de productos automáticamente.

### 2026-09-29 — Menú transcrito a Markdown estructurado
- **Qué se hizo**: se creó una transcripción operativa de las categorías, productos, precios y descripciones legibles del menú PDF, con referencias de disponibilidad y datos pendientes de validar.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA.
- **Responsable**: MY SEO (preparación documental).
- **Evidencia**: [`MENU_ESTRUCTURADO_2026.md`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/MENU_ESTRUCTURADO_2026.md).
- **Notas**: no sustituye la carga/validación del catálogo en AriCRM ni habilita la activación del agente.

### 2026-09-29 — Catálogo de menú incrustado en el prompt
- **Qué se hizo**: se incorporaron al prompt las categorías, productos, precios y descripciones operativas legibles del menú estructurado, con reglas de disponibilidad y escalamiento.
- **Obligación asociada**: 5 — IA de atención automatizada con escalamiento a personal humano.
- **Responsable**: MY SEO (borrador interno).
- **Evidencia**: [`prompt-v3.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v3.md) y [`MENU_ESTRUCTURADO_2026.md`](../../evidencias/el-efecto-barbacoa/vertical-restaurantes/MENU_ESTRUCTURADO_2026.md).
- **Notas**: no activado; precios, productos con disponibilidad limitada y consultas de alergias permanecen sujetos a validación operativa.

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.

### 2026-10-11 — Línea base del prompt recuperada de producción y borrador v5 con herramientas
- **Qué se hizo**: se leyó (solo lectura) el `system_prompt` realmente desplegado y se archivó como snapshot con hash; se corrigió la nota de `prompt-v3.md` (sí estuvo en producción); se redactó `prompt-v5-tools-borrador.md`, que retira el JSON de 144 tarifas y usa `get_catalog` → UUID real → `get_delivery_fee`, sin prometer pedidos/reservas.
- **Obligación asociada**: 5 — IA de atención con escalamiento (C-04, sigue `en_progreso`; no se cierra).
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: [`prompt-produccion-2026-10-11.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-produccion-2026-10-11.md), [`prompt-v5-tools-borrador.md`](../../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v5-tools-borrador.md).
- **Notas**: agente apagado; v5 no desplegado ni aprobado por el cliente. `config.prompt_sha256` en la DB está desactualizado respecto al texto real.
