# CLIENTE — Trattorias y Pastificios S.A.S.

Ficha del establecimiento beneficiario. Este archivo contiene **datos** del cliente. El **estado** de las obligaciones vive en `TASKS.md` (fuente canónica).

## Identificación

- **Nombre comercial**: ONO / DOYO (marcas operativas reportadas en la caracterización 2026-10-03) — grupo TRATTORIAS Y PASTIFICIOS S.A.S. El grupo también opera la marca KOMO (asiática). **Marca que atiende la línea del beneficio: ONO** (decisión del establecimiento 2026-10-03; DOYO queda en stand-by y se pedirá a MenuApp que lo oculte; verificado en producción 2026-10-05).
- **Razón social**: Trattorias y Pastificios S.A.S.
- **NIT**: 900322813
- **Ciudad / dirección**: Manizales — Cra 24a # 59-15 (tabla Cámara); MenuApp reporta Calle 77 #21-117 (discrepancia abierta, 2026-10-03).
- **Tipo de cocina / propuesta**: Múltiples marcas bajo la misma razón social: KOMO (asiática), ONO, DOYO — cocinas diferentes por marca
- **Categoría**: restaurante

## Contactos

- **Contacto principal**: Lorena Briceño — representante legal — 3176372474
- **Contacto dirección (reportado 2026-10-03)**: Paulo Restrepo — Director — paulo_restrepo@me.com
- **Contacto operativo (operará AriCRM y recibe escalamientos de la IA, reportado 2026-10-03)**: Ángela Bedoya — Administradora de Punto — bedoyaangela1507@gmail.com
- **Líder del proyecto por el establecimiento (reportado 2026-10-03)**: Steven — área de tecnología y apoyo a compras; auditor diario designado de las conversaciones del bot (usuario AriCRM por crear) y segundo contacto de escalamiento para órdenes especiales/muy grandes (apellido y correo por confirmar).
- **Contacto operativo previo (línea 3245170251)**: Juan Pablo López — 3245170251
- **Correo principal**: paulo_restrepo@me.com (reportado 2026-10-03)
- **Contacto técnico**: _pendiente_
- **Contacto administrativo**: _pendiente_

## Alcance contractual asignado (Parágrafo Primero – Cláusula Primera)

- Usuarios AriCRM: hasta 3. Designados: Ángela Bedoya (operadora, 2026-10-03) y Steven (auditor/seguimiento del proyecto, 2026-10-03, por invitar); slot adicional pendiente.
- Líneas de WhatsApp: 3. Línea principal reportada (2026-10-03): 310 482 3232 (atendía ONO/DOYO; **desde 2026-10-03 atiende solo ONO**, DOYO en stand-by). Líneas 2 y 3: pendientes. (Línea histórica en la tabla: 3245170251.) **Por ahora se conectará una sola línea** (decisión operativa 2026-10-03).
- Contactos disponibles: hasta 2000.

## Hitos temporales (con evidencia)

- **Fecha de caracterización**: 2026-10-03 (levantamiento preliminar, pendiente validación) · evidencia: `../../evidencias/trattorias-y-pastificios/caracterizacion-2026-10-03.md`
- **Fecha estimada de activación**: _pendiente_
- **Fecha de activación EFECTIVA (día D)**: _pendiente_ · evidencia (log AriCRM + captura): _pendiente_
- **Fecha de licenciamiento — inicio**: (= fecha activación efectiva) · evidencia: _pendiente_
- **Fecha de licenciamiento — fin**: (= activación efectiva + 4 meses calendario) · evidencia de renovación/expiración: _pendiente_
- **Fecha de entrega de informe individual**: _pendiente_ · acuse de recibo: _pendiente_
- **Fecha de cierre del período de soporte**: _pendiente_ · comunicación de cierre: _pendiente_

## Canales digitales existentes (obligación 6)

- WhatsApp: 310 482 3232 (ONO/DOYO, ~2 años de uso; reportado 2026-10-03; **desde 2026-10-03 atiende solo ONO**, DOYO en stand-by). Línea histórica en la tabla: 3245170251. **Conectada en AriCRM** (evolution, 2026-10-03 01:07 UTC; verificación waterfall en `../../evidencias/trattorias-y-pastificios/config-tenant/verificacion-2026-10-03.md`).
- Instagram: sí — canal activo para el proyecto, handle `@doyo_col` (2026-10-03)
- Facebook: no activo para el proyecto (2026-10-03)
- Web / dominio propio: no activo para el proyecto (2026-10-03)
- Otros: menú vía link de MenuApp/MenuUp (fotos cargadas); base de clientes en Excel (remarketing). Canales activos: WhatsApp e Instagram.
- Menú MenuApp (links recibidos 2026-10-03): `../../evidencias/trattorias-y-pastificios/menu-menupp-2026-10-03.md` (DOYO, ONO y general).

## Restricciones específicas del cliente

- Horarios de operación: lunes a viernes 11:30–15:00 y 18:00–22:00; sábado 11:30–22:00; domingo 11:30–20:40; festivos cerrado (2026-10-03).
- Zonas de cobertura de domicilios: Manizales y Villamaría; flota tercerizada (2026-10-03).
- Métodos de pago aceptados: Bold, Datáfono Bancolombia, transferencia bancaria y Bre-B; no se acepta efectivo a domicilio (confirmado 2026-10-03).
- Restricciones legales/sanitarias: _pendiente por confirmar (2026-10-03)_
- Aforo / tráfico al lugar: no se trabaja aforo ni se envía tráfico al lugar; operación a domicilio (2026-10-03).
- Tono de comunicación: neutro, jovial (2026-10-03).
- **Multi-marca**: opera 3 marcas con cocinas diferentes (KOMO, ONO, DOYO). Nota Sandra 31/08: podría requerir **2 configuraciones/robots** (uno para KOMO y otro para ONO+DOYO). A validar contra el alcance contractual (3 líneas WA por establecimiento) y confirmar con la Cámara si esto se acomoda dentro del alcance de UN tenant o requiere tratamiento especial. **Actualización 2026-10-03**: el formulario de caracterización fue respondido para las marcas **ONO/DOYO**, con línea principal 310 482 3232. **Actualización 2026-10-03 (resuelto)**: la línea atiende **solo ONO**; DOYO en stand-by (el establecimiento pedirá a MenuApp que lo oculte). KOMO queda fuera de la línea actual. Ver `../../evidencias/trattorias-y-pastificios/reunion-revision-bot-2026-10-03.md`.

## Contexto pre-caracterización (línea base recibida de la Cámara)

- **Estado en programa**: Renovada 2026 — reunión inicial realizada. **Aceptación aún no confirmada explícitamente** en la fuente; la rep legal manifestó que consultaría. **Actualización 2026-10-03**: el establecimiento (Paulo Restrepo, Director) respondió el formulario de caracterización —señal de vinculación—; la aceptación formal sigue pendiente.
- **Afectación**: Daños estructurales y cierre de operaciones. Pérdida total de cristalería, inventario de vinos y menaje.
- **Operación actual**: _pendiente confirmar_.
- **Fuente**: gestión Sandra 31/08/2026 con Lorena Briceño (rep legal); mensaje inicial por WhatsApp pendiente de respuesta.

## Estado

El estado de cada obligación se consulta en `TASKS.md` de esta misma carpeta.

## SLA de soporte (obligación 11)

- Referencia al SLA vigente: ver `../../workflows/07_soporte_sla.md` (o SLA aprobado por la Cámara en `../../DECISIONS.md`).
- Canales de soporte publicados al cliente: _pendiente_.
