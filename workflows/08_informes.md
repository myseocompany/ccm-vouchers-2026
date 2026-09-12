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

## Pasos por informe individual

1. Confirmar formato oficial de la Cámara (P-004 en `../TASKS.md` (global)). Si no lo dan, usar `../templates/INFORME_ESTABLECIMIENTO.md`.
2. Poblar `../clientes/<slug>/INFORME.md` desde: `../clientes/<slug>/CARACTERIZACION.md`, `../clientes/<slug>/PROGRESS.md`, evidencias en `../evidencias/<slug>/`, métricas del dashboard.
3. Revisión interna. Verificar que cada cifra tiene fuente (ver `../POLICIES.md`).
4. Exportar a PDF. Firmar por responsable MY SEO. Solicitar validación del establecimiento cuando aplique.
5. Enviar a la Cámara con acuse. Archivar copia firmada en `../entregables/informes/`.
6. Cerrar `C-09` en `../clientes/<slug>/TASKS.md` del cliente.

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
