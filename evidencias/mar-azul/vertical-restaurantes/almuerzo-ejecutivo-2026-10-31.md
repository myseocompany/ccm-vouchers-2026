# Calamar Azul — almuerzo ejecutivo (reglas confirmadas)

Reglas de negocio del almuerzo ejecutivo, confirmadas por la gerente administrativa del establecimiento el **2026-10-31** (comunicación retransmitida por Nicolás). Esta página es la fuente canónica; el `system_prompt` del agente y el menú del día de AriCRM deben derivarse de aquí, no al contrario.

## Definición confirmada

| Regla | Valor |
|---|---|
| Opciones de pescado (a elegir una) | Filete apanado, bagre, mojarra, sierra o trucha |
| Acompañamientos | Sopa de pescado, arroz de coco, patacón y ensalada |
| Bebida incluida | **Agua de panela con limón** |
| Precio | $26.000 |
| Horario | Solo hasta las 3:00 p. m. |
| Disponibilidad | Sujeta a agotados (reporte del levantamiento 2026-10-16; sin integración de inventario) |
| Variación diaria | **Ninguna**: el establecimiento tiene el mismo menú todos los días; las cinco opciones son siempre las mismas |

Texto confirmado por la cliente: «Filete apanado, bagre, mojarra, sierra o trucha, acompañado de sopa de pescado, arroz de coco, patacón y ensalada — $26.000. (Con bebida agua de panela con limón), solo hasta las 3:00 p. m.»

## Menú fijo — sin variación diaria

Confirmado el 2026-10-31: **el establecimiento no cambia el menú a diario; tiene el mismo menú todos los días**. La carta es fija (el levantamiento registró que cambia normalmente una vez al año, por precios) y el almuerzo ejecutivo mantiene siempre las mismas cinco opciones. En consecuencia:

- El agente nunca responde con un «menú del día» variable ni dice que no sabe qué hay hoy: presenta la misma carta y el mismo ejecutivo todos los días.
- **La herramienta `get_daily_menu` no se debe usar en este tenant** (decisión de Nicolás, 2026-10-31): la definición del ejecutivo va embebida en el `system_prompt` (v6). En el despliegue de la v6, retirar `get_daily_menu` de `enabled_tools` del agente (hoy figura habilitada según la verificación de producción del 2026-10-30).

## Qué hace el agente IA

- Describe siempre esta composición: no existe un «almuerzo del día» variable (confirmado expresamente por el establecimiento el 2026-10-31; ya acordado en la sesión de coaching — transcripción `../../../reunion_03.md` en la raíz del repo, pendiente de archivo formal).
- Las opciones de pescado disponibles del día las confirma con caja antes de tomar el pedido (no hay inventario integrado).
- Después de las 3:00 p. m. no ofrece el ejecutivo; ofrece la carta regular.

## Puntos sin confirmación expresa (quedan abiertos)

1. **Arroz blanco en vez de arroz de coco**: reportado en la sesión de coaching como solicitud frecuente que atienden. Falta confirmar si el agente debe preguntar proactivamente o solo cambiar a petición (recomendación de la sesión: solo a petición, «cállate y vende»).
2. **Cambios de acompañamiento** (p. ej., ensalada por más patacón) **y su posible costo**: sin confirmar.

## Diferencias con el prompt vivo (pendiente para la próxima versión)

- El prompt evolucionó después de la captura del v5: v6 publicada el 2026-10-30 y **v7 publicada el 2026-10-31** (v8 en preview, sin publicar); ver el registro de rondas en `../ia-conversacional/MENSAJES_PRUEBA_2026-10-30.md`. **Ninguna versión hasta la v8 incluye la bebida confirmada** (las confirmaciones del establecimiento llegaron después de las rondas 1–4): el ejecutivo sigue descrito sin agua de panela con limón.
- En la prueba de la sesión de coaching el agente respondió que incluía «sopa y limonada de la casa»: **incorrecto**; la bebida confirmada es **agua de panela con limón**.
- El menú del día de AriCRM está vacío y **la herramienta `get_daily_menu` no se debe usar en este tenant** (decisión del 2026-10-31): la definición debe ir embebida en el prompt, no en el menú del día. El bloque «Menú del día (herramienta obligatoria)» lo añade el código en la ruta productiva (`AiAgentService::appendDailyMenuToolContext`), así que retirarlo requiere cambio en `velo_wa`, además de quitar la tool de `enabled_tools` (cambio de producción).

## Registro

- **Fecha de confirmación**: 2026-10-31.
- **Fuente**: respuesta de la gerente administrativa al borrador `../../../clientes/mar-azul/borrador-confirmacion-almuerzo-ejecutivo-2026-10-31.md`, retransmitida por Nicolás.
- **Confirmación adicional (mismo día)**: el establecimiento no cambia el menú a diario; tiene el mismo menú todos los días (retransmitido por Nicolás; ya acordado en la sesión de coaching).
- **Guion de pruebas derivado**: `../../../clientes/mar-azul/PRUEBAS_CONVERSACIONALES.md`.
