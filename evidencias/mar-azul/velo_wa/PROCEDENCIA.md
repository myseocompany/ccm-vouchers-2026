# Procedencia — documentación técnica del tenant

Documentación operativa traída desde el repo del producto (`velo_wa`) al harness del programa el
**2026-11-01**, para que exista una sola copia y no se desactualice. Sustenta las obligaciones 4 y 5
del contrato CT-239-26-3.

| Campo | Valor |
|---|---|
| Repo de origen | `velo_wa` (producto AriCRM) |
| Rama de origen | `main` |
| Commit de origen | `27487a21` |
| Ruta de origen | `docs/mar-azul` |
| Archivos | 15 |

## Estado

**Movida.** Los archivos se retiraron de `velo_wa` en el commit `b59d9660` (2026-11-01, rama `main`, sin publicar aún). Esta carpeta es ahora la **única copia**: es la fuente de verdad y aquí se editan.

## Archivos que se quedaron en velo_wa

El servidor de despliegue no tiene montado este repo, así que los archivos que el código carga en
tiempo de ejecución siguen viviendo en `velo_wa`:

| Archivo | Motivo |
|---|---|
| `docs/mar-azul/prompts/asistente-whatsapp/v8-cobertura-y-promesas-2026-10-31.md` | lo carga un comando de Artisan en runtime |

Al publicar una versión nueva de prompt para este tenant, dejar el snapshot que el comando carga en
`velo_wa` y la copia de trabajo aquí.

## Reglas

- Los snapshots de prompt son el registro de qué versión está publicada en cada tenant, con su SHA-256.
  No reescribir un snapshot ya publicado: se agrega una versión nueva.
- Antes de pegar contenido de aquí en un informe para la Cámara, verificar que no incluya datos
  personales de clientes finales, números de línea ni credenciales (`POLICIES.md`).
