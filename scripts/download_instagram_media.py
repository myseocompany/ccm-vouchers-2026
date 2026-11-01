#!/usr/bin/env python3
"""Descarga los medios (imágenes/videos) de datasets de Instagram scrapeados con Apify.

Espera encontrar posts.json y reels.json (salida del actor apify/instagram-scraper)
en la carpeta indicada y baja los archivos a media/, deduplicando por shortCode.

Uso:
    python3 scripts/download_instagram_media.py clientes/<cliente>/instagram
"""

import json
import sys
import time
from pathlib import Path

import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
}

EXT_BY_MIME = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "video/mp4": ".mp4",
    "video/quicktime": ".mov",
}


def collect_downloads(items, seen):
    """Devuelve lista de (url, ruta_relativa) para un item del dataset."""
    downloads = []
    for it in items:
        sc = it.get("shortCode")
        if not sc or sc in seen:
            continue
        seen.add(sc)
        is_video = bool(it.get("videoUrl"))

        # Video principal
        if is_video:
            downloads.append((it["videoUrl"], f"{sc}.mp4"))
            if it.get("displayUrl"):
                downloads.append((it["displayUrl"], f"{sc}_thumb.jpg"))
        # Imagen única
        elif it.get("displayUrl"):
            downloads.append((it["displayUrl"], f"{sc}.jpg"))

        # Hijos de carrusel
        for i, child in enumerate(it.get("childPosts") or [], start=1):
            if child.get("videoUrl"):
                downloads.append((child["videoUrl"], f"{sc}_{i}.mp4"))
            elif child.get("displayUrl"):
                downloads.append((child["displayUrl"], f"{sc}_{i}.jpg"))
    return downloads


def download(url, dest: Path, retries=3):
    if dest.exists() and dest.stat().st_size > 0:
        return "skip"
    for attempt in range(1, retries + 1):
        try:
            with requests.get(url, headers=HEADERS, stream=True, timeout=60) as r:
                r.raise_for_status()
                ctype = r.headers.get("Content-Type", "").split(";")[0].strip()
                final = dest.with_suffix(EXT_BY_MIME.get(ctype, dest.suffix))
                tmp = final.with_suffix(final.suffix + ".part")
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1 << 16):
                        f.write(chunk)
                tmp.rename(final)
                return "ok"
        except Exception as e:  # noqa: BLE001
            if attempt == retries:
                return f"error: {e}"
            time.sleep(2 * attempt)
    return "error"


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    folder = Path(sys.argv[1])
    media_dir = folder / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    seen = set()
    downloads = []
    for name in ("posts.json", "reels.json"):
        src = folder / name
        if not src.exists():
            print(f"AVISO: no existe {src}, se omite")
            continue
        with open(src) as f:
            items = json.load(f)
        got = collect_downloads(items, seen)
        print(f"{name}: {len(items)} items -> {len(got)} archivos (nuevos: {len(set(d[1] for d in got))})")
        downloads.extend(got)

    ok = skip = err = 0
    errors = []
    for i, (url, rel) in enumerate(downloads, start=1):
        status = download(url, media_dir / rel)
        if status == "ok":
            ok += 1
        elif status == "skip":
            skip += 1
        else:
            err += 1
            errors.append((rel, status))
        if i % 10 == 0 or i == len(downloads):
            print(f"  progreso: {i}/{len(downloads)} (ok={ok} skip={skip} error={err})")

    manifest = {
        "total_descargas": len(downloads),
        "ok": ok,
        "skip": skip,
        "error": err,
        "archivos": [{"archivo": rel, "url": url} for url, rel in downloads],
    }
    with open(media_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nListo: {ok} descargados, {skip} ya existían, {err} errores")
    for rel, status in errors:
        print(f"  ERROR {rel}: {status}")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
