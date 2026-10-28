# Tarea de producto — clonación segura de configuración de tenants

**Destino de implementación:** `../velo_wa/` (AriCRM, producto preexistente de MY SEO).  
**Estado:** especificación lista para desarrollo; no implementada.  
**Origen:** P-010 en `../TASKS.md`; dos entrevistas iniciales del programa indican dos variantes operativas: solo domicilios y domicilios con reservas.

## Decisión de diseño propuesta

Implementar una función genérica de AriCRM llamada **clonación segura de configuración**, disponible para cualquier tenant de restaurantes. No debe mencionar CCM ni Vouchers ni crear un producto particular para este contrato.

La función aplica un perfil de configuración aprobado a un tenant destino vacío. No copia un tenant operativo de un restaurante a otro. El origen permitido es una plantilla/base saneada, sin información de clientes.

Perfiles iniciales:

| Identificador | Uso | Incluye |
|---|---|---|
| `restaurante-domicilios-v1` | Restaurante que atiende pedidos a domicilio | Estructura de pedido, etiquetas y respuestas genéricas, campos de zonas, costos y horarios |
| `restaurante-domicilios-reservas-v1` | Restaurante que atiende domicilios y reservas | El perfil anterior más estructura, etiquetas y respuestas genéricas de reservas |

## Lista permitida para copiar

- estructura vacía de menú, categorías y variantes de ejemplo claramente ficticias;
- etiquetas, estados y campos operativos genéricos;
- flujos, plantillas de respuesta y reglas genéricas de automatización;
- capacidades habilitadas del perfil, incluidas las reservas cuando aplique;
- estructura de roles, nunca usuarios ni asignaciones.

## Exclusiones obligatorias

Nunca exportar, mostrar en la previsualización ni crear en el destino:

- contactos, conversaciones, pedidos, reservas, métricas o archivos de un restaurante;
- productos, precios, fotos, horarios, zonas, costos, políticas, tono o conocimiento específico de un restaurante;
- usuarios, correos, teléfonos, contraseñas, sesiones, credenciales, tokens, QR, números de WhatsApp ni integraciones conectadas;
- identificadores internos o referencias que permitan vincular al tenant origen.

## Flujo de operador requerido

1. El operador autorizado elige un perfil versionado y un tenant destino vacío.
2. AriCRM calcula una previsualización del cambio: perfil, versión, objetos permitidos a crear y cualquier conflicto.
3. El operador confirma explícitamente la aplicación después de revisar la previsualización.
4. AriCRM crea únicamente los objetos permitidos dentro del destino, en una transacción reversible o con una reversión documentada.
5. El sistema registra auditoría con actor, fecha/hora, tenant destino, perfil, versión, resultado y conteos por tipo de objeto. La auditoría no incluye datos excluidos.
6. El implementador parametriza los datos reales del restaurante después, con la aprobación de producción aplicable.

## Reglas de seguridad y consistencia

- Solo administradores autorizados pueden crear, publicar, versionar o aplicar perfiles.
- El destino debe estar vacío para los tipos de objeto que se crearán. Si hay conflicto, bloquear la operación; no sobrescribir ni fusionar.
- El perfil se almacena como recurso independiente y saneado, no como exportación directa de un tenant de cliente.
- Cada perfil debe tener versión inmutable. Una modificación crea una nueva versión.
- La operación debe ser idempotente por `tenant_destino + perfil + versión`: un reintento no duplica objetos.
- La API y la interfaz deben aplicar exactamente la misma lista permitida y las mismas exclusiones.

## Criterios de aceptación

- Un administrador puede previsualizar y aplicar los dos perfiles iniciales en tenants de prueba vacíos.
- La prueba de `restaurante-domicilios-v1` crea solo configuración genérica de domicilios; la de `restaurante-domicilios-reservas-v1` añade la configuración genérica de reservas.
- Pruebas automatizadas demuestran que ninguna tabla, campo, relación, archivo o secreto de la lista de exclusiones se lee del origen ni se escribe en el destino.
- Un destino que contiene datos configurables incompatibles queda bloqueado y no se modifica.
- Aplicar dos veces el mismo perfil/versionado no duplica objetos.
- Una auditoría consultable permite demostrar actor, perfil, versión, destino, fecha/hora y resultado.
- La documentación de AriCRM explica que después de aplicar el perfil se deben parametrizar menú, precios, horarios, cobertura, pagos, reservas, usuarios, líneas y escalamiento de cada restaurante.

## Verificación para el programa

Antes de usar la capacidad con un beneficiario, Nicolás debe aprobar la acción de producción. Para cada aplicación, archivar en `evidencias/<slug>/config-tenant/` la versión del perfil, la auditoría de AriCRM, la previsualización aprobada y las pruebas del workflow 03. Esta automatización no cierra C-02 a C-06 por sí sola.

## Encuadre de propiedad intelectual

Es una evolución reutilizable de AriCRM para el vertical restaurantes. No es un módulo, marca ni producto de Vouchers Digitales o de la Cámara.
