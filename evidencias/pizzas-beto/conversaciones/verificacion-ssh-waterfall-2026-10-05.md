# Verificación SSH waterfall — tenant Beto's Pizza

- **Fecha**: 2026-10-05 (conexión de solo lectura, autorizada por pedido explícito de Nicolás).
- **Método**: `ssh waterfall` → `php artisan tinker` con SELECT sobre PostgreSQL (tablas `conversations`, `messages`). Sin escrituras.
- **Tenant**: `01a0c569-e7a1-70f8-9ee8-c187f35b37ff` (Beto's Pizza).
- **Advertencia**: los `created_at` del servidor se asumen en hora local del tenant (supuesto del análisis local; tz sin confirmar).

## Consultas y resultados

### 1. Estado general del tenant

| Métrica | Valor en producción |
|---|---|
| Conversaciones | 363 (última creada: 2026-10-05 14:38:25) |
| Mensajes (join conversations) | 6.321 totales; 20 nuevos después del corte del export local (2026-10-05 12:28:29); último mensaje 2026-10-05 15:02:58 |

Nota: el export local contiene 6.355 mensajes y la BD reporta 6.321 por join — diferencia de 34 pendiente de explicar (posibles mensajes huérfanos o eliminados; no bloquea el análisis).

### 2. Las 6 conversaciones con etiqueta `pedido_abandonado` (prioridad de auditoría)

| ID | Status | Inicio | Último mensaje | Cerrada |
|---|---|---|---|---|
| `01a0cc61-83ca-72e7-9171-b931434eb419` | pending | 2026-09-23 03:48:57 | 2026-10-03 04:59:27 | no |
| `01a0e0bb-accf-7300-a6a8-3b9b9e877301` | pending | 2026-09-27 02:39:46 | 2026-09-27 02:54:55 | no |
| `01a0e0c2-581c-711f-9afc-73f71e75150c` | pending | 2026-09-27 02:47:08 | 2026-09-27 03:08:58 | no |
| `01a0eecb-5db8-7172-9ba2-1c267bd8fc70` | pending | 2026-09-29 20:11:40 | 2026-10-03 18:06:01 | no |
| `01a104c1-25af-72be-8e88-f0cce5435b4f` | pending | 2026-10-04 02:32:05 | 2026-10-04 02:35:03 | no |
| `01a104dd-d324-706d-babd-eefad610547c` | pending | 2026-10-04 03:03:28 | 2026-10-04 03:06:10 | no |

## Lectura

- Las 6 conversaciones con pedido real sin respuesta siguen **pending** y sin cerrar en producción: nunca fueron tomadas por un humano. La primera es un caso vivo: el cliente escribió el 23-09 a las 03:48, volvió a escribir el 03-10 a las 04:59 y sigue sin respuesta.
- El tenant sigue operando: hay 20 mensajes nuevos posteriores al export del análisis, por lo que la línea está activa hoy.
