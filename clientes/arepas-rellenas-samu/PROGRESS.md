# PROGRESS — Arepas Rellenas Samu

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

### 2026-09-30 — Caracterización completa

- **Qué se hizo**: Reunión de caracterización con Adrián Sepúlveda. Se completó formulario CSV (AriCRM_CCMPC - arepasSamu.csv) y sesión de preguntas. Se llenaron CARACTERIZACION.md y CLIENTE.md con datos de operación, canales, menú, pedidos, pagos, FAQs, tono de marca y brechas. Se conectaron las dos líneas WA al tenant (314 337 1048 y 313 492 9669).
- **Obligación asociada**: C-01 (obligación 2 — caracterización)
- **Responsable**: Nicolás Navarro Rincón
- **Evidencia**: `evidencias/arepas-rellenas-samu/caracterizacion-2026-09-30.md`
- **Notas**: Menús entre sedes aún no unificados; Adrián los iguala semana del 2026-10-06 (tocineta + precios). Sandra (Cámara) confirmó que el alcance aplica para las dos sedes — formalizar por escrito. Cliente interesado en línea Cloud API para campañas futuras.

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.

### 2026-09-30 — Piloto del flujo bienvenida + carta; acción `send_template` publicada
- **Qué se hizo**: (1) Se publicó la acción V2 `send_template` de AriCRM a `main` (PR #19, squash `396ea59`); el merge no deploya (deploy manual). (2) Se designó este establecimiento como piloto del flujo "plantilla de bienvenida al inicio de la conversación + plantilla de carta cuando el cliente la pide", para aprender en un solo tenant y replicar la configuración a los demás locales.
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04.
- **Responsable**: MY SEO (agente LLM del harness); decisión de piloto: Nicolás.
- **Evidencia**: `PLANTILLAS_WHATSAPP.md` (prerrequisitos del piloto con estado); PR fusionado: https://github.com/myseocompany/velo_wa/pull/19
- **Notas**: bloqueos del piloto a la fecha: las líneas actuales son Evolution y la acción exige línea Cloud API, el menú entre sedes se unifica la semana del 2026-10-06, y las plantillas aún no están registradas en Meta. El deploy a producción se coordina cuando la línea Cloud API esté lista.

### 2026-09-30 — Rectificación: el piloto usa «Enviar secuencia», no «Enviar plantilla»
- **Qué se hizo**: se ajustó el diseño del piloto (decisión de Nicolás): las reglas V2 (bienvenida y carta) usan la acción `send_sequence`, no `send_template`. Consecuencias: (1) funciona sobre las líneas Evolution actuales sin migrar a Cloud API; (2) no requiere plantillas aprobadas por Meta; (3) las "plantillas de respuesta" del programa se definen como secuencias de mensajes (texto/imagen con pausas acumuladas y guardas de corte).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04.
- **Responsable**: decisión: Nicolás; actualización de documentos: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md` (secuencias y prerrequisitos actualizados); `../../templates/PLANTILLAS_WHATSAPP.md` (mecanismo con `send_sequence`).
- **Notas**: esta entrada rectifica la anterior de hoy en cuanto al mecanismo: la línea Cloud API y la aprobación de Meta dejan de ser bloqueos del piloto. Pendientes reales: deploy a producción, flags V2 del tenant, intención `pedir_menu`, contenido de la carta (unificación de menús entre sedes, semana del 2026-10-06) y validación del copy con Adrián.

### 2026-09-30 — Deploy a producción verificado; piloto acotado a la sede San Jorge
- **Qué se hizo**: (1) Deploy de producción completado por el mecanismo estándar de Waterfall (push a `origin/main` → Forge): release activo `396ea59` con las acciones `send_sequence` y `send_template`. Verificación post-deploy del runbook completa: `/up` y `/login` en 200, manifest de assets presente (build 14:18), 0 migraciones pendientes. (2) Piloto acotado a la sede San Jorge (decisión de Nicolás): el primer agente envía el menú como bienvenida — réplica automatizada de la práctica actual del negocio (carta automática al primer mensaje), usando la carta actualizada de San Jorge (con tocineta) según la caracterización.
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04.
- **Responsable**: MY SEO (agente LLM del harness); decisión de alcance: Nicolás.
- **Evidencia**: release verificado por SSH en `waterfall` (`git log -1` = `396ea59`, manifest OK, `migrate:status` sin pendientes); salud pública `https://app.aricrm.co/up` = 200; secuencias del piloto en `PLANTILLAS_WHATSAPP.md` de esta carpeta.
- **Notas**: pendientes del piloto: confirmar con Adrián cuál de las 2 líneas es la de San Jorge (313 492 9669, suposición), flags V2 del tenant, intención `pedir_menu`, carta de San Jorge con el número corregido en el diseño (Adrián) y validación del copy.

### 2026-09-30 — Flags V2 activados en el tenant de prueba `restaurante-domicilios-v1`

- **Qué se hizo**: se activaron los flags `automation_rule_builder_v2` (editor) y `automation_engine_v2_execute` (ejecución) en el tenant de prueba `restaurante-domicilios-v1` de AriCRM producción, para poder armar ahí el demo del piloto (reglas V2 de bienvenida + carta con `send_sequence`). El write replica el endpoint SuperAdmin (`TenantMessagingFeature::updateOrCreate`) vía SSH a `waterfall`. Verificación previa de blast radius: el tenant no tenía reglas V2 (solo 4 automatizaciones plantilla V1 inactivas) → activar el motor no dispara nada hasta crear reglas.
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04 (demo en tenant de prueba, no en el tenant del cliente).
- **Responsable**: MY SEO (agente LLM del harness); aprobación explícita: Nicolás.
- **Evidencia**: fila en `tenant_messaging_features` (tenant `01a0af48-00e2-70c0-ad2d-10efad059912`): `automation_rule_builder_v2=1`, `automation_engine_v2_execute=1`; verificación efectiva vía `MessagingFeatureFlags::enabled` = `editor_v2=1 engine_v2_execute=1` (SSH waterfall, 2026-09-30).
- **Notas**: el tenant real de Samu (`arepas-rellenas-samu-UK5K`) queda **pendiente** de flags hasta validar el demo en el tenant de prueba. `updated_by` quedó null (sin sesión SuperAdmin); esta entrada funge como auditoría del cambio. No existe ningún preset `restaurante-domicilios-v1` en el código: es simplemente el tenant de prueba ya provisionado (con 4 automatizaciones plantilla V1 inactivas).

### 2026-09-30 — Flags V2 activados en el tenant real de Samu; intención `pedir_menu` verificada y creada

- **Qué se hizo**: (1) Tras el bloqueo reportado por Nicolás en la UI del tenant de Samu (`settings/automations` sin builder V2), se activaron los flags `automation_rule_builder_v2` y `automation_engine_v2_execute` también en el tenant **real** de Samu (`arepas-rellenas-samu-UK5K`), con el mismo mecanismo verificado (updateOrCreate vía SSH waterfall). (2) Verificación previa de blast radius: el tenant solo tiene 4 automatizaciones plantilla V1 inactivas → activar el motor no dispara nada. (3) Hallazgo: la intención `pedir_menu` (slug `pedir-menu`) **ya existía activa** en el tenant de Samu — prerrequisito cumplido sin cambio. (4) Se creó la intención `pedir_menu` en el tenant de prueba `restaurante-domicilios-v1` (aprobación de Nicolás del turno anterior), replicando la referencia de Friends Chicken (condition_text «el cliente solicita conocer el menú o la carta»). (5) Hallazgo adicional: el agente IA del tenant de Samu («Asistente de domicilios — plantilla», `tool_calling_enabled=1`) está **deshabilitado** (`is_enabled=false`) → el disparador `AiIntentDetected` de la regla de la carta no disparará hasta habilitarlo.
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04.
- **Responsable**: MY SEO (agente LLM del harness); aprobación explícita: Nicolás.
- **Evidencia**: verificación SSH waterfall 2026-09-30: `tenant_messaging_features` de Samu con ambos flags en 1 y `MessagingFeatureFlags::enabled` = `editor_v2=1 engine_v2_execute=1`; `ai_intents` de Samu con `pedir_menu`/`pedir-menu` activa (preexistente); `ai_intents` del tenant de prueba con la intención creada (`pedir_menu`/`pedir-menu`, activa); `ai_agents` de Samu: 1 agente conversacional con `tool_calling_enabled=1` e `is_enabled=false`.
- **Notas**: habilitar el agente IA de Samu queda como decisión coordinada: al habilitarlo empieza a responder conversaciones reales de las líneas asignadas. Hacerlo únicamente en la ventana de pruebas con teléfonos controlados, no antes. El demo puede construirse y dejar las reglas inactivas mientras tanto.

### 2026-09-30 — Demo del piloto en el tenant real: regla `enviar_carta` creada, carta en CDN, primer test end-to-end y prompt de producción

- **Qué se hizo**: (1) Nicolás creó por UI la regla V2 `enviar_carta` en el tenant de Samu: disparador `ai_intent_detected` → intención `pedir_menu`, activa; acción `send_sequence` con 1 paso imagen+caption. (2) Se subió la carta de San Jorge (`carta-san-jorge-2026-09-30.png`) al CDN público de AriCRM (`s3_public`): `https://aricdn.sfo3.digitaloceanspaces.com/tenants/01a0ac93-dc1c-73e6-b872-b2c572070661/carta-san-jorge-2026-09-30.png` (HTTP 200 verificado). (3) Se corrigió el `media_url` del paso: quedó guardado desde la UI como path de storage (`tenants/.../message-templates/...png`), que Evolution no puede descargar; se reemplazó por la URL del CDN. (4) Primer test end-to-end (conversación `01a0f308-a895-7241-8126-4b2b1ca114e3`, teléfono controlado): la intención se detectó, la regla corrió (`automation_runs` status success) y la secuencia envió el mensaje — pero con el media_url aún roto (el envió ocurrió 15:57:28 UTC, antes de la corrección) → la imagen no llegó. El agente IA contestó además con texto que incluía `![Carta San Jorge](vertical-restaurantes/...)` en markdown: su prompt era `prompt-adrian-v1.md` pegado completo (línea equivocada + encabezado interno con la ruta del archivo + instrucción «envía la imagen de la carta», imposible para un agente de texto). En un segundo mensaje de prueba el agente no reportó la intención y contestó directo → la secuencia no volvió a disparar. (5) Se reemplazó el prompt del agente por la versión limpia de producción de San Jorge (`prompt-san-jorge-prod-v1.md`: sin encabezado de documento, sin rutas, carta delegada al sistema, sin pasos de stickers) — verificado en producción (8.585 chars, sin `# Prompt`, sin `vertical-restaurantes`, con cláusula «No puedes enviar imágenes»). (6) Confirmación de línea: 313 492 9669 se muestra en WhatsApp como «~Arepas Rellenas Samu San Jorge» → es la línea de San Jorge (etiqueta «Principal» en el tenant, conectada, Evolution; el agente está asignado a ella).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04 (demo en el tenant real del piloto).
- **Responsable**: MY SEO (agente LLM del harness); regla y agente creados/habilitados por Nicolás en la UI.
- **Evidencia**: `automation_runs` (status success, 15:57:25 UTC) y `ai_intent_detections` en el tenant de Samu; mensajes de la conversación de prueba (`media_url` roto en el envío de 15:57:28); carta en CDN (HTTP 200); prompt verificado en el agente; `prompt-san-jorge-prod-v1.md` en este repo.
- **Notas**: pendiente del demo: re-test limpio con el `media_url` corregido (mensaje desde teléfono controlado pidiendo la carta → debe llegar la imagen del CDN). El doble mensaje (respuesta del agente + secuencia) es inherente al disparo por intención (la supresión `suppresses_ai_reply` solo aplica a disparadores V1 procesados en `HandleInboundMessage`); el prompt limpio minimiza la duplicación. La carta usada es la del repo; falta la versión con el número corregido por Adrián. Formalizar con Adrián la confirmación de la línea San Jorge.

### 2026-09-30 — Re-test exitoso: la secuencia entrega la carta como imagen (demo del piloto operativo)

- **Qué se hizo**: re-test end-to-end del flujo con el `media_url` corregido y el prompt de producción limpio, desde teléfono controlado (conversación nueva `01a0f314-768f-7128-927a-0811854b2303`): mensaje «me pasas la carta por favor?» (16:09:56 UTC) → detección de la intención `pedir_menu` (16:10:16) → run de `enviar_cart`a status success (16:10:16) → mensaje automatizado `media=image` con la URL del CDN, status **delivered** (16:10:16) → respuesta del agente limpia, sin markdown ni rutas, delegando la carta al sistema («Te acabo de enviar la carta, ya debe estar en tu WhatsApp 📜…», 16:10:20).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. El demo del piloto (detección semántica → secuencia con carta) queda operativo en el tenant real de Samu, línea San Jorge.
- **Responsable**: MY SEO (agente LLM del harness); prueba ejecutada por Nicolás desde teléfono controlado.
- **Evidencia**: `ai_intent_detections` y `automation_runs` (status success) del tenant de Samu en producción, conversación `01a0f314-768f-7128-927a-0811854b2303`; mensaje automatizado con `media_url` = CDN de la carta, status delivered; captura del chat en poder de Nicolás (teléfono controlado).
- **Notas**: pendientes para cerrar el piloto: regla de bienvenida (`NewConversation` → `Enviar secuencia` con carta — hoy la bienvenida la hace el agente por prompt), validación del copy con Adrián, carta con número corregido (Adrián), formalización de la línea San Jorge con Adrián, y archivo de evidencias en `evidencias/arepas-rellenas-samu/vertical-restaurantes/secuencias/`. El agente queda habilitado en producción en la línea San Jorge: revisar con Adrián la ventana de operación asistida.

### 2026-09-30 — Root cause de la imagen no renderizable: `mimetype:"false"` en el imageMessage (tarea P-009 en velo_wa)

- **Qué se hizo**: diagnóstico a fondo del porqué la secuencia entregaba (`status=delivered`, ACK de WhatsApp) pero la imagen no se veía en el teléfono. (1) La DB de Evolution (Postgres en hetzner, tabla `Message`) mostró el `imageMessage` enviado con `"mimetype": "false"` — WhatsApp no puede renderizar un medio sin tipo válido. (2) Se corrigió el `content-type` del objeto en el CDN (`image/png` vía putObject explícito) y se re-disparó el paso de la secuencia: **siguió produciendo `mimetype:"false"`** → Evolution NO infiere el tipo desde la descarga. (3) Prueba con el mismo endpoint y cliente del app pasando `mimetype: image/png` + `fileName: carta.png`: Evolution produjo `imageMessage` con `mimetype: image/png` y la imagen llegó al teléfono controlado → confirmado que el request necesita mime/filename reales. (4) Comparación con envíos que funcionan (otros tenants, composer): llevan mimetype real porque el medio fue subido al sistema; la secuencia en cambio solo guarda `media_url` → el mensaje queda con `media_mime_type`/`media_filename` null → el adapter rellena `application/octet-stream` + `archivo` (sin extensión) → Evolution no resuelve el tipo.
- **Obligación asociada**: 4 y 5 — bloquea el criterio «imagen de la carta visible» del piloto; tarea de código P-009 registrada en `TASKS.md` global.
- **Responsable**: MY SEO (agente LLM del harness) — diagnóstico; fix de código: pendiente en `velo_wa` (este harness no edita ese repo).
- **Evidencia**: DB Evolution (hetzner): `imageMessage` de la secuencia con `mimetype:"false"` (16:10:35 y 16:21:58 UTC) vs prueba con mime/filename correctos `mimetype:"image/png"` (16:23:33 UTC, entregada y renderizada en teléfono controlado); envíos de referencia de otros tenants con `image/jpeg`; código: `SendAutomationSequenceStep` (no fija mime/filename), `LegacyWhatsAppAdapter`/`WhatsAppClientService::sendMedia` (fallbacks `application/octet-stream`/`archivo`).
- **Notas**: la carta en CDN y todo el flujo (intención → regla → secuencia → envío) funcionan; el único eslabón roto es el mimetype del medio en envíos de secuencia por URL. El fix en `velo_wa` es pequeño (inferir mime/filename de la extensión del `media_url`). Mientras tanto, el envío de la carta queda verificado por la prueba directa (imagen renderizada). El estado `delivered` del app no garantiza renderización del medio — tenerlo en cuenta para futuras verificaciones.
