# Sede Cable y tarifas de domicilio — verificación de producción

**Fecha:** 2026-10-16. **Autorización:** instrucción explícita de Nicolás en esta conversación.

- Tenant: Grupo D Mar Azul SAS (`01a0fcc8-7908-71e0-ac67-c8aca5e05bf2`).
- Sede creada: `Sede Cable`, slug `cable`, activa, orden 1 (`01a14579-4916-7150-af8f-6f805542d8b1`).
- Tarifas activas creadas: mínima $5.000, intermedia $8.000 y lejana $12.000.
- Las tres se etiquetaron `barrio pendiente`: no existe todavía un mapa barrio→banda. No deben utilizarse para cotizar automáticamente hasta completar dicha asignación.

Verificación posterior mediante consulta de modelos `Branch` y `DeliveryTariff` en el release activo de Waterfall.
