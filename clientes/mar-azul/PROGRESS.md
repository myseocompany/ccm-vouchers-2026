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

### 2026-10-31 — Material interno de capacitación de salón archivado y transcrito
- **Qué se hizo**: se revisó el archivo `CAPACITACION PERSONAL SALON.pptx` (23 diapositivas, material interno del establecimiento: saludo institucional, recordación de marca, diferencias entre platos, técnicas de venta, propinas, ofrecimiento de postres y tabla de incentivos del personal). Se archivó el original en `evidencias/mar-azul/capacitacion/` (verificado por SHA-256 `08269d7433c3de984e795cab8ee53b22b9da61441a2c5b9c751b704b44e9aa6f`) y se transcribió a Markdown para trabajo. El deck es preexistente al contrato: creado 2018-04-17, última modificación 2021-07-23 según metadatos; la copia recibida en `~/Downloads` tenía fecha 2026-10-02.
- **Obligación asociada**: 7 — insumo de C-05 (`05_capacitacion`); también insumo de descripciones de platos para C-03/C-04. No acredita capacitación ejecutada ni cierra C-05.
- **Responsable**: MY SEO (harness), por instrucción de Nicolás.
- **Evidencia**: `../../evidencias/mar-azul/capacitacion/CAPACITACION PERSONAL SALON.pptx` y `capacitacion/capacitacion-personal-salon-2026-10-31.md`.
- **Notas**: **(1)** Las descripciones de platos del deck (sabor, preparación, alérgenos frecuentes, recomendaciones por perfil de cliente) son más ricas que la carta transcrita y pueden alimentar el menú y el prompt v6, previa validación del establecimiento. **(2)** La tabla de incentivos menciona hamburguesa de filete (noche) y pizzas (noche), productos que no están en la carta de WhatsApp transcrita: pendiente confirmar si siguen ofreciéndose (el deck es de 2021). **(3)** La política de propina sugerida (5%) y los incentivos son información interna del personal: no incorporarlas al prompt del agente ni a comunicaciones a clientes finales.

### 2026-10-31 — Almuerzo ejecutivo confirmado por el establecimiento; regla canónica y guion de pruebas
- **Qué se hizo**: la gerente administrativa confirmó la definición del almuerzo ejecutivo: filete apanado, bagre, mojarra, sierra o trucha, acompañado de sopa de pescado, arroz de coco, patacón y ensalada, **con bebida de agua de panela con limón**, $26.000, solo hasta las 3:00 p. m. Se creó la fuente canónica en evidencias, se actualizó `CLIENTE.md` (restricciones operativas) y `CARACTERIZACION.md` (§3, §6, §9), y se creó `PRUEBAS_CONVERSACIONALES.md` con los casos del ejecutivo ajustados a la definición confirmada (corrigen la respuesta errónea de la prueba de la sesión, que decía «limonada de la casa»). El borrador de confirmación quedó respondido.
- **Obligación asociada**: 4 — C-03 vertical restaurantes (definición de menú); insumo de C-04 (regla v6 del agente). No acredita carga en producción ni cierre de tareas.
- **Responsable**: establecimiento (confirmación, vía Nicolás); MY SEO (documentación).
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/almuerzo-ejecutivo-2026-10-31.md`, `PRUEBAS_CONVERSACIONALES.md`, `borrador-confirmacion-almuerzo-ejecutivo-2026-10-31.md` (respondido).
- **Notas**: **(1)** La bebida confirmada (agua de panela con limón) no aparece en la carta de WhatsApp transcrita ni en el prompt v5; el `menú del día` de AriCRM sigue vacío y esta definición es la que debe cargarse allí o derivarse a la v6. **(2)** Quedan sin confirmación expresa: si las cinco opciones son siempre las mismas o cambian por día; el manejo del arroz blanco (¿preguntar o solo a petición?); los cambios de acompañamiento y su costo. **(3)** El guion de pruebas es plan, no prueba ejecutada: registrar los resultados en `evidencias/mar-azul/ia-conversacional/` cuando se corra.

### 2026-10-31 — Acompañantes de los platos de carta confirmados; guion de pruebas ampliado
- **Qué se hizo**: la gerente administrativa confirmó las reglas de acompañantes: los platos de carta van **sin sopa ni bebida**; cazuelas, sancocho, pescados de carta y especialidades llevan **arroz, patacón y ensalada** (excepciones: ensalada Brisa del Mar y mix de mariscos, solo arroz y patacón por ser a base de verduras); los arroces llevan **patacón y ensalada** (la paella, **patacón con queso**); los ceviches, **galletas de soda**. Se creó la fuente canónica en evidencias, se amplió el guion de pruebas con los casos T11–T18 de acompañantes (renumerando el resto, sin resultados ejecutados previos que dependieran de los IDs) y se actualizaron `CLIENTE.md` y `CARACTERIZACION.md` (§3 y §9).
- **Obligación asociada**: 4 — C-03 vertical restaurantes (definición de menú); insumo de C-04 (regla v6 del agente). No acredita carga en producción ni cierre de tareas.
- **Responsable**: establecimiento (confirmación, vía Nicolás); MY SEO (documentación).
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/acompanantes-carta-2026-10-31.md`, `PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: consistente con la carta transcrita (todos los pescados «con arroz de coco, patacón y ensalada») y con lo discutido en la sesión de coaching para las cazuelas. Quedan por confirmar: si el arroz estándar de los acompañamientos es siempre de coco (la carta lo especifica así; la regla confirmada dice «arroz») y el caso de la langosta (el deck de capacitación de 2021 la trae con arroz caribeño).

### 2026-10-31 — Menú fijo confirmado: sin variación diaria
- **Qué se hizo**: el establecimiento confirmó que **no cambia el menú a diario: tiene el mismo menú todos los días**; el almuerzo ejecutivo mantiene siempre las mismas cinco opciones. Cierra el punto abierto 1 de la confirmación del ejecutivo (carácter fijo de las opciones) y formaliza lo ya acordado en la sesión de coaching («no vamos a tener almuerzo del día»). Se actualizó la fuente canónica del ejecutivo (nueva sección «Menú fijo» y fila «Variación diaria: ninguna»), `CLIENTE.md`, `CARACTERIZACION.md` (§3 y §9) y el guion de pruebas (nuevo caso T11 de menú fijo; los acompañantes pasan a T12–T19 y el resto a T20–T27, sin resultados ejecutados previos que dependieran de los IDs).
- **Obligación asociada**: 4 — C-03 vertical restaurantes; insumo de C-04 (regla v6: el agente nunca responde con un menú variable ni dice que no sabe qué hay hoy).
- **Responsable**: establecimiento (confirmación, vía Nicolás); MY SEO (documentación).
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/almuerzo-ejecutivo-2026-10-31.md` (sección «Menú fijo»), `PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: consistente con el levantamiento (§3: la carta cambia ~una vez al año por precios) y con la decisión de la sesión de coaching. El `menú del día` de AriCRM no se usa para publicar menús distintos por fecha; la definición fija del ejecutivo puede cargarse allí o derivarse al prompt v6.

### 2026-10-31 — `get_daily_menu` fuera del tenant; correcciones de acompañantes por plato
- **Qué se hizo**: **(1)** Nicolás decidió que la herramienta `get_daily_menu` **no se debe usar en este tenant**: la definición del ejecutivo va embebida en el prompt v6 (hoy la herramienta figura habilitada en `enabled_tools` según la verificación de producción del 2026-10-30; retirarla es cambio de producción para el despliegue de la v6). **(2)** La gerente administrativa corrigió/confirmó acompañantes por plato (WhatsApp 11:38–11:40): **Cayana Mar Azul con arroz y ensalada** (la base es patacón con trucha; corrige la carta transcrita, que decía «arroz de coco, patacón y ensalada»), **patacón marinero con ensalada** y **pasta marinera con patacón**. Se actualizaron las fuentes canónicas, la nota de la carta transcrita y el guion de pruebas.
- **Obligación asociada**: 4 — C-03 vertical restaurantes; insumo de C-04 (regla v6 del agente).
- **Responsable**: Nicolás (decisión de herramienta); establecimiento (correcciones, vía WhatsApp); MY SEO (documentación).
- **Evidencia**: `../../evidencias/mar-azul/vertical-restaurantes/almuerzo-ejecutivo-2026-10-31.md` (sección «Menú fijo»), `../../evidencias/mar-azul/vertical-restaurantes/acompanantes-carta-2026-10-31.md` (actualización 11:38–11:40), `PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: **(1)** Guion de pruebas: caso T11 de menú fijo, casos T20–T22 de platos corregidos y contextos reformulados sin `get_daily_menu` (ejecutivo T01–T10; acompañantes T12–T19; reservas/domicilio/pagos/seguridad T23–T30). **Rectificación**: el renumerado anunciado en la entrada «Menú fijo confirmado» quedó aplicado solo con esta entrada. **(2)** Pendientes de confirmación: si el patacón marinero también lleva arroz y si la pasta marinera también lleva ensalada; se suman al tipo de arroz estándar y al caso de la langosta. **(3)** Patrón emergente (inferencia): los platos cuya base es el propio acompañante no lo repiten como guarnición (los a base de patacón no llevan patacón, como los a base de verduras no llevan ensalada).

### 2026-10-31 — Addendum al guion de regresión MA: decisiones y confirmaciones posteriores a las rondas
- **Qué se hizo**: se detectó trabajo paralelo registrado en `../../evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md`: guion de regresión MA-01…MA-32 corrido hoy en 4 rondas (v6 publicada 2026-10-30; **v7 publicada 2026-10-31** con `gpt-4.1`; v8 en preview sin publicar). Las expectativas MA-01/MA-02 exigen consultar `get_daily_menu`, en conflicto con la decisión del mismo día de no usar esa tool en el tenant. Se añadió un **addendum con fecha al final del guion** (sin tocar el registro histórico de rondas) que invierte esas expectativas, señala que el bloque «Menú del día (herramienta obligatoria)» lo añade el código (`AiAgentService::appendDailyMenuToolContext` → cambio en `velo_wa`) y registra la definición del ejecutivo con bebida y las correcciones de acompañantes como pendientes para la próxima versión del prompt. Se actualizaron además las referencias al prompt vivo en la fuente canónica del ejecutivo y en `PRUEBAS_CONVERSACIONALES.md` (contextos y nota de domicilio alineados con el comportamiento verificado en las rondas).
- **Obligación asociada**: 5 — C-04 IA conversacional (gestión del guion de pruebas); insumo de la próxima versión del prompt.
- **Responsable**: MY SEO (harness).
- **Evidencia**: `../../evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md` (addendum), `../../evidencias/mar-azul/vertical-restaurantes/almuerzo-ejecutivo-2026-10-31.md`, `PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: **(1)** El archivo PREGUNTAS_DUENA_2026-10-30.md, referenciado por el guion MA, no existe en este repo (probablemente en `velo_wa`); el validador la reporta como referencia rota. **(2)** Pendientes para la próxima versión del prompt (trabajo en `velo_wa`/producción, con autorización): retirar `get_daily_menu` de `enabled_tools`, retirar el bloque de menú del día de la ruta productiva, e incorporar la definición del ejecutivo con bebida y las reglas de acompañantes confirmadas. **(3)** Rectifica la entrada anterior: el retiro de la tool ya no es «para el despliegue de la v6» (v6 y v7 ya publicadas), sino para la versión siguiente a la v8.

### 2026-10-31 — Spec P-016 para velo_wa: retiro de `get_daily_menu` y prompt v9
- **Qué se hizo**: se redactó el spec `../../tasks/P-016-retiro-daily-menu-y-prompt-v9-calamar-azul.md` para el agente de `velo_wa`, con tres frentes: **(A)** config del tenant — quitar `get_daily_menu` e `is_holiday` de `enabled_tools` y pasar `daily_menu_tool_enabled` a `false`; **(B)** gate de código — que `appendDailyMenuToolContext()` solo agregue el bloque «Menú del día» a agentes con la tool habilitada (evolución del producto, sin afectar a tenants de menú variable como La Rancha); **(C)** prompt v9 — ramificado de la v8, incorporando la definición confirmada del ejecutivo (con bebida), el menú fijo y las reglas de acompañantes, conservando las ganancias v7/v8. Se registró la tarea P-016 en `TASKS.md` como pendiente.
- **Obligación asociada**: 5 — C-04 IA conversacional (coordinación del cambio; la implementación vive en `velo_wa`).
- **Responsable**: MY SEO (harness, redacción del spec); implementación pendiente por el agente de `velo_wa`.
- **Evidencia**: `../../tasks/P-016-retiro-daily-menu-y-prompt-v9-calamar-azul.md` y fila P-016 en `../../TASKS.md`.
- **Notas**: el spec cita los datos verificados de producción del 2026-10-30 (agente `01a14570-da52-70b4-b234-ba7b128d642a`, 12 tools, flag `daily_menu_tool_enabled: true`, `is_holiday` muerta, metadatos de versión falsos) y deja fuera de alcance la deuda del campo de notas de `quote_order`, los aliases de barrios y los bloqueos del camino WhatsApp real. Este harness no edita `velo_wa`: el spec es la tarea específica para ese repo.

### 2026-10-31 — Guion MA-01..32 de velo_wa archivado; rondas v6→v8 registradas; guion para el establecimiento

- **Qué se hizo**: (1) se localizó en `velo_wa` el guion de pruebas del agente (MA-01..MA-32, derivado de un dump de producción del 30-oct: 179 conversaciones, 2.645 mensajes, estímulos anonimizados) y se archivó copia fiel verificada por hash; (2) se registró su estado: **prompt v6 publicado el 30-oct** (domicilios y reservas con `get_delivery_fee`), **v7 publicado el 31-oct** (`v7-disciplina-tools-y-escalamiento`) con modelo `gpt-4.1` persistido — ronda 3 con el harness del release: **32/32 casos en verde, cero errores de herramienta**; **v8 en preview** (diff de dos líneas) cerrando los 3 defectos restantes de «promesas» sin publicarse; (3) se reescribió `PRUEBAS_CLIENTE_AGENTE_2026-10-31.md` derivándolo del guion MA — 16 casos customer-facing con las expectativas del prompt vigente — en el formato usado para The Boss (reemplaza el borrador anterior basado en `PRUEBAS_CONVERSACIONALES.md`).
- **Obligación asociada**: 5 — C-04 (IA conversacional): guion, rondas y verificación con el establecimiento; insumo para C-03 (pedido end-to-end desde WhatsApp real).
- **Responsable**: MY SEO — rondas y prompts ejecutados en velo_wa (worktrees `calamar_azul` / `calamar-azul-v6`); archivo para el establecimiento redactado por el harness.
- **Evidencia**: copia `../../evidencias/mar-azul/ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md` (hash verificado == original); original canónico `../../../velo_wa/docs/mar-azul/MENSAJES_PRUEBA_2026-10-30.md`; guion para el establecimiento `PRUEBAS_CLIENTE_AGENTE_2026-10-31.md`.
- **Notas**: **(1)** El agente sigue `is_enabled = false` con pilot mode (3 teléfonos autorizados): el camino real de WhatsApp — `create_order` de punta a punta y handoff efectivo a la cajera — sigue pendiente y es exactamente lo que la prueba con el establecimiento debe cubrir; requiere autorizar el teléfono de prueba en `pilot_allowed_phones` (escritura en producción, con aprobación explícita). **(2)** Deuda de producto anotada en las rondas: `quote_order` sin campo de notas (los cambios de acompañamiento viven solo en el texto del bot); `get_daily_menu` sin marker `ReadOnlyTool`; menú del día sin publicar (el ejecutivo se cotiza desde el catálogo y las opciones del día las confirma caja). **(3)** Pendientes de datos: tarifas contradictorias (Arenillo, La Castellana, Santos) y aliases de barrios sin cargar. **(4)** El envío del guion al establecimiento requiere aprobación explícita de Nicolás (`../../POLICIES.md`).


