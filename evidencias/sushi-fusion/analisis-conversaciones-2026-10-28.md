# Análisis de conversaciones — Sushi Fusion (Mercado Gastronómico Fusión)

Fuente: `mensajes-sushi-2026-10-20.csv` (export del tenant `01a140b0-1dd9-7012-b03a-80cc84eb76f3`).
Insumo para redactar el prompt del agente de IA. Análisis realizado 2026-10-28 sobre el corpus del 15–20 oct 2026.

## 0. Tamaño y naturaleza del corpus

- 1.278 mensajes · 76 conversaciones · 55 contactos · rango 15–20 oct (6 días).
- **100% de los mensajes son `is_automated = f`** (ninguno del bot): el agente entró en *modo escucha* el 20 oct y aún no responde. Por eso este corpus retrata **el playbook humano**, que es justo lo que queremos clonar.
- Media de ~17 mensajes/conversación. Media types: 1.013 texto, 134 imagen, 58 audio, 40 documento (PDF de cartas), 28 sticker, 5 video.

**⚠️ Hallazgo crítico — la línea es mixta.** Varias de las conversaciones más largas NO son atención a cliente, sino **operación interna**: coordinación con "Ana" y "Mauro" (dueño/gerente), turnos del personal, adelantos de nómina, pagos a proveedores (Postobón, Bancolombia), avisos de Rappi, cuadres de caja. El agente de IA **debe atender solo el flujo cara-a-cliente** (pedido / reserva / información) y **no intervenir** en hilos internos. Hay que definir cómo distingue un hilo interno (p. ej. contactos conocidos del equipo / palabras como "turno", "adelanto", "cuadre", "Mauro").

## 1. El flujo de pedido (playbook humano observado)

Secuencia típica y muy consistente (conversaciones 2, 4, 6, 7):

1. **Saludo automático**: «Gracias por comunicarte con Mercado Gastronómico Fusión. ¿Cómo podemos ayudarte?» (aparece 37x, es su mensaje de bienvenida actual).
2. **Saludo personalizado**: «Hola {nombre} buenas noches, ¿cómo estás?» + «¿En qué te podemos servir?». Tono cálido, usa el nombre, emojis 😊😉🥳, "con mucho gusto" como muletilla constante.
3. **Envío de cartas**: ante "quiero sushi" / "promociones" envían **imagen + PDF**. Por defecto arrancan con **SUSHI FUSIÓN** y **SUSHI HOUSE** (combos). Si el cliente pide "las otras cartas", envían las 6: SUSHI FUSIÓN, SUSHI HOUSE, INCA FUSIÓN, LEMON FISH, **KRABBIES**, **RICE TO GO**.
4. **Asesoría / upsell**:
   - Recomiendan el más vendido: «El Mozarella Crunch es el que más vendemos».
   - Describen ingredientes y **nº de bocados**; ajustan a nº de personas («es para una persona» → sugieren roll de 10 bocados).
   - Upsell de combo: «🥳 SUSHI HOUSE — Agranda tu Combo por $20.000 adicionales y lleva 10 bocados más».
   - Upsell de bebida: «¿Deseas alguna bebida?».
5. **Dirección**: «Me compartes la dirección de entrega por favor» y, clave para el costo, «**¿Cuál es el barrio?**».
6. **Total**: «Permíteme un momento te confirmo el valor total» → «El valor total de tu pedido es **$X incluyendo el domicilio**».
7. **Medio de pago**: «¿Deseas cancelar en **efectivo o transferencia**?».
8. **Datos de pago**: envían **imagen** con QR / llave / cuenta Bancolombia. Para **tarjeta de crédito** generan **link de pago** (accivalconnect.com) — paso manual.
9. **Comprobante antes de cocina**: «Cuando tengas el comprobante de pago me lo envías por favor **para enviar tu pedido a preparación**». Verifican la transferencia manualmente (en conv. 4 el cliente mandó un comprobante borrado y tocó re-verificar).
10. **Cierre y post-venta**: stickers, «me avisas cuando salga», y manejo de incidencias («el domi no ha llegado» → «el domiciliario está allá pero nos dice que no le abren»).

## 2. Preguntas / intenciones más frecuentes (sobre 546 mensajes entrantes)

| Intención | Frecuencia aprox. |
|---|---|
| Agradecimientos / cierre ("gracias", "listo", "vale") | 95 |
| Saludo | 52 |
| Pago (efectivo/transferencia/llave/QR/tarjeta) | 47 |
| Precio / "¿cuánto vale?" | 28 |
| Sushi / rolls / makis | 20 |
| Domicilio / "¿tienen envío?" | 16 |
| "Quiero / para pedir" | 10 |
| Arroz / chaufa / tepán / thai | 10 |
| Pide carta/menú | 8 |
| Dirección / barrio | 7 |
| Reserva / mesa / cumpleaños | 5 |
| Ceviche | 3 |

Lectura: el grueso es **pedido a domicilio de sushi**, con el **precio** y el **medio de pago** como los dos puntos que más fricción generan (y los que hoy resuelve el humano confirmando total + enviando datos de pago).

## 3. Qué podría automatizar el agente vs. qué debe escalar

**Automatizable (replica directa del playbook):**
- Saludo personalizado + pregunta de apertura.
- Envío de cartas (las 6 PDF) y recomendación de best-sellers / combos.
- Asesoría por componentes (tipo de plato → ¿mariscos? → proteína → preparación/sabor) y upsell (agrandar combo, bebida).
- Captura de datos: nombre, dirección, **barrio**, teléfono, medio de pago.
- Informar horarios; fuera de horario, enviar cartas y ofrecer pedido programado.

**Debe escalar / confirmar humano (visto en el corpus):**
- **Cálculo del valor total con domicilio**: hoy depende del barrio contra la tabla de tarifas y a veces lo "confirma" el humano. El bot necesitará la tabla; mientras tanto, escala.
- **Verificación del comprobante de pago** antes de mandar a cocina (paso humano explícito).
- **Pago con tarjeta de crédito**: generación del link accivalconnect (manual).
- **Barrio ambiguo / fuera de cobertura**: nunca decir "no despacho" en seco → comunicar/escalar.
- **Incidencias**: "no llegó", cobro doble, quejas, cambios.
- **Hilos internos/operativos** (Ana, Mauro, turnos, proveedores): el bot no debe responderlos.

## 4. Tono de marca a replicar

Cálido y cercano, tratamiento por el nombre, "con mucho gusto" como firma, emojis moderados (😊😉🥳🍱🥢), mezcla tú/usted según el cliente. Nunca cortante; siempre ofrece asesoría ("quedamos atentos a lo que necesites o si requieres alguna asesoría").

## 5. Respuestas a dudas abiertas del proyecto

- **Krabbies y Rice To Go**: aparecen como **cartas vigentes** — el negocio las envía junto a las demás y los clientes piden sus productos (p. ej. "krabtacon criollo", "perrushi", "Rice Perú Chaufa Familiar"). → Actualizar la ficha: no son 4 marcas sino **6 cartas** (pendiente confirmar jerarquía marca/sub-marca con el establecimiento). *(La transcripción de cartas la está haciendo un subagente en paralelo.)*
- **Nombre público**: operan de cara al cliente como **"Mercado Gastronómico Fusión"** (así se presentan), no "Sushi Fusion" a secas.

## 6. Limitaciones de este análisis

- Ventana corta (6 días) y sin ejemplos del bot respondiendo (no hay `is_automated = t`).
- Teléfonos/direcciones de clientes no se reproducen aquí (PII). El corpus crudo queda en el CSV de evidencia.
- **Recomendado**: refrescar el export (15–28 oct) para ~duplicar la muestra y capturar, si el agente ya empezó a responder, su comportamiento actual.
