#!/usr/bin/env bash
# Build main manuscript + electronic supplementary material (ESM).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

bash scripts/sync_figures.sh

build_doc() {
  local doc="$1"
  echo "=== Building ${doc}.pdf ==="
  pdflatex -interaction=nonstopmode "${doc}.tex" || true
  bibtex "${doc}" 2>/dev/null || true
  pdflatex -interaction=nonstopmode "${doc}.tex" || true
  pdflatex -interaction=nonstopmode "${doc}.tex" || true
  echo "  -> ${doc}.pdf"
}

build_doc stillwell2026b_ecological_inference_structured_erm
build_doc stillwell2026b_ESM

echo ""
echo "Done."
echo "  Main: stillwell2026b_ecological_inference_structured_erm.pdf"
echo "  ESM:  stillwell2026b_ESM.pdf"
