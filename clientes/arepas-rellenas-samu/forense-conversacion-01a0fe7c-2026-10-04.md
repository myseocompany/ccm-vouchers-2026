# AUDITORÍA FORENSE — Conversación `01a0fe7c-1072-7199-9af0-cec2b091602c`

**Cliente del programa**: Arepas Rellenas Samu (tenant `arepas-rellenas-samu-UK5K`)
**Cliente final (contacto)**: Leidy Catherine — `153622423851092@lid`
**Línea**: `01a0ac98-f82d-7181-ab1f-d99d5503e705` (label "Principal", Evolution, instancia `line_01a0ac98f82d`, hoy **disconnected**)
**Pedido**: `PED-G9YUCN`
**Fecha real (Bogotá GMT-5)**: 2026-10-02, 16:18–17:59 (UTC en DB: 21:18–22:59)
**Método**: lectura directa de producción (SSH waterfall, solo lectura) — `conversations`, `messages`, `orders`, `ai_intent_detections`, `automation_runs`, `delivery_tariffs`, `whatsapp_lines`

---

## 1. Resumen

Segunda conversación con problema operativo el mismo día del incidente. A diferencia del caso Jhoanna, **el bot cotizó CORRECTAMENTE** ($19.000 × 2 arepas + $7.000 domicilio = $45.000). El problema aquí fue el mismo patrón: el pedido se confirmó al cliente pero **nadie del restaurante lo atendió**, la cliente esperó ~1.5 horas, y el bot no pudo ayudarla con el estado del envío.

Al final, un humano tomó la conversación y le dijo a la clienta: **"estamos probando un bot de respuesta automática"**.

---

## 2. Timeline (hora Bogotá GMT-5)

| Hora | Actor | Mensaje |
|---|---|---|
| 16:18:53 | CLIENTE | "Buena tarde" |
| 16:18:58 | BOT | Bienvenida (run de automatización, status success) |
| 16:23:17 | CLIENTE | "Carne .mondongo.choti" |
| 16:23:27 | BOT | Confirma ingredientes, pregunta cuántas |
| 16:25:01 | CLIENTE | "Carne mondongo chorizo maduritos maicitos" (5 ingredientes) |
| 16:25:40 | CLIENTE | "Dos arepas" |
| 16:26:34 | CLIENTE | "Cuánto sería" / "San Sebastián" |
| **16:26:52** | BOT | **"Las dos arepas con 5 ingredientes cada una quedan en $19.000 cada una, es decir $38.000 en total"** ✅ |
| 16:28:05 | CLIENTE | "X nexi" (pago) |
| 16:28:22 | CLIENTE | "San Sebastián torre 31 apto 2134" |
| 16:28:36 | CLIENTE | "3118119795" |
| 16:28:53 | CLIENTE | "Torre 21 apto 2134" (corrección) |
| 16:29:14 | CLIENTE | "Si" |
| **16:29:26** | BOT | **"Pedido confirmado, Soi. Tu código es PED-G9YUCN. En breve estarás disfrutando..."** |
| — | **[ESPERA ~45 MIN]** | — |
| 17:14:53 | CLIENTE | "Buena tardes" |
| 17:15:10 | CLIENTE | "Ya salieron las arepa6" |
| 17:15:22 | BOT | "No tengo la información en este momento sobre el estado de envíos previos" |
| 17:16:33 | CLIENTE | "PED-aG9YUCN" (código con typo) |
| 17:18:53 | CLIENTE | "Gracias" |
| 17:19:07 | BOT | "Lamento que no tenga acceso directo para consultar el estado actual del pedido" |
| 17:19:38 | CLIENTE | "**X favor ya llevo una ho[ra]**" |
| 17:19:51 | BOT | "He informado la situación... **Adrián te contactará pronto**" |
| 17:38:12 | CLIENTE | "Hola" |
| 17:38:55 | CLIENTE | "Nececito saber si ya salieron" / "Con mi domicilio" |
| 17:39:10 | BOT | "Lamentablemente yo no puedo confirmar el estado del envío" |
| 17:39:35 | BOT | "ya le informé a Adrián para que se comunique contigo" |
| 17:39:52 | BOT | "De nada, ¡para eso estamos! ... ¡Hasta pronto! 😊" |
| 17:49:06 | CLIENTE | "Buenas" / [media] |
| 17:49:19 | BOT | "Hola, ¿qué tal? ¿Quieres hacer un pedido o necesitas algo más?" |
| **17:56:58** | **HUMANO** | **"Hola buenas tardes, disculpa, es que estamos probando un bot de respuesta automática"** |
| 17:58:54 | HUMANO | "Dale te entiendo perfectamente" |
| 17:59:14 | HUMANO | "Mil disculpas de verdad" |
| 17:59:49 | HUMANO | "Esperamos servirte en otra oportunidad con mayor celeridad" |

`ai_pause_reason`: `human_phone_takeover` (el humano tomó la conversación al responder)

---

## 3. Análisis del pedido `PED-G9YUCN`

```
PED-G9YUCN | status: new | total: $45.000 | delivery_fee: NULL | creada: 16:29:25 Bogotá
items: [{"name":"Arepa rellena con carne, mondongo, chorizo, maduritos y maicitos","qty":2,"price":19000}]
```

### 3.1 Precios — ¡CORRECTOS!

| Concepto | Valor | Catálogo | ¿Correcto? |
|---|---|---|---|
| Arepa (5 ingredientes: carne, mondongo, chorizo, maduritos, maicitos) | $19.000 c/u | 5 ing. = $19.000 | ✅ |
| 2 arepas | $38.000 | $19.000 × 2 | ✅ |
| Domicilio San Sebastián | $7.000 | San Sebastian = $7.000 | ✅ |
| **Total** | **$45.000** | **$45.000** | ✅ |

**Contraste con el caso Jhoanna**: allí el bot cobró mal la Arepa 1 ($12.000 por 3 ingredientes). Aquí, con 5 ingredientes, cotizó correcto ($19.000). Esto confirma que el error de pricing es **inconsistente** — típico de un LLM haciendo aritmética: a veces acierta, a veces no. Refuerza la necesidad del pricing determinista.

### 3.2 Falla estructural repetida

- `delivery_fee` = **NULL** otra vez. El domicilio ($7.000) se diluyó dentro del `total` ($45.000), sin campo separado. Mismo problema que en `PED-GUSO61`.

---

## 4. Comportamiento del bot

| Aspecto | Evaluación |
|---|---|
| Toma del pedido | ✅ Completa y correcta (ingredientes, cantidad, dirección, teléfono, pago) |
| Precio | ✅ Correcto esta vez |
| Confirmación | ⚠️ Confirmó el pedido al cliente ("Pedido confirmado, PED-G9YUCN") sin que el restaurante lo viera |
| Manejo de estado del pedido | ❌ No pudo consultar el estado ("no tengo la información", "no tengo acceso directo", "no puedo confirmar el estado del envío") |
| Escalamiento | ⚠️ Dijo "Adrián te contactará pronto" / "ya le informé a Adrián" — pero **nadie contactó a la clienta** |
| Tono | ⚠️ Siguió alegre ("¡Hasta pronto! 😊") mientras la clienta llevaba 1 hora esperando |

**Falla clave**: el bot prometió **dos veces** que "Adrián te contactará" sin ningún mecanismo que garantizara el contacto. La clienta esperó ~1.5 horas.

---

## 5. Intenciones y automatizaciones

- **Detecciones de intención: NINGUNA** — sin carta-spam.
- **Runs de automatización: 1** — bienvenida (16:18:58, success).

> Igual que en Jhoanna: en esta conversación el carta-spam NO ocurrió. Las reglas de detección no dispararon falsos positivos. El problema fue 100% operativo (pedido no atendido + bot sin manejo de estado).

---

## 6. Hallazgo crítico — Admisión del humano

A las **17:56**, un humano le dijo a la clienta:

> "Hola buenas tardes, disculpa, es que **estamos probando un bot de respuesta automática**"

Esto significa una de dos:
1. **Era un cliente real** y el restaurante le admitió que estaba probando un bot → malísima imagen, y confirma que el bot estaba en la línea real **en fase de prueba**.
2. **Era una persona conocida** (amigo/ayudante) probando el bot en la línea real → igualmente confirma que la línea de producción se usó como banco de pruebas con conversaciones que parecen reales (pedido, dirección, pago).

En cualquier caso: **el bot se usó en la línea real mientras "se estaba probando"**. Esto respalda la hipótesis de que no hubo un aislamiento entre prueba y producción.

---

## 7. Comparación con el caso Jhoanna (`01a0ff15`)

| | Leidy Catherine (`01a0fe7c`) | Jhoanna (`01a0ff15`) |
|---|---|---|
| Fecha/hora (Bogotá) | Oct 2, 16:18–17:59 | Oct 2, 19:06–19:58 |
| Línea | Principal (San Jorge) | Principal (San Jorge) |
| Bot cotizó | ✅ Correcto ($45.000) | ❌ Arepa 1 mal ($4.000 abajo) |
| Carta-spam | No | No |
| Pedido confirmado al cliente | Sí | Sí |
| Espera del cliente | ~1.5 h | ~50 min |
| Bot manejó estado | No | Parcial (dijo "ya pasó ese tiempo") |
| Humano respondió | 17:56 (~1.5 h) | 19:54 (~48 min) |
| Humano corrigió precio | No (no hacía falta) | Sí ($51.500 → $58.000) |
| `delivery_fee` separado | ❌ NULL | ❌ NULL |

**Patrón**: dos conversaciones, misma línea, mismo día, mismo problema operativo (pedido no atendido, cliente espera, bot no escala de verdad). Pero pricing inconsistente (una mal, una bien).

---

## 8. Conclusiones

| # | Hallazgo | Severidad | Responsabilidad |
|---|---|---|---|
| 1 | Pedido confirmado al cliente sin que el restaurante lo atendiera | **Alta** | MY SEO (diseño del bot) |
| 2 | Cliente esperó ~1.5 h | **Alta** | Compartida |
| 3 | Bot no maneja estado de pedidos (no puede decir si salió) | Alta | MY SEO (capacidad faltante) |
| 4 | Bot promete "Adrián te contactará" sin mecanismo real | **Alta** | MY SEO (diseño) |
| 5 | `delivery_fee` no separado del total | Media | MY SEO |
| 6 | Humano admitió a la clienta "estamos probando un bot" | Media | MY SEO / operación |
| 7 | Pricing fue CORRECTO en esta conversación | — | (evidencia de inconsistencia del LLM) |
| 8 | Sin carta-spam ni falsos positivos de intención en esta conversación | — | (las reglas endurecidas funcionaron aquí) |

**Conclusión central**: el problema del piloto **no fue principalmente de precio ni de carta** — fue que **el bot tomaba y confirmaba pedidos que el restaurante no atendía**, y no tenía forma de gestionar el estado ni de escalar de verdad. El precio mal calculado (Jhoanna) fue un problema real pero secundario e inconsistente.

---

## 9. Para el reporte a la Cámara

Este caso **confirma** que:
- El problema operativo (pedido no atendido) fue **sistemático**, no un caso aislado → dos conversaciones la misma tarde.
- El humano admitió que "estaba probando un bot" → el bot se usó en producción en fase de prueba.
- **No conviene compartir los prints crudos** — contiene datos personales (nombre, dirección, teléfono) y muestra la admisión "estamos probando un bot", que es peor para la narrativa.

---

*Reporte generado 2026-10-04 con verificación directa en producción (SSH waterfall, solo lectura). Datos personales del cliente final incluidos solo con fines internos. No compartir sin redacción.*
