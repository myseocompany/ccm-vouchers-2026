# Corte de avance — 2026-11-01

Consolidación de estado por beneficiario, cruzando el harness (`clientes/<slug>/TASKS.md`, `PROGRESS.md`) con el repo del producto (`../velo_wa`, solo lectura) y con las sesiones de Orca. **Hecho vs. inferencia separados**: cada fila cita su fuente.

> Regla aplicada (`AGENTS.md`): este harness no edita `velo_wa`; solo referencia. Ninguna obligación se cierra por este documento.

## 1. Hallazgo principal

El harness **subregistra el avance real**. El trabajo técnico de los agentes IA vive en `velo_wa` (snapshots de prompt versionados, con SHA-256, release y rondas de prueba) y no estaba reflejado en los `TASKS.md` del programa. Ejemplo: el expediente daba a Beto's Pizza `C-03 pendiente`, cuando su catálogo está sembrado y validado en la base del tenant desde el 2026-10-26 y el prompt v5 está publicado.

## 2. Estado por beneficiario

| # | Cliente | Tenant | Prompt / versión | Estado real del agente | Fuente (`velo_wa`) |
|---|---|---|---|---|---|
| 1 | the-boss | The Boss (`01a12179…`) | **v3.2** | **PUBLICADO en producción** 2026-10-31 ~14:00 UTC, release 81742408, gpt-4.1, `inject_open_status=true` | `docs/the-boss/prompts/asistente-domicilios/v3.2-estado-negocio-2026-10-31.md` |
| 2 | mar-azul | Calamar Azul (`01a0fcc8…`) | **v7 publicado / v8 preparado** | v7 publicado 2026-10-31 con gpt-4.1; **ronda 3: 32/32 casos en verde, cero errores de herramienta, 7 `quote_order` exitosos**. `is_enabled=false` + pilot mode con 3 teléfonos autorizados. v8 sin desplegar | `docs/mar-azul/prompts/asistente-whatsapp/v8-…-2026-10-31.md` |
| 3 | sushi-fusion | Mercado Gastronómico Fusión (`01a140b0…`) | **v13** | Publicado 2026-10-29. 13 iteraciones en 2 días. Validaciones 28 y 29-oct + hallazgos de latencia | `docs/sushi-fusion/` (6 docs de validación) |
| 4 | trattorias-y-pastificios (ONO) | — | **v15** | 12 versiones (v4→v15) entre 28 y 30-oct + guion de pruebas. **Rama `myseocompany/review-trattoria-implementation` sin fusionar a main** | `docs/trattorias/` en esa rama |
| 5 | pizzas-beto | BETO'S PIZZA (`01a0c569…`) | **v5** | Publicado 2026-10-26. Catálogo **sembrado y validado en la DB del tenant** el 26-oct; menú retirado del prompt. Tools: `get_catalog, quote_order, create_order, update_contact` — **sin `handoff_to_human`, escalamiento eliminado por decisión del operador**. **Línea WhatsApp `disconnected` desde 2026-10-07**; **cero usuarios en el tenant** (sin membresías). Docs solo en la rama `myseocompany/betos` | `docs/betos/prompts/agente-domicilios/v5-catalogo-db-2026-10-26.md`, `docs/betos/test-conversations.md` |
| 6 | friends-chicken-cable | Friends Chicken (`01a0a5a4…`) | **v5** | Publicado 2026-10-25, ronda C del playground verificada. Sede Cable **cerrada**; opera desde sede Centro | `docs/friends-chicken/prompts/agente-domicilios/v5-fc-cobertura-escala-2026-10-25.md` |
| 7 | indecente | — | **v4.2** | 4 versiones; bienvenida automática neutralizada (26-oct), corte amable de pedidos 20 min antes del cierre (25-oct) | `docs/indecente/prompts/asistente-domicilios/` en rama `myseocompany/indecente` |
| 8 | la-patateria | La Patatería (`01a0cb62…`) | **v9 preparado** | 9 versiones el 12-oct. **No aplicado**: espera confirmación del dueño y regeneración de la KB desde la carta física (95 productos de 20 fotos) | `docs/patateria/prompts/reservas/v9-carta-fisica-2026-10-12.md` |
| 9 | el-efecto-barbacoa | `01a0ac43…` | v3 | **Agente APAGADO** (`is_enabled=false`) desde 2026-10-11 01:58 UTC por incidente: el bot se intercalaba con el equipo humano y prometía reservas no registradas. Fase B ejecutada: sede `Principal` creada + **144 tarifas** cargadas en una transacción, bot OFF. Reactivación requiere acuerdo con Juan Guillermo | `specs/active/efecto-barbacoa-recovery/SPEC.md` (rama `myseocompany/efecto`) |
| — | **cupo 10** | — | — | **sin definir** | `DECISIONS.md` 2026-10-30 |

## 3. Lo que esto cambia frente al estado registrado

| Obligación | Estado en el harness | Estado real evidenciado |
|---|---|---|
| 5 — IA conversacional | 6 de 9 «en progreso» | **4 agentes con prompt publicado en producción** (the-boss, mar-azul, beto's, friends) + 2 publicados sin verificar en main (sushi v13, ONO v15). Mar Azul con batería formal de 32 casos aprobada |
| 4 — Vertical restaurantes | mayoría «pendiente» | Catálogos cargados en DB para beto's (26-oct), efecto barbacoa (144 tarifas, 11-oct), mar-azul, trattorias. **Está más avanzado de lo registrado** |
| 3 — Tenant (3 usuarios, 3 líneas WA) | «pendiente» en 7 de 9 | Confirmado como **real**: Beto's tiene **cero usuarios** y la línea **caída desde el 7-oct**. No es subregistro, es trabajo faltante |

## 4. Riesgos contractuales detectados

1. **Beto's sin escalamiento.** El prompt v5 retiró `handoff_to_human` «por decisión del operador». La obligación 5 exige explícitamente «IA con escalamiento a humano». Hay que documentar la decisión del operador o restituir la tool; si no, la obligación no se puede acreditar.
2. **Beto's con línea caída desde el 7-oct** y sin usuarios en el tenant: las obligaciones 3 y 6 están materialmente sin ejecutar, y el guion de pruebas lo bloquea («no enviar mientras la línea siga en `qr_pending`»).
3. **Efecto Barbacoa con incidente abierto.** Bot apagado por petición del cliente tras fallas en producción. La reanudación depende de una conversación con Juan Guillermo que no está confirmada.
4. **Obligaciones 7 (capacitación) y 8 (activación) en cero** en los 9. Sin activación efectiva no corren los 4 meses de licenciamiento ni de SLA (obligaciones 10 y 11), y el pago es 100% al final.
5. **Evidencia visual inexistente.** Ver `../../evidencias/PLAN_CAPTURAS_2026-10-30.md`: las 17 tomas siguen sin tomarse.
6. **Trabajo disperso en ramas sin fusionar**: trattorias (v4–v15), indecente, beto's y efecto barbacoa viven en ramas de `velo_wa`; `main` del harness está 7 commits por delante de `origin/main` sin empujar.

## 5. Fuentes

- Harness: `clientes/<slug>/TASKS.md` y `PROGRESS.md` al 2026-11-01; commits `546b267`, `b4fcc05`, `040535c`, merge `87c8667`.
- Producto: documentación de tenants ya movida a `evidencias/<slug>/velo_wa/` (ver `DECISIONS.md` 2026-11-01 y cada `PROCEDENCIA.md`). Estado del código en `../velo_wa` commit `27487a21`.
- Orca: 95 worktrees activos; los de este programa son `docs/indecente-octubre`, `sushi-manifesto-intent-flows`, `patateria-carta-{manizales,pereira}`, `patateria-descargar-conversaciones`.
