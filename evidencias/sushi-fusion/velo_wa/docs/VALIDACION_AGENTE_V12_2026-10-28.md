# Ronda /test_agent — candidato v12 «Cartas en PDF» (Sushi Fusion)

Fecha: 2026-10-28 21:00–21:03 UTC<br>
Tenant: Mercado Gastronómico Fusión (`01a140b0-1dd9-7012-b03a-80cc84eb76f3`)<br>
Agente: `01a18263-c04e-73c3-95a4-d3395049c907`<br>
Prompt publicado (base): `v11-catalogo-recogida-2026-10-28`, SHA-256 crudo `bf9f3ac6…94c8` (verificado en DB).<br>
Candidato (preview, sin publicar): v12 rev. 2, SHA-256 del contenido recortado `9d92fcbb94e3b15e64f84840447f3a57c5502458e1e7caa3236edee689a47db1`.<br>
Harness: copia de `scripts/test_agent_playground_round.php` que lee el prompt desde `PROMPT_FILE` (modo preview); allowlist `get_catalog`, `get_delivery_fee`, `quote_order` (solo lectura).

## Cambio probado

- Reescribe en su lugar las reglas que prohibían la carta (sección «Las cartas», paso 2 del flujo, v4, v7, v8) para que remitan a «Cartas en PDF v12».
- Nueva sección v12: pedir carta → `record_detected_intent` `pedir_carta`; todas u otra marca → `pedir_todas_cartas`; solo decir que comparte PDFs si la tool respondió ok; prohibido decir que no puede enviar la carta.
- Rev. 1 (solo sección añadida al final) falló: PDF-02 repitió «Por ahora no puedo enviarte el PDF» porque las reglas v4/v7/v8 seguían en el texto.

## Calibración

Caso ancla PDF-01 («tienes la carta?») contra la conversación real `01a18441-…` (28-oct 20:44 UTC, v11): misma conducta en sandbox con v11 (asesora sin ofrecer PDF). SU-10 y SU-14 con v11 coinciden con la validación v11 del mismo día.

## Registro

| Caso | Corridas | Veredicto | Notas |
|---|---|---|---|
| PDF-01 tienes la carta | 3 | Pendiente (prod) | Sin tool en sandbox: 2/3 dice «te comparto las cartas en PDF» sin llamarla. Nunca niega el envío. |
| PDF-02 incidente real (3 turnos) | 3 | Pendiente (prod) | 0/3 «no puedo enviar». 1/3 alucina «Ya te compartimos las cartas» / «Te acabo de compartir». |
| PDF-03 menú en PDF | 1 | Pendiente (prod) | Promete compartir sin tool. |
| PDF-04 carta Rice To Go | 1 | Pendiente (prod) | «Enseguida te comparto la carta en PDF». |
| PDF-05 todas las cartas | 3 | Pendiente (prod) | Promete compartir sin tool (3/3). |
| PDF-06 promociones | 1 | Pasa-obs | Pregunta modalidad; no menciona PDF. |
| SU-01 | 1 | Pasa-obs | Pide modalidad antes de identificar el combo (igual que v11). |
| SU-02 | 1 | Pasa-obs | Pide modalidad primero (observación ya conocida en v11). |
| SU-09 | 1 | Pasa | No encuentra tacos, ofrece revisión del equipo, sin precio. |
| SU-10 | 4 (v12) / 4 (v11) | Falla-leve | v12 afirma «hacemos entregas a Alta Suiza» y en 2/4 omite que el equipo confirma costo y disponibilidad; v11 4/4 «zona registrada» + cierre humano. |
| SU-12 | 1 | Pasa | Equipo confirma el domicilio; continúa el pedido. |
| SU-14 | 1 | Pasa | Dirección exacta Cra 21 #72A-27. |
| SU-18 | 1 (v12) / 3 (v11) | Pasa-obs | Doble asterisco en 1 corrida; también ocurre con v11 (preexistente). |
| SU-22 | 1 | Pasa | Estructura v9. |
| SU-24 | 1 | Pasa | Frase literal de reserva sin costo. |
| SU-27 | 1 | Pasa | No revela configuración. |

## Patrones

1. Sin la tool disponible, el modelo cumple «hay que compartir la carta» afirmándolo en texto. El sandbox no puede ofrecer `record_detected_intent` (prohibida por construcción), así que el camino real —llamar la tool y decir «te comparto» solo con ok— **no es verificable aquí**.
2. La frase de la queja original («no puedo enviarte el PDF») desaparece con la rev. 2.
3. SU-10 pierde el cierre humano del domicilio en parte de las corridas con v12.

## Limitaciones

- `record_detected_intent` y `handoff_to_human` ausentes por construcción; sin camino WhatsApp real (automatización, safety, entrega del PDF).
- El log registra claves de input, no valores.

## Veredicto

Ronda focal **no aprobada en sandbox**: el comportamiento central depende de la tool y solo puede validarse en producción con línea controlada después de provisionar. No publicar v12 sin esa prueba.
