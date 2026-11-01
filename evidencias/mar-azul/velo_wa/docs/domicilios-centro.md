# Calamar Azul — tarifas de domicilio, sede Centro

Tabla oficial barrio → tarifa de la **sede Centro**, cargada a producción el **2026-10-30**.

Fuente primaria: `docs/mar-azul/fuentes/domicilios-centro-2026-10-15.md` (transcripción de WhatsApp de Yady del 2026-10-15), organizada por comuna de Manizales. Equivalente de Cable: `docs/mar-azul/domicilios-cable.md`.

## Estado en producción (Waterfall)

| Elemento | Valor |
|---|---|
| Tenant | `01a0fcc8-7908-71e0-ac67-c8aca5e05bf2` · slug `grupo-d-mar-azul-sas-LQ3L` |
| Sede (Branch) | `Sede Centro` (`01a18e9a-26a8-7136-a92f-bd81bec466bd`) · slug `centro` · `sort_order` 2 · `whatsapp_line_id` null |
| Estado | **`is_active = false`** — ver "Por qué la sede nace inactiva" |
| Tarifas activas | **133** (`delivery_tariffs`), 10 bandas de precio |
| Universo de barrios | Idéntico barrio por barrio al de Sede Cable (diff vacío contra producción), misma grafía canónica |

## Por qué la sede nace inactiva

Activarla cambia lo que el bot le dice al cliente, y el prompt todavía no está listo para dos sedes:

1. `AiAgentService::injectBranchContext()` (`app/Services/AiAgentService.php:862`) lee las sedes **activas** frescas de DB **en cada turno** y las inyecta al system prompt. Una sede nueva aparece en el turno siguiente, sin despliegue.
2. `get_delivery_fee` y `get_catalog` exigen `branch_id` obligatorio (`app/Services/AiAgent/Tools/GetDeliveryFeeTool.php:54`). Con dos sedes activas el modelo tiene que elegir una, y nada en el prompt le dice cómo.
3. El prompt vivo es **monosede**: «Eres el asistente de Calamar Azul, **sede Cable**» (`prompts/asistente-whatsapp/v4-catalogo-descriptivo-2026-10-16.md:20`). Dos sedes activas lo pondrían en contradicción directa con el bloque inyectado.

Verificado tras la carga: `injectBranchContext` sigue devolviendo sólo `Sede Cable`, así que el agente en piloto no cambió de comportamiento.

**Para activarla** hace falta, en este orden: (a) nueva versión del prompt que pregunte la sede cuando la respuesta dependa de ella —o la derive del barrio—, (b) decidir si Centro tendrá su propia línea de WhatsApp (`whatsapp_line_id`, hoy null) o comparte la de Cable, (c) `is_active = true`. Las tarifas ya resuelven bien sin tocar nada más.

## Tarifas por banda

| Tarifa | Barrios | Detalle |
|---|---|---|
| $5.000 | 13 | Alcázares, Bella Montaña, Campo Hermoso, Campoamor, Centro, Chipre, Fundadores, La Francia, Las Américas, Los Agustinos, Sacatín, San Joaquín, Villa Pilar |
| $6.000 | 9 | Asís, Avanzada, Colón, Estrada, Galán, Jazmín, Las Delicias, San Ignacio, San José |
| $6.500 | 6 | Centenario, El Bosque, El Carmen, Estambul, Nogales, San Antonio |
| $7.500 | 44 | Alférez Real, Arboleda, Arrayanes, Bajo Andes, Bajo Prado, Barrio Colombia, Belén, Camelia, Cervantes, El Campín, El Palmar, El Sol, El Trébol, Eucaliptos, González, Guamal, Guayacanes, La Argentina, La Asunción, La Estrella, La Isabela, La Leonora, La Rambla, Las Águilas, Laureles, Lleras, Los Cedros, Marmato, Milán, Nevado, Palermo, Palo Grande, Panamericana, Paraíso, Persia, Prado, Rosales, San Jorge, Sancancio, Santa Elena, Uribe Vélez, Versalles, Villa Carmenza, Villa del Río |
| $8.000 | 11 | Altos de Granada, Comuneros, El Porvenir, La Carola, La Carolita, Portón del Guamo, Samaria, Sinaí, Solferino, Villa Café, Villahermosa |
| $8.500 | 29 | Alta Suiza, Aranjuez, Baja Suiza, Betania, Bosques de Niza, Camilo Torres, Castilla, Colseguros, El Aguacate, El Encuentro, Fátima, Kennedy, La Cumbre, La Paz, La Sultana, La Toscana, Las Colinas, Licorera, Malabar, Minitas, Pío 12, Residencias Manizales, San Luis, Villa Luz, Viveros, Vivienda Popular, Yarumales 1, Yarumales 2, Yarumos |
| $9.000 | 10 | Altos de Capri, Bosques del Norte, El Caribe, Fanny González, Palo Negro, Peralonso, Puerta del Sol, San Cayetano, San Sebastián, Villa Julia |
| $10.000 | 1 | Cerro de Oro Ecoturístico |
| $12.000 | 9 | Alhambra, Cerros de la Alhambra, Chachafruto, La Enea, La Linda, Lusitania, Maltería, San Marcel, Zona Industrial |
| $15.000 | 1 | Turín Villa María |

## Correspondencia con las comunas, y contraste con Cable

Las dos sedes cubren exactamente los mismos barrios con precios distintos. El patrón es coherente con la geografía: Centro cobra menos por el centro y el occidente, y más por el norte y el oriente.

| Comuna (fuente) | Centro | Cable | Δ |
|---|---|---|---|
| 1 Atardeceres | $5.000 | $10.000 | −$5.000 |
| 2 San José | $6.000 | $8.000 | −$2.000 |
| 3 Cumanday | $5.000 | $7.500 | −$2.500 |
| 4 Estación | $7.500 | $6.000 | +$1.500 |
| 5 Ciudadela del Norte | $9.000 | $7.500 | +$1.500 |
| 6 Cerro de Oro | $8.500 | $8.500 | — |
| 7 Tesorito | $12.000 | $13.000 | −$1.000 |
| 8 Palogrande | $7.500 | $6.000 | +$1.500 |
| 9 Universitaria | $8.500 | $7.500 | +$1.000 |
| 10 La Fuente | $7.500 | $8.000 | −$500 |
| 11 La Macarena | $6.500 | $8.000 | −$1.500 |
| 12 Nuevo Horizonte | $8.000 | $7.500 | +$500 |
| Periferia: Cerro de Oro Ecoturístico | $10.000 | $10.000 | — |
| Periferia: La Linda | $12.000 | $13.000 | −$1.000 |
| Periferia: Turín Villamaría | $15.000 | $15.000 | — |

Nombres que la fuente traía pegados por el formato de WhatsApp y que se separaron al cargar (idéntico a Cable): `San Joaquín Campoamor Fundadores`, `Altos de Capri bosques del Norte`, `Yarumales 1 y 2 Licorera`, `Cerros de la alhambra  Lusitania`, `La Carola Villahermosa Comuneros`, `Portón del guamo Sinaí`.

## Pendientes

### 3 barrios con tarifa contradictoria (los mismos que en Cable)

La fuente les asigna dos precios porque quedan a caballo entre dos comunas. No se cargaron: el resolver es determinista y la DB impone `(branch_id, barrio)` único, así que el agente responde `ZONE_NOT_COVERED` y escala en vez de cotizar un precio inventado.

| Barrio | Precio A | Precio B |
|---|---|---|
| Arenillo | $5.000 (Comuna 1 Atardeceres) | $6.500 (Comuna 11 La Macarena) |
| La Castellana | $6.500 (Comuna 11 La Macarena) | $8.000 (Comuna 12 Nuevo Horizonte) |
| Santos | $8.500 (Comuna 9 Universitaria) | $7.500 (Comuna 10 La Fuente) |

Que el conflicto se repita en las dos sedes refuerza que es un problema de **límite de comuna**, no un error de digitación: conviene resolverlo una sola vez para ambas sedes.

### La Floresta, sin precio

La fuente de Centro cierra el grupo de periferia con `La Floresta` **sin valor de domicilio** (la fuente de Cable no la menciona). Queda sin cargar hasta que el negocio confirme la tarifa, y si aplica también para Cable.

## Comportamiento del resolver (release `d4e3cf55`)

`app/Services/Orders/DeliveryTariffResolver.php` resuelve en tres niveles, siempre de forma determinista:

1. **Barrio exacto** normalizado (minúsculas, sin tildes, sin puntuación, espacios colapsados).
2. **Alias exacto** registrado en `delivery_tariff_aliases`.
3. **Match asistido:** el nombre de una zona activa (o su alias) aparece como *frase contigua de tokens* dentro de la dirección en texto libre, y queda **una sola** candidata. Las coincidencias subsumidas por una más larga se descartan. Nunca resuelve por subcadena cruda: `san jose` no se cuela en `San Joaquín`.

Verificado en producción contra el release desplegado:

| Entrada del cliente | Resultado (sede Cable) |
|---|---|
| `Palermo` | Palermo · $6.000 |
| `Vivo en la calle 65 #23-40 barrio Palermo` | Palermo · $6.000 |
| `carrera 23 con 65, Palo Grande, apto 501` | Palo Grande · $6.000 |
| `estoy en san joaquin` | San Joaquín · $7.500 |
| `Arenillo`, `La Floresta`, `mi casa queda cerca` | `ZoneUnresolvedError` |

**Un no-match es `ZONE_UNRESOLVED`, cuya semántica es «escalar», nunca «sin cobertura».** `get_delivery_fee` lo traduce a `status: "unresolved"`, el orquestador crea el handoff de forma determinista en el camino productivo, y el agente debe decirle al cliente que el equipo le confirma el domicilio — jamás que no hay cobertura.

Por eso al agente se le pide pasar **el barrio o la dirección completa tal cual la dijo el cliente**: el match asistido necesita el texto original. Sigue sin haber aliases cargados, pero el match asistido ya cubre buena parte de lo que antes caía en escalamiento.
