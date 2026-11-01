# Procedencia — documentación técnica del tenant

Documentación operativa traída desde el repo del producto (`velo_wa`) al harness del programa el
**2026-11-01**, para que exista una sola copia y no se desactualice. Sustenta las obligaciones 4 y 5
del contrato CT-239-26-3.

| Campo | Valor |
|---|---|
| Repo de origen | `velo_wa` (producto AriCRM) |
| Rama de origen | `main` |
| Commit de origen | `27487a21` |
| Ruta de origen | `docs/the-boss` |
| Archivos | 4 |

## Estado

**Movida.** Los archivos se retiraron de `velo_wa` en el commit `b59d9660` (2026-11-01, rama `main`, sin publicar aún). Esta carpeta es ahora la **única copia**: es la fuente de verdad y aquí se editan.

## Reglas

- Los snapshots de prompt son el registro de qué versión está publicada en cada tenant, con su SHA-256.
  No reescribir un snapshot ya publicado: se agrega una versión nueva.
- Antes de pegar contenido de aquí en un informe para la Cámara, verificar que no incluya datos
  personales de clientes finales, números de línea ni credenciales (`POLICIES.md`).
