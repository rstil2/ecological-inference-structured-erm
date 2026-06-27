#!/usr/bin/env bash
# Build MEE ScholarOne submission bundle (docx main + title page + SI PDF + figures).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

SUB="$ROOT/submission"
FIG="$SUB/figures"
TEX="$SUB/tex/stillwell2026b_mee_main.tex"

echo "=== Sync figures ==="
bash scripts/sync_figures.sh
mkdir -p "$FIG"
cp -f figures/*.png "$FIG/"

echo "=== Build Supporting Information PDF ==="
bash scripts/build_submission.sh >/dev/null
cp -f stillwell2026b_ESM.pdf "$SUB/stillwell2026b_SupportingInformation.pdf"

echo "=== Generate MEE LaTeX (anonymous main text) ==="
python3 scripts/prepare_mee_tex.py

echo "=== Convert main manuscript to Word ==="
pandoc "$TEX" \
  --from=latex \
  --to=docx \
  --output="$SUB/stillwell2026b_main.docx" \
  --bibliography="$ROOT/stillwell2026b.bib" \
  --citeproc \
  --resource-path="$ROOT:$ROOT/figures:$FIG" \
  2>/dev/null || pandoc "$TEX" \
  --from=latex \
  --to=docx \
  --output="$SUB/stillwell2026b_main.docx" \
  --bibliography="$ROOT/stillwell2026b.bib" \
  --citeproc \
  --resource-path="$ROOT:$ROOT/figures:$FIG"

echo "=== Convert title page to Word ==="
pandoc "$SUB/stillwell2026b_title_page.md" \
  --to=docx \
  --output="$SUB/stillwell2026b_title_page.docx"

echo "=== Package checklist ==="
cat > "$SUB/README_UPLOAD.txt" <<'EOF'
MEE ScholarOne upload checklist
===============================

Main document (anonymous, for review):
  stillwell2026b_main.docx

Title page (Supplemental Document — NOT for review):
  stillwell2026b_title_page.docx

Supporting Information:
  stillwell2026b_SupportingInformation.pdf

Figures (if not embedded in docx — upload separately if portal requires):
  figures/fig1_simulation_lopo_mismatch_rates.png
  figures/fig2_stator_empirical_summary_composite.png

Before upload — open stillwell2026b_main.docx and verify:
  [ ] Double line spacing (Home → Line spacing → 2.0)
  [ ] Continuous line numbers (Layout → Line Numbers → Continuous)
  [ ] Equations and citations rendered correctly
  [ ] Figures 1–2 visible; re-insert from submission/figures/ if missing
  [ ] No author name in main text (double-anonymous)
  [ ] Abstract numbered 1–4
  [ ] Section order: Introduction → Materials and Methods → Results → Discussion

Portal: https://mc.manuscriptcentral.com/mee-besjournals
EOF

echo ""
echo "Done. Submission files in: $SUB/"
ls -la "$SUB"/*.docx "$SUB"/*.pdf "$SUB"/*.txt 2>/dev/null || true
