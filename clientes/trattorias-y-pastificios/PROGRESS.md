# PROGRESS — Trattorias y Pastificios S.A.S.

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

_(vacío inicial)_

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.

### 2026-10-03 — Caracterización preliminar ONO/DOYO (formulario de 9 bloques)
- **Qué se hizo**: se transcribió y consolidó el formulario de caracterización respondido por el establecimiento para las marcas ONO/DOYO (Paulo Restrepo, Director); se diligenció `CARACTERIZACION.md` con las secciones 1–8 y ≥3 brechas digitales priorizadas, y se actualizó `CLIENTE.md` con los datos reportados (contactos, línea 310 482 3232, horarios, cobertura, pagos, canales).
- **Obligación asociada**: 2 — C-01 (caracterización). Levantamiento preliminar; no es configuración, activación ni aceptación.
- **Responsable**: MY SEO (agente LLM del harness) con datos del establecimiento.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/caracterizacion-2026-10-03.md`.
- **Notas**: quedan campos por confirmar (menú/catálogo, volúmenes, ticket, tiempos, líneas 2 y 3) y por definir qué marca(s) atiende(n) la(s) línea(s) del beneficio (ONO/DOYO vs. KOMO), lo que ajusta el borrador `PLANTILLAS_WHATSAPP.md` y el alcance del workflow 03. C-01 queda `en_revision`.

### 2026-10-03 — Entrevista operativa con el establecimiento (minuta depurada)
- **Qué se hizo**: se depuró la transcripción de la entrevista con Paulo Restrepo (Director) y se archivó como minuta operativa; se incorporaron al `CARACTERIZACION.md` y al `CLIENTE.md` los datos confirmados (horarios, canales activos WhatsApp+Instagram, una sola línea por ahora, pagos incl. Bre-B, zonas Manizales/Villamaría con flota tercerizada, escalamiento a Ángela, alcance del agente IA con entrega a humano para cobro/domicilio, tono neutro-jovial, no aforo). La transcripción cruda no se conserva por contener datos personales.
- **Obligación asociada**: 2 — C-01 (caracterización). Complementa el formulario y afina el alcance de C-03/C-04.
- **Responsable**: MY SEO (agente LLM del harness) con datos del establecimiento.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/caracterizacion-entrevista-2026-10-03.md`.
- **Notas**: siguientes entregables del cliente: mensajes preestablecidos actuales y links de carta (ONO y DOYO) vía Ángela, y lista de tarifas de domicilio. Se acordó poner el bot a correr hacia jueves/viernes y agendar reunión de pruebas; la promoción de reactivación se define después. Sigue abierta la decisión de marca (ONO/DOYO vs. KOMO).

### 2026-10-03 — Links de menú MenuApp (ONO y DOYO) recibidos
- **Qué se hizo**: se registraron los links de MenuApp para DOYO, ONO y el general (cuenta `doyoyono`); se actualizó el pendiente de menú en `CARACTERIZACION.md`, `CLIENTE.md` y la minuta de entrevista.
- **Obligación asociada**: 4 — insumo para C-03 (vertical restaurantes / carta).
- **Responsable**: MY SEO (agente LLM del harness) con datos del establecimiento.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/menu-menupp-2026-10-03.md`.
- **Notas**: falta definir qué link envía la secuencia de carta según la marca que atienda la línea (decisión de marca abierta); el link general es un valor seguro intermedio.

### 2026-10-03 — Carta MenuApp capturada (DOYO & ONO) + plantillas WhatsApp v2
- **Qué se hizo**: se exploraron los 3 links de MenuApp con agentes (webfetch + render headless) y se consolidó la carta completa (DOYO: 65 productos/11 categorías; ONO: pokes + «arma tu poke» + bebidas/postres) en evidencia; se redactó el borrador v2 de `PLANTILLAS_WHATSAPP.md` para ONO/DOYO (bienvenida con mensaje del sismo + carta por link, escalamiento a Ángela, tono neutro/jovial), sustituyendo el borrador KOMO. Se actualizó `CARACTERIZACION.md` (conteos, fotos, precios, agotados) y `CLIENTE.md` (Instagram `@doyo_col`, discrepancia de dirección).
- **Obligación asociada**: 4 — C-03 (vertical restaurantes, insumo) y 5 — C-04 (agente IA). Borrador; no es configuración en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/carta-menupp-2026-10-03.md` y `PLANTILLAS_WHATSAPP.md`.
- **Notas**: discrepancias a resolver con el establecimiento: dirección (Cámara vs. MenuApp), pagos a domicilio (MenuApp muestra efectivo; el cliente dijo no), y reservas (MenuApp habilitadas; el cliente dijo no). C-03 pasa a `en_progreso`. Promoción/bono diferida hasta que el bot funcione.

### 2026-10-03 — Verificación del tenant en producción (waterfall, solo lectura)
- **Qué se hizo**: se consultó AriCRM en producción por SSH (`waterfall`, `php artisan tinker`, solo lectura) para verificar el tenant `trattorias-y-pastificios-sas-q1Vz`. La línea 310 482 3232 está **connected** (evolution, 2026-10-03 01:07 UTC). Se revisaron flags V2, agente IA, intención `pedir_menu` y usuarios.
- **Obligación asociada**: 3 y 6 — C-02 (tenant); insumo para C-04 (agente).
- **Responsable**: MY SEO (agente: solo lectura en producción).
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/config-tenant/verificacion-2026-10-03.md`.
- **Notas**: la línea conectada **no completa C-02** (per SOURCES). Brechas para correr el bot: flags V2 sin activar, intención `pedir_menu` no creada, agente IA deshabilitado y sin asignar a la línea (usa prompt genérico), y solo 1 usuario (Paulo, email sin verificar; falta invitar a Ángela). Todas son escrituras en producción que requieren aprobación. C-02 y C-04 pasan a `en_progreso`.

### 2026-10-03 — Configuración del agente ejecutada en producción (con aprobación)
- **Qué se hizo**: con aprobación de Nicolás, se escribieron en AriCRM producción (SSH `waterfall`, Eloquent): (1) flags V2 `automation_rule_builder_v2` y `automation_engine_v2_execute` en `tenant_messaging_features`; (2) intención `pedir_menu` (slug `pedir-menu`, activa); (3) agente IA `01a101af-…` habilitado, asignado a la línea `01a0c5dc-…` e con `prompt-v1` instalado (7489 chars, version `v1-trattorias-doyo-ono`). Verificación post-escritura confirmó todo.
- **Obligación asociada**: 5 — C-04 (agente IA); insumo para C-03 (reglas V2).
- **Responsable**: MY SEO (agente) con aprobación de Nicolás.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/config-tenant/verificacion-2026-10-03.md` (sección «Actualización 2026-10-03») y `../../evidencias/trattorias-y-pastificios/ia-conversacional/prompt-v1.md`.
- **Notas**: **el agente quedó en vivo** en 310 482 3232. Pendiente: invitar a Ángela (vía admin, flujo de email), crear y probar las reglas V2 (bienvenida + carta) con teléfonos controlados, y completar C-02 (líneas 2/3, contactos, canal Instagram). C-04 sigue `en_progreso` hasta las 5 conversaciones de prueba y el escalamiento verificado.

### 2026-10-03 — Carta física ONO + reglas V2 (bienvenida y carta) creadas en producción
- **Qué se hizo**: (1) se registró la foto de la carta impresa de ONO «Los Recomendados» (9 pokes con composición) como evidencia y se enriqueció el `prompt-v1` del agente con esas descripciones (reinstalado, 8753 chars). (2) Se crearon en producción las dos reglas V2 con acción `send_sequence`: **Bienvenida** (`new_conversation`, id `0b8ce31d-…`) y **Carta** (`ai_intent_detected` → `pedir-menu`, id `518c6f82-…`), ambas activas, de 2 pasos de texto cada una.
- **Obligación asociada**: 4 — C-03 (vertical restaurantes) y 5 — C-04 (agente IA).
- **Responsable**: MY SEO (agente) con aprobación de Nicolás.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/reglas-v2-2026-10-03.md` y `../../evidencias/trattorias-y-pastificios/carta-ono-recomendados-2026-10-03.md`.
- **Notas**: el bot queda funcional de punta a punta (agente + secuencias). Pendiente: **prueba con teléfonos controlados**, validar el copy/marca y confirmar que no haya mensaje duplicado. El asset de la foto de la carta no se archivó como archivo (llega solo como imagen en el chat); guardar en `evidencias/trattorias-y-pastificios/assets/carta-ono-recomendados-2026-10-03.jpg`.

### 2026-10-03 — Pruebas con teléfono controlado: la secuencia de bienvenida SÍ dispara; el paso 2 llega con ~78 s de retardo (no 2 s)
- **Qué se hizo**: pruebas end-to-end desde un teléfono controlado ("My SEO Company") a la línea 310 482 3232. En la prueba ~08:38 la **regla 1 (bienvenida, `new_conversation` → `send_sequence`)** entregó sus 2 pasos: el paso 1 (texto/sismo, sin link) a los ~8 s y el paso 2 (link `menupp.co/doyoyono`) a los ~86 s. Es decir, **la secuencia funciona**; el paso 2 llega con **~78 s de retardo** respecto al paso 1, no los 2 s configurados. En este run no hubo doble mensaje del agente. (Una prueba anterior ~08:26 había confundido el diagnóstico; se descarta como ruido.)
- **Obligación asociada**: 4 y 5 — C-03/C-04.
- **Responsable**: MY SEO (agente) con datos de la prueba reportada.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/test-bienvenida-2026-10-03.md`.
- **Notas**: descartado deploy de `send_sequence` (verificado 2026-09-30, `396ea59`) y flags V2 (activos). Hipótesis principal del retardo: los pasos con `delay_seconds > 0` se despachan por cron ~1 min (0s = inline, >0s = próximo tick) → 2s se vuelve ~78s. El chat de prueba del agente en UI (`app.aricrm.co/settings/ai-agent`) no dispara secuencias (solo prueba prompt/intenciones; los triggers `NewConversation`/`AiIntentDetected` requieren inbound real). Próximos: decidir retardo del paso 2 (recomendado: un solo paso con bienvenida+link, o paso 2 a 0s); con aprobación leer `automation_runs` del run 08:38; confirmar en `velo_wa` el despacho de pasos diferidos; validar copy/marca (1 vs 2 links) con Paulo/Ángela. C-03/C-04 siguen `en_progreso`.

### 2026-10-03 — Lectura a producción (SSH waterfall, solo lectura): retardo explicado y fix confirmado
- **Qué se hizo**: con aprobación, se leyó en producción `automation_runs` + `messages` de la regla 1 (bienvenida, id `0b8ce31d-…`). 2 runs, ambos `success`. El más reciente (13:43 UTC) tiene **un solo mensaje automatizado** (no dos): `hola` 13:43:38 → AUTO 13:43:42 (~4 s). Se leyó el cuerpo: copy reescrito (sismo condensado) + **link general** `doyoyono`. Además se confirmó en código (`velo_wa`, solo lectura) la causa del retardo de la prueba 08:38: el cooldown de seguridad `conversation_cooldown_seconds`=60 + jitter 0-15 en `AiAgentSafetyService::reserveOutboundSlot`, aplicado al segundo mensaje automatizado (no el `delay_seconds` ni un cron).
- **Obligación asociada**: 4 y 5 — C-03/C-04.
- **Responsable**: MY SEO (agente) con aprobación para lectura en producción.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/test-bienvenida-2026-10-03.md` (sección «Lectura a producción» y «Causa del retardo»); código `../velo_wa/app/Services/AiAgentSafetyService.php` y `app/Jobs/SendAutomationSequenceStep.php`.
- **Notas**: el usuario fusionó los dos pasos en un solo mensaje → retardo resuelto (~4 s). **Pendiente**: cambiar el link general por los dos links etiquetados (DOYO + ONO; la línea atiende ambas marcas, decisión 2026-10-03) y validar el copy con Paulo/Ángela. C-03/C-04 siguen `en_progreso`.

### 2026-10-03 — Swap de links ejecutado en producción (con aprobación)
- **Qué se hizo**: con aprobación, se actualizó en producción la acción `send_sequence` `01a10201-3061-73ff-bc71-381479e530f4` de la regla de bienvenida: se reemplazó el link general `https://menupp.co/doyoyono` por los dos links etiquetados (🍜 DOYO + 🥗 ONO) dentro del mismo paso de texto (un solo mensaje). Guarda de seguridad: solo se escribió si había exactamente 1 ocurrencia del link general (hubo 1). Verificación por relectura del `config` confirmó el nuevo cuerpo. No se tocó `delay_seconds`, `type`, `media_url` ni demás campos.
- **Obligación asociada**: 4 — C-03 (vertical restaurantes / carta).
- **Responsable**: MY SEO (agente) con aprobación explícita.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/vertical-restaurantes/secuencias/test-bienvenida-2026-10-03.md` (sección «Lectura a producción» + pendiente actualizado); `PLANTILLAS_WHATSAPP.md` (secuencia 1 con el cuerpo en producción).
- **Notas**: la línea 310 482 3232 atiende DOYO y ONO a la vez (decisión 2026-10-03). Pendiente: **re-probar con teléfono controlado** (verificar que el mensaje llega con ambos links renderizados) y **validar el copy con Paulo/Ángela** antes de abrir a clientes. C-03/C-04 siguen `en_progreso`.

### 2026-10-03 (tarde) — Reunión de equipo con el establecimiento: revisión del agente y decisión de marca (solo ONO)
> Corrección 2026-10-05: esta entrada se registró inicialmente con fecha 2026-10-05 (día de recepción de la transcripción). La verificación en producción de ese día mostró que los cambios pactados (prompt solo-ONO, links solo-ONO) quedaron guardados el 2026-10-03 entre las 16:04 y las 16:09 (hora del servidor), por lo que la reunión fue el 2026-10-03 por la tarde.
- **Qué se hizo**: reunión de avance (Nicolás por MY SEO; Paulo Restrepo, Steven y Sebastián por el establecimiento). Se revisó y validó con Paulo el `prompt-v1` ítem por ítem (9 pokes ONO + «Arma tu Poke»; confirmó Poke Pork fuera de producción) y se probó el agente en vivo (consulta veggie, lechuga, toppings, adición de zanahoria, salsa Fuji) con resultado correcto. **Decisiones del establecimiento**: (1) la línea 310 482 3232 atiende **solo ONO**; **DOYO queda en stand-by** (pedirán a MenuApp que lo oculte); en la reunión se ajustó en vivo la plantilla de bienvenida al link solo-ONO —pendiente de verificación—; (2) escalamiento a Ángela Bedoya (pedidos/catering) y **Steven como segundo contacto** para órdenes especiales/muy grandes; (3) crear **usuario AriCRM para Steven** para auditoría diaria de conversaciones; (4) cambiar el icono de la línea al logo ONO; (5) el cierre del pedido lo hace **MenuApp** (comanda a cocina + impresión en punto de venta): el bot guía el armado y entrega a la persona humana, no cobra ni factura. Propuestas abiertas (no decididas): bono de $5.000 post-Rappi para capturar contactos, campaña masiva de recuperación con la base propia (sin CRM; preocupación por fuga de datos y baneo), línea API para reducir el delay.
- **Obligación asociada**: 2, 4 y 5 — C-01 (marca de la línea definida), C-03 (link solo-ONO) y C-04 (prompt validado con el establecimiento).
- **Responsable**: MY SEO (agente LLM del harness); reunión dirigida por Nicolás.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/reunion-revision-bot-2026-10-03.md` (transcripción depurada con decisiones, glosario y acuerdos).
- **Notas**: pendientes salidos de la reunión: tarifas de la flota tercerizada (discrepancias MenuApp vs. entrevista), screenshot del placeholder del link (lo envía Paulo), crear el usuario de Steven, carga de contactos con guía anti-ban (indicar a Steven), activación del link solo-ONO en MenuApp (Paulo conversa con MenuApp), replicar el prompt para la línea unificada. Config visible: contexto 20 mensajes, modelo GPT-4 mini. El ajuste de la plantilla se hizo en vivo durante la reunión: la configuración quedó verificada en producción el 2026-10-05 (ver esa entrada); falta la re-prueba con teléfono controlado. C-03/C-04 siguen `en_progreso`; C-01 avanza (marca definida, sigue `en_revision`).

### 2026-10-05 — Verificación en producción (SSH waterfall, solo lectura): el prompt del agente SÍ corresponde a lo pactado
- **Qué se hizo**: a solicitud de Nicolás, se leyó en producción (SSH `waterfall`, `php artisan tinker`, sin escrituras) el agente `01a101af-…`, las reglas V2, la línea y la intención, y se compararon contra lo pactado en la reunión del 2026-10-03. **Corresponde en lo esencial**: el prompt (7945 chars, actualizado 2026-10-03 16:04) ya dice «asistente virtual de *Ono*», sin catálogo DOYO, con link específico de ONO, catering escalando a Steven y escalamiento general a Ángela; los datos operativos (pagos, horarios, cobertura, 30 min, no reservas), el catálogo ONO validado ítem por ítem y el flujo pactado están intactos. Bienvenida y carta envían **solo el link de ONO** (acciones actualizadas 16:06). Agente habilitado, `allow_all_lines=true` (todas las líneas, como se pactó), `context_messages=20`, `llm_model=gpt-4o-mini`; línea `connected` sin pausa IA; intención `pedir-menu` activa. **Residuos a corregir** (no cambian el comportamiento esencial): nombres de reglas siguen «DOYO & Ono», label de línea sigue «Dojo», texto interno del prompt dice «Link general (una sola línea atiende ambas marcas)» sobre el link de ONO, contradicción menor en escalamiento de catering (sección eventos→Steven vs. lista obligatoria→Ángela), sección «Puntos abiertos» y escapes de sanitización (`\$`, `\*\* escala**`) dentro del prompt, y `config.prompt_version` aún `v1-trattorias-doyo-ono`. El icono de perfil de WhatsApp no se gestiona desde AriCRM (pendiente desde el teléfono, como se pactó con Steven).
- **Obligación asociada**: 5 — C-04 (agente IA); también C-03 (verificación de links solo-ONO).
- **Responsable**: MY SEO (agente) — lectura en producción autorizada por Nicolás en esta conversación.
- **Evidencia**: `../../evidencias/trattorias-y-pastificios/ia-conversacional/verificacion-prompt-2026-10-05.md` y `../../evidencias/trattorias-y-pastificios/ia-conversacional/prompt-v1.1-solo-ono-2026-10-03.md` (texto exacto en producción).
- **Notas**: fechado de la reunión corregido a 2026-10-03 con base en estos timestamps. La verificación es de **configuración**, no de entrega del mensaje: falta la re-prueba con teléfono controlado y las 5 conversaciones de C-04. C-03/C-04 siguen `en_progreso`.
