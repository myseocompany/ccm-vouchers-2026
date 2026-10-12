# PROGRESS — La Patateria

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

### 2026-10-12 — Extracción del catálogo (carta digital bibisoft)
- **Qué se hizo**: se descargó la carta digital publicada del establecimiento desde la API pública de bibisoft (endpoint `list-products-marketplace`, store_id=63, menu_id=12, resueltos vía `menu/list/?url=patateria`). Se guardó el crudo y se generaron versiones legibles. Resultado: 8 categorías y 46 productos (todos activos y visibles en menú).
- **Obligación asociada**: 2 — C-01, insumo de caracterización (sección Menú).
- **Responsable**: MY SEO (agente LLM del harness), a solicitud de Nicolás.
- **Evidencia**: `carta/productos.json` (crudo), `carta/carta.md`, `carta/carta.csv`. Fuente: `https://patateria.bibisoft.co/tienda/productos`.
- **Notas**: no es la validación de la "carta nueva": queda pendiente confirmar con el establecimiento si este catálogo publicado es el definitivo y la vigencia de precios. El crudo proviene del catálogo (no incluye datos operativos sensibles del local); el endpoint hermano `menu/list` sí expone WhatsApp/IP local, por lo que no se versionó esa respuesta.

### 2026-10-12 — Incorporación y extracción inicial del formulario de caracterización
- **Qué se hizo**: se copió el CSV entregado por Nicolás a la carpeta de evidencia del cliente y se trasladaron a `CARACTERIZACION.md` los datos operativos reportados. Se distinguieron datos reportados, hipótesis y pendientes fechados; se priorizaron cuatro brechas digitales.
- **Obligación asociada**: 2 — C-01, caracterización inicial.
- **Responsable**: MY SEO (agente LLM del harness), a solicitud de Nicolás.
- **Evidencia**: `../../evidencias/la-patateria/caracterizacion/AriCRM_CCMPC-patateria-2026-10-12.csv`; `../../evidencias/la-patateria/caracterizacion/extraccion-2026-10-12.md`; `CARACTERIZACION.md`.
- **Notas**: C-01 queda `en_progreso`. El formulario carece de confirmaciones finales y mantiene pendientes operativos; no se considera caracterización cerrada ni autorización para configurar producción.

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.
