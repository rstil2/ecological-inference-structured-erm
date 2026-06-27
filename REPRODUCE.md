# Reproducing Volume II analyses

Repository for *Ecological Inference Is Structured Empirical Risk Minimization* (Stillwell, 2026).

## Requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## One-command rebuild

```bash
bash scripts/reproduce_all.sh
```

This runs simulation, Figure 2 composite, figure sync, and PDF build.

## Individual steps

| Step | Command | Output |
|------|---------|--------|
| Semi-synthetic simulation (500 reps) | `python scripts/simulation_lopo_confounding.py` | `outputs/tables/simulation_lopo_mismatch.json`, Fig. 1 PNG |
| *Stator* composite figure | `python scripts/stator_figure2_composite.py` | Fig. 2 PNG |
| Sync figures for LaTeX | `bash scripts/sync_figures.sh` | `figures/*.png` |
| PDFs | `bash scripts/build_submission.sh` | Main + ESM PDFs |

## Empirical data

*Stator limbatus* population means and covariates are from Stillwell et al. (2007, *Am. Nat.*). LOPO reanalysis uses published summary statistics and population-level tables embedded in `scripts/stator_figure2_composite.py` and ESM Tables S1–S4 (from Project 50 workflow).

## Citation

On public release, assign a Zenodo DOI and cite in Methods as:

> Stillwell RC (2026). Code for *Ecological Inference Is Structured Empirical Risk Minimization*. Zenodo. \<DOI\>

## Pre-submission checklist

- [x] Push to public GitHub
- [ ] Mint Zenodo archive from release tag
- [ ] Update `\repoUrl` in manuscript Methods
