# TASKS — Trattorias y Pastificios S.A.S.

Tareas específicas de este cliente. Las tareas globales del programa viven en `../../TASKS.md`.

## Convención

Estados: `pendiente`, `en_progreso`, `en_revision`, `bloqueada`, `completa`.

**Regla de sincronización**: este archivo es la fuente canónica de estado por obligación para este cliente. `CLIENTE.md`, `PROGRESS.md` y el dashboard consumen de aquí. No duplicar estado en `CLIENTE.md`.

**Regla de aceptación**: los criterios de esta tabla replican textualmente los criterios de aceptación del workflow correspondiente. Si un workflow cambia, actualizar aquí también. No cerrar una tarea sin cumplir el criterio del workflow (no solo el resumen).

| ID | Obligación | Workflow | Resultado esperado | Estado | Responsable | Vence | Siguiente acción | Criterio de terminado (tomado del workflow) |
|----|-----------|----------|--------------------|--------|-------------|-------|------------------|---------------------------------------------|
| C-01 | 2 | `01_caracterizacion` | Caracterización completa | pendiente | — | — | Agendar sesión con el cliente | `CARACTERIZACION.md` sin secciones vacías (o con "pendiente por confirmar" fechado); ≥3 brechas digitales priorizadas; evidencia archivada en `evidencias/<slug>/caracterizacion-<YYYY-MM-DD>.md` |
| C-02 | 3, 6 | `02_config_tenant` | Tenant AriCRM operativo (3 usuarios, 3 líneas WA, capacidad 2000 contactos) + canales integrados | pendiente | — | — | Enviar invitaciones AriCRM al cliente y coordinar sesión de conexión de líneas WA con un operador del establecimiento (NO recibir contraseñas) | Tenant activo con 3 usuarios logueables por invitación (nunca por contraseña compartida); 3 líneas WhatsApp en estado conectado verificado por captura; límite de 2000 contactos verificado en configuración; al menos un canal adicional integrado si el cliente lo tiene; capturas en `evidencias/<slug>/config-tenant/` |
| C-03 | 4 | `03_vertical_restaurantes` | Vertical restaurantes activo: menú digital, pedidos, reservas, plantillas, etiquetas | pendiente | — | — | Solicitar menú y reglas de operación al cliente | Menú completo cargado y visible desde flujo conversacional; al menos un pedido y una reserva de prueba completados end-to-end; plantillas y etiquetas activas; evidencia en `evidencias/<slug>/vertical-restaurantes/` |
| C-04 | 5 | `04_ia_conversacional` | Agente IA operando con escalamiento a humano | pendiente | — | — | Definir criterios de escalamiento con el cliente | 5 conversaciones de prueba con clasificación correcta (resolvió/escaló); escalamiento llega al humano designado con contexto suficiente; prompt versionado en `evidencias/<slug>/ia-conversacional/prompt-v1.md` |
| C-05 | 7 | `05_capacitacion` | Personal capacitado con práctica ejecutada | pendiente | — | — | Agendar capacitación | Acta firmada por asistentes y responsable MY SEO en `../../entregables/actas/`; al menos 1 usuario del cliente ejecutó la tarea de práctica (evidencia); contacto para dudas de la primera semana identificado |
| C-06 | 8 | `06_activacion` | Activación acompañada con confirmación de autonomía | pendiente | — | — | Coordinar día D con el cliente | Fecha de activación registrada en `CLIENTE.md`; reporte de primera semana con métricas base en `evidencias/<slug>/activacion/semana-1.md`; **confirmación escrita del cliente** (correo/WhatsApp/acta) de que puede operar autónomamente |
| C-07 | 10 | `07_soporte_sla` | Licenciamiento activo por 4 meses desde activación | pendiente | — | — | Configurar suscripción/renovación en AriCRM al activar | Registro de licenciamiento con fecha inicio y fecha fin (activación + 4 meses) en `CLIENTE.md`; verificación de acceso vigente en día -30, día -7 y día 0 del vencimiento |
| C-08 | 11 | `07_soporte_sla` | Soporte SLA operativo durante los 4 meses | pendiente | — | — | Abrir log de tickets al activar; publicar canales de soporte al cliente | Log de tickets vivo en `evidencias/<slug>/soporte/tickets.md`; % de cumplimiento SLA reportado mensualmente; incidentes fuera de SLA con causa registrada |
| C-09 | 15 | `08_informes` | Informe individual entregado a la Cámara con acuse | pendiente | — | — | Consolidar evidencias en `INFORME.md` | Informe firmado en `../../entregables/informes/informe-<slug>-<YYYY-MM-DD>.pdf`; **acuse de recibo de la Cámara** archivado (correo, radicado o firma en acta) |
| C-10 | — | `07_soporte_sla` | Cierre del período de 4 meses | pendiente | — | activación + 4m | Consolidar métricas del período y comunicar al cliente el fin del soporte incluido | Reporte de cierre en `evidencias/<slug>/soporte/cierre-<YYYY-MM-DD>.md`; comunicación de cierre al cliente con acuse; entrada final en `PROGRESS.md` |
