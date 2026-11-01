# SPEC — Recuperación controlada de El Efecto Barbacoa

**Estado:** propuesta para revisión; no autoriza cambios en producción ni reactivación del agente.  
**Fecha:** 2026-10-11  
**Tenant:** `01a0ac43-8975-70be-aece-616ac37c2bb4`  
**Agente:** `01a0ef1e-a4fb-7300-adaf-4ae6f921c2b8`  
**Línea principal:** `01a0ac4c-e490-705d-8014-24f5c452f01d`  
**Responsable de aprobar una nueva prueba con clientes:** Nicolás, tras acordar el alcance con Juan Guillermo.

## Registro de ejecución

**2026-10-11 — Fase B, carga de sede y tarifas autorizada por Nicolás**

- Se creó la sede activa `Principal` (`01a12a56-a47f-71bc-bf53-44e1a2a84a08`) asociada a la línea principal `01a0ac4c-e490-705d-8014-24f5c452f01d`.
- Se insertaron, en una sola transacción, 144 tarifas activas de la fuente JSON con SHA-256 `3937a0dd4f495abe42d4603a27bd4bd2ce2bda619bf3a2b267243cfe75ec58a2`. No existían sedes ni tarifas previas para el tenant.
- Verificación posterior en producción: `get_catalog` devuelve la sede y su UUID; `get_delivery_fee` devuelve Carola $6.000 y Laureles $5.000. Carolita y una zona inexistente devuelven `ZONE_NOT_COVERED`; no se creó alias porque aún requiere confirmación del establecimiento.
- El agente quedó y sigue con `is_enabled=false`; no se enviaron mensajes ni se modificaron conversaciones, pedidos, reservas o aliases.

## 1. Objetivo y límite de seguridad

Configurar una sede real del restaurante y sus tarifas de domicilio en AriCRM, corregir los fallos que hicieron que el bot se intercalara con el equipo y prometiera acciones no registradas, y preparar una prueba limitada que Juan pueda evaluar. El resultado inicial es un sistema **preparado y verificado, con el bot apagado**. Crear la sede o cargar tarifas no cambia `ai_agents.is_enabled`.

La solicitud de apagado del 10-oct-2026 sigue vigente. El mensaje posterior de Juan, «Listo Nicolás muchas gracias», no distingue claramente entre acuse del apagado y aceptación de conversar el martes; no se debe presentar la reunión como confirmada. Antes de fijar el alcance final, Nicolás debe escuchar qué le preocupó a Juan y confirmar si desea continuar con una prueba. Ningún paso de este SPEC permite escribirle a clientes, reencender el agente, activar tools de escritura o modificar producción sin la autorización correspondiente.

## 2. Evidencia de partida

| Hecho | Evidencia |
| --- | --- |
| Agente apagado desde 2026-10-11 01:58:52 UTC; `branches=0`, `reservations=0`, `orders=0` para el tenant | Consulta de solo lectura en Waterfall, 2026-10-11; `docs/incidents/2026-10-11-efecto-barbacoa-bot-diagnostico.md` |
| Cuatro llamadas a `get_delivery_fee` en La Carolita, 2026-10-10 22:18:32–35 UTC, con `INVALID_BRANCH`; otra a 22:19:49 | `storage/logs/laravel.log` de la release activa; conversación `01a127e4-220a-73d6-b3ca-8183fb731389` |
| El fallo inmediato fue un `branch_id` no válido. La tool exige un UUID real y `get_catalog` puede devolver el ID de sedes activas | `app/Services/AiAgent/Tools/{GetDeliveryFeeTool,GetCatalogTool}.php` |
| El documento del programa contiene 144 tarifas RAPIDOMIS sin duplicados tras normalización; incluye `Carola` $6.000 y `Laureles` $5.000, pero no `Carolita`; `Avanzada` y `Marmato` llevan `SRV. 5PM` | `/Volumes/ExternoMS/projects/ccm-vouchers-2026/evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.json`; SHA-256 `3937a0dd4f495abe42d4603a27bd4bd2ce2bda619bf3a2b267243cfe75ec58a2` |
| El JSON tiene confirmación de Nicolás del 29-sep, pero la vigencia actual, equivalencia Carola/Carolita y condiciones del operador deben revisarse con Juan | `.../tarifas-domicilio-2026-09-29.md`, `clientes/el-efecto-barbacoa/CARACTERIZACION.md` |
| El prompt efectivo en producción contiene tarifas incrustadas y la instrucción de no confirmar reservas; el bot afirmó que algunas estaban registradas sin invocar `create_appointment` | Consulta de solo lectura del `system_prompt` y logs; conversaciones `01a1082f` (4-oct 18:34:31) y `01a12650` (10-oct 15:11:55) |
| Un outbound humano puede entrar por la conversación gemela LID/PN; el flag `ai_agent_enabled=true` evita el chequeo histórico de humano, y no hay revalidación después de generar la respuesta | `HandleInboundMessage`, `AiAgentService`, `FlushAiAgentBufferedReply`; logs del merge 10-oct 22:19:06 |
| El harness del programa deja C-03 pendiente, C-04 en progreso y C-06 pendiente; su prompt v3 está rotulado «no activado» aunque otro prompt sí respondió en producción | `/Volumes/ExternoMS/projects/ccm-vouchers-2026/clientes/el-efecto-barbacoa/TASKS.md`, `.../evidencias/el-efecto-barbacoa/ia-conversacional/prompt-v3.md` |

## 3. Alcance por fases

### Fase A — Fuente validada y preparación sin exposición a clientes

1. Preparar una hoja de revisión para Juan con **una fila por cada una de las 144 zonas** del JSON, valor, condición, fuente y decisión: aprobar, corregir o excluir. Confirmar fecha de vigencia, si RAPIDOMIS sigue prestando el servicio y si el valor es el que se comunica al cliente. Registrar explícitamente recargo de datáfono no definido y zonas con condiciones horarias.
2. Confirmar nombre operativo de la sede, si es única, su asociación a la línea principal y la dirección que debe mostrarse al cliente. `CLIENTE.md` registra Cra 23 # 71-15, pero el modelo actual de `branches` **no tiene campo de dirección**; la carga de sede no debe aparentar que la dirección quedó configurada. Tratar su almacenamiento/publicación como decisión separada si hace falta.
3. Resolver con Juan si `Carola` y `Carolita` son la misma zona a $6.000. Solo si lo confirma, crear `Carolita` como alias de `Carola`; nunca usar coincidencia parcial automática. Revisar también nombres que incorporan aclaraciones o abreviaturas, como `Arenillo (Hotel búho)` y `Enea / Z. Ind.`. Las dos filas `SRV. 5PM` quedan **inactivas o excluidas de la cotización automática** hasta que se determine el significado y se soporte la condición en el resolver; no introducirlas como tarifa incondicional.
4. Guardar la versión aprobada de la fuente, autor de la aprobación, fecha y hash. Si Juan no confirma la tabla completa, cargar solo las filas aprobadas y documentar el subconjunto. No tomar el `estado` del JSON como aprobación nueva de Juan.

### Fase B — Sede y tarifas en AriCRM, con bot apagado

1. Verificar en producción, inmediatamente antes de actuar, tenant, línea, sedes, tarifas, aliases, estado del agente y release activo. Tomar un respaldo de las filas del tenant afectadas y un reporte de diferencias contra la fuente aprobada.
2. Crear **una sede activa** del tenant con nombre confirmado y, si corresponde, `whatsapp_line_id` de la línea principal. Usar los mecanismos existentes de Ajustes → Sedes (`BranchController`), sin copiar sedes ni tarifas de otro tenant.
3. Cargar de forma reproducible las zonas aprobadas en `delivery_tariffs` para esa sede y sus aliases aprobados en `delivery_tariff_aliases`. Para el volumen de 144 filas, preparar un importador operativo con validación y `dry-run`, limitado a tenant y sede explícitos, que aplique el lote en transacción, sea idempotente y falle ante colisiones de barrio normalizado o alias. **No** borrar ni sobrescribir silenciosamente filas preexistentes; cada diferencia inesperada requiere revisión. Registrar conteos, hash de entrada, ID de sede, IDs de filas y resultado sin datos de clientes finales.
4. Verificar en solo lectura el conteo esperado de activas, excluidas y aliases, y comparar cada precio con la fuente aprobada. Comprobar `get_catalog` sin `branch_id`, tomar el UUID real devuelto y probar `get_delivery_fee` con ese UUID para `Carola`, `Laureles` y una zona ausente. `Carolita` debe devolver $6.000 **solo si** se aprobó el alias. La zona ausente debe devolver `ZONE_NOT_COVERED`; el ID inventado debe devolver `INVALID_BRANCH`.
5. Mantener el agente apagado durante toda la fase. Un resultado correcto de la tool prueba datos y resolución, no calidad conversacional ni autorización de reencendido.

### Fase C — Convivencia bot/humano y respuestas fiables

1. Corregir el control de propiedad de la conversación. La creación automática con `ai_agent_enabled=true` no debe permitir que el bot responda tras una toma humana. A la vez, se debe conservar la posibilidad existente de **habilitar manualmente el bot de nuevo** por conversación. Definir y persistir el instante/origen de esa habilitación y de la toma humana, para que la precedencia dependa del evento más reciente, no de «existe cualquier outbound humano histórico». Resolver el estado de las dos conversaciones al fusionar LID/PN; si la gemela recibió una respuesta humana, la principal no puede seguir elegible por un flag viejo.
2. Revalidar elegibilidad y ausencia de intervención humana **después de generar** y de nuevo inmediatamente antes del envío externo de cualquier mensaje IA diferido. La comprobación debe usar el estado vigente de DB, tolerar jobs duplicados y no bloquear respuestas humanas. Identificar de forma inequívoca los mensajes generados por IA para este control; hoy `messages.ai_agent_id` puede ser `NULL` en el camino normal. Considerar el saludo automático del WhatsApp Business del teléfono como un caso separado de una respuesta manual, sin reconocerlo mediante comparación frágil de texto.
3. Acordar una sola bienvenida para cada conversación. La opción operativa preferida para el pilot es desactivar el greeting del teléfono **con Juan** y verificarlo en el dispositivo; si no se acepta, diseñar y probar supresión determinista del welcome del bot. No cambiar la configuración de su teléfono por cuenta de MY SEO.
4. Para este agente, configurar un allowlist de tools adecuado a la fase informativa: lecturas verificadas y escalamiento probado. No exponer `create_order` ni `create_appointment` hasta que estén completos catálogo, disponibilidad, confirmación explícita y aceptación operativa. La ausencia de tool en el allowlist no basta: bloquear en la salida afirmaciones de «registrado», «confirmado», total o tarifa cuando no exista resultado autoritativo de la tool/registro correspondiente. Ante duda, solicitar validación humana sin decir que ya fue notificada si no lo fue.
5. Versionar el prompt realmente desplegado como línea base recuperada de producción, con fecha de recuperación y hash. Crear un v2 específico de El Efecto que retire el JSON duplicado de tarifas si la DB pasa a ser fuente canónica, indique `get_catalog` → UUID real → `get_delivery_fee`, prohíba reservar por afirmación y no invente festivos, decoración, disponibilidad ni menú diario. Conservar snapshots anteriores. Corregir en el harness la nota que confunde el borrador v3 con la versión que efectivamente respondió en producción.

### Fase D — Pilot y decisión del cliente

1. Preparar cinco o más conversaciones controladas con teléfonos autorizados y un responsable humano disponible; incluir los casos de la sección 4. Documentar IDs, resultado esperado/observado y recepción real de escalamiento.
2. Mantener el switch global apagado durante el pilot con whitelist efectiva **si ese mecanismo satisface las pruebas de aislamiento**. Revisar los tres `pending` que aún tenían `ai_agent_enabled=true` al 11-oct y cualquier buffer/job residual. Demostrar que un teléfono no autorizado no recibe respuesta IA, incluso en conversaciones antiguas o nuevas. No asumir que activar globalmente aplica la whitelist: el código actual no funciona así.
3. Presentar resultados y limitaciones a Juan; preguntarle si desea otra prueba y qué alcance acepta. Solo un GO explícito de Nicolás, con conformidad de Juan para la ventana acordada y checklist de despliegue satisfecho, permite reactivar. La fase de pedidos/reservas automáticos requiere una aprobación y pruebas propias.

## 4. Criterios de aceptación verificables

- **AC1 — Identidad y fuente:** dada la aprobación de Juan, existe una fuente versionada con hash, fecha, 144 decisiones de fila o subconjunto explícito, y resolución escrita de Carola/Carolita, `SRV. 5PM` y recargo de datáfono. Ninguna zona no aprobada queda activa.
- **AC2 — Sede:** dado el tenant de El Efecto, al consultar `get_catalog` aparece exactamente la sede activa aprobada con su UUID y línea correspondiente. No aparecen cambios en otros tenants.
- **AC3 — Importación segura:** ejecutar el lote dos veces produce el mismo conjunto de tarifas y aliases; `dry-run` no escribe; una colisión normalizada o una fila alterada falla sin aplicación parcial; el reporte permite revertir el lote.
- **AC4 — Tarifa exacta:** con el UUID obtenido de `get_catalog`, `get_delivery_fee(Carola)` devuelve $6.000 y `get_delivery_fee(Laureles)` $5.000 **si esas filas se ratifican**; `Carolita` solo resuelve con alias aprobado; una zona ausente no recibe estimación; las zonas condicionales no devuelven una tarifa sin comprobar su condición.
- **AC5 — Silencio global:** con `is_enabled=false` y sin pilot autorizado, ningún inbound nuevo, job en buffer ni mensaje IA ya generado produce un envío externo. El estado del agente no cambia al crear sede o importar tarifas.
- **AC6 — Toma humana:** ante greeting, outbound manual desde el teléfono, outbound desde AriCRM o merge LID/PN, la política documentada decide una sola fuente de respuesta. Un humano que toma el caso mientras se generan tools o durante el retraso de envío evita el mensaje IA posterior.
- **AC7 — Reanudación deliberada:** si un operador habilita manualmente el bot después de una intervención humana y el agente está autorizado para ese contacto, los outbounds anteriores no lo silencian para siempre; una intervención humana nueva vuelve a pausarlo. Se prueba en conversación `open` y `pending`.
- **AC8 — Sin promesas ficticias:** sin `create_appointment`/`create_order` permitido y confirmado, el agente no dice que registró o confirmó una reserva/pedido; un 9-oct no se trata como festivo sin fuente; decoración y menú diario no se afirman sin datos vigentes.
- **AC9 — Pilot aislado:** cinco conversaciones de prueba cubren tarifa aprobada, zona no cubierta, reserva, toma humana y saludo; un sexto teléfono no autorizado recibe cero mensajes IA. Escalamiento recibido por el humano designado con contexto, o la prueba falla.
- **AC10 — Trazabilidad:** snapshot del prompt con hash y versión, evidencia de importación y pruebas, checklist de despliegue y estados C-03/C-04/C-06 del programa reflejan hechos verificados; ningún criterio se marca completo por la mera carga de datos.
- **AC11 — FAQs:** si la entrega modifica una capacidad visible o utilizable para clientes, operadores o administradores, `resources/views/public/faq.blade.php` y `docs/FAQ_ARICRM.md` describen la misma capacidad, alcance, requisitos, límites y uso, sin prometer funciones aún no publicadas.

## 5. Pruebas y verificaciones

| Área | Prueba mínima |
| --- | --- |
| Datos | Validador del JSON aprobado: estructura, precios numéricos, 144 decisiones o subconjunto documentado, unicidad normalizada, condiciones y hash; `dry-run` y segunda ejecución idempotente. |
| Tarifas | `DeliveryTariffResolverTest`, `GetDeliveryFeeToolTest` y prueba del caso Carola/Carolita; rechazo de barrio no cubierto y de `branch_id` inválido. |
| Conversaciones | Regresión en `AiAgentSafetyServiceTest`, `AiAgentConversationOverrideTest`, tests de merge LID/PN y despacho WhatsApp: takeover antes/durante/después de generación, override manual posterior, greeting, job retrasado y switch global OFF. |
| Tools y respuestas | Tests de `enabled_tools` del agente, resultado vacío/error de tool y bloqueo de afirmaciones transaccionales sin registro; fechas festivas y no festivas. |
| Pilot | Teléfonos controlados conforme a `templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` del programa, con capturas/IDs sin datos personales en el SPEC. |
| Gate SPECBOOT | `/verify`: tests dirigidos, `npm run lint`, `npm run typecheck`, `graphify update .`; `/code_review` sin hallazgos bloqueantes. |

## 6. Orden de ejecución y decisiones pendientes

1. **Primero, escuchar a Juan y aprobar fuente/alcance.** La revisión interna no sustituye su versión del incidente. Si no desea continuar, no ejecutar cargas ni pilot; registrar su decisión y tratar el alcance del programa con la Cámara por el canal formal.
2. **Después, sede y tarifas**, con bot OFF y una validación de tool de solo lectura. Se puede entregar este avance sin activar IA.
3. **Después, correcciones generales y pruebas**, con cambios de código por SPECBOOT y snapshot del prompt. No mover simplemente `conversationHasHumanOutbound` antes del retorno `true`: rompería la reanudación manual.
4. **Al final, decisión de pilot.** Cualquier autorización debe referirse a una configuración, release, teléfonos, fecha y criterios de parada concretos. No convertir una aceptación de conversar en autorización de activar.

## 7. Fuera de alcance de esta entrega

- Encender el bot, contactar clientes finales, confirmar reservas antiguas o crear pedidos reales.
- Automatizar pedidos o reservas antes de completar las pruebas y la aceptación operativa correspondientes.
- Suponer que todas las 144 tarifas siguen vigentes, que `Carola` equivale a `Carolita`, que `SRV. 5PM` significa una regla determinada o que el saludo del teléfono puede modificarse sin Juan.
- Dar por cerradas las obligaciones contractuales C-03, C-04 o C-06 por el hecho de configurar sede y tarifas.

## 8. Referencias

- Diagnóstico y revisión adversarial: `docs/incidents/2026-10-11-efecto-barbacoa-bot-diagnostico.md` y verificación de DB/logs de la release `d0ee6c6` del 11-oct-2026.
- Harness de la Cámara: `/Volumes/ExternoMS/projects/ccm-vouchers-2026/`, en particular `clientes/el-efecto-barbacoa/{CLIENTE,CARACTERIZACION,TASKS,PROGRESS}.md`, `evidencias/el-efecto-barbacoa/vertical-restaurantes/tarifas-domicilio-2026-09-29.json`, `workflows/{03_vertical_restaurantes,04_ia_conversacional,06_activacion}.md` y `templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md`.
- Código relevante: `app/Http/Controllers/Api/V1/BranchController.php`, `app/Services/Orders/DeliveryTariffResolver.php`, `app/Services/AiAgent/Tools/{GetCatalogTool,GetDeliveryFeeTool}.php`, `app/Jobs/{HandleInboundMessage,FlushAiAgentBufferedReply,SendWhatsAppMessage}.php`, `app/Services/{AiAgentService,AiAgentSafetyService}.php`.

**Siguiente paso SPECBOOT:** convertir este documento en `01-user-story.md`, `02-refined.md` y `03-proposal.md` al iniciar implementación; ejecutar `/apply`, `/verify` y `/code_review` antes de preparar publicación. El SPEC no es un GO de producción.
