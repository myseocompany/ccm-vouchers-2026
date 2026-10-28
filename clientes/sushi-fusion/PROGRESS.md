# PROGRESS — Sushi Fusion (Compañía de Restaurantes Sushi S.A.S.)

Bitácora cronológica de lo que se hizo, con evidencia. No borrar entradas: rectificar con nueva entrada si algo cambia.

## Formato

```
### YYYY-MM-DD — Título corto
- **Qué se hizo**:
- **Obligación asociada**:
- **Responsable**:
- **Evidencia**: ubicación (ruta al archivo, ID de acta, log ID, correo).
- **Notas**:
```

## Entradas

### 2026-10-20 — Alta del cliente y caracterización preliminar
- **Qué se hizo**: se creó la carpeta del cliente (`clientes/sushi-fusion/`) a partir de `_template`; se llenó `CLIENTE.md` con los datos de la Cámara + formulario; se levantó `CARACTERIZACION.md` extrayendo los requisitos del agente IA desde la reunión de onboarding y el formulario.
- **Obligación asociada**: Obligación 2 (caracterización).
- **Responsable**: Nicolás Navarro Rincón — MY SEO.
- **Evidencia**: reunión `../../evidencias/sushi-fusion/reunion-caracterizacion-2026-10-20.md`; formulario `../../evidencias/sushi-fusion/formulario-caracterizacion-2026-10-20.csv`.
- **Notas**: en la sesión se vinculó la línea de WhatsApp a AriCRM por QR en **modo escucha** (no responde aún). Caracterización **preliminar**, pendiente validación del establecimiento. Pendientes abiertos: número de la línea WA; segundo receptor de escalamiento ("los dos"); estructura de catálogo mesa vs domicilio (~400 productos, PDF de 12 MB a aligerar); hora de corte de pedidos (11:30 vs 12:00); detalle de reservas (cumpleaños, no-show, anticipación).

### 2026-10-28 — Prompt v1 consolidado, tarifas→JSON y runbook de onboarding
- **Qué se hizo**: (1) se consolidó el prompt del agente (`ia-conversacional/prompt-v1.md`, reemplaza el borrador) con catálogo apuntando al tool del sistema y regla de canal; (2) un subagente extrajo las tarifas de domicilio del PDF a `tarifas-domicilio.json` (180 barrios, $5.000–$20.000, 0 ilegibles, 32 "zonas en rojo"); (3) se creó el runbook de onboarding del cliente (`ONBOARDING.md`) y su versión reutilizable (`../../workflows/02b_onboarding_runbook.md`).
- **Obligación asociada**: insumo Obligaciones 4 (IA) y 5 (catálogo); operacionaliza workflows 02/03/04/06.
- **Responsable**: Nicolás Navarro Rincón — MY SEO.
- **Evidencia**: `ia-conversacional/prompt-v1.md`, `ia-conversacional/catalogo-skus-v1.md`, `tarifas-domicilio.json`, `ONBOARDING.md`.
- **Decisiones**: la carta digital va en el **tool de catálogo** (precio determinista por el sistema), NO incrustada en el prompt. Discrepancia del contacto de tarifas **resuelta**: la tabla es de Flash Delivery (flota tercerizada), vigencia confirmada por el establecimiento. Las 32 zonas en rojo deben **escalar** en vez de cotizar automático.
- **Notas**: paquete de preparación completo para el deploy; la ejecución (crear sede/horarios/cargar catálogo/prompt en AriCRM prod) se hará desde una sesión en `velo_wa`. Pendientes de validación con el establecimiento: nº línea WA, 2.º receptor de escalamiento, 6 dudas de catálogo (§8 de catalogo-skus-v1).

### 2026-10-28 — Catálogo de SKUs y re-export de conversaciones
- **Qué se hizo**: (1) se construyó el catálogo interno de SKUs por canal (`evidencias/sushi-fusion/ia-conversacional/catalogo-skus-v1.md`, ~360 SKUs de producto + ~40 compartidos) aplicando la regla de desduplicación mesa/domicilio; (2) un agente codex (Orca + `ssh waterfall`, conexión del app en prod) re-exportó las conversaciones del tenant y verificó el resultado contra una consulta agregada directa.
- **Obligación asociada**: Obligación 2 / insumo Obligación 5 (carga de catálogo y prompt del agente).
- **Responsable**: Nicolás Navarro Rincón — MY SEO (export corrido por el usuario vía agente codex).
- **Evidencia**: `evidencias/sushi-fusion/mensajes-sushi-2026-10-28.csv` (perms 600); catálogo en `ia-conversacional/catalogo-skus-v1.md`.
- **Notas**: corpus fresco = **2.905 mensajes · 170 conversaciones** (15–28 oct); **is_automated t = 0** → el agente sigue sin responder (modo escucha), el playbook sigue siendo 100% humano. El prompt v1 mantiene el alcance "arma pedido + escala total/pago/domicilio". Quedan 6 dudas de catálogo para validar con el establecimiento (ver §8 del catálogo). Durante la sesión el disco externo se desmontó y se reconectó; sin pérdida de datos.

### 2026-10-28 — Transcripción de las 6 cartas y corrección a 6 marcas
- **Qué se hizo**: un subagente transcribió las 6 cartas PDF a `evidencias/sushi-fusion/cartas/` (sushi-fusion, inca-fusion, lemon-fish, sushi-house, krabbies, rice-to-go). Se corrigió la ficha: no son 4 marcas sino **6** ("6 marcas, un solo corazón"); "Cravis" del acta = **Krabbies**. Se lanzaron en paralelo: (1) agente codex (vía Orca + `ssh waterfall`) para re-exportar conversaciones, y (2) subagente para detectar conflictos/precios repetidos entre cartas.
- **Obligación asociada**: Obligación 2 (caracterización) / insumo para carga de catálogo (Obligación 5).
- **Responsable**: Nicolás Navarro Rincón — MY SEO.
- **Evidencia**: `evidencias/sushi-fusion/cartas/` (6 .md); análisis de conversaciones `evidencias/sushi-fusion/analisis-conversaciones-2026-10-28.md`.
- **Notas**: cartas confirman — **The Sushi House** y **Rice To Go** son líneas **solo domicilio/para llevar**; Inca Fusión y Lemon Fish mixtas; precios **incluyen impuesto al consumo 8%**, propina sugerida 10%. Sede: Cra 21 #72A-27, Alta Suiza. Resueltos 2 pendientes (Krabbies/Rice To Go vigentes; nombre público "Mercado Gastronómico Fusión"). Pendiente: conflictos de precio entre cartas (en análisis por subagente) y confirmación de jerarquía marca/sub-marca con el establecimiento.

### 2026-10-20 — Recepción de cartas por marca y material de apoyo
- **Qué se hizo**: se copiaron desde `~/Downloads/archivos_mercado` a `media/` los 9 archivos del lote: 6 cartas PDF (Sushi Fusion, Inca Fusion, Lemon Fish, Sushi House, Krabbies, Rice To Go), 1 tabla de tarifas de domicilio y 2 imágenes de WhatsApp. Integridad verificada con shasum (hash del lote igual en origen y destino).
- **Obligación asociada**: Obligación 2 (caracterización); insumo para la carga del catálogo.
- **Responsable**: Nicolás Navarro Rincón — MY SEO.
- **Evidencia**: `media/` (9 archivos, ~49 MB).
- **Notas**: (1) Krabbies y Rice To Go NO figuran entre las 4 marcas de la ficha (Sushi Fusion, Inca Fusion, Lemon Fish, Cravis) — confirmar si son marcas vigentes, sub-marcas o cartas legacy. (2) `Tarifas alta suiza 2026 (2).pdf` es una tabla de tarifas "flash delivery" por barrios de Manizales con contacto 302 798 2676, que no coincide con el contacto del contrato (300 620 7614) — verificar si es del establecimiento o de un tercero. (3) Las 2 imágenes WhatsApp quedan sin clasificar: POLICIES §confidencialidad prohíbe cargar material del cliente en herramientas externas sin autorización escrita.
