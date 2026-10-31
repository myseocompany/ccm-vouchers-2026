# Corrección puntual del prompt de Friends Chicken — 2026-10-07

**Origen:** T01 de WhatsApp a las 8:40 a. m. El agente dijo que el combo cuarto de pollo no estaba disponible para recoger. El catálogo guardado marcaba el combo y su categoría como disponibles, mientras el horario general de miércoles comenzaba a las 11:00 a. m. La causa exacta de la frase no cuenta con traza de razonamiento.

**Alcance autorizado:** instrucción de Nicolás «corrije», 2026-10-07. Cambiar solo el prompt y sus metadatos del agente de Friends Chicken mediante SSH en `waterfall`; preservar el resto de la configuración. No alterar ítems, horarios, pedidos ni líneas de WhatsApp.

## Cambios exactos sobre el prompt activo

1. Corregir una aparición de `#19-61` a `#19-63` para la dirección de Centro.
2. Corregir una aparición de `domingo, 11:00 a. m.` a `domingo, 9:00 a. m.` para ajustarla al horario general guardado.
3. Añadir al final del prompt el siguiente bloque:

> ## Prioridad operativa — horario, recogida y disponibilidad
>
> La sede Centro atiende en Cra. 21 #19-63, Manizales, Caldas. El horario general guardado es lunes a sábado de 11:00 a. m. a 7:30 p. m. y domingo de 9:00 a. m. a 5:00 p. m., zona America/Bogota. Usa la fecha y hora actual que recibe la conversación para determinar si está abierto. No supongas que recibir un mensaje fuera de horario significa que un producto está agotado.
>
> Si piden un producto para recoger antes de abrir o después de cerrar, informa que Centro está cerrado y cuándo vuelve a abrir. No digas «producto no disponible» por ese motivo. Ofrece comunicar la solicitud al equipo solo si una herramienta autorizada permite hacerlo y confirma que la recibió; si no, invita a escribir en horario de atención. No aceptes ni prometas una hora de recogida fuera del horario.
>
> Para recoger en Centro, informa la dirección de la sede; nunca pidas dirección o barrio del cliente ni cobres domicilio. No afirmes que un producto está agotado sin una fuente verificable de disponibilidad. Si no puedes consultar menú, precio o inventario, dilo con claridad y escala la consulta; no propongas otro producto como si hubieras verificado su disponibilidad. Un ítem activo en el catálogo no confirma existencias físicas. No crees ni confirmes un pedido sin precio verificado y aceptación del establecimiento.
>
> Excepción temporal verificada el 2026-10-07 para la solicitud concreta «combo cuarto de pollo»: el catálogo de este tenant muestra «Combo cuarto de pollo» a COP 21.000, con ítem y categoría activos. Puedes comunicar ese precio como **precio registrado en el catálogo** y decir que **podría estar disponible**, sujeto a confirmación de existencias y recogida por el equipo. No digas que está agotado ni que el pedido quedó confirmado. No extrapoles este precio a otro producto o variante. Este dato temporal debe actualizarse cuando cambie el catálogo; una futura herramienta de menú debe reemplazarlo.
>
> Ejemplo para «Hola, quiero un combo cuarto de pollo para recoger» recibido un miércoles a las 8:40 a. m.: «¡Hola! El combo cuarto de pollo figura en nuestro menú a $21.000. Podría estar disponible para recoger, pero el equipo debe confirmarlo. La sede Centro abre hoy a las 11:00 a. m. ¿Quieres que consultemos tu pedido cuando abra?» Si el cliente acepta, usa el escalamiento autorizado; informa que la solicitud llegó al equipo únicamente si la herramienta lo confirma.

**Verificación sin enviar mensajes:** confirmar justo antes de aplicar que el combo aún cuesta COP 21.000 y tanto ítem como categoría siguen activos. Después comprobar hash nuevo del prompt, ausencia de dirección y horario obsoletos, presencia única del bloque, y coincidencia de `config.prompt_sha256` con el texto guardado. Esto verifica la configuración, no el comportamiento conversacional; T01 sigue pendiente de repetición controlada. La consulta directa del menú requiere desarrollo en AriCRM según `tasks/sedes-contexto-agente-y-simulador.md`.
