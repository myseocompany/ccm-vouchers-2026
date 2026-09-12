# Workflow 04 — Agente IA con escalamiento a humano

**Obligación contractual**: Cláusula Quinta, numeral 5.
**Objetivo**: configurar el agente IA de atención automatizada del tenant, con reglas de escalamiento a personal humano del establecimiento.

## Precondiciones

- Vertical restaurantes activo (workflow 03).
- Menú, políticas y horarios del cliente cargados (son la base de conocimiento del agente).
- Criterios de escalamiento definidos con el cliente (qué debe atender la IA y qué debe pasar a humano).

## Pasos

1. Configurar el prompt/base de conocimiento del agente con: nombre del negocio, tono, menú, políticas de pedido/reserva, horarios, zonas de cobertura, información de contacto humano.
2. Definir reglas de escalamiento: quejas, pedidos fuera de horario, temas fuera de dominio, palabras clave sensibles, N mensajes sin resolver.
3. Configurar destinatario del escalamiento (usuario/grupo AriCRM + notificación).
4. Pruebas de conversación cubriendo: pedido feliz, reserva feliz, queja (debe escalar), pregunta fuera de menú (debe escalar), consulta de horario (debe resolver).
5. Ajustar prompt según resultados. Iterar hasta que la tasa de escalamiento sea razonable (ni todo pasa, ni nada pasa a humano).
6. Documentar el prompt/versión utilizada en `evidencias/<c>/ia-conversacional/prompt-v1.md`.
7. Cerrar `C-05` en `TASKS.md` del cliente.

## Criterio de aceptación

- 5 conversaciones de prueba con clasificación correcta (resolvió / escaló).
- Escalamiento llega efectivamente al humano designado con contexto suficiente.
- Prompt versionado y guardado.

## Notas

- El agente IA es funcionalidad **preexistente de AriCRM** (ver `PROGRAMA.md`). La configuración por cliente NO se cede a la Cámara; es parametrización de producto.
- No usar datos personales de contactos como ejemplos en el prompt.
