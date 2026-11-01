# Análisis de fricción de menú — Beto's Pizza

- **Fecha**: 2026-10-05. Análisis asistido por LLM sobre la exportación de conversaciones (`raw/waterfall-conversaciones-2026-10-05.json`), el reporte cuantitativo (`analisis-conversaciones-2026-10-05.md`) y las preguntas redactadas (`raw/analisis/preguntas-clientes-redactadas.md`, fuera de git).
- **Método**: reclasificación semántica de los 125 turnos del bucket «Otras preguntas», cruzada con las categorías del script y contrastada contra la secuencia de bienvenida (`clientes/pizzas-beto/PLANTILLAS_WHATSAPP.md`), la carta transcrita (`vertical-restaurantes/menu/menu-estructurado-carta-2026-10-05.md`) y el prompt v0 (`ia-conversacional/prompt-v0-borrador.md`).
- **Convención**: conteos = hecho observado; lecturas = inferencia marcada como tal. Citas de clientes ya redactadas. Ningún dato aquí reemplaza la validación del establecimiento.

## A) Reclasificación del bucket «Otras preguntas» (125 casos)

| # | Subtema | ~Casos | Ejemplos redactados |
|---|---|---:|---|
| 1 | Disponibilidad del servicio / gate de apertura («¿tienen domicilio?», «¿aún atienden?») | 18 | «tienen servicio?», «Aún tienen domicilio?», «aun trabajan?» |
| 2 | Saludos, cortesía y ruido no accionable | 13 | «Hola Cómo estás?», «??», enlace de Instagram |
| 3 | Cierre de cuenta: «¿cuánto sería todo?» (total con domicilio/bebida) | 11 | «Cuánto sería en total?», «Sería 125000?», «Cuánto seria todo» |
| 4 | Bebidas: qué hay, marcas, sabores, presentaciones | 9 | «Que gaseosa tienes?», «tienes naranja?», «Tienes limonada?» |
| 5 | Productos fuera de carta o disponibilidad puntual (pan de ajo, calzone, estofada, dulce) | 9 | «Tienes panes de ajo?», «Calzone y estofada tienen?», «vendes algo dulce?» |
| 6 | Pago: medios, titularidad de cuenta, anticipo, devuelta | 7 | «Que medio de pago tienes?», «se requiere un anticipo?» |
| 7 | Estado/seguimiento del pedido | 7 | «Sabes por dónde viene el domi?», «ok ya salieron?» |
| 8 | Sede/ubicación/recogida y multisede (Palermo, multicentro, parque Caldas) | 8 | «Ustedes no son sede Palermo?», «En el parque caldas?» |
| — | Resto (~43): mitad-y-mitad (~4), fragmentos de pedido en curso (~8), B2B/vouchers (~5), instrucciones de entrega (~3), quejas (~3), escapes de tiempo (~3), tarifa por zona (~3), grupos/eventos (~3), ingredientes «qué trae» (~3), horario (~2), cambio de pedido (~2), factura/NIT (1), ambiguos (~2) | 43 | — |

**Inferencia clave**: ~60 % del bucket «otras» es operativa de pedido real (disponibilidad, total, bebidas, pago, seguimiento) que ni el menú ni la autorrespuesta cubren; ~10 % es ruido extraíble.

## B) Elementos que el menú debe aclarar (priorizados, 11)

### 1. Política mitad-y-mitad (dos sabores en una pizza) — fricción #1
- **Falta hoy**: ninguna fuente dice si se puede, en qué tamaños, con qué combinaciones ni si tiene recargo.
- **Evidencia**: ~25–30 turnos en el dataset (18 en «Tamaños», ~6 en «Sabores», ~4 en «otras»). Patrones: «Se puede mitad y mitad carnes hawaiana Para una Familiar», «La personal es de solo un sabor o se pueden 2?».
- **Dónde**: bienvenida + carta imagen + regla del agente IA. **(iv) Validar**: ¿aplica en personal y small?, ¿recargo?, ¿mezclas permitidas?

### 2. Combo gaseosa incluida: qué tamaños la traen y de qué presentación
- **Falta hoy**: contradicción — la bienvenida dice mediana y familiar «+ gaseosa»; el menú estructurado no registra gaseosa incluida (bebidas aparte $1.500–$7.000).
- **Evidencia**: ~10 turnos: «las individuales van solas sin la gaseosa?», «Viene con gaseosa, verdad?», «la gaseosa es grande?».
- **Dónde**: **(iv) validar primero** (si el combo existe y qué presentación); luego bienvenida, carta y agente. Riesgo: activar la bienvenida sin validar hereda una promesa posiblemente incumplida.

### 3. Tamaños: nomenclatura, porciones y mapeo precio↔tamaño
- **Falta hoy**: los clientes ordenan por precio o porciones («pizza de 20 mil», «de 6 porciones»), no por nombre; la restricción «porción sola solo hawaiana o carnes» no es visible.
- **Evidencia**: 50 turnos en «Tamaños» + ~4 en «otras».
- **Dónde**: bienvenida (tabla precio→tamaño→porciones→para cuántas personas), carta, agente (mapear apodos). **(iv) Validar**: porciones exactas por tamaño. **Contradicción interna**: plantilla dice mediana «8 porciones pequeñas» vs menú estructurado «8 medianas»; expectativa de precio desalineada («Mediana cuesta 25?» vs $55.000).

### 4. Catálogo de bebidas: marcas, sabores y presentaciones
- **Falta hoy**: la carta lista «Gaseosa» genérica (7 oz/400 ml/1,5 L) sin marcas; los clientes piden Pepsi, «manzana», «naranja», «2 litros», limonada, jugo natural.
- **Evidencia**: ~15 turnos.
- **Dónde**: carta imagen con marcas/presentaciones + agente. **(iv) Validar**: marcas reales, si hay 2L y jugos naturales.

### 5. Tarifa de domicilio por zona y cobertura
- **Falta hoy**: la carta no incluye domicilio; la bienvenida dice «$5.000 reportado» sujeto a validación; no hay tabla por barrio.
- **Evidencia**: 27 turnos en «Cobertura» + ~4 en «otras»: «que vale un domicilio hasta el sena?», «que valdría el domicilio a Villamaria?».
- **Dónde**: **(iv) validar** tabla por zona (Villamaría, La Linda, Enea, Alcázares…); luego agente con esa tabla.

### 6. Horario y estado del servicio (abierto/cerrado)
- **Falta hoy**: la autorrespuesta no informa horario; discrepancia documentada entre sitio público y horario reportado.
- **Evidencia**: 18 turnos de gate «¿tienen servicio?» + 4 de horario + ~4 dispersos. Tráfico intenso 23:00–04:00 sin respuesta.
- **Dónde**: **(iv) validar** horario real; luego bienvenida y agente con estado por contexto temporal.

### 7. Medios de pago, titular de cuenta y «devuelta»/anticipo
- **Falta hoy**: ninguna fuente publica los medios aceptados; el flujo de «devuelta» no está formalizado.
- **Evidencia**: 28 en «Pago» + ~7 en «otras» ≈ 35: «No tienen datáfono?», «A nombre de quien aparece el Nequi?», «se requiere un anticipo?».
- **Dónde**: **(iv) validar** medios, titular, política de anticipo; bienvenida con lista de medios (sin números); agente capturando monto de pago/devuelta.

### 8. Sabores e ingredientes consultables + modificaciones
- **Falta hoy**: ingredientes en menú estructurado pero no consultables en la operación; sin política de modificaciones.
- **Evidencia**: 21 en «Sabores» + ~3: «Cómo es la hawaiana que trae»; modificaciones reales: «sin champiñones» (repetido), «solo quesos».
- **Dónde**: carta con ingredientes legibles + agente. **(iv) Validar**: costo de quitar/agregar ingredientes.

### 9. Complementos que el cliente espera y no están en carta
- **Falta hoy**: no hay entradas ni postres; los clientes asumen pan de ajo, calzone, algo dulce.
- **Evidencia**: 8 turnos; «Tienes panes de ajo?» aparece 3 veces.
- **Dónde**: **(iv) validar** si existen complementos fuera de carta; agente con respuesta definida «no lo manejamos» + alternativa.

### 10. Sede, recogida y multisede
- **Falta hoy**: ni bienvenida ni carta publican dirección ni opción de recoger; hay referencias recurrentes a sedes antiguas (Palermo, multicentro, parque Caldas).
- **Evidencia**: 6 en «Ubicación» + ~8 en «otras» ≈ 12–14.
- **Dónde**: **(iv) validar** sedes y dirección de recogida; luego bienvenida y agente.

### 11. Pedidos para grupos/eventos, anticipación y canales corporativos
- **Falta hoy**: sin política de anticipación ni precios por volumen; el prompt v0 escala a humano.
- **Evidencia**: ~7 turnos: «en cuanto quedarían 40-50 porciones», «Si son para el 18 con cuánto tiempo debo hacer el pedido?»; incluye pedidos corporativos de bonos del propio programa.
- **Dónde**: **(iv) validar** capacidad/anticipación/precio por volumen; agente cotizando con escalamiento.

## C) Hallazgos de fricción en pedidos reales

1. **La mitad-y-mitad es la mayor fricción de menú sin documentar** (~25–30 turnos, ≈8–9 % del dataset), concentrada en personal y small, patrón «2 de carnes y 2 hawaianas».
2. **El combo-gaseosa es una promesa ambigua con riesgo de incumplimiento**: la bienvenida lo promete, la carta no lo registra; los clientes dudan incluso en porción/personal y encadenan pregunta por marca/tamaño.
3. **El cliente ordena por precio y por número de porciones, no por nombre de tamaño**; hay contradicción interna entre fuentes sobre las porciones de la mediana (8 pequeñas vs 8 medianas) que debe conciliarse antes de activar secuencias.
4. **Dos datos bloquean casi todos los cierres de venta**: tarifa de domicilio por zona y estado del servicio. El arquetipo «¿cuánto sería todo?» (~22 turnos) depende del domicilio al barrio específico; el gate «¿tienen servicio?» (25 líneas) se concentra 23:00–04:00 sin respuesta.
5. **Canales y sedes paralelos sin trazabilidad**: pedidos hechos por la web cuyo estado se pregunta por WhatsApp, confusión de multisede y ~13 turnos de seguimiento «¿ya salió?» sin herramienta de estado; ingresa además prospección B2B.
