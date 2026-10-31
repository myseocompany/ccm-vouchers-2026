# PROGRESS — Friends Chicken Cable

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

### 2026-10-30 — Verificación de producción: la bitácora quedó dos versiones de prompt atrás
- **Qué se hizo**: verificación de solo lectura por SSH (`waterfall`, release `d4e3cf55`) del tenant completo, hecha junto con la de Calamar Azul para comparar ambos. Se registró por primera vez el tenant_id, aportado por Nicolás en sesión y ausente de todo el repositorio hasta hoy.
- **Obligación asociada**: 3, 4 y 5 — insumo de C-02/C-03/C-04; no acredita cierre.
- **Responsable**: MY SEO (harness), por instrucción de Nicolás.
- **Evidencia**: `../../evidencias/friends-chicken-cable/ia-conversacional/verificacion-produccion-2026-10-30.md`.
- **Notas**: el prompt en producción es `v5-fc-cobertura-escala-2026-10-25`, con linaje desde `v4-fc-tono-whatsapp-2026-10-09`; esta bitácora solo documentaba hasta `v1-fc-menu-snapshot-2026-10-07`. **El prompt ya referencia `get_delivery_fee`, `get_catalog`, `quote_order` y `create_order`**, así que la causa documentada del fallo de T01 quedó obsoleta y T01 debe repetirse. **Contradicción por resolver**: el prompt afirma «Friends Chicken no acepta reservas», contra la entrada del 2026-09-30 de esta misma bitácora. El riesgo de la 2.ª línea está mitigado (`allow_all_lines = true`). `orders = 0` y `tenant_user_memberships = 0`: criterios de C-03 y C-02 incumplidos. Solo 1 de 5 automatizaciones está activa y ningún ítem del catálogo tiene imagen.

### 2026-10-07 — Verificación de la instancia en waterfall: parche de prompt aplicado
- **Qué se hizo**: consulta de solo lectura (SSH `waterfall`, tinker, 14:05 UTC) del tenant completo. Se confirmó que el parche de prompt autorizado por Nicolás está **aplicado e íntegro**: bloque «Prioridad operativa» (1 vez), dirección `#19-63` sin rastro de `#19-61`, «domingo, 9:00» sin rastro de «domingo, 11:00», `prompt_version=v1-fc-menu-snapshot-2026-10-07` y `prompt_sha256` coincidente con el texto guardado (actualizado 13:57 UTC). `business_hours` ya está guardado (lun–sáb 11:00–19:30, dom 09:00–17:00). Línea «Principal» connected; sede Centro activa con 179/179 tarifas; menú 7 categorías/31 ítems disponibles; intención `pedir-menu` y plantilla `menu-friends-chicken` activas (sin uso); flags V2 activos; 0 automatizaciones activas. Usuarios: 0. Hallazgo de código: el agente (sin línea vinculada, `allow_all_lines=false`) responde porque el tenant tiene una sola línea; al conectar la 2.ª línea dejaría de responder salvo vinculación o `allow_all_lines`.
- **Obligación asociada**: 3, 4 y 5 — insumo de C-02/C-03/C-04; no acredita cierre.
- **Responsable**: MY SEO (harness), por instrucción de Nicolás.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/verificacion-instancia-2026-10-07.md`.
- **Notas**: la aplicación del parche (13:57 UTC) no tenía entrada propia en esta bitácora; esta verificación la documenta. T01 sigue pendiente de repetición controlada. C-02 sin acreditar: 0 usuarios, 1 de 3 líneas.

### 2026-10-07 — Segunda ejecución de T01 contradice disponibilidad del catálogo
- **Qué se hizo**: se contrastó por SSH, en modo solo lectura, el mensaje de WhatsApp que declaró no disponible el combo cuarto de pollo para recoger. El catálogo muestra el combo disponible (COP 21.000) y categoría activa; el agente tiene tool calling activo pero no cuenta con herramienta de consulta de menú ni base de conocimiento vinculada.
- **Obligación asociada**: 5 — prueba de C-04, pendiente.
- **Responsable**: Nicolás (prueba); MY SEO (verificación y análisis).
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/t01-2026-10-07.md`; matriz `PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: el mensaje salió a las 8:40 a. m., antes de la apertura de las 11:00 a. m. El cierre es una explicación plausible, aunque no verificable sin traza del razonamiento. La respuesta atribuyó el problema al producto en vez de explicar el horario. No prueba el inventario físico ni descarta una regla separada para recogida. No se modificó producción. T01 continúa fallido.

### 2026-10-07 — Tarifas de domicilio cargadas en sede Centro
- **Qué se hizo**: se cargaron las 179 tarifas del JSON en la sede activa Centro. Las tres entradas inicialmente inactivas se activaron después de que Nicolás confirmara los nombres. «Conju La Estacion» se corrigió a «Conjunto La Estación». Centro 1 y Centro 2 quedan en COP 5.000; «Centro» genérico requiere precisión.
- **Obligación asociada**: 4 y 5 — tarifas del vertical e insumo para el agente.
- **Responsable**: MY SEO; carga autorizada por Nicolás y verificada por SSH.
- **Evidencia**: `evidencias/friends-chicken-cable/operacion/tarifas-cargadas-sede-centro-2026-10-07.md`; fuente sincronizada: `evidencias/friends-chicken-cable/operacion/domicilios/tarifas-flash-delivery-2026.json`.
- **Notas**: 179 de 179 registros activos. La tarifa no garantiza disponibilidad de Flash; verificar antes de aceptar un domicilio.

### 2026-10-07 — Horario general del tenant verificado por SSH
- **Qué se hizo**: consulta de solo lectura de `business_hours` y `timezone` en producción. Horario guardado: lunes a sábado 11:00–19:30; domingo 09:00–17:00; zona `America/Bogota`.
- **Obligación asociada**: 4 y 5 — insumo para horario del vertical y del agente; no prueba activación.
- **Responsable**: MY SEO (harness), por instrucción de Nicolás.
- **Evidencia**: `evidencias/friends-chicken-cable/operacion/horario-tenant-2026-10-07.md`.
- **Notas**: difiere del prompt borrador en el horario de domingo y siguen sin resolverse los límites de domicilio. Las sedes aún no tienen dirección ni horario en el modelo actual.

### 2026-10-07 — Verificación de producción por SSH antes de la reunión
- **Qué se hizo**: lectura de código y consultas minimizadas del tenant en `waterfall`. Se verificó el release, la sede Centro, horario general no guardado, línea Principal conectada y agente habilitado con tool calling. Se confirmó que el simulador no ejecuta herramientas y que la sede aún carece de dirección y horario propios en el modelo.
- **Obligación asociada**: 3, 4 y 5 — diagnóstico previo de C-02/C-03/C-04; no acredita cierre.
- **Responsable**: MY SEO (harness), por instrucción directa de Nicolás.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/estado-produccion-2026-10-07.md`.
- **Notas**: no hubo cambios de producción. La ausencia de restricción `enabled_tools` exige revisar el alcance efectivo antes de más pruebas de pedidos.

### 2026-10-07 — T01 parcial falló en simulador y WhatsApp
- **Qué se hizo**: Nicolás ejecutó el primer mensaje de T01 en el simulador y en WhatsApp. El simulador no pudo consultar el menú; WhatsApp pidió datos de pago y contacto antes de validar el producto y luego solicitó una dirección para un pedido para recoger. Se archivó un análisis sin los datos personales usados en la prueba. No se verificó creación de pedido ni escalamiento.
- **Obligación asociada**: 5 — prueba de C-04, pendiente.
- **Responsable**: Nicolás (prueba); MY SEO (análisis documental).
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/t01-2026-10-07.md`.
- **Notas**: revisar el prompt efectivamente guardado, el acceso del agente al catálogo y la lógica de recogida antes de repetir T01. Esta prueba no cumple el criterio de aceptación.

### 2026-10-07 — Guiones sintéticos de prueba del agente
- **Qué se hizo**: se prepararon 12 conversaciones de prueba para el agente de Friends Chicken: cinco del workflow 04 y siete casos de regresión sobre carta, domicilios, cambios de pedido, duplicados, demoras, pagos y toma humana. No se han ejecutado ni enviado mensajes.
- **Obligación asociada**: 5 — preparación de C-04.
- **Responsable**: MY SEO (harness).
- **Evidencia**: `clientes/friends-chicken-cable/PRUEBAS_CONVERSACIONALES.md`.
- **Notas**: usar teléfonos controlados y registrar resultados antes de solicitar activación; los datos operativos pendientes deben validarse con el establecimiento.

### 2026-10-07 — Preparación de reunión de caracterización y ensayo
- **Qué se hizo**: se preparó una guía para la reunión de las 9:00 a. m. con preguntas sobre sede y línea operativa, vigencia del menú, horarios, domicilios, pagos, reservas, escalamiento y pruebas controladas. Se actualizó la siguiente acción de C-01. No se ejecutó configuración ni activación.
- **Obligación asociada**: 2, 4 y 5 — preparación de C-01, C-03 y C-04.
- **Responsable**: MY SEO (harness).
- **Evidencia**: `clientes/friends-chicken-cable/PREPARACION_REUNION_2026-10-07.md`.
- **Notas**: la hora de reunión fue indicada por Nicolás el 2026-10-07; las respuestas del establecimiento están pendientes.

### 2026-09-28 — Inicio de carga del menú digital en AriCRM
- **Qué se hizo**: en el tenant de Friends Chicken se creó la categoría `Combos` y el ítem `Combo cuarto de pollo` (COP 21.000), con su descripción tomada de la carta vigente de septiembre. La categoría y el ítem permanecen sin activar para evitar que el flujo de WhatsApp entregue un catálogo incompleto.
- **Obligación asociada**: 4 — plantilla vertical restaurantes (configuración parcial; no activación).
- **Responsable**: MY SEO, mediante sesión de superadministración en modo impersonación del tenant.
- **Evidencia**: `evidencias/friends-chicken-cable/vertical-restaurantes/menu/aricrm-menu-parcial-2026-09-28.png`; fuente de catálogo: `evidencias/friends-chicken-cable/vertical-restaurantes/menu/menu-friends-chicken-2026-09.pdf`.
- **Notas**: quedan por cargar las demás categorías e ítems; las fotografías se mantienen sin asignación a productos porque el establecimiento no entregó un mapeo verificable. C-03 continúa en progreso y no se cumplen aún sus pruebas ni criterios de aceptación.

### 2026-09-28 — Catálogo digital de septiembre cargado y verificado
- **Qué se hizo**: se completó la carga transaccional del menú vigente en el tenant de Friends Chicken. Quedaron activas 7 categorías y disponibles 31 ítems: Combos (7), Especiales (4), Pollo (4), Alitas (6), Alternos (2), Bebidas (7) y Salsas (1). Se actualizaron nombre, precio, descripción, orden y disponibilidad a partir de la carta entregada.
- **Obligación asociada**: 4 — plantilla vertical restaurantes (configuración de menú; no cierre de obligación).
- **Responsable**: MY SEO, con autorización explícita del responsable operativo para configurar el tenant mediante el canal administrativo.
- **Evidencia**: `evidencias/friends-chicken-cable/vertical-restaurantes/menu/verificacion-carga-aricrm-2026-09-28.md`; fuentes: PDF y cartas de septiembre en la misma carpeta.
- **Notas**: las 16 fotografías siguen sin asociarse a ítems por falta de mapeo verificable. Faltan reglas de pedidos/domicilios, etiquetas y plantillas, además de pruebas end-to-end de pedido y reserva; C-03 permanece en progreso.

### 2026-09-28 — Regla de cobro de domicilios incorporada al prompt
- **Qué se hizo**: Friends Chicken confirmó que la tarifa aplicable de Flash Delivery Manizales se traslada íntegramente al cliente, sin subsidio ni recargo propio. El prompt exige identificar la zona, consultar la tarifa, validar disponibilidad y discriminar el domicilio en el total.
- **Obligación asociada**: 4 y 5 — reglas de pedido del vertical e insumo para el agente IA (borrador documental; no activación).
- **Responsable**: Friends Chicken confirmó la regla operativa; MY SEO actualizó el borrador.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`; `evidencias/friends-chicken-cable/operacion/domicilios/tarifas-flash-delivery-2026.json`.
- **Notas**: la cobertura efectiva y la disponibilidad deben verificarse antes de cada confirmación; la tabla conserva advertencias del proveedor.

### 2026-09-28 — Plantilla interna de menú creada
- **Qué se hizo**: se creó y activó en el tenant la plantilla interna `Menú Friends Chicken` (`menu-friends-chicken`), compuesta por un saludo y las dos imágenes de la carta vigente. El prompt prioriza esta plantilla ante solicitudes de menú.
- **Obligación asociada**: 4 y 5 — plantillas de respuesta del vertical e insumo para el agente IA (configuración; no prueba de envío ni activación).
- **Responsable**: MY SEO, con autorización explícita para configurar la plantilla.
- **Evidencia**: `evidencias/friends-chicken-cable/vertical-restaurantes/plantillas/menu-friends-chicken-2026-09-28.md`.
- **Notas**: no se enviaron mensajes. Falta conectar la línea WhatsApp y probar el envío desde una conversación de prueba.

### 2026-09-30 — Ajuste solicitado para reservas y abono no reembolsable
- **Qué se hizo**: se corrigió el borrador del prompt: Friends Chicken recibe solicitudes de reserva, el caso se escala primero a un asesor humano y no se anuncia una reserva como agendada antes de la confirmación verificable. Se incorporó el abono de COP 50.000, no reembolsable si no se utiliza, pero consumible en el restaurante dentro de los tres meses siguientes, con lenguaje claro y no confrontativo.
- **Obligación asociada**: 5 — agente IA con escalamiento a humano (ajuste documental; no activación).
- **Responsable**: Friends Chicken suministró la regla operativa; MY SEO actualizó el borrador.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`.
- **Notas**: falta confirmar por escrito la fecha desde la cual se cuentan los tres meses y probar el escalamiento en una conversación real.

### 2026-09-28 — Borrador de prompt para pedidos por WhatsApp
- **Qué se hizo**: se redactó el prompt v1 de Friends Chicken con los datos de caracterización recibidos. Menú, zonas, costo de domicilio, línea conectada e instrucciones de recogida permanecen bloqueados para verificación o escalamiento.
- **Obligación asociada**: 5 — agente IA con escalamiento a humano (preparación documental; no activación).
- **Responsable**: MY SEO / borrador generado a solicitud del establecimiento.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`.
- **Notas**: C-04 continúa pendiente: faltan el vertical activo, configuración del destinatario de escalamiento y pruebas conversacionales.

### 2026-09-28 — Catálogo parcial y formulario de domicilio recibidos
- **Qué se hizo**: se incorporaron al borrador del prompt los acompañamientos, salsas, bebidas, composiciones de picada x2 y x4, y los campos de nombre, teléfono, dirección, barrio y pago para domicilio.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA (insumo documental; no configuración ni activación).
- **Responsable**: Friends Chicken Centro suministró la información; MY SEO actualizó el borrador.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`.
- **Notas**: el catálogo no incluye precios, categorías comerciales, reglas de agotados, zonas, costo de domicilio ni disponibilidad. C-03 y C-04 continúan pendientes.

### 2026-09-28 — Horario comercial y regla de transferencia recibidos
- **Qué se hizo**: se incorporó el horario comercial por día, el mensaje de comprobante para transferencias y el cierre de atención al borrador del prompt.
- **Obligación asociada**: 5 — agente IA con escalamiento a humano (insumo documental; no activación).
- **Responsable**: Friends Chicken Centro suministró la información; MY SEO actualizó el borrador.
- **Evidencia**: `evidencias/friends-chicken-cable/ia-conversacional/prompt-v1.md`.
- **Notas**: el horario comercial recibido no coincide exactamente con las referencias previas de cierre para domicilios; el prompt exige verificarlas antes de prometer un horario de despacho.

### 2026-09-28 — Archivos del establecimiento organizados
- **Qué se hizo**: se archivaron el menú vigente en PDF, la foto de menú, 16 fotografías de catálogo y dos soportes de transferencia en las rutas aisladas del cliente. Las fotos se numeraron sin atribuirlas a productos específicos porque no existe un mapeo confirmado.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA (evidencia fuente; no configuración ni activación).
- **Responsable**: MY SEO.
- **Evidencia**: `evidencias/friends-chicken-cable/vertical-restaurantes/menu/menu-friends-chicken-2026-09.pdf`, `evidencias/friends-chicken-cable/vertical-restaurantes/imagenes-productos/`, `evidencias/friends-chicken-cable/pagos/`.
- **Notas**: el PDF es la fuente documental del menú; su carga y validación en AriCRM permanecen pendientes.

### 2026-09-28 — Páginas de carta en imagen archivadas
- **Qué se hizo**: se archivaron dos imágenes de la carta: especiales y combos; alitas, pollo y alternos. Su contenido coincide con las páginas operativas del menú PDF de septiembre.
- **Obligación asociada**: 4 — vertical restaurantes (evidencia fuente; no configuración ni activación).
- **Responsable**: MY SEO.
- **Evidencia**: `evidencias/friends-chicken-cable/vertical-restaurantes/menu/carta-friends-chicken-2026-09-especiales-y-combos.jpeg`, `evidencias/friends-chicken-cable/vertical-restaurantes/menu/carta-friends-chicken-2026-09-alitas-pollo-y-alternos.jpeg`.
- **Notas**: se tratan como formatos complementarios del mismo menú, no como una versión distinta.

### 2026-09-28 — Tarifas de domicilio estructuradas
- **Qué se hizo**: se reclasificó la fotografía de tarifas de Flash Delivery como evidencia operativa y se transcribieron 179 zonas y valores a JSON.
- **Obligación asociada**: 4 y 5 — vertical restaurantes y agente IA (insumo documental; no configuración ni activación).
- **Responsable**: MY SEO.
- **Evidencia**: `evidencias/friends-chicken-cable/operacion/domicilios/tarifas-flash-delivery-2026-09-15.jpeg`, `evidencias/friends-chicken-cable/operacion/domicilios/tarifas-flash-delivery-2026.json`.
- **Notas**: la tabla advierte que la tarifa varía según el servicio y exige consultar disponibilidad para zonas marcadas en rojo; el prompt requiere validación antes de confirmar un domicilio. Tres etiquetas con lectura potencialmente incompleta fueron marcadas para contraste antes de producción.

### 2026-09-30 — Borrador v1 de plantillas WhatsApp (bienvenida + carta)
- **Qué se hizo**: se redactó el borrador de las dos plantillas de WhatsApp (bienvenida al inicio de la conversación y carta cuando el cliente la pide) junto con sus reglas de automatización V2, con base en la acción `send_template` de AriCRM (rama `feature/v2-send-template-action`, commit `0e22de0`, pendiente de fusión a `main`).
- **Obligación asociada**: 4 y 5 — preparación de C-03/C-04. No es registro en producción.
- **Responsable**: MY SEO (agente LLM del harness).
- **Evidencia**: `PLANTILLAS_WHATSAPP.md`; formato y mecanismo en `../../templates/PLANTILLAS_WHATSAPP.md`.
- **Notas**: el registro en Meta/AriCRM requiere aprobación (POLICIES) y se ejecuta en el workflow 03. Pendientes: URL del menú digital y validación del copy con el establecimiento.
