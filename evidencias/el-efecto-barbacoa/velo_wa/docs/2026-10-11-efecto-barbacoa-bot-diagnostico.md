# Incidente — Bot IA de El Efecto Barbacoa: calidad insuficiente y apagado a pedido del cliente

## STATUS: BOT OFF (deliberado) — diagnóstico cerrado 2026-10-11, plan pendiente de ejecutar

- **Qué pasó**: el agente IA de domicilios corrió en producción ~12 días (29-sep → 10-oct) sin conocimiento del territorio (0 sedes, 0 zonas, 0 tarifas cargadas), deflexionando en la pregunta más frecuente de un restaurante de domicilios ("¿cuánto vale el envío a mi barrio?"), respondiendo por encima del operador humano y prometiendo reservas que no quedaban registradas en ningún sistema.
- **Trigger**: 2026-10-10 17:17 COT (22:17 UTC) — conversación de Luna Velandia (barrio La Carolita): el bot intercaló dos deflexiones entre los mensajes manuales de Juan mientras la clienta miraba. La clienta: *"enreda un poquito"*; Juan: *"es una prueba de IA que están haciendo, pero no me ayuda mucho"* (textual en el chat).
- **Acción**: nicolas deshabilitó el agente el 2026-10-11 01:58:52 UTC (20:58 COT) a pedido de Juan (chat WhatsApp 20:57–21:00 COT). Reunión con el cliente: **martes 13-oct-2026** ("Lo miramos el martes").
- **Urgente al momento del diagnóstico**: reserva de cumpleaños de Cristian González (conv `01a12907-afe9`) para el **domingo 11-oct 19:00 COT, 5 personas, SIN confirmar** — Cristian no respondió al pedido de abono de decoración que Juan envió 57 min después. Sin registro en `reservations`. Seguir esta mañana y confirmar aunque sea sin decoración.
- **Urgente 2 (detectado en revisión)**: reserva fantasma del **15-oct 20:00, 10 personas** (conv `01a1082f`, prometida por el bot el 4-oct 18:34 UTC sin fila en `reservations`). Verificar con Juan si ese grupo tiene mesa (el prompt fija límite habitual 19:00 los fines de semana).
- **Revisión adversarial** (Codex, 2026-10-11, solo lectura; código local = release activa = commit `d0ee6c6`): 5/5 causas confirmadas (dos con matiz), una sub-afirmación REFUTADA (las tools de reservas SÍ existen — §4) y hallazgos nuevos que corrigen el plan → ver «Hallazgos de la revisión».
- **Ronda 2 (Claude, 2026-10-11)**: **bug de plataforma, no solo del tenant** — el merge LID/PN descarta el takeover humano (mecanismo central, §3 y «Ronda 2»). El flag inferido quedó PROBADO con activity_log (corrigiendo a Codex), y la deflexión de La Carolita resultó **conforme al prompt** (JSON con «Carola», sin «Carolita», y regla que prohíbe inferir abreviaturas).

---

## Contexto e IDs

- Tenant: **EL EFECTO BARBACOA SAS**, id `01a0ac43-8975-70be-aece-616ac37c2bb4`, owner Juan Guillermo Barrera Ospina (`01a0ac43-8b1e-734e-a625-f1c19e99a3f7`).
- Línea WhatsApp: `01a0ac4c-e490-705d-8014-24f5c452f01d` ("Principal", instancia Evolution `line_01a0ac4ce490`, webhook vía gateway).
- Agente IA: `01a0ef1e-a4fb-7300-adaf-4ae6f921c2b8` "Asistente de domicilios — plantilla", gpt-4o-mini, `is_enabled=false` desde 2026-10-11 01:58:52 UTC, `tool_calling_enabled=true`, prompt v1 genérico (derivado de Botanazo sanitizado, ~16.7k chars) sin datos verificados de Barbacoa. Sin KB vinculada. Sin pilot mode.
- Referente útil: Friends Chicken (tenant `01a0a5a4-1cda-7099-bfe7-c993e6f1352b`) usa el mismo template con tools (`get_catalog`, `get_delivery_fee`, sedes) YA CONFIGURADAS y evolucionó a prompt v3/v4. La infra de tools existe; lo que falta en Efecto son los **datos**.

## Causas raíz (verificadas con código, DB y logs)

### 1. El tenant no tiene datos cargados → la tool de tarifas siempre falla

- `branches` del tenant: **0 filas** (verificado 2026-10-11). `reservations`: **0 en toda su historia**. `orders`: **0 en toda su historia**.
- Log del incidente (`storage/logs/laravel.log`, 2026-10-10 22:18:32–35 UTC): el bot llamó `get_delivery_fee` **4 veces seguidas**, todas `INVALID_BRANCH` ("La sede indicada no es un id válido. Consulta get_catalog…"). Nunca llamó `get_catalog` pese a que el error se lo indicaba. Segunda ronda igual a las 22:19:49.
- Resultado: deflexión "Lamentablemente, no puedo verificar el valor del domicilio… habla directamente con el equipo de atención" — dos veces, frente al cliente. La tarifa real (Carolita $6.000) la dio Juan de memoria.
- **Matiz (Codex)**: el prompt v1 SÍ contiene un JSON de tarifas con «Carola»: $6.000 y «Laureles»: $5.000 — el bot tenía la respuesta correcta en su propio prompt y aun así prefirió la tool (4 fallos) y deflexionó. El problema de fondo es la **coexistencia de dos fuentes incompatibles** (JSON del prompt vs `branches` vacía) y que el modelo no resolvió Carolita→Carola ni llamó `get_catalog`. «Laureles $5.000» del warmup proviene de ese JSON; no está validado contra el negocio.
- **Matiz (Claude, ronda 2) — la deflexión fue CONFORME al prompt**: el prompt v1 menciona `branch_id`, `get_catalog` y `get_delivery_fee` **cero veces**; las tools llegan al modelo solo por esquema, sin precedencia. Las líneas 39-40 y 121 hacen del JSON la «fuente obligatoria» y **prohíben inferir abreviaturas** → con «Carolita» ausente del JSON, escalar era lo que el prompt mandaba. Además: línea 290 (usar la tool) contradice línea 300 («no confirmes, se registra manualmente»), y la línea 315 pide esperar una herramienta de reanudación **que no existe**. La fix es datos+alias+coherencia del prompt, no solo disciplina del modelo.

### 2. El bot responde aunque el humano ya esté escribiendo (bypass por diseño)

- Toda conversación nueva nace con `ai_agent_enabled=true` cuando el agente está habilitado: `app/Jobs/HandleInboundMessage.php:186`.
- En `shouldRespond()` (`app/Services/AiAgentService.php:191`) el early-return del flag `true` (línea 210) ocurre **ANTES** del check `conversationHasHumanOutbound` (línea 218) → con el flag en true, el bot habla sin importar que el operador haya escrito.
- Verificado en la 2ª deflexión (22:19:51 UTC): los 3 mensajes manuales de Juan ya estaban en la conversación y el bot respondió igual.
- **Cerrado (Claude, ronda 2)**: el valor `true` a las 22:19:48 quedó **probado** con `activity_log`: null→true a las 22:17:04 y true→false (`human_phone_takeover`) a las 22:20:46 — era `true` cuando respondió. **Corrige a Codex**: el `false` actual viene del takeover de las 22:20:46, no del outbound «CON GUSTO» de la 01:15. Rutas que escriben `true`: `HandleInboundMessage:186`, `WebchatService:52`, `ConversationController:315`, `ContactController:322`, `AutomationV2Engine:542` (las automatizaciones de Efecto están inactivas, 0 runs). Escriben `false`: el takeover, `abortLoop` (`AiAgentService:1856`), `pauseLine`, `disableConversationBot`. `MessageTemplateSender:43` solo lee (bloquea envíos con 409). Barrido del tenant: 42 de 63 mensajes del bot llegaron tras un outbound humano en 16 conversaciones; en 12 el «humano» era solo el greeting; humano real en 4 casos (`0ef32` prueba 29-sep, `1047c`, `1285f`, `127e4`).
- **Nota de alcance (Claude)**: con un humano real escribiendo en la MISMA conversación, el takeover funciona (Friends Chicken: 53 mensajes del bot tras outbound humano en 31 conversaciones, todos greeting, 0 con humano real). El bypass de la línea 210 casi nunca decide solo — quien rompe la señal sistemáticamente es el merge (§3).

### 3. Race + conversaciones gemelas LID/PN en la 1ª respuesta

- La 1ª deflexión (22:18:36 UTC) se decidió en el flush del buffer (~22:18:30, `buffer_until`) antes de que el mensaje de Juan aterrizara; además los mensajes del teléfono cayeron en la **conversación gemela por LID** (`01a127e4-39f5`), que se fusionó con la principal (`01a127e4-220a`) recién a las 22:19:06 (`lid_pn.contact_merged`, 4 mensajes transferidos).
- `FlushAiAgentBufferedReply` re-valida `shouldRespond` y `hasHumanReplyAfterTrigger` al inicio (`app/Jobs/FlushAiAgentBufferedReply.php:90,131`) pero **no re-valida justo antes del envío** tras la generación (~6 s con 4 tool calls). El envío se programa tras generar en `app/Services/AiAgentService.php:431` sin re-comprobar humano — ahí va el re-check atómico.
- **Reencuadre (Claude, ronda 2) — este es el mecanismo central, no un accidente del caso**: cada cliente nuevo que llega por LID genera dos conversaciones. El lado LID recibe el inbound y vive el bot (flag `true`); el lado PN recibe el greeting del teléfono y los mensajes manuales de Juan, donde el takeover SÍ se dispara (`human_phone_takeover`). Al fusionarse (~2 min), `MergeConversations` conserva la conversación más antigua y **descarta el estado de la otra**: en 9 de 10 merges del 5-11 oct el sobreviviente quedó `true` mientras el gemelo tenía el takeover registrado (`contact_merge_audits`; 36 merges en el tenant). En 3 merges (`1036e`, `10460`, `1047c`) pasó lo inverso: el sobreviviente quedó `false` y el bot respondió desde la gemela. En Carolita, los «4 mensajes transferidos» eran el greeting + los 3 mensajes de Juan.
- **Veredicto plataforma (B4)**: Friends Chicken (mismo template, bot activo) muestra el mismo patrón LID (8 contactos provisionales, 6 merges el 9-11 oct). El fallo afecta a cualquier tenant con línea telefónica + bot: el merge borra la señal de takeover. Las specs lid-pn y el reporte del 24-sep NO mencionan `ai_agent_enabled` ni el takeover (hueco no conocido, B6).

### 4. Promesas sin respaldo operativo (alucinaciones de confirmación)

- 2026-10-04 18:34:31 UTC, conv `01a1082f` (Nicol Correa): «ha sido registrada» una reserva de 10 personas para el 15-oct 20:00 — sin fila en `reservations`. El patrón venía de antes del caso Sergio.
- 2026-10-10 15:11:55 UTC, conv `01a12650` (Sergio Cuadrado): el bot dijo *"tu reserva queda registrada"* — `reservations` está vacía. Ninguna reserva del bot quedó en el libro en 12 días.
- 2026-10-09 14:23:26 UTC, conv `01a12105` (Xime): el bot rechazó una reserva con *"no podemos realizar reservas para hoy, ya que es festivo"* — **invención confirmada (Codex)**: el tenant tiene `respect_holidays=false` y `holiday_hours=null`, `HolidayService` devuelve null para el 9-oct y no hay llamada `is_holiday` en el log. El humano, además, ofreció reservar a las 14:38 contradiciendo el rechazo operativo.
- **CORRECCIÓN (Codex) — las tools SÍ existen**: el registro ofrece `create_appointment` (escribe en `reservations`) y `create_order`; el agente tiene `tool_calling_enabled=true` y ninguna exclusión en `enabled_tools`. El modelo **no las llamó** antes de afirmar «registrada», y el prompt ya prohíbe confirmar reservas: lo incumplió dos veces. No es falta de tools; es conducta del modelo que hay que rediseñar (confirmar solo con registro real vía tool, o escalar a humano).

### 5. Doble saludo en cada conversación nueva

- El WhatsApp Business del teléfono del negocio manda un greeting automático ~4 s después del primer inbound (llega como outbound humano). El bot saludaba encima con su welcome completo — incluso a un "." (su último mensaje, 2026-10-11 00:32:02 UTC, conv `01a1285f`).
- Nota: en el camino normal (flag null), ese greeting humano haría `conversationHasHumanOutbound` → true y el bot NO respondería nunca. El bot solo respondía por el bypass del punto 2 y/o por el split LID/PN del punto 3. La coexistencia teléfono-humano + bot no está diseñada.

## Hallazgos de la revisión adversarial (Codex, 2026-10-11)

- **Decoración descrita de más**: el bot (10-oct 18:09:25 UTC) enumeró manteles, velas, globos y centros de mesa; el negocio (18:16:28) describe otra oferta: ramillete de globos con burbuja, postre y vela volcán. Contenido comercial inventado.
- **Deflexión de menú del día ya visible el 5-oct** (conv `01a10d05`): bot remitió al PDF general (17:03:58), admitió no disponer del menú del día (17:05:14) y «prometió escalar» (17:23:27); el humano entregó el menú a las 18:00:42. El bot necesita contenido diario o traspaso verificable, no solo tarifas.
- **Precios de postres citados el 10-oct** (conv `01a126af`) siguen sin cotejar contra menú vigente — no darlos por validados.
- **Doble saludo confirmado en 3 conversaciones**: `01a126af` (16:39:40 → 16:40:05), `01a10460` (00:47:00 → 00:47:21), `01a1285f` (00:31:44 → 00:32:02). El origen exacto del primer saludo no es acreditable desde AriCRM (llega como outbound no automatizado; compatible con el greeting de WhatsApp Business del teléfono).
- **Riesgo crítico del re-encendido**: al apagar, las conversaciones abiertas con flag `true` pasaron a `false`, pero quedaron **3 conversaciones `pending` con `ai_agent_enabled=true` y sin outbound humano**: `01a101cd` (Christian Rios), `01a0fde8` (contacto "?"), `01a0fd97` (Andrey Duque). Al reactivar globalmente, un inbound nuevo en cualquiera de ellas reanudaría el bot. Y con el switch global APAGADO, en conversaciones nuevas el flag nace `null` y el greeting del teléfono silencia al bot **incluso para contactos pilot** (el check de humano en `shouldRespond` línea 218 va antes de la excepción pilot línea 230).

## Ronda 2 (Claude, 2026-10-11) — hallazgos y correcciones

- **N1 — El merge descarta el takeover humano** (mecanismo central, §3). Refuta el plan anterior: «distinguir el greeting» NO basta; hay que **propagar el takeover al sobreviviente del merge** y resolver N2.
- **N2 — Decisión de producto para el martes**: arreglar solo N1 dejaría al bot mudo para todo cliente LID nuevo (el greeting cuenta como takeover). O se apaga el greeting del teléfono, o se discrimina. Hoy NO hay marcador en `messages` que lo distinga (`wa_message_id` mismo formato, `sent_by`/`channel_metadata` null — B5); heurística posible: primer outbound, ≤~20 s tras el primer inbound, texto igual al greeting configurado. Falta revisar el payload crudo de Evolution.
- **N3 — `disableConversationBot` (`AiAgentController:214`) solo toca conversaciones `open`**: por eso las 3 `pending` quedaron en `true`, y volverá a pasar. `pauseLine` sí incluye pending.
- **N4 — El takeover exige `created_at >= now()-5 min`**: un webhook retrasado o un backfill de un mensaje humano no pausa al bot aunque el mensaje quede registrado.
- **N5 — Handoffs que nadie consume**: el 7-oct (`01a117e0`) el bot hizo handoff de un cliente que estaba en el restaurante, sin avisar; Juan llegó 59 min después («el que responde es una ia»). El handoff hoy no pausa el bot (fix del 7-oct) ni notifica: queda una fila en `handoffs` — pendiente en Efecto, 5 sin atender en Friends. Antes de pilot: notificación mínima al equipo.
- **N6 — Más deflexiones de menú del día**: 7-oct (`01a11724`, el humano respondió 14 min después). El 5-oct el bot además asumió «frustración» inexistente y prometió escalar.
- **N7 — Contradicción de horarios**: el prompt dice reservas hasta 19:30 entre semana / 19:00 fin de semana; la plantilla humana dice «de 8am a 8pm». La reserva fantasma del 15-oct 20:00 cae justo en esa contradicción → aclarar con Juan cuál rige.
- **N8 — Los logs de las releases rotan**: fechas anteriores al 9-oct solo reconstruibles por DB (`activity_log`, `contact_merge_audits`). Copiar la evidencia ya recopilada.

### Daño colateral observado

- 2026-10-10 19:31 COT: Juan, saturado gestionando a mano el domicilio de las 8pm, envió por error la dirección de Luna a otro chat (conv `01a1285f`) — el bot sumó carga en la hora pico en vez de quitarla.
- Conv `01a0ad09`: 5 inbound multimedia sin respuesta tras el apagado.
- Con el bot OFF, los clientes nocturnos solo reciben el greeting del teléfono con respuesta humana ~1 h después (Cristian: 57 min).

## Línea de tiempo (UTC)

- 2026-09-29 21:42 — onboarding: agente + automatizaciones plantilla creadas.
- 2026-09-29 22:08 — habilitado y probado (flujo de reserva de prueba OK; citó "domicilio a Laureles $5.000" — dato de referencia del prompt genérico, no verificado para este tenant).
- 29-sep → 10-oct — bot vivo, ~9-11 msgs/día en días pico. Aciertos reales: precios de postres, ingredientes de pizzas, contenido de decoración.
- 2026-10-10 22:17–23:32 — incidente La Carolita (conv `01a127e4`), ver arriba. Venta ($140.000) cerrada por Juan a mano.
- 2026-10-11 00:32:02 — último mensaje del bot (welcome a un ".").
- 2026-10-11 01:58:52 — nicolas deshabilita el agente.
- 2026-10-11 03:35–04:33 — Cristian pide reserva para ese mismo día 19:00 COT; Juan responde a las 04:32 pidiendo abono de decoración; Cristian sin responder → **sin confirmar**.

## Plan de acción

### Hoy (operativo, humano)
1. Follow-up de la reserva de Cristian (conv `01a12907-afe9`) y confirmar la mesa.
2. Revisar los 5 multimedia sin responder (conv `01a0ad09`) — baja prioridad.
3. Acordar con Juan la cobertura nocturna mientras el bot está apagado.

### Antes de re-habilitar (orden de trabajo)
1. **Cargar datos reales del tenant y definir UNA sola fuente de verdad de tarifas** (hoy coexisten el JSON del prompt y `branches` vacía — el bot puede contradecirse a sí mismo): sedes con zonas y tarifas (incluida la correspondencia Carola/Carolita acordada con Juan), menú y menú del día, horarios, decoración real, política de reservas/abono. Vía `branches`/tools o KB.
2. **Arreglar convivencia bot-humano** (SPECBOOT + tests; **rediseñado tras ronda 2**). Mover sin más el check de humano antes del early-return de `ai_agent_enabled=true` (`AiAgentService.php:210`) rompe la activación manual por conversación (`ConversationController.php:297`) — y distinguir el greeting NO basta (N1). Diseño: (a) **propagar el takeover al sobreviviente del merge** (la fix central); (b) resolver N2 (apagar el greeting del teléfono o discriminarlo — sin marcador hoy, heurística B5); (c) re-check atómico justo antes de crear/despachar el mensaje (`AiAgentService.php:431` despacha sin re-comprobar) — necesario pero NO suficiente: no cubre la race del merge porque el humano está en OTRA conversación; (d) la semántica «desde el último habilitado explícito» requiere columna `ai_enabled_at` que hoy no existe (solo activity_log); (e) cerrar el hueco N4 (ventana de 5 min del takeover ante webhooks retrasados/backfill). El panel ya es seguro: con flag true el envío devuelve 409 (`MessageController:303`); el único canal sin control es el teléfono.
3. **Doble saludo**: apagar el greeting del WhatsApp Business del teléfono, o suprimir el welcome del bot si ya hubo greeting.
4. **Rediseñar la confirmación de reservas**: las tools `create_appointment`/`create_order` SÍ existen y el prompt ya prohíbe confirmar sin registro (incumplido 2×: 4-oct y 10-oct). Regla dura: el bot solo confirma si llamó la tool y obtuvo registro real; si no, responde «te confirmamos en un momento» y marca `needs_human_review`.
5. **Prompt v2 tenant-específico**, versionado según regla del repo: `docs/<tenant>/prompts/<agente>/vN-<desc>.md` con SHA-256, autor y fecha.
6. **Pilot = switch global APAGADO + whitelist**. La whitelist es la excepción que deja pasar contactos de prueba cuando el agente está globalmente apagado; NO es un filtro de producción — re-encender `is_enabled=true` de inmediato expone a clientes normales. Antes de cualquier prueba: auditar/limpiar las 3 conversaciones `pending` con flag `true` (`01a101cd`, `01a0fde8`, `01a0fd97`) **con el toggle (`ConversationController:315`), no con SQL**, para dejar rastro en activity_log (y arreglar N3: `disableConversationBot` ignora `pending`). Ojo: en conversaciones de prueba nuevas, el greeting del teléfono silencia al bot incluso para contactos pilot (flag null + check de humano antes de la excepción pilot) → habilitar el flag por conversación o apagar el greeting. Agujeros detectados (ronda 2): el match de la whitelist usa `contact->phone` y un contacto provisional LID puede no tener teléfono hasta el merge (~2 min) — verificar antes de probar; y el pilot no valida el caso peligroso (humano real escribiendo con la conversación dividida) salvo que se simule a propósito → incluirlo en los criterios de aceptación. Validar: tarifa de Carolita, silencio ante mensajes humanos, cero promesas de registro. Luego producción gradual.
7. **Notificación mínima del handoff** (N5): hoy el handoff deja solo una fila que nadie consume (1 pendiente en Efecto, 5 en Friends). Sin esto, el bot «entrega» al humano y el humano no se entera.

### Comunicación con el cliente (martes 13-oct) — guion afinado (ronda 2)
- **Abrir con**: la reserva de Cristian resuelta y la del 15-oct (Nicol Correa) verificada con Juan.
- **Mostrar**: la línea de tiempo de La Carolita con DOS causas concretas y comprensibles: (1) «Carolita» no estaba cargada (el sistema tenía «Carola» y tiene prohibido adivinar abreviaturas); (2) el sistema perdió la señal de que Juan ya estaba escribiendo (el merge de conversaciones la borró).
- **Prometer**: nada se reactiva sin su aprobación; primero una prueba cerrada con teléfonos de prueba; el bot no confirmará reservas ni dará datos sin fuente.
- **NO prometer**: fecha de reactivación, cero errores, ni cobertura nocturna (el handoff hoy no avisa a nadie — N5).
- **Preguntarle (decisiones de producto)**: ¿apagamos el greeting automático del teléfono? (N2) · ¿hasta qué hora se reserva de verdad — 19:00/19:30 del prompt o 8pm de la plantilla? (N7) · correspondencia de barrios/alias y tarifas para el prompt v2.

## Reglas para el siguiente agente

- **NO re-habilitar el agente ni escribir a clientes sin GO explícito de nicolas.**
- Producción: `ssh waterfall`, artisan desde la release activa (`ls -lt /home/forge/app.aricrm.co/releases/ | head -3`). Solo lecturas salvo GO.
- Mensajes del bot: tabla `messages`, `is_automated=true`, `direction` in/out (`ai_agent_id` viene NULL en el camino normal de IA — no es señal de "no fue el bot").
- Logs: `storage/logs/laravel.log` de la release — buscar `01a0ac43-8975` + `ai_safety` / `AiAgent tool`.

## Verificaciones realizadas (2026-10-11: nicolas + ZCode; revisiones adversariales Codex y Claude)

- Conversaciones, mensajes, flags `ai_agent_enabled` y timestamps: dumps por tinker (evidencia arriba).
- Logs `reply_buffered` / `token_consumed` / `AiAgent tool` / `human_touch_recorded` / `lid_pn.*` de las ventanas críticas.
- Código: `AiAgentService::shouldRespond()` (líneas 191–244), `FlushAiAgentBufferedReply` (líneas 90–136), `HandleInboundMessage:186`.
- Conteos DB: `branches`=0, `reservations`=0, `orders`=0 (histórico del tenant).

- Conteos DB: `branches`=0, `reservations`=0, `orders`=0 (histórico del tenant).
- Revisión ronda 2 (Claude, solo lectura): mecanismo del merge LID/PN sobre `contact_merge_audits` y `activity_log` (logs pre-9-oct rotados, N8), barrido 4-8 oct, veredicto plataforma con Friends Chicken, prompt v1 línea a línea. Correcciones integradas en §§1-3, plan y guion del martes.

### Pendiente de verificar
- ~~Config de festivos del tenant~~ RESUELTO (Codex): `respect_holidays=false`, `HolidayService` null para 9-oct → invención del modelo.
- ~~Fuente de "domicilio a Laureles $5.000" del warmup~~ RESUELTO (Codex): proviene del JSON de tarifas del prompt v1; falta validar contra el negocio.
- ~~Valor del flag a las 22:19:48~~ RESUELTO (Claude): `true` probado por `activity_log` (corrección en §2).
- ~~Más «registrada/agendada» en el histórico~~ RESUELTO (Claude): solo las 2 documentadas; `reservations` sigue en 0.
- Precios de postres citados por el bot el 10-oct (conv `01a126af`) contra el menú real.
- **Reserva fantasma del 15-oct 20:00, 10 personas (conv `01a1082f`)**: ¿el grupo tiene mesa? Verificar con Juan antes del 15-oct (cae en la contradicción de horarios N7).
- Las 3 conversaciones `pending` con `ai_agent_enabled=true` (`01a101cd` Christian Rios, `01a0fde8` "?", `01a0fd97` Andrey Duque): limpiar con el toggle antes de cualquier re-encendido (no SQL).
- Contraejemplo limpio de flag `true` + bot callado ante humano real: no encontrado (las 3 pending están calladas solo por falta de inbound) — único extremo suelto de la causa 2.
- Verificar antes del pilot (inferencia de código): el match de la whitelist con contactos LID provisionales sin `phone`.
- Revisar el payload crudo de Evolution del greeting: ¿trae algún campo que lo distinga? (B5).
- Copiar la evidencia de logs que rotan (N8): antes del 9-oct ya solo queda lo reconstruible por DB.
