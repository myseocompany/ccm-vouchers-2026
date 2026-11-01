# Workflow 08 — Informes y entregables

**Obligación contractual**: Cláusula Quinta, numerales 12, 13, 14, 15, 16 + Parágrafo Primero – Entregables.
**Objetivo**: producir y entregar los informes exigidos por el contrato en el formato aceptado por la Cámara.

## Entregables

| Entregable | Origen | Cadencia | Ubicación borrador | Ubicación final |
|-----------|--------|----------|--------------------|-----------------|
| Informes de avance del programa (obl. 12) | Consolidación de los 10 clientes | Según cadencia acordada con la Cámara | `../entregables/avances/` (WIP) | `../entregables/avances/` (firmado) |
| Dashboard de seguimiento (obl. 13) | Datos consolidados AriCRM | Continuo, actualización periódica | `../templates/DASHBOARD_METRICAS.md` | Enlace vivo + snapshot en `../entregables/dashboard/` |
| Reporte final de resultados (obl. 14) | Consolidación al cierre de 6 semanas | Una vez | `../templates/INFORME_FINAL.md` | `../entregables/informe-final/` |
| Informe individual por establecimiento (obl. 15) | Por cliente | Una vez, al cierre de activación | `../clientes/<slug>/INFORME.md` | `../entregables/informes/informe-<cliente-slug>-<YYYY-MM-DD>.pdf` |
| Informe final con evidencias técnicas (obl. 16) | Consolidación técnica | Una vez, al cierre | `../templates/INFORME_FINAL.md` | `../entregables/informe-final/` |

## Informe de avance (parcial) con formato oficial de la Cámara

**Formato oficial** (confirmado por Nicolás, 2026-10-29): `../templates/INFORME_CAMARA_OFICIAL.docx`. Es la copia canónica única: nunca editarla ni generar copias alternativas. Copiarla a un directorio de trabajo y editar la copia (skill docx) conservando encabezado, logo, estilos y estructura. El título «VAUCHERS» viene así en el formato oficial; no corregirlo. Los parciales por cliente alimentan el informe de avance consolidado (obl. 12).

1. Identificación: marcar [X] Parcial No. 1. Periodo: desde la fecha de caracterización/activación del cliente (`../clientes/<slug>/CLIENTE.md`, `PROGRESS.md`) hasta hoy. Contrato CT-239-26-3. Empresa, NIT y contacto desde `CLIENTE.md`.
2. Proveedor: MY SEO COMPANY S.A.S., NIT 900.489.574-1, líder Nicolás Navarro Rincón (`../PROGRAMA.md`). Teléfono y correo solo si constan en el repo; si no, dejar `[PENDIENTE]`.
3. Actividades: borrar las filas de ejemplo; una fila por obligación (2 caracterización, 3 tenant, 4 vertical restaurantes, 5 IA + escalamiento, 6 integración de canales, 7 capacitación, 8 acompañamiento) con entregable, estado (Finalizado / En proceso / Pendiente) y % de avance acumulado, tomados de `../clientes/<slug>/TASKS.md` y `PROGRESS.md`.
4. Evidencias: imágenes pegadas dentro del documento (no como anexos) desde `../evidencias/<slug>/`, cada una con descripción breve. Si una actividad no tiene evidencia visual, no inventarla: registrarla en la lista de faltantes. Las tomas exigidas por obligación, su nomenclatura y las reglas de privacidad están en `../evidencias/PLAN_CAPTURAS_2026-10-30.md`. **No usar como evidencia de implementación los insumos entregados por el cliente** (cartas, fotos de producto, tarifas, QR de pago) ni los registros de incidencias: la evidencia visual es la captura de AriCRM funcionando.
5. Observaciones: dificultades, retrasos y próximos pasos desde `PROGRESS.md` y `TASKS.md`.
6. Firmas: campos en blanco para firmar.

Reglas: cada cifra, fecha y estado debe salir de una fuente del repo; separar hechos de inferencias; lo que falte se marca `[PENDIENTE: <qué falta y de dónde>]`. No mezclar datos entre clientes ni leer/copiar credenciales. Comprimir imágenes si el .docx supera ~10 MB. Salida: `../entregables/informes/informe-<slug>-parcial-1-<YYYY-MM-DD>.docx` (crear la carpeta si no existe) + línea en `../clientes/<slug>/PROGRESS.md` remitiendo al borrador. Es un borrador para revisión de Nicolás: no enviar a la Cámara ni al cliente; no commit sin autorización expresa.

## Pasos por informe individual

1. Confirmar formato oficial de la Cámara (P-004 en `../TASKS.md` (global)). Si no lo dan, usar `../templates/INFORME_ESTABLECIMIENTO.md`.
2. Poblar `../clientes/<slug>/INFORME.md` desde: `../clientes/<slug>/CARACTERIZACION.md`, `../clientes/<slug>/PROGRESS.md`, evidencias en `../evidencias/<slug>/`, métricas del dashboard.
3. Revisión interna. Verificar que cada cifra tiene fuente (ver `../POLICIES.md`).
4. Exportar a PDF. Firmar por responsable MY SEO. Solicitar validación del establecimiento cuando aplique.
5. Enviar a la Cámara con acuse. Archivar copia firmada en `../entregables/informes/`.
6. Cerrar `C-09` en `../clientes/<slug>/TASKS.md` del cliente.

## Corte de avance del programa

1. Seguir `../SOURCES.md`: revisar `waterfall` en solo lectura en la fecha del corte y cruzar los tenants con los 10 clientes. Consultar únicamente nombres comerciales, conteos y estados; nunca teléfonos, contactos, conversaciones o secretos.
2. Contrastar la caracterización con la hoja de trabajo indicada por Nicolás y con los soportes por cliente. Si una fuente es inaccesible, indicar «reportado, no verificado».
3. Presentar un resumen pivote: una fila por restaurante; columnas para caracterización, tenant, WhatsApp, vertical, IA, capacitación y activación. Separar «tenant creado», «línea registrada», «línea conectada», «agente en borrador» y «activación aceptada».
4. Fecha, fuente y criterio de cada cifra deben quedar explícitos. Mantener `../TASKS.md`, `../clientes/<slug>/TASKS.md` y `../clientes/<slug>/PROGRESS.md` alineados solo con evidencia suficiente; no cerrar obligaciones por conteos agregados.

## Pasos para el informe final

1. Consolidar los 10 informes individuales.
2. Agregar sección de indicadores del piloto (totales, promedios, tasas).
3. Adjuntar evidencias técnicas: configuración, parametrización, integración, capacitación, puesta en funcionamiento.
4. Revisión legal y de forma. Verificar que nada compromete la propiedad intelectual del producto AriCRM (`../POLICIES.md`).
5. Firmar y enviar.
6. Habilita la facturación (Cláusula Cuarta: pago 100% al final).

## Criterio de aceptación

- Cada entregable con acuse de recibo de la Cámara.
- Certificado de cumplimiento emitido por el responsable de seguimiento de la Cámara antes de facturar.
