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

_(vacío inicial)_

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`). Queda con placeholders porque la Cámara no ha entregado los datos del beneficiario (P-002).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: bloqueado hasta recibir datos de la Cámara; completar junto con la caracterización (C-01).

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
