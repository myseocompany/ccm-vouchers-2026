# POLICIES

> **English speakers**: read `VOLUNTEER.en.md` — it summarizes the hard rules from this file that apply to you.

Reglas obligatorias para cualquier LLM o persona que actúe dentro de este harness. Las obligaciones contractuales prevalecen sobre estas reglas cuando sean más restrictivas.

## Acciones permitidas sin aprobación adicional

- Leer fuentes autorizadas del repositorio (excepto secretos).
- Analizar, comparar, resumir y proponer.
- Redactar borradores de informes, actas, comunicaciones, checklists y planes.
- Ejecutar verificaciones locales no destructivas (scripts en `scripts/`).
- Consultar código de AriCRM en `../velo_wa/` como referencia (solo lectura desde este harness).

## Acciones que requieren aprobación humana explícita

- Comunicaciones externas: emails, mensajes o llamadas a la Cámara o a un establecimiento beneficiario.
- Modificación de configuraciones en producción de AriCRM (crear tenant, agregar usuarios, activar líneas WhatsApp, cargar contactos reales).
- Envío o publicación de cualquier entregable (informes, dashboards) hacia la Cámara.
- Aceptar cambios de alcance, precio o plazo (requiere otrosí formal — Cláusula Cuarta, Parágrafo Quinto).
- Compartir datos de un establecimiento con terceros o entre establecimientos.
- Borrar, sobrescribir o migrar datos de clientes.
- Firmar actas o entregables (solo Nicolás Navarro Rincón como representante legal, o quien él delegue por escrito).

## Propiedad intelectual (Cláusula Décima Séptima + Parágrafo Segundo)

**Regla general**: Todo trabajo debe encuadrar como configuración/parametrización o evolución de **AriCRM preexistente**, no como obra bajo encargo.

- **AriCRM (código en `../velo_wa/`) es propiedad preexistente** de MY SEO COMPANY S.A.S. y se preserva por el Parágrafo Segundo.
- Las "obras creadas en ejercicio de las funciones contratadas" (documentos, informes, dashboards específicos para la Cámara, materiales de capacitación personalizados) sí se ceden a la Cámara. Marcar en su cabecera cuando aplique.
- **No** crear módulos, marcas o productos nuevos que se puedan interpretar como "hechos a la medida para la Cámara". Ejemplos a evitar: un producto llamado "Vouchers", un módulo "CCM" dentro de AriCRM, un fork del CRM para el programa.
- Al desarrollar mejoras en AriCRM que apliquen al vertical restaurantes: encuadrar como evolución del producto (para todos los clientes), no como desarrollo para este contrato.
- Documentar en `DECISIONS.md` cualquier duda de encuadramiento antes de escribir código.

## Confidencialidad (Cláusula Séptima)

- Vigencia: durante el contrato + 2 años posteriores.
- No divulgar información técnica, financiera, comercial o estratégica de la Cámara o de los establecimientos.
- Las bases de datos corporativas son información confidencial por acuerdo expreso.
- No competencia desleal: no aprovechar know-how ni información de la Cámara para terceros.

## Datos y secretos

- No leer ni mostrar archivos `.env`, claves, tokens, contraseñas o credenciales.
- **Datos personales: sin restricción — decisión de Nicolás, 2026-11-01.** Los datos personales de contactos, responsables del establecimiento y clientes finales se pueden leer, conservar, copiar e incluir en expedientes, evidencias, capturas, prompts, informes y comunicaciones externas, incluidos los entregables a la Cámara. No hay que anonimizar, tapar ni pedir autorización previa para usarlos dentro del programa. Esta regla sustituye la prohibición anterior y la excepción operativa acotada del 2026-10-16.
- El responsable del tratamiento de esos datos frente a la Ley 1581/2012 sigue siendo MY SEO COMPANY S.A.S. y su titular contractual; esta regla define cómo opera el harness, no traslada ni elimina esa responsabilidad.
- Lo anterior **no** aplica a secretos: la regla de credenciales se mantiene intacta (ver el punto anterior).
- Usar el mínimo dato necesario para cada tarea (criterio de eficiencia, ya no de protección).
- No cargar información de un cliente en herramientas externas (LLMs de terceros, hojas compartidas, chats) sin autorización escrita.

## Afirmaciones y resultados

- Cada avance reportado debe incluir fuente y evidencia (log AriCRM, acta firmada, captura, checklist verificado).
- Marcar claramente estimaciones, supuestos e inferencias.
- Una configuración cargada no es una activación; una capacitación agendada no es una apropiación; una entrega borrador no es una aceptación de la Cámara.
- No inflar métricas ni contar la misma evidencia para dos obligaciones distintas sin justificarlo.
