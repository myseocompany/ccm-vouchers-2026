# PROGRESS — Indecente

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

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`). Queda con placeholders porque la Cámara no ha entregado los datos del beneficiario (P-002).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: bloqueado hasta recibir datos de la Cámara; completar junto con la caracterización (C-01).

### 2026-10-09 — Formulario inicial procesado
- **Qué se hizo**: se copió localmente y procesó el formulario de caracterización; se trasladaron a `CLIENTE.md` y `CARACTERIZACION.md` únicamente los datos sustentados, y los faltantes quedaron fechados como pendientes. Se identificaron cuatro brechas digitales preliminares.
- **Obligación asociada**: obligación 2 — caracterización inicial.
- **Responsable**: Nicolás Navarro Rincón / información suministrada por Indecente.
- **Evidencia**: `../../evidencias/indecente/caracterizacion-2026-10-09.md`; fuente cruda local excluida de Git: `../../evidencias/indecente/insumos/AriCRM_CCMPC - Indecente.csv`.
- **Notas**: C-01 queda `en_progreso`; el formulario no satisface todavía el criterio de cierre.

### 2026-10-09 — Mensaje de bienvenida registrado
- **Qué se hizo**: se guardó el texto propuesto de bienvenida para WhatsApp, sin publicarlo ni configurarlo en producción.
- **Obligación asociada**: obligaciones 4 y 5 — vertical restaurantes e IA conversacional.
- **Responsable**: Nicolás Navarro Rincón.
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`.
- **Notas**: pendiente de aprobación y prueba antes de activar el disparador de conversación nueva.

### 2026-10-09 — Carta visual archivada y transcrita
- **Qué se hizo**: se archivó la imagen recibida y se transcribieron tres perritos y dos referencias de bebidas con sus precios e ingredientes visibles.
- **Obligación asociada**: obligación 4 — plantilla vertical restaurantes / menú digital.
- **Responsable**: Nicolás Navarro Rincón.
- **Evidencia**: `CARTA.md` y `../../evidencias/indecente/menu/carta-indecente-2026-09-22.jpg`.
- **Notas**: antes de cargar en AriCRM se debe confirmar vigencia, alcance completo, variantes, agotados y el significado de “Otras”.

### 2026-10-09 — Prompt principal v1 preparado
- **Qué se hizo**: se preparó un borrador de prompt para fase A: información de la carta, toma preliminar de solicitud y escalamiento a humano. No crea ni confirma pedidos automáticamente.
- **Obligación asociada**: obligación 5 — agente IA con escalamiento a humano.
- **Responsable**: Nicolás Navarro Rincón.
- **Evidencia**: `../../evidencias/indecente/ia-conversacional/prompt-v1.md`.
- **Notas**: pendiente de validación del establecimiento, configuración, pruebas controladas y autorización específica de activación.

### 2026-10-09 — Catálogo digital creado y verificado
- **Qué se hizo**: se crearon en el tenant INDECENTE las categorías Perritos y Bebidas, con cinco productos activos conforme a la carta visual: Gringo, Mero Mero, Perrini, Gaseosa pequeña y Otras.
- **Obligación asociada**: obligación 4 — plantilla vertical restaurantes / menú digital.
- **Responsable**: Nicolás Navarro Rincón.
- **Evidencia**: `../../evidencias/indecente/vertical-restaurantes/catalogo-2026-10-09.md`.
- **Notas**: no se configuraron productos no verificados, modificadores, disponibilidad en tiempo real, tarifas de domicilio ni automatización de pedidos. C-03 continúa `en_progreso` hasta realizar las pruebas requeridas por el workflow.

### 2026-10-09 — Sede principal creada y asociada
- **Qué se hizo**: se creó la sede activa “Sede principal” en AriCRM y se asoció a la línea Principal conectada. La dirección física fue registrada en la ficha del establecimiento.
- **Obligación asociada**: obligaciones 3 y 6 — configuración del tenant e integración de canal.
- **Responsable**: Nicolás Navarro Rincón.
- **Evidencia**: `../../evidencias/indecente/config-tenant/sede-principal-2026-10-09.md`.
- **Notas**: no se configuraron tarifas de domicilio; la sede no almacena dirección como campo técnico dentro de AriCRM.

### 2026-10-25 — Formulario incorporado y corrección operativa del agente
- **Qué se hizo**: se archivó el formulario de INDECENTE, se contrastó con el incidente conversacional reportado por Paola y se actualizaron la ficha, la caracterización y las tareas. Se preparó el horario general del tenant y el prompt v4 con reglas de horario, recogida y cobertura honesta.
- **Obligaciones asociadas**: 2, 3, 4, 5 y 6 — caracterización, configuración, vertical restaurantes, IA y canales.
- **Responsable**: Nicolás Navarro Rincón / MY SEO; fuente operativa del establecimiento: María Josefina Salazar Lopera y Paola Haya.
- **Evidencia**: `../../evidencias/indecente/caracterizacion/AriCRM_CCMPC-Indecente-2026-10-25.csv`, `../../evidencias/indecente/caracterizacion/resumen-validacion-2026-10-25.md`, `../../evidencias/indecente/ia-conversacional/prompt-v4.md` y `../../evidencias/indecente/ia-conversacional/prompt-v4.1.md`.
- **Notas**: el cierre del sábado fue escrito como 3:00 p. m.; se usa provisionalmente 3:00 a. m. por coherencia con el turno nocturno y debe confirmarse. El modelo actual de AriCRM no permite guardar horario por sede ni cierres excepcionales por fecha; al existir una sola sede, el horario se configura temporalmente a nivel tenant.

### 2026-10-25 — Corte amable de pedidos 20 minutos antes del cierre
- **Qué se hizo**: a partir del segundo reporte de Paola, se añadió al prompt v4.1 una ventana de cierre de 20 minutos. El agente no inicia pedidos nuevos en esa ventana; ofrece la carta para el próximo turno y, si el pedido ya estaba detallado, escala para confirmación humana sin prometer aceptación.
- **Obligaciones asociadas**: 4 y 5 — vertical restaurantes y agente IA.
- **Responsable**: Nicolás Navarro Rincón / MY SEO; fuente operativa: Paola Haya.
- **Evidencia**: `../../evidencias/indecente/ia-conversacional/prompt-v4.1.md`.
- **Notas**: el corte vive por ahora en la configuración del agente (`order_cutoff_minutes=20`). Una protección determinista en creación de pedidos requerirá evolución del producto.

### 2026-10-26 — Bienvenida automática neutralizada
- **Qué se hizo**: se detectó que la automatización activa `enviar_carta` enviaba “¿Qué te llevamos?” en toda conversación nueva, sin condición de horario. Tras una reactivación posterior desde la operación, se conservó activa pero su texto se cambió por una bienvenida neutral que anuncia que primero se revisará el horario; el agente v4.2 decide después si puede iniciar un pedido.
- **Obligaciones asociadas**: 4 y 5 — vertical restaurantes y agente IA.
- **Responsable**: Nicolás Navarro Rincón / MY SEO.
- **Evidencia**: `../../evidencias/indecente/ia-conversacional/prompt-v4.2.md` y verificación de producción del 2026-10-26.
- **Notas**: la condición `business_hours` de automatizaciones V2 no interpreta actualmente el formato moderno `enabled/blocks`; por seguridad no se añadió una condición incompatible. La automatización conserva la imagen de bienvenida, pero ya no pregunta “¿Qué te llevamos?” antes de verificar horario y corte.
