# Snapshot de prompt — Agente de pedidos (Sushi Fusion)

- Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)
- Agente: Agente IA — Mercado Gastronómico Fusión (`01a18263-c04e-73c3-95a4-d3395049c907`)
- Versión: `v2-canal-y-cotizacion-segura-2026-10-28`
- Fecha de publicación: 2026-10-28 (America/Bogota)
- Responsable: Nicolás / MY SEO
- SHA-256 del contenido aplicado: `e7dcd5ce5d0d3673d77537f4a7802150918c3a2e3fc440d6224917dd496e00a7`
- Versión anterior: `v1-catalogo-escalamiento-2026-10-28`

## Cambios funcionales

Corrección después de Playground SU-01–SU-07:

- Prohibido comunicar precios, rangos, subtotales, domicilio o total durante v1; el cierre es humano.
- Modalidad obligatoria (mesa, domicilio o recoger) antes de recomendar productos cuyo canal modifica el catálogo.
- Prohibido inferir bocados, ingredientes, tamaños, disponibilidad o popularidad.
- «Ceviche de pescado» debe desambiguarse por marca, presentación y canal.
- Mozzarella Crunch no se presenta como best-seller hasta validación del establecimiento.
- Ambigüedad o ausencia de dato verificable = escala, no inferencia.

El contenido aplicado es v1 más este bloque de prioridad de seguridad, persistido en `ai_agents.system_prompt`.
