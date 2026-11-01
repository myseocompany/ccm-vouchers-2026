# AriCRM — dirección y horario por sede; herramientas seguras en el simulador

**Destino de implementación:** `../velo_wa/` (producto AriCRM preexistente). Este harness solo registra el requerimiento y el criterio de verificación. **Origen:** prueba T01 de Friends Chicken y decisión de Nicolás del 2026-10-07: cada sede debe tener dirección y horario; el simulador debe poder probar herramientas sin efectos reales.

## Estado observado en producción por SSH (`waterfall`, 2026-10-07 13:30 UTC)

- `app/Models/Branch.php` y la migración `2026_10_03_000001_create_branches_table.php` no incluyen dirección ni horario por sede.
- `TenantSettingsController` devuelve `business_hours` del tenant para Configuración general; `BranchOpenStatusService` usa ese horario general para indicar abierto/cerrado.
- `AiAgentController::playground` usa el prompt del formulario cuando hay `preview`, pero llama a `generateReplyWithMeta` sin `useTools` ni conversación. `AiAgentService` exige una conversación para tool calling. WhatsApp usa el prompt guardado y puede activar herramientas según `tool_calling_enabled`.
- No se identificó una herramienta de lectura del menú o del contexto de sede en `app/Services/AiAgent/Tools/`. Una carga en el módulo de menú no demuestra que el agente pueda consultarla.

El release activo verificado es `9585614`; los hallazgos de estructura y simulador anteriores también se confirmaron en él. Para Friends Chicken, la sede Centro está activa pero sin línea vinculada, `business_hours` del tenant es `null` y el agente está habilitado con tool calling. La configuración del agente no restringe `enabled_tools`; el código interpreta esa ausencia como todas las herramientas registradas, incluida potencialmente `create_order`. Ver `evidencias/friends-chicken-cable/ia-conversacional/estado-produccion-2026-10-07.md`. Las páginas privadas `/settings/branches` y `/settings/general` no se inspeccionaron en navegador.

## A. Sede como fuente operativa

1. Cada sede activa debe tener **dirección de recogida** y **horario semanal** explícitos, con zona horaria del tenant. Guardar además excepciones o festivos si el modelo ya las soporta. La pantalla General puede ofrecer valores iniciales para nuevas sedes; una edición posterior del horario general no debe cambiar inadvertidamente los horarios ya confirmados por sede.
2. Migrar sedes existentes sin inventar datos: los campos pueden ser nulos durante la transición, pero la UI debe marcar «pendiente de completar» y bloquear su uso para prometer recogida o aceptar pedidos hasta que el establecimiento confirme dirección y horario. Evitar cerrar sedes existentes por una migración automática.
3. El cálculo de abierto/cerrado y las páginas públicas de pedido deben usar la sede seleccionada. Si una línea WhatsApp está vinculada a una sede, el agente recibe **esa** sede; si hay varias sedes sin relación inequívoca, pregunta cuál desea el cliente antes de ofrecer dirección u horario.
4. Exponer al agente un contexto o herramienta de **solo lectura** con nombre, dirección, horario vigente, estado abierto/cerrado y fuente/fecha de actualización de la sede. Exponer por separado menú y precio vigentes mediante fuente realmente accesible, con aislamiento estricto por tenant y sede.
   - La consulta de menú debe devolver identidad del producto, precio, `is_available`, estado de categoría, sede/modalidad aplicable y fecha de actualización. Si la disponibilidad física o la aptitud para recogida no están modeladas, devolver estado «no verificado» en lugar de inferirlas desde `is_available`.
   - Separar el motivo «sede cerrada» del motivo «producto no disponible» en las respuestas y la traza. Un producto activo solicitado antes de abrir no debe presentarse como agotado. Si hay escalamiento, informar recepción solo tras éxito de la herramienta.
5. Para recogida, el agente puede comunicar la dirección de la sede seleccionada y nunca pide dirección de entrega al cliente. Para domicilio, usa la zona y tarifa de entrega según la sede de origen. En ambos casos, no promete preparación cuando la sede está cerrada o el horario es incierto.

## B. Simulador con herramientas

1. Añadir modos visibles: **sin herramientas**, **lectura segura** y **simulación completa**. Mostrar claramente si se prueba el prompt del formulario aún sin guardar o el prompt guardado que usa WhatsApp, junto con modelo y configuración efectivos.
2. En lectura segura, permitir únicamente consultas necesarias, por ejemplo sede, horario, menú y tarifas. Resolverlas con el mismo tenant, sede y versión de fuente que la conversación real; no usar datos de contactos reales para fabricar contexto.
3. En simulación completa, herramientas con efectos (`create_order`, `handoff_to_human`, tareas, mensajes o automatizaciones) deben producir resultados ficticios etiquetados **simulados**, sin escribir en DB, contactar personas, enviar WhatsApp ni llamar servicios externos. El motor debe impedir efectos por construcción, no por una instrucción al modelo.
4. Devolver una traza por turno: herramienta solicitada, entrada depurada, resultado, fuente y si el efecto fue simulado. Incluir resultado de escalamiento y estado de aceptación del pedido para poder evaluar promesas del agente.
5. Reutilizar el flujo conversacional de WhatsApp tanto como sea posible, con un contexto de conversación sintético y aislado. Añadir un control que impida que un cambio futuro en herramientas convierta el simulador en una ruta de escritura real.

## Criterio de terminado

- Una sede de prueba con dirección y horario confirmados responde correctamente «¿dónde recojo?» y «¿están abiertos?»; otra sede del mismo tenant puede tener datos distintos sin mezcla.
- El simulador resuelve el combo de T01 desde una fuente de menú vigente accesible, muestra qué herramienta consultó y no solicita dirección del cliente para recogida.
- A las 8:40 a. m. de un miércoles, T01 informa que Centro abre a las 11:00 a. m.; no afirma que el combo esté agotado. Dentro del horario, consulta menú y distingue disponibilidad de catálogo de inventario físico. En ambos casos deja el pedido sujeto a aceptación humana.
- La misma conversación, con el mismo prompt guardado y fuentes, produce decisiones equivalentes en simulador y en WhatsApp controlado; se documentan diferencias inevitables de transporte.
- Al simular un pedido y una transferencia a humano, la traza muestra efectos ficticios y se verifica que no hubo orden, mensaje, tarea ni notificación reales.
- Falta de dirección, horario, catálogo o sede inequívoca lleva a aclaración o escalamiento, nunca a una promesa o precio inventado.

## Evidencia requerida

Guardar referencia a commit y release desplegado de `velo_wa`, capturas o logs depurados de T01 y de los casos de sede múltiple, y verificación de ausencia de efectos reales del simulador. La configuración en producción y cualquier prueba en líneas reales siguen el flujo de aprobación de `POLICIES.md`.
