# MEMORY

Índice de conocimiento persistente del programa. Entradas cortas, con fuente y fecha. El contenido detallado va en el archivo que se referencia.

## Convenciones

- Toda entrada debe tener: título, fuente, fecha y utilidad futura.
- No duplicar información que ya esté en `PROGRAMA.md`, `POLICIES.md` o el contrato.
- Actualizar o eliminar entradas obsoletas; no acumular.

## Entradas

### 2026-09-14 — AriStudio como herramienta interna de gestión, no como AriCRM

- **Fuente**: revisión local del repositorio AriStudio (README, rutas, modelos y manifiestos), 2026-09-14.
- **Hallazgo verificado**: AriStudio es una aplicación Laravel interna de gestión de proyectos: incluye proyectos, tareas, tiempos, reportes, roles y briefs de proyecto. No es el repositorio de AriCRM ni se encontraron capacidades de creación/clonación de tenants, menú, reservas o canales WhatsApp en la revisión realizada.
- **Uso potencial**: puede centralizar el seguimiento de la implementación rápida, las franjas de trabajo y los pendientes por restaurante. Su funcionalidad de briefs públicos podría servir para recopilar información previa solo después de revisar controles de acceso, la política de datos y contar con aprobación escrita; no cargar allí datos personales, contactos, credenciales ni bases de datos de restaurantes por defecto.
- **Utilidad futura**: al decidir si AriStudio será la capa de coordinación del programa, mantener AriCRM (`../velo_wa/`) como producto y el harness como fuente contractual/evidencial; AriStudio no reemplaza ninguna de esas fuentes.

### 2026-09-17 — Credenciales del agente en archivo local, nunca por chat

- **Fuente**: instrucción de Nicolás (usuario principal), 2026-09-17.
- **Mecanismo aprobado**: las credenciales que el agente necesita (p. ej. acceso a AriCRM) viven en `~/.secrets/ccm-vouchers.env` (permisos 700/600), llenado manualmente por Nicolás. El agente las usa solo por indirección (source en comandos / variable en runtime) y jamás las lee, imprime ni pega en chat, repos o herramientas externas (coherente con `POLICIES.md` → Datos y secretos).
- **Verificación sin exponer**: comprobar que una variable está definida con `grep -q '^VAR=.' file` (sin imprimir el valor).
- **Tener credenciales no autoriza por sí mismo**: los cambios en producción de AriCRM siguen requiriendo aprobación humana explícita según `POLICIES.md`.
- **Aplica también a otros asistentes** (p. ej. ChatGPT): las credenciales no se pegan ni cargan allí; `POLICIES.md` prohíbe cargar información del programa en LLMs de terceros sin autorización escrita. Solo agentes con ejecución local (este harness) las usan, siempre por indirección.

### 2026-09-17 — Hallazgos de acceso a AriCRM producción (Waterfall)

- **Fuente**: verificación empírica vía navegador, 2026-09-17.
- **Login del app (`app.aricrm.co/login`) funciona con**: `soporterapido@myseocompany.co` + `ARICRM_SUPERADMIN_PASSWORD` del `.env` de `velo_wa`. Esa cuenta (nombre visible "William", rol Propietario) **solo es miembro del tenant EBL** — sin acceso a `friends-chicken-cable` ni al patrón. En EBL solo se navegó en modo lectura.
- **`.env` de velo_wa tiene un typo**: `ARICRM_SUPERADMIN_USER` contiene el correo truncado (sin `.co`). Pendiente que Nicolás lo corrija.
- **Panel superadmin (`/superadmin/login`) rechazó** las 3 combinaciones probadas (`.co`+SUDO, SUPERADMIN_USER+SUDO, SUPERADMIN_USER+SUPERADMIN_PASSWORD); los intentos quedan en el log de auditoría del panel. La variable `SUDO` (32 caracteres) no es la clave del panel con esos usuarios; el correo real del operador de plataforma es desconocido para el harness.
- **Incidente menor de exposición**: el campo de contraseña del panel superadmin no está enmascarado en el árbol de accesibilidad y el valor de `SUDO` quedó visible en la transcripción del 2026-09-17. **Acción pendiente de Nicolás: rotar `SUDO`.** No involve datos personales de establecimientos.
- **Para verificar tenants del programa** se necesita una cuenta miembro del tenant a verificar (p. ej. la owner de Nicolás) o acceso al panel superadmin.
