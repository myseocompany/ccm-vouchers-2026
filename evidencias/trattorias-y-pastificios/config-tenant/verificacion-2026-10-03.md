# Verificación de tenant en producción — Trattorias y Pastificios S.A.S.

- **Fecha**: 2026-10-03 (consulta solo lectura)
- **Método**: SSH `waterfall` → `php artisan tinker` sobre `~/app.aricrm.co/current`. Solo SELECT / lectura de schema. No se exponen teléfonos completos, contactos, mensajes ni credenciales.
- **Tenant**: `01a0c5d9-0f5c-73ba-b0ae-0e663da0507f` · slug `trattorias-y-pastificios-sas-q1Vz` · "Trattorias y Pastificios S.A.S."

## 1. Línea WhatsApp

| Campo | Valor |
|---|---|
| id | `01a0c5dc-679f-72d3-8e3f-ef567b074671` |
| status | **connected** |
| provider | evolution |
| phone | …3232 (coincide con 310 482 3232) |
| label | `Dojo` (default) |
| connected_at | 2026-10-03 01:07:37 |
| ai_pause | sin pausa |
| updated_at | 2026-10-03 01:10:04 |

**Conclusión**: la línea está conectada hoy. Nota: el label dice `Dojo` (posible typo de DOYO); corregir en producción si aplica.

## 2. Flags V2 (automatizaciones)

- `tenant_messaging_features`: **sin fila para este tenant** → `automation_rule_builder_v2` y `automation_engine_v2_execute` **NO activos**.
- **Impacto**: las reglas V2 (`send_sequence` de bienvenida y carta) no se ejecutarán hasta activar los flags.

## 3. Agente IA

- `ai_agents`: 1 registro — `01a101af-1bf1-737b-a4bc-d8d03a883e83` · «Asistente de domicilios — plantilla» · modelo `gpt-4o-mini` · `is_enabled=false` · `tool_calling_enabled=true` · `type=conversational` · **sin línea asignada** (`whatsapp_line_id` vacío).
- **Impacto**: el agente existe pero está **deshabilitado** y **sin asignar a la línea**; además usa el prompt genérico, no el `../ia-conversacional/prompt-v1.md` de este cliente.

## 4. Intenciones IA

- `ai_intents`: **0** para este tenant.
- **Impacto**: la intención `pedir_menu` no existe → el disparador `AiIntentDetected` de la secuencia de carta no disparará.

## 5. Usuarios

- `users`: 1 — Paulo Restrepo · role `owner` · `is_active=true` · **email no verificado** (`email_verified_at=null`) · `p***@me.com`.
- **Impacto**: solo hay 1 usuario (sin verificar); falta invitar a Ángela Bedoya (operadora/escalamiento). C-02 requiere hasta 3 usuarios logueables por invitación.

## Brecha para “bot corriendo” (meta jue–vie)

| # | Prerrequisito | Estado | Acción (requiere aprobación, es producción) |
|---|---|---|---|
| 1 | Línea conectada | ✅ | — |
| 2 | Flags V2 activos | ❌ | `updateOrCreate` en `tenant_messaging_features` (editor_v2=1, execute_v2=1) |
| 3 | Intención `pedir_menu` | ❌ | Crear `ai_intents` (slug `pedir-menu`, condition «el cliente solicita conocer el menú o la carta») |
| 4 | Agente IA habilitado y asignado | ❌ | `is_enabled=true`, asignar `whatsapp_line_id`, instalar `../ia-conversacional/prompt-v1.md` |
| 5 | Usuarios (Ángela) | ⚠️ | Invitar a Ángela; verificar email de Paulo |
| 6 | Reglas V2 (bienvenida + carta) | ❌ | Crear tras 2 y 3; probar con teléfonos controlados |

## Actualización 2026-10-03 — Configuración ejecutada en producción (con aprobación)

Escrituras realizadas vía SSH `waterfall` (Eloquent), 2026-10-03:

| # | Acción | Resultado |
|---|---|---|
| 1 | Flags V2 (`tenant_messaging_features`) | ✅ `automation_rule_builder_v2=1`, `automation_engine_v2_execute=1` (id `01a101cf-4b44-7181-aeb5-90dac92af834`) |
| 2 | Intención `pedir_menu` (`ai_intents`) | ✅ slug `pedir-menu`, activa (id `01a101cd-bc0a-70be-9ed3-d838341f1656`) |
| 3 | Agente IA (`ai_agents` `01a101af-…`) | ✅ `is_enabled=1`, asignado a la línea `01a0c5dc-…`, `system_prompt` = `prompt-v1` (7489 chars), `config.prompt_version=v1-trattorias-doyo-ono` |

Verificación post-escritura (solo lectura): V2 editor=1/execute=1 · intent `pedir-menu` activa · agente `enabled=1` con línea y prompt v1 · línea `connected` sin pausa.

> **El agente IA quedó EN VIVO** en la línea 310 482 3232. Aún **no** hay reglas V2 de bienvenida/carta: no se envían automáticamente hasta crearlas y probarlas.

**Pendiente**:
- Invitar a Ángela Bedoya (vía admin de AriCRM, flujo de invitación con verificación de email; no compartir contraseñas). Paulo existe pero su email sigue sin verificar.
- Crear y probar las reglas V2 (bienvenida + carta) con teléfonos controlados.
- Líneas 2 y 3, límite de 2000 contactos y canal adicional (Instagram) para cerrar C-02.

## Nota

Per `../../../SOURCES.md`: el estado `connected` de una línea **no equivale** a tenant configurado ni a obligación C-02 completa. Esta verificación confirma la línea y deja registradas las brechas restantes.
