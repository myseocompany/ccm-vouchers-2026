# Reunión de equipo — revisión de avance del agente IA (ONO) — 2026-10-03

> **Uso interno del harness.** Contiene nombres y roles de personas del establecimiento (POLICIES — Datos y secretos). No incluir en entregables públicos ni compartir por canales no seguros.

## Metadatos

- **Cliente**: Trattorias y Pastificios S.A.S. (marcas ONO / DOYO / KOMO).
- **Fecha de la reunión**: **2026-10-03 por la tarde** (inferida de producción: los cambios pactados —prompt solo-ONO, links solo-ONO en las secuencias— quedaron guardados ese día entre las 16:04 y las 16:09, hora del servidor; ver `ia-conversacional/verificacion-prompt-2026-10-05.md`). La transcripción se recibió y registró el 2026-10-05.
- **Canal**: videollamada (grabación con transcripción automática; la grabación se corta al inicio y a mitad de la prueba en vivo por fallas de pantalla).
- **Asistentes**:
  - **Nicolás Navarro Rincón** — MY SEO (presenta el avance y opera la plataforma).
  - **Paulo Restrepo** — Director del establecimiento (transcrito como «Pablo»).
  - **Steven** — por el establecimiento; área de tecnología y apoyo a compras; designado líder del proyecto y auditor diario de conversaciones (apellido pendiente).
  - **Sebastián** — invitado, sin rol en la empresa; estudiante de Administración (CESA, Bogotá).
- **Fuente**: transcripción automática provista por Nicolás. El texto llegó duplicado; se conserva una sola copia.
- **Alcance del documento**: transcripción **depurada** — texto verbatim del autotranscriptor (solo limpieza de puntuación/cortes y deduplicación; sin cambio de palabras), segmentada por hablantes con **atribución inferida** (la fuente no identifica hablantes; las etiquetas entre corchetes son reconstrucción). Acotaciones editoriales en _cursiva entre corchetes_.

## Glosario de nombres mal transcritos

| En la transcripción | Término correcto (según evidencias del repo) |
|---|---|
| Dojo, dollo, «dojo uno» | DOYO (marca) |
| Ono, Uno, ay, «Bono» (icono), «uno poke» | ONO (marca) / «Ono Poke» |
| Pablo | Paulo Restrepo |
| Steam | Steven |
| Menú App, Menú Up, Menúa, Menup, «menú» | MenuApp (`menupp.co`) |
| breve | Bre-B |
| Alma tu Poke | «Arma tu Poke» |
| Vaya ($40.000, tartar de atún) | en MenuApp el poke de $40.000 con tartar de atún es **Poke Bahía**; Paulo validó el nombre del prompt «tal cual está escrito» |
| Onolulu | Poke Honolulu |
| Grasqui | Poke Kraskí |
| pan set (proteína) | Panceta |
| salsa hormon | probablemente «salsa ONO» (por confirmar) |
| maíz iracha / sriracha | sriracha |
| Belli | Veggie |
| bonito (varias veces) | bono |
| «lloras al vapor» | fragmento ininteligible del ejemplo de atención lenta por WhatsApp |
| Miriam («voy para Miriam») | ¿Villamaría? (prueba de cobertura) |
| Daniel | persona a quien se le pediría dejar MenuApp solo ONO (rol por identificar; posiblemente de MenuApp) |
| GPT 4 mini | GPT-4 mini |

## Decisiones y acuerdos de la reunión

**Decisiones del establecimiento (aprobadas en reunión):**

1. **Marca**: la línea 310 482 3232 atiende **solo ONO**; **DOYO queda en stand-by**. Pedirán a MenuApp que oculte DOYO. En la reunión se cambió en vivo la plantilla de bienvenida al link solo-ONO (pendiente de verificación con teléfono controlado).
2. **Escalamiento**: Ángela Bedoya (pedidos y catering) y **Steven como segundo contacto** para órdenes especiales/muy grandes.
3. **Auditoría**: crear **usuario de AriCRM para Steven** para revisar diariamente las conversaciones del bot y los tiempos de respuesta de Ángela (prefiere usuario remoto a tener el teléfono físico).
4. **Icono de perfil** de la línea: cambiar al **logo de ONO**.
5. **Cierre del pedido**: lo arma y factura **MenuApp** (emite comanda a cocina e imprime en punto de venta). El bot guía la construcción del pedido pero no cobra ni factura; al final entrega a la persona humana (Ángela) que confirma.

**Propuestas abiertas (no decididas):**

- Bono de $5.000 post-compra Rappi enviado por WhatsApp para capturar el contacto y migrar pedidos al canal propio (el establecimiento ya hizo bonos físicos y no los ha repetido).
- Campaña masiva de recuperación con la base de contactos (no tienen CRM; preocupación explícita por fuga de datos y por baneo de la línea). Nicolás indicará a Steven cómo cargar y proteger los contactos.
- Línea API para reducir el retardo de respuesta del bot (hoy responde despacio a propósito para cuidar la línea).

**Pendientes técnicos que salieron de la reunión:**

- Tarifas de la flota tercerizada de domicilio (no están en el prompt); resolver discrepancias MenuApp vs. entrevista (efectivo a domicilio, reservas).
- Screenshot del placeholder/preview que muestra el link en la bienvenida (posible confusión para el consumidor); Paulo lo envía.
- Activar en MenuApp el enlace solo-ONO y el link de la secuencia de carta (Paulo conversa con la gente de MenuApp; quedaron de responder por chat).
- Prompt a replicar considerando que la línea se unificó (antes se habló de una línea por marca).
- Config actual vista en reunión: contexto de 20 mensajes hacia atrás, modelo GPT-4 mini (se puede subir), «categorías y rangos 16, 24» (pendiente interpretar).
- Plan: dejar el bot corriendo, recoger ajustes y lanzar a producción cuando no tenga errores; después del lanzamiento, pauta pagada («es inorgánico, le metemos billete»).

## Transcripción

### 1. Apertura, asistentes y roles

**[Paulo]**: …de equipo y voy a comenzar a tomar notas. Entonces, a ver si entendí bien, quiero repetir los nombres: Steven va a estar el nombre del proyecto, ¿cierto? Es lo que entiendo.

**[Steven]**: Sí, sí, sí.

**[Nicolás]**: Ok, ¿y dentro de la organización tiene algún rol, algún…?

**[Paulo]**: Sí, sí, digamos que en este momento lo tenemos como en área de tecnología. ¿Sí? ¿Tecnología, sí, señor? Y un poquito de apoyo en compras, pues.

**[Nicolás]**: Ok, ok. Y me presentaste tú… dijo, qué pena, no recuerdo el nombre.

**[Paulo]**: Sebastián. — Sebastián, sí señor.

**[Nicolás]**: ¿Y Sebastián tiene algún rol dentro de la empresa para anotar?

**[Paulo]**: En este momento no, en este momento no, sino que él está ahorita en la Universidad en Bogotá, estudiando Administración de CESA. Entonces, nada, yo lo quise invitar para que escuchara todo y nada, pues es más por representar, que te conozca un poco.

**[Nicolás]**: Sí señor, claro que sí. Bueno, nada, entonces les cuento un poquito como del proceso. Muchas gracias, Pablo [sic].

### 2. Recuerdo de la sesión anterior y contexto del negocio

**[Nicolás]**: Estamos en el tema de desarrollar agentes para que les ayuden al tema de las ventas. _[La pantalla se congela para ambos lados; apagan la cámara; verifican que la conexión de red está bien.]_

**[Nicolás]**: Bueno, entonces en la sesión anterior hicimos un poco el requerimiento inicial; la tarea principal era tratar de entender qué negocio íbamos a implementar. En la conversación dijimos que teníamos tres negocios, que íbamos a arrancar por dos de ellos y que dos de ellos estaban en una única línea. La principal digamos como interés era que el robot respondiera —fue como lo que anotamos en la reunión— y que ya existían unos enlaces que estaban en MenuApp, que sería como lo que principalmente pasaría el robot. Entonces esa es como la prueba que le vamos a hacer como al robot: así si logra contestar esto, es un universo… es como contratar.

**[Paulo]**: Claro que sí. De hecho, Nicolás, te cuento una cosa: nosotros antes de pandemia, por supuesto, vendíamos… el 1% de la venta era domicilios con Rappi. Llegó a niveles del 35%; hoy es el 25%. Pero Rappi claramente se queda con una porción horrorosa, se queda con una cuota importante. Cuando apareció Menú, vimos que era una tremenda solución, pero no solucionamos el tema de los domiciliarios y la plataforma; o sea, el nivel de atención y de rapidez para poder atender un pedido por WhatsApp era un ser humano que a veces son unos HPS, otras veces son unos dormidos, otras veces son muy pilos, pero normalmente no responden. Entonces le preguntan «¿tiene llosas al vapor?» y entonces la niña no vio el celular y se demora 10 minutos. Entonces los amigos me llamaban y me decían: «venga viejo, pedirles a ustedes por WhatsApp es un horror»; por eso es que pedimos por Rappi. En Rappi es de una, o sea, yo no tengo tiempo de esperar si la persona me quiere contestar o no, ¿cierto? Entonces el tema de Menú digamos que está tan bien montado como una plataforma Rappi. Y casualmente me puse a mirar las reservas que teníamos una tarde y por alguna razón se me conectó el Menú en mi computador, y el computador me timbraba y me timbraba y me timbraba, y era precisamente el Menú que estaba gestionando órdenes de compra de los clientes, ¿cierto? de clientes. Realmente es una herramienta que si la unimos con lo tuyo pues es fantástico. Listo. Entonces ya: yo no logré entender, o sea, cuando vi los enlaces, como por dónde se hacían los pedidos y demás.

**[Nicolás]**: Pero bueno, les voy a mostrar el estado de avance del proyecto y ya miramos cómo podemos continuar, ¿les parece?

**[Paulo]**: Dale, perfecto.

### 3. Estado del tenant y situación de la línea

**[Nicolás]**: Bueno, de momento tenemos creado un tenant, digamos una instancia para Trattorias. Y pues la primera cosa que hay que decir es que parte de la iniciativa de la agencia de apoyar los restaurantes es como ayudarles con las ventas. Todas las comparaciones son odiosas. Yo aquí lo que veo es que tenemos pocas conversaciones, y pues entonces me pongo ahí a disposición de ustedes por si de alguna manera los podemos apoyar para que haya más conversaciones sobre este WhatsApp. ¿Este WhatsApp está activo y es el oficial o es uno de pruebita?

**[Paulo]**: No, está activo, es el oficial, pero acuérdate que desde el terremoto nosotros apagamos completamente el restaurante; nosotros estamos apagados. Solamente estamos prendidos por Rappi. O sea, toda la conversación está fluyendo a través de Rappi. Toda la conversación está fluyendo a través de Rappi. Nosotros estamos haciendo cero, cero, cero. O sea, nosotros hemos dicho: tenemos el negocio en cuidados intensivos, prácticamente. Total.

**[Nicolás]**: Bueno, la idea de todo esto es tratar de apoyar, ¿cierto? Perdón si oí ideas con lo que no me han pedido. Yo sé que cuando a uno le hacen propuestas y uno no las ha pedido, puede sonar grosero, entonces les pido excusas.

**[Paulo]**: No, no, no, no se preocupe, Nicolás; no me ofende. Incluso, usted nos dice lo ineficiente o lo mal que lo estamos haciendo: para eso es la conversación. Eso es como la amiga que le dice a la otra «ay, cómo estás de gorda», entonces la otra, pues queriéndole ayudar, pues tratándole de cuidar la salud, hace que la otra pues se ofenda, ¿cierto?

### 4. Propuesta: capturar clientes de Rappi con un bono

**[Nicolás]**: Bueno, entonces lo primero sería como: si está corriendo la información a través de Rappi, de pronto si logramos entender cómo capturar el prospecto sería muy bueno. Es decir, enviarle después de la comunicación un bonito [sic] que diga: «mira, vos me compraste por Rappi, aquí te envío por WhatsApp el bono de compra de 5 mil pesos de lo que sea, para que nos compres la siguiente vez». Tiene doble sentido: el primero es que nos comience a hablar por esta línea y el segundo que nos quedemos con el contacto. De pronto si eso se puede hacer.

**[Paulo]**: Segundo, nosotros lo hemos hecho —no digital, no de manera digital, pero sí lo hemos hecho de manera física—: o sea, enviamos un bonito o enviamos alguna cosa. No lo hemos vuelto a hacer, lo cual es una tontería de nuestra parte, ¿me entiendes?

**[Nicolás]**: Sí, porque es muy importante capturarlo. Vale.

### 5. Revisión del prompt v1 (lectura y validación)

**[Nicolás]**: Este agente que tenemos aquí capturado tiene la posibilidad de crearle un prompt, y nosotros hemos creado la primera versióncita del prompt. Entonces, la idea es que revisemos juntos como el alcance que tiene y miremos qué le podemos ajustar. Si me permiten, se los leo. Entonces dice: «eres el asistente virtual de Dojo [DOYO] o no [ONO]; atiendes pedidos a domicilio por WhatsApp, en español colombiano, con tono neutro jovial, cercano y de tú; no uses un estilo temático oriental. Formato de los mensajes: bloques cortos, una idea por párrafo, una o dos preguntas por mensaje. Utiliza estos emojis. Énfasis con asteriscos simples en WhatsApp. No envíes tablas, JSON, Markdown, enlaces tipo… No envíes rutas de archivos, nombres de archivos ni datos internos». Una cosa que no tenemos de pronto es: si ustedes tienen un partner que haga los domicilios, ¿cuál es el cobro que nos haría de ese domicilio? Entiendo que estamos pasando por la plataforma de MenuApp, pero en principio algunos restaurantes nos dan una listica para que la persona se pueda orientar de más o menos cuánto le va a costar de extra el domicilio. «La bienvenida y el link de la carta se envía automáticamente al comenzar la conversación. No envíes el saludo tradicional ni transcribas la carta porque justo está dentro de MenuApp». Y acá está el enlace a MenuApp. Si están viendo mi pantalla, perdón.

**[Paulo]**: Sí, perfecto.

**[Nicolás]**: Vale. Yo entendí que teníamos que enviar esta donde están ambos, DOYO y ONO. Y entonces yo le di clic acá, vi los productos —entrada, salmón— y hasta ahí logré llegar. No supe cómo continuaba la compra.

**[Paulo]**: Claro, devuélvete, devuélvete, por favor. … Claro, ahí es donde está. Oye, esa es la carta, ¿cierto? Devuélvete más. Otra. Ok. Pide aquí. … _[Navegan juntos por MenuApp: dirección en Manizales, «cambiar dirección», agregar al carrito.]_ … ¿Sabes qué creo? Señor, ¿sabes qué creo yo? Que con 2 y 2 no están activos. Ah, bueno, ok, ok, ok: creo que no están activos. Si quisiéramos hacer una prueba, la hacemos por KOMO [sic]. Pero ahí, inmediatamente él te lleva la carta, y ahí empiezas a seleccionar y agregar al carrito normal. Pues es una compra bien intuitiva.

**[Nicolás]**: Ah, listo, listo, listo. Bueno, les quería contar que yo no supe cómo hacer el proceso. Sigamos entonces acá. Datos operativos: de los pagos, el agente no cobra; se dice que existe Bold, datáfono; hay transferencia bancaria y Bre-B; y que no se acepta efectivo a domicilio. ¿Vamos bien?

**[Paulo]**: Bien.

**[Nicolás]**: Horario: lunes a viernes, o sea, en 3:30 [sic] y de 6 a 10 pm; sábado, 11 y 30 a 10 pm; y domingo, 11 y 30 a 8 y 40. Festivo, cerrado. Cobertura: Manizales, Villamaría; domicilio con una flota tercerizada —que falta la lista de los cobros de la flota que les mencionaba ahorita—. Tiempo de entrega: 30 minutos; no se hacen reservas; y que a quien hay que escalar es Ángela Bedoya.

**[Paulo]**: Sí.

### 6. Validación de la carta ONO del prompt, ítem por ítem

**[Nicolás]**: Vale, ok. Entonces yo cogí esos enlaces y lancé tres agentes para que trataran de sacar la información que estaba ahí; no disponía, digamos, como de un archivito con los precios, entonces seguramente me debe haber equivocado ahí con algunas de las descripciones. Puse entonces, Pokes: **Caribe, 34 [mil]**: arroz sushi integral, camarones, palmito de cangrejo, aguacate, repollo encurtido, mango, maíz tostado, cilantro y salsa hormon [sic]. ¿Está bien?

**[Paulo]**: Sí, señor.

**[Nicolás]**: **Acevichado, 30.000**: arroz sushi integral, pescado blanco, aguacate, maíz dulce, maíz tostado, repollo encurtido, cilantro, salsa ponzu y salsa ONO [«salsa on»].

**[Paulo]**: _[valida]_

**[Nicolás]**: **Vaya [sic], 40.000**: arroz sushi integral, tarta de atún, aguacate, repollo encurtido, cebolla crunchy, maíz dulce, mayo… Está mal escrito, ¿cierto?

**[Paulo]**: No, no, está bien escrito.

**[Nicolás]**: Sí, ahora listo, listo. Sí, sí, sí, gracias. Ok, ok. **Orange, 39.000**: arroz sushi integral, salmón, aguacate, edamame, cebollita, mango, quinoa crocante, repollo encurtido. **Paísa, 30.000**: arroz sushi integral, sobrebarriga, repollo encurtido, maíz dulce, maíz tostado, tomate cherry, lechuga, maíz sriracha y salsa ONO [«salsa oní»]. **Teriyaki, 30.000**: arroz sushi, pollo, aguacate, repollo encurtido, zanahoria, cilantro, cebolla crunchy, salsa teriyaki y topping [«tapping»] de maíz tostado. **Veggie, 28 mil**: salsa de quinoa, arroz, edamame, cebolla crunchy, maíz dulce, maíz tostado, mango, aguacate, repollo encurtido, cilantro, quinoa, aguacate, maíz sriracha [«maíz iracha»] y salsa ONO. **Onolulu [sic], 36 mil**: arroz sushi integral, camarón crocante, aguacate, mango y repollo encurtido, maíz sriracha y salsa ponzu [«ponzo»]. **Grasqui [sic], 34 mil**: arroz sushi integral, pollo crocante, aguacate, maíz tostado, repollo encurtido, salsa ONO y salsa ponzu. Este está tachado: creo que en la imagen que me habías proporcionado estaba **Poke Pork de 34**, pero entonces yo puse que no estaba disponible porque no se encontró en la otra búsqueda. ¿Aprobado?

**[Paulo]**: Sí, no: ese era un nuevo producto que estábamos sacando, pero al final no tenemos la producción de ese. Ese está… Entonces está bien, chuleado. Está bien, chuleado.

**[Nicolás]**: Listo. ONO, «Alma tu Poke» [Arma tu Poke]: precio según la construcción que se haga —una base, una proteína y hasta cuatro toppings—. Entonces la base puede ser arroz sushi integral, mix de lechugas o quinoa. La proteína: pollo teriyaki, res desmechada, pescado blanco, edamame, calamar crocante, salmón, palmitos de cangrejo, tartar de atún, camarones, camarón crocante, pollo crocante, pollo agridulce y panceta [«pan set»]. En toppings, hasta cuatro: cebolla crunchy, repollo encurtido, lechuga, mango, tomate cherry, maíz tierno [«maíz tierna»], maíz tostado [«maíz tostada»], jonjolí, zanahoria, aguacate, pepino, edamames, lenteja crocante, plátano maduro, quinoa crocante, gari, alga nori, jalapeño, wakame, chutney de piña.

**[Paulo]**: Bien ahí los toppings, bien las proteínas. Sí, señor.

**[Nicolás]**: Listo. Salsas: ponzu, mayo spicy, mayo ONO, Fuji y teriyaki. De acuerdo. Listo. Entonces, categorías y rangos: 16, 24.

**[Paulo]**: Señor.

### 7. Decisión de marca: solo ONO, DOYO en stand-by

**[Paulo]**: Nicolás, una cosita. Tengo un temita, hermano. Yo creo que es prudente —y se lo estaba comentando aquí a Steven— yo creo que es prudente omitir a DOYO de esto como marca por ahora. Yo creo que si ONO se activa seriamente, como lo estamos haciendo desde una cocina oculta, yo creo que no tendríamos como por ahora atender DOYO. Entonces yo quisiera, digamos, tener en stand-by a DOYO y dejar solo ONO. Incluso yo le puedo pedir a la gente de Menú que me lo oculte, para que sea solo una experiencia ONO. Creo que tenemos una versióncita de un enlace de solamente ONO. Yo creo que sí.

**[Nicolás]**: Tú me habías pasado de pronto una. Perdón, yo trato de buscar.

**[Paulo]**: Eso lo podríamos hacer para que probemos solo ONO. Es que no quisira… no quisiera tener una mala experiencia del cliente y que colapsemos. Prefiero ir de menos a más que generar una expectativa de venta brutal y que… Porque yo a esto le voy a meter pauta, le voy a meter todo. _[busca el enlace]_ Creo que era este el enlace que tenía. Ese es DOYO y ONO [«doyoyono»], y tengo uno que es este, donde directamente…

**[Nicolás]**: Cambiamos el link entonces. Cambiémoslo y miremos a ver si ese se pide aquí.

**[Paulo]**: Pero bueno, yo creo que eso hay que activarlo. Pero no, usa ese. Usa mejor ese. Y yo le pregunto a la gente de Rappi lo de las órdenes, y yo creo que aquí yo no puedo pedir, pero pues será como activarlo, ¿cierto? Se organiza.

**[Nicolás]**: Listo, entonces en el enlace voy a cambiar no este sino este. Luego entonces no somos DOYO y ONO, sino solo ONO… pero este dice los dos.

**[Paulo]**: Ok, entonces somos solamente uno, ¿cierto? Sí, señor: ONO Poke.

### 8. Flujo del agente y escalamiento (Ángela + Steven)

**[Nicolás]**: Listo, listo, listo. Entonces «Arma tu Poke» estaría bien. Y listo el flujo: identifica si quiere pedir; si pide el menú, se le envía el link; le ayudas a construir el pedido; confirma el nombre del producto, variante; si tiene alergias —pedía que sin maní—; resume los productos antes de pedir; confirma la zona del barrio, la dirección; verifica la cobertura; y no cobra ni pide el método de pago; dice que se lo va a pasar a Ángela y ahí termina.

**[Paulo]**: Perfecto, sí, listo. Si nos piden catering o algún tipo de pedido grande, en catering de una vez escalar a Ángela. De acuerdo; podría a otra persona al que tú consideres.

**[Nicolás]**: Sí señor. Yo se lo escalaría por ejemplo a Steven: que le llegue cuando requieran una orden especial muy grande o algo así, que lo escalen a otra persona, para que haya dos personas de contacto y que una persona responsablemente diga «hey, venga, venga, aquí puedo dar una venta grande; esto como se atiende», ¿cierto?

**[Paulo]**: Sí. Yo creo que el equipo al que escalamos, el que está pendiente del WhatsApp, es crucial para que esto funcione. ¿Qué va a pasar? Esto es como tener un practicante: uno haciendo cosas que sabe que se va a equivocar. Tenemos a alguien que está contestándole a la gente por delante, y un poco lo que se está tratando de hacer es que esté de frente al consumidor para que vea que estamos presentes, pero hay que tener a alguien que esté revisando, que le quite la conversación a la mitad. Entonces todos los que podamos poner de frente es muy bueno.

### 9. Auditoría diaria por parte de Steven (usuario en el sistema)

**[Nicolás]**: Precisamente, y yo quisiera saber eso: ¿hay forma de que Steven pueda auditar diariamente la conversación?

**[Paulo]**: Si él tiene el teléfono en el WhatsApp, simplemente se mete ahí y ve la conversación como está ocurriendo; o si no, le creamos un usuario dentro del sistema y él puede entrar en cualquier momento. Yo prefiero un usuario, para que él de manera remota, en nuestra oficina, pueda ingresar y revisar [«publicar»] la conversación que está teniendo primero el bot y segundo lo que corresponda a responsabilidad de Ángela; que veamos el nivel de respuesta, ¿me entiendes?

**[Nicolás]**: Claro que sí. Entonces yo le escribo a Steven y ya con él creo el usuario.

**[Paulo]**: De una vez, o lo creamos de una vez, como quieras. Yo digo que revisamos el robot y ya con él. Entonces solamente vamos a hablar de ONO.

### 10. Puntos a resolver y guardado del prompt

**[Nicolás]**: Y entonces algunos puntos a resolver: el mensaje de bienvenida pues yo lo veo un poquito como medio abierto; el tema de los domicilios, no tenemos las tarifas —en Menú Up yo vi unas cosas y en la entrevista parece que hay otras—, entonces como tratar de solucionar esas diferencias. Y ahí en principio habíamos dicho que teníamos una línea telefónica por cada marca, luego dijimos que lo unificamos, entonces habría que replicar el prompt. Pero creo que con esto podemos trabajar: vamos a lanzárselo hacia la gente como lo tenemos y a probar. Entonces, yo le doy aquí guardar. ¿Están viendo de pronto ahí la pantalla, cierto?

**[Paulo]**: Sí, señor.

### 11. Prueba en vivo del agente

**[Nicolás]**: Listo. Entonces aquí podemos hacer una prueba inicial. El robot tiene automatizaciones que responden sobre WhatsApp y unas que se pueden probar, digamos, aquí. Vamos con las básicas. Entonces, si quieren, yo le hago una pruebita y luego ustedes me dicen cómo hacemos para poncharlo.

**[Paulo]**: Perfecto. _[Nicolás escribe desde el panel de prueba: pide «algo vegetariano».]_

**[Nicolás]**: Ok, entonces ahí nos dio una opcioncita. No sé si esté bien: «Veggie» [«Belli»] por 28.

**[Paulo]**: ¿Y tú estás en este momento en vivo?

**[Nicolás]**: Está en vivo, está corriendo. Si le pregunto por WhatsApp me contestaría una cosa similar. Pero esto es una prueba, esto no está sucediendo en vivo. Sí, sí, o sea, le podemos preguntar lo que quieran. El robot está corriendo en este momento.

**[Paulo]**: Ah, bueno. Entonces dice: «¿tienes algo veggie?» — «Sí, claro, tenemos el Veggie por 28 mil, viene con quinoa. ¿Te gustaría pedir este poke? Si es así, ¿qué base prefieres, quinoa o arroz?». Ponle que si tiene lechuga. Vamos a asustar el bot, pues, vamos. De una. Ponle ahí, no sé: perfecto, entonces, dime todos los toppings que contiene. Dice: edamame, cebolla crunchy, maíz dulce, maíz tostado, mango, aguacate, repollo encurtido, cilantro, quinoa crocante [«crocan»]. Ponle que sí, que quisiera agregar zanahoria. Listo. ¿Alguna salsa? Ponle Fuji.

**[Nicolás]**: Tenemos la siguiente salsa: Fuji y Mayo Spicy [«Mayo Spice»].

### 12. Armado del pedido: el robot guía, MenuApp cierra

**[Nicolás]**: Yo entiendo que la idea es como que el link le arme la orden, o sea que el robot no lo calcule, ¿cierto? ¿O hacemos que el robot le calcule el precio?

**[Paulo]**: No, lo ideal sería exactamente lo que estás diciendo. Lo ideal sería que lo arme Menú, porque Menú emite la comanda a cocina. Además, no se va a equivocar en la zona. Si lo armamos desde este WhatsApp y es del robot, no va a quedar la forma de que se imprima en el punto de venta.

**[Nicolás]**: ¿Quién imprime y quién emite el pedido?

**[Paulo]**: Bueno, realmente ahí va a entrar el humano. A ver, ¿a quién le va a decir? La idea es que sea Menú el que lo diga. Entonces, digamos que la conversación está bien, pero si lo quiere ordenar, tiene que llevarlo a Menú.

**[Nicolás]**: Listo, hay que organizarle eso. Perfecto. En este momento sería como un doble trabajo: dice «¿para qué me responde y me lo arma por WhatsApp si no me lo va a facturar?». O la otra sería dejar las dos opciones. No sé, ¿tú qué dices?

**[Paulo]**: Yo creo que sería bueno que le ayude a armar, pero que la confirmación se pueda hacer a través de una página. Yo no sé si Menú puede hacer eso, como que le quede el pedido en firme, que le confirme de alguna manera. Creo que la gente está muy acostumbrada a chatbots conversacionales y estamos saliendo justo de las interfaces web. O sea, la gente no se mete a páginas, sino que habla por WhatsApp, y cada vez más el sistema agéntico va a ser la forma en la que vamos a pedir: apunta a conversación, no apunta HTML. Entonces, yo diría que le puedo dar orientaciones, pero yo no sé si Menú me pueda, o sea, lo que tú dices, que no me ponga a hacer doble trabajo, porque si no, ¿para qué lo dice? Yo diría que si aquí le decimos que se lo va a confirmar una persona, que esa persona lo monte y le dice: ok, te quedó montado acá y yo te lo pido.

_[Nicolás sigue probando en vivo; dicta algo tipo «Nicolás, voy para Miriam [¿Villamaría?]».]_

**[Paulo]**: ¿No le hemos dicho cuál es la base, cierto? Ah, sí. Y hasta ahí llegaría él. Entonces la idea es que existe una persona pendiente para que entre ahí y le diga: «ay mira, yo soy Ángela, mucho gusto, ya te confirmo el pedido». Buenísimo, está espectacular, hermano. Sí, ha funcionado súper, me parece espectacular, súper.

### 13. Configuración técnica del agente

**[Nicolás]**: Entonces aquí yo le puedo definir… le decimos aquí que esté en todas las líneas; digamos que aquí en principio tenemos una asignada. La cantidad de mensajes que él está analizando son 20 hacia atrás, subir o bajar. El modelo con el que está analizando es GPT, la versión 4 mini. Yo le puedo subir ahí a algún otro que yo quiera. Le doy guardar y ya. O sea, si le escribimos, vamos a hacer una prueba ya en caliente: voy a borrar la conversación que tiene conmigo y podemos probar desde otro teléfono.

### 14. Placeholder del link en la bienvenida

**[Paulo]**: Perdón. Aquí pasa algo, yo no sé si ustedes lo han notado, y es que cuando él responde la primera vez y pasa el enlace, el enlace tiene un placeholder, tiene una imagencita previa —que es esto— que no sé si confunda al consumidor. _[comparte pantalla]_ Entonces mira, aparece eso ahí; entonces pues él sí responde, pero yo no sé si… ¿Me puedes mandar un screen de eso para yo…?

**[Nicolás]**: Claro que sí. Voy a dejar un mensaje a Daniel que sea solo ONO [sic].

### 15. Plantilla de bienvenida ajustada a solo ONO (en vivo)

**[Nicolás]**: Ahí, como nosotros configuramos la bienvenida, aquí hay una automatización que tiene los dos enlaces. Entonces acá se lo podemos personalizar en la plantilla de bienvenida. ¿Tiene DOYO o ONO? Entonces aquí voy a quitarle… le quito DOYO, ¿cierto?

**[Paulo]**: Sí, señor.

**[Nicolás]**: Listo. Y si nos piden menú, también. … Ya no sería DOYO y ONO [«dojo uno»], sino el otro.

**[Paulo]**: Usa Menú, porque Menú descarga la comanda a cocina. Pero bueno, aquí ya, Nicolás, le pregunté a la gente de Menú, ya me respondieron; vamos a ver qué me dicen y yo te cuento cualquier cosa por chat ahorita.

**[Nicolás]**: Listo, entonces ahí tenía configurado ambos, por eso digamos que responde ahí loquito. Entonces, misma historia.

### 16. Icono de la línea

**[Paulo]**: Steven, hay que cambiarle el icono, es horroroso ese icono. Pongo un icono por ahora de ONO [«Bono»] solamente —el icono que tienes del restaurante, el que pusieron—. ¿Cómo se llama eso? La imagen de perfil. ¿Será solamente el logo? Sí, primero el logo de ONO.

### 17. Velocidad de respuesta (anti-ban) y línea API

**[Nicolás]**: Entonces aquí contesta el robot. El robot, como es una línea de QR, trata de responder despacio para que no nos vayan a banear, ¿cierto? Entonces aquí, cuando le preguntan «¿qué vende?, ¿cuál es el portafolio?», digamos que lo predeterminado es que nos pase la carta. Cuando él recibe aquí la información, comenzamos a ver qué tiene. Regularmente tiene, pues como les contaba, ese delay para cuidar la línea, para que no la vayamos a spamear. Para que quede más rápido podemos meterle una línea API que en algún momento habíamos conversado, si es que es del caso. Aquí nos llega el requerimiento —quiero un poke [«bow»]—, entonces él calcula la respuesta, como un poco lo haría una persona que está pues como ahí frente al servicio. Entonces nos pregunta cuál base quiere, cuál proteína, y hace el proceso similar que estábamos creando ahorita.

### 18. Plan hacia producción y cierre

**[Nicolás]**: Una cosa que podemos hacer es dejarlo prendido para que podamos ver cómo le va yendo al robot, y pues conforme nos salgan ajustes ustedes me los van comunicando, ¿alguna cosa? Y cuando ya veamos que no tiene errores, pues lo lanzamos ya a producción.

**[Paulo]**: Perfecto, súper. Sí.

**[Nicolás]**: Listo. Bueno, eso era como todo: el espacio, el enlacecito con el prompt para que lo puedan revisar si quieren hacerle alguna cosa. Y cualquier cambio, pues estoy súper atento.

**[Paulo]**: Listo, perfecto, Nicolás, muchas gracias. Ahí te voy a dejar en contacto con Steven para cualquier cosa. Y en teoría, nosotros… a partir de, digamos, yo voy a tener la comunicación con la gente de Menú para ver cómo integramos eso, pero ya Steven empieza a hacer seguimiento.

**[Nicolás]**: Listo. Habíamos dicho que de pronto el teléfono tenía como algunos WhatsApp y que podíamos enviar una campaña masiva para tratar de recuperar clientes. Si quieren, yo les indico cómo hacer para que la línea la podamos cargar, que podamos cargar esos prospectos.

**[Paulo]**: Eso va a ser muy importante, porque nosotros no tenemos un CRM instalado y tenemos cualquier cantidad de contactos. Entonces ahí sería bueno que le expliques a Steven cómo cargarlos y cómo protegerlos, sobre todo, y sobre todo cómo tener la data para que no se filtre, ¿me entiendes? Porque mañana se me roban esa data y se me llevan todos los clientes.

**[Nicolás]**: No, y se bloquea la línea de WhatsApp y se mueren todas las comunicaciones; ya nunca más puedes entrar y no puedes acceder a la línea.

**[Paulo]**: Es que la carguemos y que quede la basecita.

**[Nicolás]**: Sí, señor, claro que sí.

**[Paulo]**: Bueno, pues ya entonces. Sebastián, que la pasen bien. Chao, chao, gracias.

---

**Fin de la transcripción.** Registrada por MY SEO (agente LLM del harness) el 2026-10-05 a partir de la transcripción automática provista por Nicolás.
