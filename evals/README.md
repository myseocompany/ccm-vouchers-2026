# Evals

Checklists de verificación por vertical, por obligación y por integridad del harness. Se ejecutan manualmente o vía `scripts/validate.sh`.

## Convención

Cada eval es un archivo Markdown con:

- **Objetivo**: qué se verifica.
- **Precondiciones**: qué debe existir antes de correrlo.
- **Checklist**: puntos concretos (usar `[ ]` / `[x]`).
- **Criterio global**: cuándo se considera aprobado.

Un eval en verde no aprueba automáticamente una tarea del contrato: es insumo para el responsable, no reemplazo del criterio del workflow.
