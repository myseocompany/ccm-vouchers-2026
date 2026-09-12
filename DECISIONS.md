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

### 2026-09-12 — Corrección de cierres y validación de evidencias
- **Contexto**: segunda auditoría detectó IDs de cierre desalineados, aceptación de rutas genéricas como evidencia, omisión de conformidad de soporte y placeholders no detectados.
- **Decisión**: corregir los IDs de seis workflows; añadir Evidencia a tareas globales, plantilla y diez clientes; rechazar cierres sin archivos concretos existentes y no vacíos; detectar campos básicos pendientes sin imprimir sus valores; exigir conformidad escrita de soporte en C-08/C-10.
- **Responsable**: Nicolás autorizó la corrección; Codex la implementó.
- **Impacto**: controles documentales; no cambia estados de avance ni configuraciones de producción. La suficiencia del contenido probatorio sigue requiriendo revisión humana.
- **Fuente**: auditoría y autorización «hazlo» en esta conversación, 2026-09-12.

### 2026-09-12 — Poblado inicial de 9 CLIENTE.md desde tabla de la Cámara + tercera auditoría
- **Contexto**: la Cámara envió tabla con datos de 10 establecimientos. 9 coinciden con los slugs previamente creados; Indecente NO aparece; Sevicheria El Costeño DG aparece con datos completos pero no está en la lista original de 10. Contexto crítico: todos los diagnósticos son por sismo (daño estructural severo, colapso, operación desde casas).
- **Decisión**:
  - Poblar los 9 CLIENTE.md coincidentes con NIT/cédula, contacto principal, dirección, canal WhatsApp y "Contexto pre-caracterización" (afectación por sismo + operación actual).
  - Normalizar campo `**NIT/Cédula**` → `**NIT**` para que el validador lo detecte.
  - Levantar discrepancia a Nicolás: qué hacer con Indecente (sin datos) y Sevicheria El Costeño DG (con datos, no en lista). Pendiente de decisión.
  - Tercera auditoría (2026-09-12): 6 workflows cerraban IDs de tarea equivocados (heredado del scaffolding inicial, antes de que Codex reordenara los C-XX). Corregido: 02→C-02, 03→C-03, 04→C-04, 05→C-05, 06→C-06, 08→C-09. 07_soporte_sla cubre C-07/C-08/C-10 (continuas durante 4 meses, no se "cierran" en un paso).
  - Alta 2 de la tercera auditoría (validador acepta cierres sin evidencia real) verificada como resuelta por Codex: bash validate.sh sale con exit 1 cuando una tarea se marca completa sin evidencia.
- **Responsable**: Nicolás autorizó ("dale"); Claude Code implementó.
- **Impacto contractual**: los datos poblados quedan bajo la política de protección de datos personales (Ley 1581/2012). Repo privado en GitHub. Discrepancia Indecente/Sevicheria bloquea confirmación total de la obligación 2 hasta que se decida.
- **Fuente**: tabla enviada por Nicolás con datos de la Cámara (registros de llamada 26–31/08/2026); auditoría reportada en conversación 2026-09-12.

### 2026-09-12 — Resolución discrepancia Indecente / Sevichería El Costeño DG
- **Contexto**: la tabla de la Cámara del 2026-09-12 incluía datos de "Sevichería El Costeño DG" (que no estaba en la lista original de 10) y omitía datos de "Indecente" (que sí estaba).
- **Decisión**: Sevichería no entra en la lista. Indecente se mantiene como uno de los 10 beneficiarios; los datos de contacto llegan después. La carpeta `clientes/indecente/` queda con placeholder hasta que se reciban.
- **Responsable**: Nicolás, 2026-09-12.
- **Impacto contractual**: los 10 beneficiarios siguen siendo los originalmente registrados. La obligación 2 (caracterización) para Indecente queda bloqueada hasta que llegue la información.
- **Fuente**: instrucción directa en conversación 2026-09-12.
