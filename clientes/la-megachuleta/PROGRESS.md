# PROGRESS — La Megachuleta

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
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.
