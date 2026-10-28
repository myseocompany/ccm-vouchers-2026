# Evidencia — creación del tenant patrón de domicilios

- Fecha: 2026-09-17.
- Entorno: AriCRM producción (Waterfall).
- Acción aprobada por: Nicolás, mediante instrucción directa en conversación.
- Nombre: `restaurante-domicilios-v1`.
- Slug: `restaurante-domicilios-v1`.
- Tenant ID: `01a0af48-00e2-70c0-ad2d-10efad059912`.
- Zona horaria: `America/Bogota`.
- Límites verificados: 3 usuarios, 2000 contactos y 3 líneas WhatsApp.
- Estado inicial verificado: 0 usuarios, 0 contactos, 0 líneas WhatsApp, 0 productos y 0 agentes IA.

## Configuración de referencia aplicada

- Agente IA: `Asistente de domicilios — plantilla`.
- Agent ID: `01a0af72-0db0-72f9-907b-5b3be6b9ead0`.
- Modelo: `gpt-4o-mini`; contexto: 20 mensajes; tool calling y transcripción de audio en español configurados.
- Estado seguro: agente desactivado, no predeterminado, sin línea, credencial ni webhook.
- Prompt: `prompts/agente-domicilios/v1-prompt-generico.md`.
- Versión: `v1-prompt-generico`.
- SHA-256 verificado en archivo y producción: `99dfcf0ae399ad34681d7b37bed61b81584ca3fe1fc3e4841154e642134559a7`.
- Etiquetas creadas: 10.
- Automatizaciones creadas: 4, todas desactivadas.
- Verificación posterior: 0 usuarios, 0 contactos, 0 líneas, 0 categorías y 0 productos; el prompt no contiene la palabra `Botanazo`.

La estructura operativa toma como referencia el aprendizaje de Botanazo, pero se saneó antes de aplicarse. No se copiaron menú, precios, imágenes, horarios, cobertura, datos, canales, credenciales ni textos propios de ese establecimiento.

## Acceso administrativo

- Propietario creado: Nicolas Navarro (`nicolas@myseocompany.co`).
- User ID: `e8171e8e-6b1f-4dac-aeab-c2e843b99207`.
- Rol: `owner`, activo; membresía del tenant verificada.
- El acceso reutiliza internamente la misma contraseña ya establecida para ese correo, sin leerla, copiarla ni exponerla.
- Al iniciar sesión, AriCRM detectará dos tenants activos para el correo y mostrará el selector de empresa. Elegir `restaurante-domicilios-v1`.
