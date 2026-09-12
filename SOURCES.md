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
- Antes de afirmar un dato del contrato, verificarlo abriendo el PDF (no confiar solo en resúmenes previos).
- Las decisiones de la Cámara deben quedar en correo o acta antes de ejecutarse.
- Las decisiones internas del contratista quedan en `DECISIONS.md` con fecha, contexto, alternativas consideradas y responsable.
