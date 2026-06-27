# Ecological inference is structured empirical risk minimization

**R. Craig Stillwell** · Independent researcher

Code and manuscript source for *Ecological Inference Is Structured Empirical Risk Minimization: Generalization Across Space, Nested Units, and Niche Support* (Volume II of the ERM program; companion to [Volume I — natural selection is ERM](https://github.com/rstil2/selection-as-learning)).

**Target venue:** *Journal of the Royal Society Interface*

---

## Reproduce analyses

See [`REPRODUCE.md`](REPRODUCE.md). One command:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
bash scripts/reproduce_all.sh
```

This regenerates semi-synthetic simulation output (Figure 1), the *Stator limbatus* composite (Figure 2), syncs `figures/`, and builds main + ESM PDFs.

---

## Repository layout

| Path | Contents |
|------|----------|
| `scripts/simulation_lopo_confounding.py` | Semi-synthetic LOPO mismatch simulation (500 replicates) |
| `scripts/stator_figure2_composite.py` | Empirical vignette composite figure |
| `scripts/cv_common.py` | Shared CV utilities |
| `figures/` | PNGs embedded in the LaTeX manuscript |
| `outputs/` | Simulation tables and intermediate figures |
| `stillwell2026b_ecological_inference_structured_erm.tex` | Main manuscript |
| `stillwell2026b_ESM.tex` | Electronic supplementary material |
| `SIMULATION_RESULTS.md` | Simulation summary statistics |

---

## Citation

Stillwell RC (2026). Code for *Ecological Inference Is Structured Empirical Risk Minimization*. GitHub: https://github.com/rstil2/ecological-inference-structured-erm

A Zenodo DOI will be minted at publication.

---

## License

CC BY-NC 4.0 — see [selection-as-learning](https://github.com/rstil2/selection-as-learning) for the program license pattern.
