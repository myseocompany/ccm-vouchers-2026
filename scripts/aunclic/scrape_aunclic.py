#!/usr/bin/env python3
"""
Scraper del marketplace "A un Clic" (Cámara de Comercio de Manizales por Caldas).

Extrae todos los productos de una categoría (por defecto Alimentos y Bebidas,
category_id=1) recorriendo la paginación del API público, y con eso arma una
base de datos de las empresas vendedoras: NIT, dirección, contacto, teléfono,
WhatsApp, email, geolocalización, etc.

API descubiertos:
  - GET https://api.aunclic.com.co/api/v1/products?category_id=<id>&page=N
    (paginador Laravel: last_page, data[]; per_page fijado por servidor en 9)
  - GET https://api.aunclic.com.co/api/v1/business/<business_id>
    (registro completo de la empresa, incluye shops con contacto)

Rate limit del API: 60 requests/minuto (headers x-ratelimit-*). El scraper
se auto-ajusta con esos headers y ante HTTP 429 espera 65s. Todo queda en
caché (cache/) para poder reanudar sin repetir requests.

Salidas (en --outdir, por defecto junto a este script):
  - productos_alimentos_y_bebidas.csv   (una fila por producto)
  - empresas_alimentos_y_bebidas.csv    (una fila por empresa única)
  - cache/*.json                        (respuestas crudas por página/empresa)

Uso:
  python3 scrape_aunclic.py                # categoría 1 (Alimentos y Bebidas)
  python3 scrape_aunclic.py --categoria 44 # otra categoría
"""

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.aunclic.com.co/api/v1"
SITE = "https://aunclic.com.co"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
}
RITMO = 1.1          # segundos entre requests (≈54/min, bajo el límite de 60)
RESERVA = 5          # si x-ratelimit-remaining baja de esto, pausa extra
SLUGS = {1: "alimentos_y_bebidas"}


class Cliente:
    """GET JSON con rate-limiting adaptativo y reintentos ante 429/errores."""

    def __init__(self, cachedir):
        self.cachedir = cachedir
        cachedir.mkdir(parents=True, exist_ok=True)

    def _get_http(self, url):
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            cuerpo = r.read().decode("utf-8")
            remaining = r.headers.get("x-ratelimit-remaining")
            return json.loads(cuerpo), (int(remaining) if remaining else None)

    def get(self, url, cache_path=None):
        """Devuelve JSON; usa caché en disco si existe (reanudación)."""
        if cache_path and cache_path.exists():
            return json.loads(cache_path.read_text(encoding="utf-8"))
        espera_429 = 65
        while True:
            try:
                data, remaining = self._get_http(url)
                if cache_path:
                    cache_path.write_text(
                        json.dumps(data, ensure_ascii=False), encoding="utf-8")
                # pausa proactiva si el budget del minuto anda justo
                pausa = RITMO
                if remaining is not None and remaining < RESERVA:
                    pausa = max(pausa, 15)
                time.sleep(pausa)
                return data
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(f"  · 429 Too Many Requests: espero {espera_429}s…", flush=True)
                    time.sleep(espera_429)
                    espera_429 = min(espera_429 * 2, 300)
                    continue
                raise
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
                print(f"  ! error {e}; reintento en 5s", flush=True)
                time.sleep(5)


def limpio(v):
    """El API serializa vacíos como string 'null'; normalizar a ''."""
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() == "null" else s


def precios_variaciones(producto):
    """(precio_min, precio_max) entre variaciones con precio > 0."""
    precios = [float(v["price"]) for v in producto.get("variations") or []
               if v.get("price") and float(v["price"]) > 0]
    return (min(precios), max(precios)) if precios else ("", "")


def recorrer_productos(cliente, category_id):
    productos = []
    pagina = 1
    while True:
        data = cliente.get(
            f"{API}/products?category_id={category_id}&page={pagina}",
            cache_path=cliente.cachedir / f"cat{category_id}_pagina{pagina:04d}.json")
        lote = data.get("data") or []
        productos.extend(lote)
        ultima = data.get("last_page", "?")
        print(f"  página {pagina}/{ultima}: +{len(lote)} (acumulado {len(productos)})"
              f" de {data.get('total', '?')}", flush=True)
        if not lote or pagina >= (data.get("last_page") or pagina):
            break
        pagina += 1
    return productos


def fila_producto(p):
    pmin, pmax = precios_variaciones(p)
    return {
        "producto_id": p.get("id"),
        "producto": limpio(p.get("name")),
        "marca": limpio(p.get("brand")),
        "categoria": limpio(p.get("category_name")),
        "categoria_id": p.get("category_id"),
        "empresa_id": p.get("business_id"),
        "empresa": limpio(p.get("business_name")),
        "precio_min": pmin,
        "precio_max": pmax,
        "num_variaciones": len(p.get("variations") or []),
        "estado": p.get("status"),
        "publicado": limpio(p.get("created_at")),
        "url": f"{SITE}/product/{p.get('id')}",
    }


def fila_empresa(b, n_productos):
    shops = b.get("shops") or []
    # el contacto completo vive en "shop" (sucursal principal detallada);
    # "shops" solo trae nombre/dirección/coordenadas
    shop = b.get("shop") or next(
        (s for s in shops if s.get("is_principal")), shops[0] if shops else {})
    return {
        "empresa_id": b.get("id"),
        "nit": limpio(b.get("nit")),
        "nombre": limpio(b.get("name")),
        "descripcion": limpio(b.get("description")),
        "palabras_clave": limpio(b.get("keywords")),
        "categorias": limpio(b.get("categories")),
        "direccion": limpio(shop.get("address")),
        "barrio": limpio(shop.get("neighborhood_name")),
        "ciudad": limpio(shop.get("city_name")),
        "departamento": limpio(shop.get("department_name")),
        "latitud": limpio(shop.get("latitude")),
        "longitud": limpio(shop.get("longitude")),
        "persona_contacto": limpio(shop.get("person")),
        "telefono": limpio(shop.get("phone")),
        "whatsapp": limpio(shop.get("whatsapp")),
        "email": limpio(shop.get("email")),
        "sitio_web": limpio(shop.get("website")),
        "num_sucursales": len(shops),
        "num_productos_categoria": n_productos,
        "afiliado": b.get("is_affiliate"),
        "sector_id": b.get("sector_id"),
        "registrado_en": limpio(b.get("created_at")),
        "logo": limpio(b.get("url_image")),
    }


def escribir_csv(path, filas):
    if not filas:
        print(f"  ! sin filas para {path}")
        return
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f"  -> {path.name} ({len(filas)} filas)")


def main():
    ap = argparse.ArgumentParser(description="Scraper de empresas por categoría de aunclic.com.co")
    ap.add_argument("--categoria", type=int, default=1, help="category_id (1 = Alimentos y Bebidas)")
    ap.add_argument("--outdir", default=str(Path(__file__).parent), help="directorio de salida")
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    slug = SLUGS.get(args.categoria, f"categoria_{args.categoria}")
    cliente = Cliente(outdir / "cache")

    print(f"[1/3] Recorriendo paginación de productos (category_id={args.categoria})…", flush=True)
    productos = recorrer_productos(cliente, args.categoria)
    vistos, unicos = set(), []
    for p in productos:
        if p.get("id") not in vistos:
            vistos.add(p.get("id"))
            unicos.append(p)
    print(f"  total productos únicos: {len(unicos)}", flush=True)

    conteo = {}
    for p in unicos:
        conteo[p.get("business_id")] = conteo.get(p.get("business_id"), 0) + 1
    ids = sorted(b for b in conteo if b is not None)
    print(f"[2/3] Consultando detalle de {len(ids)} empresas únicas…", flush=True)

    negocios, fallidos = {}, []
    for i, bid in enumerate(ids, 1):
        try:
            negocios[bid] = cliente.get(
                f"{API}/business/{bid}",
                cache_path=cliente.cachedir / f"empresa_{bid}.json")
        except Exception as e:
            fallidos.append(bid)
            print(f"  ! empresa {bid}: {e}", flush=True)
        if i % 50 == 0 or i == len(ids):
            print(f"  avance empresas: {i}/{len(ids)}", flush=True)

    print(f"[3/3] Escribiendo salidas en {outdir}…", flush=True)
    escribir_csv(outdir / f"productos_{slug}.csv", [fila_producto(p) for p in unicos])
    escribir_csv(outdir / f"empresas_{slug}.csv",
                 [fila_empresa(negocios[b], conteo[b]) for b in ids if b in negocios])

    if fallidos:
        print(f"  ! {len(fallidos)} empresas sin detalle por errores: {fallidos}")
        sys.exit(1)
    print("Listo.")


if __name__ == "__main__":
    main()
