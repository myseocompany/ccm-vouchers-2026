# Calamar Azul — acompañantes de los platos de carta (reglas confirmadas)

Reglas de acompañantes de los platos de carta, confirmadas por la gerente administrativa del establecimiento el **2026-10-31** (comunicación retransmitida por Nicolás). Esta página es la fuente canónica; el `system_prompt` del agente y el catálogo de AriCRM deben derivarse de aquí, no al contrario.

## Reglas confirmadas

| Categoría | Acompañantes |
|---|---|
| Platos de carta (regla general) | **Sin sopa y sin bebida.** La sopa y la bebida (agua de panela con limón) son exclusivas del almuerzo ejecutivo. |
| Cazuelas, sancocho, pescados de carta y especialidades | Arroz, patacón y ensalada |
| — Excepción: ensalada Brisa del Mar | Solo arroz y patacón (plato a base de verduras) |
| — Excepción: mix de mariscos | Solo arroz y patacón (plato a base de verduras) |
| Arroces | Patacón y ensalada |
| — Excepción: paella | Patacón con queso |
| Ceviches | Galletas de soda |

Texto confirmado por la cliente: «Los platos de carta sin sopa ni bebida. Los acompañantes de cazuelas, sancocho, pescados de carta y especialidades: arroz, patacón y ensalada. La ensalada brisa del mar y mix de mariscos vienen sólo con arroz y con patacón ya que son a base de verduras. Los acompañantes de arroces: patacón y ensalada. El de la paella es patacón con queso. El acompañante de ceviches son galletas de soda.»

## Actualización del mismo día (WhatsApp de la gerente, 11:38–11:40)

> «Pasta marinera viene con patacón y patacón marinero viene con ensalada» (11:38)
> «Cayana Mar Azul viene con arroz y ensalada porque la base principal es patacón con trucha» (11:40)

| Plato | Acompañantes confirmados | Observación |
|---|---|---|
| Cayana Mar Azul | Arroz y ensalada | **Corrige la carta transcrita**, que la mostraba con «arroz de coco, patacón y ensalada»: siendo la base un patacón con trucha, no lleva patacón adicional. |
| Patacón marinero | Ensalada | Pendiente confirmar si también lleva arroz (el patrón de la Cayana, también a base de patacón, lo sugiere — inferencia, no confirmación). |
| Pasta marinera | Patacón | Pendiente confirmar si también lleva ensalada (la carta transcrita la mostraba con «patacón y ensalada»). |

Patrón emergente (inferencia): los platos cuya base es el propio acompañante no lo repiten como guarnición — así como los platos a base de verduras no llevan ensalada, los platos a base de patacón no llevan patacón.

## Consistencia con fuentes previas

- La carta transcrita ya mostraba «arroz de coco, patacón y ensalada» en todos los pescados de carta, Cayana Mar Azul, sancocho de bagre, camarones al ajillo y langostinos; el propio archivo anota «Todos los pescados se muestran con arroz de coco, patacón y ensalada en el material fuente». Esta confirmación generaliza la regla por categoría.
- La sesión de coaching reportó lo mismo para las cazuelas, citando el documento de formación del personal; queda formalmente confirmado por el establecimiento.

## Detalles por confirmar

1. **Tipo de arroz**: la regla dice «arroz»; la carta transcrita especifica «arroz de coco» en todos los casos legibles, y la sesión de coaching reportó que el cliente puede pedir arroz blanco. Pendiente confirmar si el arroz estándar de estos acompañamientos es siempre de coco (con blanco como variación a petición).
2. **Langosta**: el deck de capacitación (2021) la describe «acompañada de una porción de arroz caribeño», caso específico que conviene validar contra la regla general de especialidades al estructurar el catálogo.
3. **Patacón marinero**: confirmado con ensalada; falta confirmar si también lleva arroz.
4. **Pasta marinera**: confirmada con patacón; falta confirmar si también lleva ensalada (la carta transcrita incluía ensalada).

## Qué hace el agente IA

- Responde los acompañamientos según la tabla por categoría, con sus excepciones.
- Responde Cayana Mar Azul, patacón marinero y pasta marinera según la actualización del mismo día, sin añadir acompañantes no confirmados.
- No ofrece sopa ni bebida como parte de un plato de carta; solo del almuerzo ejecutivo.
- Los cambios de acompañamiento solicitados por el cliente se toman como nota y se verifican con caja (el posible costo no está confirmado).

## Registro

- **Fecha de confirmación**: 2026-10-31.
- **Fuente**: comunicación de la gerente administrativa retransmitida por Nicolás (continuación de la confirmación del almuerzo ejecutivo del mismo día).
- **Actualización (mismo día, 11:38–11:40)**: mensajes de WhatsApp de la gerente administrativa con los acompañantes de pasta marinera, patacón marinero y Cayana Mar Azul, retransmitidos por Nicolás.
- **Guion de pruebas derivado**: `../../../clientes/mar-azul/PRUEBAS_CONVERSACIONALES.md`.
