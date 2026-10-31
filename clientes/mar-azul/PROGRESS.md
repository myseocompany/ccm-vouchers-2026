# PROGRESS — Calamar Azul (Grupo D Mar Azul S.A.S.)

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

### 2026-10-16 — Sede Cable y bandas de domicilio creadas
- **Qué se hizo**: se creó y verificó en producción la sede Cable y tres bandas de domicilio: $5.000, $8.000 y $12.000.
- **Obligación asociada**: preparación de C-02/C-03; no constituye tenant completo, línea conectada ni activación.
- **Responsable**: MY SEO, con autorización explícita de Nicolás.
- **Evidencia**: `../../evidencias/mar-azul/config-tenant/sede-cable-tarifas-2026-10-16.md`.
- **Notas**: falta el mapa barrio→banda; no automatizar cotización por barrio todavía.

### 2026-10-16 — Prompt v1 y fuentes privadas archivadas
- **Qué se hizo**: se archivaron la conversación y el CSV aportados como fuentes privadas, se incorporó la carta estructurada y se elaboró el prompt v1 con toma segura de solicitudes y escalamiento humano.
- **Obligación asociada**: preparación de C-01, C-03 y C-04; no se realizó carga ni activación en producción.
- **Responsable**: MY SEO, por instrucción de Nicolás.
- **Evidencia**: `../../evidencias/mar-azul/caracterizacion/fuentes/`, `../../evidencias/mar-azul/vertical-restaurantes/menu/carta-mar-azul-whatsapp-2026-10-16.md` y `../../evidencias/mar-azul/ia-conversacional/prompt-v1.md`.
- **Notas**: validar disponibilidad, tarifas de domicilio, reglas de pago y reservas antes de publicación.

### 2026-10-16 — Borrador de carta WhatsApp transcrito desde capturas
- **Qué se hizo**: se estructuró un borrador de carta con productos, precios y descripciones legibles en las capturas entregadas para Mar Azul. No se cargó ni publicó en AriCRM.
- **Obligación asociada**: 4 — plantilla vertical restaurantes (preparación de menú digital).
- **Responsable**: MY SEO.
- **Evidencia**: `clientes/mar-azul/carta/carta-whatsapp-2026-10-16.md`; fuente local suministrada: `~/Desktop/carta_whatsApp/` (26 capturas, consultadas 2026-10-16).
- **Notas**: pendiente validación expresa del establecimiento sobre precios, gramajes, disponibilidad y descripciones antes de cualquier carga o envío.

### 2026-10-30 — Tarifas reales de domicilio cargadas a producción (Cable y Centro)
- **Qué se hizo**: se construyó el mapa barrio→tarifa de las dos sedes a partir de las transcripciones de WhatsApp de la gerente administrativa (2026-10-15 Centro, 2026-10-16 Cable) y se cargó a producción: **133 tarifas en Sede Cable** (7 bandas, de $6.000 a $15.000) y **133 en Sede Centro** (10 bandas), mismo universo de barrios y misma grafía canónica. Se eliminaron los 3 placeholders del onboarding (`Tarifa mínima/intermedia/lejana — barrio pendiente`, $5.000/$8.000/$12.000), con respaldo previo en el servidor antes de borrarlos.
- **Obligación asociada**: 4 — C-03 vertical restaurantes. Cierra la brecha digital 3 del levantamiento (domicilios sin tarifa estandarizada) en la capa de datos.
- **Responsable**: MY SEO, por instrucción de Nicolás.
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/domicilios/domicilios-cable-2026-10-30.md` y `../../evidencias/mar-azul/vertical-restaurantes/domicilios/domicilios-centro-2026-10-30.md` (copias fieles de los documentos técnicos de `velo_wa`, worktree `calamar_azul`, rama `myseocompany/calamar_azul`).
- **Notas**: Sede Centro nace con `is_active = false` deliberadamente: el prompt no está preparado para dos sedes y `get_delivery_fee`/`get_catalog` exigen `branch_id`. **La carga de datos no cambia nada para el cliente todavía**: el prompt en producción no referencia `get_delivery_fee`, así que el agente sigue escalando el valor del domicilio a caja. Ver entrada del mismo día sobre el prompt v5.

### 2026-10-30 — Reglas de reserva confirmadas por el cliente
- **Qué se hizo**: Nicolás confirmó la franja de reserva y se documentó como fuente canónica: **lunes a sábado de 2:00 a 4:30 p. m.**, retención de 30 minutos, excepción en fechas especiales (Día de la Madre), **eventos empresariales pactables fuera de la franja**, y costo de $20.000 la reserva / $30.000 con decoración. Se registró también el motivo de negocio: el alto flujo del almuerzo y el no-show que bloquea mesas.
- **Obligación asociada**: 4 — C-03 vertical restaurantes. Resuelve la ambigüedad de valores de la brecha digital 4; el procedimiento de cobro sigue pendiente.
- **Responsable**: Nicolás (fuente) y MY SEO (documentación).
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/reservas-2026-10-30.md`.
- **Notas**: el tope de 4:30 p. m. y los eventos empresariales **no existen en el prompt vivo**, que sigue diciendo «después de las 2:00 p. m.» sin tope. El agente no confirma reservas: toma la solicitud y escala a la cajera en turno.

### 2026-10-30 — Prompt de producción editado por fuera del repo; capturado como línea base v5
- **Qué se hizo**: se detectó que el `system_prompt` del agente fue editado directamente en producción (`ai_agents.updated_at` = 2026-10-30 20:51:46, autor no registrado), divergiendo del último snapshot versionado (v4). Se capturó como línea base `v5-recuperada-produccion-2026-10-30`, verificada contra producción por SHA-256 `4c21a851…` y confirmada íntegra (4943 caracteres, sin truncamiento).
- **Obligación asociada**: 5 — C-04 IA conversacional.
- **Responsable**: MY SEO.
- **Evidencia**: `../../evidencias/mar-azul/ia-conversacional/prompt-v5-recuperada-produccion-2026-10-30.md`.
- **Notas**: **cuatro desfases pendientes de corregir en una v6**, ninguno desplegado aún: (1) el prompt declara las bandas obsoletas de $5.000/$8.000/$12.000, afirma que falta el mapa barrio→banda y perdió toda referencia a `get_delivery_fee`, por lo que las 266 tarifas cargadas quedan inertes; (2) falta el tope de 4:30 p. m. en reservas; (3) no contempla eventos empresariales; (4) reintrodujo la carta con precios literales que el v4 había quitado a propósito para que todo saliera de `get_catalog`, creando dos fuentes de precio que pueden desfasarse. **Riesgo abierto**: `is_enabled = true` al momento de la captura, mientras AGENTS.md documenta el pilot mode con `is_enabled = false`; confirmar con Nicolás si abrir el agente fue deliberado antes de cualquier despliegue, porque define si el bot ya responde a clientes reales.

### 2026-10-30 — Rectificación: el agente está apagado y las herramientas sí están habilitadas
- **Qué se hizo**: verificación de solo lectura de producción por SSH (`waterfall`, release `d4e3cf55`) de los dos tenants del programa que tienen agente IA. Rectifica tres afirmaciones de la entrada «Prompt de producción editado por fuera del repo» de este mismo día, que se basaba en la captura del v5 y no en una consulta directa.
- **Obligación asociada**: 3, 4 y 5 — insumo de C-02/C-03/C-04; no acredita cierre de ninguna.
- **Responsable**: MY SEO (harness), por instrucción de Nicolás.
- **Evidencia**: `../../evidencias/mar-azul/ia-conversacional/verificacion-produccion-2026-10-30.md`.
- **Notas**: **(1)** `is_enabled = false`, no `true`: el agente estuvo habilitado durante la edición de las 20:51 y se desactivó a las 21:29:32, y `pilot_mode_enabled` sigue en `true` con 3 teléfonos autorizados, así que el pilot mode nunca se abrió y el bot no está atendiendo clientes reales. **(2)** `config.enabled_tools` sí habilita `get_catalog`, `quote_order`, `create_order`, `get_delivery_fee` y `get_daily_menu`: el desfase de las 266 tarifas es solo del texto del prompt, no de la configuración. **(3)** Aparecen dos desfases nuevos: `enabled_tools` arrastra `is_holiday`, herramienta que ya no existe en el código desplegado, y `config.prompt_sha256`/`prompt_version` no corresponden al prompt vivo. **(4)** La capa conversacional está vacía (0 plantillas, 0 etiquetas, 0 intenciones, 0 automatizaciones) y `orders = 0`, así que dos criterios de C-03 están incumplidos, no solo pendientes de documentar. **(5)** Hay una línea WhatsApp conectada y vinculada al agente, lo que corrige el «pendiente de autorización» de `CLIENTE.md`.

