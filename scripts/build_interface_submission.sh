#!/usr/bin/env bash
# Interface ScholarOne bundle: .docx main (required by portal) + ESM PDF + figures.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

SUB="$ROOT/submission/interface"
TEX="$SUB/tex/stillwell2026b_interface_main.tex"
MAIN=stillwell2026b_ecological_inference_structured_erm
ESM=stillwell2026b_ESM

echo "=== Sync figures & build PDFs (reference + ESM) ==="
bash scripts/sync_figures.sh
bash scripts/build_submission.sh

mkdir -p "$SUB/figures" "$SUB/source" "$SUB/tex"

echo "=== Generate pandoc LaTeX ==="
python3 scripts/prepare_interface_tex.py

echo "=== Convert main manuscript to Word (.docx) ==="
pandoc "$TEX" \
  --from=latex \
  --to=docx \
  --output="$SUB/${MAIN}.docx" \
  --bibliography="$ROOT/stillwell2026b.bib" \
  --citeproc \
  --resource-path="$ROOT:$ROOT/figures:$SUB/figures"

echo "=== Copy supplementary files ==="
cp -f figures/*.png "$SUB/figures/"
cp -f "${MAIN}.pdf" "$SUB/${MAIN}.pdf"
cp -f "${ESM}.pdf" "$SUB/${ESM}.pdf"
cp -f "${MAIN}.tex" "$SUB/source/"
cp -f "${ESM}.tex" "$SUB/source/"
cp -f interface_submission.sty "$SUB/source/"
cp -f stillwell2026b.bib "$SUB/source/"
cp -f REPRODUCE.md "$SUB/source/"
cp -f stillwell2026b_coverletter_interface.md "$SUB/cover_letter.md"
cp -f stillwell2026b_media_summary.md "$SUB/media_summary.md"
cp -f "$TEX" "$SUB/source/stillwell2026b_interface_main.tex"

cat > "$SUB/README_UPLOAD.txt" <<'EOF'
Journal of the Royal Society Interface — ScholarOne upload
==========================================================

Portal: https://mc.manuscriptcentral.com/rsif

REQUIRED BY PORTAL (docx)
  stillwell2026b_ecological_inference_structured_erm.docx  ← MAIN upload
  (Identical copy: stillwell2026b_ecological_inference_structured_erm_THIS_IS_IT.docx)

DO NOT upload an older build. Rebuild before every submission:
  bash scripts/build_interface_submission.sh
  Verify Methods + Acknowledgments contain:
  https://github.com/rstil2/ecological-inference-structured-erm

ELECTRONIC SUPPLEMENTARY MATERIAL
  stillwell2026b_ESM.pdf

FIGURES (upload separately if docx embed fails)
  figures/fig1_simulation_lopo_mismatch_rates.png
  figures/fig2_stator_empirical_summary_composite.png

COVER LETTER
  cover_letter.md

MEDIA SUMMARY (≤100 words; also required at final-files stage)
  media_summary.md  (included in main docx as §Media summary)

After opening the .docx — REQUIRED manual formatting:
  [ ] Select All → Line spacing → Double (2.0)
  [ ] Layout → Line Numbers → Continuous
  [ ] Verify Figures 1–2 appear; if missing, Insert → Pictures from figures/
  [ ] Verify equations and references rendered (regenerate docx if not)
  [ ] Confirm abstract has NO numbered references (Interface rule)

Reference PDF (your eyes only — do not upload if portal rejects PDF):
  stillwell2026b_ecological_inference_structured_erm.pdf

Data/code (ScholarOne form + Methods):
  https://github.com/rstil2/ecological-inference-structured-erm

Rebuild:
  bash scripts/build_interface_submission.sh
EOF

echo ""
echo "Done."
echo "  UPLOAD THIS: $SUB/${MAIN}.docx"
echo "  ESM:         $SUB/${ESM}.pdf"
ls -lh "$SUB/${MAIN}.docx" "$SUB/${ESM}.pdf"
