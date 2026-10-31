> **Copia de evidencia — archivada el 2026-10-30.** Captura fiel de docs/mar-azul/domicilios-cable.md en el repositorio velo_wa, worktree `calamar_azul`, rama `myseocompany/calamar_azul`.
> El cuerpo no se modifica. Las rutas relativas que aparecen dentro del documento (`docs/mar-azul/…`, rutas de
> `app/`) resuelven en ese repositorio, no en este harness; el validador las reporta como referencias rotas y es
> esperado. Este harness no edita `velo_wa`: los cambios de código se piden como tareas en ese repositorio.

# Calamar Azul — tarifas de domicilio, sede Cable

Tabla oficial barrio → tarifa de la **sede Cable**, cargada a producción el **2026-10-30**.

Fuente primaria: transcripción de WhatsApp de Yady del 2026-10-16 (`domicilios_cable.md` en la raíz del repo), organizada por comuna de Manizales. Equivalente de Centro: `docs/mar-azul/domicilios-centro.md`.

## Estado en producción (Waterfall)

| Elemento | Valor |
|---|---|
| Tenant | `01a0fcc8-7908-71e0-ac67-c8aca5e05bf2` · slug `grupo-d-mar-azul-sas-LQ3L` |
| Sede (Branch) | `Sede Cable` (`01a14579-4916-7150-af8f-6f805542d8b1`) · slug `cable` · `sort_order` 1 — única sede **activa** (Sede Centro existe inactiva) |
| Tarifas activas | **133** (`delivery_tariffs`), 7 bandas de precio |
| Reemplazo | Los 3 placeholders del onboarding (`Tarifa mínima/intermedia/lejana — barrio pendiente`, $5.000/$8.000/$12.000) fueron eliminados |
| Respaldo previo | `waterfall:/home/forge/calamar-cable-tariffs-backup-20261030.json` (3 filas, modo 0600) |

## Tarifas por banda

| Tarifa | Barrios | Detalle |
|---|---|---|
| $6.000 | 24 | Arboleda, Belén, Camelia, El Campín, El Sol, El Trébol, Guayacanes, La Argentina, La Asunción, La Estrella, La Leonora, La Rambla, Laureles, Lleras, Los Cedros, Milán, Palermo, Palo Grande, Rosales, San Jorge, Sancancio, Santa Elena, Versalles, Villa del Río |
| $7.500 | 41 | Altos de Capri, Altos de Granada, Aranjuez, Betania, Bosques del Norte, Camilo Torres, Campoamor, Castilla, Centro, Comuneros, El Aguacate, El Caribe, El Encuentro, El Porvenir, Fanny González, Fundadores, Fátima, Kennedy, La Carola, La Carolita, La Paz, Las Américas, Las Colinas, Los Agustinos, Malabar, Palo Negro, Peralonso, Portón del Guamo, Puerta del Sol, Pío 12, Samaria, San Cayetano, San Joaquín, San Luis, San Sebastián, Sinaí, Solferino, Villa Café, Villa Julia, Villahermosa, Vivienda Popular |
| $8.000 | 35 | Alférez Real, Arrayanes, Asís, Avanzada, Bajo Andes, Bajo Prado, Barrio Colombia, Centenario, Cervantes, Colón, El Bosque, El Carmen, El Palmar, Estambul, Estrada, Eucaliptos, Galán, González, Guamal, Jazmín, La Isabela, Las Delicias, Las Águilas, Marmato, Nevado, Nogales, Panamericana, Paraíso, Persia, Prado, San Antonio, San Ignacio, San José, Uribe Vélez, Villa Carmenza |
| $8.500 | 15 | Alta Suiza, Baja Suiza, Bosques de Niza, Colseguros, La Cumbre, La Sultana, La Toscana, Licorera, Minitas, Residencias Manizales, Villa Luz, Viveros, Yarumales 1, Yarumales 2, Yarumos |
| $10.000 | 8 | Alcázares, Bella Montaña, Campo Hermoso, Cerro de Oro Ecoturístico, Chipre, La Francia, Sacatín, Villa Pilar |
| $13.000 | 9 | Alhambra, Cerros de la Alhambra, Chachafruto, La Enea, La Linda, Lusitania, Maltería, San Marcel, Zona Industrial |
| $15.000 | 1 | Turín Villa María |

## Correspondencia con las comunas de la fuente

| Comuna (fuente) | Tarifa |
|---|---|
| 1 Atardeceres | $10.000 |
| 2 San José | $8.000 |
| 3 Cumanday | $7.500 |
| 4 Estación | $6.000 |
| 5 Ciudadela del Norte | $7.500 |
| 6 Cerro de Oro | $8.500 |
| 7 Tesorito | $13.000 |
| 8 Palogrande | $6.000 |
| 9 Universitaria | $7.500 |
| 10 La Fuente | $8.000 |
| 11 La Macarena | $8.000 |
| 12 Nuevo Horizonte | $7.500 |
| Lejanos: Cerro de Oro Ecoturístico | $10.000 |
| Lejanos: La Linda | $13.000 |
| Lejanos: Turín Villamaría | $15.000 |

Nombres que la fuente traía pegados por el formato de WhatsApp y que se separaron al cargar:

- Comuna 3: `San Joaquín Campoamor Fundadores` → **San Joaquín**, **Campoamor**, **Fundadores**
- Comuna 5: `Altos de Capri bosques del Norte` → **Altos de Capri**, **Bosques del Norte**
- Comuna 6: `Yarumales 1 y 2 Licorera` → **Yarumales 1**, **Yarumales 2**, **Licorera**
- Comuna 7: `Cerros de la alhambra  Lusitania` → **Cerros de la Alhambra**, **Lusitania**
- Comuna 12: `La Carola Villahermosa Comuneros` → **La Carola**, **Villahermosa**, **Comuneros**
- Comuna 12: `Portón del guamo Sinaí` → **Portón del Guamo**, **Sinaí**

## Pendiente: 3 barrios con tarifa contradictoria

La fuente asigna dos precios distintos al mismo barrio. Como la DB impone `(branch_id, barrio)` único (`database/migrations/2026_10_03_000004_create_delivery_tariffs_table.php:24`) y el resolver es determinista, **no se cargaron**: el agente responde `ZONE_NOT_COVERED` y escala en vez de cotizar un precio inventado.

| Barrio | Precio A | Precio B |
|---|---|---|
| Arenillo | $10.000 (Comuna 1 Atardeceres) | $8.000 (Comuna 11 La Macarena) |
| La Castellana | $8.000 (Comuna 11 La Macarena) | $7.500 (Comuna 12 Nuevo Horizonte) |
| Santos | $7.500 (Comuna 9 Universitaria) | $8.000 (Comuna 10 La Fuente) |

Hay que confirmar con el negocio cuál es el precio correcto de cada uno (o si corresponden a sectores distintos que deban cargarse con nombres distintos) y luego crearlos desde Settings → Sedes → Tarifas.

El mismo conflicto aparece en los tres barrios en la fuente de **sede Centro**, con otros precios. Eso refuerza que es un problema de límite de comuna y no de digitación: conviene resolverlo una sola vez para ambas sedes.

## Comportamiento del resolver

`app/Services/Orders/DeliveryTariffResolver.php` resuelve **solo por coincidencia exacta del barrio normalizado** (minúsculas, sin tildes, sin puntuación, espacios colapsados) o por alias registrado — nunca por subcadena, dirección ni nombre de sede.

Verificado en producción tras la carga:

| Entrada del cliente | Resultado |
|---|---|
| `chipre` | Chipre · $10.000 |
| `LA LEONORA` | La Leonora · $6.000 |
| `Turin Villa Maria` | Turín Villa María · $15.000 |
| `la enea` | La Enea · $13.000 |
| `palogrande` | no cubierto |
| `enea` | no cubierto |
| `Arenillo` / `Santos` | no cubierto (conflicto pendiente) |

**Sin aliases cargados todavía.** Las formas cortas o pegadas que la gente escribe de verdad (`palogrande`, `enea`, `la alhambra`, `bosques`, `ciudadela`) no resuelven y caen en escalamiento. Vale la pena sembrar `delivery_tariff_aliases` con las variantes más frecuentes una vez haya corpus de pedidos reales de la sede Cable.

## Recarga de la tabla

La carga se hizo con un script temporal vía `php artisan tinker` sobre Waterfall, dentro de una transacción (borra las tarifas de la sede y reinserta las 133). Para repetirla o ajustarla, la tabla de esta página es la fuente canónica. Cambios puntuales de una sola tarifa se hacen desde la UI (Settings → Sedes → Tarifas), que valida la ambigüedad de normalización en `app/Http/Requests/Api/StoreDeliveryTariffRequest.php`.
