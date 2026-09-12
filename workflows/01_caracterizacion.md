# Workflow 01 — Caracterización del establecimiento

**Obligación contractual**: Cláusula Quinta, numeral 2.
**Objetivo**: identificar necesidades del establecimiento en atención al cliente, gestión de menú, pedidos y reservas, para dimensionar la configuración de AriCRM.

## Precondiciones

- **Este** cliente específico confirmado como beneficiario por la Cámara (correo/acta de la Cámara identificándolo por nombre y NIT — no depende de que los 10 estén confirmados).
- Contacto principal identificado en `clientes/<slug>/CLIENTE.md`.
- Sesión agendada (presencial o remota).

## Pasos

1. Confirmar canal y horario de la sesión con el contacto principal. No suplantar, no grabar sin consentimiento explícito.
2. Revisar antes canales públicos del cliente (WhatsApp Business, IG, FB, web) para llegar con hipótesis, no en blanco.
3. Conducir la sesión guiada por `clientes/<c>/CARACTERIZACION.md`. Completar todas las secciones. Marcar lo que no se pueda responder en la primera sesión.
4. Confirmar priorización de módulos (menú digital / pedidos / reservas / IA) con el cliente.
5. Guardar notas de la sesión en `evidencias/<c>/caracterizacion-<YYYY-MM-DD>.md`.
6. Actualizar `clientes/<c>/PROGRESS.md` y marcar `C-01` como `completa` en `clientes/<c>/TASKS.md` cuando `CARACTERIZACION.md` esté lleno.

## Criterio de aceptación

- `CARACTERIZACION.md` sin secciones vacías (o con nota explícita de "pendiente por confirmar" con fecha).
- Al menos 3 brechas digitales priorizadas.
- Evidencia archivada.

## Bloqueos frecuentes

- Cliente no responde o no agenda: escalar a la Cámara (obligación 17 — informar oportunamente).
- Información contradictoria sobre operación: dejar constancia y priorizar la fuente escrita.
