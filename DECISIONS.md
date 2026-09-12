# DECISIONS

Registro cronológico de decisiones aprobadas que afectan el programa. Una vez registrada, una decisión no se borra: se anota su reversión con nueva entrada.

## Formato

```
### YYYY-MM-DD — Título corto
- **Contexto**: qué desencadenó la decisión.
- **Alternativas consideradas**: opciones que se evaluaron.
- **Decisión**: qué se decidió.
- **Responsable**: quién decidió / quién aprobó.
- **Impacto contractual**: obligación / cláusula afectada, si aplica.
- **Fuente**: correo, acta, reunión (con enlace o ubicación).
```

## Entradas

### 2026-09-12 — Correcciones tras auditoría inicial del harness
- **Contexto**: auditoría del scaffolding recién creado identificó 6 hallazgos (3 Alta, 3 Media): criterios de aceptación laxos que permiten cierres prematuros, ausencia de tareas de post-implementación y soporte, C-02 pedía credenciales violando POLICIES, precondición del workflow 01 dependía del listado completo de la Cámara, doble estado editable entre CLIENTE.md y TASKS.md, y referencias a archivos inexistentes.
- **Decisión**:
  - `clientes/_template/TASKS.md`: los criterios de aceptación por tarea replican textualmente los del workflow correspondiente. Se agregaron C-07 (licenciamiento 4m), C-08 (soporte SLA), C-09 (informe individual con acuse), C-10 (cierre de período). C-02 sustituyó "solicitar credenciales" por "invitaciones desde AriCRM + conexión asistida por operador del establecimiento sin recepción de contraseñas".
  - `clientes/_template/CLIENTE.md`: se agregaron hitos temporales con evidencia (activación efectiva, licenciamiento inicio/fin, informe, cierre soporte). Se eliminó la tabla "Estado" — TASKS.md es la fuente canónica.
  - `workflows/01_caracterizacion.md`: precondición ahora exige confirmación específica del cliente por la Cámara, no P-002 global.
  - `evals/vertical_restaurantes.md` y `evals/README.md`: creados para respaldar P-006.
  - `scripts/validate.sh`: validador local que revisa archivos raíz, carpetas, 10 clientes, workflows, templates, referencias .md rotas, campos vacíos de CLIENTE.md y tareas "completa" sin evidencia.
  - Correcciones de referencias rotas en workflow 06, README, TASKS, templates y VOLUNTEER.en.md.
  - Templates re-propagados a los 10 clientes (CLIENTE.md, TASKS.md, CARACTERIZACION.md sobreescritos; INFORME.md y PROGRESS.md preservados).
- **Responsable**: Nicolás (aprobó la auditoría) + Claude Code (aplicó).
- **Impacto contractual**: refuerza trazabilidad de cumplimiento (reduce riesgo de cierres sin evidencia) y aísla mejor la ejecución por cliente (reduce bloqueos cruzados).
- **Fuente**: auditoría reportada en conversación 2026-09-12; validador corrió con 0 errores críticos.

### 2026-09-12 — Estructura del harness del programa
- **Contexto**: Necesidad de coordinar cumplimiento del contrato CT-239-26-3 con evidencia por cliente y por obligación.
- **Alternativas consideradas**:
  - Reusar `myseo-env` con `clients/ccm-vouchers-2026/` (rechazado: mezclaría un contrato específico con el harness transversal de MySEO).
  - Meter la gestión del programa dentro del repo `velo_wa` (rechazado: contamina el producto AriCRM con obligaciones de un solo contrato y complica la posición de propiedad intelectual).
  - Harness propio en `/Volumes/ExternoMS/projects/ccm-vouchers-2026/` (elegido).
- **Decisión**: Harness independiente en `ccm-vouchers-2026/`, con estructura inspirada en `myseo-env` (AGENTS/SOUL/POLICIES + clientes/ + workflows/ + templates/). El código de AriCRM permanece en `velo_wa` y este harness no lo modifica.
- **Responsable**: Nicolás.
- **Impacto contractual**: Ninguno directo. Refuerza la posición de propiedad intelectual (Cláusula 17): AriCRM es producto preexistente separado del contrato.
- **Fuente**: Conversación con Claude Code, 2026-09-12.
