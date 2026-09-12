# AGENTS

> **English speakers**: read `VOLUNTEER.en.md` first. It is the concise operating guide in English.

Punto de entrada para cualquier LLM que opere en el harness del programa Vouchers Digitales 2026 (contrato CT-239-26-3 con la Cámara de Comercio de Manizales por Caldas).

Antes de actuar, leer en este orden:

1. `SOUL.md` — rol y principios del harness.
2. `PROGRAMA.md` — objeto contractual, obligaciones, plazos y entregables.
3. `POLICIES.md` — límites, aprobaciones, IP y protección de datos.
4. `MEMORY.md` — índice de conocimiento persistente.
5. `SOURCES.md` — jerarquía de fuentes.
6. `TASKS.md` — trabajo actual del programa.
7. `DECISIONS.md` — decisiones aprobadas.
8. `README.md` — mapa del repositorio.

## Reglas de operación

- Identificar el cliente y la obligación contractual antes de trabajar. Si no está claro, no mezclar contextos entre clientes.
- Cargar detalles bajo demanda; no leer todo el repositorio por defecto.
- Separar hechos, inferencias, propuestas y decisiones aprobadas.
- Toda cifra/afirmación de avance debe tener fuente verificable (evidencia técnica, acta, log de AriCRM).
- Antes de una acción externa (comunicación con la Cámara o con un cliente, publicación, envío), verificar `POLICIES.md` y el workflow aplicable.
- El código de AriCRM vive en `../velo_wa/`. Este harness NO edita ese repo: solo referencia y coordina. Los cambios de código se piden como tareas específicas para trabajar en `velo_wa`.
- Credenciales, tokens y datos personales de los clientes nunca se leen, copian ni exponen.
- Mantener `TASKS.md`, `clientes/<c>/PROGRESS.md` y `clientes/<c>/TASKS.md` actualizados.
- Una obligación contractual se cierra por evidencia (entregable + acta + verificación), no porque el LLM declare que terminó.

## Flujo mínimo por obligación

`entender obligación → localizar workflow → planear → ejecutar en el cliente correspondiente → verificar contra el criterio del workflow → adjuntar evidencia → actualizar PROGRESS.md → si aplica, generar entregable en templates/`

## Clientes

- Cada uno de los 10 establecimientos beneficiarios vive en `clientes/cliente-<NN>/`.
- Nunca copiar datos, credenciales, líneas de WhatsApp ni contactos entre clientes.
- Usar `clientes/_template/` para iniciar un cliente nuevo (o renombrar `cliente-XX` a un slug significativo cuando se conozca).
- Las restricciones del cliente prevalecen sobre las generales cuando sean más restrictivas.
