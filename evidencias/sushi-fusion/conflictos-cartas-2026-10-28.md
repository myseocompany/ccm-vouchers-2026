# Conflictos entre cartas — Mercado Gastronómico Fusión (sushi-fusion)

- Fecha de análisis: 2026-10-28
- Insumo: 6 cartas transcritas en `evidencias/sushi-fusion/cartas/` (sushi-fusion, inca-fusion, lemon-fish, sushi-house, krabbies, rice-to-go).
- Objetivo: detectar productos/precios repetidos o en conflicto antes de cargar el catálogo al agente IA de WhatsApp.
- Regla de evidencia: cada fila cita carta + ítem + precio textual tal como aparece en la transcripción. No se infieren precios no escritos. Ningún ítem aparece marcado "ilegible"/"sin precio" en las transcripciones.

Nomenclatura de servicio (según encabezado de cada carta):
- **Mesa + domicilio**: Sushi Fusión (ancla, mesa; sin sello "solo domicilio"), Inca Fusión, Lemon Fish, Krabbies.
- **SOLO domicilio / para llevar** (sello explícito): The Sushi House, Rice To Go.

---

## 1. Tabla de conflictos (ordenada por impacto para el bot)

### A. Mismo nombre (o casi) con PRECIO DISTINTO — riesgo #1

| Producto | Cartas | Precio por carta | Tipo de conflicto | Riesgo para el bot |
|---|---|---|---|---|
| CEVICHE DE PESCADO | Sushi Fusión (Acevichados Gold) · Sushi House (Entradas) · Krabbies (Krabtacones) | SF $60.000 · SH $38.000 · Krabbies $42.000 | Mismo nombre, 3 precios, 3 productos distintos (roll gold vs ceviche vs canasta de patacón) | ALTÍSIMO: nombre idéntico pedible en la marca de domicilio (SH); diferencia de hasta $22.000 |
| COCTEL MIXTO | Sushi Fusión (Gold) · Sushi House (Entradas) · Krabbies (Krabtacones) | SF $62.000 · SH $49.000 · Krabbies $54.000 | Mismo nombre, 3 precios, 3 productos | ALTÍSIMO: triple colisión |
| CEVICHE DE CAMARÓN | Sushi Fusión (Gold) · Sushi House (Entradas) | SF $62.000 · SH $46.000 | Mismo nombre, roll gold vs ceviche entrada | ALTO: $16.000 de diferencia |
| COCTEL DE CAMARÓN | Sushi Fusión (Gold) · Sushi House (Entradas) | SF $62.000 · SH $46.000 | Mismo nombre, productos distintos | ALTO |
| CEVICHE DE LA COSTA | Sushi Fusión (Gold) · Sushi House (Entradas) · Krabbies (Krabtacones) | SF $62.000 · SH $44.000 · Krabbies $55.000 | Mismo nombre, 3 precios | ALTO: triple colisión |
| CAUSA SALMÓN | Sushi Fusión (Especiales Gold) · Inca Fusión (Causas Limeñas) | SF $65.000 · Inca $49.000 | Mismo nombre, roll vs causa limeña real | ALTO: $16.000 |
| CAUSA DE CAMARÓN / Causa Camarón | Sushi Fusión (Gold) · Inca Fusión | SF $65.000 · Inca $48.000 | Mismo nombre, roll vs causa | ALTO |
| CAUSA DE ATÚN | Sushi Fusión (Gold) · Inca Fusión | SF $66.000 · Inca $52.000 | Mismo nombre, roll vs causa | ALTO |
| PRIMAVERA | Sushi Fusión (Acevichados Peruanos Gold) · Inca Fusión (Ceviche Primavera) · Krabbies (Burgersushi/Perrushi) | SF $68.000 · Inca $59.000 · Krabbies $58.000 (burgersushi) / $53.000 (perrushi) | Mismo nombre, 3-4 precios, 3 productos | ALTO: colisión múltiple |
| ANDINO | Sushi Fusión (Gold) · Inca Fusión (Ceviche Andino) | SF $68.000 · Inca $59.000 | Mismo nombre, roll vs ceviche | ALTO |
| TRADICIONAL PERUANO | Sushi Fusión (Gold) · Inca Fusión (Ceviche Tradicional Peruano) | SF $60.000 · Inca $44.000 | Mismo nombre, roll vs ceviche | ALTO: $16.000 |
| PULPO A LA PARMESANA | Sushi Fusión (Gold) · Inca Fusión (Ceviche Pulpo a la Parmesana) | SF $64.000 · Inca $50.000 | Mismo nombre, roll vs ceviche | ALTO |
| ROCOTO | Sushi Fusión (Gold) · Inca Fusión (Ceviche Rocoto) | SF $65.000 · Inca $58.000 | Mismo nombre, roll vs ceviche | MEDIO-ALTO |
| ROCOTO JAPONÉS | Sushi Fusión (Gold) · Inca Fusión (Ceviche Rocoto Japones) | SF $65.000 · Inca $58.000 | Mismo nombre, roll vs ceviche | MEDIO-ALTO |
| OJO DE TIGRE | Sushi Fusión (Sushi otros) · Sushi House (Cocidos) | SF $46.000 · SH $42.000 | Mismo nombre, receta y precio distintos (SF lleva palmito/atún; SH palmito cangrejo + tempura) | ALTO: roll muy pedido en ambas |
| FILADELFIA | Sushi Fusión (Sushi otros) · Sushi House (Maki Rolls) | SF $38.000 · SH $36.000 | Mismo nombre, precio distinto (mesa vs domicilio) | ALTO: roll básico muy pedido |
| CALIFORNIA | Sushi Fusión (Sushi otros) · Sushi House (Maki Rolls) | SF $38.000 · SH $35.000 | Mismo nombre, precio distinto | ALTO: roll básico muy pedido |
| TORNADO SERRANO | Sushi Fusión (Especiales Gold) · Inca Fusión (Platos Ligeros Tornados) | SF $65.000 · Inca $46.000 | Mismo nombre, roll gold vs tornado ligero | ALTO: $19.000 |
| TORNADO / Tornado de Salmón | Sushi Fusión (Gold "Tornado") · Inca Fusión (Tornado de Salmón) | SF $65.000 · Inca $46.000 | Nombre casi igual, productos distintos | MEDIO-ALTO |
| CAMARONES A LA PARMESANA | Lemon Fish (Ceviche de Camarón) · Krabbies (Krabtacones) | Lemon $55.000 · Krabbies $52.000 | Mismo nombre, ceviche vs canasta patacón | MEDIO |
| NIGUIRI ATÚN (Maguro) | Sushi Fusión (Sashimi·Niguiri) · Sushi House (Niguiris) | SF $33.000 (Sashimi 60g + 2 Niguiri) · SH $30.000 (niguiri) | Distinta composición (bundle vs pieza) + precio | MEDIO: unidad de venta distinta |
| NIGUIRI SALMÓN (Sake) | Sushi Fusión · Sushi House | SF $33.000 (Sashimi 60g + 2 Niguiri) · SH $30.000 | Igual al anterior | MEDIO |
| NIGUIRI KANIKAMA (Palmitos) | Sushi Fusión · Sushi House | SF $28.000 (Sashimi 4 und + 2 Niguiri) · SH $30.000 | Bundle vs pieza; aquí SH es MÁS caro | MEDIO |
| AGUA MANANTIAL | Rice To Go · (resto de cartas) | Rice $10.000 · SF/Inca/Lemon/SH/Krabbies $12.000 | Mismo ítem, precio distinto (Rice marca "300ml personal") | MEDIO: bebida de alta frecuencia |
| FUZE TEA | Sushi House · (resto) | SH $11.000 · SF/Inca/Lemon/Krabbies/Rice $10.000 | Mismo ítem, $1.000 de diferencia | MEDIO |
| Sodas saborizadas Schweppes | Lemon Fish · Sushi Fusión / Inca / Krabbies | Lemon "Sabores" $14.000 · SF/Inca/Krabbies "saborizada" $16.000 | Mismo producto, estructura y precio distintos | MEDIO |

#### A.1 Híbridos Burgersushi/Perrushi (Krabbies) que reusan nombres de rolls de Sushi Fusión — doble precio por fila

Producto distinto (arroz de sushi en formato burger/perro), pero el **nombre colisiona** con el roll premium de Sushi Fusión y trae **dos precios** (Burgersushi / Perrushi):

| Nombre | Sushi Fusión (roll) | Krabbies Burgersushi | Krabbies Perrushi |
|---|---|---|---|
| SAKE SIRACHA | $60.000 | $58.000 | $53.000 |
| NIPPON | $62.000 | $60.000 | $57.000 |
| TUPAC AMARÚ | $60.000 (Especiales Gold) | $52.000 | $47.000 |
| EBI / EBY PARMESAN | $65.000 | $60.000 | $54.000 |
| TUNA GARI | $62.000 | $59.000 | $54.000 |
| HIMALAYA / HIMALAYA gratin | $54.000 | $50.000 | $45.000 |
| SAKE KUNSEI | $60.000 (Especiales Gold) | $56.000 | $51.000 |
| MOZZARELLA CRUNCH | $60.000 (Especiales Gold) | $56.000 | $51.000 |

Nota: "TUPAC AMARÚ" además aparece en Inca Fusión como **Pescado Tupac Amarú $70.000** y **Solomo Tupac Amarú $75.000** (platos distintos). "CEVICHE JAPONÉS" aparece dos veces dentro de Krabbies: Burgersushi $59.000 / Perrushi $54.000 **y** Krabtacón $52.000.

### B. Mismo nombre con MISMO precio — duplicado benigno (decidir en qué carta vive en el catálogo)

Bloques replicados idénticos en precio entre 2+ cartas; no confunden al bot por precio, pero deben cargarse una sola vez:

| Bloque / ítem | Cartas donde se repite | Precio idéntico |
|---|---|---|
| Coca Cola (normal/zero) | Las 6 | $10.000 |
| Jugos del Valle | Las 6 | $10.000 |
| Maracumbé | Las 6 | $14.000 |
| Té Hatsu / Hatsu | Las 6 | $14.000 |
| Soda Hatsu | Las 6 | $12.000 |
| Ginger Ale Schweppes | Las 6 | $11.000 |
| Soda Schweppes | Las 6 | $11.000 |
| Cervezas: 3 Cordilleras / Heineken / Sol / Miller Lite | Las 6 | $17.000 |
| Cerveza: Stella Artois | Las 6 | $18.000 |
| Michelado (adición a bebida) | SF, Inca, Lemon, Krabbies | $4.000 |
| Postres: Helado frito / Duraznos tempura | SF, Inca, SH, Krabbies | $20.000 |
| Postres: Turrones (maracuyá, oreo, arequipe, frutos) / Won tones mora / Won tones lychee / Suspiro limeño | SF, Inca, SH, Krabbies | $25.000 |
| Postre: Suspiro de mora | SF, Inca, Krabbies | $26.000 |
| Acompañantes: Papas a la francesa / Yuca frita / Chips de plátano | Lemon, Krabbies, Rice, SF | $15.000 |
| Acompañante: Aros de cebolla | Lemon, Krabbies, Rice | $18.000 |
| Anillos de calamar panko / IKA PANKO / Calamares al panko | SF, SH, Lemon, Krabbies | $40.000 |
| Palmitos tempura | SF (entrada), Krabbies (acompañante) | $34.000 |
| Adición Camarón / Calamar (12 und) | SF, Rice | $32.000 |
| Adición Pescado blanco (150g) / Cerdo (150g) | SF, Rice | $28.000 |
| Adición Pollo (160g) | SF, Rice | $25.000 |
| Cazuela de Mariscos | Inca, Lemon | $80.000 |
| Ceviche de Chicharrón | Lemon (ceviche), Krabbies (krabtacón) | $40.000 |

### C. Colisiones de nombre ambiguas (misma palabra, distinto producto/estructura)

| Caso | Detalle | Riesgo |
|---|---|---|
| "Chaufa" Inca vs Rice To Go | Inca: platos de chaufa a **precio único** de mesa (Chaufa de Pollo $62.000, Mar y Tierra $88.000, Trilogía $70.000, Mariscos $82.000, Solomito $65.000). Rice To Go: **PERÚ CHAUFA** por 3 tamaños (Familiar $92.000 / Media $82.000 / Personal $55.000), solo domicilio. Inca NO tiene tamaños familiar/personal. | ALTO: "quiero una chaufa" es ambiguo entre marca mesa y marca domicilio con precios y gramaje distintos |
| Rolls mesa vs domicilio | Nombres compartidos (Filadelfia, California, Ojo de Tigre) existen en Sushi Fusión (mesa) y The Sushi House (domicilio) con recetas y precios distintos | ALTO (ya listados en sección A) |
| Niguiris | Sushi Fusión vende Sashimi+2 Niguiri como bundle; Sushi House vende niguiri suelto. Mismo nombre de pescado, unidad de venta distinta | MEDIO |
| Rainbow Maki vs Arco Iris | SH "RAINBOW MAKI" $47.000 ≈ concepto de SF "ARCO IRIS" $54.000 (nombre traducido, precio y receta distintos) | BAJO-MEDIO |

### D. Mismo nombre, distinta GRAMÁTICA de precio

| Carta | Estructura de precio | Choque con |
|---|---|---|
| Lemon Fish — Ceviches de Pescado | Precio **base + recargo por proteína** (Salmón +$10.000, Atún +$10.000, Tilapia +$7.000, Trucha +$8.000, Pescado Blanco +$0). Ej.: "PESCADO TRADICIONAL $40.000 base" | Resto de cartas usan precio único; el bot debe saber calcular base+recargo |
| Rice To Go — todos los arroces | **3 tamaños** por producto (Familiar / Media Caja / Personal) | Inca/SF venden arroces y chaufas a precio único |
| Sushi Fusión — Sashimi·Niguiri | **Bundle** (sashimi en gramos + 2 niguiri) | Sushi House vende niguiri por pieza |
| Krabbies — Burgersushi/Perrushi | **Dos precios por fila**; además Krabbdog "con arroz de sushi al panko +$10.000" y combo "+$25.000" | Resto usa precio único |

---

## 2. Recomendación de desduplicación (regla por tipo)

1. **Rolls / sushi con nombre compartido (Filadelfia, California, Ojo de Tigre, etc.):** para pedidos **a domicilio / para llevar usar SIEMPRE The Sushi House** (es la carta sellada "SOLO A DOMICILIO O PARA LLEVAR"); la versión de **Sushi Fusión es solo mesa**. Cargar ambas como SKUs separados etiquetados por canal (`_mesa` vs `_domicilio`) y nunca mezclar precios.

2. **Ceviches / cocteles / causas / tornados con nombre compartido:** son productos **distintos** aunque compartan nombre. Separar por marca:
   - "Ceviche/Coctel X" pedido como **plato de entrada a domicilio** → The Sushi House (o Lemon Fish para su carta de ceviches).
   - "Ceviche/Causa/Tornado/Primavera/Andino… X" como **roll Acevichado/Especial Gold** → Sushi Fusión (mesa), categoría "Gold", precio $60.000–$68.000.
   - Versión en **canasta de patacón** → Krabbies (Krabtacón).
   Marcar cada uno con prefijo de categoría para desambiguar ("Roll Gold –", "Ceviche –", "Krabtacón –").

3. **Combos The Sushi House (HOUSE 30 $95.000 · ESPECIAL 50 $145.000 · SUPERIOR 70 $220.000 · PREMIUM 100 $270.000):** cargarlos UNA sola vez desde la carta The Sushi House (fuente canónica, domicilio). **Los "COMBOS FUSIÓN" de Sushi Fusión son otros combos** (NIKKEI $185.000, MOZARELLA/NIKKO/PRIMAVERA/NIPPON/LIMA PANKO/ACEVICHADO $165.000, Combo 1 y Combo 2 $165.000) — no confundir. Ver duda #1 sobre la referencia cruzada.

4. **Bloques compartidos con precio idéntico (bebidas, cervezas, michelados, postres, acompañantes):** definir **una sola carta "fuente de verdad"** para estos bloques (sugerido: **Sushi Fusión** como marca ancla) y no replicarlos por marca en el catálogo, salvo las excepciones de precio distinto (ver puntos 5–7).

5. **Agua Manantial:** confirmar con el establecimiento; cargar $12.000 como precio general y, si Rice To Go realmente vende presentación 300ml a $10.000, cargarla como SKU aparte "Agua Manantial 300ml".

6. **Fuze Tea:** unificar; usar $10.000 (5 de 6 cartas) salvo que The Sushi House confirme $11.000.

7. **Sodas saborizadas:** usar $16.000 (saborizada) + $14.000 (michelada tradicional) como en SF/Inca/Krabbies; verificar el $14.000 de Lemon Fish.

8. **Lemon Fish ceviches de pescado:** cargar como producto con **modificador obligatorio de pescado** (precio base + recargo), no como precio fijo.

9. **Rice To Go:** cargar cada arroz con **selector de tamaño** (Familiar/Media/Personal); mantener la palabra "chaufa" desambiguada ("Rice – Perú Chaufa" vs "Inca – Chaufa de Pollo").

10. **Krabbies Burgersushi/Perrushi:** cada ítem es un SKU con **dos variantes** (Burgersushi / Perrushi); no fusionar con el roll homónimo de Sushi Fusión.

---

## 3. Dudas para el establecimiento

1. **Referencia cruzada de combos Sushi House dentro de la carta Sushi Fusión:** el encabezado de `carta-sushi-fusion.md` dice que incluye una sección "combos Sushi House SOLO A DOMICILIO / PARA LLEVAR" como referencia, **pero el cuerpo transcrito no contiene esa tabla con precios**. No se puede confirmar desde las cartas si los precios ahí coinciden con The Sushi House (HOUSE $95.000 / ESPECIAL $145.000 / SUPERIOR $220.000 / PREMIUM $270.000). ¿Es solo un puntero o había una tabla con precios? Pedir la página faltante.
2. **Agua Manantial $10.000 (Rice To Go) vs $12.000 (resto):** ¿es por presentación 300ml más pequeña o es un error? ¿Cuál rige para domicilio?
3. **Fuze Tea $11.000 (Sushi House) vs $10.000 (resto):** ¿intencional o error de carta?
4. **Sodas saborizadas Schweppes $14.000 (Lemon Fish "Sabores") vs $16.000 (SF/Inca/Krabbies):** ¿mismo producto a distinto precio o son productos distintos (michelada vs saborizada)?
5. **Niguiris:** Sushi Fusión los vende como "Sashimi + 2 Niguiri" (bundle) y Sushi House como niguiri suelto. ¿El catálogo del bot debe ofrecer niguiri por pieza, por bundle, o ambos según canal?
6. **Canal por marca:** confirmar oficialmente qué marcas aceptan pedido a domicilio por el bot. Las cartas marcan solo a The Sushi House y Rice To Go como "exclusivo domicilio/para llevar"; Sushi Fusión, Inca, Lemon y Krabbies traen WhatsApp de domicilio pero están rotuladas como carta de mesa. ¿El bot puede vender platos de mesa (p. ej. Teppan, Wok, platos fuertes Inca) a domicilio?
7. **Papa frita vs Trozos de papa frita (Rice To Go):** "Papas a la francesa 150g $15.000" (acompañante) vs "Trozos de papa frita 150g $16.000" (adición). ¿Son productos distintos o duplicado con $1.000 de diferencia?
8. **Nombre idéntico, producto distinto (Causa, Primavera, Andino, Tradicional Peruano, Tornado Serrano, Ceviche de Pescado, etc.):** confirmar la nomenclatura final que verá el cliente para que el bot no ofrezca el roll Gold cuando piden el ceviche/causa de Inca o Sushi House (y viceversa).
