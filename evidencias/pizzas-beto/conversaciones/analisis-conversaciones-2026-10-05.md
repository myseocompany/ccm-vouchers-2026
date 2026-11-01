# Análisis de conversaciones — Beto's Pizza

- **Fuente**: `evidencias/pizzas-beto/conversaciones/raw/waterfall-conversaciones-2026-10-05.json` (exportación Waterfall 2026-10-05T12:37:26+00:00), 6355 mensajes de 363 conversaciones.
- **Rango observado**: 2026-09-21 19:33:13 → 2026-10-05 12:28:29 (timestamps en hora local del tenant, supuesto documentado).
- **Ventana de atención aplicada**: 08:00–22:00 todos los días (atención WhatsApp reportada por el establecimiento); las esperas fuera de ventana no acumulan tiempo.
- **Respuesta automática descontada**: mensajes out que casan con las plantillas «Gracias por comunicarte…» (tarifario) y «En este momento no podemos responder…». El export marca `is_automated=false` en todos los out, por eso se detectan por contenido.
- **Privacidad**: identificadores anónimos; textos de clientes redactados. El detalle con IDs reales queda solo en el directorio local `raw/` (fuera de git).
- **Advertencia**: los umbrales de «oportunidad perdida» son heurística de análisis, no una confirmación comercial; una conversación puede retomarse días después.

## 1. Oportunidades perdidas por no contestar a tiempo

- Conversaciones con mensajes del cliente: **362** de 363.
- **Silencio total** (el cliente escribió y no hubo NINGUNA respuesta, ni automática): **8** conversaciones.
- **Solo respondió la máquina** (hubo autorrespuesta pero ningún humano tomó la conversación en todo el export): **20** conversaciones.
- Turnos del cliente (ráfagas de mensajes entrantes): **1938** totales; 1737 observados con ventana completa (se excluyen 201 de las últimas 24 h del export por censura).
- **Turnos sin respuesta humana** en lo restante del export: **150** (9% de los observados). Clasificación de esos turnos:
  - **Con pedido real en el texto** (dirección/barrio, sabor o tamaño concretos, pago o pedido explícito): **6** → **oportunidades comerciales probables**. Horario: 02:54 del 27-09, 03:08 del 27-09, 03:31 del 29-09, 18:06 del 03-10, 02:35 del 04-10, 03:06 del 04-10.
  - Solo despedida/cortesía o archivo sin texto (no son oportunidades): **62**.
  - Saludos o consultas sin intención clara de pedido: **82**.
- **Turnos atendidos tarde** (primera respuesta humana > 60 min de atención): **30**.
- Turnos atendidos entre 15 y 60 min: **35**; atendidos ≤ 15 min: **1522**.
- Conversaciones con ≥1 turno sin respuesta humana: `conv-051`×3, `conv-052`×2, `conv-080`×2, `conv-161`×2, `conv-162`×2, `conv-291`×2, `conv-323`×2, `conv-324`×2, `conv-325`×2, `conv-001`×1, `conv-006`×1, `conv-008`×1, `conv-010`×1, `conv-014`×1, `conv-015`×1…
- Hora (local) de los turnos sin respuesta: 00:00→18, 01:00→14, 02:00→14, 03:00→8, 04:00→5, 05:00→1, 06:00→1, 08:00→1, 10:00→1, 16:00→4, 17:00→3, 18:00→6, 19:00→4, 20:00→7, 21:00→7, 22:00→18, 23:00→38

## 2. Tiempo hasta la primera respuesta humana

- Conversaciones tomadas por un humano: **334** de 362 con mensajes del cliente (92%).
- En **283** de ellas la primera respuesta fue la autorrespuesta (ya descontada: se mide hasta el primer humano).
- Mediana de toma: **0 min** · p75 0 min · p90 3 min · peor caso 88.4 h.
- Distribución del tiempo de toma (minutos de atención):

| Rango | Conversaciones | % |
|---|---:|---:|
| ≤ 1 min | 267 | 80% |
| 1–5 min | 43 | 13% |
| 5–15 min | 10 | 3% |
| 15–30 min | 1 | 0% |
| 30–60 min | 2 | 1% |
| 1–4 h | 7 | 2% |
| > 4 h | 4 | 1% |

Las 20 tomas más lentas (anónimas):

| Conv | Primera toma humana |
|---|---:|
| `conv-098` | 88.4 h |
| `conv-082` | 30.0 h |
| `conv-260` | 28.0 h |
| `conv-022` | 12.4 h |
| `conv-204` | 2.4 h |
| `conv-003` | 2.2 h |
| `conv-262` | 1.9 h |
| `conv-263` | 1.8 h |
| `conv-071` | 1.4 h |
| `conv-105` | 1.4 h |
| `conv-095` | 1.2 h |
| `conv-023` | 56 min |
| `conv-219` | 45 min |
| `conv-030` | 21 min |
| `conv-024` | 10 min |
| `conv-329` | 8 min |
| `conv-074` | 8 min |
| `conv-293` | 7 min |
| `conv-241` | 7 min |
| `conv-336` | 6 min |

- Conversaciones donde NINGÚN humano respondió jamás: **28** (no entran a la distribución; ver sección 1).

## 3. Qué debe aclarar el menú (preguntas de los clientes)

- Mensajes entrantes analizados: 3019; turnos con pregunta explícita o implícita: **331**.

| Tema | Preguntas | % | ¿Lo responde la autorrespuesta? | ¿Lo resuelve la carta? |
|---|---:|---:|---|---|
| Otras preguntas | 125 | 38% | **no** | **no** |
| Tamaños y porciones | 50 | 15% | sí | sí |
| Tiempo de entrega / demora | 44 | 13% | **no** | **no** |
| Métodos de pago | 28 | 8% | **no** | **no** |
| Cobertura de domicilio / zonas | 27 | 8% | **no** | **no** |
| Sabores, ingredientes y disponibilidad | 21 | 6% | sí | sí |
| Precios de productos | 11 | 3% | sí | sí |
| Factura electrónica | 6 | 2% | **no** | **no** |
| Ubicación de la sede / recogida | 6 | 2% | **no** | **no** |
| Estado del pedido (¿dónde va?, ¿ya salió?) | 6 | 2% | **no** | **no** |
| Horario de atención | 4 | 1% | **no** | **no** |
| Solicitud de menú/carta | 3 | 1% | sí | sí |

Ejemplos redactados por tema (máx. 3):

**Tamaños y porciones**
- «Me das una porción de pizza porfa Carnes Y que gaseosas toenes?»
- «Se puede mitad y mitad carnes hawaiana Para una. Familiar»
- «Una pizza S de carnes Carrera #22 16-20 hotel escala Isabella [tel] De 40mil En recepción Que bebidas personales tienes?»

**Tiempo de entrega / demora**
- «cuanto se demora?»
- «1 hawaiana familiar 1 de carnes familiar [dirección] Barrio la palma Argemiro Orozco [tel] Devuelta de 170mil Las gaseosas familiares deben ser Pepsi normal Cuánto tiempo se demora?»
- «Cuanto tiempo se demora mas o menos m Muchas gracias»

**Métodos de pago**
- «No tienen datáfono? Está caído Bancolombia»
- «Pizza familiar [dirección] El palmar Jaír García [tel] Para pagar por transferencia se puede?»
- «Y te puedo pagar por transferencia?»

**Cobertura de domicilio / zonas**
- «Desde qué horas está abierto el seguro, y que vale un domicilio hasta el sena?»
- «Pizza hawaiana familiar [dirección], Barrio las colinas parte baja Jerónimo [tel] Te puedo pagar por transferencia?»
- «Por favor una familiar mitad carne y mitad hawaiana [dirección] Barrio Palermo Adriana parra [tel] Tienes Nequi o llave?»

**Sabores, ingredientes y disponibilidad**
- «Te hago una pregunta se puede mitad de un sabor y mitad de otro ?»
- «Puede ser de varios sabores?»
- «Que sabores tienes»

**Precios de productos**
- «Cuanto es?»
- «Si cuánto vale ? Ok viene con gaseosa ?»
- «Q precio tienen las lasagñas?»

**Factura electrónica**
- «Tienes factura electrónica?»
- «una pregunta y que pena, entregan la factura cierto? pues, que tipo de factura manejan ustedes?»
- «Buenos días, hoy nos haces llegar la factura?»

**Ubicación de la sede / recogida**
- «Dónde queda el local porfa para recoger el pedido»
- «Donde se encuentra ubicado el punto que quedaba en la Santander al frente de la católica? O ya esta funcionando?»
- «En donde? Me podrías dar la dirección porfa»

**Estado del pedido (¿dónde va?, ¿ya salió?)**
- «Para recordarte el pedido Ya salió ? Son 205 mil»
- «Dale ya te envío Oye una pregunta Ya salió el domi?»
- «Dale de una Muchas gracias!! Ya salió el carro?»

**Horario de atención**
- «🙏🏼 Gracias Hola, tienen servicio hoy ? Si es así, Hasta qué hora? Gracias»
- «Ustedes ah que horas abren mañana?»
- «Más o menos a qué hora podemos estar pendientes para esperarlas?»

**Solicitud de menú/carta**
- «me compartes la carta?»
- «Hola tienen el menu del parque caldas ?»
- «Buenas tardes cómo estás? Me podrías regalar porfavor información de la carta, muchas gracias»

## 4. Conversaciones etiquetadas para auditoría

Cada conversación del export quedó etiquetada en `raw/analisis/conversaciones-etiquetadas.json` (con IDs reales, solo local) para filtrar y escoger casos a auditar con el método forense por conversación. Distribución agregada:

| Etiqueta | Conversaciones |
|---|---:|
| `toma_rapida` | 310 |
| `actividad_nocturna` | 255 |
| `turno_sin_respuesta` | 140 |
| `pregunta:otro` | 84 |
| `pregunta:tamanos` | 46 |
| `censurada_reciente` | 44 |
| `pregunta:tiempo_entrega` | 44 |
| `pregunta:pago` | 26 |
| `sin_toma_humana` | 26 |
| `pregunta:cobertura` | 24 |
| `pregunta:sabores_disp` | 21 |
| `solo_autorrespuesta` | 18 |
| `toma_tardia` | 11 |
| `pregunta:precios` | 11 |
| `silencio_total` | 8 |
| `pregunta:ubicacion` | 6 |
| `pedido_abandonado` | 6 |
| `pregunta:estado_pedido` | 6 |
| `pregunta:factura` | 5 |
| `pregunta:horario` | 4 |
| `pregunta:menu` | 3 |

Definiciones de las etiquetas en el propio JSON (`definicion_etiquetas`).

---
_Generado por `scripts/analisis_conversaciones.py`; heurística e inferencias sujetas a validación con el establecimiento._
