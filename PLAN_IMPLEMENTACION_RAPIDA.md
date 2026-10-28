# Plan de implementación rápida — AriCRM Plan Crecer

**Estado:** borrador interno — requiere aprobación de Nicolás antes de adoptarse como operación.

## Decisión operativa propuesta

Se busca que cada restaurante salga con un servicio útil el mismo día, usando un tenant patrón de restaurantes y una sesión de implementación de **máximo 4 horas**. Esto no reduce el alcance contractual: para cerrar C-02 a C-06 siguen aplicando los criterios de los workflows y la evidencia correspondiente.

La sesión de medio día es viable solo para clientes **precalificados**. El trabajo que normalmente consume tiempo (recibir y depurar menú, políticas, usuarios y números) se debe cerrar de forma asíncrona antes de la sesión. Un cliente sin insumos completos pasa a la siguiente franja; no se improvisan precios, horarios, políticas ni conexiones.

## Principios de la plantilla patrón

- Crear y mantener un tenant/base genérico, versionado como `restaurantes-base-vN`; contiene solo estructura, etiquetas, flujos, respuestas modelo y datos ficticios.
- Clonar únicamente configuración y contenido reutilizable. Nunca contactos, conversaciones, credenciales, tokens, números de WhatsApp ni datos de otro restaurante.
- Parametrizar después de clonar: identidad, menú, horarios, pagos, cobertura, políticas, usuarios, líneas y reglas de escalamiento.
- Tratar la plantilla como configuración del producto AriCRM preexistente; no crear un módulo o producto denominado CCM o Vouchers.
- Registrar versión de plantilla y fecha de clonación en la evidencia de cada cliente para permitir reversión y trazabilidad.

### Perfiles reutilizables para el piloto

Las dos entrevistas disponibles sugieren dos puntos de partida del vertical, no dos tenants que puedan copiarse entre sí:

- `restaurante-domicilios-v1`: estructura de pedido, zonas, costos, horarios, etiquetas y respuestas genéricas de domicilio.
- `restaurante-domicilios-reservas-v1`: el perfil anterior más la estructura genérica de reservas, sus etiquetas y respuestas.

El implementador elige el perfil que corresponda durante el preflight y lo parametriza con las reglas vigentes del restaurante. El perfil no exime ningún criterio contractual ni reemplaza la caracterización: si un restaurante no opera reservas, la decisión y configuración final deben quedar registradas y verificarse contra el workflow 03 antes de cerrar C-03.

## Cadencia propuesta

| Momento | Trabajo | Responsable propuesto | Salida verificable |
|---|---|---|---|
| D-5 a D-2 | Enviar y revisar formulario de preimplementación; pedir menú y políticas | Restaurante + MY SEO | Formulario completo y archivos recibidos |
| D-1 | Validación de datos, clonar patrón, preparar menú y guion de pruebas | MY SEO | Cliente clasificado listo / no listo |
| Día D, 4 h | Configurar, conectar, probar, capacitar y dejar operación inicial | MY SEO + operador del restaurante | Servicio operativo y evidencia técnica |
| D+1 a D+2 | Correcciones menores y monitoreo de arranque | MY SEO | Incidencias y ajustes registrados |
| D+7 | Métricas base y confirmación de autonomía | MY SEO + restaurante | Cierre de C-06, si cumple criterios |

Con un bloque de 4 horas por cliente se pueden programar **dos sesiones por día**. Para no saturar soporte ni calidad, se recomienda comenzar con una ola piloto de 2 restaurantes, ajustar el patrón y luego ejecutar olas de 2–3 por día. La caracterización ligera puede hacerse mediante el formulario y una llamada de validación de 20–30 minutos, pero sigue debiendo cumplir el workflow 01.

## Regla de entrada: listo para sesión

Un restaurante entra a agenda solo si, a más tardar D-1, tiene:

- formulario completo y responsable operativo presente en la sesión;
- menú y precios finales; fotos son opcionales para el lanzamiento, no para inventar contenido;
- horario, medios de pago, cobertura/costo de domicilio y política de reservas;
- hasta 3 usuarios definidos con correo y rol;
- hasta 3 líneas WhatsApp cuyos titulares/operadores estarán disponibles para autorizar y escanear QR; nunca se reciben contraseñas;
- decisión explícita sobre qué consultas resuelve la IA y cuáles escalan a humano;
- confirmación de que hay computador, conexión y tiempo de una persona del restaurante.

Si falta un elemento crítico (menú, operador de WhatsApp, responsable humano o reglas comerciales), se mantiene la sesión como diagnóstico/preparación y se agenda activación al completar el faltante. No se marca una obligación como terminada por una configuración parcial.

## SOP de sesión de medio día

| Bloque | Minutos | Actividad | Evidencia / criterio |
|---|---:|---|---|
| 1. Apertura y validación | 0–20 | Confirmar insumos, alcance, responsable humano y prueba de conectividad | Lista de preflight completada |
| 2. Base y accesos | 20–60 | Clonar patrón, renombrar tenant, crear usuarios por invitación | Tenant y usuarios verificables |
| 3. Canales | 60–100 | Conectar líneas autorizadas; integrar canal adicional si existe y es soportado | Estado conectado capturado |
| 4. Operación | 100–175 | Parametrizar menú, pedidos, reservas, etiquetas y respuestas | Menú y reglas validadas por restaurante |
| 5. IA | 175–205 | Ajustar conocimiento, tono, horarios y reglas de escalamiento | Prompt versionado; humano receptor definido |
| 6. Pruebas | 205–225 | Probar pedido, reserva, horario, queja y pregunta fuera de menú | Resultados de 5 pruebas |
| 7. Microcapacitación | 225–240 | Inbox, escalamiento, menú y soporte; definir día D si no se activa en el acto | Responsable capacitado y próximos pasos |

La capacitación formal, el acompañamiento de la primera semana y las actas siguen el workflow 05 y 06. Si el bloque no alcanza para las tres líneas o la capacitación completa, no se declara implementación completa: se deja una actividad con dueño y fecha dentro de las 48 horas siguientes.

## Semáforo de factibilidad

- **Verde:** todos los datos y operadores disponibles. Sesión de 4 h puede activar el servicio y avanzar C-02–C-04.
- **Amarillo:** faltan fotos, canal adicional o una línea secundaria. Puede salir una operación inicial, con pendientes fechados; no cerrar el criterio incompleto.
- **Rojo:** falta menú/precios, responsable humano, acceso autorizado a líneas o conectividad. No programar activación; usar el espacio para caracterización y desbloqueo.

## Control posterior

- Primeras 48 horas: monitoreo de conversaciones, líneas y escalamiento; registrar correcciones.
- Día 7: guardar métricas de línea base y pedir confirmación escrita de autonomía.
- Cada mes hasta completar 4 meses desde la activación efectiva: tickets, SLA, licenciamiento y métricas.
- Al cierre: informe individual con evidencia y acuse de la Cámara; luego consolidado final.

## Límites de aprobación

Este plan no autoriza contactar restaurantes, crear tenants, invitar usuarios, conectar líneas, cargar contactos ni publicar entregables. Cada acción de producción o comunicación externa requiere la aprobación humana indicada en `POLICIES.md`.
