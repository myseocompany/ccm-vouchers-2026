# Catálogo de SKUs v1 — Mercado Gastronómico Fusión (Compañía de Restaurantes Sushi S.A.S.)

Catálogo interno para el agente IA, construido 2026-10-28 desde las 6 cartas transcritas (`../cartas/*.md`) aplicando la regla de desduplicación de `../conflictos-cartas-2026-10-28.md`.
**Todos los precios incluyen el impuesto al consumo del 8%.** Propina sugerida 10%. Moneda: COP.

## Reglas de canal y desduplicación

- **Canal `domicilio`** (sushi y arroces para llevar) → usar **The Sushi House** (`SH-*`) y **Rice To Go** (`RG-*`). Nunca cotizar un pedido a domicilio de sushi con los precios de la carta de mesa Sushi Fusión.
- **Canal `mesa`** → **Sushi Fusión** (`SF-*`) es la carta amplia de salón.
- **Canal `ambos`** (mesa + domicilio, misma carta/precio) → **Inca Fusión** (`IF-*`), **Lemon Fish** (`LF-*`), **Krabbies** (`KB-*`).
- **Bloques compartidos** (bebidas, cervezas, michelados, postres base) → SKUs canónicos `CMP-*` con el precio de **Sushi Fusión**; las discrepancias por carta están marcadas ⚠ en §7 y son *dudas para el establecimiento*.
- **Homónimos mesa vs domicilio** (p. ej. Filadelfia, California, Ojo de Tigre, Ceviche de Pescado, Coctel Mixto) = **SKUs distintos** con precio distinto; el canal decide cuál se cotiza.

Esquema de SKU: `MARCA-CAT-##` (MARCA = SF/IF/LF/KB/SH/RG/CMP).

---

## 1. SUSHI FUSIÓN (`SF-*`) — canal: **mesa**

### Entradas
| SKU | Producto | Precio |
|---|---|---|
| SF-ENT-01 | Palmitos Tempura | $34.000 |
| SF-ENT-02 | Gyosas | $40.000 |
| SF-ENT-03 | Ika Panko | $40.000 |
| SF-ENT-04 | Tori Niku | $37.000 |
| SF-ENT-05 | Sakana Panko | $39.000 |
| SF-ENT-06 | Gyosas Kamaron | $42.000 |
| SF-ENT-07 | Kamaron Panko | $40.000 |
| SF-ENT-08 | Tataki Surai | $46.000 |
| SF-ENT-09 | Tuna Kahi | $54.000 |

### Sushi — principiantes
| SKU | Producto | Precio |
|---|---|---|
| SF-SUP-01 | Vulcano | $50.000 |
| SF-SUP-02 | Cielo Azúl | $48.000 |
| SF-SUP-03 | Playa Azúl | $48.000 |
| SF-SUP-04 | Kioto | $50.000 |
| SF-SUP-05 | Río | $46.000 |
| SF-SUP-06 | Nara | $48.000 |
| SF-SUP-07 | Lima Panko | $56.000 |
| SF-SUP-08 | Sake Siracha | $60.000 |
| SF-SUP-09 | Chizu | $62.000 |
| SF-SUP-10 | Kazan | $52.000 |
| SF-SUP-11 | Panko Maracuyá | $62.000 |

### Sushi — especiales
| SKU | Producto | Precio |
|---|---|---|
| SF-SUE-01 | Shiroi | $62.000 |
| SF-SUE-02 | Nikkei | $68.000 |

### Sushi — intermedio
| SKU | Producto | Precio |
|---|---|---|
| SF-SUI-01 | Marino | $59.000 |
| SF-SUI-02 | Sushi Fusión | $50.000 |
| SF-SUI-03 | Nevada | $52.000 |
| SF-SUI-04 | Mediterraneo | $48.000 |
| SF-SUI-05 | Neptuno | $60.000 |
| SF-SUI-06 | Ibérico | $54.000 |
| SF-SUI-07 | Arco Iris | $54.000 |
| SF-SUI-08 | Hakone | $52.000 |
| SF-SUI-09 | Tuna Gari | $62.000 |
| SF-SUI-10 | Zumi | $65.000 |
| SF-SUI-11 | Kurimi | $64.000 |
| SF-SUI-12 | Perú-Hito | $64.000 |
| SF-SUI-13 | Ro-Koto | $69.000 |
| SF-SUI-14 | Tuna Sake | $52.000 |
| SF-SUI-15 | Tokio | $58.000 |
| SF-SUI-16 | Himalaya | $54.000 |

### Sushi — avanzado
| SKU | Producto | Precio |
|---|---|---|
| SF-SUA-01 | Orenji | $58.000 |
| SF-SUA-02 | Ebi Parmesan | $65.000 |
| SF-SUA-03 | Monte Fuji | $58.000 |
| SF-SUA-04 | Nippon | $62.000 |
| SF-SUA-05 | Kinkaku | $59.000 |
| SF-SUA-06 | Lima Fusión | $62.000 |
| SF-SUA-07 | Nikko | $65.000 |
| SF-SUA-08 | Naito | $50.000 |
| SF-SUA-09 | Okinawa | $50.000 |
| SF-SUA-10 | Tropical | $42.000 |
| SF-SUA-11 | Tuna Acevichado | $68.000 |
| SF-SUA-12 | Nigai | $68.000 |
| SF-SUA-13 | Kuromai | $55.000 |
| SF-SUA-14 | Nori Kaiyo | $48.000 |
| SF-SUA-15 | Océano | $45.000 |

### Sushi — Roll Haru / otros
| SKU | Producto | Precio |
|---|---|---|
| SF-SUH-01 | Ojo de Tigre | $46.000 |
| SF-SUH-02 | Filadelfia | $38.000 |
| SF-SUH-03 | California | $38.000 |
| SF-SUH-04 | Haru | $65.000 |
| SF-SUH-05 | Sake Chalaca | $68.000 |
| SF-SUH-06 | Kani Japo | $52.000 |

### Sushi — vegetariano
| SKU | Producto | Precio |
|---|---|---|
| SF-SUV-01 | Doraitomato | $46.000 |
| SF-SUV-02 | Yasai | $42.000 |
| SF-SUV-03 | Mozzarela Gari | $48.000 |
| SF-SUV-04 | Zukkini | $48.000 |
| SF-SUV-05 | Nara Avocado | $48.000 |
| SF-SUV-06 | Abokado | $40.000 |
| SF-SUV-07 | Kenko | $42.000 |
| SF-SUV-08 | Zukkini Tempura | $48.000 |
| SF-SUV-09 | Gari Tropical | $48.000 |

### Acevichados Gold
| SKU | Producto | Precio |
|---|---|---|
| SF-ACG-01 | Coctel Mixto | $62.000 |
| SF-ACG-02 | Coctel de Camarón | $62.000 |
| SF-ACG-03 | Ceviche de Pescado | $60.000 |
| SF-ACG-04 | Ceviche de Camarón | $62.000 |
| SF-ACG-05 | Ceviche de la Costa | $62.000 |

### Acevichados Peruanos Gold
| SKU | Producto | Precio |
|---|---|---|
| SF-APG-01 | Tradicional Peruano | $60.000 |
| SF-APG-02 | Parrilla Pesto | $64.000 |
| SF-APG-03 | Andino | $68.000 |
| SF-APG-04 | Pulpo a la Parmesana | $64.000 |
| SF-APG-05 | Rocoto Japonés | $65.000 |
| SF-APG-06 | Rocoto | $65.000 |
| SF-APG-07 | Primavera | $68.000 |

### Especiales Gold
| SKU | Producto | Precio |
|---|---|---|
| SF-ESG-01 | Tupac Amarú | $60.000 |
| SF-ESG-02 | Mozzarella Crunch *(best-seller)* | $60.000 |
| SF-ESG-03 | Causa Salmón | $65.000 |
| SF-ESG-04 | Causa de Camarón | $65.000 |
| SF-ESG-05 | Causa de Atún | $66.000 |
| SF-ESG-06 | Shifudo | $68.000 |
| SF-ESG-07 | Kamaron Maracuyá | $62.000 |
| SF-ESG-08 | Muru Kai | $68.000 |
| SF-ESG-09 | Tornado | $65.000 |
| SF-ESG-10 | Tornado Serrano | $65.000 |
| SF-ESG-11 | Sake Tempura | $62.000 |
| SF-ESG-12 | Tataki | $58.000 |
| SF-ESG-13 | Sake Kunsei | $60.000 |

### Combos Fusión (30 bocados salvo indicación)
| SKU | Producto | Precio |
|---|---|---|
| SF-CMB-01 | Combo Nikkei (arma tu combo) | $185.000 |
| SF-CMB-02 | Combo Mozarella | $165.000 |
| SF-CMB-03 | Combo Nikko | $165.000 |
| SF-CMB-04 | Combo Primavera | $165.000 |
| SF-CMB-05 | Combo Nippon | $165.000 |
| SF-CMB-06 | Combo Lima Panko | $165.000 |
| SF-CMB-07 | Combo Acevichado | $165.000 |
| SF-CMB-08 | Combo 1 | $165.000 |
| SF-CMB-09 | Combo 2 | $165.000 |

> ⚠ Estos **Combos Fusión** (mesa) NO son los combos por bocados de The Sushi House (ver `SH-CMB-*`). Son productos distintos; no confundir.

### Sashimi · Niguiri (sashimi + 2 niguiri)
| SKU | Producto | Precio |
|---|---|---|
| SF-SAS-01 | Maguro (Atún) — 60 g + 2 niguiri | $33.000 |
| SF-SAS-02 | Sake (Salmón) — 60 g + 2 niguiri | $33.000 |
| SF-SAS-03 | Kani Kama (Palmitos) — 4 und + 2 niguiri | $28.000 |
| SF-SAS-04 | Izumi Dai (Tilapia) — 80 g + 2 niguiri | $28.000 |

### Teppan (incluye arroz/vegetales al wok; pasta +$3.000)
| SKU | Producto | Precio |
|---|---|---|
| SF-TEP-01 | Teppan Mixto | $62.000 |
| SF-TEP-02 | Teppan Light | $60.000 |
| SF-TEP-03 | Teppan Tory | $55.000 |
| SF-TEP-04 | Teppan Orenji | $60.000 |
| SF-TEP-05 | Teppan Teriyaki | $62.000 |
| SF-TEP-06 | Teppan Butaniku | $60.000 |
| SF-TEP-07 | Teppan Kaniku | $63.000 |
| SF-TEP-08 | Teppan Vietnamita | $90.000 |
| SF-TEP-09 | Teppan Thai | $90.000 |
| SF-TEP-10 | Teppan Salmón | $82.000 |
| SF-TEP-11 | Teppan Shifudo | $90.000 |
| SF-TEP-12 | Teppan Especial | $85.000 |
| SF-TEP-13 | Teppan Tuna | $90.000 |
| SF-TEP-14 | Teppan Kamaron | $75.000 |
| SF-TEP-15 | Teppan Akame | $72.000 |

### Wok (Tailandia) (incluye arroz/vegetales; pasta +$3.000)
| SKU | Producto | Precio |
|---|---|---|
| SF-WOK-01 | Wok 1 | $46.000 |
| SF-WOK-02 | Wok 2 | $54.000 |
| SF-WOK-03 | Wok Mixto | $50.000 |
| SF-WOK-04 | Wok Butaniku | $50.000 |
| SF-WOK-05 | Wok Niku | $54.000 |
| SF-WOK-06 | Wok Light | $54.000 |
| SF-WOK-07 | Wok Kamaron | $59.000 |
| SF-WOK-08 | Wok Explosión | $62.000 |
| SF-WOK-09 | Wok Especial | $62.000 |
| SF-WOK-10 | Wok Trilogía | $69.000 |
| SF-WOK-11 | Wok Sake | $69.000 |
| SF-WOK-12 | Wok Tuna | $70.000 |
| SF-WOK-13 | Wok Kaiyo | $64.000 |
| SF-WOK-14 | Wok Kongo | $58.000 |

### Especiales al wok
| SKU | Producto | Precio |
|---|---|---|
| SF-WOE-01 | Vietktron | $65.000 |
| SF-WOE-02 | Kao Phat Thai | $65.000 |
| SF-WOE-03 | Green Thai | $65.000 |
| SF-WOE-04 | Wok Umi | $75.000 |
| SF-WOE-05 | Wok Bejitarian | $48.000 |

### Platos fuertes chinos (arroz incl.; pasta +$3.000)
| SKU | Producto | Precio |
|---|---|---|
| SF-CHI-01 | Fusión China | $60.000 |
| SF-CHI-02 | Camarón Fusión | $60.000 |
| SF-CHI-03 | Pollo Fusión | $60.000 |
| SF-3MU-01 | Fusión de 3 Mundos (para compartir) | $115.000 |

### Wok to Sushi (combo personal, precio único)
| SKU | Producto | Precio |
|---|---|---|
| SF-W2S-01 | Wok to Sushi (elige wok + sushi 5 bocados) | $85.000 |

### Sopas
| SKU | Producto | Precio |
|---|---|---|
| SF-SOP-01 | Tom Ka | $54.000 |
| SF-SOP-02 | Supu Mixta | $48.000 |
| SF-SOP-03 | Supu Fusión | $55.000 |
| SF-SOP-04 | Supu Kamaron | $58.000 |

### Menú infantil (incluye jugo/Fuze Tea)
| SKU | Producto | Precio |
|---|---|---|
| SF-INF-01 | Nuggets Pollo | $38.000 |
| SF-INF-02 | Lomito Teriyaki | $38.000 |
| SF-INF-03 | Pollito Teriyaki | $38.000 |
| SF-INF-04 | Yaki Tori | $38.000 |
| SF-INF-05 | Cushi Teriyaki | $38.000 |

### Adicionales (proteínas/porciones Sushi Fusión) y vinos
| SKU | Producto | Precio |
|---|---|---|
| SF-ADI-01 | Camarón 12 und | $32.000 |
| SF-ADI-02 | Salmón 200 g | $35.000 |
| SF-ADI-03 | Calamar 12 und | $32.000 |
| SF-ADI-04 | Langostino 3 und | $36.000 |
| SF-ADI-05 | Pescado Blanco 150 g | $28.000 |
| SF-ADI-06 | Solomito 150 g | $28.000 |
| SF-ADI-07 | Pollo 160 g | $25.000 |
| SF-ADI-08 | Pesca del Día 200 g | $30.000 |
| SF-ADI-09 | Wakame 100 g | $30.000 |
| SF-ADI-10 | Cerdo 150 g | $28.000 |
| SF-ADI-11 | Papa Frita 150 g | $15.000 |
| SF-ADI-12 | Yuca Frita 6 und | $15.000 |
| SF-VIN-01 | Vino de la Casa — Piccolo | $45.000 |
| SF-VIN-02 | Vino de la Casa — Botella | $105.000 |

---

## 2. INCA FUSIÓN (`IF-*`) — canal: **ambos**

### Tornados / Tiraditos / Tartar
| SKU | Producto | Precio |
|---|---|---|
| IF-TOR-01 | Tornado Serrano | $46.000 |
| IF-TOR-02 | Tornado de Salmón | $46.000 |
| IF-TIR-01 | Tiradito de Salmón | $42.000 |
| IF-TIR-02 | Tiradito a la Chalaca | $36.000 |
| IF-TIR-03 | Tiradito Tropical | $44.000 |
| IF-TIR-04 | Tiradito Mixto a la Chalaca | $42.000 |
| IF-TAR-01 | Tartar Mixto | $46.000 |
| IF-TAR-02 | Tartar de Atún | $47.000 |
| IF-TAR-03 | Tartar de Salmón Fresco | $45.000 |
| IF-TAR-04 | Tartar de Salmón en Mostaza | $48.000 |

### Ceviches
| SKU | Producto | Precio |
|---|---|---|
| IF-CEV-01 | Ceviche Primavera | $59.000 |
| IF-CEV-02 | Ceviche Andino | $59.000 |
| IF-CEV-03 | Ceviche Tradicional Peruano | $44.000 |
| IF-CEV-04 | Ceviche Pulpo a la Parmesana | $50.000 |
| IF-CEV-05 | Ceviche Tropical | $54.000 |
| IF-CEV-06 | Ceviche a la Parrilla | $52.000 |
| IF-CEV-07 | Ceviche Rocoto (picante) | $58.000 |
| IF-CEV-08 | Ceviche Rocoto Japonés (picante) | $58.000 |
| IF-CEV-09 | Ceviche Fusión Trilogía | $70.000 |

### Causas Limeñas (también en cucharitas)
| SKU | Producto | Precio |
|---|---|---|
| IF-CAU-01 | Causa Salmón | $49.000 |
| IF-CAU-02 | Causa Camarón | $48.000 |
| IF-CAU-03 | Causa de Atún | $52.000 |
| IF-CAU-04 | Causa de Pollo | $42.000 |
| IF-CAU-05 | Cucharitas Dinamita (6) | $46.000 |

### Ají de Gallina / Sopas y Cazuelas
| SKU | Producto | Precio |
|---|---|---|
| IF-AJI-01 | Ají de Gallina (Pollo) | $62.000 |
| IF-AJI-02 | Ají de Gallina (Pollo y camarones) | $68.000 |
| IF-SOP-01 | Aguadito de Mariscos | $55.000 |
| IF-SOP-02 | Cazuela de Mariscos | $80.000 |
| IF-SOP-03 | Parihuela de Mariscos (picante) | $55.000 |

### Arroces con Queso (pasta +$3.000)
| SKU | Producto | Precio |
|---|---|---|
| IF-ARQ-01 | Arroz Tradicional Peruano (amarillo) | $85.000 |
| IF-ARQ-02 | Arroz Tradicional Norteño al Cilantro | $85.000 |
| IF-ARQ-03 | Arroz Roquefort (blanco) | $80.000 |
| IF-ARQ-04 | Arroz Tinta de Calamar | $85.000 |

### Chaufas (pasta +$3.000)
| SKU | Producto | Precio |
|---|---|---|
| IF-CHA-01 | Chaufa de Pollo | $62.000 |
| IF-CHA-02 | Chaufa Mar y Tierra | $88.000 |
| IF-CHA-03 | Chaufa Trilogía | $70.000 |
| IF-CHA-04 | Chaufa de Mariscos | $82.000 |
| IF-CHA-05 | Chaufa de Solomito | $65.000 |

### Saltados
| SKU | Producto | Precio |
|---|---|---|
| IF-SAL-01 | Saltado de Lomo | $72.000 |
| IF-SAL-02 | Saltado de Pollo | $68.000 |
| IF-SAL-03 | Saltado Mar y Tierra | $78.000 |
| IF-SAL-04 | Saltado de Mariscos | $76.000 |

### Pescados / Salmón
| SKU | Producto | Precio |
|---|---|---|
| IF-PES-01 | Pescado Tradicional Peruano | $75.000 |
| IF-PES-02 | Pescado Tupac Amarú | $70.000 |
| IF-PES-03 | Pescado a lo Macho (picante) | $79.000 |
| IF-PES-04 | Pescado al Cilantro | $75.000 |
| IF-PES-05 | Pescado a la Chorillana | $70.000 |
| IF-PES-06 | Salmón Teriyaki | $80.000 |
| IF-PES-07 | Salmón al Coco | $82.000 |

### Carnes
| SKU | Producto | Precio |
|---|---|---|
| IF-CAR-01 | Solomo Fusión | $78.000 |
| IF-CAR-02 | Solomo Cuatro Quesos | $76.000 |
| IF-CAR-03 | Solomo Tradicional Peruano | $76.000 |
| IF-CAR-04 | Solomo al Cilantro | $72.000 |
| IF-CAR-05 | Solomo Tupac Amarú | $75.000 |

---

## 3. LEMON FISH (`LF-*`) — canal: **ambos**

> **Ceviches de pescado**: el precio es **base**; el final suma el pescado elegido → Salmón +$10.000 · Atún +$10.000 · Trucha +$8.000 · Tilapia +$7.000 · Pescado Blanco +$0.

### Ceviches de Camarón
| SKU | Producto | Precio |
|---|---|---|
| LF-CAM-01 | Camarones en Mostaza (CO) | $46.000 |
| LF-CAM-02 | Camarones en Salsa Rosada (CO) | $48.000 |
| LF-CAM-03 | Camarones en Salsa de Tomate (CO) | $46.000 |
| LF-CAM-04 | Camarones en Suero Costeño (CO) | $48.000 |
| LF-CAM-05 | Camarones en Mayonesa Japonesa (JP) | $52.000 |
| LF-CAM-06 | Camarones Agridulces (JP) | $55.000 |
| LF-CAM-07 | Camarones Primavera (PE) | $55.000 |
| LF-CAM-08 | Camarones Rocoto (PE) | $54.000 |
| LF-CAM-09 | Camarones a la Parmesana (PE) | $55.000 |
| LF-CAM-10 | Camarones en Ají Amarillo (PE) | $55.000 |
| LF-CAM-11 | Camarones Parrilla Pesto (PE) | $52.000 |
| LF-CAM-12 | Camarones Tradicional (PE) | $48.000 |

### Ceviches de Pescado (precio base + pescado)
| SKU | Producto | Precio base |
|---|---|---|
| LF-PES-01 | Pescado en Mostaza (CO) | $38.000 |
| LF-PES-02 | Pescado en Mayonesa Japonesa (JP) | $44.000 |
| LF-PES-03 | Pescado Agridulce (JP) | $47.000 |
| LF-PES-04 | Pescado Tradicional (PE) | $40.000 |
| LF-PES-05 | Pescado Primavera (PE) | $47.000 |
| LF-PES-06 | Pescado Rocoto (PE) | $46.000 |
| LF-PES-07 | Pescado a la Parmesana (PE) | $47.000 |
| LF-PES-08 | Pescado en Ají Amarillo (PE) | $47.000 |
| LF-PES-09 | Pescado Parrilla Pesto (PE) | $44.000 |

### Ceviches de Mariscos
| SKU | Producto | Precio |
|---|---|---|
| LF-MAR-01 | Mariscos en Mostaza (CO) | $52.000 |
| LF-MAR-02 | Mariscos en Salsa Rosada (CO) | $54.000 |
| LF-MAR-03 | Mariscos en Salsa de Tomate (CO) | $52.000 |
| LF-MAR-04 | Mariscos en Suero Costeño (CO) | $56.000 |
| LF-MAR-05 | Mariscos en Mayonesa Japonesa (JP) | $58.000 |
| LF-MAR-06 | Mariscos Agridulces (JP) | $59.000 |
| LF-MAR-07 | Mariscos Primavera (PE) | $59.000 |
| LF-MAR-08 | Mariscos Rocoto (PE) | $58.000 |
| LF-MAR-09 | Mariscos a la Parmesana (PE) | $59.000 |
| LF-MAR-10 | Mariscos en Ají Amarillo (PE) | $59.000 |
| LF-MAR-11 | Mariscos Parrilla Pesto (PE) | $58.000 |
| LF-MAR-12 | Mariscos Tradicional (PE) | $55.000 |

### Ceviches Res · Cerdo · Pollo
| SKU | Producto | Precio |
|---|---|---|
| LF-RCP-01 | Ceviche de Chicharrón | $40.000 |
| LF-RCP-02 | Ceviche de Solomito en Pimienta | $54.000 |
| LF-RCP-03 | Ceviche de Pernil de Cerdo | $42.000 |
| LF-RCP-04 | Ceviche de Chorizo al Pesto | $35.000 |
| LF-RCP-05 | Ceviche de Ropa Vieja Agridulce | $40.000 |
| LF-RCP-06 | Ceviche de Pollo Cremoso | $40.000 |

### Cazuelas / Arroces
| SKU | Producto | Precio |
|---|---|---|
| LF-CAZ-01 | Cazuela de Mariscos | $80.000 |
| LF-CAZ-02 | Cazuela de Camarones | $80.000 |
| LF-CAZ-03 | Cazuela de Tilapia | $65.000 |
| LF-CAZ-04 | Cazuela de Salmón | $78.000 |
| LF-CAZ-05 | Cazuela de Trucha | $70.000 |
| LF-CAZ-06 | Cazuela de Atún | $80.000 |
| LF-CAZ-07 | Cazuela Mixta de Pescado | $80.000 |
| LF-ARR-01 | Arroz con Mariscos | $76.000 |
| LF-ARR-02 | Arroz con Camarones | $72.000 |
| LF-ARR-03 | Arroz Mixto de Pescado | $70.000 |

### Acompañantes Lemon Fish
| SKU | Producto | Precio |
|---|---|---|
| LF-ACO-01 | Arroz con Coco 200 g | $18.000 |
| LF-ACO-02 | Chips de Plátano 150 g | $15.000 |
| LF-ACO-03 | Patacones 4 und | $18.000 |
| LF-ACO-04 | Papas a la Francesa 150 g | $15.000 |
| LF-ACO-05 | Yucas Fritas 6 und | $15.000 |
| LF-ACO-06 | Aros de Cebolla 10 und | $18.000 |
| LF-ACO-07 | Anillos de Calamar Apanados 6 und | $40.000 |

---

## 4. KRABBIES (`KB-*`) — canal: **ambos**

> **Burgersushi/Perrushi**: dos presentaciones (precio Burgersushi / Perrushi). Combo (cualquier plato principal) = **+$25.000** (plato + Hatsu + papa o yuca).

### Burgersushi / Perrushi
| SKU | Producto | Burgersushi | Perrushi |
|---|---|---|---|
| KB-BPS-01 | Sake Siracha | $58.000 | $53.000 |
| KB-BPS-02 | Krabb Gari (temporada) | $62.000 | $57.000 |
| KB-BPS-03 | Himalaya Gratin | $50.000 | $45.000 |
| KB-BPS-04 | Nippon | $60.000 | $57.000 |
| KB-BPS-05 | Tupac Amarú | $52.000 | $47.000 |
| KB-BPS-06 | Eby Parmesan | $60.000 | $54.000 |
| KB-BPS-07 | Tuna Gari | $59.000 | $54.000 |
| KB-BPS-08 | Sake Kunsei | $56.000 | $51.000 |
| KB-BPS-09 | Primavera | $58.000 | $53.000 |
| KB-BPS-10 | Mozzarella Crunch | $56.000 | $51.000 |
| KB-BPS-11 | Ceviche Japonés | $59.000 | $54.000 |

### Krabburgers
| SKU | Producto | Precio |
|---|---|---|
| KB-BUR-01 | Krabb Dijon Burger (temporada) | $46.000 |
| KB-BUR-02 | Krabb Cream Burger (temporada) | $46.000 |
| KB-BUR-03 | Kamaron Grill Burger | $42.000 |
| KB-BUR-04 | Salmón Grill Burger | $46.000 |
| KB-BUR-05 | Tuna Burger | $46.000 |
| KB-BUR-06 | Panko Fish Burger | $40.000 |
| KB-BUR-07 | Chicken Grill Burger | $36.000 |
| KB-BUR-08 | Panko Chicken Burger | $39.000 |
| KB-BUR-09 | Spicy Chicken Burger | $40.000 |
| KB-BUR-10 | Sirloin Teriyaki | $42.000 |
| KB-BUR-11 | Burger Meat | $35.000 |
| KB-BUR-12 | Veggie Burger | $32.000 |

### Krabbdogs (arroz de sushi al panko +$10.000)
| SKU | Producto | Precio |
|---|---|---|
| KB-DOG-01 | Eby Parmesan Dog | $39.000 |
| KB-DOG-02 | Eby Dog | $38.000 |
| KB-DOG-03 | Kamaron Grill Dog | $36.000 |
| KB-DOG-04 | Kamaron Panko | $36.000 |
| KB-DOG-05 | Panko Fish Dog | $36.000 |
| KB-DOG-06 | Salmón Grill Dog | $38.000 |
| KB-DOG-07 | Tataki Dog | $39.000 |
| KB-DOG-08 | Lomo Salteado Dog | $38.000 |
| KB-DOG-09 | Panko Chicken Dog | $36.000 |
| KB-DOG-10 | Veggie Dog | $32.000 |

### Krabtacones
| SKU | Producto | Precio |
|---|---|---|
| KB-TAC-01 | Ceviche Colombiano | $50.000 |
| KB-TAC-02 | Ceviche Japonés | $52.000 |
| KB-TAC-03 | Camarones a la Parmesana | $52.000 |
| KB-TAC-04 | Coctel Mixto | $54.000 |
| KB-TAC-05 | Ceviche de la Costa | $55.000 |
| KB-TAC-06 | Ceviche de Pescado | $42.000 |
| KB-TAC-07 | Ceviche de Chicharrón | $40.000 |
| KB-TAC-08 | Criollo | $40.000 |
| KB-TAC-09 | Pollo Tupac | $50.000 |
| KB-TAC-10 | Lomo al Cilantro | $42.000 |
| KB-TAC-11 | Veggie | $40.000 |
| KB-ACO-01 | Adición de salsas | $7.000 |

---

## 5. THE SUSHI HOUSE (`SH-*`) — canal: **domicilio / para llevar**

### Entradas
| SKU | Producto | Precio |
|---|---|---|
| SH-ENT-01 | Calamares al Panko | $40.000 |
| SH-ENT-02 | Ceviche de Pescado | $38.000 |
| SH-ENT-03 | Ceviche de Camarón | $46.000 |
| SH-ENT-04 | Ceviche de la Costa | $44.000 |
| SH-ENT-05 | Coctel de Camarón | $46.000 |
| SH-ENT-06 | Coctel Mixto | $49.000 |
| SH-ENT-07 | Sopa de la House | $56.000 |

### Niguiris
| SKU | Producto | Precio |
|---|---|---|
| SH-NIG-01 | Atún | $30.000 |
| SH-NIG-02 | Salmón | $30.000 |
| SH-NIG-03 | Kanikama | $30.000 |

### Maki Rolls / Crudos
| SKU | Producto | Precio |
|---|---|---|
| SH-CRU-01 | Filadelfia | $36.000 |
| SH-CRU-02 | California | $35.000 |
| SH-CRU-03 | Tuna Maki | $42.000 |
| SH-CRU-04 | Mango Maki | $37.000 |
| SH-CRU-05 | Salmón Maki | $37.000 |
| SH-CRU-06 | Spicy Tuna | $42.000 |
| SH-CRU-07 | Kani Maki | $38.000 |

### Combinados
| SKU | Producto | Precio |
|---|---|---|
| SH-COM-01 | Rainbow Maki | $47.000 |
| SH-COM-02 | House on Fire | $44.000 |
| SH-COM-03 | Salmón Ebi Tempura | $42.000 |

### Cocidos
| SKU | Producto | Precio |
|---|---|---|
| SH-COC-01 | Vegetal Maki | $35.000 |
| SH-COC-02 | Vegetal Plátano | $35.000 |
| SH-COC-03 | Ajillo Maki | $39.000 |
| SH-COC-04 | Crispy Salmón | $39.000 |
| SH-COC-05 | Calamar-Chipotle | $39.000 |
| SH-COC-06 | Platanito Maki | $38.000 |
| SH-COC-07 | Salmón Skin | $36.000 |
| SH-COC-08 | Ojo de Tigre | $42.000 |
| SH-COC-09 | Langostino Tempura | $38.000 |
| SH-COC-10 | Sushicharrón | $37.000 |
| SH-COC-11 | Salmón Teriyaki | $39.000 |

### Combos promocionales por bocados
| SKU | Producto | Precio |
|---|---|---|
| SH-CMB-01 | HOUSE — 30 bocados | $95.000 |
| SH-CMB-02 | ESPECIAL — 50 bocados | $145.000 |
| SH-CMB-03 | SUPERIOR — 70 bocados | $220.000 |
| SH-CMB-04 | PREMIUM — 100 bocados | $270.000 |
| SH-CMB-add | Agranda +10 bocados | +$20.000 |

---

## 6. RICE TO GO (`RG-*`) — canal: **domicilio / para llevar**

> 3 tamaños: **Familiar** (2000 g / ~5 pers.) · **Media caja** (1000 g / ~3 pers.) · **Personal** (350 g / ~1 pers.).

| SKU | Producto | Familiar | Media | Personal |
|---|---|---|---|---|
| RG-ARR-01 | Chicken Rice | $75.000 | $65.000 | $39.000 |
| RG-ARR-02 | Rice del Campo | $75.000 | $65.000 | $39.000 |
| RG-ARR-03 | Perú Chaufa | $92.000 | $82.000 | $55.000 |
| RG-ARR-04 | Perú al Cilantro | $92.000 | $82.000 | $55.000 |
| RG-ARR-05 | Tailandia Mixto | $84.000 | $74.000 | $47.000 |
| RG-ARR-06 | Tailandia Especial | $88.000 | $78.000 | $51.000 |
| RG-ARR-07 | Tailandia Mariscos | $95.000 | $85.000 | $58.000 |
| RG-ARR-08 | Oriente (China) | $92.000 | $82.000 | $55.000 |
| RG-ARR-09 | Asia | $80.000 | $70.000 | $47.000 |
| RG-ARR-10 | Marino | $95.000 | $85.000 | $58.000 |
| RG-ARR-11 | México | $82.000 | $72.000 | $49.000 |
| RG-ARR-12 | Cuba | $87.000 | $77.000 | $54.000 |
| RG-ARR-13 | Colombia | $82.000 | $72.000 | $54.000 |
| RG-ARR-14 | Rice de la Montaña | $79.000 | $69.000 | $44.000 |
| RG-ARR-15 | Rice de la Casa | $80.000 | $70.000 | $47.000 |

### Acompañantes Rice To Go
| SKU | Producto | Precio |
|---|---|---|
| RG-ACO-01 | Vegetales al Wok 200 g | $18.000 |
| RG-ACO-02 | Papas a la Francesa 150 g | $15.000 |
| RG-ACO-03 | Yuca Frita 6 und | $15.000 |
| RG-ACO-04 | Chips de Plátano 150 g | $15.000 |
| RG-ACO-05 | Aros de Cebolla Apanados 10 und | $18.000 |

### Adiciones Rice To Go
| SKU | Producto | Precio |
|---|---|---|
| RG-ADI-01 | Camarones 12 und | $32.000 |
| RG-ADI-02 | Calamar 12 und | $32.000 |
| RG-ADI-03 | Pescado Blanco 150 g | $28.000 |
| RG-ADI-04 | Lomo de Res 150 g | $28.000 |
| RG-ADI-05 | Cerdo 150 g | $28.000 |
| RG-ADI-06 | Pollo 160 g | $25.000 |
| RG-ADI-07 | Chicharrón 150 g | $26.000 |
| RG-ADI-08 | Chorizo 180 g | $25.000 |
| RG-ADI-09 | Champiñones 180 g | $24.000 |
| RG-ADI-10 | Madurito 200 g | $18.000 |
| RG-ADI-11 | Trozos de Papa Frita 150 g | $16.000 |
| RG-ADI-12 | Trozos de Yuca Frita 150 g | $16.000 |
| RG-ADI-13 | Tocineta 150 g | $20.000 |

---

## 7. COMPARTIDOS (`CMP-*`) — bebidas, cervezas, michelados, postres (canónico Sushi Fusión)

> Estos ítems se repiten en varias cartas. Precio **canónico = Sushi Fusión**. Las ⚠ son discrepancias reales entre cartas, a resolver con el establecimiento (§8).

### Bebidas
| SKU | Producto | Precio canónico | ⚠ Discrepancias |
|---|---|---|---|
| CMP-BEB-01 | Coca Cola (Normal/Zero) | $10.000 | — |
| CMP-BEB-02 | Agua Manantial (con/sin gas) | $12.000 | ⚠ Rice To Go la cobra **$10.000** |
| CMP-BEB-03 | Jugos del Valle (Citrus/Mandarina) | $10.000 | — |
| CMP-BEB-04 | Maracumbé (Maracuyá/Lulo) | $14.000 | — |
| CMP-BEB-05 | Té Hatsu | $14.000 | — |
| CMP-BEB-06 | Soda Hatsu | $12.000 | — |
| CMP-BEB-07 | Fuze Tea (Manzana/Limón/Durazno) | $10.000 | ⚠ Sushi House la cobra **$11.000** |
| CMP-BEB-08 | Ginger Ale Schweppes | $11.000 | — |
| CMP-BEB-09 | Soda Schweppes | $11.000 | — |

### Cervezas (idénticas en todas las cartas)
| SKU | Producto | Precio |
|---|---|---|
| CMP-CER-01 | 3 Cordilleras (Blanca/Mestiza/Mulata/Negra/Rosada) | $17.000 |
| CMP-CER-02 | Heineken | $17.000 |
| CMP-CER-03 | Sol | $17.000 |
| CMP-CER-04 | Miller Lite | $17.000 |
| CMP-CER-05 | Stella Artois | $18.000 |
| CMP-CER-06 | Michelado (agrega a tu bebida) | $4.000 |

### Michelados / Cócteles / Sodas saborizadas
| SKU | Producto | Precio | ⚠ |
|---|---|---|---|
| CMP-MIC-01 | Cóctel Michelado (Soda Hatsu + 3 Cordilleras) | $30.000 | — |
| CMP-MIC-02 | Móctel Michelado (Soda Hatsu + siropes) | $20.000 | — |
| CMP-MIC-03 | Limonada de Vino | $25.000 | — |
| CMP-MIC-04 | Vino Caliente | $25.000 | — |
| CMP-MIC-05 | Sodas Saborizadas Schweppes | $16.000 | ⚠ Lemon Fish las cobra **$14.000** |
| CMP-MIC-06 | Soda Michelada Tradicional | $14.000 | — |

### Postres (set compartido SF/Inca/Krabbies)
| SKU | Producto | Precio |
|---|---|---|
| CMP-POS-01 | Helado Frito | $20.000 |
| CMP-POS-02 | Duraznos Tempura | $20.000 |
| CMP-POS-03 | Turrón de Maracuyá | $25.000 |
| CMP-POS-04 | Turrón de Oreo | $25.000 |
| CMP-POS-05 | Turrón de Arequipe | $25.000 |
| CMP-POS-06 | Turrón Frutos del Bosque / Frutos Rojos | $25.000 |
| CMP-POS-07 | Won Tones Mora | $25.000 |
| CMP-POS-08 | Won Tones Lychee | $25.000 |
| CMP-POS-09 | Suspiro de Mora / Limeño de Mora | $26.000 |
| CMP-POS-10 | Suspiro Limeño | $25.000 |

### Bebidas calientes (solo Sushi Fusión)
| SKU | Producto | Precio |
|---|---|---|
| CMP-CAL-01 | Café Americano | $5.000 |
| CMP-CAL-02 | Café Espresso | $7.000 |
| CMP-CAL-03 | Milo Caliente | $8.000 |
| CMP-CAL-04 | Té Hatsu caliente | $16.000 |
| CMP-CAL-05 | Capuccino | $6.000 |
| CMP-CAL-06 | Infusión de Fruta deshidratada | $9.000 |
| CMP-CAL-07 | Maracumbé caliente | $16.000 |

---

## 8. Dudas para el establecimiento (resolver antes de producción)

1. **Discrepancias de precio en compartidos** (⚠ arriba): ¿se unifica al canónico Sushi Fusión, o el precio depende de la carta/canal? — Agua Manantial ($12.000 vs $10.000 en Rice To Go), Fuze Tea ($10.000 vs $11.000 en Sushi House), Sodas Saborizadas ($16.000 vs $14.000 en Lemon Fish).
2. **Rolls exclusivos de Sushi Fusión a domicilio**: la mayoría de rolls `SF-SU*` no existen en The Sushi House. ¿Se venden a domicilio? ¿A qué precio (mesa o recargo)?
3. **Homónimos por canal**: confirmar que para domicilio los rolls básicos se cobran con precio The Sushi House (Filadelfia $36.000, California $35.000, Ojo de Tigre $42.000) y no con el de mesa (Filadelfia $38.000, California $38.000, Ojo de Tigre $46.000).
4. **Combos**: distinguir siempre Combos Fusión de mesa (`SF-CMB-*`, $165.000–$185.000) de los combos por bocados de The Sushi House (`SH-CMB-*`, $95.000–$270.000). Falta la página de combos de la carta Sushi Fusión para confirmar si cruza con los de The Sushi House.
5. **Productos de temporada** (Krabb Gari, Krabb Dijon, Krabb Cream): marcar disponibilidad.
6. **Disponibilidad por franja/marca**: ¿todas las cartas están disponibles en todo el horario?

## Resumen

~360 SKUs de producto principal + ~40 compartidos (bebidas/cervezas/michelados/postres/acompañantes/adiciones). Fuente: 6 cartas 2026 en `../cartas/`. Pendiente de validación del establecimiento en los 6 puntos de §8.
