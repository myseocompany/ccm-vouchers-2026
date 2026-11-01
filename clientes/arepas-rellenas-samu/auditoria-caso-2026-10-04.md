# AUDITORÍA DEL CASO AREPAS RELLENAS SAMU — Reporte detallado (verificado en producción)

**Fecha del reporte**: 2026-10-04
**Autor**: MY SEO (agente LLM del harness), a solicitud de Nicolás Navarro Rincón
**Cliente**: Arepas Rellenas Samu (NIT 28956191)
**Tenant AriCRM**: `arepas-rellenas-samu-UK5K` (id `01a0ac93-dc1c-73e6-b872-b2c572070661`)
**Contrato**: CT-239-26-3 (Cámara de Comercio de Manizales por Caldas ↔ MY SEO COMPANY S.A.S.)
**Método**: consultas de solo lectura vía SSH a `waterfall` (`php artisan tinker`), git log del deploy, lectura de código en `velo_wa`, conversaciones WhatsApp compartidas por Nicolás, y evidencia del repo del programa.

---

## 1. Resumen ejecutivo

Arepas Rellenas Samu, uno de los 10 beneficiarios del programa, **se retiró voluntariamente** el 3 de octubre de 2026 tras un incidente durante el piloto del agente conversacional. El incidente tuvo **dos componentes**:

1. **Técnico (responsabilidad de MY SEO)**: el bot calculó precios erróneos, operó fuera del horario del restaurante (tomó pedidos a medianoche con el restaurante cerrado), confirmó pedidos que el restaurante no podía atender, y en conversaciones anteriores envió la carta repetidamente.
2. **Operativo (responsabilidad compartida)**: el restaurante no atendió los pedidos que el bot confirmaba; un cliente esperó ~50 minutos a medianoche antes de recibir respuesta humana.

Los fixes técnicos principales (mimetype, intent detection, pricing determinista) están **deployados en producción**. El `CreateOrderTool` sigue aceptando precios del LLM sin validar contra el catálogo. El establecimiento decidió retirarse a pesar de las correcciones.

---

## 2. Estado verificado en producción (SSH waterfall, 2026-10-04)

### 2.1 Deploy

| Ítem | Valor verificado |
|---|---|
| Release activo | `5499016` — "fix(ai): incluir transcript y URL de media en payload a webhook externo (#28)" |
| Fecha de archivos | 2026-10-04 13:51 (deploy de hoy) |
| P-009 fix en `SendAutomationSequenceStep` | ✅ Presente (líneas 99-102 con `MediaAttributes::guessMimeType`) |
| `OrderPricingService` | ✅ Presente (`app/Services/Pricing/OrderPricingService.php`, 12.313 bytes) |
| `CreateOrderTool` | ❌ **Sigue siendo el viejo** — acepta `price` y `total` del LLM, `resolveTotal` solo suma lo que le mandan, sin referencia a `OrderPricingService` |

### 2.2 Tenant Samu

| Ítem | Valor verificado |
|---|---|
| Agente | "Asistente de domicilios — plantilla" (id `01a0f215-6eb7-7028-8cd2-e5dde36c7eec`) |
| Modelo | **`gpt-4.1-mini`** (upgraded desde gpt-4o-mini) |
| Habilitado | **NO** (desactivado desde 2026-10-03 03:32) |
| Tool calling | SÍ |
| Intención `pedir-menu` | Activa |
| `condition_text` real | **"El cliente manifiesta querer conocer la carta, menú, productos"** |

> **Hallazgo crítico sobre la condición**: la palabra "productos" está explícita en la condición. En una conversación de restaurante, **todo mensaje trata sobre productos** — pedir una arepa, preguntar un precio, enviar el nombre para el pedido. La condición es estructuralmente incapaz de distinguir "muéstrame la carta" de "quiero una arepa de pollo". Es la causa raíz del carta-spam documentado en el incidente del 02/10.

---

## 3. Conversación analizada: `01a0ff15-e42a-705f-9597-f10087dbce4f` (Jhoanna)

**URL**: `https://app.aricrm.co/inbox/01a0ff15-e42a-705f-9597-f10087dbce4f`
**Creada**: 2026-10-03 00:06:59 · **Status**: open

Esta es la conversación donde el cliente esperó ~1 hora. Timeline completo verificado:

### 3.1 Timeline

| Hora | Actor | Evento |
|---|---|---|
| 00:06:56 | CLIENTE | "Hola", "Buenas" |
| 00:06:59 | BOT | Bienvenida (secuencia de automatización, run status: success — **única automatización en esta conversación**) |
| 00:09:01 | CLIENTE | Pide 3 arepas con ingredientes específicos |
| 00:09–00:18 | BOT↔CLIENTE | Refinamiento del pedido (queso, ingredientes, correcciones) — el bot maneja bien el flujo |
| 00:15:27 | BOT | Calcula precios: Arepa 1 $12.000, Arepa 2 $16.000, Arepa 3 $18.000, domicilio Arboleda $5.500, **total $51.500** |
| 00:17:07 | BOT | Resume el pedido y pide confirmación explícita: "¿Confirmas el pedido así para proceder?" |
| 00:18:00 | CLIENTE | "Acuérdate que quiero el queso de la primera arepa en la segunda" |
| 00:18:11 | BOT | Confirma el cambio de queso — **pero NO vuelve a pedir confirmación del pedido** |
| — | **[SILENCIO DE 22 MINUTOS]** | El bot espera confirmación que nunca llega; la cliente cree que su pedido ya está hecho |
| 00:40:28 | CLIENTE | "Hola", "Ya enviaron mi pedido?" |
| 00:40:45 | BOT | "aún no he creado tu pedido porque necesito tu confirmación explícita" |
| 00:40:54 | CLIENTE | "Dios", "Si confirmado", "En eso quedamos no!??" |
| 00:41:16 | SISTEMA | Se crea orden **PED-GUSO61** (total $51.500, status new) |
| 00:41:18 | BOT | "Listo Jhoanna, tu pedido PED-GUSO61 **ya está en proceso**" — **FALSO: el restaurante está cerrado** |
| 00:41:33 | CLIENTE | "**Llevo media hora eso**" |
| 00:42:16 | BOT | "Voy a reportar el retraso de tu pedido" — **no hay evidencia de que alguien fuera notificado** |
| 00:48:11 | CLIENTE | Pregunta otra vez cuándo llega |
| 00:48:23 | BOT | "Ya pasó ese tiempo" — reconoce el retraso sin poder hacer nada |
| 00:49:00 | BOT | "te avisaré apenas tenga novedades" |
| 00:54:50 | HUMANO | Primer mensaje humano (media) — **48 minutos después del inicio de la conversación** |
| 00:55:32 | CLIENTE | "**No podré esperar más**", "Confirmen por favor", "Espero o no" |
| 00:55:52 | HUMANO | "**Serían en total $58.000**" — corrige el precio del bot ($51.500) |
| 00:56:04 | HUMANO | "Si claro ya salió el domi de acá" |
| 00:56:25 | CLIENTE | "Incluido domicilio?" |
| 00:56:30 | HUMANO | "Si" |
| 00:57:58 | CLIENTE | Envía soporte de pago (Nequi) |
| 00:58:30 | CLIENTE | "Gracias" |

### 3.2 Orden creada

```
PED-GUSO61 | status: new | total: $51.500 | creada: 2026-10-03 00:41:16
items:
  - Arepa con pollo, maíz y maduritos sin queso — $12.000
  - Arepa con doble carne, mondongo, plátano maduro y queso — $16.000
  - Arepa con pollo, carne, maíz y maduro con queso — $18.000
notes: Domicilio barrio Arboleda, Tel: 3103778576, Nombre: Jhoanna, Pago: Nequi
```

### 3.3 Análisis de precios

| Arepa | Ingredientes | Precio del bot | Precio catálogo | Correcto? |
|---|---|---|---|---|
| 1 | pollo, maíz, maduritos (3 ing.) | $12.000 | 3 ing. = **$16.000** | ❌ Cobró precio de 1 ingrediente |
| 2 | doble carne, mondongo, plátano, queso | $16.000 | 3 ing. = $16.000 (queso gratis) | ✅ |
| 3 | pollo, carne, maíz, maduro, queso | $18.000 | 4 ing. = $18.000 (queso gratis) | ✅ |
| **Total bot** | | **$51.500** (con domicilio) | | |
| **Total humano** | | **$58.000** (con domicilio) | | **Diferencia: $6.500** |

El bot subcotizó la Arepa 1 en $4.000 (cobró $12.000 por 3 ingredientes). El humano corrigió a $58.000 a medianoche, manualmente.

### 3.4 Detecciones de intención y automatizaciones

- **Detecciones de intención en esta conversación: NINGUNA** — no hubo falsos positivos de `pedir_menu` aquí.
- **Runs de automatización: 1** — la bienvenida (00:06:59, status success). La carta se envió una sola vez, correctamente.

> En esta conversación el carta-spam NO ocurrió. Los problemas aquí fueron: precio erróneo, flujo de confirmación roto, operación fuera de horario, y falta de escalamiento.

### 3.5 Qué funcionó bien

- La bienvenida + carta se envió una vez, correctamente (P-009 fix funcionando)
- El bot siguió el flujo del prompt (ingredientes → dirección → teléfono → nombre → pago)
- Pidió confirmación explícita (paso 7 del prompt)
- 2 de 3 precios correctos
- Tono y formato correctos, sin markdown ni rutas
- Sin falsos positivos de intención

### 3.6 Qué falló

| # | Falla | Causa |
|---|---|---|
| 1 | Arepa 1 subcotizada ($12.000 vs $16.000) | `CreateOrderTool` acepta precios del LLM sin validar contra catálogo |
| 2 | Confirmación perdida → 22 min de silencio | El bot confirmó el cambio de queso pero no re-pidió la confirmación del pedido; la cliente creyó que ya estaba hecho |
| 3 | Bot operando a medianoche | Sin gate de horario; el restaurante cierra a 10:30 PM |
| 4 | "Ya está en proceso" — falso | El bot confirma pedidos sin verificar que el restaurante pueda cumplirlos |
| 5 | "Voy a reportar el retraso" — sin efecto | No hay mecanismo de notificación al restaurante; Adrián apareció 48 min después por su cuenta |
| 6 | Cliente esperó ~50 min | Combinación de 2+3+4+5 |

---

## 4. Hallazgos técnicos consolidados

### 4.1 Fixes deployados (verificados en el servidor)

| Fix | Estado | Evidencia |
|---|---|---|
| P-009: mimetype de medios | ✅ Deployado | `SendAutomationSequenceStep.php` líneas 99-102 |
| Intent detection endurecida (PR #24) | ✅ Deployado | Reglas 1-5 en `AiAgentService::appendIntentContext` |
| `OrderPricingService` (PR #30) | ✅ Deployado | `app/Services/Pricing/` existe (12.313 bytes) |
| Web de pedidos pública | ✅ Deployada | PRs #31, #33 |
| Modelo `gpt-4.1-mini` | ✅ En producción | Agente Samu configurado con él |

### 4.2 Pendientes críticos (verificados como ausentes en producción)

| Pendiente | Impacto | Evidencia |
|---|---|---|
| `CreateOrderTool` wireado a `OrderPricingService` | El bot puede poner precios arbitrarios | Tool sigue con `resolveTotal` que suma lo que el LLM manda |
| Idempotencia de pedidos | Pedidos duplicados | No existe guard en el tool |
| `condition_text` acotada | Carta-spam | Condición actual: "El cliente manifiesta querer conocer la carta, menú, **productos**" |
| Gate de horario | Bot opera con restaurante cerrado | La conversación de Jhoanna es de medianoche |
| Flujo de confirmación por humano | Bot confirma pedidos no atendibles | "Ya está en proceso" a las 00:41 con restaurante cerrado |
| Timeout + notificación al restaurante | Cliente espera indefinidamente | "Voy a reportar el retraso" no notificó a nadie |

---

## 5. Root causes (verificados)

| # | Root cause | Tipo | Fix necesario | Estado |
|---|---|---|---|---|
| RC-1 | `CreateOrderTool` acepta precios del LLM | Código | Wirear `OrderPricingService` | ❌ Pendiente |
| RC-2 | Sin idempotencia de pedidos | Código | Guard de 1 orden activa por conv. | ❌ Pendiente |
| RC-3 | `condition_text` incluye "productos" | Configuración | Acotar a "pide explícitamente la carta" | ❌ Pendiente |
| RC-4 | Sin gate de horario | Código/Config | Bot inactivo fuera de horario | ❌ Pendiente |
| RC-5 | Bot confirma sin validación del restaurante | Código/Design | Confirmación por humano | ❌ Pendiente |
| RC-6 | Sin timeout/notificación | Código | Timeout + alerta al restaurante | ❌ Pendiente |
| RC-7 | Flujo de confirmación se pierde en correcciones | Prompt/Design | Re-pedir confirmación tras cada cambio | ❌ Pendiente |
| RC-8 | Mimetype de medios | Código | `MediaAttributes` | ✅ Corregido |
| RC-9 | Intent detection sin reglas de frontera | Código | Reglas 1-5 inyectadas | ✅ Corregido (parcial: RC-3 sigue abierto) |

---

## 6. Timeline general del caso

| Fecha | Evento | Fuente |
|---|---|---|
| 2026-09-30 | Caracterización completada | `evidencias/.../caracterizacion-2026-09-30.md` |
| 2026-09-30 ~16:00 UTC | Piloto activado en línea real San Jorge | `PROGRESS.md` |
| 2026-09-30 20:15–02:16 | Bot atiende conversaciones reales: 8 conv, 6 pedidos, 19 detecciones, 25 runs | Diagnóstico 02/10 |
| 2026-10-02 | Diagnóstico del incidente (SSH producción) | `incidentes/2026-10-02-diagnostico-pedidos-cartas.md` |
| 2026-10-02 20:08 | Adrián pide desactivar el bot | WhatsApp |
| 2026-10-03 00:06–00:58 | **Conversación Jhoanna**: pedido a medianoche, cliente espera ~50 min, humano corrige precio | Producción (este reporte) |
| 2026-10-03 03:32 | Bot desactivado | WhatsApp |
| 2026-10-03 15:28 | PR #30: pricing determinista mergeado | git log |
| 2026-10-03 15:54 | Adrián: "estamos evaluando si continuamos o no" | WhatsApp |
| 2026-10-03 16:24 | Adrián: "yo creo que podemos dejar ahí" — retiro voluntario | WhatsApp |
| 2026-10-03 | Sandra (Cámara): "sumamente importante que eso no vuelva a suceder" | WhatsApp |
| 2026-10-04 13:51 | Deploy con P-009 fix + OrderPricingService + web de pedidos | SSH waterfall |

> **Nota**: la conversación de Jhoanna (00:06–00:58 del 3/10) ocurrió **después** de que Adrián pidiera desactivar el bot (20:08 del 2/10) y **antes** de la desactivación efectiva (03:32). El bot siguió operando ~7 horas con el restaurante cerrado tras la solicitud de desactivación.

---

## 7. Entregables producidos para el establecimiento

| Entregable | Estado | Evidencia |
|---|---|---|
| Caracterización completa | ✅ Entregada | `evidencias/.../caracterizacion-2026-09-30.md` |
| Página web de pedidos (pricing determinista) | ✅ Deployada | PRs #31, #33 |
| Carta personalizada San Jorge | ✅ Entregada | `evidencias/.../carta-san-jorge-2026-10-03.jpeg` |
| Carta personalizada Chipre | ✅ Entregada | `evidencias/.../carta-chipre-2026-09-30.png` |
| Mini manual de marca | ✅ Entregado | `evidencias/.../estrategia_de_marca.jpeg` |
| Stickers de WhatsApp | ✅ Entregados | `evidencias/.../assets/sticker-*.png` |
| Prompt de producción limpio | ✅ Instalado | `prompt-san-jorge-prod-v1.md` |
| Tarifas de domicilio estructuradas | ✅ Entregadas | `tarifas-san-jorge-2026-09-30.json` |
| Logo + favicon | ✅ Entregados | `media/`, `favicon_io/` |
| Catálogo Instagram | ✅ Recopilado | `instagram/` |

---

## 8. Recomendaciones para los 9 beneficiarios restantes

### 8.1 Fixes de código (hacen los bugs imposibles por construcción)

1. **Wirear `OrderPricingService` en `CreateOrderTool`** (RC-1) — el bot no puede poner precios; solo el catálogo.
2. **Idempotencia de pedidos** (RC-2) — 1 orden activa por conversación.
3. **Gate de horario** (RC-4) — el bot no opera fuera del horario del restaurante.
4. **Confirmación por humano** (RC-5) — el bot toma datos, notifica al restaurante, el restaurante confirma, entonces el bot dice "confirmado".
5. **Timeout** (RC-6) — si el restaurante no confirma en X minutos, el bot avisa al cliente con el número directo.

### 8.2 Fix de configuración

6. **Acotar `condition_text`** (RC-3) — de "El cliente manifiesta querer conocer la carta, menú, productos" a "el cliente pide explícitamente que le envíen o muestren la carta completa (ej: 'me pasas la carta', 'muéstrame el menú'). No incluye preguntas sobre productos específicos, precios, ingredientes ni armado de pedido."

### 8.3 Fix de prompt

7. **Re-confirmación tras cambios** (RC-7) — si el cliente corrige algo después del resumen, el bot debe re-presentar el resumen y re-pedir confirmación.

### 8.4 Proceso

8. **Rollout escalonado**: Fase 1 bot solo envía carta → Fase 2 bot toma pedidos (tras N días estable).
9. **Aprobación del empresario** antes de activar en línea real.
10. **Pruebas desde teléfono controlado** antes de línea real.
11. **Monitoreo las primeras horas** de operación live con el empresario presente.

### 8.5 No recomendado

- **Shadow mode ahora**: los fixes de código hacen los bugs imposibles; el shadow mode detecta, no previene. Considerarlo post-rollout como herramienta de monitoreo.
- **Exoneración upfront para los 9**: asusta y señala desconfianza en el producto.
- **Cooldown en reglas V2**: si RC-3 se fixa, el cooldown es redundante.

---

## 9. Estado contractual y comunicaciones

- **Retiro**: voluntario, 2026-10-03 16:24.
- **Cupos**: Mar Azul (Yady Milena) cubre el cupo 10 que faltaba. El retiro de Samu abre un cupo adicional.
- **Cámara informada**: Sandra Obando notificada vía WhatsApp; solicitó garantías de no repetición.
- **Borradores pendientes de envío** (requieren aprobación de Nicolás):
  - `borrador-correo-camara-2026-10-03.md` — correo formal
  - `borrador-exoneracion-2026-10-04.md` — acuerdo de exoneración (recomendado simplificar a acta de retiro)

---

## 10. Tareas derivadas

| ID | Descripción | Tipo | Estado |
|---|---|---|---|
| P-009 | Fix mimetype secuencias V2 | Código | ✅ Corregido y deployado |
| P-010 | Guardas anti-repetición reglas V2 | Código | ❌ No registrada en `TASKS.md` |
| P-011 | Endurecer `create_order`: total server-side, idempotencia, validación catálogo | Código | ❌ No registrada |
| P-012 | Gate de horario del bot | Código | ❌ No registrada |
| P-013 | Confirmación de pedido por humano + timeout | Código | ❌ No registrada |
| P-014 | Re-confirmación tras correcciones en el prompt | Prompt | ❌ No registrada |
| INC-02 | Acotar `condition_text` de `pedir_menu` | Configuración | ❌ Pendiente |

> P-010 a P-014 no existen en `TASKS.md` global. Hay que crearlas.

---

*Reporte generado el 2026-10-04 con verificación directa en producción (SSH waterfall, solo lectura). Todas las consultas fueron no destructivas: `git log`, `grep` de archivos, y `SELECT` vía tinker sobre `conversations`, `messages`, `orders`, `ai_intent_detections`, `automation_runs`, `ai_agents`, `ai_intents`.*
