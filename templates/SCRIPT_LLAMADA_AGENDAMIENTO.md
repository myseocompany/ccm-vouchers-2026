# Script de llamada — agendamiento de onboarding

**Programa:** Vouchers Digitales — Cámara de Comercio de Manizales (CCM).
**Producto:** AriCRM Plan Crecer.
**Objetivo único de la llamada:** dejar **fecha y franja horaria** para la sesión de implementación de 4 horas. **No** se hace onboarding en la llamada, **no** se piden datos operativos ni credenciales.
**Duración objetivo:** 3–5 minutos.
**Estado:** borrador interno — requiere aprobación de Nicolás antes de usarse en llamadas reales (ver `POLICIES.md`).

---

## 0. Antes de marcar (30 s)

Abrir `clientes/<slug>/CLIENTE.md` y confirmar:

- Nombre del contacto principal y del establecimiento.
- Número al que se va a llamar.
- Última interacción registrada (fecha, canal, resultado).
- Situación especial si existe (ej. Manuelina — sede colapsada, opera desde casa).

Tener a la mano **2 franjas propuestas** de 4 horas dentro de los próximos 7–14 días.

---

## 1. Apertura y verificación de identidad (20–30 s)

> "Buenos días, ¿hablo con **[Nombre del contacto]** de **[Nombre del restaurante]**? Le habla **[Nombre del agente]**, de **MY SEO COMPANY**. Le contacto por el programa de **Vouchers Digitales de la Cámara de Comercio de Manizales**, del que su restaurante es beneficiario. ¿Es buen momento para 3 minutos?"

**Si NO es buen momento:**
> "Sin problema. ¿Le llamo hoy en la tarde o mañana en la mañana? ¿A qué hora exactamente?"
Cerrar con hora concreta y colgar.

**Si NO es la persona correcta:**
> "¿Me podría indicar quién es la persona que estará a cargo de la implementación digital del restaurante, y a qué número la puedo contactar?"
Registrar y llamar al nuevo contacto.

---

## 2. Contexto mínimo (30–40 s)

> "La Cámara ya confirmó a **[Nombre restaurante]** dentro de los beneficiarios del programa. Nosotros somos el equipo que va a hacer la implementación, sin costo para ustedes. Todavía no tenemos agendada su sesión y por eso lo llamo."

*No detallar funcionalidades, no vender, no prometer resultados.* Si preguntan qué incluye, respuesta corta:

> "Es AriCRM, un CRM con IA para responder WhatsApp, gestionar pedidos y reservas, con acompañamiento de 4 meses. Los detalles se los explicamos completos en la sesión."

---

## 3. Propuesta de agenda (60–90 s)

> "La implementación se hace en **una sesión de 4 horas seguidas**, con la persona que va a manejar la herramienta día a día presente todo el tiempo. Tengo dos opciones cercanas: **[Fecha 1, hora–hora]** o **[Fecha 2, hora–hora]**. ¿Cuál le sirve mejor?"

Si dice que **ninguna funciona**:
> "¿Qué día y en qué franja de la próxima semana o la siguiente le queda mejor? Necesitamos 4 horas continuas."

Si dice **cualquiera está bien**:
> "Perfecto, dejo la **[Fecha 1]** de **[hora]** a **[hora]**."

---

## 4. Confirmar responsable y canal (30–40 s)

Solo dos preguntas — nada más:

1. *"¿Quién va a ser la persona del restaurante presente esa sesión completa? Necesito su nombre y su número de WhatsApp."*
2. *"¿Le puedo mandar la confirmación y el formulario de preparación al WhatsApp **[número desde el que llamamos o el que dio en el paso 1]**?"*

**Registrar textualmente**, no interpretar.

---

## 5. Compromisos y cierre (30 s)

> "Entonces confirmamos: sesión el **[Fecha, hora–hora]**, con **[Nombre responsable]** presente. En las próximas 24 horas le envío al WhatsApp **[número]**:
> 1. Confirmación de la fecha.
> 2. Un formulario corto de preparación.
> 3. La lista corta de lo que necesitamos tener listo el día anterior.
>
> Si necesita cambiar la fecha, me escribe al mismo número. ¿Alguna pregunta antes de colgar?"

Responder solo preguntas de logística (fecha, hora, formato, quién asiste). Preguntas operativas sobre el producto: aplazar.

> "Esa la vemos completa en la sesión, para poder dedicarle el tiempo que merece."

Cerrar:
> "Gracias, **[Nombre]**. Nos vemos el **[Fecha]**. Buen día."

---

## 6. Manejo de objeciones — solo lo mínimo para agendar

| Objeción | Respuesta corta |
|---|---|
| *"¿Cuánto cuesta?"* | "Cero. Está cubierto por el programa de la Cámara." |
| *"¿Ustedes son de la Cámara?"* | "No. Somos MY SEO COMPANY, el equipo implementador contratado por la Cámara. Puede verificarlo con ellos." |
| *"Mándeme info por WhatsApp y le respondo."* | "Con gusto la mando, pero necesito dejar una fecha tentativa en esta llamada para reservar su cupo. ¿Le sirve **[Fecha 1]** o **[Fecha 2]**?" |
| *"No tengo tiempo para 4 horas."* | "Entiendo. La sesión es una sola vez y deja el servicio operando ese mismo día. Podemos elegir el horario más flojo del restaurante." |
| *"No me interesa / no quiero participar."* | No presionar. "Entiendo. ¿Prefiere que informemos a la Cámara que declina el beneficio, o quiere pensarlo y le llamo el **[Fecha]**?" — registrar y escalar. |
| Preguntas técnicas / operativas | "Buena pregunta. Esa la resolvemos en la sesión con el detalle que merece. Hoy solo estoy dejando la fecha." |

---

## 7. Reglas duras (no cruzar en la llamada)

- **No** hacer el onboarding en la llamada — la llamada es solo para agendar.
- **No** pedir contraseñas, códigos SMS, QR, ni datos de tarjetas.
- **No** pedir menú, precios, horarios ni políticas por teléfono — eso va en el formulario asíncrono.
- **No** prometer resultados de negocio (ventas, pedidos, ROI, tiempos de respuesta).
- **No** ofrecer funcionalidades fuera del alcance contratado (integraciones con Rappi, POS, dominios propios, etc.).
- **No** aceptar cambios de alcance, plazo o precio — escalar a Nicolás.
- **No** grabar la llamada sin consentimiento explícito al inicio.
- **No** compartir información de otros restaurantes del programa.

---

## 8. Registro post-llamada (obligatorio, dentro de 10 min)

1. `clientes/<slug>/PROGRESS.md` — entrada con fecha de llamada, resultado (agendado / re-llamar / declinado / no contactado) y fecha de sesión si aplica.
2. `clientes/<slug>/CLIENTE.md` — actualizar contacto, número, responsable operativo si cambiaron.
3. `evidencias/<slug>/llamada-agendamiento-<YYYY-MM-DD>.md` — hora, duración, con quién se habló, fecha acordada, número de WhatsApp confirmado, compromisos.
4. Si el contacto **declinó** o hay bloqueo mayor: registrar en `DECISIONS.md` y escalar a Nicolás antes de reportar a la Cámara.

---

## 9. Resultado posible de la llamada — clasificación

- **AGENDADO** → sesión con fecha, hora y responsable confirmados. Enviar formulario en 24 h.
- **RE-LLAMAR** → contacto pide llamada posterior con hora concreta anotada.
- **CONTACTO INCORRECTO** → obtenido nuevo número/responsable; llamar en 24 h.
- **NO CONTESTA** → registrar intento; máximo 3 intentos en 3 días distintos y en franjas distintas; luego escalar.
- **DECLINA** → registrar razón textual y escalar a Nicolás para comunicación a la Cámara.
