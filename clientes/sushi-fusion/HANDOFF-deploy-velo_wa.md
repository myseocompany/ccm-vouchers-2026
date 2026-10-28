# HANDOFF — Deploy del agente IA de Sushi Fusion (para sesión en velo_wa)

Brief para el agente que ejecutará el **deploy en AriCRM producción**. La **preparación** está hecha en el harness del contrato (`ccm-vouchers-2026`); tú ejecutas la **configuración** en el producto.

## Contexto

- Cliente: **Compañía de Restaurantes Sushi S.A.S.** — opera como **"Mercado Gastronómico Fusión"** (6 marcas en una cocina).
- Tenant AriCRM: **`01a140b0-1dd9-7012-b03a-80cc84eb76f3`**.
- Programa: Vouchers Digitales 2026 (CCM). Es **configuración de AriCRM preexistente**, no desarrollo para el contrato. Si necesitas código nuevo (p. ej. un comando `ConfigureSushiFusionAgent`), es evolución de producto en velo_wa.
- Estado del canal hoy: una sola línea WhatsApp, en **modo escucha** (el agente aún NO responde; `is_automated=0` en 2.905 mensajes). El playbook actual es 100% humano.

## Regla de oro

**La carta va en el tool/catálogo del sistema, NO incrustada en el prompt.** El **precio y el total los calcula el sistema** de forma determinista; el modelo nunca inventa precios (ver Checklist de despliegue, Puerta 2 / Fase B).

## Insumos ya preparados (rutas absolutas)

> Nota: los CSV de mensajes de clientes contienen PII y están fuera de git (`.gitignore`). No los subas a ningún servicio externo.

- Prompt del agente (cargar en config del agente): `/Volumes/ExternoMS/projects/ccm-vouchers-2026/evidencias/sushi-fusion/ia-conversacional/prompt-v1.md`
- Catálogo de SKUs por canal (cargar al catálogo del tenant): `/Volumes/ExternoMS/projects/ccm-vouchers-2026/evidencias/sushi-fusion/ia-conversacional/catalogo-skus-v1.md`
- Tarifas de domicilio (cargar en la sede): `/Volumes/ExternoMS/projects/ccm-vouchers-2026/evidencias/sushi-fusion/tarifas-domicilio.json` (180 barrios; 32 "zonas en rojo" → deben **escalar**, no cotizar)
- Cartas PDF (para enviar al cliente y como fuente): `/Volumes/ExternoMS/projects/ccm-vouchers-2026/clientes/sushi-fusion/media/` (6 PDFs)
- Runbook paso a paso: `/Volumes/ExternoMS/projects/ccm-vouchers-2026/clientes/sushi-fusion/ONBOARDING.md`
- Ficha del cliente: `/Volumes/ExternoMS/projects/ccm-vouchers-2026/clientes/sushi-fusion/CLIENTE.md`

## Secuencia de deploy (resumen de ONBOARDING.md)

1. **Tenant/sede**: confirmar sede, dirección Cra 21 #72A-27 Alta Suiza; invitar usuarios (Carlos Mauricio Villa Sánchez operador; Ana María Sepúlveda); conectar la línea WA por QR con el titular.
2. **Horarios** (config general): L–S 12:00–21:30, Dom 12:00–21:00; pedidos/domicilio desde 11:30. Bloquear toma de pedidos fuera de franja.
3. **Tarifas de domicilio** (sede): cargar `tarifas-domicilio.json`. Configurar que las 32 zonas en rojo **escalen a humano**. Fuente = Flash Delivery (flota tercerizada), vigente.
4. **Catálogo** (vertical restaurantes): cargar SKUs respetando canal **mesa vs domicilio** (domicilio = The Sushi House / Rice To Go; Sushi Fusión = mesa y bloques compartidos). Homónimos = SKUs distintos.
5. **Prompt**: cargar `prompt-v1.md` en la config del agente.
6. **Reservas / etiquetas / plantillas**.
7. **Pruebas + despliegue gradual**: copiar `templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` a `evidencias/sushi-fusion/ia-conversacional/despliegue-<fecha>.md` y correr Puertas 1–4.

## Alcance del agente v1

Arma el pedido y captura datos (nombre, barrio, dirección, teléfono) y **escala al humano el cierre**: total, costo de domicilio, pago y verificación de comprobante. Tarjeta de crédito = link manual del humano. Línea mixta: NO responder hilos internos (equipo/proveedores/turnos).

## Validaciones pendientes con el establecimiento (antes de activar en prod)

1. Número de la línea WhatsApp y **2.º receptor de escalamiento** (se dijo "los dos").
2. **6 dudas de catálogo** (§8 de `catalogo-skus-v1.md`): discrepancias de bebidas (Agua Manantial, Fuze Tea, Sodas), rolls exclusivos de Sushi Fusión a domicilio, combos (falta página de combos de la carta SF), productos de temporada, disponibilidad por franja.
3. Validar el prompt v1 con el establecimiento.

## Guardrails

- Toda acción en producción requiere **aprobación explícita de Nicolás** (`POLICIES.md`).
- No activar pedidos automáticos hasta superar Fase A (informativa) del checklist.
- No copiar datos personales de clientes al repo del contrato.
