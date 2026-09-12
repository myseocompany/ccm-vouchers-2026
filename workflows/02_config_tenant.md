# Workflow 02 — Configuración del tenant en AriCRM

**Obligación contractual**: Cláusula Quinta, numerales 3 y 6.
**Objetivo**: crear y parametrizar el tenant del cliente en AriCRM Plan Crecer con el alcance contractual e integrar los canales digitales existentes del beneficiario.

## Precondiciones

- Caracterización cerrada (workflow 01).
- Números de WhatsApp del cliente confirmados y autorizados por su titular.
- Usuarios definidos (nombres, correos, roles).
- Aprobación humana para actuar en producción de AriCRM (ver `../POLICIES.md`).

## Pasos

1. Crear tenant en AriCRM con nombre y slug del cliente. Registrar `tenant_id` en `../clientes/<slug>/CLIENTE.md`.
2. Crear 3 usuarios (o los que apliquen), asignar roles. Enviar invitaciones desde la plataforma, nunca compartir credenciales por WhatsApp.
3. Conectar las 3 líneas de WhatsApp vía Evolution API. Verificar QR + estado conectado.
4. Cargar plantilla vertical restaurantes (workflow 03).
5. Configurar integraciones con canales existentes del cliente (obligación 6): IG DM, FB Messenger si aplican y están soportados por AriCRM.
6. Verificar que el cliente puede iniciar sesión y ver el inbox vacío.
7. Guardar evidencia (capturas del panel + IDs de tenant/usuarios) en `../evidencias/<slug>/config-tenant/`.
8. Actualizar `../clientes/<slug>/PROGRESS.md` y cerrar `C-02` en `../clientes/<slug>/TASKS.md` del cliente.

## Criterio de aceptación

- Tenant activo, 3 usuarios logueables, 3 líneas WA en estado conectado.
- Al menos un canal adicional integrado (si el cliente los tiene).
- Capturas de verificación archivadas.

## Notas de propiedad intelectual

Toda esta actividad es **configuración de AriCRM preexistente**. Si aparece una necesidad que requiera código nuevo (ej. un conector no existente), abrir tarea separada en `../velo_wa/` como evolución del producto, no como desarrollo para el contrato (ver `../POLICIES.md`).
