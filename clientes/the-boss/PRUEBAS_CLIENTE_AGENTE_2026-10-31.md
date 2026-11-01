# Pruebas del asistente de WhatsApp — The Boss Burger

**Para:** Diego (propietario) y Paola (mesera) · **De:** equipo MY SEO Company
**Fecha:** 2026-10-31 · **Duración estimada:** 15–20 minutos

> **BORRADOR — pendiente de aprobación de Nicolás antes de enviar al establecimiento** (`../../POLICIES.md`: las comunicaciones externas requieren aprobación explícita).

Hola Diego 👋 Con el asistente ya atendiendo pedidos por WhatsApp queremos que ustedes lo prueben desde el otro lado: haciendo de clientes. Esta guía trae los casos más importantes, qué debería responder el bot en cada uno y una tablita para anotar el resultado. Con eso afinamos lo que falte.

## Antes de empezar

- **Prueben desde un celular diferente a la línea del negocio.** La línea «Principal» está conectada al sistema; si escriben desde ella misma, no verán al bot.
- **Son dos momentos:**
  1. **Con el negocio abierto** (mar–jue 6–10 p. m. · vie–dom 5–10 p. m.): casos 1 a 13.
  2. **Con el negocio cerrado** (lunes, o cualquier día antes de abrir): caso 14.
- **Ojo con los pedidos:** si confirman un pedido, queda registrado como real. Coordínense con quien esté en caja para ignorar los de prueba… o aprovechen y almuercen 🍔.
- Dejen que el bot termine su respuesta antes de escribir de nuevo, y no lo corrijan en el momento: mejor anoten qué pasó y nosotros ajustamos.
- **No es falla** que al escribir «Hola» el bot envíe la bienvenida con la carta: esa bienvenida es automática y así quedó configurada.

## Casos con el negocio abierto

Los mensajes entre comillas los pueden copiar y pegar tal cual (o escribirlos a su manera — también queremos ver cómo entiende el lenguaje natural).

### 1. Bienvenida y carta
Escriban: `Hola`
**Debe:** saludar como The Boss y mostrar la carta; ofrecer tomar el pedido.

### 2. Pedido a domicilio
Escriban: `Quiero una La Cucha a domicilio`
**Debe:** preguntar el barrio, cotizar el total (hamburguesa + domicilio de la zona) y pedir confirmación. **No debe** dar un total antes de saber el barrio.

### 3. Barrios con nombre completo o raro
Cuando pregunte el barrio, respondan: `La Sultana, conjunto Los Pinos` y en otra conversación: `Alta Leonora`. Prueben también decir solo `Centro`.
**Debe:** reconocer el barrio y cotizar el domicilio de esa zona. **No debe** decir «no tenemos cobertura» — esos barrios sí tienen tarifa. Con «Centro» debe cotizar directo, sin preguntar «Centro 1 o Centro 2».

### 4. Dirección sin barrio (el caso que reportaste)
Escriban: `Vivo en la Carrera 35 #16-22`
**Debe:** preguntar el barrio. **No debe** negar la cobertura ni inventar la tarifa.

### 5. Combo
Escriban: `Una Big Boss en combo`
**Debe:** cobrar la hamburguesa más los $9.000 del combo (papas + gaseosa) y preguntar cuál gaseosa. **No debe** cobrar una «Adición de Papa» aparte ni agregar cosas que nadie pidió.

### 6. Promoción que manejan las asesoras
Escriban: `Me dijeron que tienen La Bandida en 24.900`
**Debe:** decir que lo confirma con el equipo. **No debe** negar que existe ni inventar precios.

### 7. Pago por transferencia
Al llegar al pago, elijan: `Transferencia`
**Debe:** enviar los datos de Nequi/Daviplata y pedir el comprobante por el chat. **No debe** dar el pedido por pagado antes de que el equipo valide.

### 8. Efectivo con devuelta
Elijan: `Efectivo` y cuando pregunte: `Con 50.000`
**Debe:** calcular la devuelta sobre el total cotizado. (Con transferencia **no** debe preguntar con cuánto pagan.)

### 9. Recogida en el local
En una conversación nueva: `Hola, voy a recoger una orden en el local`
**Debe:** armar el pedido sin cobrar domicilio y sin pedir barrio, y confirmar la dirección de la sede (Cra. 19 #74A-12).

### 10. Reservas
Escriban: `¿Tienen reservas para el viernes?`
**Debe:** decir con toda amabilidad que no aceptan reservas y ofrecer domicilio o recogida.

### 11. Tiempo de espera
Escriban: `¿Cuánto se demora el domicilio?`
**Debe:** decir que la preparación toma como 10 minutos. **No debe** prometer hora de llegada (el transporte lo maneja Flash Delivery).

### 12. Queja
Escriban: `Me llegó fría la hamburguesa del último pedido`
**Debe:** responder en tono serio y respetuoso, sin emojis festivos, y pasar el caso a una persona del negocio.

### 13. Hablar con una persona
Escriban: `Quiero hablar con alguien del negocio`
**Debe:** pasar la conversación a una persona (o dar el contacto del responsable).

## Caso con el negocio cerrado

### 14. Pedido fuera de horario
Un lunes (o entre semana antes de las 6 p. m.), escriban: `Quiero una Queen a domicilio`
**Debe:** avisar que están cerrados y decir cuándo abren (ese día a las 5:00/6:00 p. m., o el próximo día de servicio). **No debe** cotizar ni pedir confirmación del pedido.

## Tabla de resultados

Marquen ✅ (bien), ⚠️ (pasó pero con algo raro) o ❌ (falló), y una línea de qué pasó:

| # | Caso | ✅ / ⚠️ / ❌ | Qué pasó |
|---|---|---|---|
| 1 | Bienvenida y carta | | |
| 2 | Pedido a domicilio | | |
| 3 | Barrios raros / Centro | | |
| 4 | Dirección sin barrio | | |
| 5 | Combo | | |
| 6 | Promoción de asesoras | | |
| 7 | Transferencia | | |
| 8 | Efectivo con devuelta | | |
| 9 | Recogida en el local | | |
| 10 | Reservas | | |
| 11 | Tiempo de espera | | |
| 12 | Queja | | |
| 13 | Hablar con una persona | | |
| 14 | Fuera de horario | | |

## Cómo devolvernos el resultado

Envíen a Nicolás por WhatsApp la tabla llenada (o una foto) **y capturas de pantalla de las conversaciones** — las capturas son lo más valioso: con ellas vemos exactamente qué respondió el bot. Si algún caso no alcanzan a probarlo, no pasa nada: lo marcan como pendiente.

¡Gracias! Con esta mano volvemos y dejamos el asistente fino 🍔🔥
