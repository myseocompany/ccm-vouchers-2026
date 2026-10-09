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
