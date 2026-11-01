# Hallazgos — conversación de prueba 2026-10-29 (Sushi Fusion)

Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)<br>
Agente: `01a18263-c04e-73c3-95a4-d3395049c907`, prompt `v12-cartas-pdf-2026-10-28` (SHA-256 `536cbf86…78ce9`)<br>
Conversación: `01a18462-7479-72fc-ab0f-f507adce6fb3` — remitente controlado My SEO Company (`+57 300 441 0097`, línea `line_56e08751ac91`) → línea Sushi `573188069542` (Evolution)<br>
Ventana revisada: 2026-10-29 08:02–10:11 UTC<br>
Casos nuevos en el guion: SU-34 a SU-41 (`ccm-vouchers-2026/evidencias/sushi-fusion/ia-conversacional/MENSAJES_PRUEBA_2026-10-28.md`, sección J).

## Lo que funcionó

- **Cartas en PDF de punta a punta.** «tienes la carta rice to go?» (08:02) → `record_detected_intent` `pedir_todas_cartas` → 4 PDFs `delivered`. «me pasas la carta en PDF?» (10:06) → `pedir_carta` → texto + *Carta Sushi Fusión 2026.pdf* + *Carta The Sushi House 2026.pdf*, `delivered` a las 10:09–10:10. Los archivos salen del media disk (S3) con el nombre del manifiesto.
- El robot ya no dice «no puedo enviarte la carta».

## Errores

### E1 — `quote_order` con un id de producto inventado, presentado como «producto no encontrado» (crítico)

**Qué pasó.** En el turno «Agrégalo» (09:29) el robot consultó `get_catalog` y cotizó bien. En el turno siguiente, «Finaliza» (09:30), volvió a llamar `quote_order` **sin consultar el catálogo** y con un `menu_item_id` que no existe. Respondió «No encuentro el Rice del Campo en el catálogo». Lo mismo pasó con el Perú Chaufa: cotizó bien en el turno «Chaufa» (09:35) y falló en el turno «Así» (09:36). Terminó en handoff (09:38) por un pedido válido.

**Evidencia** (`laravel.log` de la release `81499058`; ids verificados en `menu_items`):

| Hora UTC | Turno | Tool | Resultado |
|---|---|---|---|
| 09:29:25 / 09:29:28 | «Agrégalo» | `get_catalog` → `quote_order` | ok (664 B) |
| 09:30:39 | «Finaliza» | `quote_order` (sin `get_catalog`) | `OPTION_NOT_IN_CATALOG`: «El ítem "f7c6690b-3637-4809-8868-ad3fd4165824" no existe en el catálogo del tenant» |
| 09:35:29 / 09:35:31 | «Chaufa» | `get_catalog` → `quote_order` | ok (662 B) |
| 09:36:39 | «Así» | `quote_order` (sin `get_catalog`) | `OPTION_NOT_IN_CATALOG`: ítem "a7c39738-1afd-42e9-8c53-1dd63ca139ed" |

Ninguno de los dos UUID existe en `menu_items` (de ningún tenant): el modelo los inventó. Los productos reales sí cotizan: `Rice del Campo` + `Té Hatsu caliente` → $55.000 (reproducido en solo lectura).

**Causa.** Entre turnos, el historial conserva el texto de las respuestas pero no los resultados de las tools. En el turno siguiente el modelo ya no tiene los ids reales, no vuelve a consultar el catálogo y reconstruye un UUID de memoria. Después interpreta el error como que el producto no existe.

**Domicilio.** No se consultó en ningún momento: `get_delivery_fee` no se llamó en toda la conversación. El cliente solo escribió «Domi» (08:14) y nunca dio un barrio, aunque el robot lo pidió a las 09:29 y a las 09:35. Las cuatro llamadas a `quote_order` traen la clave `barrio`, pero el log no registra su valor. Los errores no fueron de zona.

**Corrección propuesta.**

- Prompt (v13): consultar `get_catalog` en el mismo turno antes de cada `quote_order`, y no reutilizar ids de turnos anteriores. Ante `OPTION_NOT_IN_CATALOG`, volver a consultar el catálogo y reintentar una vez antes de decir algo al cliente; nunca decir que un producto que ya cotizó no existe.
- Código (a evaluar): que `quote_order` acepte el nombre del producto como respaldo o que el error sugiera volver a llamar `get_catalog`; o conservar los resultados de las tools entre turnos.

**Nota de diagnóstico.** La primera versión de este documento atribuía el fallo a `ZONE_UNRESOLVED`. Fue una inferencia por tamaño de respuesta (224 B), sin ver el `error_code`. El log, que tras el deploy de las 10:15 vive en la release anterior, muestra `OPTION_NOT_IN_CATALOG`. La prueba de `ZONE_UNRESOLVED` sigue siendo válida como riesgo (un barrio no resoluble tumba toda la cotización), pero no ocurrió en esta conversación.

### E2 — Rice To Go sin tamaños en el catálogo (alto)

**Qué pasó.** El robot nunca preguntó el tamaño del arroz. `quote_order` cotiza el Rice del Campo a $39.000.

**Evidencia.** En producción, los ítems de Rice To Go tienen los precios pegados al nombre y un solo precio: `Rice del Campo | $75.000 | $65.000` (unit_price 39.000) y `Perú Chaufa | $92.000 | $82.000`. El catálogo validado (`catalogo-skus-v1.md`, RG-ARR-02) define tres tamaños: Familiar $75.000 · Media $65.000 · Personal $39.000. El reporte de conflictos ya pedía cargar cada arroz «con selector de tamaño» (`conflictos-cartas-2026-10-28.md`, punto 9); no se aplicó.

**Riesgo.** Un arroz familiar puede cotizarse a precio personal, y el cliente ve nombres con precios.

**Corrección propuesta.** Limpiar los nombres de Rice To Go y cargar los tres tamaños como modificador obligatorio con su precio. En el prompt, preguntar el tamaño antes de cotizar.

### E3 — «Más pedidos» inventados (medio)

**Qué pasó.** A «El más pedido» (08:12) el robot respondió que los más pedidos de Rice To Go «suelen ser» Chicken Rice, Rice del Campo y Perú Chaufa.

**Evidencia.** El único best-seller validado es *Mozzarella Crunch* (Sushi Fusión, `catalogo-skus-v1.md` SF-ESG-02, guion SU-03). Para Rice To Go no hay ninguno validado.

**Corrección propuesta.** En el prompt: presentar como «más pedido» solo productos validados; si no hay, asesorar por gustos (proteína, tamaño, personas).

### E4 — Confirmaciones contradictorias (medio)

**Qué pasó.** «¡Listo! Agregué a tu pedido el Rice del Campo…» (09:29) antes de una cotización exitosa; luego «no puedo confirmarlo» (09:30); luego lo listó como disponible (09:31) y reconoció la confusión (09:33). Con el Chaufa, «Te confirmo que puedo armar tu pedido» (09:35) y luego «no aparece en el catálogo» (09:36).

**Causa.** Deriva de E1 (ids inventados entre turnos). El robot afirma que el producto está en el pedido antes de que `quote_order` lo confirme.

**Corrección propuesta.** En el prompt: solo decir «agregué» o «te confirmo» después de un `quote_order` ok en ese turno.

### E5 — Mensaje doble al compartir la carta (bajo)

**Qué pasó.** A las 10:07 llegaron dos textos: el del robot («aquí te comparto la carta en PDF…») y el paso de texto de la automatización («¡Con gusto! Te comparto nuestras cartas 🍣»).

**Corrección propuesta.** Quitar el paso `text` de las automatizaciones en el manifiesto y volver a provisionar (el robot ya anuncia el envío).

### E6 — Intención por marca envía cuatro cartas (bajo)

**Qué pasó.** «tienes la carta rice to go?» envió Inca Fusión, Krabbies, Lemon Fish y Rice To Go.

**Causa.** Diseño del manifiesto v1: `pedir_todas_cartas` agrupa «todas» y «una marca específica».

**Corrección propuesta.** Una intención y una automatización por marca (`pedir_carta_rice_to_go`, …) en el manifiesto.

### E7 — «Todas las cartas» envía solo cuatro (bajo)

**Qué pasó.** Por diseño, `pedir_todas_cartas` envía las 4 restantes, pensando en un cliente que ya recibió las 2 por defecto. Si el cliente pide «todas» de entrada, recibe 4 de 6.

**Corrección propuesta.** Separar «todas» (6 PDFs) de «las otras» (4 PDFs), o hacer que «todas» envíe siempre las 6.

### E8 — Orden de llegada mezclado (observación)

La respuesta del robot llegó intercalada entre los PDFs, y el espaciado anti-baneo retrasó el último PDF unos 3 minutos (`ai_safety.token_consumed`, `final_delay_seconds` 194). Es el comportamiento esperado del safety. Se documenta para que el operador no lo lea como falla.

## Notas de la prueba

- A las 10:09 y 10:10 UTC entraron en la misma conversación mensajes «PRUEBA VELOCIDAD CONTROLADA» que no forman parte de esta ronda. Hay otra prueba en curso con el mismo remitente; conviene separar las conversaciones para no mezclar evidencias.
- Los agentes de My SEO Company (MAIA Piloto, MAIA 3) están deshabilitados, así que no hay riesgo de bucle robot↔robot.

## Prioridad

1. E1 (prompt v13: catálogo antes de cada cotización; evaluar cambio en `quote_order` o en el historial de tools).
2. E2 (catálogo Rice To Go con tamaños).
3. E3, E4 (prompt v13).
4. E5, E6, E7 (manifiesto v2 + reprovisión).
- Los logs no son compartidos entre releases: tras el deploy `d2e674c` (10:15 UTC) las trazas de la mañana quedaron en `releases/81499058/storage/logs/laravel.log`.
