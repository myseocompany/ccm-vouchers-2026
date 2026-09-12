# PROGRAMA — Vouchers Digitales 2026

Contexto contractual del programa. Fuente autoritativa: `CT-239-26-3 - MY SEO - VOUCHERS DIGITALES.docx.pdf` en la raíz.

## Partes

- **La Cámara**: Cámara de Comercio de Manizales por Caldas (NIT 890.801.042-6). Delegado: César Augusto Cárdenas Molina.
- **El Contratista**: MY SEO COMPANY S.A.S. (NIT 900.489.574-1). Representante legal: Nicolás Navarro Rincón.
- **Responsable de seguimiento (Cámara)**: Nestor H. Cortés Jiménez (Área de Transformación Digital Empresarial).
- **Elaboró**: David Valencia Rendón.

## Objeto

Implementación, configuración, parametrización, puesta en funcionamiento y apropiación de **AriCRM – Plan Crecer** en 10 establecimientos gastronómicos beneficiarios del programa Vouchers Digitales 2026, incluyendo caracterización, IA de atención, capacitación, acompañamiento y soporte.

## Alcance por cliente (Parágrafo Primero – Cláusula Primera)

- Hasta 3 usuarios.
- 3 líneas de WhatsApp.
- 2000 contactos.
- Plantilla vertical restaurantes: menú digital, pedidos, reservas, etiquetas, plantillas de respuesta, flujos automáticos, canal WhatsApp.
- IA para atención automatizada + escalamiento a personal humano.

## Plazos (Cláusula Segunda)

- **Implementación**: 6 semanas calendario contadas desde la firma del contrato.
- **Soporte técnico prioritario + licenciamiento**: 4 meses desde la activación en cada establecimiento beneficiario.
- **Fechas concretas**: registrar en `DECISIONS.md` cuando se confirme fecha de firma y de activación por cliente.

## Valor y pago (Cláusula Cuarta)

- Valor total: **$5.236.000 COP** IVA incluido.
- Forma de pago: **100% al finalizar** las 6 semanas de implementación, previa presentación de entregables y certificación de cumplimiento.
- Fuente presupuestal: PUB – Escuela de Transformación Digital (0012-1207-6).

## Obligaciones del contratista (Cláusula Quinta) — resumen mapeado a workflows

| Nº | Obligación | Workflow |
|----|-----------|----------|
| 2 | Caracterización inicial de cada uno de los 10 | `workflows/01_caracterizacion.md` |
| 3 | Configurar y poner en funcionamiento AriCRM Plan Crecer (3 usuarios / 3 líneas WA / 2000 contactos) | `workflows/02_config_tenant.md` |
| 4 | Implementar plantilla vertical restaurantes | `workflows/03_vertical_restaurantes.md` |
| 5 | Configurar e integrar agente IA con escalamiento a humano | `workflows/04_ia_conversacional.md` |
| 6 | Integrar canales digitales existentes de cada beneficiario | `workflows/02_config_tenant.md` |
| 7 | Capacitar al personal responsable de cada establecimiento | `workflows/05_capacitacion.md` |
| 8 | Acompañamiento durante activación y adopción | `workflows/06_activacion.md` |
| 9 | Completar implementación dentro de las 6 semanas | Gestión global (`TASKS.md`) |
| 10 | Garantizar licenciamiento por 4 meses tras activación | `workflows/07_soporte_sla.md` |
| 11 | Soporte técnico prioritario 4 meses con SLA | `workflows/07_soporte_sla.md` |
| 12 | Entregar informes de avance para consolidar los 10 | `workflows/08_informes.md` |
| 13 | Dashboard de seguimiento del piloto | `templates/DASHBOARD_METRICAS.md` |
| 14 | Reporte final de resultados e indicadores | `workflows/08_informes.md` |
| 15 | Informe individual por cada empresa beneficiaria | `workflows/08_informes.md` + `clientes/<c>/INFORME.md` |
| 16 | Informe final con evidencias técnicas | `templates/INFORME_FINAL.md` |
| 20 | Garantizar titularidad/licencia del software usado | Ver `POLICIES.md` — propiedad intelectual |
| 22-25 | Confidencialidad y protección de datos (Ley 1581/2012, 1266/2008) | Ver `POLICIES.md` — datos |

## Entregables contractuales (Parágrafo Primero – Cláusula Quinta)

- **a.** Un informe por cada uno de los 10 establecimientos, formato Cámara. Ver `templates/INFORME_ESTABLECIMIENTO.md`.
- **b.** Un informe final con evidencias técnicas (configuración, parametrización, implementación, capacitación, puesta en funcionamiento). Ver `templates/INFORME_FINAL.md`.
- **Adicional**: dashboard de seguimiento y datos consolidados del piloto.

Los entregables firmados/enviados se archivan en `entregables/`. Las evidencias técnicas por cliente en `evidencias/`.

## Riesgos y restricciones críticas

- **Propiedad intelectual (Cláusula Décima Séptima + Parágrafo Segundo)**: los derechos patrimoniales de "obras creadas en ejercicio de las funciones contratadas" se ceden a la Cámara, pero la propiedad intelectual preexistente se conserva. **AriCRM es preexistente** y debe tratarse siempre así. Ver `POLICIES.md`.
- **Cláusula penal (Cláusula Décima Tercera)**: 20% del valor total en caso de incumplimiento. **$1.047.200 COP** de exposición máxima.
- **Causal 6 de terminación**: incumplimiento de la Política de Protección de Datos de la Cámara puede terminar el contrato.
- **Pago 100% al final**: sin pagos parciales, todos los entregables deben estar cerrados antes de facturar.

## Estado del programa

| Hito | Estado | Fecha | Evidencia |
|------|--------|-------|-----------|
| Firma del contrato | Registrado en PDF (Zoho Sign) | Por confirmar | `CT-239-26-3 - MY SEO - VOUCHERS DIGITALES.docx.pdf` |
| Kickoff con la Cámara | Pendiente | — | — |
| Confirmación de los 10 clientes beneficiarios | Pendiente | — | — |
| Caracterización completa (10/10) | Pendiente | — | — |
| Configuración AriCRM (10/10) | Pendiente | — | — |
| Capacitación (10/10) | Pendiente | — | — |
| Activación (10/10) | Pendiente | — | — |
| Entrega informes individuales (10/10) | Pendiente | — | — |
| Entrega informe final | Pendiente | — | — |
| Factura emitida y pagada | Pendiente | — | — |
