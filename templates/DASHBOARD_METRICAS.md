# DASHBOARD DE SEGUIMIENTO — Programa Vouchers Digitales 2026

**Obligación contractual**: Cláusula Quinta, numeral 13.
**Actualización**: continua durante ejecución + snapshot quincenal para la Cámara.

_Este documento describe el CONTENIDO del dashboard. La implementación técnica (BI, panel embebido en AriCRM, hoja compartida) se decide y se registra en `../DECISIONS.md`._

## Estructura propuesta

### Vista 1 — Estado del programa

- Semana actual (1..6) y % avance.
- Establecimientos activados: N/10.
- Establecimientos con capacitación completa: N/10.
- Establecimientos con caracterización completa: N/10.
- Riesgos abiertos.

### Vista 2 — Cumplimiento por obligación

Matriz de 10 clientes × obligaciones (2, 3, 4, 5, 6, 7, 8). Semáforo por celda.

### Vista 3 — Métricas operativas agregadas

Rango últimos 7 / 30 días, filtrable por establecimiento:

- Conversaciones totales.
- Conversaciones únicas.
- Tiempo de primera respuesta promedio (Dt1) y mediana.
- Pedidos generados.
- Reservas gestionadas.
- Tasa de escalamiento IA → humano.
- Usuarios activos por establecimiento.

### Vista 4 — Detalle por establecimiento

Al hacer clic en un establecimiento: sus métricas propias, evidencias enlazadas, próximos hitos, tickets abiertos de soporte.

### Vista 5 — Soporte (visible durante los 4 meses posteriores a activación)

- Tickets abiertos por severidad.
- Cumplimiento SLA % por severidad.
- Incidentes fuera de SLA con causa.

## Fuentes de datos

- Métricas operativas: base de datos de AriCRM (tenant por establecimiento, consultas agregadas).
- Estado de obligaciones: `clientes/<c>/TASKS.md` (traducido a semáforo).
- Tickets de soporte: log en `evidencias/<c>/soporte/`.

## Reglas de datos

- Nunca exponer PII de contactos en el dashboard (solo agregados).
- Cifras trazables a la fuente en AriCRM.
- Snapshot para la Cámara: PDF exportado con fecha, guardado en `entregables/dashboard/snapshot-<YYYY-MM-DD>.pdf`.
