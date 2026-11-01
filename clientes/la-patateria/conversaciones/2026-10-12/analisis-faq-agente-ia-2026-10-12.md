# La Patatería — preguntas frecuentes y base de conocimiento para agente IA

Fecha del análisis: 2026-10-12  
Tenant: `01a0cb62-1d87-7101-ab7b-c2a0ddc30f5f`

## Resumen ejecutivo

El principal trabajo del canal no es responder preguntas aisladas: es gestionar reservas. En 104 de 240 conversaciones reales analizadas (43,3 %) aparece una solicitud o gestión de reserva. Los cumpleaños y la decoración aparecen en 56 (23,3 %). Carta/menú, ubicación, horarios y domicilios forman el segundo bloque de demanda.

La primera versión del agente debería:

1. resolver información operativa por ciudad y fecha;
2. recopilar datos de reserva de forma estructurada, pero no prometer disponibilidad hasta consultar una fuente vigente o recibir confirmación humana;
3. entregar la carta vigente y explicar el menú del día;
4. escalar cambios, cancelaciones, quejas, fallos de reserva, grupos grandes y excepciones;
5. usar una base de conocimiento versionada por sede, porque varias respuestas observadas contradicen la caracterización documental.

No conviene publicar todavía como hechos definitivos la cobertura de domicilios, el horario de viernes/sábado, la dirección temporal, la capacidad de grupos, el corte horario de reservas ni los beneficios de cumpleaños. Esos puntos necesitan validación del establecimiento.

## Corpus y método

- Fuente: `conversations-2026-10-12.jsonl`.
- Integridad verificada por el agente extractor: 250 conversaciones, 2.497 mensajes, 250 IDs de conversación únicos y 2.497 IDs de mensaje únicos; sin cruces incorrectos de tenant o conversación.
- Periodo: 2026-09-22 23:21:33 a 2026-09-30 23:35:58 (hora almacenada por la aplicación, reportada como UTC).
- SHA-256 del export: `a2f08f5c9833c15d42d98dbd097170f1a425eeac01d6780c588f64fb2edfa0cf`.
- Se excluyeron 20 mensajes diagnósticos cuyo texto empieza por `[TEST`.
- Denominador del análisis: 240 conversaciones con al menos un mensaje entrante no diagnóstico. Las diez restantes no tenían texto entrante útil después de excluir pruebas.
- Las categorías son multietiqueta: una conversación puede pedir, por ejemplo, reserva, decoración, carta y ubicación. Por eso los porcentajes no suman 100 %.
- Los conteos se obtuvieron por patrones de intención sobre mensajes entrantes y se contrastaron con las respuestas salientes. Son una línea base reproducible, no una taxonomía entrenada.
- El export contiene PII. Este informe no reproduce nombres, teléfonos, correos, datos particulares de reservas ni mensajes identificables.

## Preguntas e intenciones frecuentes

| Intención | Conversaciones | % de 240 | Variantes anonimizadas observadas |
|---|---:|---:|---|
| Crear, consultar, modificar o cancelar una reserva | 104 | 43,3 % | “Quiero reservar”; “¿hay mesa para un grupo?”; “necesito cambiar el número de personas”; “quiero liberar la reserva” |
| Cumpleaños y decoración | 56 | 23,3 % | “¿Decoran para cumpleaños?”; “¿la decoración cuesta?”; “¿qué incluyen para la persona que cumple?” |
| Carta o menú del día | 42 | 17,5 % | “¿Me envían la carta?”; “¿qué menú tienen hoy?”; “¿hay varias opciones de almuerzo?” |
| Ubicación o sede actual | 25 | 10,4 % | “¿Dónde están atendiendo después del sismo?”; “¿cuál es la nueva ubicación?”; “¿dónde queda la sede?” |
| Horarios y apertura | 21 | 8,8 % | “¿Hasta qué hora atienden?”; “¿abren hoy?”; “¿a qué hora cierran el domingo?” |
| Domicilios y cobertura | 18 | 7,5 % | “¿Tienen domicilio?”; “¿cómo pido?”; “¿llevan a esta zona?” |
| Pedidos o recogida | 18 | 7,5 % | “Quiero hacer un pedido”; “¿puedo pedir para recoger?”; “¿cuánto tarda?” |
| Precio o cotización | 11 | 4,6 % | “¿Cuánto cuesta la decoración?”; “¿qué precio tiene?”; “necesito una cotización para un grupo” |
| Promociones y descuentos | 7 | 2,9 % | “¿Qué promociones hay?”; “¿aplica para domicilio?”; “¿sigue vigente el convenio?” |
| Queja o novedad de servicio explícita | 3 | 1,2 % | “La reserva no aparece”; “estoy en la mesa y no me atienden”; recomendación por una falla repetida |
| Empleo | 3 | 1,2 % | “¿Están buscando personal?”; envío de hoja de vida |

La detección literal de preguntas sobre ingredientes fue baja (1 conversación; 0,4 %), pero no debe interpretarse como ausencia de necesidad: el formulario de caracterización sí reporta explicación de platos e ingredientes como caso frecuente, y parte de la carta se intercambió como PDF o audio, que este análisis textual no interpreta.

## Cómo se atendieron las reservas

Dentro de las 104 conversaciones que mencionan reservas:

- en 54 (51,9 %) se pidió el formulario de datos: nombre, celular, correo, día/hora, número de personas y ocasión;
- en 44 (42,3 %) aparece una confirmación explícita de reserva;
- en 23 (22,1 %) se indicó falta de cupo o que no se gestionaban reservas para el mismo día;
- en 8 (7,7 %) se mencionó como hora máxima las 7:30 p. m.;
- en 7 (6,7 %) se afirmó que la decoración no tenía costo;
- en 2 (1,9 %) se mencionó un postre de cortesía para cumpleaños.

Estos porcentajes describen lo escrito, no necesariamente el resultado operacional final. Una confirmación textual no demuestra que la reserva haya quedado persistida correctamente; el corpus contiene al menos un caso en el que una reserva reportada por el cliente no se reflejó en el sistema.

## Resolución, vacíos y escalamiento

- 237 de 240 conversaciones con entrada real (98,8 %) recibieron algún mensaje saliente después del primer mensaje del cliente.
- En 17 conversaciones (7,1 %) las salidas fueron únicamente saludos, acuses, mensajes automáticos o frases genéricas, sin una respuesta sustantiva detectable.
- 49 conversaciones incluyeron al menos un archivo o medio saliente. En las solicitudes de menú, 19 conversaciones recibieron un documento, normalmente la carta en PDF. Por ello, medir resolución solo por texto subestima algunas respuestas.
- La ubicación temporal fue respondida de forma repetida, pero no siempre; algunas conversaciones terminaron tras pedir ciudad o con una respuesta genérica.
- Las preguntas de horario recibieron respuestas breves como “hasta las 9”, frecuentemente sin precisar sede, día ni zona horaria. Esto puede ser incorrecto para viernes, sábado o domingo.
- En domicilios se observó una respuesta dominante (“solo Pereira mediante Rappi”), junto con mensajes que describen el servicio como deshabilitado o en recuperación. La vigencia no puede inferirse solo del histórico.
- Cambios de reserva y grupos grandes se procesaron manualmente. Hay cambios aceptados a 18, 24 y 25 personas, pero también una negativa por limitación del espacio temporal. El agente no debe decidir capacidad por sí solo.
- Deben escalarse siempre: quejas y PQR; cobros o pagos; reserva ausente del sistema; cambios/cancelaciones; grupos por encima del umbral aprobado; disponibilidad excepcional; alergias; empleo/proveedores; y cualquier respuesta que dependa de ocupación en tiempo real.

## Información empresarial observada en conversaciones

Lo siguiente es útil para la base de conocimiento, pero “observado” no equivale a “vigente”. Debe validarse antes de habilitar respuestas automáticas.

| Tema | Lo observado de forma repetida | Confianza del corpus | Acción antes de publicar |
|---|---|---|---|
| Reservas | Se recogen nombre, celular, correo, fecha/hora, cantidad de personas y ocasión | Alta | Confirmar campos mínimos, tratamiento de datos y persistencia en AriCRM |
| Reserva el mismo día | Se respondió repetidamente que no se hacen o que ya no hay cupos; se ofrece atención sin reserva según disponibilidad | Media-alta | Convertir en política explícita por sede y definir hora de corte |
| Hora máxima de reserva | Se mencionó 7:30 p. m. | Media | Confirmar si es una regla permanente y por cuál sede/día |
| Cumpleaños | Globos sencillos con reserva previa; se mencionan cumpleaños y grado | Media | Confirmar diseños, anticipación, sedes y excepciones |
| Costo de decoración | Se respondió que no tiene costo o viene incluida con la reserva | Media | Validar vigencia y condiciones |
| Cortesía de cumpleaños | Se mencionó un postre para la persona que cumple | Baja-media | No automatizar hasta confirmación formal |
| Horario | Se respondió 12:00–21:00 y domingo hasta las 20:00 | Alta para el periodo, no para vigencia | Resolver contradicción de viernes/sábado y versionar por sede |
| Manizales | Se informó una ubicación temporal dentro de otro establecimiento tras el sismo | Alta para el periodo | Confirmar nombre comercial, dirección normalizada, mapa y fecha de vigencia |
| Domicilios | Se afirmó repetidamente que solo estaban disponibles en Pereira mediante Rappi | Alta para el periodo | Resolver contradicción documental y confirmar URL/cobertura vigentes |
| Menú del día | Disponible de lunes a viernes y solo para consumo en el punto | Alta para el periodo | Confirmar sede, festivos, precio, horario y stock diario |
| Carta | Se envió un PDF de menú de forma recurrente | Alta como práctica | Validar cuál archivo es la carta vigente, fecha y precios |
| Promociones/convenios | Aparece al menos un convenio con descuento y condiciones específicas | Baja para uso general | Mantener fuera del agente salvo segmentación y vigencia verificadas |

## Contradicciones que deben resolverse

1. **Domicilios:** `CLIENTE.md` y `CARACTERIZACION.md` dicen que Pereira no tiene domicilios; el corpus repite que los domicilios solo funcionan en Pereira por Rappi. Es la contradicción más crítica.
2. **Horario:** la documentación reporta viernes y sábado hasta las 22:00; el corpus responde todos los días hasta las 21:00 y domingo hasta las 20:00.
3. **Ubicación:** la dirección histórica de Manizales figura como afectada y en ruinas. El corpus usa una sede temporal. El agente necesita ubicación vigente por ciudad, no una dirección global.
4. **Carta:** la caracterización dice que se espera una carta nueva, mientras el canal envió un PDF existente. Debe identificarse la versión, fecha y sede de ese PDF.
5. **Grupos:** la caracterización propone mesas hasta 15 personas y llamada para grupos mayores, pero el corpus muestra reservas o cambios a grupos mayores y también rechazos por espacio.
6. **Mismo día y corte de 7:30 p. m.:** aparecen como reglas frecuentes en el corpus, pero no están consolidadas en la caracterización.
7. **Decoración y cortesía:** el corpus promete globos sin costo y, en pocos casos, postre de cumpleaños; la documentación todavía pide verificar estas reglas.

## Base de conocimiento recomendada

### Prioridad 0 — bloquear hasta validar

- Matriz por ciudad/sede con estado operativo, dirección, enlace de mapa, horario por día y fecha de vigencia.
- Domicilios por sede: disponible/no disponible, plataforma o canal, enlace oficial, zonas, tarifas, horarios y tiempos estimados.
- Carta vigente versionada: archivo/URL, sede, fecha de vigencia, precios, disponibilidad y menú del día.
- Política de reservas: anticipación mínima, corte diario, disponibilidad, capacidad, grupos grandes, cambios, cancelaciones y no-show.
- Cumpleaños/decoración: qué incluye, costo, anticipación, ocasiones admitidas, restricciones y cortesía.

### Prioridad 1 — automatizar en el primer lanzamiento

- Detección de ciudad antes de responder información operativa.
- Respuesta de ubicación y horario con sello de vigencia.
- Envío de carta correcta por sede.
- Información de domicilios y enlace oficial.
- Flujo guiado de reserva que recopile campos, valide formato y solicite consentimiento de uso de datos.
- Estado claro: “solicitud recibida” no debe convertirse en “reserva confirmada” sin confirmación del sistema o de una persona.

### Prioridad 2 — automatizar con datos en tiempo real

- Disponibilidad de mesas y horarios.
- Creación, consulta, modificación y cancelación de reservas.
- Productos agotados, menú del día y promociones vigentes.
- Estado y tiempo de pedidos.

### Prioridad 3 — derivar a humano

- Quejas, reclamos, cobros, pagos fallidos y pedidos incorrectos.
- Reserva no encontrada o discrepancia entre canales.
- Alergias y restricciones alimentarias cuando no exista ficha técnica aprobada.
- Grupos grandes, eventos, cotizaciones y excepciones.
- Empleo, proveedores, prensa y alianzas.

## Reglas de comportamiento propuestas

1. Preguntar primero la ciudad cuando la respuesta dependa de sede.
2. No inferir disponibilidad, precio, cobertura, tiempo de entrega ni stock.
3. Citar únicamente contenido con `sede`, `vigente_desde`, `vigente_hasta` o estado vigente y responsable de aprobación.
4. Diferenciar “solicitud de reserva” de “reserva confirmada”.
5. Antes de capturar PII, explicar brevemente para qué se usa; mostrar un resumen y pedir confirmación.
6. No repetir datos personales completos en el chat; enmascarar teléfono y correo al confirmar.
7. Si falta un dato o dos fuentes se contradicen, reconocerlo y escalar, sin elegir la respuesta más reciente por intuición.
8. Mantener tono cercano, natural y paisa sin exagerar modismos; usar mensajes cortos y una pregunta por turno.
9. Para quejas, empezar con reconocimiento y pasar a una persona con contexto; no discutir ni prometer compensaciones.
10. Registrar intención, sede, resultado y motivo de escalamiento para mejorar la taxonomía.

## Intenciones mínimas sugeridas

- `reserva_crear`, `reserva_consultar`, `reserva_modificar`, `reserva_cancelar`
- `cumpleanos_decoracion`
- `menu_carta`, `menu_del_dia`, `producto_ingredientes`
- `ubicacion`, `horario`
- `domicilio_cobertura`, `domicilio_iniciar`
- `pedido_iniciar`, `pedido_estado`, `pedido_recoger`
- `promocion_convenio`
- `queja_pqr`, `pago_cobro`
- `empleo`, `proveedor_otro`
- `humano_solicitado`, `fuera_de_alcance`

## Documentos puntuales contrastados

Solo se consultaron, en lectura, los siguientes archivos de `/Volumes/ExternoMS/projects/ccm-vouchers-2026/clientes/la-patateria/`:

- `CLIENTE.md`
- `CARACTERIZACION.md`
- `PLANTILLAS_WHATSAPP.md`

No se modificó ese repositorio. `PLANTILLAS_WHATSAPP.md` sigue marcado como borrador y no debe configurarse en producción sin aprobación; además, su mensaje de bienvenida promete domicilio o recogida sin distinguir sede, por lo que debe corregirse después de validar la matriz operativa.

## Limitaciones

- El periodo cubre solo nueve días y coincide con una operación transitoria posterior al sismo; no representa necesariamente la demanda anual.
- Audios, imágenes y contenido del PDF no fueron transcritos ni interpretados. Las frecuencias textuales pueden subestimar ingredientes, platos y respuestas contenidas en medios.
- Los porcentajes miden presencia de intención por conversación, no número total de preguntas ni clientes únicos.
- No se verificó contra sistemas de reservas, Rappi, mapas ni inventario. El informe distingue observación histórica de información autorizada para producción.
