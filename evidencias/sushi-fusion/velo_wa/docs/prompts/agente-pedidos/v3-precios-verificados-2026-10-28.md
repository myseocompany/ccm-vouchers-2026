# Snapshot de prompt — Agente de pedidos (Sushi Fusion)

- Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)
- Agente: `01a18263-c04e-73c3-95a4-d3395049c907`
- Versión: `v3-precios-verificados-2026-10-28`
- Publicación: 2026-10-28, America/Bogota
- Responsable: Nicolás / MY SEO
- SHA-256 aplicado: `0ccc8e69d00e515c0e92ee5521b02324c68790e743b5de4560a131fd4ea1b8a3`
- Base: `v2-canal-y-cotizacion-segura-2026-10-28`

## Cambio

Permite comunicar precios de productos únicamente cuando modalidad e ítem estén desambiguados y el monto provenga de `get_catalog` o `quote_order` en la conversación actual. Los modifiers se cotizan exclusivamente con `quote_order`. Total final, domicilio, pago, disponibilidad y confirmación permanecen bajo cierre humano.
