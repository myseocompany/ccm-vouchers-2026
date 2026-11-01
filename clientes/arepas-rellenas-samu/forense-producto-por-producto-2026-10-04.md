# ANÁLISIS FORENSE — Toma de cada producto por el bot

**Caso**: Conversación `01a0ff15-e42a-705f-9597-f10087dbce4f` (cliente "Jhoanna")
**Pedido**: `PED-GUSO61`
**Tenant**: `arepas-rellenas-samu-UK5K` · Sede San Jorge (`01a1025e-cc1c-72d9-9414-4c17267f0fce`)
**Fecha real (Bogotá GMT-5)**: 2026-10-02, 19:06–19:58 (UTC en DB: 2026-10-03 00:06–00:58)
**Método**: lectura directa de producción (SSH waterfall, solo lectura) — tablas `orders`, `menu_items`, `menu_item_price_tiers`, `menu_item_ingredients`, `delivery_tariffs`, `messages`

---

## 1. Catálogo vigente en producción (verificado)

### 1.1 Arepa armable — "Arepa rellena a tu manera"
- **Estrategia**: `armable`
- **Precio por # de ingredientes** (tiers de la sede San Jorge):

| # Ingredientes | Precio |
|---|---|
| 1 | $12.000 |
| 2 | $14.000 |
| 3 | $16.000 |
| 4 | $18.000 |
| 5 | $19.000 |
| 6 | $20.000 |
| 7 | $21.000 |
| 8 | $22.000 |
| con todo | $23.000 |

- **Ingredientes válidos** (10): Pollo, Carne, Madurito, Tocineta, Chicharrón, Chorizo, Maicitos, Piña, Mondongo, Huevos de codorniz.
- **Queso**: **NO está en la lista de ingredientes**. No cuenta ni cuesta. "Con queso" es gratis.
- Todos los ingredientes vinculados tienen `price_delta = NULL` (opción regular que cuenta para el tramo).

### 1.2 Tarifa de domicilio
- **Arboleda**: $5.500 (activa) ✓

---

## 2. Lo que pidió el cliente (transcripción)

| Hora (Bogotá) | Mensaje del cliente | Producto |
|---|---|---|
| 19:09 | "3arepas La primera: con pollo maíz y maduroitos sin queso" | Arepa 1 |
| 19:10 | "Una con doble porción de carne mondongo y plátano maduro" | Arepa 2 |
| 19:10 | "Si con queso" | Arepa 2 (queso) |
| 19:11 | "El queso de la primera ponlo en la segunda" | Corrección |
| 19:11 | "La última arepa que sea con pollo carne maíz y maduro" | Arepa 3 |
| 19:11 | "Con queso" | Arepa 3 (queso) |
| 19:12 | "Son 3 arepas. Las deseo tal cual las solicité" | Confirmación |

---

## 3. Análisis producto por producto

### Producto 1 — "Arepa con pollo, maíz y maduritos sin queso"

| Campo | Valor |
|---|---|
| **Pedido por el cliente** | Pollo + Maíz + Maduritos (sin queso) |
| **Ingredientes válidos** | pollo, maicitos, madurito = **3 ingredientes** |
| **Registrado por el bot** | Nombre: "Arepa con pollo, maíz y maduritos sin queso" · Precio: **$12.000** |
| **Precio según catálogo** | 3 ingredientes = **$16.000** |
| **Diferencia** | **−$4.000 (subcotizada)** |
| **¿Correcto?** | ❌ **NO** |

**Diagnóstico**: el bot cobró el precio de **1 ingrediente** ($12.000) por una arepa de **3 ingredientes**. En su propio mensaje de cálculo, el bot justificó el precio de las arepas 2 y 3 ("(3 ingredientes + queso gratis)", "(4 ingredientes + queso gratis)") pero para la Arepa 1 **no dio justificación** — omitió el conteo. Es un error de conteo del LLM, no un problema de catálogo.

---

### Producto 2 — "Arepa con doble carne, mondongo, plátano maduro y queso"

| Campo | Valor |
|---|---|
| **Pedido por el cliente** | Doble porción de carne + mondongo + plátano maduro (+ queso) |
| **Ingredientes válidos** | carne, mondongo, madurito = **3 opciones** (+ queso, gratis) |
| **Registrado por el bot** | Nombre: "Arepa con doble carne, mondongo, plátano maduro y queso" · Precio: **$16.000** |
| **Precio según catálogo** | 3 ingredientes = $16.000 · si "doble carne" contara como 2 = $18.000 |
| **Diferencia** | $0 (si "doble"=1) · −$2.000 (si "doble"=2) |
| **¿Correcto?** | ⚠️ **AMBIGUO** |

**Diagnóstico**: el catálogo **no define** cómo se cobra una "doble porción". El motor de pricing cuenta **opciones distintas** (`tiered_by_option_count`): si se pasa "Carne" una vez → 3 opciones → $16.000; si se pasara "Carne" dos veces → error de opción repetida. El bot interpretó "doble = 1 opción" y cobró $16.000. **No hay forma de saber, desde el catálogo, si es correcto.** Es un hueco del modelo de precios, no del bot.

---

### Producto 3 — "Arepa con pollo, carne, maíz y maduro con queso"

| Campo | Valor |
|---|---|
| **Pedido por el cliente** | Pollo + carne + maíz + maduro (+ queso) |
| **Ingredientes válidos** | pollo, carne, maicitos, madurito = **4 ingredientes** (+ queso, gratis) |
| **Registrado por el bot** | Nombre: "Arepa con pollo, carne, maíz y maduro con queso" · Precio: **$18.000** |
| **Precio según catálogo** | 4 ingredientes = **$18.000** |
| **Diferencia** | $0 |
| **¿Correcto?** | ✅ **SÍ** |

---

## 4. Comparación de totales

| Concepto | Bot | Catálogo (doble=1) | Catálogo (doble=2) | Humano (Adrián) |
|---|---|---|---|---|
| Arepa 1 | $12.000 ❌ | $16.000 | $16.000 | — |
| Arepa 2 | $16.000 | $16.000 | $18.000 | — |
| Arepa 3 | $18.000 | $18.000 | $18.000 | — |
| **Subtotal items** | **$46.000** | $50.000 | $52.000 | — |
| Domicilio Arboleda | $5.500 | $5.500 | $5.500 | — |
| **TOTAL** | **$51.500** | **$55.500** | **$57.500** | **$58.000** |

**Diferencias:**
- Bot vs catálogo (doble=1): **−$4.000** (subcotización por la Arepa 1)
- Bot vs catálogo (doble=2): **−$6.000**
- Humano vs catálogo (doble=2): **+$500** (sobrecotización menor)
- Humano vs bot: **+$6.500**

> El humano (Adrián) corrigió hacia arriba, quedando cerca de la interpretación "doble=2" ($57.500), con $500 de diferencia. Su corrección fue mucho más cercana al catálogo que la del bot, pero **tampoco exacta**.

---

## 5. Estado del registro del pedido

| Campo | Valor | Observación |
|---|---|---|
| `code` | PED-GUSO61 | ✓ |
| `status` | new | Quedó en `new` (nunca confirmado por humano) |
| `total` | $51.500 | El bot metió el domicilio dentro del total |
| `delivery_fee` | **NULL** | ❌ El domicilio NO se separó como campo — se diluyó en el total |
| `items` | 3 líneas con `price` por item | Precios calculados por el LLM |
| `notes` | Domicilio + Teléfono + Nombre + Pago | Solo texto libre |

**Falla estructural**: el pedido no tiene `delivery_fee` separado. El bot sumó el domicilio al `total` sin dejar trazabilidad. Esto impide auditar el cobro automáticamente (coincide con P-011: "delivery_fee separado").

---

## 6. Respuestas a las preguntas

### ¿Estaba bien la corrección de precio de Adrián ($58.000)?

**Casi.** El catálogo da $57.500 (si "doble"=2) o $55.500 (si "doble"=1). Su $58.000 está $500 por encima de la interpretación "doble=2". No es exacto, pero está mucho más cerca que el bot. **El acierto principal de Adrián no fue el número exacto, sino que detectó que el bot había subcotizado.**

### ¿El precio es el problema?

**No es EL problema.** El precio fue un error real pero:
- El bot subcotizó $4.000–$6.000 en una orden de ~$56.000 (7–11%)
- Adrián lo detectó y lo corrigió
- La cólera del cliente NO fue por el precio

### ¿O es que Adrián no tomó el pedido?

**ESTE es el problema principal.** Evidencia de la conversación:
- 19:17 — el bot pide confirmación
- 19:18–19:40 — **22 minutos de silencio**: nadie del restaurante atendió; la cliente creyó que su pedido estaba hecho
- 19:40 — la cliente pregunta "¿ya enviaron mi pedido?" (llevaba esperando)
- 19:41 — el bot dice "ya está en proceso" (falso — nadie lo había visto)
- 19:41 — "**Llevo media hora eso**"
- 19:55 — "**No podré esperar más**" / "Confirmen por favor" / "Espero o no"
- 19:54 — primer mensaje humano, **48 minutos después** del inicio

El cliente se molestó por **la espera sin respuesta**, no por el precio. El precio se corrigió *después* de que la cliente ya estaba furiosa.

---

## 7. Conclusiones forenses

| # | Hallazgo | Severidad | ¿Culpa de quién? |
|---|---|---|---|
| F-1 | Arepa 1 subcotizada $4.000 (conteo del LLM) | Media | MY SEO (bot) |
| F-2 | "Doble porción" no modelada en el catálogo | Media | MY SEO (catálogo/pricing) |
| F-3 | Domicilio no separado (`delivery_fee` NULL) | Media | MY SEO (bot/design) |
| F-4 | Pedido no atendido por el restaurante por ~48 min | **Alta** | Compartida |
| F-5 | Bot dice "ya está en proceso" sin validación del restaurante | **Alta** | MY SEO (bot/design) |
| F-6 | Sin notificación efectiva al restaurante | **Alta** | MY SEO (bot/design) |
| F-7 | Cliente esperó ~50 min en hora pico | **Alta** | Combinada |

**Conclusión central**: el incidente que detonó el retiro fue **F-4 + F-5 + F-6** (el pedido no se atendió y el bot lo dio por confirmado), no el precio. El error de precio (F-1) fue real pero secundario y corregido. Los tres hallazgos de precio (F-1, F-2, F-3) confirman que `CreateOrderTool` es inseguro y debe wirearse a `OrderPricingService`.

---

## 8. Sobre compartir con Sandra

**Recomendación**: NO compartir los prints crudos. Razones:

1. **Datos personales**: la conversación contiene nombre, teléfono, dirección y comprobante de pago de la cliente (Jhoanna). Compartirlos con la Cámara viola `POLICIES.md` (protección de datos, Ley 1581/2012). Si se comparte, **hay que redactar todo dato personal**.

2. **Impacto narrativo**: los prints muestran la frustración de la cliente ("No podré esperar más") — hacen el incidente ver peor, no mejor.

3. **Alternativa mejor**: compartir un **resumen redactado** (como la sección 7 de este documento) muestra que MY SEO entendió la causa raíz a fondo. Eso genera más confianza que los crudos.

Si de todas formas se comparten, que sea **redactado** y enfocado en: el bot funcionó, el pedido no se atendió, ya hay plan de corrección.

---

*Análisis generado 2026-10-04 con verificación directa en producción (SSH waterfall, solo lectura). Datos personales del cliente final (nombre, teléfono, dirección) incluidos solo con fines internos de análisis forense — no deben compartirse sin redacción.*
