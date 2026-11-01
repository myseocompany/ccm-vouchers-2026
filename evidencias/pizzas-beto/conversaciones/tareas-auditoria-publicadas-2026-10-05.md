# Publicación de tareas de revisión en AriCRM — tenant Beto's Pizza

- **Fecha**: 2026-10-05. Escritura en producción autorizada por pedido explícito de Nicolás («publica lo encontrado como pedidos para revisar con el cliente»).
- **Método**: `ssh waterfall` → `php artisan tinker`, creación vía `App\Models\Task::create` (Eloquent). Creador: usuario «Nicolas Navarro» (`e8171e8e-6b1f-4dac-aeab-c2e843b99207`). Sin `assigned_to` (el tenant aún no tiene usuarios; cuando Leidy/Alex existan las verán como tareas del tenant).
- **Tenant**: `01a0c569-e7a1-70f8-9ee8-c187f35b37ff`.

## Tareas creadas (7, prioridad alta, abiertas)

| ID tarea | Vinculada a conversación | Título |
|---|---|---|
| `01a10c9f-6403-72ad-844e-fde6e89b3e41` | `01a0cc61-83ca-72e7-9171-b931434eb419` | Pedido sin respuesta — 29-sep 03:31 a. m. |
| `01a10c9f-6427-7235-94f8-ff6e62557b07` | `01a0e0bb-accf-7300-a6a8-3b9b9e877301` | Pedido sin respuesta — 27-sep 02:54 a. m. |
| `01a10c9f-642a-706b-b36b-52d091926ecb` | `01a0e0c2-581c-711f-9afc-73f71e75150c` | Pedido sin respuesta — 27-sep 03:08 a. m. |
| `01a10c9f-642d-7340-a80b-bc6bf6560b0c` | `01a0eecb-5db8-7172-9ba2-1c267bd8fc70` | Pedido programado sin respuesta — 03-oct 18:06 |
| `01a10c9f-642f-715a-b947-ea4a59d1e646` | `01a104c1-25af-72be-8e88-f0cce5435b4f` | Pedido sin respuesta — 04-oct 02:35 a. m. |
| `01a10c9f-6432-709b-b700-a55446b7bce5` | `01a104dd-d324-706d-babd-eefad610547c` | Pedido sin respuesta — 04-oct 03:06 a. m. |
| `01a10c9f-6435-7345-9f4f-14d328eeda7b` | — | Revisar con Beto's las 12 validaciones del menú |

Cada tarea describe el pedido (sin datos personales) y la acción sugerida; las 6 de pedidos citan la conversación exacta para abrirla en `https://app.aricrm.co/inbox/<id>` al mostrar el caso al cliente.

## Verificación posterior (SELECT)

7 tareas en el tenant, todas `priority=high`, abiertas (`completed_at` null); 6 con `conversation_id` correcto y 1 sin conversación (la de validaciones). Contenido validado contra `analisis-conversaciones-2026-10-05.md` y `conversaciones-etiquetadas.json`.

## Reversibilidad

Las tareas pueden eliminarse o completarse por ID si el mecanismo no se quiere usar; no se modificaron conversaciones, mensajes ni configuración del tenant.
