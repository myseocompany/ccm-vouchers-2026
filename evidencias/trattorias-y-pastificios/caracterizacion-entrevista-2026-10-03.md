# Minuta operativa de entrevista — Trattorias y Pastificios S.A.S. (ONO / DOYO)

- **Fecha de registro**: 2026-10-03
- **Fuente**: entrevista / llamada con Paulo Restrepo (Director) — transcripción compartida por Nicolás en la conversación de trabajo.
- **Estado**: levantamiento operativo; **pendiente de validación formal** del establecimiento. No es configuración, activación ni aceptación.
- **Protección de datos**: la transcripción cruda no se archiva; esta minuta conserva únicamente información operativa mínima y los datos de contacto necesarios para la implementación.

---

## 1. Objetivo y alcance del agente IA

- El agente debe **atender la venta hasta cierto punto**: presentar la carta, tomar el pedido y la dirección.
- **De ahí en adelante continúa una persona** (cobro y manejo del domicilio). La persona que continúa es **la misma**: **Ángela Bedoya** (mismo chat).
- No se trabajará el **aforo** ni se enviará tráfico al lugar; la operación del beneficio es a **domicilio**.
- Se busca **competir con Rappi**: Rappi es muy rápido y hoy la falta de respuesta efectiva empuja a los clientes a pedir por Rappi.

## 2. Operación y horarios

- **Lunes a viernes**: 11:30–15:00 y 18:00–22:00.
- **Sábado**: horario corrido 11:30–22:00.
- **Domingo**: 11:30–20:40.
- **Festivos**: cerrado.
- No se atiende salón de manera relevante para el proyecto (ONO opera cerrado / solo domicilio).

## 3. Canales y líneas

- Canales activos y aprovechables: **WhatsApp e Instagram**.
- **Por ahora se trabaja con una sola línea de WhatsApp** (no las 3 del alcance contractual, que quedan disponibles).
- La línea actual tiene ~2 años y conserva los contactos/historial. Antes existía un celular por marca (ONO y DOYO) pero se unificó en uno por simplicidad operativa.
- No hay línea API hoy; queda **por revisar** como opción para campañas sin riesgo de bloqueo.

## 4. Menú y catálogo

- El menú está publicado en **MenuApp / MenuUp** (fotos cargadas). Preferencia del cliente: **usar el link de MenuApp** ya establecido, no construir un menú propio.
- **Pendiente**: ~~link de la carta de **ONO** y de **DOYO**~~ — **recibidos 2026-10-03** (`../../evidencias/trattorias-y-pastificios/menu-menupp-2026-10-03.md`). Falta definir cuál link envía la secuencia según la marca que atienda la línea.
- Lógica de armado: **DOYO** tiene platos preestablecidos y, sobre todo, el **«arma tu poke»**; **ONO** es mayoritariamente «arma tu poke». El armado puede requerir conversación (p. ej. «sin maní» por **alergia**), por lo que el agente debe manejarlo antes del cierre.

## 5. Pedidos, pagos y domicilios

- **Medios de pago**: **Bold**, **Datáfono Bancolombia**, **transferencia bancaria** y **«breve» (Bre-B)**. Efectivo **no** para domicilio.
- **Zonas cubiertas**: toda **Manizales** y **Villamaría** (solo esas dos).
- **Domicilio**: flota **tercerizada**; cobra una **tarifa estándar por zona/dirección**. **Pendiente**: lista de tarifas (Ángela la comparte).

## 6. Reservas y eventos

- **Reservas**: no aplican.
- **Eventos/catering**: frecuentes (p. ej. fiesta de 50 niños, bao o sushi). El agente debe ofrecer el mensaje **«Pregúntanos aquí por nuestros eventos»** y escalar el caso.

## 7. Escalamiento a humano

- Se escalan al mismo chat / a **Ángela Bedoya**: **quejas, alergias, pagos, cambios y reclamos**.
- Otros temas que el agente puede orientar antes de escalar: **ubicaciones**, **alergias**, **inconformidades** («me llegó mal el pedido»), **proveedores**, **servicio a domicilio** y **«¿a partir de qué hora?»**.

## 8. Tono y marca

- **Tono**: neutro, **jovial** (marcas relajadas). **No** usar un tono temático «oriental».

## 9. Remarketing y campañas

- Ventas a domicilio hoy: **~5%** del total; meta: **10–15%**. Hipótesis: responder más rápido aumenta la intención de compra.
- **Campañas y redes paradas**: DOYO en **«0»** y ONO **reactivando desde la semana pasada** (se reactivó con MenuApp). No hay community manager.
- **Remarketing**: sí vale la pena. Hay **base de clientes en Excel** + historial descargable de WhatsApp. Propuesta: **línea API** o envío por lotes (20–100 mensajes) para evitar bloqueos. Cliente abierto a revisar la API.

## 10. Equipos y factibilidad

- Hay **celular con WhatsApp** y **computadora**. Antes cada marca tenía su equipo; hoy comparten la computadora de KOMO, así que **se accede a las dos aplicaciones desde un mismo PC**.

## 11. Mensaje inicial propuesto y promociones

- El cliente propone un **mensaje de bienvenida** con contexto del sismo, del tipo: «Gracias por escribirnos. Como bien saben, nuestros locales sufrieron por el terremoto y temporalmente estamos a servicio a domicilio exclusivamente, hasta nuevo aviso; pronto anunciaremos la reapertura.»
- Explora un **bono simbólico** (p. ej. **$2.000** en el primer pedido) o un artículo/insumo gratis con compra superior a X. **Decisión**: primero se pone a funcionar el bot y luego se define la promoción.

## 12. Próximos pasos acordados

1. **Ángela** comparte los **mensajes preestablecidos** actuales y la **lista de tarifas de domicilio** (los **links de carta ONO y DOYO ya se recibieron** el 2026-10-03).
2. El bot debe estar **corriendo hacia el jueves/viernes**.
3. **Nicolás escribe** para agendar una reunión de **pruebas**: mostrar qué conversa el bot, corregir en caliente y pasar a **producción**.
4. Definir promoción de reactivación **después** de validar el funcionamiento del bot.

## 13. Riesgos declarados

- Preocupación principal del cliente: **no hacer promesas falsas al cliente** respecto a la calidad/rapidez de la respuesta del bot. Mitigar con pruebas antes de promocionar.

---

## Observaciones del harness

- Varios campos que figuraban como «pendiente por confirmar» en `../../clientes/trattorias-y-pastificios/CARACTERIZACION.md` quedan **confirmados** por esta entrevista (horarios, canales, pagos, zonas, escalamiento, alcance del agente, una sola línea inicial).
- Sigue **abierta** la decisión de qué marca(s) atiende(n) la línea (ONO/DOYO vs. KOMO) y la formalización con el establecimiento.
