# CCM Vouchers Digitales 2026

> **English speakers**: read `VOLUNTEER.en.md` first. Spanish is the source of truth for all contractual artifacts.

Harness operativo del contrato **CT-239-26-3** entre la Cámara de Comercio de Manizales por Caldas y MY SEO COMPANY S.A.S., para implementar **AriCRM Plan Crecer** en 10 establecimientos gastronómicos beneficiarios.

## Inicio para un LLM

Empezar en `AGENTS.md` y seguir el orden de lectura indicado ahí.

## Inicio para una persona

1. Leer `PROGRAMA.md` para entender objeto, obligaciones, plazos y valor.
2. Leer `POLICIES.md` para reglas de aprobación, propiedad intelectual y protección de datos.
3. Ver `TASKS.md` para el trabajo actual.

## Estructura

- Archivos raíz: identidad (`SOUL`), programa (`PROGRAMA`), políticas (`POLICIES`), memoria (`MEMORY`), fuentes (`SOURCES`), tareas (`TASKS`), decisiones (`DECISIONS`).
- `clientes/` — contexto aislado por cada establecimiento beneficiario (1 al 10). Copiar `_template/` para iniciar.
- `workflows/` — procedimientos operativos, uno por obligación clave del contrato.
- `templates/` — formatos reutilizables (informe individual, informe final, acta de capacitación, dashboard).
- `entregables/` — versiones finales enviadas a la Cámara (informes, actas firmadas).
- `evidencias/` — soportes técnicos por cliente (capturas, logs, exportes).
- `evals/` — checklists de verificación por obligación / vertical.
- `scripts/` — utilidades locales no destructivas.

## Alta de un cliente beneficiario

1. Copiar `clientes/_template/` a `clientes/<slug-del-restaurante>/` (o renombrar un `cliente-NN` existente).
2. Completar `clientes/<slug>/CLIENTE.md` con datos del establecimiento.
3. Ejecutar `workflows/01_caracterizacion.md`.
4. Registrar fecha estimada de activación en `PROGRAMA.md` (para calcular fin de los 4 meses de soporte).
5. No ejecutar acciones externas en producción sin aprobación (ver `POLICIES.md`).

## Relación con otros repos

- `../velo_wa/` — código de AriCRM (producto preexistente de MY SEO). Este harness NO edita ese repo, solo referencia.
- `../myseo-env/` — harness transversal de MySEO. Este contrato NO se documenta ahí; permanece aislado por su naturaleza contractual y su cláusula de propiedad intelectual.
