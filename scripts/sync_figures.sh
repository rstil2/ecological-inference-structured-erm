#!/usr/bin/env bash
# Copy canonical figure assets into figures/ for LaTeX (embedded submission bundle).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/outputs/figures"
DST="$ROOT/figures"

mkdir -p "$DST"

copy_if() {
  local src_name="$1"
  local dst_name="$2"
  if [[ -f "$SRC/$src_name" ]]; then
    cp -f "$SRC/$src_name" "$DST/$dst_name"
  fi
}

copy_if simulation_lopo_mismatch_rates.png fig1_simulation_lopo_mismatch_rates.png
copy_if stator_empirical_summary_composite.png fig2_stator_empirical_summary_composite.png
copy_if simulation_aic_vs_lopo_example.png fig_esm_simulation_aic_vs_lopo_example.png

echo "Synced figures/ ($(ls -1 "$DST"/*.png 2>/dev/null | wc -l | tr -d ' ') files)"
