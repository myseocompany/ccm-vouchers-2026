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
| P-004 | Definir formato del informe individual aceptado por la Cámara | pendiente | Nicolás | Formato oficial recibido 2026-10-29: `templates/INFORME_CAMARA_OFICIAL.docx` (informe de avance; llenado según `workflows/08_informes.md`). Confirmar si aplica también al informe individual (obl. 15) | Formato aprobado por la Cámara por escrito  — |
| P-005 | Definir formato del dashboard de seguimiento (obligación 13) | pendiente | Nicolás | Proponer versión inicial usando `templates/DASHBOARD_METRICAS.md` | Dashboard disponible y aprobado por la Cámara  — |
| P-006 | Verificar en AriCRM que el vertical restaurantes soporta menú digital + pedidos + reservas listos para 10 tenants | pendiente | Nicolás | Abrir tarea en `velo_wa` para revisar/gapear vertical | Checklist en `evals/vertical_restaurantes.md` en verde  — |
| P-007 | Definir SLA de soporte prioritario para los 4 meses posteriores a activación (obligación 11) | pendiente | Nicolás | Redactar SLA y validar con la Cámara | SLA por escrito registrado en `DECISIONS.md` y referenciado en cada `clientes/<slug>/CLIENTE.md` (sección "SLA de soporte")  — |
| P-008 | Poblar cada `clientes/<slug>/CLIENTE.md` con datos reales (NIT, contactos, canales) | pendiente | Nicolás | Completar campos faltantes en cada carpeta (10 slugs ya creados) | 10 fichas de cliente sin secciones vacías críticas (NIT, contacto principal, ciudad)  — |
| P-009 | Corregir envío de medios de secuencias V2 en AriCRM: el mensaje se crea sin `media_mime_type`/`media_filename` → adapter manda fallbacks (`application/octet-stream`, `archivo`) → Evolution arma `imageMessage` con `mimetype:"false"` → WhatsApp entrega pero no renderiza la imagen | pendiente | MY SEO (código en `velo_wa`) | Entregar el spec al agente de velo_wa: `tasks/P-009-sequence-media-mimetype.md`; implementar, deployar y re-probar la secuencia `enviar_carta` del piloto Samu | Secuencia envía imagen renderizable: `imageMessage` con mimetype real (p. ej. `image/png`) en la DB de Evolution y el teléfono controlado la muestra; sin regresión en envíos de medios del composer (base64)  Diagnosis y evidencia del bug: `clientes/arepas-rellenas-samu/PROGRESS.md` (entradas del 2026-09-30); spec: `tasks/P-009-sequence-media-mimetype.md` |
| P-015 | Registrar dirección y horario por sede y habilitar herramientas seguras en el simulador del agente | pendiente | MY SEO (código en `velo_wa`) | Implementar en `velo_wa` según `tasks/sedes-contexto-agente-y-simulador.md`; comprobar T01 de Friends Chicken sin efectos reales | Sedes con dirección/horario verificados por línea; simulador consulta sede y menú con traza, simula herramientas de escritura sin efectos; T01 resuelto en prueba controlada  — |
| P-016 | Retirar `get_daily_menu` del agente de Calamar Azul (menú fijo) y publicar el prompt v9 con las definiciones confirmadas del establecimiento | pendiente | MY SEO (código en `velo_wa`) | Entregar el spec al agente de velo_wa: `tasks/P-016-retiro-daily-menu-y-prompt-v9-calamar-azul.md`; implementar el gate de `appendDailyMenuToolContext`, ajustar `enabled_tools`/`daily_menu_tool_enabled` y publicar la v9 | `enabled_tools` sin `get_daily_menu` ni `is_holiday` y `daily_menu_tool_enabled=false`; bloque «Menú del día» ausente en la ruta productiva del tenant y presente para tenants que sí usan la tool; suite MA 32/32 con expectativas del addendum, cero `ok=false` y sin llamadas a `get_daily_menu`; v9 versionada con hash y metadatos de versión correctos  — Evidencia: `evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md` (addendum y ronda post-deploy); spec: `tasks/P-016-retiro-daily-menu-y-prompt-v9-calamar-azul.md` |

## Evidencia de cierre

Para marcar `completa`, registrar en la columna Evidencia rutas concretas entre backticks, relativas a la raíz del repositorio, dentro de `evidencias/` o `entregables/`. Cada archivo debe existir y tener contenido. No usar placeholders ni el criterio de terminado como evidencia. Revisar manualmente que los archivos demuestren todos los criterios del workflow; el validador comprueba estructura y existencia, no suficiencia del contenido.
