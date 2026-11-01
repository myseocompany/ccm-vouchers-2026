#!/usr/bin/env python3
"""Análisis de conversaciones exportadas de AriCRM/Waterfall para un establecimiento.

Evalúa tres cosas sobre el JSON de exportación (conversations + messages):

1. Oportunidades perdidas por no contestar a tiempo (heurística multicapa:
   silencio total, turnos del cliente sin respuesta humana, atención tardía).
2. Tiempo hasta la primera respuesta HUMANA por conversación, descontando las
   respuestas automáticas (detectadas por contenido: autorrespuesta y mensaje
   de ausencia; el export no marca `is_automated`).
3. Qué elementos debería aclarar el menú: extracción y categorización de las
   preguntas de los clientes, cruzadas contra lo que hoy cubren la
   autorrespuesta y la carta.

Privacidad: los reportes usan identificadores anónimos (conv-NNN) y los textos
de clientes pasan por un redactor de teléfonos/correos/direcciones. Los
archivos de detalle y el listado completo de preguntas se escriben en un
directorio LOCAL (por defecto junto al JSON, bajo `raw/`, excluido de git);
solo el reporte agregado indicado con --reporte-md es apto para versionarse.

Uso:
    python3 scripts/analisis_conversaciones.py \
        evidencias/<cliente>/conversaciones/raw/<export>.json \
        --cliente "Beto's Pizza" \
        --reporte-md evidencias/<cliente>/conversaciones/analisis-<fecha>.md
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from statistics import median

# ---------------------------------------------------------------------------
# Detección de respuestas automáticas (el export trae is_automated=false para
# todo, así que se detectan por contenido conocido de las plantillas).
AUTOMATIZADOS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"gracias por comunicarte con",   # autorrespuesta con tarifario
        r"no podemos responder",          # mensaje de ausencia
    ]
]


def es_automático(mensaje):
    cuerpo = mensaje.get("body") or ""
    return any(p.search(cuerpo) for p in AUTOMATIZADOS)


# ---------------------------------------------------------------------------
# Redacción de datos personales en textos de clientes.
REDACTAR = [
    (re.compile(r"(\+?57[\s\-]?)?\b3\d{2}[\s\-]?\d{3}[\s\-]?\d{4}\b"), "[tel]"),
    (re.compile(r"\b60\d[\s\-]?\d{3}[\s\-]?\d{3,4}\b"), "[tel]"),
    (re.compile(r"\S+@\S+\.\S+"), "[correo]"),
    (re.compile(
        r"(?i)\b(calle|carrera|cll|cra|cl|kr|av|avenida|transversal|tv|circunvalar|manzana|casa)\s*\.?\s*n?°?\s*\d+[^,;.\n]*"),
     "[dirección]"),
    (re.compile(r"\b\d{7,}\b"), "[número]"),
]


def redactar(texto, largo=200):
    texto = texto or ""
    for patron, reemplazo in REDACTAR:
        texto = patron.sub(reemplazo, texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto[:largo] + ("…" if len(texto) > largo else "")


# ---------------------------------------------------------------------------
# Categorización de preguntas (orden = precedencia). `auto` y `carta` indican
# si el contenido lo resuelve hoy la autorrespuesta o la carta, según el
# menú estructurado del cliente (menu-estructurado-carta-2026-10-05.md).
CATEGORIAS = [
    ("estado_pedido", "Estado del pedido (¿dónde va?, ¿ya salió?)",
     r"(?i)\b(ya sal(ió|io)|va en camino|d(ó|o)nde (est(á|a)|va).*(pedido|domicili)|no (ha )?llegad|a(ú|u)n no lleg|ya lleg|est(á|a) listo|mi pedido|est(á|a) demor)",
     False, False),
    ("tiempo_entrega", "Tiempo de entrega / demora",
     r"(?i)(cu(á|a)nto (tarda|se demora|demora)|tiempo de entrega|se demoran|tarda mucho|demora el domicilio|cu(á|a)nto tiempo)",
     False, False),
    ("cobertura", "Cobertura de domicilio / zonas",
     r"(?i)(hacen (el )?domicilio (a|hasta|en)|llegan (a|hasta)|domicilio (a|hasta) (el|la)?\s|hacen env(í|i)o|villamar(í|i)a|neira|la estrella|otro municipio|barrio)",
     False, False),
    ("domicilio_costo", "Costo del domicilio",
     r"(?i)(cu(á|a)nto (vale|es|cuesta|cobra).*(domicilio|env(í|i)o)|valor (del )?domicilio|domicilio.*(vale|cuesta|cu(á|a)nto))",
     True, False),
    ("horario", "Horario de atención",
     r"(?i)(horario|a qu(é|e) hora|abren|cierran|est(á|a)n abiert|atienden hasta|atienden ma(ñ|n)ana|domingo|festivo)",
     False, False),
    ("pago", "Métodos de pago",
     r"(?i)(nequi|bancolombia|davi?enda|transferencia|dat(á|a)fono|efectivo|contra ?entrega|tarjeta|pago digital|la llave)",
     False, False),
    ("tamanos", "Tamaños y porciones",
     r"(?i)(tama(ñ|n)o|porci(ó|o)n|cu(á|a)ntas porciones|small|personal|mediana|familiar|grande|peque(ñ|n)a)",
     True, True),
    ("sabores_disp", "Sabores, ingredientes y disponibilidad",
     r"(?i)(sabor|tienen de|hay de|disponib|se acab|no tienen|sin (queso|cebolla|carne|pi(ñ|n)a)|vegetarian|ingrediente|combinar|mitad)",
     True, True),
    ("precios", "Precios de productos",
     r"(?i)(cu(á|a)nto (vale|es|cuesta|cobran)|precio|valor de|cu(á|a)nto es)",
     True, True),
    ("ubicacion", "Ubicación de la sede / recogida",
     r"(?i)(d(ó|o)nde (est(á|a)n|queda)|direcci(ó|o)n|ubicad|recoger|paso (por|all))",
     False, False),
    ("menu", "Solicitud de menú/carta",
     r"(?i)(men(ú|u)|carta|cat(á|a)logo|qu(é|e) tienen)",
     True, True),
    ("factura", "Factura electrónica",
     r"(?i)(factura)",
     False, False),
    ("eventos", "Eventos / pedidos programados",
     r"(?i)(evento|programad|reserva|anticipad|ma(ñ|n)ana (a )?las)",
     False, False),
    ("promos", "Promociones y descuentos",
     r"(?i)(promoci(ó|o)n|promo|descuento|oferta|2x1|especial de)",
     False, False),
]


def categorizar(texto):
    for nombre, _, patron, _, _ in CATEGORIAS:
        if re.search(patron, texto):
            return nombre
    return "otro"


INTERROGATIVO = re.compile(
    r"(?i)^(qu(é|e)|cu(á|a)l|c(ó|o)mo|cu(á|a)ndo|d(ó|o)nde|cu(á|a)nto|por qu(é|e)|qui(é|e)n|tiene[n]?|hacen|puedo|se puede|hay)\b"
)

# Señal de intención de pedido real: datos de entrega, producto concreto o pago.
SENAL_PEDIDO = re.compile(
    r"(?i)(carrera|calle\s*\d|cll|cra\s*\d|\bbarrio\b|apto|torre| mans|"
    r"hawaiana|de carnes|napolitana|monta(ñ|n)era|vegetariana|suprema|champi(ñ|n)|tropical|"
    r"una? (familiar|mediana|small|personal|porci(ó|o)n|pizza|gaseosa|lasa(ñ|n)a|maicito|nachos)|"
    r"devuelta de|transferencia|nequi|bancolombia|dat(á|a)fono|el domicilio[, .]|mi pedido|el pedido)"
)

# Turno que solo contiene despedida/cortesía: no constituye oportunidad comercial.
SOLO_CORTESIA = re.compile(
    r"(?i)^[\s¡!.,]*(much(í|i)simas )?(gracias|chao|listo|perfecto|bendiciones|dale|"
    r"ok(ay)?|bueno|ya lleg(ó|o)|ya vamos|nos vemos|hasta luego)[\s,!¡.¿?]*$"
)


def es_pregunta(texto):
    return "?" in (texto or "") or bool(INTERROGATIVO.search(texto or ""))


# ---------------------------------------------------------------------------
# Ventana de atención: minutos transcurridos entre dos momentos contando solo
# horas dentro de la ventana diaria (por defecto 08:00–22:00, atención WhatsApp
# reportada por el establecimiento).
def min_atencion(t0, t1, abre, cierra):
    if t1 <= t0:
        return 0.0
    total = 0.0
    dia = t0.replace(hour=0, minute=0, second=0, microsecond=0)
    while dia <= t1:
        ini = dia.replace(hour=abre.hour, minute=abre.minute)
        fin = dia.replace(hour=cierra.hour, minute=cierra.minute)
        total += max(0.0, (min(t1, fin) - max(t0, ini)).total_seconds() / 60.0)
        dia += timedelta(days=1)
    return total


def percentil(valores, p):
    if not valores:
        return None
    orden = sorted(valores)
    k = (len(orden) - 1) * p / 100.0
    bajo, alto = int(k), min(int(k) + 1, len(orden) - 1)
    return orden[bajo] + (orden[alto] - orden[bajo]) * (k - bajo)


def fmt_min(m):
    if m is None:
        return "—"
    if m < 60:
        return f"{m:.0f} min"
    return f"{m/60:.1f} h"


# ---------------------------------------------------------------------------
# Etiquetado por conversación para auditoría: cada conversación del export
# recibe etiquetas estables que permiten filtrar casos a auditar (mismo
# método forense de conversaciones individuales).
DEFINICION_ETIQUETAS = {
    "silencio_total": "el cliente escribió y no hubo ninguna respuesta (ni automática)",
    "sin_toma_humana": "ningún humano respondió en todo el export",
    "solo_autorrespuesta": "solo respondió la autorrespuesta; ningún humano",
    "toma_rapida": "primera respuesta humana ≤ 5 min de atención",
    "toma_tardia": "primera respuesta humana > umbral de pérdida (default 60 min)",
    "turno_sin_respuesta": "≥1 turno del cliente quedó sin respuesta humana (no censurado)",
    "pedido_abandonado": "≥1 turno sin respuesta con pedido real en el texto",
    "actividad_nocturna": "≥1 turno entre las 22:00 y las 06:00",
    "censurada_reciente": "último turno dentro de las 24 h finales del export (observación incompleta)",
    "pregunta:<categoría>": "algún turno con pregunta de esa categoría (ver categorías)",
}


def etiquetar_conversaciones(resumen_conv, turnos, umbral_perdida):
    por_conv = defaultdict(list)
    for t in turnos:
        por_conv[t["conv"]].append(t)
    salida = {}
    for cid, r in resumen_conv.items():
        ts = sorted(por_conv.get(cid, []), key=lambda t: t["fin"])
        etiquetas, notas = set(), []
        if r["n_in"] > 0:
            if r["n_out"] == 0:
                etiquetas.add("silencio_total")
            if r["n_humano"] == 0:
                etiquetas.add("sin_toma_humana")
                if r["n_out"] > 0:
                    etiquetas.add("solo_autorrespuesta")
            elif r["toma_min"] is not None:
                if r["toma_min"] <= 5:
                    etiquetas.add("toma_rapida")
                elif r["toma_min"] > umbral_perdida:
                    etiquetas.add("toma_tardia")
            abandonados = [t for t in ts if not t["censurado"] and t["resp_humana"] is None]
            if abandonados:
                etiquetas.add("turno_sin_respuesta")
                pedidos = [t for t in abandonados if t["clase_abandono"] == "pedido"]
                if pedidos:
                    etiquetas.add("pedido_abandonado")
                notas.append(f"{len(abandonados)} turno(s) sin respuesta humana"
                             + (f", {len(pedidos)} con pedido real" if pedidos else ""))
            if any(t["fin"].hour >= 22 or t["fin"].hour < 6 for t in ts):
                etiquetas.add("actividad_nocturna")
            cats = Counter(categorizar(t["texto"]) for t in ts if es_pregunta(t["texto"]))
            for cat in cats:
                etiquetas.add(f"pregunta:{cat}")
            if cats:
                notas.append("preguntas: " + ", ".join(f"{c}×{n}" for c, n in cats.most_common(3)))
        if ts and ts[-1]["censurado"]:
            etiquetas.add("censurada_reciente")
        salida[cid] = {
            "etiquetas": sorted(etiquetas),
            "notas": "; ".join(notas),
            "turnos": len(ts),
            "mensajes_in": r["n_in"],
            "mensajes_out": r["n_out"],
            "respuestas_humanas": r["n_humano"],
            "toma_humana_min": round(r["toma_min"], 1) if r["toma_min"] is not None else None,
            "inicio": r["primer_in"].isoformat() if r["primer_in"] else None,
            "fin": max((t["fin"] for t in ts), default=None),
        }
    return salida


# ---------------------------------------------------------------------------
def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        data = json.load(f)
    conversaciones = {c["id"]: c for c in data["conversations"]}
    por_conv = defaultdict(list)
    for m in data["messages"]:
        m["_dt"] = datetime.fromisoformat(m["created_at"])
        m["_auto"] = es_automático(m) if m["direction"] == "out" else False
        por_conv[m["conversation_id"]].append(m)
    for ms in por_conv.values():
        ms.sort(key=lambda m: (m["_dt"], m["id"]))
    return data, conversaciones, por_conv


def analizar(por_conv, abre, cierra, umbral_tomo, umbral_perdida, fin_export):
    """Devuelve turnos y resúmenes por conversación."""
    resumen_conv, turnos = {}, []
    for cid, ms in por_conv.items():
        entrantes = [m for m in ms if m["direction"] == "in"]
        salientes = [m for m in ms if m["direction"] == "out"]
        humanos = [m for m in salientes if not m["_auto"]]

        primer_in = entrantes[0]["_dt"] if entrantes else None
        primer_out_cualq = salientes[0]["_dt"] if salientes else None
        primer_out_auto = next((m["_dt"] for m in salientes if m["_auto"]), None)
        primer_humano = None
        if primer_in is not None:
            primer_humano = next(
                (m["_dt"] for m in humanos if m["_dt"] >= primer_in - timedelta(seconds=2)), None)

        # Turnos: ráfagas máximas de mensajes entrantes sin un saliente entre medias.
        actual = []
        for m in ms:
            if m["direction"] == "in":
                actual.append(m)
            elif actual:
                turnos.append({"conv": cid, "mensajes": actual})
                actual = []
        if actual:
            turnos.append({"conv": cid, "mensajes": actual})

        resumen_conv[cid] = {
            "n_in": len(entrantes), "n_out": len(salientes),
            "n_humano": len(humanos), "n_auto": sum(1 for m in salientes if m["_auto"]),
            "primer_in": primer_in, "primer_humano": primer_humano,
            "primer_out_auto": primer_out_auto,
            "toma_min": (min_atencion(primer_in, primer_humano, abre, cierra)
                         if (primer_in and primer_humano) else None),
            "primer_out_cualq": primer_out_cualq,
        }

    for t in turnos:
        ms = t["mensajes"]
        t["inicio"] = ms[0]["_dt"]
        t["fin"] = ms[-1]["_dt"]
        t["solo_media"] = all(m.get("media_type") for m in ms)
        t["censurado"] = t["fin"] >= fin_export - timedelta(hours=24)
        resto = [m for m in por_conv[t["conv"]]
                 if m["direction"] == "out" and m["_dt"] >= t["fin"]]
        resp_humana = next((m for m in resto if not m["_auto"]), None)
        t["resp_humana"] = resp_humana["_dt"] if resp_humana else None
        t["hubo_auto_posterior"] = any(m["_auto"] for m in resto)
        t["latencia_min"] = (min_atencion(t["fin"], resp_humana["_dt"], abre, cierra)
                             if resp_humana else None)
        t["texto"] = " ".join(filter(None, (m.get("body") or "" for m in ms))).strip()
        t["senal_pedido"] = bool(SENAL_PEDIDO.search(t["texto"]))
        if t["senal_pedido"]:
            t["clase_abandono"] = "pedido"
        elif not t["texto"] or t["solo_media"] or SOLO_CORTESIA.match(t["texto"]):
            t["clase_abandono"] = "cortesia"
        else:
            t["clase_abandono"] = "otros"
    return resumen_conv, turnos


# ---------------------------------------------------------------------------
def generar_reporte(data, resumen_conv, turnos, args, fin_export, etiquetas=None):
    n_conv = len(resumen_conv)
    conv_con_in = {c: r for c, r in resumen_conv.items() if r["primer_in"]}
    conv_resp_humana = {c: r for c, r in conv_con_in.items() if r["primer_humano"]}
    conv_sin_humano = {c: r for c, r in conv_con_in.items() if not r["primer_humano"]}
    conv_silencio = {c: r for c, r in conv_con_in.items() if r["n_out"] == 0}
    conv_solo_auto = {c: r for c, r in conv_sin_humano.items() if r["n_out"] > 0}

    activos = [t for t in turnos if not t["censurado"]]
    abandonados = [t for t in activos if t["resp_humana"] is None]
    tardios = [t for t in activos if t["resp_humana"] is not None
               and t["latencia_min"] > args.umbral_perdida]
    moderados = [t for t in activos if t["resp_humana"] is not None
                 and args.umbral_tomo < t["latencia_min"] <= args.umbral_perdida]
    rapidos = [t for t in activos if t["resp_humana"] is not None
               and t["latencia_min"] <= args.umbral_tomo]

    tomas = [r["toma_min"] for r in conv_resp_humana.values()]
    conv_auto_primero = sum(
        1 for r in conv_resp_humana.values()
        if r["primer_out_auto"] and r["primer_out_auto"] <= r["primer_humano"])

    anon = {cid: f"conv-{i:03d}" for i, cid in enumerate(sorted(resumen_conv), 1)}

    lineas = []
    a = lineas.append
    a(f"# Análisis de conversaciones — {args.cliente}")
    a("")
    a(f"- **Fuente**: `{args.json}` (exportación Waterfall {data.get('exported_at_utc', '?')}), "
      f"{data['messages'].__len__()} mensajes de {n_conv} conversaciones.")
    a(f"- **Rango observado**: {min(t['inicio'] for t in turnos)} → {fin_export} "
      f"(timestamps en hora local del tenant, supuesto documentado).")
    a(f"- **Ventana de atención aplicada**: {args.abre:%H:%M}–{args.cierra:%H:%M} todos los días "
       "(atención WhatsApp reportada por el establecimiento); las esperas fuera de ventana "
       "no acumulan tiempo.")
    a(f"- **Respuesta automática descontada**: mensajes out que casan con las plantillas "
      "«Gracias por comunicarte…» (tarifario) y «En este momento no podemos responder…». "
      "El export marca `is_automated=false` en todos los out, por eso se detectan por contenido.")
    a("- **Privacidad**: identificadores anónimos; textos de clientes redactados. "
      "El detalle con IDs reales queda solo en el directorio local `raw/` (fuera de git).")
    a("- **Advertencia**: los umbrales de «oportunidad perdida» son heurística de análisis, "
      "no una confirmación comercial; una conversación puede retomarse días después.")
    a("")
    a("## 1. Oportunidades perdidas por no contestar a tiempo")
    a("")
    a(f"- Conversaciones con mensajes del cliente: **{len(conv_con_in)}** de {n_conv}.")
    a(f"- **Silencio total** (el cliente escribió y no hubo NINGUNA respuesta, ni automática): "
      f"**{len(conv_silencio)}** conversaciones.")
    a(f"- **Solo respondió la máquina** (hubo autorrespuesta pero ningún humano tomó la "
      f"conversación en todo el export): **{len(conv_solo_auto)}** conversaciones.")
    a(f"- Turnos del cliente (ráfagas de mensajes entrantes): **{len(turnos)}** totales; "
      f"{len(activos)} observados con ventana completa (se excluyen {len(turnos)-len(activos)} "
      "de las últimas 24 h del export por censura).")
    a(f"- **Turnos sin respuesta humana** en lo restante del export: **{len(abandonados)}** "
      f"({100*len(abandonados)/max(1,len(activos)):.0f}% de los observados). "
      "Clasificación de esos turnos:")
    con_pedido = [t for t in abandonados if t["clase_abandono"] == "pedido"]
    cortesia = [t for t in abandonados if t["clase_abandono"] == "cortesia"]
    otros = [t for t in abandonados if t["clase_abandono"] == "otros"]
    a(f"  - **Con pedido real en el texto** (dirección/barrio, sabor o tamaño concretos, "
      f"pago o pedido explícito): **{len(con_pedido)}** → **oportunidades comerciales probables**. "
      + ("" if not con_pedido else
         "Horario: " + ", ".join(
             f"{t['fin']:%H:%M} del {t['fin']:%d-%m}" for t in sorted(con_pedido, key=lambda x: x["fin"])) + "."))
    a(f"  - Solo despedida/cortesía o archivo sin texto (no son oportunidades): "
      f"**{len(cortesia)}**.")
    a(f"  - Saludos o consultas sin intención clara de pedido: **{len(otros)}**.")
    a(f"- **Turnos atendidos tarde** (primera respuesta humana > {args.umbral_perdida} min de "
      f"atención): **{len(tardios)}**.")
    a(f"- Turnos atendidos entre {args.umbral_tomo} y {args.umbral_perdida} min: **{len(moderados)}**; "
      f"atendidos ≤ {args.umbral_tomo} min: **{len(rapidos)}**.")
    convs_abandono = Counter(t["conv"] for t in abandonados)
    if convs_abandono:
        a("- Conversaciones con ≥1 turno sin respuesta humana: "
          + ", ".join(f"`{anon[c]}`×{n}" for c, n in convs_abandono.most_common(15))
          + ("…" if len(convs_abandono) > 15 else ""))
        horas = Counter(t["fin"].hour for t in abandonados)
        a("- Hora (local) de los turnos sin respuesta: "
          + ", ".join(f"{h:02d}:00→{n}" for h, n in sorted(horas.items())))
    a("")
    a("## 2. Tiempo hasta la primera respuesta humana")
    a("")
    a(f"- Conversaciones tomadas por un humano: **{len(conv_resp_humana)}** de "
      f"{len(conv_con_in)} con mensajes del cliente "
      f"({100*len(conv_resp_humana)/max(1,len(conv_con_in)):.0f}%).")
    a(f"- En **{conv_auto_primero}** de ellas la primera respuesta fue la autorrespuesta "
      "(ya descontada: se mide hasta el primer humano).")
    if tomas:
        a(f"- Mediana de toma: **{fmt_min(median(tomas))}** · p75 {fmt_min(percentil(tomas,75))} · "
          f"p90 {fmt_min(percentil(tomas,90))} · peor caso {fmt_min(max(tomas))}.")
        buckets = [
            ("≤ 1 min", lambda v: v <= 1), ("1–5 min", lambda v: 1 < v <= 5),
            ("5–15 min", lambda v: 5 < v <= 15), ("15–30 min", lambda v: 15 < v <= 30),
            ("30–60 min", lambda v: 30 < v <= 60), ("1–4 h", lambda v: 60 < v <= 240),
            ("> 4 h", lambda v: v > 240)]
        a("- Distribución del tiempo de toma (minutos de atención):")
        a("")
        a("| Rango | Conversaciones | % |")
        a("|---|---:|---:|")
        for etiqueta, cond in buckets:
            n = sum(1 for v in tomas if cond(v))
            a(f"| {etiqueta} | {n} | {100*n/len(tomas):.0f}% |")
    peores = sorted(conv_resp_humana.items(), key=lambda kv: -kv[1]["toma_min"])[:20]
    if peores:
        a("")
        a("Las 20 tomas más lentas (anónimas):")
        a("")
        a("| Conv | Primera toma humana |")
        a("|---|---:|")
        for cid, r in peores:
            a(f"| `{anon[cid]}` | {fmt_min(r['toma_min'])} |")
    a("")
    a(f"- Conversaciones donde NINGÚN humano respondió jamás: **{len(conv_sin_humano)}** "
      "(no entran a la distribución; ver sección 1).")
    a("")
    a("## 3. Qué debe aclarar el menú (preguntas de los clientes)")
    a("")
    preguntas = [t for t in turnos if es_pregunta(t["texto"])]
    por_cat = defaultdict(list)
    for t in preguntas:
        por_cat[categorizar(t["texto"])].append(t)
    a(f"- Mensajes entrantes analizados: {sum(r['n_in'] for r in resumen_conv.values())}; "
      f"turnos con pregunta explícita o implícita: **{len(preguntas)}**.")
    a("")
    a("| Tema | Preguntas | % | ¿Lo responde la autorrespuesta? | ¿Lo resuelve la carta? |")
    a("|---|---:|---:|---|---|")
    etiquetas_cat = {n: (e, au, ca) for n, e, _, au, ca in CATEGORIAS}
    etiquetas_cat["otro"] = ("Otras preguntas", False, False)
    orden = sorted(por_cat.items(), key=lambda kv: -len(kv[1]))
    for nombre, ts in orden:
        etiqueta, auto, carta = etiquetas_cat[nombre]
        a(f"| {etiqueta} | {len(ts)} | {100*len(ts)/max(1,len(preguntas)):.0f}% | "
          f"{'sí' if auto else '**no**'} | {'sí' if carta else '**no**'} |")
    a("")
    a("Ejemplos redactados por tema (máx. 3):")
    for nombre, ts in orden:
        if nombre == "otro":
            continue
        etiqueta = etiquetas_cat[nombre][0]
        a("")
        a(f"**{etiqueta}**")
        for t in ts[:3]:
            a(f"- «{redactar(t['texto'])}»")
    a("")
    a("## 4. Conversaciones etiquetadas para auditoría")
    a("")
    if etiquetas:
        conteo = Counter(e for v in etiquetas.values() for e in v["etiquetas"])
        a("Cada conversación del export quedó etiquetada en "
          "`raw/analisis/conversaciones-etiquetadas.json` (con IDs reales, solo local) para "
          "filtrar y escoger casos a auditar con el método forense por conversación. "
          "Distribución agregada:")
        a("")
        a("| Etiqueta | Conversaciones |")
        a("|---|---:|")
        for e, n in conteo.most_common():
            a(f"| `{e}` | {n} |")
        a("")
        a("Definiciones de las etiquetas en el propio JSON (`definicion_etiquetas`).")
    a("")
    a("---")
    a("_Generado por `scripts/analisis_conversaciones.py`; heurística e inferencias "
      "sujetas a validación con el establecimiento._")
    return "\n".join(lineas), por_cat, anon, preguntas


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("json", help="Ruta al JSON de exportación (conversations+messages)")
    ap.add_argument("--cliente", default="establecimiento", help="Nombre para el reporte")
    ap.add_argument("--abre", default="08:00", help="Hora local apertura atención (HH:MM)")
    ap.add_argument("--cierra", default="22:00", help="Hora local cierre atención (HH:MM)")
    ap.add_argument("--umbral-tomo", type=float, default=15,
                    help="Min de atención considerados 'a tiempo' (default 15)")
    ap.add_argument("--umbral-perdida", type=float, default=60,
                    help="Min de atención considerados 'atendido tarde' (default 60)")
    ap.add_argument("--out-dir", default=None,
                    help="Directorio local de salidas (default: <dir json>/analisis, bajo raw/)")
    ap.add_argument("--reporte-md", default=None,
                    help="Ruta del reporte agregado apto para git (opcional)")
    args = ap.parse_args()
    args.abre = datetime.strptime(args.abre, "%H:%M")
    args.cierra = datetime.strptime(args.cierra, "%H:%M")

    ruta = Path(args.json)
    data, conversaciones, por_conv = cargar(ruta)
    fin_export = max(m["_dt"] for m in data["messages"])
    resumen_conv, turnos = analizar(
        por_conv, args.abre, args.cierra, args.umbral_tomo, args.umbral_perdida, fin_export)

    etiquetas = etiquetar_conversaciones(resumen_conv, turnos, args.umbral_perdida)
    reporte, por_cat, anon, preguntas = generar_reporte(
        data, resumen_conv, turnos, args, fin_export, etiquetas=etiquetas)

    out_dir = Path(args.out_dir) if args.out_dir else ruta.parent / "analisis"
    out_dir.mkdir(parents=True, exist_ok=True)
    detalle = {
        "parametros": {k: str(v) for k, v in vars(args).items()},
        "mapa_anonimos": anon,
        "conversaciones": {
            anon[cid]: {k: (v.isoformat() if isinstance(v, datetime) else v)
                        for k, v in r.items()} for cid, r in resumen_conv.items()},
        "turnos": [
            {"conv": anon[t["conv"]], "inicio": t["inicio"].isoformat(),
             "fin": t["fin"].isoformat(),
             "resp_humana": t["resp_humana"].isoformat() if t["resp_humana"] else None,
             "latencia_min": round(t["latencia_min"], 1) if t["latencia_min"] is not None else None,
             "pregunta": es_pregunta(t["texto"]),
             "categoria_pregunta": categorizar(t["texto"]) if es_pregunta(t["texto"]) else None,
             "senal_pedido": t["senal_pedido"],
             "censurado": t["censurado"], "solo_media": t["solo_media"]}
            for t in turnos],
    }
    with open(out_dir / "detalle-analisis.json", "w", encoding="utf-8") as f:
        json.dump(detalle, f, ensure_ascii=False, indent=1)

    with open(out_dir / "conversaciones-etiquetadas.json", "w", encoding="utf-8") as f:
        json.dump({
            "generado_por": "scripts/analisis_conversaciones.py",
            "json_fuente": str(ruta),
            "definicion_etiquetas": DEFINICION_ETIQUETAS,
            "conversaciones": {
                anon[cid]: {**v, "conversation_id_real": cid}
                for cid, v in etiquetas.items()},
        }, f, ensure_ascii=False, indent=1, default=str)

    with open(out_dir / "preguntas-clientes-redactadas.md", "w", encoding="utf-8") as f:
        f.write(f"# Preguntas de clientes — {args.cliente} (redactadas)\n\n")
        f.write("Insumo local para análisis del menú. NO versionar en git.\n\n")
        etiquetas = {n: e for n, e, _, _, _ in CATEGORIAS}
        for nombre, ts in sorted(por_cat.items(), key=lambda kv: -len(kv[1])):
            f.write(f"\n## {etiquetas.get(nombre, 'Otras preguntas')} ({len(ts)})\n")
            for t in ts:
                f.write(f"- ({t['inicio'].isoformat()}) «{redactar(t['texto'], 300)}»\n")

    if args.reporte_md:
        Path(args.reporte_md).parent.mkdir(parents=True, exist_ok=True)
        Path(args.reporte_md).write_text(reporte + "\n", encoding="utf-8")
        print(f"reporte  → {args.reporte_md}")
    print(f"detalle  → {out_dir / 'detalle-analisis.json'}")
    print(f"etiquetas→ {out_dir / 'conversaciones-etiquetadas.json'}")
    print(f"preguntas→ {out_dir / 'preguntas-clientes-redactadas.md'}")


if __name__ == "__main__":
    sys.exit(main())
