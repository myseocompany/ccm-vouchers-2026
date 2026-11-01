# PROGRESS — The Boss Burger

Bitácora cronológica de lo que se hizo, con evidencia. No borrar entradas: rectificar con nueva entrada si algo cambia.

## Formato

```
### YYYY-MM-DD — Título corto
- **Qué se hizo**:
- **Obligación asociada**:
- **Responsable**:
- **Evidencia**: ubicación (ruta al archivo, ID de acta, log ID, correo).
- **Notas**:
```

## Entradas

### 2026-10-11 — Recepción de la caracterización y confirmaciones operativas

> Entrada retrospectiva registrada el 2026-10-31: el trabajo precede a la creación de este expediente.

- **Qué se hizo**: se recibió el formulario de caracterización diligenciado por el propietario (Diego López Benjumea), pegado por Nicolás y normalizado sin editar contenido. El mismo día Nicolás aportó confirmaciones adicionales: preparación ~10 min, recogida en sitio sí (Cra. 19 #74A-12), reservas no, redes sociales y WhatsApp del propietario.
- **Obligación asociada**: Obligación 2 (caracterización).
- **Responsable**: establecimiento (formulario) + Nicolás Navarro Rincón — MY SEO (normalización y confirmaciones).
- **Evidencia**: `../../evidencias/the-boss/caracterizacion-2026-10-11.md`.
- **Notas**: caracterización **preliminar** — bloques 2–9 con múltiples campos «sin respuesta» y sin firmas del bloque 9. Pendiente de validación con el establecimiento.

### 2026-10-11 — Implementación temprana en el tenant (carta, tarifas, horario, prompt)

> Entrada retrospectiva registrada el 2026-10-31: el trabajo precede a la creación de este expediente.

- **Qué se hizo**: (1) se transcribió la carta impresa y se verificó producto por producto contra las capturas ampliadas (6 categorías, 23 productos) y se cargó en producción; (2) se creó la sede Principal y se cargaron 180 tarifas Flash Delivery (verificadas por lectura: 180 activas, suma COP 1.538.000, coincide con el JSON); (3) se cargó el horario del tenant (lunes cerrado; mar–jue 18:00–22:00; vie–dom 17:00–22:00) verificado por lectura; (4) se iteró y publicó el prompt del agente de domicilios hasta v2.7 (`v2.7-boss-2026-10-11`), corrigiendo fallos vistos en conversaciones de prueba (combo sin pedido explícito, ids inventados, barrio asumido por defecto, totales sin `quote_order`).
- **Obligación asociada**: insumos de Obligaciones 3, 4 y 5 (tenant, vertical restaurantes, IA conversacional).
- **Responsable**: MY SEO (sesión de configuración productiva del 2026-10-11).
- **Evidencia**: carta `../../evidencias/the-boss/vertical-restaurantes/menu/carta-the-boss-2026-10-11.md`; tarifas `../../evidencias/the-boss/vertical-restaurantes/tarifas-cargadas-sede-principal-2026-10-11.md`; horario `../../evidencias/the-boss/operacion-horario-tenant-2026-10-11.md`; prompt `../../evidencias/the-boss/ia-conversacional/prompt-v2.md`.
- **Notas**: sin capturas de pantalla archivadas — ver `../../evidencias/PLAN_CAPTURAS_2026-10-30.md` (tomas 1-4, 6-7, 12-13 pendientes para the-boss). Zonas «en rojo» del PDF de tarifas sin modelar; festivos sin configurar. Pendientes del agente: casos/palabras sensibles que siempre escalan y teléfono de Paola Camacho (receptora de escalamientos).

### 2026-10-31 — Creación del expediente del cliente

- **Qué se hizo**: se creó `clientes/the-boss/` a partir de `clientes/_template/`; se poblaron `CLIENTE.md` y `CARACTERIZACION.md` exclusivamente desde las evidencias existentes del 2026-10-11; se registró el estado de tareas (C-01…C-04 `en_progreso` según evidencias; C-05…C-10 `pendiente`) y las entradas retrospectivas de esta bitácora.
- **Obligación asociada**: transversal — habilita el seguimiento por obligación para este beneficiario.
- **Responsable**: MY SEO (harness, sesión del 2026-10-31).
- **Evidencia**: esta carpeta (`clientes/the-boss/`); fuentes: `../../evidencias/the-boss/` (caracterización, carta, tarifas, horario, prompt).
- **Notas**: pendientes abiertos — validación de la caracterización con el establecimiento; correos/teléfono de Paola Camacho; número de la línea WhatsApp «Principal»; capturas 1-4, 6-7 y 12-13 del plan; soporte formal de la Cámara por la sustitución (roster 2026-10-30).

### 2026-10-31 — Hallazgos en velo_wa: bot en producción, ronda de pruebas y prompts v3.1/v3.2

- **Qué se hizo**: revisión de solo lectura de `../velo_wa/` que reveló trabajo del 31-oct no registrado en este expediente: (1) el agente «Asistente de domicilios» **opera en producción desde el 12-oct** — respondió en 29 de 135 conversaciones de los últimos 60 días y registró 2 pedidos el 30 y 31-oct; (2) guion de pruebas TB-01..TB-36 generado desde un dump de producción (135 conversaciones, 2.659 mensajes, 9-sep→31-oct) con citas anonimizadas; (3) ronda `/test_agent` de 3 corridas en sandbox: v2.7+gpt-4o-mini 10❌ («no apto»), v2.7+gpt-4.1-mini 6❌, v3.0/v3.1+gpt-4.1 1❌; causa raíz confirmada con sonda: `gpt-4o-mini` corrompe UUID del catálogo y cobra el combo como nota sin los $9.000; (4) publicación del prompt v3.1 (~12:56 UTC, modelo subido a `gpt-4.1`) y v3.2 (~14:00 UTC, con `inject_open_status=true` junto al feature `agent-open-status-context`); (5) prueba real por WhatsApp desde línea del operador que motivó v3.2 (con v3.1 cotizó $44.000 un sábado cerrado). Se archivaron copias verificadas por hash del guion y de los prompts.
- **Obligación asociada**: Obligación 5 (IA conversacional) — guion, corridas y versionado del prompt; insumo para la Obligación 4 (pedidos registrados por el bot).
- **Responsable**: MY SEO — operación del 31-oct registrada en velo_wa (commits `e78e7de7`…`8ba0bc32`); incorporación a este expediente por el harness.
- **Evidencia**: copias en `../../evidencias/the-boss/ia-conversacional/`: `../../evidencias/the-boss/ia-conversacional/MENSAJES_PRUEBA_2026-10-31.md` (SHA-256 verificado == original), `../../evidencias/the-boss/ia-conversacional/v2.7-baseline-2026-10-31.md`, `../../evidencias/the-boss/ia-conversacional/v3-horario-combo-promos-2026-10-31.md` (v3.1 publicada), `../../evidencias/the-boss/ia-conversacional/v3.2-estado-negocio-2026-10-31.md` (vigente). Originales canónicos en `../velo_wa/docs/the-boss/`; features en `../velo_wa/specs/done/agent-test-script-generator/` y `../velo_wa/specs/done/agent-open-status-context/`.
- **Notas**: discrepancias por depurar contra la evidencia del 11-oct — **179 tarifas activas** leídas el 31-oct vs **180 cargadas** el 11-oct; **31 ítems de catálogo** vs **23 productos** de la carta. Incidente abierto: `provider_unavailable` (OpenAI 503, 29-oct). Reporte del dueño (31-oct, TB-36: negativa de cobertura en «Carrera 35 #16-22») no se reproduce con v3+gpt-4.1. Pendientes de la ronda: alias de barrios (0 configurados), promociones no cargadas al catálogo (La Bandida, precios de asesoras), tope bot↔bot y respuestas a mensajes vacíos, acuerdo turno bot vs asesora, casos ⏳ (línea de prueba/horario/staging) y ronda en horario ABIERTO con v3.2. La automatización `enviar_menu` (`new_conversation`) está activa; transcripción de audio e interpretación de imágenes deshabilitadas.

### 2026-10-31 — Guion de pruebas para el establecimiento (borrador)

- **Qué se hizo**: se redactó `PRUEBAS_CLIENTE_AGENTE_2026-10-31.md` (esta carpeta): versión para el establecimiento (Diego y Paola) de los casos de prueba del agente — 14 casos customer-facing con mensajes copiables, resultado esperado y tabla de reporte con capturas. Derivado del guion interno TB-01..TB-36, sin jerga técnica, IDs internos ni datos del tenant.
- **Obligación asociada**: Obligación 5 (IA conversacional) — verificación con el establecimiento; insumo para las capturas 12-13 del plan.
- **Responsable**: MY SEO (harness, borrador).
- **Evidencia**: `PRUEBAS_CLIENTE_AGENTE_2026-10-31.md`.
- **Notas**: BORRADOR — el envío al establecimiento requiere aprobación explícita de Nicolás (`../../POLICIES.md`). El resultado devuelto (tabla + capturas) alimenta la validación de C-04.


