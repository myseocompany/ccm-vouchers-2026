# Plan de capturas para el informe de avance parcial No. 1

**Fecha**: 2026-10-30. **Origen**: el formato oficial de la Cámara (`templates/INFORME_CAMARA_OFICIAL.docx`) exige evidencias visuales pegadas dentro del documento (`workflows/08_informes.md`, paso 4).

## Por qué este plan

Auditoría del 2026-10-30 sobre `evidencias/`: las imágenes archivadas son **insumos entregados por el cliente** (cartas, fotos de producto, tarifas de domicilio, QR de pago) o registros de incidencias, no capturas de AriCRM mostrando la implementación en funcionamiento. Única excepción parcial: `friends-chicken-cable/vertical-restaurantes/menu/aricrm-menu-parcial-2026-09-28.png`. Las carpetas `config-tenant/` existentes (trattorias, mar-azul) contienen solo `.md`.

Consecuencia: **ninguna obligación tiene hoy evidencia visual que acredite avance**. Las capturas de este plan hay que tomarlas nuevas antes de generar los informes. No reutilizar los insumos del cliente como evidencia de implementación.

## Reglas de captura

- Ruta y nombre: `evidencias/<slug>/<carpeta>/<asunto>-<YYYY-MM-DD>.png`. Un archivo por afirmación del informe.
- Tomar la captura con la interfaz de AriCRM visible e identificable (nombre del tenant o sede en pantalla).
- **Antes de archivar, tapar** teléfonos, correos, nombres y mensajes de clientes finales. `POLICIES.md`: no se exponen datos personales ni contactos.
- Nunca capturar pantallas con tokens, contraseñas, claves de API ni paneles de credenciales.
- No mezclar capturas entre clientes: cada archivo va en la carpeta de su `<slug>`.
- Si una toma no se puede obtener, no inventarla: registrarla como faltante en el informe (`[PENDIENTE: <qué falta>]`).

## Catálogo de tomas requeridas

### Obligación 3 — Tenant operativo → `evidencias/<slug>/config-tenant/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 1 | `usuarios-<fecha>.png` | Los 3 usuarios del tenant en estado activo o invitado (nunca contraseñas) |
| 2 | `lineas-whatsapp-<fecha>.png` | Las líneas de WhatsApp en estado **conectado** |
| 3 | `limite-contactos-<fecha>.png` | Configuración del plan con la capacidad de 2000 contactos |
| 4 | `sedes-<fecha>.png` | Sede(s) creadas y activas, donde aplique |

### Obligación 6 — Canales integrados → `evidencias/<slug>/config-tenant/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 5 | `canales-integrados-<fecha>.png` | Instagram / Facebook / sitio web conectados. Solo si el cliente tiene el canal; si no tiene, se declara en el informe |

### Obligación 4 — Vertical restaurantes → `evidencias/<slug>/vertical-restaurantes/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 6 | `aricrm-menu-cargado-<fecha>.png` | Catálogo cargado en AriCRM: productos con precios |
| 7 | `menu-en-conversacion-<fecha>.png` | La carta entregada dentro del flujo conversacional de WhatsApp |
| 8 | `pedido-prueba-<fecha>.png` | Un pedido de prueba completado end-to-end: conversación + registro del pedido |
| 9 | `reserva-prueba-<fecha>.png` | Una reserva de prueba completada |
| 10 | `plantillas-<fecha>.png` | Plantillas activas |
| 11 | `etiquetas-<fecha>.png` | Etiquetas activas |

### Obligación 5 — IA conversacional → `evidencias/<slug>/ia-conversacional/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 12 | `prueba-0N-<caso>-<fecha>.png` (×5) | Las 5 conversaciones de prueba con su desenlace: resolvió o escaló |
| 13 | `escalamiento-<fecha>.png` | El escalamiento llegando al humano designado, con contexto suficiente |

### Obligación 7 — Capacitación → `evidencias/<slug>/capacitacion/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 14 | `sesion-<fecha>.png` | Registro de la sesión. El acta firmada va aparte en `entregables/actas/` |
| 15 | `practica-usuario-<fecha>.png` | Un usuario del cliente ejecutando la tarea de práctica |

### Obligación 8 — Activación → `evidencias/<slug>/activacion/`

| Toma | Archivo | Qué debe mostrar |
|---|---|---|
| 16 | `metricas-semana-1-<fecha>.png` | Métricas base de la primera semana |
| 17 | `confirmacion-autonomia-<fecha>.png` | Confirmación escrita del cliente de que puede operar autónomamente |

## Prioridad por cliente

Los nueve beneficiarios confirmados (`DECISIONS.md`, 2026-10-30). Prioridad según el estado en `clientes/<slug>/TASKS.md`:

| Cliente | Estado C-01…C-06 | Tomas prioritarias para el parcial No. 1 |
|---|---|---|
| el-efecto-barbacoa | C-01 y C-04 en progreso | 1-4, 6-7, 12-13 |
| trattorias-y-pastificios | C-01 revisión; C-02, C-03, C-04 en progreso | 1-4, 6-11, 12-13 |
| mar-azul | C-01 revisión; C-03, C-04 en progreso | 1-4, 6-11, 12-13 |
| indecente | C-01…C-04 en progreso | 1-4, 6-7, 12-13 |
| pizzas-beto | C-01 revisión; C-04 en progreso | 1-4, 6-7, 10-11, 12-13 |
| friends-chicken-cable | C-03 en progreso | 1-4, 6-11 (la captura de menú existente es parcial: repetirla) |
| sushi-fusion | C-04 en progreso | 1-4, 12-13 |
| the-boss | expediente creado 2026-10-31; C-01–C-04 en progreso | 1-4, 6-7, 12-13 |
| la-patateria | C-01 en progreso | 1-4, 6-7 |

Ninguno tiene hoy evidencia para las tomas 14-17: las obligaciones 7 y 8 están pendientes en los nueve.

## Siguiente paso

Sesión de capturas en AriCRM por tenant, en el orden de la tabla de prioridad. Cada captura archivada se referencia desde `clientes/<slug>/PROGRESS.md` con fecha y obligación que acredita.
