# CARACTERIZACIÓN — Calamar Azul, sede Cable

Levantamiento de obligación 2, consolidado el 2026-10-16. Los datos son reportados por el establecimiento; no prueban activación ni autorizan configuración en producción.

## 1. Operación actual

- 28 mesas de cuatro personas (aforo aproximado de 112) y dos rotaciones en el servicio fuerte de mediodía (aprox. 224 comensales).
- Atención lunes a domingo, incluidos festivos, 11:00 a. m.–5:00 p. m.; mayor demanda alrededor de 12:00 m.–2:00 p. m.
- Volumen por canal, ticket promedio y estacionalidad: pendientes de medir.

## 2. Atención al cliente

- WhatsApp lo atiende caja; el agente debe escalar a la cajera en turno, prioritariamente a Viviana Andrea Arango.
- Consultas recurrentes: almuerzo ejecutivo, medios de pago, cambios de acompañamiento y composición de los platos.
- Quejas, alergias, pagos, reclamos, disponibilidad y excepciones deben escalar a humano.
- Tiempo de respuesta, número diario de conversaciones y detalle de canales: pendientes.

## 3. Menú

- Existe un catálogo mediante enlace de WhatsApp, con fotos y precios por plato. Se recibieron 26 capturas; falta URL y matriz estructurada vigente.
- Categorías reportadas: arroces, cazuelas, pescados, almuerzos y especialidades de la casa.
- Cambia normalmente una vez al año, por precios; puede añadir platos ocasionalmente.
- El almuerzo ejecutivo mantiene cinco opciones de pescado, cuesta $26.000 y puede agotarse antes de las 3:00 p. m. No hay integración de inventario.

## 4. Pedidos y pagos

- Pedidos por WhatsApp; otros canales, recogida y modalidad de flota pendientes.
- Programación posible antes de las 11:00 a. m.; despacho desde las 11:00 a. m.; recepción hasta las 4:30 p. m.
- Cobertura: Manizales y Villamaría. **Actualizado 2026-10-30**: existe tabla oficial barrio→tarifa cargada a producción, 133 tarifas por sede (Cable, 7 bandas de $6.000 a $15.000; Centro, 10 bandas). Las tres bandas reportadas en el levantamiento ($5.000/$8.000/$12.000) eran placeholders de onboarding y fueron eliminadas. Caja sigue confirmando el valor mientras el prompt no consulte `get_delivery_fee` — ver sección 9.
- Pagos reportados: efectivo, tarjetas en local, Nequi y QR/cuentas. No hay datáfono en domicilio. Por riesgo reportado de comprobantes falsos, el agente no debe dar datos de recaudo ni confirmar transferencias sin instrucción y verificación humana aprobadas.

## 5. Reservas

- **Actualizado 2026-10-30**: lunes a sábado de **2:00 a 4:30 p. m.** El levantamiento registró «después de las 2:00 p. m.» sin tope; el cliente confirmó que 4:30 p. m. es el último acomodo, consistente con el cierre a las 5:00 p. m. No se reserva en fechas especiales, incluido Día de la Madre.
- Se reserva por 30 minutos tras la hora acordada.
- **Actualizado 2026-10-30**: los **eventos empresariales sí se pueden pactar fuera de la franja**. Es una excepción que el levantamiento no recogió.
- **Actualizado 2026-10-30**: el cliente confirmó $20.000 la reserva y $30.000 la reserva con decoración (no son un valor único acumulado). Queda pendiente el consumo aplicable y el procedimiento de cobro antes de automatizar confirmaciones.
- La franja arranca a las 2:00 p. m. por el alto flujo del almuerzo; la retención de 30 minutos y el costo existen para gestionar el no-show. Fuente canónica: `../../evidencias/mar-azul/vertical-restaurantes/reservas-2026-10-30.md`.

## 6. Brechas digitales priorizadas

1. Falta matriz validada de productos, precios, variantes y agotados; impacto: atención consistente y pedido guiado.
2. Almuerzo ejecutivo con hora de corte y stock variable sin inventario; impacto: evitar promesas de disponibilidad no verificable.
3. Domicilios sin tarifa estandarizada y pagos vulnerables a fraude; impacto: impedir cotizaciones/cobros erróneos y escalar a caja. **Parcialmente cerrada 2026-10-30**: la tarifa quedó estandarizada en datos (266 tarifas en producción), pero el prompt no las consulta, así que el efecto para el cliente es el mismo. La vulnerabilidad de pagos sigue abierta.
4. Reglas de reserva y decoración con valor ambiguo; impacto: evitar cobros y expectativas incorrectas. **Parcialmente cerrada 2026-10-30**: valores y franja confirmados; falta el procedimiento de cobro y corregir el prompt.

## 7. Prioridades de implementación

1. Validar y estructurar el catálogo, URL, precios y reglas de sustitución.
2. Automatizar respuestas de menú, horario y almuerzo ejecutivo con límites de disponibilidad claros.
3. Preparar toma de pedido sin confirmar inventario, domicilio ni pago hasta validación humana.
4. Configurar reservas tras validar tarifas, fechas excluidas y flujo de pago.
5. Activar IA con escalamiento a caja para casos sensibles y excepciones.

## 8. Riesgos y bloqueos

- Hay roles internos propuestos para operación; invitaciones, equipos, conectividad y titular de la línea quedan por verificar.
- Faltan: confirmación documental de Cámara, URL/matriz de menú, línea autorizada, tiempos de entrega e instrucciones de pago verificables. **Actualizado 2026-10-30**: la tarifa de domicilios y las condiciones de reserva ya están resueltas y documentadas.
- No se reportó resistencia al cambio.

## 9. Actualizaciones posteriores al levantamiento

Este documento es el levantamiento del 2026-10-16 y no se reescribe: los cambios se marcan en la sección correspondiente y se registran aquí con su fecha y evidencia.

| Fecha | Qué cambió | Secciones | Evidencia |
|---|---|---|---|
| 2026-10-30 | Tabla oficial barrio→tarifa cargada a producción (133 por sede); placeholders de onboarding eliminados | 4, 6, 8 | `../../evidencias/mar-azul/vertical-restaurantes/domicilios/` |
| 2026-10-30 | Franja de reserva con tope de 4:30 p. m., eventos empresariales fuera de franja y valores desambiguados | 5, 6, 8 | `../../evidencias/mar-azul/vertical-restaurantes/reservas-2026-10-30.md` |
| 2026-10-30 | Prompt de producción editado por fuera del repo; capturado como línea base v5 con hash verificado | — | `../../evidencias/mar-azul/ia-conversacional/prompt-v5-recuperada-produccion-2026-10-30.md` |

**Advertencia vigente**: el `system_prompt` en producción no refleja ninguna de las dos actualizaciones de datos anteriores. No reportar las brechas 3 y 4 como cerradas ante la Cámara hasta que exista una v6 desplegada y verificada. Detalle en `PROGRESS.md`, entradas del 2026-10-30.

## Registro

- **Fecha**: 2026-10-16.
- **Responsables**: MY SEO y establecimiento.
- **Evidencia**: `evidencias/mar-azul/caracterizacion-2026-10-16.md` y capturas de carta en `evidencias/mar-azul/vertical-restaurantes/menu/`.
