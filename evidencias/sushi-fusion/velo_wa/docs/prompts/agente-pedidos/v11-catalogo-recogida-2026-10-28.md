# Snapshot de prompt — Agente de pedidos (Sushi Fusion)

- Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)
- Agente: `01a18263-c04e-73c3-95a4-d3395049c907`
- Versión: `v11-catalogo-recogida-2026-10-28`
- Publicación: 2026-10-28, America/Bogota
- Responsable: Nicolás / MY SEO
- SHA-256 aplicado: `bf9f3ac67fc9659f72ca0ef25e7d75ded1c5ba6777780a9716d1324ca27394c8`
- Base: `v10-intents-escalamiento-2026-10-28`

## Cambios

- Cuando un producto no aparece en el catálogo, exige revisión humana y evita cerrar ofreciendo sustitutos o categorías.
- Cuando el cliente solicita recogida, confirma take-away con la dirección exacta configurada y no pide datos de domicilio.

## Evidencia

SU-09 y SU-14 se repitieron en Playground con tools de solo lectura después de publicar esta versión. SU-09 no inventó producto ni precio y pidió revisión del equipo; SU-14 respondió `Cra 21 #72A-27, Alta Suiza, Manizales`.
