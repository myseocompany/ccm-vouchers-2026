# PROGRESS — Friends Chicken Cable

Bitácora cronológica de lo que se hizo, con evidencia. No borrar entradas: rectificar con nueva entrada si algo cambia.

## Formato

```
### YYYY-MM-DD — Título corto
- **Qué se hizo**:
- **Obligación asociada**:
- **Responsable**:
- **Evidencia**: ubicación (ruta al archivo, ID de acta, log ID, correo).
- **Notas**:
```

## Entradas

### 2026-09-17 — Copia del tenant patrón aplicada y verificada (SOP 09)
- **Qué se hizo**: Nicolás aplicó la copia de configuración desde `restaurante-domicilios-v1` al tenant `Friends Chicken` (`friends-chicken-uHMR`, ID `01a0a5a4-1cda-7099-bfe7-c993e6f1352b`) a las 13:35:11. Verificación posterior por lectura directa de BD de producción (servidor `waterfall`, solo lectura, vía `php artisan tinker`).
- **Resultado de la copia**: ✅ 10 etiquetas genéricas; 4 automatizaciones "Plantilla - …" todas desactivadas; agente `Asistente de domicilios — plantilla` desactivado, no predeterminado, sin línea ni credencial; 0 menús/productos/plantillas/credenciales; 0 apariciones de `Botanazo` en nombres, prompts y configs.
- **Incidentes detectados** (previos a la copia, no causados por ella):
  1. Línea WhatsApp en estado `connected` desde 2026-09-15 15:23.
  2. 60 contactos y 60 conversaciones creadas el 15/09 (23) y 16/09 (37) — tráfico previo en el tenant.
  3. 0 membresías de usuario: nadie puede entrar al tenant por login normal; la copia se hizo presumiblemente vía panel superadmin.
- **Obligación asociada**: 3 y 6 (C-02).
- **Responsable**: copia: Nicolás; verificación: agente del harness.
- **Evidencia**: `evidencias/friends-chicken-cable/config-tenant/2026-09-17-verificacion-copia-config.md`.
- **Notas**: Pendiente decisión de Nicolás sobre los datos previos (conservar si corresponden al arranque real del cliente; borrar requiere aprobación explícita según `POLICIES.md`). Pendiente invitar administrador del establecimiento. Agente y automatizaciones permanecen desactivados conforme al SOP ante verificaciones fallidas.
