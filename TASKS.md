# TASKS

Tareas globales del programa. Las tareas por cliente viven en `clientes/<c>/TASKS.md`.

## Convención

Estados: `pendiente`, `en_progreso`, `en_revision`, `bloqueada`, `completa`.

No marcar una tarea `completa` sin enlazar evidencia o resultado verificable (acta, entregable, log, correo).

| ID | Resultado esperado | Estado | Responsable | Siguiente acción | Criterio de terminado  Evidencia |
|----|--------------------|--------|-------------|------------------|----------------------- --- |
| P-001 | Confirmar fecha efectiva de firma del contrato y calcular fechas de las 6 semanas | pendiente | Nicolás | Revisar Zoho Sign del PDF y registrar en `PROGRAMA.md` | Fecha registrada + hitos calculados en `PROGRAMA.md`  — |
| P-002 | Recibir de la Cámara la lista de los 10 establecimientos beneficiarios con contacto | en_progreso | Cámara → Nicolás | Solicitar a la Cámara los datos de Indecente (los otros 9 ya están poblados 2026-09-12) | Cada `clientes/<slug>/CLIENTE.md` con NIT, contacto principal, ciudad (9/10 completos)  — |
| P-003 | Agendar kickoff formal con la Cámara | pendiente | Nicolás | Proponer fechas | Acta de kickoff firmada en `entregables/actas/`  — |
| P-004 | Definir formato del informe individual aceptado por la Cámara | pendiente | Nicolás | Solicitar formato oficial a la Cámara; si no existe, proponer `templates/INFORME_ESTABLECIMIENTO.md` | Formato aprobado por la Cámara por escrito  — |
| P-005 | Definir formato del dashboard de seguimiento (obligación 13) | pendiente | Nicolás | Proponer versión inicial usando `templates/DASHBOARD_METRICAS.md` | Dashboard disponible y aprobado por la Cámara  — |
| P-006 | Verificar en AriCRM que el vertical restaurantes soporta menú digital + pedidos + reservas listos para 10 tenants | pendiente | Nicolás | Abrir tarea en `velo_wa` para revisar/gapear vertical | Checklist en `evals/vertical_restaurantes.md` en verde  — |
| P-007 | Definir SLA de soporte prioritario para los 4 meses posteriores a activación (obligación 11) | pendiente | Nicolás | Redactar SLA y validar con la Cámara | SLA por escrito registrado en `DECISIONS.md` y referenciado en cada `clientes/<slug>/CLIENTE.md` (sección "SLA de soporte")  — |
| P-008 | Poblar cada `clientes/<slug>/CLIENTE.md` con datos reales (NIT, contactos, canales) | pendiente | Nicolás | Completar campos faltantes en cada carpeta (10 slugs ya creados) | 10 fichas de cliente sin secciones vacías críticas (NIT, contacto principal, ciudad)  — |

## Evidencia de cierre

Para marcar `completa`, registrar en la columna Evidencia rutas concretas entre backticks, relativas a la raíz del repositorio, dentro de `evidencias/` o `entregables/`. Cada archivo debe existir y tener contenido. No usar placeholders ni el criterio de terminado como evidencia. Revisar manualmente que los archivos demuestren todos los criterios del workflow; el validador comprueba estructura y existencia, no suficiencia del contenido.
