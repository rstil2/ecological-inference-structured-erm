# Ecological Inference Is Structured Empirical Risk Minimization

**R. Craig Stillwell** · Volume II of the ERM program  
**Companion to:** [Project 42 — *Natural Selection Is ERM*](../Project%2042%20-%20AI:ML/)

---

## Start here

| What | File |
|------|------|
| **Volume I ↔ II alignment** | [`VOLUME_I_II_ALIGNMENT.md`](VOLUME_I_II_ALIGNMENT.md) (compare to [`1.docx`](1.docx)) |
| **§2–3 proof drafts** | [`stillwell2026b_section2_3_proofs.md`](stillwell2026b_section2_3_proofs.md) |
| **§2 vignette tables (2007 LOPO)** | [`stillwell2026b_table_2007_lopo_vignette.md`](stillwell2026b_table_2007_lopo_vignette.md) |
| **LaTeX manuscript (draft PDF)** | [`stillwell2026b_ecological_inference_structured_erm.pdf`](stillwell2026b_ecological_inference_structured_erm.pdf) |
| **LaTeX source** | [`stillwell2026b_ecological_inference_structured_erm.tex`](stillwell2026b_ecological_inference_structured_erm.tex) |
| **Simulation (§3)** | [`scripts/simulation_lopo_confounding.py`](scripts/simulation_lopo_confounding.py), [`SIMULATION_RESULTS.md`](SIMULATION_RESULTS.md) |
| **Bibliography (BibTeX + map)** | [`stillwell2026b.bib`](stillwell2026b.bib), [`stillwell2026b_bibliography.md`](stillwell2026b_bibliography.md) |
| **Venue / submission** | [`VENUE_DECISION.md`](VENUE_DECISION.md), [`stillwell2026b_coverletter_interface.md`](stillwell2026b_coverletter_interface.md) |
| Volume I (evolution / temporal ERM) | [Project 42](../Project%2042%20-%20AI:ML/) |
| LOPO methods companion (empirical) | [Project 50](../Project%2050%20-%20Ecology:AI/) |

---

## Program role

Project 55 is the **home for Volume II** — ecology / spatial generalization in the two-volume ERM theory program.

| Volume | Project | Axis | Question |
|--------|---------|------|----------|
| I — *Natural selection is ERM* | 42 | Time | When does a population learn reliably? |
| **II — *Ecological inference is structured ERM*** | **55** | Space | When does an ecological model generalize reliably? |

---

## Status (June 2026)

- [x] Detailed outline with 9 formal propositions
- [x] §2–3 proof drafts (P1–P4)
- [x] LOPO numbers table for §2 vignette (from Project 50)
- [x] Literature bib (~54 BibTeX keys + proposition map)
- [x] LaTeX scaffold restructured to match Volume I (`1.docx`): Results-first, Table 1, dual-audience intro (~8 pp draft)
- [x] Collinearity / LOPO simulation (ported from Project 50)
- [x] Venue decision: **Interface** (~5k words main + ESM; paired with Volume I)

---

## Submission

| | |
|--|--|
| **Primary venue** | *Journal of the Royal Society Interface* (Volume II companion) |
| **Volume I status** | PNAS rejected → **submitted to Interface** (Project 42) |
| **Strategy doc** | [`VENUE_DECISION.md`](VENUE_DECISION.md) |
| **Cover letter** | [`stillwell2026b_coverletter_interface.md`](stillwell2026b_coverletter_interface.md) |
| **Fallback** | *Ecological Monographs* |

---

## Compile

```bash
cd "Project 55 - Ecology:ML"
pdflatex stillwell2026b_ecological_inference_structured_erm.tex
bibtex stillwell2026b_ecological_inference_structured_erm
pdflatex stillwell2026b_ecological_inference_structured_erm.tex
pdflatex stillwell2026b_ecological_inference_structured_erm.tex
```
