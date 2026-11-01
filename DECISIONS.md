# DECISIONS

Registro cronológico de decisiones aprobadas que afectan el programa. Una vez registrada, una decisión no se borra: se anota su reversión con nueva entrada.

## Formato

```
### YYYY-MM-DD — Título corto
- **Contexto**: qué desencadenó la decisión.
- **Alternativas consideradas**: opciones que se evaluaron.
- **Decisión**: qué se decidió.
- **Responsable**: quién decidió / quién aprobó.
- **Impacto contractual**: obligación / cláusula afectada, si aplica.
- **Fuente**: correo, acta, reunión (con enlace o ubicación).
```

## Entradas

### 2026-11-01 — Los datos personales se usan sin restricción dentro del programa

- **Contexto**: la regla de `POLICIES.md` («no incluir datos personales identificables en entregables») y la de `AGENTS.md` («credenciales, tokens y datos personales nunca se leen, copian ni exponen») estaban frenando trabajo operativo: obligaban a anonimizar capturas, a tapar teléfonos y a pedir autorización para material que el programa necesita. La excepción acotada del 2026-10-16 cubría solo datos de contacto de responsables dentro del expediente.
- **Alternativas consideradas**: abrir solo el uso interno y mantener el filtro al salir hacia la Cámara y servicios externos (planteada y descartada por Nicolás); abrir además el cruce de datos entre establecimientos (no solicitada: la regla de no mezclar clientes se mantiene).
- **Decisión**: los datos personales de contactos, responsables y clientes finales se usan **sin restricción** en todo el programa: expedientes, evidencias, capturas, prompts, informes y comunicaciones externas, incluidos los entregables a la Cámara. No se anonimiza ni se tapa nada, y no hace falta autorización previa. **La regla de credenciales, tokens, `.env` y contraseñas se mantiene intacta** por decisión expresa. También se mantiene la prohibición de cruzar datos entre establecimientos (`AGENTS.md`).
- **Responsable**: Nicolás (instrucción directa, 2026-11-01).
- **Impacto contractual**: el responsable del tratamiento frente a la Ley 1581/2012 sigue siendo MY SEO COMPANY S.A.S. y su titular contractual; esta decisión define cómo opera el harness, no traslada ni elimina esa responsabilidad. Se le advirtió a Nicolás que borrar la regla del repo cambia el comportamiento del harness, no la exposición legal, y que los datos son de los clientes finales de los diez establecimientos. Confirmó el alcance completo.
- **Fuente**: instrucción directa de Nicolás en sesión del 2026-11-01.

### 2026-11-01 — La documentación de tenants se trae de velo_wa al harness

- **Contexto**: la documentación operativa de los establecimientos (snapshots de prompt versionados con SHA-256, guiones de prueba, validaciones, tarifas) vivía en `../velo_wa/docs/<tenant>/` y en ramas sin fusionar de ese repo. El harness del programa la desconocía, por lo que `clientes/<slug>/TASKS.md` subregistraba el avance real de las obligaciones 4 y 5.
- **Alternativas consideradas**: copiarla al harness y mantener las dos (rechazado por Nicolás: las copias se desactualizan); referenciar las rutas de `velo_wa` sin traerla (rechazado: parte vive en ramas de trabajo desechables).
- **Decisión**: mover la documentación de tenants a `evidencias/<slug>/velo_wa/`, que queda como única copia y fuente de verdad. En `velo_wa` se retiraron los archivos (commit `b59d9660`, rama `main`, **sin publicar**) y se dejó el puntero `docs/TENANTS_CCM_VOUCHERS.md`. Tres excepciones permanecen en `velo_wa` porque `ConfigureCalamarAzulAgent` y `ConfigureLaPatateriaAgent` las cargan en runtime y el servidor de despliegue no tiene montado este repo: el snapshot v8 de Calamar Azul, y el v9 y la carta de La Patatería. La documentación que vive en las ramas `myseocompany/{betos,indecente,efecto}` y `myseocompany/review-trattoria-implementation` ya está traída, pero se retira de origen solo cuando esas ramas se fusionen.
- **Responsable**: Nicolás (instrucción directa, 2026-11-01); ejecutado por ZCode.
- **Impacto contractual**: habilita sustentar las obligaciones 4 y 5 con evidencia técnica trazable. Excepción expresa a la regla de `AGENTS.md` de que este harness no edita `velo_wa`: la autorización cubre este movimiento de documentación, no cambios de código.
- **Fuente**: instrucción directa de Nicolás en sesión del 2026-11-01; `velo_wa` commit `b59d9660`.

### 2026-10-30 — Depuración del listado de beneficiarios (9 de 10 definidos)

- **Contexto**: el roster canónico de `scripts/validate.sh` seguía listando La Megachuleta, Arepas Rellenas Samu, Cheesecake Pizza Milán y Manuelina, mientras Calamar Azul, Sushi Fusión y The Boss Burger tenían trabajo y evidencias en el repo sin estar registrados en el cupo. El listado operativo no cuadraba en diez.
- **Alternativas consideradas**: mantener el roster anterior y tratar los tres nuevos como adicionales (rechazado: el contrato cubre diez cupos); esperar soporte formal de la Cámara antes de ajustar el roster (rechazado: bloquea la generación de los informes parciales).
- **Decisión**: La Megachuleta, Arepas Rellenas Samu, Cheesecake Pizza Milán y Manuelina **no van**. Quedan **nueve** beneficiarios confirmados: el-efecto-barbacoa, friends-chicken-cable, la-patateria, pizzas-beto, trattorias-y-pastificios, indecente, sushi-fusion, mar-azul (Calamar Azul) y the-boss (The Boss Burger). **El décimo cupo queda sin definir** (La Rancha sigue fuera hasta confirmación escrita). Las carpetas de los cuatro excluidos no se borran: quedan como expediente histórico.
- **Responsable**: Nicolás (instrucción directa, 2026-10-30).
- **Impacto contractual**: define sobre qué establecimientos se acreditan las obligaciones 2–16 y para quiénes se emiten los informes individuales (obl. 15). El soporte documental de la Cámara para las sustituciones queda pendiente de archivar; hasta entonces no reportar esas sustituciones como cierre contractual.
- **Fuente**: instrucción directa de Nicolás en sesión del 2026-10-30.

### 2026-10-29 — Plantilla única del informe de avance de la Cámara en el harness
- **Contexto**: la Cámara entregó el formato oficial de informe de avance (`INFORME_CAMARA_OFICIAL.docx`); la única copia quedó sin trackear en el worktree orca `sushi-manifesto-intent-flows`, y las instrucciones de llenado circulaban solo como prompt de chat.
- **Alternativas consideradas**: referenciar la ruta del worktree orca (rechazado: workspace desechable, archivo sin commit, ruta inestable); mantener plantilla e instrucciones duplicadas (rechazado: divergencia entre copias).
- **Decisión**: copia canónica única en `templates/INFORME_CAMARA_OFICIAL.docx` (verificada por md5 contra el original); instrucciones de llenado consolidadas en `workflows/08_informes.md`, sección «Informe de avance (parcial)». Ningún agente edita la plantilla original; se copia a un directorio de trabajo para cada informe.
- **Responsable**: Nicolás (confirmó el formato 2026-10-29); ZCode consolidó.
- **Impacto contractual**: soporta la obligación 12 (informes de avance); no cambia plazos ni alcance.
- **Fuente**: conversación con Nicolás 2026-10-29; archivo del formato entregado por la Cámara.

### 2026-10-16 — Calamar Azul sustituye a Arepas Rellenas Samu
- **Contexto**: Nicolás informó la pérdida de Arepas Rellenas Samu y solicitó implementar Calamar Azul, sede Cable.
- **Alternativas consideradas**: conservar a Samu activo o preservarlo como expediente histórico y usar el cupo para Calamar Azul.
- **Decisión**: Calamar Azul reemplaza a Samu en el listado operativo de diez. Samu no se borra; Calamar Azul queda en revisión hasta soporte formal de la Cámara.
- **Responsable**: Nicolás.
- **Impacto contractual**: obligaciones del cupo sustituido; no acredita activación.
- **Fuente**: instrucción directa de Nicolás, 2026-10-16.

### 2026-10-16 — Calamar Azul sustituye a Arepas Rellenas Samu
- **Contexto**: Nicolás informó la pérdida de Arepas Rellenas Samu y solicitó implementar Calamar Azul, sede Cable.
- **Alternativas consideradas**: conservar a Samu activo o preservarlo como expediente histórico y usar el cupo para Calamar Azul.
- **Decisión**: Calamar Azul reemplaza a Samu en el listado operativo de diez. Samu no se borra; Calamar Azul queda en revisión hasta soporte formal de la Cámara.
- **Responsable**: Nicolás.
- **Impacto contractual**: obligaciones del cupo sustituido; no acredita activación.
- **Fuente**: instrucción directa de Nicolás, 2026-10-16.

### 2026-10-05 — Habilitación de automatizaciones V2 para Beto's Pizza
- **Contexto**: preparación de las secuencias de bienvenida y carta, y del agente conversacional de Beto's Pizza.
- **Alternativas consideradas**: mantener las automatizaciones V2 deshabilitadas o habilitar por separado el editor y el motor de ejecución.
- **Decisión**: Nicolás autorizó habilitar ambos flags por SSH para el tenant de Beto's Pizza: `automation_rule_builder_v2` y `automation_engine_v2_execute`.
- **Responsable**: Nicolás autorizó; MY SEO aplicó y verificó.
- **Impacto contractual**: preparación de obligaciones 4 y 5. No implica la publicación de reglas, envío de mensajes ni activación del agente IA.
- **Fuente**: instrucción directa en esta conversación, 2026-10-05; evidencia `evidencias/pizzas-beto/vertical-restaurantes/flags-v2-2026-10-05.md`.

### 2026-10-05 — Exportación controlada de conversaciones de Beto's Pizza
- **Contexto**: se requiere revisar conversaciones reales del tenant para caracterización y parametrización del asistente de Beto's Pizza.
- **Alternativas consideradas**: limitarse a métricas agregadas o descargar un export acotado y local.
- **Decisión**: Nicolás autorizó explícitamente descargar en modo solo lectura las conversaciones de este único tenant. El material se conserva exclusivamente de forma local en `evidencias/pizzas-beto/conversaciones/raw/`, excluido de Git, y se usa únicamente dentro del propósito contractual.
- **Responsable**: Nicolás.
- **Impacto contractual**: protección de datos (Cláusula Quinta, obligaciones 22–25); aplica las salvaguardas documentadas en `SOURCES.md`.
- **Fuente**: instrucción directa en esta conversación, 2026-10-05.

### 2026-09-12 — Correcciones tras auditoría inicial del harness
- **Contexto**: auditoría del scaffolding recién creado identificó 6 hallazgos (3 Alta, 3 Media): criterios de aceptación laxos que permiten cierres prematuros, ausencia de tareas de post-implementación y soporte, C-02 pedía credenciales violando POLICIES, precondición del workflow 01 dependía del listado completo de la Cámara, doble estado editable entre CLIENTE.md y TASKS.md, y referencias a archivos inexistentes.
- **Decisión**:
  - `clientes/_template/TASKS.md`: los criterios de aceptación por tarea replican textualmente los del workflow correspondiente. Se agregaron C-07 (licenciamiento 4m), C-08 (soporte SLA), C-09 (informe individual con acuse), C-10 (cierre de período). C-02 sustituyó "solicitar credenciales" por "invitaciones desde AriCRM + conexión asistida por operador del establecimiento sin recepción de contraseñas".
  - `clientes/_template/CLIENTE.md`: se agregaron hitos temporales con evidencia (activación efectiva, licenciamiento inicio/fin, informe, cierre soporte). Se eliminó la tabla "Estado" — TASKS.md es la fuente canónica.
  - `workflows/01_caracterizacion.md`: precondición ahora exige confirmación específica del cliente por la Cámara, no P-002 global.
  - `evals/vertical_restaurantes.md` y `evals/README.md`: creados para respaldar P-006.
  - `scripts/validate.sh`: validador local que revisa archivos raíz, carpetas, 10 clientes, workflows, templates, referencias .md rotas, campos vacíos de CLIENTE.md y tareas "completa" sin evidencia.
  - Correcciones de referencias rotas en workflow 06, README, TASKS, templates y VOLUNTEER.en.md.
  - Templates re-propagados a los 10 clientes (CLIENTE.md, TASKS.md, CARACTERIZACION.md sobreescritos; INFORME.md y PROGRESS.md preservados).
- **Responsable**: Nicolás (aprobó la auditoría) + Claude Code (aplicó).
- **Impacto contractual**: refuerza trazabilidad de cumplimiento (reduce riesgo de cierres sin evidencia) y aísla mejor la ejecución por cliente (reduce bloqueos cruzados).
- **Fuente**: auditoría reportada en conversación 2026-09-12; validador corrió con 0 errores críticos.

### 2026-09-12 — Estructura del harness del programa
- **Contexto**: Necesidad de coordinar cumplimiento del contrato CT-239-26-3 con evidencia por cliente y por obligación.
- **Alternativas consideradas**:
  - Reusar `myseo-env` con `clients/ccm-vouchers-2026/` (rechazado: mezclaría un contrato específico con el harness transversal de MySEO).
  - Meter la gestión del programa dentro del repo `velo_wa` (rechazado: contamina el producto AriCRM con obligaciones de un solo contrato y complica la posición de propiedad intelectual).
  - Harness propio en `/Volumes/ExternoMS/projects/ccm-vouchers-2026/` (elegido).
- **Decisión**: Harness independiente en `ccm-vouchers-2026/`, con estructura inspirada en `myseo-env` (AGENTS/SOUL/POLICIES + clientes/ + workflows/ + templates/). El código de AriCRM permanece en `velo_wa` y este harness no lo modifica.
- **Responsable**: Nicolás.
- **Impacto contractual**: Ninguno directo. Refuerza la posición de propiedad intelectual (Cláusula 17): AriCRM es producto preexistente separado del contrato.
- **Fuente**: Conversación con Claude Code, 2026-09-12.

### 2026-09-12 — Corrección de cierres y validación de evidencias
- **Contexto**: segunda auditoría detectó IDs de cierre desalineados, aceptación de rutas genéricas como evidencia, omisión de conformidad de soporte y placeholders no detectados.
- **Decisión**: corregir los IDs de seis workflows; añadir Evidencia a tareas globales, plantilla y diez clientes; rechazar cierres sin archivos concretos existentes y no vacíos; detectar campos básicos pendientes sin imprimir sus valores; exigir conformidad escrita de soporte en C-08/C-10.
- **Responsable**: Nicolás autorizó la corrección; Codex la implementó.
- **Impacto**: controles documentales; no cambia estados de avance ni configuraciones de producción. La suficiencia del contenido probatorio sigue requiriendo revisión humana.
- **Fuente**: auditoría y autorización «hazlo» en esta conversación, 2026-09-12.

### 2026-09-12 — Poblado inicial de 9 CLIENTE.md desde tabla de la Cámara + tercera auditoría
- **Contexto**: la Cámara envió tabla con datos de 10 establecimientos. 9 coinciden con los slugs previamente creados; Indecente NO aparece; Sevicheria El Costeño DG aparece con datos completos pero no está en la lista original de 10. Contexto crítico: todos los diagnósticos son por sismo (daño estructural severo, colapso, operación desde casas).
- **Decisión**:
  - Poblar los 9 CLIENTE.md coincidentes con NIT/cédula, contacto principal, dirección, canal WhatsApp y "Contexto pre-caracterización" (afectación por sismo + operación actual).
  - Normalizar campo `**NIT/Cédula**` → `**NIT**` para que el validador lo detecte.
  - Levantar discrepancia a Nicolás: qué hacer con Indecente (sin datos) y Sevicheria El Costeño DG (con datos, no en lista). Pendiente de decisión.
  - Tercera auditoría (2026-09-12): 6 workflows cerraban IDs de tarea equivocados (heredado del scaffolding inicial, antes de que Codex reordenara los C-XX). Corregido: 02→C-02, 03→C-03, 04→C-04, 05→C-05, 06→C-06, 08→C-09. 07_soporte_sla cubre C-07/C-08/C-10 (continuas durante 4 meses, no se "cierran" en un paso).
  - Alta 2 de la tercera auditoría (validador acepta cierres sin evidencia real) verificada como resuelta por Codex: bash validate.sh sale con exit 1 cuando una tarea se marca completa sin evidencia.
- **Responsable**: Nicolás autorizó ("dale"); Claude Code implementó.
- **Impacto contractual**: los datos poblados quedan bajo la política de protección de datos personales (Ley 1581/2012). Repo privado en GitHub. Discrepancia Indecente/Sevicheria bloquea confirmación total de la obligación 2 hasta que se decida.
- **Fuente**: tabla enviada por Nicolás con datos de la Cámara (registros de llamada 26–31/08/2026); auditoría reportada en conversación 2026-09-12.

### 2026-09-12 — Resolución discrepancia Indecente / Sevichería El Costeño DG
- **Contexto**: la tabla de la Cámara del 2026-09-12 incluía datos de "Sevichería El Costeño DG" (que no estaba en la lista original de 10) y omitía datos de "Indecente" (que sí estaba).
- **Decisión**: Sevichería no entra en la lista. Indecente se mantiene como uno de los 10 beneficiarios; los datos de contacto llegan después. La carpeta `clientes/indecente/` queda con placeholder hasta que se reciban.
- **Responsable**: Nicolás, 2026-09-12.
- **Impacto contractual**: los 10 beneficiarios siguen siendo los originalmente registrados. La obligación 2 (caracterización) para Indecente queda bloqueada hasta que llegue la información.
- **Fuente**: instrucción directa en conversación 2026-09-12.
