# Procedencia — documentación técnica del tenant

Documentación operativa traída desde el repo del producto (`velo_wa`) al harness del programa el
**2026-11-01**, para que exista una sola copia y no se desactualice. Sustenta las obligaciones 4 y 5
del contrato CT-239-26-3.

| Campo | Valor |
|---|---|
| Repo de origen | `velo_wa` (producto AriCRM) |
| Rama de origen | `myseocompany/review-trattoria-implementation` |
| Commit de origen | `b595b964` |
| Ruta de origen | `docs/trattorias` |
| Archivos | 14 |

## Estado

**Traída, pendiente de retirar en origen.** Los archivos siguen en `velo_wa` en la rama `myseocompany/review-trattoria-implementation`, que no está fusionada a `main`. Borrarlos allí ahora obligaría a commitear sobre una rama de trabajo ajena y se reintroducirían al fusionar. Retirarlos cuando esa rama entre a `main` (registrado en `velo_wa/docs/TENANTS_CCM_VOUCHERS.md`). Mientras tanto, **editar aquí**.

## Reglas

- Los snapshots de prompt son el registro de qué versión está publicada en cada tenant, con su SHA-256.
  No reescribir un snapshot ya publicado: se agrega una versión nueva.
- Antes de pegar contenido de aquí en un informe para la Cámara, verificar que no incluya datos
  personales de clientes finales, números de línea ni credenciales (`POLICIES.md`).
