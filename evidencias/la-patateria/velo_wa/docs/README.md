# La Patatería — referencia operativa

Tenant de restaurante (papas rellenas y snacks) de Manizales. Onboarding del agente IA de reservas: **2026-10-12**. Fuentes del negocio: caracterización y análisis FAQ (`exports/patateria-01a0cb62/analisis-faq-agente-ia-2026-10-12.md`, carpeta del programa en `ccm-vouchers-2026/clientes/la-patateria/`).

## Identificadores de producción (Waterfall)

| Elemento | Valor |
|---|---|
| Tenant | `01a0cb62-1d87-7101-ab7b-c2a0ddc30f5f` · slug `la-patateria-oYFT` · tz `America/Bogota` |
| Owner | Jorge Eduar Zapata de los Ríos (`eduarzapatadelosrios@gmail.com`, usuario `01a0cb62-2008-719e-a6d1-2dbf35350a26`) |
| Línea WhatsApp | `Principal` (`01a0cb6b-715b-70e0-a70b-d64210799c8f`) · instancia Evolution `line_01a0cb6b715b` · +57 324 688 7353 · webhook vía gateway |
| Recurso reservable | `Restaurante Manizales` + `Restaurante Pereira` · tipo `table` · modo capacity · capacidad **40 c/u (provisional)** · servicios `mesa_manizales` / `mesa_pereira` |
| Sedes (Branch) | `Manizales` (slug `manizales`, Cra 23 # 75-48) · `Pereira` (slug `pereira`, frente al Parque Arboleda) — activas, se inyectan al prompt del agente por turno |
| Agente IA | `Reservas La Patatería` · conversational · **gpt-4.1-mini** · default de la línea |
| KB | `Carta La Patatería` · **una fuente por producto** · **publicada: 94 productos de la carta física** (v5, `carta/carta-fotos-2026-10-12.md`, transcrita desde 20 fotos — confirmada por el dueño el 12-oct) |
| Prompt activo | `docs/patateria/prompts/reservas/v8-ajustes-reunion-2026-10-12.md` |
| Comando | `php artisan patateria:configure-agent` (idempotente; `--skip-kb` para no tocar la carta) |

## Alcance del agente (v3)

- **Dos sedes con puerta de ciudad**: Manizales (Cra 23 # 75-48) y Pereira (frente al Parque Arboleda). El agente pregunta la ciudad cuando la respuesta depende de la sede, como lo hacía el equipo (174 envíos en el corpus).
- **Reservas de mesa de punta a punta**: recopila ciudad, nombre, celular, correo (opcional), día, hora, personas y ocasión; confirma; crea con `create_appointment` usando el service de la sede (`mesa_manizales`/`mesa_pereira`) y la sede en notas (modo capacity → reserva **confirmada** + QR automático). Cambios y cancelaciones se escalan (`find_reservation` + `handoff_to_human`). Reserva sin costo; última hora de reserva 7:30 p. m.
- **Carta**: explica platos y precios desde la KB (46 fuentes por producto); bases disponibles (papa en cascos, puré, francesa, criolla); menú del día (L-V, $25.500 con bebida, solo en sitio); pedidos siempre derivados al link de domicilios `https://linktr.ee/LaPatateriaDomicilios` (el agente NO arma órdenes ni cotiza).
- **Domicilios**: solo Pereira por Rappi (respuesta estándar del negocio en el corpus, 43 envíos); Manizales sin domicilio por ahora → recoger en el punto o tienda en línea.
- **Cumpleaños** (23% de la demanda): registra la ocasión; decoración gratis con globos (cumpleaños y grados), brownie con helado de cortesía para el cumpleañero, torta propia permitida — datos corpus-confirmados.
- **Mascotas** permitidas; 2x1 de hamburguesas solo en Pereira (días → equipo).
- **Escalado a humano**: quejas/PQR, pagos y facturación, alergias, grupos >15, promociones/bonos/convenios, empleo, proveedores.
- **Intenciones**: 22 sembradas (lista del análisis FAQ) → `record_detected_intent` se activa automáticamente y habilita analítica y futuros triggers de automatizaciones V2.

## Decisiones de diseño y por qué

1. **Modo capacity (table) sin tool de disponibilidad**: `get_available_slots`/`get_availability` solo resuelven unidades `professional`/`service`, no `table`; sin Google Calendar no hay consulta previa posible. El agente propone horas dentro del horario y crea tras confirmación explícita; `create_appointment` valida capacidad, horario y solapes dentro de la transacción (lock + restricción `reservations_no_overlap`). Los errores (`capacity_exceeded` con `available_party_size`, `closed`, `slot_taken`, `past_time`) guían las alternativas.
2. **Reservas confirmadas (no solicitudes)**: en modo capacity el tool crea `confirmed` + QR — mismo flujo de mesas de Los Arrieros. La creación es la verificación del cupo.
3. **Sin reservas el mismo día**: política observada en el corpus (media-alta confianza, operación temporal post-sismo). El bot ofrece atención por orden de llegada y escala si insisten. **Pendiente de validación**.
4. **Horario de la caracterización** (L-J 12–21, V-S 12–22, D 12–20): reporte formal del negocio del 2026-10-12, prevalece sobre el corpus de septiembre (que cerraba todo a las 21:00). **Pendiente de validación**.
5. **Dos sedes con puerta de ciudad (v3)**: el corpus muestra operación en Manizales (punto temporal Milán/Circunvalar, Tv 72 #16-54) y Pereira ("frente al Parque Arboleda"), con la pregunta de ciudad como saludo estándar del negocio. La dirección Cra 23 # 75-48 (Manizales) fue confirmada por Nicolás el 2026-10-12 — corresponde al local de la reapertura. Se crearon dos `Branch` (se inyectan al prompt por turno vía `injectBranchContext`) y dos unidades reservables con services distintos por sede para que la disponibilidad y la capacidad no se crucen entre ciudades; la unidad legacy "Restaurante La Patatería" se renombró a "Restaurante Manizales".
6. **Domicilios solo con link**: contradicción crítica sin resolver (docs: "Pereira sin domicilio" vs corpus: "solo Pereira por Rappi"). El agente no afirma cobertura, tarifas ni plataformas.
7. **Conversaciones existentes (250) sin backfill**: decisión del onboarding — el bot solo atiende conversaciones nuevas (las nuevas nacen con `ai_agent_enabled=true`, `HandleInboundMessage.php:191`).
8. **Contexto temporal**: el sistema inyecta fecha/hora actual + calendario de 14 días (`AiAgentService::injectCurrentTimeContext`) — el prompt solo lo referencia.

## Publicar la KB de la carta

El comando crea la versión en `draft` y despacha `ProcessKnowledgeSource`. Publicación (equivalente a `KnowledgeController::publishVersion`):

```php
// tinker en la release activa de waterfall
$v = App\Models\KnowledgeBaseVersion::withoutGlobalScopes()
    ->where('knowledge_base_id', App\Models\KnowledgeBase::withoutGlobalScopes()
        ->where('tenant_id', '01a0cb62-1d87-7101-ab7b-c2a0ddc30f5f')
        ->where('name', 'Carta La Patatería')->value('id'))
    ->orderByDesc('version_number')->first();
// verificar antes: todas las fuentes del version en status 'ready'
```

Publicar solo cuando las fuentes estén `ready` (la publicación hace `superseded` de la versión anterior y actualiza `published_version_id`). Para actualizar la carta: reemplazar/crear `docs/patateria/carta/carta-<fecha>.md`, actualizar `CARTA_PATH` en el comando y re-ejecutar (deduplica por hash del contenido).

## Versionado del prompt

- Snapshots en `docs/patateria/prompts/reservas/` — nunca sobrescribir una versión publicada.
- Historial: v1-reservas → v2-ubicacion → v3-sedes → v4-personalidad (gpt-4.1-mini) → v5-precision-carta → v6-promo-bases → v7-cuestionario → v8-ajustes-reunion → **v9-carta-fisica-2026-10-12 (activa)**: promo alineada con la carta física (hamburguesas *tradicionales*, $49.900), aplicada junto con la KB v5 (94 productos de la carta física, confirmada por el dueño).
- La carta física quedó aplicada el 2026-10-12 tras la confirmación del dueño. La tienda bibisoft puede seguir con el catálogo anterior — pendiente que el dueño la actualice para que tienda y bot coincidan.
- El comando lee el snapshot activo (`SNAPSHOT_PATH`), extrae el cuerpo entre `ARICRM_PROMPT_START/END`, calcula el SHA-256 y lo persiste en `config.prompt_version`/`prompt_sha256`/`prompt_published_at` del agente.
- Para publicar v3: crear `v3-<descripcion>-<fecha>.md` (con metadatos y hash), actualizar `SNAPSHOT_PATH`, re-ejecutar el comando y verificar el hash persistido.

## Pendientes de validación con el negocio (Jorge / Javier)

| # | Tema | Estado | Siguiente paso |
|---|---|---|---|
| 1 | Aforo real por sede | Sin respuesta en el cuestionario — 40/40 provisional | Confirmar con el dueño |
| 2 | Reservas mismo día | ✅ Resuelto (v7): sí, si se piden antes del mediodía; después → walk-in u otro día | — |
| 3 | Horario por día y por sede | Parcial: V-S cierre 10 p. m. confirmado; tabla por día sin respuesta; **última hora del domingo inferida** (7:30 p. m., de "fin de semana" = V-S) | Confirmar domingo y horario por sede |
| 4 | Direcciones | ✅ Manizales Cra 23 # 75-48 · Pereira Av. Circunvalar #5-83 (v6) | Agregar Google Maps si lo entregan |
| 5 | Punto temporal Manizales | ✅ "Ya no habrá sede temporal" (v7); Cra 23 # 75-48 abre el 13-oct desde las 6 p. m. | — |
| 6 | Domicilios | ✅ Pereira sí (solo Rappi, enlace oficial) · Manizales no; recogida en ambas (v7) | — |
| 7 | Decoración y celebraciones | ✅ Gratis en todas las sedes: cumpleaños, grados, aniversarios, eventos empresariales; centro de mesa con bombas + postre cortesía al homenajeado; torta propia OK, alcohol solo del restaurante (v7) | — |
| 8 | Última hora de reserva | ✅ L-J y domingo 7:30 p. m. · V-S 8:00 p. m. (v7; domingo inferido) | Confirmar domingo |
| 9 | Menú del día | ✅ L-V sin festivos, 12:00–2:00 p. m., solo en punto, menús rotan por día (el del día lo confirma el equipo); precio $25.500 "pendiente" de reconfirmar | Reconfirmar precio |
| 10 | 2x1 hamburguesas | ✅ Ambas sedes, solo hamburguesa Clásica, martes y jueves de 3:00 p. m. al cierre (v7) | — |
| 11 | Bono de reconstrucción | ✅ Ya no se vende; los existentes se redimen sin condiciones → equipo (v7). Convenio corporativo → humano | — |
| 12 | Usuario del equipo | ✅ **Otman David Hernandez Zea** (`ohernandez@unal.edu.co`) creado en la reunión y verificado. Javier Quinchía sin usuario (su rol operativo lo asume David) | — |
| 13 | Tono del agente | Sin respuesta explícita — se mantiene *buena papa con picardía* | Confirmar en la revisión del 14-oct |
| 14 | Cierre de validación | **Sin firmar** (sin nombre ni aprobación explícita del titular) | Obtener firma/aprobación |
| 15 | Revisión de información | **Miércoles 14 de octubre, 12:00 m** (acordado en reunión: monitoreo del bot en vivo) | Agendar |
| 16 | Reservas mismo día | ✅ Resuelto (12-oct, Nicolás): se confirma la regla vigente — misma noche sí si se pide antes del mediodía; después del mediodía, para el otro día | — |
| 17 | Duración del bloque de mesa | ✅ Resuelto (12-oct, Nicolás): se mantiene el bloque de 2 horas | — |
| 18 | Menú del día — 15 menús | El dueño enviará los 15 menús; rotación: avanzan solo L-J sin festivos, viernes siempre cazuela de frijoles, reinicia tras el 15. Hoy el agente no afirma cuál es (correcto: la conexión agente↔menú del día no existe aún) | Recibir los menús y cargarlos en menú del día |
| 19 | Festival de hamburguesas | Próxima semana; el dueño aprendió a auto-editar el prompt vía UI (esperar divergencia de hash → re-snapshot) | Re-snapshot tras su edición |
| 20 | Carta PDF vigente "hasta mañana" | El PDF/qrco.de/beIGEr se actualiza con la reapertura; el dueño mantiene el contenido del Linktree | Verificar contenido nuevo el miércoles |

**Contactos del negocio** (cuestionario): quejas/cobros/reservas con problema → **Eduard y David** · hojas de vida, proveedores, prensa y propuestas → **318 426 72 02** · facturación → actualizar datos en `https://app.bibisoft.co/register-clients?company_id=55` y solicitar de nuevo; el equipo del WhatsApp corrige.

## Runbook

1. **Reconexión de la línea** (desconectada desde el 30-sep): coordinar el escaneo del QR con Jorge (Ajustes → WhatsApp o `GET /instance/connect/line_01a0cb6b715b` en Evolution). El agente ya queda activo para las conversaciones que nazcan después.
2. **Monitoreo primera hora/día**: `grep -E 'ai_safety|ai_takeover' storage/logs/laravel.log` en la release activa; vigilar `flush_aborted abort_reason=daily_cap_exceeded` (warmup día 1 con cap bajo — Patatería es de bajo volumen, debería alcanzar; si no, revisar el spec de Botanazo P3, no implementado).
3. **Smoke test** (con la línea conectada): escribir al +57 324 688 7353 desde otro teléfono: (a) pedir la carta (debe compartir qrco.de/beIGEr y poder explicar platos), (b) preguntar por un plato específico (datos exactos de la KB), (c) preguntar por la ubicación sin decir ciudad (debe preguntar Manizales/Pereira), (d) ubicación en Pereira (debe responder Av. Circunvalar #5-83 frente al Parque Arboleda), (e) reservar para hoy **antes del mediodía** (debe aceptar) y **después del mediodía** (debe ofrecer walk-in u otro día), (f) reservar para mañana 2 personas en Manizales (debe registrar la *solicitud* con código — nunca decir "confirmada" — llegar el QR y la reserva quedar en `Restaurante Manizales` con "Sede: Manizales" en notas), (g) reservar en Pereira (debe crear en `Restaurante Pereira`), (h) preguntar por decoración de cumpleaños (centro de mesa con bombas gratis + postre cortesía), (i) domicilio en Manizales (no hay; recogida en el punto) y en Pereira (solo Rappi, enlace oficial), (j) preguntar por el 2x1 (ambas sedes, solo Clásica, martes y jueves desde las 3 p. m.), (k) preguntar por medios de pago (efectivo, datáfono, tarjetas y QR; sin transferencias).
4. **Verificación post-config**: agente enabled+default, recurso activo, 22 intenciones, KB vinculada y publicada, `prompt_sha256` del agente = hash del snapshot.

## Limitaciones conocidas

- **El contexto de KB son excerpts de ~700 chars** (`KnowledgeRetrievalService::excerptAroundMatch`), no chunks completos. Por eso la KB se estructura a una fuente por producto: cada fuente es más corta que la ventana y el modelo siempre ve el plato completo. Preguntas de categoría amplia ("¿qué hamburguesas tienen?") devuelven hasta 6 productos; el modelo lista algunos y remite a la tienda. **Follow-up de plataforma**: inyectar el chunk completo con tope por chunk en `buildKnowledgeContextBlock` (path compartido con golden test — requiere su propio ciclo de revisión).
- Sin tool de consulta de disponibilidad para unidades `table` (ver decisión 1). Si se quiere "¿qué horas tienen libres el viernes?", la mejora es extender `GetAvailableSlotsTool`/`BuildReservationSlots` a modo capacity — feature aparte.
- El cálculo de slots no es capacity-aware (documentado en `docs/flujo-agendamiento-restaurantes.md`); por eso la creación directa es la fuente de verdad.
- Las 250 conversaciones históricas quedan sin bot (sin backfill, decisión del onboarding).
