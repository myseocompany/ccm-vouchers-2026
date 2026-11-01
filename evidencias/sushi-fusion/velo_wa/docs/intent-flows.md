# Sushi Fusion — Flujos intención → automatización → documento PDF

Runbook operativo del piloto de entrega de cartas en PDF por detección de intención.
SPEC: `specs/active/ai-intent-document-flows/`.

- **Tenant piloto**: `01a140b0-1dd9-7012-b03a-80cc84eb76f3` (Mercado Gastronómico Fusión, 6 marcas).
- **Comando**: `php artisan ai-intents:provision`.
- **Código**: `app/Console/Commands/ProvisionIntentDocumentFlows.php`, `app/Services/AiIntents/IntentFlowManifest.php`.

## Propósito

El canal de salida del agente IA es solo texto: el modelo no puede adjuntar archivos. Para cumplir
«cuando el cliente pida la carta, envía el/los PDF», la entrega se separa en dos piezas que ya
existen en producción:

1. El agente IA detecta la intención con la tool `record_detected_intent` (reporta solo el **slug**
   de la intención, nunca URLs ni archivos).
2. Una automatización V2 con trigger `ai_intent_detected` ejecuta la acción `send_sequence`, cuyos
   pasos `document` entregan los PDFs por el adaptador del canal.

El modelo nunca elige qué archivo enviar: solo se envían documentos declarados en el manifiesto y
fijados en la automatización (whitelist por construcción). El `system_prompt` del agente no cambia;
la lista de intenciones activas viaja por el contexto dinámico existente.

## Manifiesto JSON

Un manifiesto por tenant declara documentos, intenciones y automatizaciones.

### Schema

```jsonc
{
  "documents": [                        // lista (puede ser vacía), máx. 50
    {
      "key": "string",                  // ^[a-z0-9][a-z0-9-_]{0,63}$, único entre documents
      "source": "string",               // path absoluto con extensión (/…/carta.pdf) o URL https://
      "filename": "string"              // nombre que ve el cliente en WhatsApp (se le agrega la extensión)
    }
  ],
  "intents": [                          // al menos 1, máx. 50
    {
      "slug": "string",                 // ^[a-z0-9][a-z0-9-_]{0,63}$, único entre intents
      "name": "string",                 // requerido y no vacío
      "condition_text": "string"        // mini-prompt de detección, requerido y no vacío
    }
  ],
  "automations": [                      // al menos 1, máx. 50
    {
      "name": "string",                 // requerido, único en el manifiesto (clave de upsert)
      "intent_slugs": ["string"],       // al menos 1; cada slug debe existir en intents[]
      "steps": [                        // al menos 1, máx. 20
        { "type": "text", "body": "string", "delay_seconds": 0 },
        { "type": "document", "document": "<key de documents[]>", "caption": "string", "delay_seconds": 0 }
      ]
    }
  ]
}
```

### Reglas de validación

- **Keys y slugs**: `^[a-z0-9][a-z0-9-_]{0,63}$` y únicos dentro de su lista.
- **`documents[].source`**: path absoluto (`/…`) con extensión, o URL que empiece por `https://`.
  Cualquier otro valor se rechaza. Las URL externas se usan tal cual, sin publicar.
- **`automations[].intent_slugs`**: cada slug tiene que estar declarado en `intents[]`.
- **Pasos `text`**: `body` requerido y no vacío; no admiten `document`.
- **Pasos `document`**: `document` requerido y debe ser una `key` de `documents[]`; `caption` es
  opcional, pero si viene no puede estar vacío; usa `caption`, no `body`. El caption admite los
  mismos placeholders del renderer de secuencias (`{{name}}`, etc.).
- **`delay_seconds`**: entero entre 0 y 86400; por defecto 0. Es la pausa antes del paso.
- **Límites**: máx. 50 documentos, 50 intenciones, 50 automatizaciones y 20 pasos por automatización.
- **Errores**: la validación es total. Todas las violaciones se reportan juntas
  (`documents[2].key: …`, `automations[0].steps[1].document: …`), así que el manifiesto se corrige
  en una sola pasada. Con cualquier violación, el comando no escribe nada.

### Ejemplo (piloto Sushi Fusion)

Replica el playbook humano: por defecto se envían Sushi Fusión + The Sushi House; si el cliente pide
«todas» o una marca concreta, se envían las 4 restantes. Los paths son ilustrativos.

```json
{
  "documents": [
    { "key": "carta-sushi-fusion",   "source": "/abs/path/carta-sushi-fusion.pdf",   "filename": "Carta Sushi Fusión" },
    { "key": "carta-the-sushi-house", "source": "/abs/path/carta-the-sushi-house.pdf", "filename": "Carta The Sushi House" },
    { "key": "carta-inca-fusion",    "source": "/abs/path/carta-inca-fusion.pdf",    "filename": "Carta Inca Fusión" },
    { "key": "carta-krabbies",       "source": "/abs/path/carta-krabbies.pdf",       "filename": "Carta Krabbies" },
    { "key": "carta-lemon-fish",     "source": "/abs/path/carta-lemon-fish.pdf",     "filename": "Carta Lemon Fish" },
    { "key": "carta-rice-to-go",     "source": "/abs/path/carta-rice-to-go.pdf",     "filename": "Carta Rice To Go" }
  ],
  "intents": [
    {
      "slug": "pedir_carta",
      "name": "Pedir la carta",
      "condition_text": "El cliente pide la carta, el menú, promociones o pregunta qué productos venden."
    },
    {
      "slug": "pedir_todas_cartas",
      "name": "Pedir todas las cartas",
      "condition_text": "El cliente pide todas las cartas, las otras cartas, o una marca específica: Krabbies, Rice To Go, Inca Fusión o Lemon Fish."
    }
  ],
  "automations": [
    {
      "name": "Enviar carta default (Sushi Fusión + The Sushi House)",
      "intent_slugs": ["pedir_carta"],
      "steps": [
        { "type": "document", "document": "carta-sushi-fusion", "caption": "Carta Sushi Fusión", "delay_seconds": 0 },
        { "type": "document", "document": "carta-the-sushi-house", "caption": "Carta The Sushi House", "delay_seconds": 2 }
      ]
    },
    {
      "name": "Enviar cartas restantes",
      "intent_slugs": ["pedir_todas_cartas"],
      "steps": [
        { "type": "document", "document": "carta-inca-fusion", "caption": "Carta Inca Fusión", "delay_seconds": 0 },
        { "type": "document", "document": "carta-krabbies",    "caption": "Carta Krabbies",    "delay_seconds": 2 },
        { "type": "document", "document": "carta-lemon-fish",  "caption": "Carta Lemon Fish",  "delay_seconds": 2 },
        { "type": "document", "document": "carta-rice-to-go",  "caption": "Carta Rice To Go",  "delay_seconds": 2 }
      ]
    }
  ]
}
```

> **Confidencialidad**: el manifiesto **real** del piloto, con las rutas absolutas a los 6 PDFs del
> cliente, vive en el expediente privado del cliente (`ccm-vouchers-2026`). **No** se commitea a este
> repo, igual que los PDFs.

## Provisioning

```bash
# 1. Previsualizar el plan, sin escribir nada
php artisan ai-intents:provision 01a140b0-1dd9-7012-b03a-80cc84eb76f3 \
  --manifest=/ruta/absoluta/manifest.json --dry-run

# 2. Aplicar
php artisan ai-intents:provision 01a140b0-1dd9-7012-b03a-80cc84eb76f3 \
  --manifest=/ruta/absoluta/manifest.json
```

- El primer argumento acepta el **ID o el slug** del tenant.
- `--manifest` es obligatorio.
- `--dry-run` imprime el plan (documentos, intenciones y automatizaciones con su estado) y termina
  con `dry-run: no se aplicaron cambios.`

### Publicación de documentos

- Los documentos locales se suben al **disco de medios** (`filesystems.media_disk`: S3 en producción),
  en `<tenant_id>/intent-docs/<key>.<ext>`, igual que el resto de medios salientes. El paso de la
  automatización guarda esa ruta, no una URL pública: no hace falta `storage:link` ni un volumen
  compartido con el contenedor web.
- Al enviar, el proveedor lee el archivo de ese disco: Evolution lo manda en base64 y Cloud API lo
  sube a Meta antes de enviarlo. Por eso el flujo funciona en líneas Evolution y Cloud API.
- **Idempotencia por sha256**: si el archivo guardado tiene el mismo hash que el origen, no se vuelve
  a subir (`unchanged`). Si el contenido cambió (por ejemplo, una carta con precios nuevos), se
  sobrescribe el archivo y **la ruta se mantiene** (`updated`). Las automatizaciones existentes siguen
  apuntando a la misma ruta sin tocarlas.
- Los documentos con `source` `https://` se usan tal cual (`external-url`). Solo funcionan en líneas
  Evolution: Cloud API no envía medios por URL. Para Cloud API usa un archivo local.
- **Nombre visible en WhatsApp**: el cliente ve el `filename` del manifiesto más la extensión del
  archivo (`"Carta Sushi Fusión"` → `Carta Sushi Fusión.pdf`).

### Semántica idempotente y rollback

- Las intenciones se actualizan por `(tenant, slug)` y las automatizaciones por `(tenant, name)`.
  Re-ejecutar el comando no duplica nada. Una automatización cuyo trigger y pasos ya coinciden con el
  manifiesto queda `unchanged` y no se toca (sus acciones conservan el mismo id).
- Intenciones y automatizaciones se escriben en **una sola transacción**: si algo falla, no queda
  ninguna a medias. Los archivos se suben antes (no pueden ir en la transacción); como la ruta es
  determinista, una corrida fallida deja a lo sumo un archivo que la siguiente sobrescribe.
- Re-ejecutar **nunca reactiva** una intención ni una automatización que el operador haya desactivado.
  Se actualiza el contenido, pero `is_active` se deja como está (estados `kept-inactive` /
  `updated-kept-inactive`).
- Re-ejecutar **nunca borra** filas que no estén en el manifiesto. Quitar algo del manifiesto no lo
  elimina del tenant.
- **Rollback operativo**: desactivar la intención (**Ajustes → Intenciones del agente**) o la
  automatización (**Ajustes → Automatizaciones**) desde el panel. Es solo configuración: no hay
  migraciones. Los PDFs guardados quedan inertes sin una automatización que los use.
- **Conflicto de nombre**: si ya existe en el tenant una automatización con el mismo `name` pero con
  otro trigger (o una automatización V1), el comando la reporta como conflicto (`skipped-conflict`) y no la toca. Renombra la
  automatización del manifiesto o resuelve el conflicto a mano.

## Comportamiento en runtime

- Un mismo mensaje del cliente no dispara dos veces la misma automatización: hay dedup por
  intención + mensaje.
- Cada paso de la secuencia pasa por el safety de salida existente (`reserveOutboundSlot`) y respeta
  su `delay_seconds`.
- Si la intención está inactiva, el agente deja de recibirla y la automatización no corre.
- El texto del agente y los PDFs se envían de forma asíncrona: el orden de llegada entre la respuesta
  del robot y los documentos no está garantizado.

## Líneas WhatsApp Cloud API

Los documentos locales funcionan igual en líneas Cloud API: el proveedor sube el archivo del disco de
medios a Meta y envía el documento. Aplica la ventana de 24 horas de Meta: fuera de ella el envío se
rechaza (`Freeform window closed; template required`). Los documentos con `source` `https://` no
funcionan en Cloud API.

## Troubleshooting

- **¿El manifiesto es válido y qué va a cambiar?** Corre siempre `--dry-run` primero. Los errores de
  schema salen todos juntos, con su ruta (`intents[1].slug: …`).
- **¿El agente detectó la intención?** Revisa `ai_intent_detections` del tenant. Ahí quedan todas las
  detecciones, **incluidas las que no dispararon ninguna automatización** (intención sin regla activa,
  dedup, etc.).
- **¿Se envió el PDF?** Revisa `automation_runs` (historial de la automatización: intención que la
  disparó, resultado y motivo de omisión) y los `messages` outbound con `media_type='document'` de la
  conversación.
- **El cliente recibe el archivo con un nombre raro**: cambia el `filename` del documento en el
  manifiesto y re-provisiona. Solo se actualizan los pasos; el archivo guardado no cambia.
- **El PDF no llega en una línea Cloud API**: revisa que la ventana de 24 horas esté abierta y que el
  documento no venga de una URL `https://` (ver arriba).
