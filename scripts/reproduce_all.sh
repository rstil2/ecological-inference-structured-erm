#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/simulation_lopo_confounding.py
python3 scripts/stator_figure2_composite.py
bash scripts/sync_figures.sh
bash scripts/build_submission.sh

echo "Reproduction complete."
