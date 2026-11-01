# Menú DOYO y ONO — snapshot de Menüpp

**Fuente:** [Menüpp — DOYO y ONO](https://menupp.co/doyoyono/venue/HL0hbbttgdQVfSFhSfnf/menu/tsFpduQ47fZCV6LkKkzn)  
**Descargado:** 2026-10-28  
**Alcance:** 8 categorías, 26 productos y 45 variantes públicas. Los JSON originales se guardan en `storage/trattorias-download/menupp-2026-10-28/`.  
**Uso:** es un snapshot operativo. Antes de comunicar disponibilidad, promociones, precio o domicilio a un cliente, el agente debe consultar las tools vigentes; este archivo no sustituye el catálogo en tiempo real.

**Cargado a producción (2026-10-28):** 5 categorías y 24 ítems subidos al tenant Trattorias y Pastificios S.A.S. (`01a0c5d9-0f5c-73ba-b0ae-0e663da0507f`, marca ONO; `01a184ce-9e20-72c5-a72c-d21cc47823cf` es su sede Belén) vía script idempotente (`upload-menu-items.php` + `ono-menu-upload.json` en esta misma carpeta). Se omitieron `Grande` y `Pequeño` (config de carta, precio $0, semántica sin confirmar) y `Arma Tu Poke` quedó `is_available=false` con las reglas del bowl en su descripción, a la espera del precio del tenant.

## Estado del catálogo

- Productos activos publicados: 24.
- Productos deshabilitados en la fuente: Cerveza en Botella y Poke Pork Belly; no ofrecerlos.
- El producto `Arma Tu Poke` tiene precio base $0 y se compone con las opciones publicadas abajo. La fuente no expone en este snapshot un precio final independiente para el bowl.
- `Grande` y `Pequeño` aparecen como productos de precio $0 dentro de Pokes; tratar como configuración de la carta, no como productos vendibles aislados, hasta que `get_catalog` confirme su semántica.

## Pokes

| Producto | Precio | Composición publicada |
|---|---:|---|
| Poke Acevichado | $30.000 | Arroz sushi o integral, pescado blanco, aguacate, repollo encurtido, mango, pico de gallo, maíz dulce/tostado, cilantro, ponzu y salsa ONO. |
| Poke Bahía | $40.000 | Arroz sushi o integral, tartar de atún, aguacate, repollo encurtido, cebolla crunchy, maíz dulce y mayo sriracha. |
| Poke Orange | $39.000 | Arroz sushi o integral, salmón, aguacate, edamame, mango, repollo encurtido, mayo sriracha y ponzu. |
| Poke Paisa | $30.000 | Arroz sushi o integral, sobrebarriga desmechada, repollo encurtido, maíz dulce/tostado, tomate cherry, lechuga, mayo sriracha y salsa ONO. |
| Poke Teriyaki | $30.000 | Arroz sushi o integral, pollo teriyaki, aguacate, repollo encurtido, zanahoria, cilantro, cebolla crunchy, maíz tostado y teriyaki. |
| Poke Veggie | $28.000 | Quinoa, arroz sushi o integral; edamame, aguacate, repollo encurtido, mango, lenteja crocante, cilantro, cebolla crunchy, maíz tostado, mayo sriracha y salsa ONO. |
| Poke Honolulu | $36.000 | Arroz sushi o integral, camarón crocante, aguacate, repollo encurtido, mango, maíz dulce, mayo sriracha y ponzu. |
| Poke Kraskí | $34.000 | Arroz sushi o integral, pollo crocante, aguacate, repollo encurtido, mango, edamame, maíz tostado, ponzu y salsa ONO. |
| Poke Caribe | $34.000 | Arroz sushi, kanikama, camarón, maíz tostado, mango, repollo encurtido, cilantro y salsa ONO. |
| Poke Pork Belly | $34.000 | **Deshabilitado.** No ofrecer. |

## Arma tu Poke

| Producto | Precio base | Reglas publicadas |
|---|---:|---|
| Arma Tu Poke | $0 | Elegir 1 base, 1 proteína, de 1 a 4 toppings y de 1 a 5 salsas. |

### Base — elegir 1

- Arroz de Sushi
- Mix de Lechugas
- Quinoa
- Arroz Integral

### Proteínas — elegir 1

- Res Desmechada
- Camarón Crocante
- Panceta
- Tartar de Atún
- Camarones
- Pollo Teriyaki
- Edamame
- Salmón
- Pollo Agridulce
- Palmitos de Cangrejo
- Calamar Crocante
- Pollo Crocante
- Pescado Blanco

### Toppings — elegir de 1 a 4

- Maíz tierno, chutney de piña, jalapeño, gari, ajonjolí, mango, lechuga
- Aguacate, zanahoria, wakame, edamames, lenteja crocante, plátano maduro
- Quinoa crocante, tomate cherry, repollo encurtido, maíz tostado, pepino
- Cebolla crunchy, alga nori

> La fuente contiene dos entradas de aguacate; se presenta una sola vez en esta guía, pero ambas permanecen en `variants.json` para trazabilidad.

### Salsas — elegir de 1 a 5

- Mayo ONO
- Mayo spicy
- Teriyaki
- Fuji
- Ponzu

### Adiciones de toppings — deshabilitadas

La categoría `Adición de Toppings` está marcada como deshabilitada en Menüpp. No ofrecer sin confirmación en tiempo real. Sus variantes publicadas son zanahoria (+$1.000) y salmón (+$8.000).

## Bebidas

| Producto | Precio | Estado |
|---|---:|---|
| Té Hatsu | $10.000 | Disponible |
| Gaseosa | $7.000 | Disponible |
| Agua | $7.000 | Disponible; la fuente muestra dos variantes al mismo precio. |
| Cerveza en Lata | $8.000 | Disponible |
| Cerveza en Botella | $10.000 | **Deshabilitada** |
| Copa de Vino de la Casa | $18.000 | Disponible |
| Media Botella de Vino de la Casa | $80.000 | Disponible |
| Botella de Vino de la Casa | $120.000 | Disponible |

## Bebidas calientes

| Producto | Precio |
|---|---:|
| Café Americano | $6.000 |
| Espresso | $6.000 |
| Capuccino | $8.000 |

## Postres

| Producto | Precio |
|---|---:|
| Galleta ONO | $7.500 |
| Postre del Día | $16.000 |

## Categorías visuales sin productos vendibles

Menüpp también publica tres categorías de tipo banner (`banne pokes`, `banner bowl` y `banner delicioso`). Son elementos visuales de la carta y no deben interpretarse como productos, precios ni promociones.

## Archivos de evidencia

- `menu.json`: configuración de menú, moneda, horarios y metadatos publicados.
- `categories.json`: categorías y banners.
- `products.json`: los 26 productos, descripciones, precios, estado y relación con categorías.
- `modifiers.json`: reglas de selección para el bowl.
- `variants.json`: las 45 bases, proteínas, toppings, salsas y adiciones, con precio y estado.

No se versionan estos archivos de descarga sin revisión explícita: son una instantánea externa y pueden cambiar sin aviso.
