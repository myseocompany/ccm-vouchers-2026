# Verificación de producción — Friends Chicken — 2026-10-07

**Hora de corte:** 13:30 UTC (8:30 a. m. Colombia). **Método:** SSH `waterfall`, lectura de código del release y consultas `SELECT` mediante `php artisan tinker`; sin cambios de configuración ni lectura de mensajes, prompts, credenciales o contactos.

## Release y estructura

- Release activo: `9585614`.
- `Branch` y la migración de `branches` no tienen dirección ni horario. `BranchController` crea sedes con nombre, línea opcional y estado; la lectura básica devuelve id, nombre y slug.
- `BranchOpenStatusService` calcula abierto/cerrado usando `business_hours` del tenant. La página General edita ese campo.
- `AiAgentController::playground` llama a `generateReplyWithMeta` sin `useTools` ni conversación. La ruta real de WhatsApp puede habilitar herramientas; `AiAgentService` exige una conversación para ejecutarlas.

## Configuración observada para Friends Chicken

- Existe una sede activa «Centro», sin línea WhatsApp vinculada en el registro de sede. No hay columnas de dirección u horario de sede.
- `business_hours` del tenant es `null` en la base de datos. La interfaz puede mostrar un horario predeterminado, pero ese valor no está guardado como horario confirmado del negocio.
- Hay una línea «Principal» con estado `connected` en el momento de la consulta. Esto no demuestra C-02 completa.
- El agente conversacional está `is_enabled=true`, `tool_calling_enabled=true` y usa `gpt-4o-mini`. Su `whatsapp_line_id` es `null`; la configuración `allow_all_lines` es `false`. La configuración no contiene una lista `enabled_tools`.
- En el release, `effectiveEnabledTools` interpreta la falta de `enabled_tools` como todas las herramientas registradas, salvo la de intención cuando no hay intenciones activas. `CreateOrderTool` figura en el registro de herramientas. Esto indica que **puede estar disponible** para el agente; no se comprobó una llamada de creación de pedido en la conversación T01.

## Consecuencia para T01

La sede Centro y el menú cargado en otro módulo no llegan automáticamente como datos verificados al simulador. La prueba de WhatsApp del 2026-10-07 mostró que el agente solicitó dirección de recogida al cliente. Antes de repetir o ampliar pruebas, confirmar horario y dirección de Centro con el establecimiento, verificar cómo el agente consulta menú/sede y revisar qué herramientas de escritura están efectivamente disponibles en su flujo.

**Fuente técnica:** `~/app.aricrm.co/current` en `waterfall`, release `9585614`; tablas `tenants`, `branches`, `whatsapp_lines`, `ai_agents` consultadas con campos minimizados.
