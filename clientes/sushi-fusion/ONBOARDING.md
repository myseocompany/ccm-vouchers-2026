# ONBOARDING — Sushi Fusion (Mercado Gastronómico Fusión)

Runbook ordenado para configurar y activar el tenant en AriCRM. **Operacionaliza** los workflows existentes (no los sustituye): `../../workflows/02_config_tenant.md`, `03_vertical_restaurantes.md`, `04_ia_conversacional.md`, `06_activacion.md` y el `../../templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` (despliegue gradual).

Tenant AriCRM: `01a140b0-1dd9-7012-b03a-80cc84eb76f3`. Toda acción en producción requiere aprobación humana (`../../POLICIES.md`).

## Decisión de diseño — carta digital: ¿prompt o tool?

**Va en el tool de catálogo del tenant, NO incrustada en el prompt.** Razones:
- Son ~400 SKUs con 34 conflictos de precio y reglas mesa/domicilio → incrustarlo en el prompt lo haría enorme y el modelo podría equivocar precios.
- La convención de la casa exige que el **precio lo calcule el sistema de forma determinista, no el modelo** (workflow 04 y Checklist Puerta 2/Fase B).
- **El prompt solo lleva**: lógica de asesoría (por componentes), overview de las 6 marcas, best-sellers y las **reglas de canal/escalamiento**. El detalle de ítems y precios vive en el catálogo (`ia-conversacional/catalogo-skus-v1.md` → cargar al módulo).
- Para el cliente final, además, se puede **enviar el PDF/enlace** de cada carta (como hoy), independiente del catálogo estructurado del bot.

## Precondiciones (estado 2026-10-28)

- [x] Caracterización cerrada — `CARACTERIZACION.md` (workflow 01).
- [x] Cartas transcritas (6) — `../../evidencias/sushi-fusion/cartas/`.
- [x] Catálogo de SKUs por canal — `../../evidencias/sushi-fusion/ia-conversacional/catalogo-skus-v1.md`.
- [x] Prompt v1 borrador — `../../evidencias/sushi-fusion/ia-conversacional/prompt-v1-borrador.md`.
- [ ] Número(s) de línea WhatsApp confirmado(s) por el titular.
- [ ] 6 dudas de catálogo validadas con el establecimiento (ver §8 del catálogo de SKUs).
- [x] Tarifas de domicilio en formato cargable (JSON barrio→precio) — `../../evidencias/sushi-fusion/tarifas-domicilio.json` (180 zonas).

---

## Secuencia de configuración

### Paso 1 — Crear/confirmar el tenant y la sede
- **Dónde**: AriCRM (superadmin/panel del tenant).
- **Qué**: el tenant ya existe (`01a140b0…`). Confirmar/crear la **sede** (venue) del restaurante: nombre, dirección **Cra 21 #72A-27, Alta Suiza, Manizales**, datos de contacto de domicilio.
- **Usuarios**: invitar a Carlos Mauricio Villa Sánchez (operador) y Ana María Sepúlveda; definir quién recibe escalamientos (pendiente 2.º receptor).
- **Líneas WhatsApp**: conectar la línea (una por ahora) vía Evolution/QR con el titular presente. Registrar el número en `CLIENTE.md`.
- **Ref**: workflow 02. **Evidencia**: `../../evidencias/sushi-fusion/config-tenant/`.

### Paso 2 — Configuración general: horarios
- **Dónde**: configuración general del tenant/sede.
- **Qué**: horario de atención **lunes a sábado 12:00 m – 9:30 p. m.; domingo 12:00 m – 9:00 p. m.** Toma de pedidos/domicilio **desde 11:30 a. m.** El horario debe **bloquear la toma de pedidos** fuera de franja (Checklist Puerta 2/Fase B). Configurar festivos/cierres excepcionales.
- **Ref**: workflow 03 paso 3.

### Paso 3 — Sede: tarifas de domicilio por barrio
- **Dónde**: módulo de la sede (zonas/tarifas de domicilio).
- **Qué**: cargar la tabla **barrio → costo de domicilio** para que el sistema calcule el total (el bot pide el barrio y el sistema cotiza; si el barrio no está, escala sin decir "no despacho").
- **Fuente**: `media/Tarifas alta suiza 2026 (2).pdf` (tabla de **Flash Delivery Manizales**, la flota tercerizada; el contacto 302 798 2676 es del domiciliario, no del restaurante — discrepancia resuelta). Vigencia confirmada por el establecimiento 2026-10-28.
- **JSON listo** ✅ `../../evidencias/sushi-fusion/tarifas-domicilio.json` — 180 barrios, precios $5.000–$20.000, 0 ilegibles. Incluye **32 "zonas en rojo"** (marcadas con nota) → el bot **debe escalar/consultar disponibilidad** en esos barrios, no cotizar automático.
- **Nota de carga**: las tarifas varían con servicios especiales/pesados/datáfono (nota de la tabla); el humano ajusta esos casos.
- **Ref**: workflow 03 paso 3.

### Paso 4 — Cargar la carta digital (catálogo estructurado)
- **Dónde**: módulo de catálogo del tenant (plantilla vertical restaurantes).
- **Qué**: cargar los SKUs desde `../../evidencias/sushi-fusion/ia-conversacional/catalogo-skus-v1.md`, respetando el **canal** (mesa / domicilio / ambos) y la regla de desduplicación. Precio determinista por el sistema.
- **Bloqueante**: resolver las 6 dudas de §8 del catálogo antes de la carga definitiva (precios de bebidas, rolls SF a domicilio, combos).
- **Ref**: workflow 03 pasos 1-2. **Criterio**: menú completo visible desde el flujo conversacional.

### Paso 5 — Montar el prompt del agente
- **Dónde**: configuración del agente IA del tenant.
- **Qué**: cargar el prompt consolidado desde `../../evidencias/sushi-fusion/ia-conversacional/prompt-v1-borrador.md` (sin catálogo inline). Verifica que el prompt referencia el catálogo/tool para precios y la regla de línea mixta.
- **Ref**: workflow 04.

### Paso 6 — Reservas, etiquetas y plantillas
- **Qué**: reservas (sí, sin costo; capturar ocasión/fecha/#personas); etiquetas base (pedido, reserva, queja, recurrente…); plantillas de saludo/carta con el tono del negocio.
- **Ref**: workflow 03 pasos 4-6.

### Paso 7 — Pruebas y despliegue gradual
- **Qué**: copiar `../../templates/CHECKLIST_DESPLIEGUE_AGENTE_IA.md` a `../../evidencias/sushi-fusion/ia-conversacional/despliegue-<fecha>.md` y correr Puertas 1-4 (pruebas con teléfonos controlados → Fase A informativa → Fase B pedidos → vigilancia).
- **Ref**: workflows 04 y 06 + checklist.

---

## Resumen de decisiones pendientes antes de activar

1. Confirmar número de línea WhatsApp y 2.º receptor de escalamiento.
2. Validar las 6 dudas de catálogo (§8 de `catalogo-skus-v1.md`).
3. Confirmar vigencia del PDF de tarifas y generar el JSON barrio→precio.
4. Validar el prompt v1 con el establecimiento.
