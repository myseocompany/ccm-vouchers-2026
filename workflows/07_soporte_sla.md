# Workflow 07 — Soporte técnico prioritario (4 meses)

**Obligación contractual**: Cláusula Segunda (Parágrafo Primero) + Cláusula Quinta, numerales 10 y 11.
**Objetivo**: garantizar licenciamiento y soporte técnico prioritario durante 4 meses contados desde la activación de cada establecimiento.

## Niveles de severidad y SLA propuestos

_(A validar con la Cámara en P-007 — `../TASKS.md` (global))_

| Severidad | Descripción | Tiempo de respuesta | Tiempo de resolución objetivo |
|-----------|-------------|--------------------|-------------------------------|
| S1 — Crítica | Servicio caído, líneas desconectadas, no llegan mensajes | 1 hora hábil | 4 horas hábiles |
| S2 — Alta | Función principal falla (pedidos, reservas, IA) | 4 horas hábiles | 1 día hábil |
| S3 — Media | Función secundaria falla o pregunta bloqueante | 1 día hábil | 3 días hábiles |
| S4 — Baja | Consulta, mejora, "cómo hago" | 2 días hábiles | Best effort |

## Canales de soporte

- Canal primario: (definir — recomendado ticket via herramienta interna).
- Canal urgente: (definir — recomendado WhatsApp dedicado con horario y ANS).
- Escalamiento: correo formal a responsable MY SEO.

## Pasos operativos

1. Registrar cada solicitud en un log por cliente (`../evidencias/<slug>/soporte/tickets.md` o herramienta equivalente): ID, fecha entrada, severidad, descripción, fecha respuesta, fecha resolución, notas.
2. Confirmar recepción dentro del SLA.
3. Diagnóstico y resolución. Si requiere cambio de código en AriCRM, abrir tarea en `../velo_wa/` (no es cambio para el contrato — es soporte del producto).
4. Cerrar con confirmación del cliente.
5. Consolidar mensualmente para el informe final (obligación 16).

## Criterio de aceptación (a cierre de los 4 meses)

- Log de tickets completo por cliente.
- Cumplimiento reportado del SLA (% en cumplimiento, incidentes fuera de SLA con causa).
- Cliente confirma que recibió soporte adecuado (correo o encuesta).
