# AriCRM — Agentes de IA especializados en restaurantes
## Descripción de la iniciativa (Fondo Emprender)

> Borrador. Las cifras de mercado son estimaciones de gremios, no estadística oficial. Los valores presentados como proyección, meta o supuesto son estimaciones de la iniciativa, no resultados ya obtenidos.

## 1. Resumen ejecutivo

La iniciativa desarrolla y comercializa **agentes de inteligencia artificial especializados en restaurantes**: asistentes que atienden por WhatsApp a los clientes de un negocio gastronómico, conocen su menú, precios, horarios, cobertura de domicilio y políticas de reserva, toman pedidos y reservas, y **escalan a una persona** cuando la conversación lo requiere.

Los agentes operan sobre **AriCRM**, una plataforma de gestión de clientes (CRM) que centraliza los chats, los contactos, los pedidos, las reservas y el seguimiento comercial. A diferencia de un chatbot genérico, el agente llega **preconfigurado para el sector** mediante una plantilla vertical de restaurantes, que se parametriza con los datos de cada negocio y permite ponerlo en operación en días.

El objetivo es consolidar este producto como SaaS por suscripción, empezando por Caldas y el Eje Cafetero, y crear los empleos y la capacidad comercial necesarios para escalarlo al resto del país.

## 2. Problema

Los restaurantes, cafeterías y emprendimientos de comida pequeños reciben la mayor parte de sus pedidos y reservas por WhatsApp. Esa operación suele funcionar así:

- Una sola persona atiende los chats desde un teléfono personal, con respuestas manuales y repetitivas (menú, precios, horarios, cobertura, medios de pago).
- Se pierden pedidos y clientes por demoras en la respuesta, sobre todo en horas pico y fuera de horario.
- No hay base de datos de clientes: los contactos quedan dispersos en teléfonos y chats, sin historial ni segmentación.
- No se miden resultados (cuántos pedidos entran, de qué canal, cuáles clientes recompran).
- Las herramientas existentes en el mercado están pensadas para empresas grandes: son costosas, complejas o no están adaptadas al flujo real de WhatsApp de un negocio gastronómico.

## 3. Solución

### 3.1 El agente de IA especializado en restaurantes

El agente conoce el lenguaje y los procesos del sector gastronómico y, con la información de cada negocio, puede:

- Responder 24/7 sobre menú, ingredientes, precios, horarios, ubicación, zonas y costo de domicilio, y medios de pago.
- Tomar pedidos completos (productos, adiciones, dirección, forma de pago) y entregarlos ordenados al equipo.
- Gestionar reservas según las políticas del restaurante.
- Hacer seguimiento y reactivación de clientes con mensajes automáticos.
- **Escalar a una persona** ante quejas, casos fuera de política o cualquier situación que el restaurante defina, conservando todo el contexto de la conversación.

Se limita a la información cargada por el restaurante: no inventa precios, horarios ni políticas.

### 3.2 La plataforma que lo sostiene

Con configuración lista para usar:

| Componente | Qué resuelve |
|---|---|
| **Bandeja multiusuario de WhatsApp** | Varias personas y varias líneas atienden desde un mismo lugar, con historial por cliente. |
| **Menú digital y pedidos** | El cliente consulta el menú y hace su pedido en la conversación; el negocio lo recibe ordenado. |
| **Reservas** | Gestión de reservas desde el chat, sin llevar agendas en papel. |
| **Plantilla vertical de restaurantes** | Estructura, etiquetas, flujos y respuestas modelo listos; solo se parametriza con los datos del negocio. |
| **Etiquetas, plantillas y flujos automáticos** | Segmentación de clientes, respuestas rápidas y mensajes automáticos de seguimiento. |
| **Base de contactos** | Construcción de un activo propio del negocio: su base de clientes. |
| **Métricas** | Indicadores de conversaciones, pedidos y adopción para tomar decisiones. |

El enfoque es la **implementación rápida**: una plantilla vertical de restaurantes que se parametriza con los datos de cada negocio (menú, horarios, políticas, usuarios, líneas), de modo que el restaurante tenga el servicio operando en días y no en meses.

## 4. Validación y tracción

AriCRM ya está en operación comercial. Como evidencia de validación:

- **Programa Vouchers Digitales 2026 (contrato CT-239-26-3)** con la Cámara de Comercio de Manizales por Caldas: implementación de AriCRM Plan Crecer en **10 establecimientos gastronómicos** de la región, con 3 usuarios, 3 líneas de WhatsApp y 2.000 contactos por establecimiento, más capacitación, acompañamiento y 4 meses de soporte prioritario y licenciamiento.
- Primer despliegue sistemático de la plantilla vertical de restaurantes, con proceso de preimplementación, clonación segura de configuración y evidencia técnica por cliente.
- **Agente en producción en un restaurante de arepas rellenas (domicilios):** el agente atendió y capturó pedidos complejos por WhatsApp. Una auditoría propia (2 y 3 de octubre de 2026; 6 conversaciones, 182 mensajes, 44 respuestas automáticas, 2 pedidos creados) mostró respuesta rápida, pero también fallas de confiabilidad: afirmar acciones no verificadas, perder el contexto de una reclamación, inventar una regla de precio y crear pedidos sin validar todos los datos.
- **Corrección estructural validada:** como respuesta, se implementó un **motor de precios determinista** en el servidor, de modo que el modelo de lenguaje ya no suma ni inventa tarifas. Un replay de 11 casos de la auditoría contra el motor real (7 de octubre de 2026) reproduce exactamente los totales correctos en los casos con barrio reconocido, y **bloquea** (error tipado `ZONE_NOT_COVERED`) en vez de cobrar una zona que no cubre. Quedan pendientes alias de barrios y la representación de la doble porción. Esto convierte el aprendizaje en una ventaja de producto: *el agente conversa, el servidor calcula*.
- **Diagnóstico de la operación real (bar-restaurante, 30 días, con autorización del negocio):** 270 conversaciones y 3.767 mensajes en WhatsApp; mediana de primera respuesta de 3,3 min, pero el 10 % de los clientes esperó más de ~53 min. En una muestra de 30 conversaciones candidatas, el análisis propuso 27 posibles oportunidades comerciales desatendidas (hipótesis a validar con etiquetado humano). No existían pedidos, tareas ni asignaciones registradas, es decir, no había forma de medir ventas ni tiempos de seguimiento.
- **ARI Pulse (en desarrollo):** módulo supervisor que detecta conversaciones comerciales desatendidas, alerta primero al asesor y escala a un supervisor si persiste. Es la capa de control que complementa al agente: *el agente atiende, el supervisor vigila*. Se construye como motor independiente con conector delgado en AriCRM, con proyecto de grado/bootcamp universitario y objetivo TRL 6.
- **Otros restaurantes con agente de IA en configuración o producción:** una cadena de pollo frito y domicilios, y un restaurante de comida típica con sistema de reservas, ambos con prompts, pruebas de regresión y especificaciones propias en el repositorio del producto.
- **Producto multi-tenant en producción** (Laravel, PostgreSQL, WhatsApp vía QR y Cloud API de Meta), con planes y límites por suscripción. Actualmente hay **14 empresas activas**.
- Los resultados medidos del piloto con la Cámara (tiempos de respuesta, pedidos, adopción) se incorporarán al cierre de las 6 semanas de implementación y 4 meses de soporte, con evidencia técnica por establecimiento.

## 5. Mercado objetivo

- **Segmento inicial:** restaurantes, cafeterías, comidas rápidas, panaderías y negocios gastronómicos pequeños y medianos que venden por WhatsApp.
- **Alcance geográfico inicial:** Manizales, Caldas y Eje Cafetero; expansión a otras ciudades intermedias de Colombia.
- **Segmentos de expansión:** otros comercios minoristas y de servicios con atención por WhatsApp (belleza, salud, retail, educación), reutilizando el mismo motor con nuevas plantillas verticales.
- **Tamaño del mercado en Colombia (estimaciones de gremios):** entre ~132.000 y más de 150.000 establecimientos gastronómicos, de los cuales ~80.000 serían formales (Acoga, Valora Analitik y Acodres, 2024–2025). El sector crece: las ventas de restaurantes de servicio rápido y casual subieron 12,7 % entre enero y junio de 2026 frente al mismo periodo de 2025, impulsadas por domicilios (GIG Latam / Alianza Team, vía Publimetro, 29-sep-2026). A la vez, Acoga reportó 861 cierres hasta septiembre de 2025 y más de 2.700 en 2024: los márgenes son estrechos y el costo de perder pedidos es alto.
- **Mercado alcanzable (supuesto):** los ~80.000 restaurantes formales son el mercado total; si el 5 % ya vende de forma sistemática por WhatsApp y puede pagar una suscripción, el mercado inicial serían unos 4.000 negocios. Este supuesto se refinará con datos del RUES y de la Cámara de Comercio de Manizales por Caldas.

## 6. Modelo de negocio

Suscripción mensual o anual (SaaS) por plan, con límites de usuarios, líneas de WhatsApp y contactos. El plan **Crecer** incluye 3 usuarios, 3 líneas y 2.000 contactos. Ingresos complementarios:

- Servicio de implementación y parametrización inicial.
- Capacitación y acompañamiento.
- Planes superiores (más usuarios, líneas, contactos, módulos de IA).
- Alianzas de canal con gremios, cámaras de comercio y programas de transformación digital.

**Precios (vigentes en el producto):**

| Plan | Usuarios | Precio de referencia |
|---|---|---|
| Gratis | 1 | Sin costo |
| Crecer | hasta 3 | Planes por agentes y contactos de USD 19 a USD 59 al mes |
| Escalar | hasta 10 | Dentro del mismo rango |

En el piloto con la Cámara de Comercio de Manizales por Caldas, la oferta fue de **$90.000 COP mensuales por establecimiento** durante 4 meses, más **$500.000 COP de implementación**; el contrato CT-239-26-3 se pactó por $5.236.000 COP para 10 establecimientos (≈ $523.600 COP por establecimiento, IVA incluido).

**Supuestos para el plan financiero:**

- Ingreso mensual por restaurante: ~$90.000–$250.000 COP según plan y módulo de agente de IA.
- Implementación rápida de 4 horas por restaurante (plantilla vertical), con costo estimado de 1 persona-día incluyendo preparación y seguimiento.
- Punto de equilibrio: nómina del equipo base + infraestructura ÷ margen por restaurante. Con el fundador y 2 personas contratadas con los recursos del Fondo, se estima en el rango de 40–60 restaurantes activos.
- Costo de adquisición: bajo en la fase inicial por canal institucional (Cámara de Comercio, gremios) y referidos entre restaurantes.

## 7. Ventaja competitiva

- Producto **propio y preexistente**, con control total del roadmap y de la propiedad intelectual.
- **Vertical especializada** en restaurantes, con plantilla lista para operar.
- **Agentes de IA especializados en restaurantes** (no un chatbot genérico), con escalamiento a humano pensado para el ritmo real del servicio.
- **Implementación rápida** y acompañamiento cercano, en español y con conocimiento del contexto local.
- **Confiabilidad por diseño:** precios y totales calculados por un motor determinista, no por el modelo de lenguaje; el agente bloquea en lugar de inventar y no promete acciones que no puede verificar.
- **Supervisión incorporada (ARI Pulse):** alertas de conversaciones desatendidas y escalamiento a humano, con revisión humana de las decisiones comerciales.
- Cumplimiento del régimen colombiano de **protección de datos personales** (Ley 1581 de 2012 y Ley 1266 de 2008) desde el diseño.
- Relación institucional con la Cámara de Comercio de Manizales por Caldas como canal de llegada a empresarios.

## 8. Impacto

- **Para los negocios:** menos pedidos perdidos, respuesta inmediata, base de clientes propia y datos para decidir.
- **Para el empleo:** creación de cargos en implementación, soporte, desarrollo y ventas. Proyección de empleos directos: 2 en los primeros 12 meses (un implementador/soporte y un desarrollador o ejecutivo comercial) y 4 en 24 meses, priorizando jóvenes de Caldas con formación técnica y tecnológica.
- **Para la región:** digitalización de micro y pequeñas empresas gastronómicas y fortalecimiento del ecosistema de tecnología en Caldas.

## 9. Uso de los recursos del Fondo Emprender

Los recursos se destinarían a:

1. **Equipo:** contratación de implementadores, soporte y ejecutivos comerciales.
2. **Producto:** evolución de la plataforma, el agente de IA y nuevas plantillas verticales.
3. **Infraestructura:** servidores, mensajería de WhatsApp y herramientas de IA.
4. **Comercialización:** marketing digital, alianzas de canal y fuerza de ventas.

Se solicitan **$80.000.000 COP**. Distribución propuesta:

| Rubro | % | Valor (COP) |
|---|---:|---:|
| Nómina (implementación/soporte y desarrollo o ventas) | 55 % | $44.000.000 |
| Infraestructura, WhatsApp e inferencia de IA | 15 % | $12.000.000 |
| Comercialización y alianzas de canal | 15 % | $12.000.000 |
| Plantillas verticales y motor de precios | 10 % | $8.000.000 |
| Legal, protección de datos y administración | 5 % | $4.000.000 |
| **Total** | **100 %** | **$80.000.000** |

Cronograma: meses 1–3, contratación y consolidación de la plantilla de restaurantes; meses 4–9, expansión en Caldas y el Eje Cafetero; meses 10–12, segunda ciudad y primera vertical adicional; meses 13–24, escala nacional y alianzas.

## 10. Equipo

- **Nicolás Navarro Rincón** — Ingeniero Electrónico de la Universidad Nacional de Colombia, gerente de MY SEO COMPANY S.A.S. desde enero de 2011 (más de 15 años diseñando estrategias digitales). Certificado en Microsoft Dynamics CRM (personalización, configuración y despliegue), desarrollo de software de Microsoft, SEO y Google Ads, con especialización en marketing. Más de 20 años como docente universitario y de formación técnica (Universidad Católica, Universidad de Caldas, Universidad Nacional, APTECH–Fundación EMTELSA, donde fue también director), lo que respalda la capacitación a los restaurantes.
- El equipo actual es el fundador. Con los recursos del Fondo se contratarán dos personas: un implementador/soporte y un desarrollador o ejecutivo comercial.

## 11. Metas a 24 meses

Metas proyectadas, partiendo de 14 empresas activas.

| Indicador | Meta |
|---|---|
| Restaurantes activos con agente de IA | 60 |
| Ingresos recurrentes mensuales | ~$9.000.000 COP |
| Empleos directos generados | 4 |
| Ciudades con presencia | 2 a 3 |
| Retención de clientes a 6 meses | 80 % |
