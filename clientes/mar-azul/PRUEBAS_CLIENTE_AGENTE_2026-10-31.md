# Pruebas del asistente de WhatsApp — Calamar Azul (sede Cable)

**Para:** Yady (gerente administrativa) y equipo de caja y coordinación · **De:** equipo MY SEO Company
**Fecha:** 2026-10-31 · **Duración estimada:** 15–20 minutos

> **BORRADOR — pendiente de aprobación de Nicolás antes de enviar al establecimiento** (`../../POLICIES.md`: las comunicaciones externas requieren aprobación explícita).

Hola Yady 👋 El asistente de WhatsApp de Calamar Azul ya está configurado con su carta, sus precios, las tarifas de domicilio por barrio y las reglas de reserva — y ya pasó nuestra batería interna de 32 casos. Lo que no podemos probar sin ustedes es el camino real: que un pedido quede **registrado de punta a punta** por WhatsApp y que el pase a la cajera funcione. Esta guía trae los casos clave para que lo prueben haciendo de clientes, con lo que debería responder en cada uno y una tablita para anotar el resultado.

## Antes de empezar

- **El asistente está en modo piloto:** solo responde a los números que nosotros autoricemos. Avísennos **desde qué celular(es) van a escribir** y nosotros los autorizamos y coordinamos el día y la hora. Mientras esté en piloto, ningún cliente real lo ve — es el momento perfecto para probar sin riesgo.
- **Prueben desde un celular diferente a la línea del negocio.** Si escriben desde la línea «Principal - Cable» no verán al asistente.
- **El horario del negocio es todos los días de 11:00 a. m. a 5:00 p. m.** (incluidos festivos). Corran los casos dentro de ese horario; el caso 14 necesita además la franja de reservas (2:00 a 4:30 p. m.).
- **Los pedidos que confirmen quedan registrados de verdad en el sistema** — eso es justo lo que queremos probar. Coordínense con caja para no preparar los de prueba… o aprovechen y almuercen 🐟.
- Dejen que el asistente termine su respuesta antes de escribir de nuevo, y no lo corrijan en el momento: mejor anoten qué pasó y nosotros ajustamos.
- Si prueban barrios aparte de los de esta guía y el valor del domicilio no cuadra con su tabla, anótenlo: hay unos pocos barrios con tarifas duplicadas que estamos depurando.

## Casos con el negocio abierto

Los mensajes entre comillas los pueden copiar y pegar tal cual (o escribirlos a su manera — también queremos ver cómo entiende el lenguaje natural).

### 1. Bienvenida
Escriban: `Hola`
**Debe:** saludar nombrando Calamar Azul y ofrecer mostrar la carta, ayudar con un pedido o una reserva.

### 2. La carta
Escriban: `¿Me envías la carta, por favor?`
**Debe:** presentar la carta vigente, por secciones y en corto. **No debe** inventar platos ni precios, ni enviar un bloque interminable.

### 3. Almuerzo ejecutivo
Escriban: `¿Qué tienen de almuerzo hoy?`
**Debe:** ofrecer el ejecutivo de $26.000 (filete apanado, bagre, mojarra, sierra o trucha, con sopa de pescado, arroz de coco, patacón, ensalada y agua de panela con limón) y dejar las opciones del día para confirmación de caja. **No debe** decir que no hay almuerzo. *(Mientras no publiquemos el menú del día en el sistema, lo cotiza desde la carta.)*

### 4. Tamaño ambiguo
Escriban: `Quiero una cazuela de mariscos`
**Debe:** preguntar si la quieren pequeña ($31.000) o grande ($37.000). **No debe** elegir un tamaño por su cuenta.

### 5. Cambio de acompañamiento
Coticen algo que lleve arroz de coco y luego escriban: `Mejor cambia el arroz de coco por arroz blanco`
**Debe:** anotar el cambio para validación de caja y recotizar. **El total no debe subir** — un cambio no es una adición. Este fue el error más caro de nuestras pruebas internas; con el ajuste actual quedó cerrado, pero vale la pena verificarlo.

### 6. Pedido para recoger
Escriban: `Una sopa de pescado, un arroz marinero pequeño y un ejecutivo con filete apanado para recoger. Lo pago con tarjeta débito en el local.`
**Debe:** resumir los tres ítems con su total ($71.500), **sin** pedir barrio ni cobrar domicilio, y registrar el pago en el local sin decir que ya se realizó.

### 7. Confirmación del pedido
Escriban: `¿Me confirmas que el pedido sí quedó?`
**Debe:** decir que quedó confirmado **solo si** el sistema lo registró; si no, explicar que queda pendiente de caja. Este caso es clave: es el registro de punta a punta que necesitamos documentar — si lo confirman, avísennos.

### 8. Tarifas de domicilio exactas
Pregunten en la misma conversación: `¿Cuánto vale el domicilio a Palermo?` · `¿Hacen domicilio a La Enea y cuánto vale?` · `El barrio es TURIN VILLA MARIA`
**Debe:** responder la tarifa exacta de su tabla: **Palermo $6.000**, **La Enea $13.000** y **Turín Villa María $15.000** (aunque se escriba en mayúsculas y sin tildes). **No debe** estimar ni dar una banda genérica.

### 9. Barrio escrito de otra forma o sin tarifa cargada
Escriban: `Es para Palogrande` y luego: `¿Cuánto vale el domicilio a La Florida?`
**Debe:** con «Palogrande», pedir que precisen el barrio — no elegir una tarifa por parecido. Con La Florida, decir que el equipo confirma el valor y **seguir tomando el pedido**. **No debe** decir «no tenemos cobertura».

### 10. Dirección sin barrio
Escriban: `Es para el edificio Paseo del Bosque, avenida principal`
**Debe:** pedir el barrio. **No debe** poner la cobertura en duda ni quedarse sin responder.

### 11. Tiempo de entrega
Escriban: `¿En cuánto tiempo llega el domicilio?`
**Debe:** pasar el caso a caja. **No debe** inventar minutos ni prometer rapidez.

### 12. Pagos y transferencias (¡la más importante para ustedes!)
Escriban: `¿Me das los datos para transferir por Nequi?`
**Debe:** **no** compartir cuentas, QR ni validar comprobantes: pasar el caso a caja. Esto quedó configurado así a propósito por el historial de comprobantes falsos — el dinero solo se maneja con personas del negocio.

### 13. Efectivo con devuelta
Escriban: `Pago en efectivo; necesito devuelta de 100.000`
**Debe:** conservar la devuelta en el resumen para caja. **No debe** contarla como un pago.

### 14. Reservas (correrlo entre 2:00 y 4:30 p. m.)
Escriban: `Quiero reservar una mesa para cinco personas el sábado a las 3:00 p. m.`
**Debe:** recoger fecha, hora, personas, nombre y ocasión; explicar que las reservas van de lunes a sábado de 2:00 a 4:30 p. m., que la mesa se conserva 30 minutos y que cuesta $20.000 ($30.000 con decoración); pasar la solicitud a la cajera. **Nunca** confirmarla ni cobrarla.
Luego prueben fuera de franja: `¿Puedo reservar hoy para dos personas a la 1:00 p. m.?` → debe explicar la franja y ofrecer atención por orden de llegada o una hora dentro de ella.

### 15. Evento empresarial
Escriban: `Tenemos una comida empresarial para doce personas a las 6:00 p. m. ¿Pueden hacer una excepción?`
**Debe:** reconocer que los eventos se pactan aparte, tomar fecha, personas y ocasión, y pasarlos a la cajera. **No debe** prometer que la excepción se puede ni negarla de plano.

### 16. Queja y seguimiento
Escriban: `El arroz del almuerzo llegó en mal estado`
**Debe:** disculparse brevemente, sin ofrecer compensaciones, y pasar el caso con resumen a la cajera.
Luego: `¿Ya salió mi domicilio?` → debe pasarlo a caja. **No debe** prometer que él mismo va a verificar el estado.

## Tabla de resultados

Marquen ✅ (bien), ⚠️ (pasó pero con algo raro) o ❌ (falló), y una línea de qué pasó:

| # | Caso | ✅ / ⚠️ / ❌ | Qué pasó |
|---|---|---|---|
| 1 | Bienvenida | | |
| 2 | La carta | | |
| 3 | Almuerzo ejecutivo | | |
| 4 | Tamaño ambiguo | | |
| 5 | Cambio de acompañamiento | | |
| 6 | Pedido para recoger | | |
| 7 | Confirmación del pedido | | |
| 8 | Tarifas exactas | | |
| 9 | Barrio raro o sin tarifa | | |
| 10 | Dirección sin barrio | | |
| 11 | Tiempo de entrega | | |
| 12 | Pagos y transferencias | | |
| 13 | Efectivo con devuelta | | |
| 14 | Reservas | | |
| 15 | Evento empresarial | | |
| 16 | Queja y seguimiento | | |

## Cómo devolvernos el resultado

Envíen a Nicolás por WhatsApp la tabla llenada (o una foto) **y capturas de pantalla de las conversaciones** — las capturas son lo más valioso: con ellas vemos exactamente qué respondió el asistente. Si confirmaron un pedido en el caso 6 o 7, avísennos también: ese registro nos sirve de evidencia. Si algún caso no alcanzan a probarlo, no pasa nada: lo marcan como pendiente.

¡Gracias! Con esta vuelta dejamos el asistente listo para recibir a sus clientes de la mejor manera ⚓🐟
