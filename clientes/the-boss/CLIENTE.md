# CLIENTE — The Boss Burger

Ficha privada del establecimiento. El estado contractual por obligación vive en `TASKS.md`.

## Identificación

- **Nombre comercial**: The Boss Burger («Horno de brasa»).
- **Razón social**: no reportada en el formulario de caracterización (2026-10-11).
- **NIT**: 1060650166.
- **Ciudad / dirección**: Manizales — Carrera 19 #74A-12, barrio Alta Suiza (código postal 170003).
- **Tipo de cocina / propuesta**: hamburguesería con carne de 160 g y pan brioche, horno de brasa; sándwiches, papas, pinchos y adiciones.
- **Categoría**: restaurante (hamburguesería).

## Contactos y operación AriCRM — uso interno restringido

- **Contacto principal**: Diego López Benjumea — propietario — eljefehamburgueseria@gmail.com — WhatsApp 317 887 5987 (mismo número de Nequi/Daviplata/Bre-B).
- **Receptora de escalamientos de la IA**: Paola Camacho — mesera — correo y teléfono sin respuesta en el formulario (pendientes, 2026-10-11).
- **Usuarios a invitar**: Diego López Benjumea (propietario) y Paola Camacho (mesera); correos y roles de acceso sin respuesta en el formulario. Tercer cupo de usuario sin designar.

Estos datos se usan exclusivamente para invitaciones, asignación de usuarios y escalamiento en AriCRM. No incluirlos en informes, prompts compartidos, capturas, comunicaciones externas ni otros expedientes.

## Alcance contractual asignado

- Usuarios AriCRM: hasta 3. Designados: Diego López Benjumea y Paola Camacho (correos pendientes); invitaciones pendientes.
- Tenant AriCRM: The Boss — `01a12179-0c6e-70d2-9694-d11125bc3295`, zona `America/Bogota`.
- Sede AriCRM: Principal (slug `principal`), creada el 2026-10-11, asociada a la línea WhatsApp «Principal».
- Líneas de WhatsApp: hasta 3. Conectada en producción: 1 («Principal»); número por registrar. Titularidad pendiente de confirmar.
- Contactos disponibles: hasta 2000 (verificación pendiente).

## Hitos temporales

- **Fecha de caracterización**: 2026-10-11 (levantamiento preliminar; pendiente validación del establecimiento) · evidencia: `../../evidencias/the-boss/caracterizacion-2026-10-11.md`.
- **Fecha estimada de activación**: _pendiente_.
- **Fecha de activación EFECTIVA (día D)**: _pendiente_ · evidencia (log AriCRM + captura): _pendiente_.
- **Fecha de licenciamiento — inicio**: (= fecha activación efectiva) · evidencia: _pendiente_
- **Fecha de licenciamiento — fin**: (= activación efectiva + 4 meses calendario) · evidencia de renovación/expiración: _pendiente_
- **Fecha de entrega de informe individual**: _pendiente_ · acuse de recibo: _pendiente_
- **Fecha de cierre del período de soporte**: _pendiente_ · comunicación de cierre: _pendiente_

## Canales digitales existentes (obligación 6)

- WhatsApp: una línea «Principal» conectada a AriCRM en producción (número por registrar).
- Agente IA en la línea «Principal»: «Asistente de domicilios» activo en producción desde el 12-oct (29 conversaciones atendidas y 2 pedidos registrados al 31-oct). Modelo `gpt-4.1`; prompt vigente `v3.2-boss-2026-10-31` (publicado el 2026-10-31, con estado abierto/cerrado inyectado por el servidor). Transcripción de audio e interpretación de imágenes deshabilitadas. Automatización `enviar_menu` (bienvenida + carta) activa.
- Instagram: https://www.instagram.com/the_boss_burgermzl/
- Facebook: https://www.facebook.com/p/The-Boss-Burger-61557136232145/
- Web / dominio propio: no reportado.
- Otros: carta impresa («Menú The Boss – Impresión.pdf») transcrita y verificada en `../../evidencias/the-boss/vertical-restaurantes/menu/carta-the-boss-2026-10-11.md` (23 productos). Nota: el catálogo en producción tenía **31 ítems** al 31-oct (guion de pruebas) — diferencia por depurar.

## Restricciones específicas del cliente

- Horarios de operación: martes a jueves 18:00–22:00; viernes a domingo 17:00–22:00; lunes sin servicio. Cargado en el tenant y verificado por lectura (`../../evidencias/the-boss/operacion-horario-tenant-2026-10-11.md`). Festivos sin configurar (sin información del cliente).
- Aforo: máximo 50 personas.
- Zonas de cobertura de domicilios: operada por **Flash Delivery Manizales** (tercerizada); la tarifa por barrio se traslada al cliente sin subsidio ni recargo. 180 tarifas cargadas en sede Principal el 2026-10-11 (verificadas contra el JSON, suma COP 1.538.000); lectura del 2026-10-31: **179 activas** — diferencia por depurar. Las zonas «en rojo» del PDF no están modeladas: verificar disponibilidad con el operador antes de prometer despacho.
- Métodos de pago aceptados: efectivo y transferencia (Nequi/Daviplata/Bre-B al 317 887 5987). Sin datáfono: si el cliente pregunta por otro medio, el agente escala.
- Recogida en sitio: sí, en Carrera 19 #74A-12 dentro del horario (confirmado 2026-10-11).
- Tiempo de preparación: ~10 minutos (confirmado 2026-10-11). El tiempo de entrega depende de Flash Delivery: no prometer hora de llegada.
- Reservas: no aceptan (confirmado 2026-10-11).
- Restricciones legales/sanitarias: pendiente por confirmar (2026-10-11).
- Tono de marca: «Street Boss» — urbana, directa, segura y cercana; destilado en `../../evidencias/the-boss/ia-conversacional/street-boss-ai-v1-voz-copy.md` (documento de copy, no va en el prompt).

## Estado de inclusión

- The Boss Burger fue incorporado al roster de beneficiarios confirmados por instrucción directa de Nicolás el 2026-10-30 (`../../DECISIONS.md`, entrada «Depuración del listado de beneficiarios»). La confirmación documental de la Cámara por la sustitución queda pendiente de archivar; hasta entonces, no reportar cierres contractuales de este cliente.

## Estado

El estado de cada obligación se consulta en `TASKS.md` de esta misma carpeta.

## SLA de soporte (obligación 11)

- Referencia al SLA vigente: ver `../../workflows/07_soporte_sla.md` (o SLA aprobado por la Cámara en `../../DECISIONS.md`).
- Canales de soporte publicados al cliente: _pendiente_.
