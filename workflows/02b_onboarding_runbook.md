# Workflow 02b — Runbook de onboarding del tenant (secuencia operativa)

**Propósito**: secuencia ordenada y concreta para configurar y activar un tenant en AriCRM. **Operacionaliza** los workflows 02 (config tenant), 03 (vertical restaurantes), 04 (IA conversacional) y 06 (activación) + el `../templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md`; no los sustituye.

**Uso**: copiar a `../clientes/<slug>/ONBOARDING.md` y completar con los datos del cliente. Marcar cada paso con evidencia. Toda acción en producción requiere aprobación humana (`../POLICIES.md`).

**Ejemplo instanciado**: `../clientes/sushi-fusion/ONBOARDING.md`.

## Separación preparación / ejecución

- **Preparación** (este harness): caracterización, cartas, catálogo de SKUs, prompt, JSON de tarifas, evidencia. Se versiona en `../evidencias/<slug>/`.
- **Ejecución** (producción AriCRM): se opera desde el panel del tenant o desde comandos de configuración en `../../velo_wa/` (p. ej. `Configure<Cliente>Agent`). Este harness **solo referencia y coordina** velo_wa; un comando nuevo es tarea de código en velo_wa, no del contrato.

## Decisión de diseño — carta digital: ¿prompt o tool?

**Regla por defecto: el catálogo va en el tool de catálogo del tenant, NO incrustado en el prompt.**
- El **precio lo calcula el sistema de forma determinista; el modelo no inventa precios** (workflow 04; Checklist Puerta 2/Fase B).
- El **prompt** solo lleva: lógica de asesoría, overview de marcas, best-sellers y reglas de canal/escalamiento.
- Excepción: catálogos muy pequeños y de precio simple pueden listarse en el prompt como "consulta interna", pero el cálculo del total del pedido sigue siendo determinista.
- Al cliente final se le puede enviar además el PDF/enlace de la carta, independiente del catálogo estructurado.

## Precondiciones

- [ ] Caracterización cerrada (workflow 01).
- [ ] Cartas/menú disponibles y transcritos.
- [ ] Catálogo de SKUs por canal construido (`../evidencias/<slug>/ia-conversacional/catalogo-skus-vN.md`).
- [ ] Prompt borrador (`../evidencias/<slug>/ia-conversacional/prompt-vN*.md`).
- [ ] Número(s) de línea WhatsApp confirmados por el titular.
- [ ] Reglas de domicilio/reservas confirmadas por el establecimiento.

---

## Secuencia

### Paso 1 — Tenant y sede
Crear/confirmar el tenant (registrar `tenant_id` en `../clientes/<slug>/CLIENTE.md`); crear la **sede** (nombre, dirección, contacto de domicilio); invitar usuarios con rol y definir receptor(es) de escalamiento; conectar la(s) línea(s) WhatsApp vía Evolution/QR con el titular presente. **Ref**: workflow 02. **Evidencia**: `../evidencias/<slug>/config-tenant/`.

### Paso 2 — Configuración general: horarios
Cargar el horario de atención y la franja de toma de pedidos/domicilio; el horario debe **bloquear la toma de pedidos fuera de franja**; configurar festivos y cierres excepcionales. **Ref**: workflow 03.

### Paso 3 — Sede: tarifas de domicilio por barrio
Cargar la tabla **barrio → costo** para que el sistema cotice el domicilio (el bot pide el barrio; si no está, escala, nunca "no despacho"). **Fuente**: tabla/PDF del establecimiento (confirmar vigencia antes de cargar). **Opción agente**: un subagente lee el PDF/foto y genera `../evidencias/<slug>/tarifas-domicilio.json` (barrio→precio, con `null` en los ilegibles) listo para cargar. **Ref**: workflow 03.

### Paso 4 — Cargar la carta digital (catálogo estructurado)
Cargar los SKUs al módulo de catálogo respetando el **canal** (mesa/domicilio/ambos) y las reglas de desduplicación; precio determinista por el sistema. Resolver los conflictos/dudas de catálogo **antes** de la carga definitiva. **Ref**: workflow 03. **Criterio**: menú visible desde el flujo conversacional.

### Paso 5 — Montar el prompt del agente
Cargar el prompt consolidado (sin catálogo inline); verificar que referencia el tool de catálogo para precios y las reglas de escalamiento/línea. **Ref**: workflow 04.

### Paso 6 — Reservas, etiquetas y plantillas
Configurar reservas (si aplican), etiquetas base y plantillas de saludo/carta con el tono del negocio. **Ref**: workflow 03.

### Paso 7 — Pruebas y despliegue gradual
Copiar `../templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` a `../evidencias/<slug>/ia-conversacional/despliegue-<fecha>.md` y correr Puertas 1-4 (pruebas con teléfonos controlados → Fase A informativa → Fase B pedidos → vigilancia y parada). **Ref**: workflows 04 y 06.

---

## Criterio de cierre

- Tenant/sede activos, línea(s) WA conectada(s), horarios y tarifas cargados.
- Catálogo visible en el flujo; prompt montado; pedido y reserva de prueba end-to-end.
- Checklist de despliegue superado con evidencia por puerta y autorización de Nicolás para cada fase en producción.
- `PROGRESS.md` y `TASKS.md` del cliente actualizados.
