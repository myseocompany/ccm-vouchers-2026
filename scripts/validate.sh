#!/usr/bin/env bash
# validate.sh — validador local no destructivo del harness ccm-vouchers-2026
# Uso: bash scripts/validate.sh
# No modifica archivos. Sale con código 1 si encuentra problemas críticos.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

errors=0
warnings=0

fail() { echo "  ERROR: $1"; errors=$((errors+1)); }
warn() { echo "  warn:  $1"; warnings=$((warnings+1)); }
ok()   { echo "  ok:    $1"; }

section() { echo; echo "== $1 =="; }

# ---------- 1. Archivos raíz obligatorios ----------
section "Archivos raíz"
for f in AGENTS.md SOUL.md PROGRAMA.md POLICIES.md SOURCES.md MEMORY.md TASKS.md DECISIONS.md README.md VOLUNTEER.en.md .gitignore; do
  [[ -f "$f" ]] && ok "$f existe" || fail "$f falta"
done

# ---------- 2. Carpetas obligatorias ----------
section "Carpetas obligatorias"
for d in clientes clientes/_template workflows templates entregables evidencias evals scripts; do
  [[ -d "$d" ]] && ok "$d/ existe" || fail "$d/ falta"
done

# ---------- 3. Template de cliente ----------
section "Template de cliente"
for f in CLIENTE.md CARACTERIZACION.md TASKS.md PROGRESS.md INFORME.md; do
  [[ -f "clientes/_template/$f" ]] && ok "_template/$f existe" || fail "_template/$f falta"
done

# ---------- 4. Los 10 clientes esperados ----------
section "10 clientes esperados"
expected_clients=(la-megachuleta la-patateria manuelina friends-chicken-cable arepas-rellenas-samu pizzas-beto el-efecto-barbacoa trattorias-y-pastificios cheesecake-pizza-milan indecente)
for c in "${expected_clients[@]}"; do
  if [[ -d "clientes/$c" ]]; then
    ok "cliente $c"
    for f in CLIENTE.md CARACTERIZACION.md TASKS.md PROGRESS.md INFORME.md; do
      [[ ! -f "clientes/$c/$f" ]] && fail "clientes/$c/$f falta"
    done
  else
    fail "clientes/$c/ falta"
  fi
done

# ---------- 5. Workflows y templates ----------
section "Workflows"
for w in 01_caracterizacion 02_config_tenant 03_vertical_restaurantes 04_ia_conversacional 05_capacitacion 06_activacion 07_soporte_sla 08_informes; do
  [[ -f "workflows/$w.md" ]] && ok "workflow $w" || fail "workflows/$w.md falta"
done

section "Templates"
for t in INFORME_ESTABLECIMIENTO INFORME_FINAL ACTA_CAPACITACION DASHBOARD_METRICAS; do
  [[ -f "templates/$t.md" ]] && ok "template $t" || fail "templates/$t.md falta"
done

# ---------- 6. Referencias a archivos .md rotas ----------
section "Referencias a archivos .md"
# Extrae de cada archivo las rutas tipo `foo.md` o `path/foo.md` y verifica que existan relativas al archivo origen.
broken=0
while IFS= read -r -d '' src; do
  # ignora líneas de bloque de código (línea completa entre backticks es OK) — simplificación
  refs=$(grep -oE '`[^`]+\.md`' "$src" 2>/dev/null | sed 's/`//g' | sort -u || true)
  src_dir="$(dirname "$src")"
  while IFS= read -r ref; do
    [[ -z "$ref" ]] && continue
    # ignora placeholders con < >
    [[ "$ref" == *"<"* || "$ref" == *">"* ]] && continue
    # resuelve ruta relativa al archivo origen
    target="$src_dir/$ref"
    # normaliza con python (siempre disponible en macOS)
    resolved="$(python3 -c "import os,sys; print(os.path.normpath(sys.argv[1]))" "$target" 2>/dev/null)"
    if [[ ! -e "$resolved" ]]; then
      warn "referencia rota: $src -> $ref (resuelta: $resolved)"
      broken=$((broken+1))
    fi
  done <<< "$refs"
done < <(find . -type f -name '*.md' -not -path './.git/*' -print0)
[[ $broken -eq 0 ]] && ok "sin referencias rotas"

# ---------- 7. Campos básicos y evidencia de tareas completas ----------
section "Registros y evidencia"
records_output=$(python3 "$ROOT/scripts/validate_records.py" "$ROOT")
records_status=$?
echo "$records_output"
record_warnings=$(printf '%s\n' "$records_output" | grep -c '^  warn:' || true)
warnings=$((warnings + record_warnings))
if [[ $records_status -ne 0 ]]; then
  fail "registros inválidos; ver errores anteriores"
fi

# ---------- Resumen ----------
section "Resumen"
echo "errores críticos: $errors"
echo "advertencias:     $warnings"
[[ $errors -gt 0 ]] && exit 1
exit 0
