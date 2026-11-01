# SOURCES

Jerarquía de fuentes. Cuando dos fuentes se contradigan, prevalece la de mayor jerarquía.

## Jerarquía

1. **Contrato firmado** — `CT-239-26-3 - MY SEO - VOUCHERS DIGITALES.docx.pdf` (raíz). Es la fuente única de verdad sobre obligaciones, plazos, valores y responsabilidades.
2. **Otrosíes formales al contrato** — cuando existan, archivar junto al contrato con sufijo `-otrosi-NN.pdf`. Prevalecen sobre la versión anterior en los puntos modificados.
3. **Propuesta comercial** — hace parte integrante del contrato (Cláusula Tercera) en cuanto no lo contradiga. Archivar en la raíz cuando se tenga.
4. **Actas firmadas** — kickoff, capacitación, activación, cierre. Archivar en `entregables/actas/`.
5. **Comunicaciones formales** — correos con la Cámara o los establecimientos que afecten alcance, plazo, aceptación o incidentes. Archivar en `evidencias/comunicaciones/<YYYY-MM-DD>-<tema>.eml` o `.pdf`.
6. **Evidencias técnicas** — capturas, logs de AriCRM, exportes de dashboard. Archivar por cliente en `evidencias/<cliente-slug>/`.
7. **Documentación de AriCRM** — `../velo_wa/CLAUDE.md`, `../velo_wa/docs/`. Solo lectura desde este harness.
8. **Este harness** — `PROGRAMA.md`, `MEMORY.md`, `DECISIONS.md`, `TASKS.md`, workflows y templates.

## Reglas

- Nunca citar sin identificar la fuente y su ubicación.
- Para informar avance operativo por establecimiento, consultar `waterfall` en modo solo lectura justo antes del corte: cruzar los tenants de AriCRM con los 10 beneficiarios, comprobar por separado existencia del tenant, usuarios y estado **actual** de cada línea WhatsApp, y anotar fecha/hora de la consulta. El estado `connected` de una línea no equivale a tenant configurado ni a obligación C-02 completa; una línea creada, pendiente de QR o conectada históricamente tampoco cuenta como conectada ahora.
- **Excepción autorizada — 2026-10-05, Beto's Pizza:** por instrucción explícita de Nicolás, se permite descargar en modo solo lectura las conversaciones del tenant de Beto's Pizza exclusivamente para caracterización, parametrización, pruebas y mejora del agente dentro de este contrato. El export se guarda únicamente en `evidencias/pizzas-beto/conversaciones/raw/`, excluido de Git; no se copia a otros clientes, no se publica, no se incorpora en prompts como ejemplos identificables y no se exponen teléfonos, contactos, datos financieros ni el contenido íntegro en informes. Registrar fecha/hora, tenant consultado, rango y número de conversaciones en una nota de metadatos sin datos personales. La excepción no autoriza leer credenciales ni exportar otros tenants.
- Para caracterización, contrastar la hoja de trabajo `AriCRM_CCMPC.xlsx` proporcionada por Nicolás con `clientes/<slug>/CARACTERIZACION.md` y la evidencia exigida por `workflows/01_caracterizacion.md`. Si el archivo externo no es accesible, marcar el dato como reportado pero no verificado; no convertir automáticamente una fila del Excel en C-01 completa.
- Los reportes de avance deben usar una tabla pivote con **una fila por cada establecimiento del cupo (nueve confirmados; ver `DECISIONS.md` 2026-10-30)** y columnas separadas para caracterización, tenant, WhatsApp, vertical restaurantes, agente IA, capacitación y activación. Distinguir en cada celda lo verificado, lo reportado y lo pendiente de verificar; no sumar estados de fuentes heterogéneas como si fueran cierres contractuales.
- Antes de afirmar un dato del contrato, verificarlo abriendo el PDF (no confiar solo en resúmenes previos).
- Las decisiones de la Cámara deben quedar en correo o acta antes de ejecutarse.
- Las decisiones internas del contratista quedan en `DECISIONS.md` con fecha, contexto, alternativas consideradas y responsable.
