# Spec velo_wa — `sequence-media-mimetype` (P-009 del programa CCM Vouchers)

**Solicitado por**: harness `ccm-vouchers-2026` (tarea P-009 en `TASKS.md`) · 2026-09-30
**Prioridad**: alta — bloquea el piloto del vertical restaurantes (Arepas Rellenas Samu): la carta enviada por secuencia V2 se entrega pero **no se renderiza** en el teléfono del cliente.
**Diagnóstico y evidencia completa**: `clientes/arepas-rellenas-samu/PROGRESS.md` (entradas del 2026-09-30) en el repo `ccm-vouchers-2026`.

## 01 — User story

Como administrador de un tenant con automatizaciones V2,
quiero que los pasos multimedia de la acción `send_sequence` (imagen/video/audio/documento) se envíen con mimetype y filename correctos,
para que WhatsApp los renderice en el teléfono del cliente (hoy llegan con `mimetype:"false"` y no se ven).

## Contexto (verificado en producción, 2026-09-30)

- Regla V2 `enviar_carta` (tenant `arepas-rellenas-samu-UK5K`, línea Evolution `line_01a0ac98f82d`): 3 ejecuciones con run `success` y mensaje `status=delivered`, pero **la imagen nunca se renderizó** en el teléfono controlado.
- DB de Evolution (Postgres en hetzner, tabla `"Message"`): los TRES `imageMessage` quedaron con `"mimetype": "false"`:
  - **15:57:43 UTC** — medio por path local (rama `local_path`→base64; el archivo EXISTE en el media disk) — key `3EB09A97D7AAD2548FF793`.
  - **16:10:35 UTC** — medio por URL CDN — key `3EB0CF20FA9D9C87C6EA2F`.
  - **16:21:58 UTC** — medio por URL CDN con `content-type: image/png` correcto en el objeto — key `3EB034A3B939A8BDBBDF46`.
- **Control positivo 16:23:33 UTC**: mismo endpoint (`/message/sendMedia/{instance}`) con `mimetype: "image/png"` + `fileName: "carta.png"` → `imageMessage.mimetype = "image/png"` → imagen renderizada en el teléfono controlado.
- Conclusión: **Evolution v2.3.7 no infiere el mimetype desde la descarga** (ni del content-type del objeto ni de la extensión de la URL); usa los campos del request. Con los fallbacks actuales no puede resolver el tipo.
- Cadena del bug: `SendAutomationSequenceStep` crea el mensaje con `media_type` + `media_url` pero **sin** `media_mime_type` ni `media_filename` → `LegacyWhatsAppAdapter` → `WhatsAppClientService::sendMedia` rellena los fallbacks `'application/octet-stream'` + `'archivo'` (sin extensión) → Evolution produce `mimetype:"false"` → WhatsApp ACKa (`delivered`) pero el cliente no renderiza el medio.
- Los envíos de medios del composer funcionan porque el mensaje lleva mime/filename reales del upload.
- Nota: el estado `delivered` del mensaje en AriCRM **no** garantiza renderización del medio.

## 02 — Criterios de aceptación

- **AC1**: Given una regla V2 con acción `send_sequence` con un paso `image` cuyo `media_url` termina en extensión conocida (`.png`), when la secuencia dispara, then el mensaje outbound queda persistido con `media_mime_type = 'image/png'` y `media_filename` = basename de la URL, y Evolution produce un `imageMessage` con mimetype real.
- **AC2**: Igual para `video`, `audio` y `document` con extensiones comunes (mp4, mp3/ogg, pdf…); `document` lleva `media_filename` con extensión.
- **AC3**: Given un paso cuyo `media_url` no tiene extensión reconocible, then el envío no se rompe: cae al fallback actual (`application/octet-stream`) y lo registra en log para observabilidad.
- **AC4**: Sin regresión: envíos del composer (base64/local_path con mime/filename presentes), voice notes (`sendWhatsAppAudio`) y `send_template` (Cloud API) siguen funcionando — suite existente en verde.
- **AC5**: La inferencia **no** sobreescribe `media_mime_type`/`media_filename` cuando el mensaje ya los trae (p. ej. uploads del composer).

## 03 — Propuesta técnica

**Fix principal (A)** — `App\Jobs\SendAutomationSequenceStep`: al crear el `Message` para un paso multimedia, inferir desde `media_url`:

```php
// solo para type !== 'text'
$filename = basename((string) parse_url($mediaUrl, PHP_URL_PATH)); // p. ej. carta-san-jorge-2026-09-30.png
$ext      = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
$mime     = MimeTypes::getDefault()->getMimeTypes($ext)[0] ?? null;  // p. ej. image/png (Symfony\Component\Mime\MimeTypes)
```

persistiendo `media_filename` y `media_mime_type` en el mensaje (queda bien guardado para reintentos y auditoría).

**Red de seguridad (B)** — `WhatsAppClientService::sendMedia` (o `LegacyWhatsAppAdapter` justo antes de llamar al provider): si `mimeType`/`filename` llegan en null y el valor (URL o path) tiene extensión reconocible, inferirlos antes de los fallbacks `'application/octet-stream'`/`'archivo'`. Cubre a otros creadores de mensajes con `media_url` sin metadatos.

Se recomienda implementar **A + B**.

**Notas**:
- No cambiar el contrato del request hacia Evolution: el formato actual funciona cuando mime/filename son correctos (verificado con el control positivo).
- El `content-type` del objeto en el CDN no es parte del fix (Evolution no lo usa), pero mantenerlo correcto es buena práctica.
- La rama `local_path`→base64 también se beneficia: el mimetype se pasa igual en el request.

## 04 — Testing

- Feature test: regla V2 con paso imagen URL `.png` → ejecutar el job → assert del mensaje con `media_mime_type='image/png'` y `media_filename` correctos.
- Feature test del fallback: URL sin extensión → no rompe, cae a octet-stream, log presente.
- Unit test de inferencia por extensión (png/jpg/jpeg/webp/gif/mp4/mp3/ogg/pdf/docx…).
- Suite de regresión: envíos de medios existentes (composer base64, voice notes) en verde.

## Verificación post-deploy (producción)

1. Re-disparar la secuencia `enviar_carta`: mensaje de prueba pidiendo la carta desde teléfono controlado a la línea San Jorge (313 492 9669).
2. Verificar en la DB de Evolution (hetzner): `message->'imageMessage'->>'mimetype'` = `image/png`.
3. Confirmar en el teléfono controlado que la carta se ve como imagen.
4. Registrar la evidencia en `clientes/arepas-rellenas-samu/PROGRESS.md` del repo `ccm-vouchers-2026` (cierre de la tarea P-009).
