# Calamar Azul — preguntas para la dueña

**Fecha:** 30 de octubre de 2026
**Para qué:** son los datos que el asistente de WhatsApp todavía no puede responder solo. Mientras no estén definidos, el bot escala esos casos a caja (no inventa), pero cada uno es una respuesta que la cajera tiene que dar a mano.

Está ordenado por impacto: las primeras son las que más veces aparecen en las conversaciones reales.

---

## 1. Domicilios

### 1.1 Tres barrios tienen dos precios distintos

En la lista que nos pasaron, estos tres barrios aparecen en dos comunas con precio diferente. Pasa en **las dos sedes**, así que no parece un error de digitación sino un barrio que queda en el límite entre dos comunas.

| Barrio | Sede Cable | Sede Centro |
|---|---|---|
| Arenillo | $10.000 o $8.000 | $5.000 o $6.500 |
| La Castellana | $8.000 o $7.500 | $6.500 o $8.000 |
| Santos | $7.500 o $8.000 | $8.500 o $7.500 |

**Necesitamos:** el precio correcto de cada uno, por sede. Si de verdad son dos sectores distintos (por ejemplo "Santos" arriba y "Santos" abajo), díganos cómo los distingue el domiciliario y los cargamos con nombres separados.

**Hoy:** si un cliente pide domicilio a esos barrios, el bot dice que el equipo le confirma el valor y pasa el caso a caja.

### 1.2 La Floresta no tiene precio

En la lista de la sede Centro, La Floresta aparece en el grupo de barrios apartados pero **sin valor**. En la lista de Cable no aparece.

**Necesitamos:** el precio de La Floresta en Centro, y si también se hace domicilio allá desde Cable.

### 1.3 ¿Hasta dónde llega Villamaría?

La información dice que la cobertura es "Manizales y Villamaría", pero en la tabla de barrios el único de Villamaría es **Turín Villa María ($15.000)**.

**Necesitamos:** si se hacen domicilios a otros barrios de Villamaría y con qué valor, o si Turín es el único.

### 1.4 ¿Cómo escribe la gente los barrios?

El sistema reconoce el barrio aunque el cliente escriba sin tildes o en mayúsculas. Lo que **no** reconoce son los apodos o las formas pegadas. Por ejemplo:

- "Palogrande" (pegado) no lo reconoce; "Palo Grande" sí.
- "Enea" sola no lo reconoce; "La Enea" sí.

**Necesitamos:** la lista de formas en que los clientes nombran los barrios en la práctica, para cargarlas como equivalencias. Esto quita trabajo a caja de inmediato.

### 1.5 ¿Cuánto se demora un domicilio?

Hoy el bot **nunca** promete tiempos: cuando preguntan "¿en cuánto llega?", pasa el caso a caja. Es la pregunta más frecuente después del precio.

**Necesitamos:** si existe un rango que el bot pueda decir con seguridad (por ejemplo "entre 40 y 60 minutos"), o si prefieren que siga escalando siempre.

---

## 2. Reservas

Lo que tenemos entendido hoy, para que lo confirmen o corrijan:

| Regla | Lo que entendimos |
|---|---|
| Días | Lunes a sábado |
| Franja | 2:00 p. m. a 4:30 p. m. |
| La mesa se guarda | 30 minutos |
| Costo | $20.000, y $30.000 con decoración |
| No se reserva | Fechas especiales como el Día de la Madre |
| Eventos empresariales | Sí se pactan en otros horarios |

**Preguntas concretas:**

1. **¿Los domingos no se reserva?** El restaurante abre domingos y festivos de 11:00 a. m. a 5:00 p. m., pero las reservas quedaron de lunes a sábado. ¿Es correcto?
2. **¿El bot puede decir el precio de la reserva?** Hoy está configurado para informar los $20.000 / $30.000 y aclarar que caja confirma. Si prefieren que no mencione cifras y solo pase el caso, lo cambiamos.
3. **¿Cuáles son todas las fechas especiales?** Tenemos solo el Día de la Madre. ¿Día del Padre, Amor y Amistad, 31 de diciembre, otras?
4. **Eventos empresariales:** ¿en qué horarios sí se pueden? ¿Hay mínimo de personas? ¿Cobran anticipo o un valor distinto?

---

## 3. Almuerzo ejecutivo y carta

### 3.1 ¿Se va a publicar el menú del día en el sistema?

Esta es la más importante de esta sección. El bot está configurado para **consultar el menú del día en el sistema** cada vez que alguien pregunta "¿qué hay de almuerzo hoy?". Si nadie lo publica ese día, el bot no puede responder y escala a caja.

**Necesitamos:** quién publica el menú del día y a qué hora. Es de las preguntas más repetidas en las conversaciones.

### 3.2 ¿Los precios de la carta están al día?

En el sistema hay **92 platos cargados**. Necesitamos que alguien del negocio confirme que los precios y los tamaños están vigentes, porque el bot los cita tal cual y no los recalcula.

### 3.3 Fotos de los platos

Ninguno de los 92 platos tiene foto cargada. Si nos pasan fotos, el bot puede enviarlas cuando el cliente pregunte por un plato.

---

## 4. Operación

### 4.1 ¿Quién recibe los casos que el bot pasa a un humano?

El bot escala a "la cajera en turno", pero **no hay ninguna persona configurada** en el sistema para recibirlos. Teníamos anotado que sería **Viviana** como cajera principal.

**Necesitamos:** nombre y correo de quien recibe las escalaciones, para crearle su usuario. Sin esto, los casos escalados no le llegan a nadie en particular.

### 4.2 ¿La sede Centro está operando?

Ya cargamos las tarifas de domicilio de las dos sedes. La sede Centro está creada pero **apagada**, porque hoy el asistente está escrito para una sola sede.

**Necesitamos saber:**

1. ¿La sede Centro ya recibe pedidos por WhatsApp?
2. ¿Es el **mismo número** de WhatsApp para las dos sedes, o cada sede tiene el suyo?
3. Si es el mismo número, el bot tendrá que **preguntarle al cliente a qué sede pide**, porque el precio del domicilio cambia bastante entre sedes (a Chipre son $10.000 desde Cable y $5.000 desde Centro).

### 4.3 Pagos — confirmar

Lo que entendimos:

- Se recibe efectivo, tarjeta débito/crédito **en el local**, Nequi y QR.
- **En domicilio no hay datáfono.**
- El bot **no** envía cuentas, QR ni confirma comprobantes: eso lo hace caja.

¿Es correcto? ¿Hay algún medio de pago nuevo?

### 4.4 Horario — confirmar

- Atención: lunes a domingo, **incluidos festivos**, de 11:00 a. m. a 5:00 p. m.
- Domicilios: se pueden programar antes de abrir, se despachan desde las 11:00 a. m. y se reciben pedidos **hasta las 4:30 p. m.**

¿Es correcto? ¿Hay días de cierre o horarios especiales que el bot deba saber?

---

## Resumen de lo que bloquea qué

| Pregunta | Qué se desbloquea al responderla |
|---|---|
| 1.1 Arenillo, La Castellana, Santos | 6 tarifas (3 por sede) que hoy escalan a caja |
| 1.2 La Floresta | 1 o 2 tarifas más |
| 1.4 Formas de nombrar barrios | Menos escalaciones por domicilio, efecto inmediato |
| 3.1 Menú del día | Que el bot responda la pregunta más frecuente |
| 4.1 Cajera receptora | Que las escalaciones lleguen a una persona concreta |
| 4.2 Sede Centro | Activar la segunda sede en el asistente |

Las demás son confirmaciones: si están bien como las entendimos, basta con decir "así es".
