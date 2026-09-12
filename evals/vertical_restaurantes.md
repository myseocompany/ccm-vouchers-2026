# Eval — Vertical Restaurantes de AriCRM

Referenciado por `../TASKS.md` global P-006.

**Objetivo**: verificar que la plantilla vertical restaurantes en `../velo_wa/` soporta el alcance contractual (menú digital, pedidos, reservas, plantillas, IA + escalamiento) para los 10 tenants antes de arrancar configuraciones.

**Precondiciones**:
- Acceso al repo `../velo_wa/`.
- Instancia de desarrollo levantada (ver `../velo_wa/CLAUDE.md`).

## Checklist

### Multi-tenancy y aislamiento
- [ ] Se pueden crear ≥10 tenants sin colisión de datos.
- [ ] Cada tenant admite hasta 3 usuarios activos.
- [ ] Cada tenant admite 3 líneas de WhatsApp conectadas simultáneamente vía Evolution API.
- [ ] Cada tenant admite ≥2000 contactos sin degradación evidente.

### Menú digital
- [ ] Carga de catálogo por tenant (productos, categorías, precios, variantes).
- [ ] Soporte de fotos y descripciones.
- [ ] Presentación al contacto final desde el flujo conversacional.
- [ ] Edición desde el panel refleja cambios en la conversación.

### Pedidos
- [ ] Captura de pedido end-to-end desde WhatsApp.
- [ ] Configuración por tenant de métodos de pago, cobertura y costo de domicilio.
- [ ] Estados de pedido visibles en el panel.
- [ ] Notificación al usuario del tenant cuando entra un pedido.

### Reservas
- [ ] Captura de reserva end-to-end desde WhatsApp.
- [ ] Configuración por tenant de horarios, tamaño de grupo, anticipación, no-show.
- [ ] Reservas visibles en el panel.

### Plantillas y etiquetas
- [ ] Set base de etiquetas cargable por plantilla.
- [ ] Set base de plantillas de respuesta cargable.
- [ ] Personalización por tenant sin afectar otros.

### IA + escalamiento
- [ ] Prompt configurable por tenant.
- [ ] Reglas de escalamiento configurables (quejas, palabras clave, fuera de dominio).
- [ ] Escalamiento entrega contexto suficiente al humano designado.
- [ ] Prompt versionable / recuperable.

### Reporting
- [ ] Métricas mínimas por tenant: conversaciones, Dt1, pedidos, reservas, tasa de escalamiento.
- [ ] Consultas agregadas para dashboard consolidado del programa.

## Criterio global

Aprobado si todos los ítems marcados `[x]`. Cualquier ítem sin marcar debe abrir una tarea en `../velo_wa/` con severidad acorde a bloqueo del cronograma (6 semanas).
