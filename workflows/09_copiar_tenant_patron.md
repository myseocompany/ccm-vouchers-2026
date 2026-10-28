# SOP 09 — Copiar el tenant patrón de domicilios

## Objetivo

Copiar la configuración genérica de `restaurante-domicilios-v1` a un tenant destino vacío, sin trasladar datos de clientes, conexiones ni decisiones comerciales específicas.

Este SOP acelera la parametrización inicial; no cierra por sí mismo C-02 a C-06 ni sustituye los workflows 02 a 06.

## Alcance de la copia actual

La función **Configuración → Copiar configuración** de AriCRM copia desde la base:

- etiquetas;
- automatizaciones, que quedan desactivadas;
- agente IA, que queda desactivado y sin línea ni credencial;
- categorías, productos, respuestas rápidas y plantillas internas, si la base los tuviera.

La base `restaurante-domicilios-v1` tiene actualmente 10 etiquetas, 4 automatizaciones y 1 agente IA. No tiene usuarios, contactos, canales, menú, productos ni categorías.

La función no copia usuarios, contactos, conversaciones, líneas de WhatsApp, credenciales, sesiones, conexiones, webhooks ni archivos de otros clientes.

## Precondiciones

- [ ] El cliente fue caracterizado y cuenta con aprobación para crear/configurar su tenant en producción.
- [ ] El tenant destino existe y tiene un usuario con rol administrador para entrar a Configuración.
- [ ] El destino no tiene etiquetas, automatizaciones, agentes IA, menú, productos, respuestas rápidas ni plantillas internas. La herramienta rechaza destinos que ya contienen esta configuración.
- [ ] El implementador tiene acceso administrativo autorizado a `restaurante-domicilios-v1` y al tenant destino.
- [ ] Están disponibles el menú, precios, horarios, zonas, costo de domicilio, tiempos, métodos de pago y responsable humano reales del cliente.
- [ ] Se abrió la carpeta de evidencia `evidencias/<slug>/config-tenant/`.

## Procedimiento

### 1. Obtener el código de la base

1. Iniciar sesión en `restaurante-domicilios-v1` con un administrador autorizado.
2. Ir a **Configuración → Copiar configuración**.
3. En **Usar este tenant como modelo**, seleccionar **Generar código**.
4. Copiar el código hexadecimal de 64 caracteres mediante un canal operativo privado. No publicarlo en documentos, chats abiertos ni entregables.

### 2. Aplicar la copia en el destino

1. Iniciar sesión en el tenant destino con un administrador autorizado.
2. Ir a **Configuración → Copiar configuración**.
3. Confirmar que el nombre mostrado en **Tenant destino** corresponde al establecimiento correcto.
4. Pegar el código de la base en **Código del tenant modelo**.
5. Seleccionar **Cargar configuración**.
6. Registrar los conteos mostrados por AriCRM y tomar una captura del resultado.

## Verificación inmediata

- [ ] Se copiaron 10 etiquetas genéricas de domicilios.
- [ ] Se copiaron 4 automatizaciones y todas siguen desactivadas.
- [ ] Se copió un agente llamado `Asistente de domicilios — plantilla`; sigue desactivado, no es predeterminado y no tiene línea o credencial.
- [ ] No aparecieron contactos, conversaciones, usuarios, líneas, canales, credenciales ni menús de otro restaurante.
- [ ] El nombre, prompt y automatizaciones no contienen información de Botanazo ni de otro cliente.
- [ ] La captura y el resultado se guardaron en `evidencias/<slug>/config-tenant/`.

Si falla cualquier verificación, no habilitar agente ni automatizaciones. Registrar el incidente en el progreso del cliente y conservar la evidencia antes de continuar.

## Parametrización obligatoria posterior

La copia solo deja una estructura. Antes de activar el servicio, completar en el tenant destino:

1. Nombre del restaurante y placeholders del prompt.
2. Menú, productos, precios, variantes y disponibilidad reales.
3. Horarios, zonas, costo de domicilio, tiempos, medios de pago y políticas de pedido.
4. Responsable humano y reglas de escalamiento.
5. Usuarios por invitación y líneas WhatsApp con sus operadores presentes; nunca solicitar contraseñas.
6. Revisión individual de cada automatización y activación únicamente cuando sus reglas y mensajes estén confirmados.
7. Pruebas de horario, pedido, cobertura, pago, queja y escalamiento conforme a los workflows 03 y 04.

## Evidencia mínima

Guardar en `evidencias/<slug>/config-tenant/`:

- captura de la pantalla de copia y sus conteos;
- fecha, tenant destino, versión `restaurante-domicilios-v1` y responsable que ejecutó la copia;
- captura del agente y automatizaciones desactivados;
- checklist de verificación anterior;
- evidencia posterior de la parametrización y pruebas reales del cliente.

Actualizar `clientes/<slug>/PROGRESS.md` y `clientes/<slug>/TASKS.md`. No marcar una obligación como completa hasta cumplir su workflow y criterio de aceptación específicos.

## Reversión y contingencia

La herramienta actual solo permite copiar sobre destinos sin configuración clonable. Si se aplicó al tenant equivocado o se detecta contenido improcedente, no reutilizar ese tenant para otro cliente. Detener la configuración, conservar evidencia y solicitar una decisión de Nicolás antes de borrar, recrear o modificar masivamente datos.
