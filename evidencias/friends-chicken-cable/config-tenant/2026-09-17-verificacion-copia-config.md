# Evidencia — verificación de copia de configuración (SOP 09) — Friends Chicken

- Fecha de verificación: 2026-09-17 (tarde).
- Tenant verificado: `Friends Chicken` — slug `friends-chicken-uHMR` — ID `01a0a5a4-1cda-7099-bfe7-c993e6f1352b` — zona `America/Bogota`.
- Ejecutor de la copia: Nicolás (2026-09-17 13:35:11, hora del servidor).
- Método de verificación: lectura directa de base de datos de producción (servidor `waterfall`), **solo lectura**, vía `php artisan tinker`. Sin capturas de pantalla del aplicativo; el volcado JSON completo queda al final de este documento.
- Patrón origen: `restaurante-domicilios-v1` (SOP `workflows/09_copiar_tenant_patron.md`).

## Checklist SOP 09 — Verificación inmediata

| Criterio | Esperado | Encontrado | Estado |
|---|---|---|---|
| Etiquetas genéricas de domicilios | 10 | 10 (nombres genéricos, sin marcas) | ✅ |
| Automatizaciones desactivadas | 4, todas inactivas | 4, 0 activas ("Plantilla - …") | ✅ |
| Agente `Asistente de domicilios — plantilla` | 1, desactivado, no predeterminado, sin línea ni credencial | 1, `is_enabled=false`, `is_default=false`, `whatsapp_line_id=null`, `credential_id=null`, modelo `gpt-4o-mini` | ✅ |
| Sin contactos/conversaciones ajenos | 0 | **60 contactos y 60 conversaciones preexistentes (2026-09-15 y 2026-09-16)** | ⚠️ Ver nota 1 |
| Sin líneas/canales ajenos | 0 | **1 línea WhatsApp con estado `connected` desde 2026-09-15 15:23** | ⚠️ Ver nota 1 |
| Sin menús de otro restaurante | 0 categorías, 0 ítems | 0 y 0 | ✅ |
| Sin `Botanazo` ni otro cliente en nombres/prompt/configs | 0 apariciones | 0 en nombre de tenant, tags, automatizaciones (nombre y configs), agente (nombre y prompt) | ✅ |
| Quick replies / plantillas internas / credenciales | 0 | 0 / 0 / 0 | ✅ |

## Notas e incidentes

1. **El tenant no estaba limpio antes de la copia.** La línea WhatsApp se conectó el 2026-09-15 15:23 y generó 60 contactos con 60 conversaciones (23 el 15/09, 37 el 16/09) — **tráfico previo, ajeno a la copia** (la copia del 17/09 13:35:11 creó únicamente etiquetas, automatizaciones y agente; no creó contactos). Pendiente decisión de Nicolás: si estos datos y esa línea corresponden al arranque real del cliente (se conservan) o no (requiere decisión formal — `POLICIES.md` exige aprobación explícita para borrar datos).
2. **0 membresías de usuario**: ningún usuario pertenece al tenant (nadie puede iniciar sesión en él por login normal). La copia se ejecutó presumiblemente vía panel superadmin/impersonación. Falta invitar al menos un administrador del establecimiento por el flujo de invitación.
3. Fechas verificadas: tenant creado 2026-09-15 15:16:31; tags/automatizaciones/agente creados exactamente 2026-09-17 13:35:11 (consistente con una única ejecución de la copia).
4. Falta toda la parametrización obligatoria posterior del SOP (menú, horarios, zonas, prompt con datos reales, usuarios, revisión de automatizaciones). El agente y las automatizaciones quedaron desactivados, como exige el SOP ante cualquier verificación fallida.

## Volcado de verificación (JSON, solo lectura)

```json
{
    "tenant": {
        "id": "01a0a5a4-1cda-7099-bfe7-c993e6f1352b",
        "name": "Friends Chicken",
        "slug": "friends-chicken-uHMR",
        "timezone": "America/Bogota"
    },
    "tags_total": 10,
    "tags_nombres": [
        "Interesado en domicilio",
        "Pedido en curso",
        "Pago pendiente",
        "Pedido confirmado",
        "Pedido completado",
        "Cliente recurrente",
        "Fuera de cobertura",
        "Requiere atención humana",
        "Incidencia de pedido",
        "No continuar contacto"
    ],
    "automaciones_total": 4,
    "automaciones_activas": 0,
    "automaciones": {
        "01a0af94-106c-715a-a4ac-ec0890d312c2": "Plantilla - marcar nuevo interesado en domicilio",
        "01a0af94-106e-70c7-8d43-b725196c6957": "Plantilla - solicitar atención humana por palabra clave",
        "01a0af94-1070-72ad-9634-8bc7b91831ad": "Plantilla - informar fuera de horario",
        "01a0af94-1072-72a1-bdf9-58527c9ad94d": "Plantilla - seguimiento de pedido incompleto a 15 minutos"
    },
    "agentes": [
        {
            "id": "01a0af94-108c-7296-ab4a-534b85acac4e",
            "name": "Asistente de domicilios — plantilla",
            "llm_model": "gpt-4o-mini",
            "is_enabled": false,
            "is_default": false,
            "whatsapp_line_id": null,
            "credential_id": null
        }
    ],
    "contactos": 60,
    "conversaciones": 60,
    "lineas_whatsapp": 1,
    "categorias_menu": 0,
    "items_menu": 0,
    "quick_replies": 0,
    "message_templates": 0,
    "credentials": 0,
    "membresias": 0,
    "escaneo_botanazo": {
        "tenant_nombre": 0,
        "tags": 0,
        "automaciones_nombre": 0,
        "automaciones_config": 0,
        "agente_nombre": 0,
        "agente_prompt": 0
    },
    "fechas": {
        "tenant_creado": "2026-09-15 15:16:31",
        "linea_wa_creada": "2026-09-15 15:23:10",
        "linea_wa_status": "connected",
        "contactos_por_fecha": { "2026-09-15": 23, "2026-09-16": 37 },
        "conversaciones_por_fecha": { "2026-09-15": 23, "2026-09-16": 37 },
        "copiado_patron": "2026-09-17 13:35:11"
    }
}
```
