# Volume I ↔ Volume II alignment check

**Volume I source:** `1.docx` (*Natural selection is empirical risk minimisation*) — foundational theory paper at Interface  
**Volume II WIP:** Project 55 outline + `stillwell2026b_ecological_inference_structured_erm.tex`

---

## Verdict: **Same track, not yet same altitude**

Volume II is the correct spatial complement to Volume I. The mathematical program (ERM on a shared geometry, different coordinates) is consistent. What still differs is **significance framing, table architecture, and empirical centerpiece** — the things that make `1.docx` work as an Interface paper.

---

## What Volume I actually does (from `1.docx`)

| Element | Volume I pattern |
|---------|------------------|
| **Opening hook** | Concrete stakes first — cancer resistance, not “learning theory” |
| **One-line thesis** | ERM on Fisher-information manifold under capacity constraint |
| **Dual audience** | Explicit paragraphs for evolution readers vs ML readers |
| **Prior-work gap** | Valiant evolvability → missing measurable \(V_A, N_e, h^2\) |
| **Core artifact** | **Table 1** — full evo ↔ ML correspondence (genotype↔hypothesis, \(N_e\)↔\(n\), etc.) |
| **Formal results** | **4 theorems** + lemmas/corollaries; proof sketches in main, full proofs in Supplementary Notes |
| **Empirical punchline** | Cross-cancer \(r = 0.96\) for PAC bound vs resistance durability (Figure 3) |
| **Computability claim** | \(N_e^\*\) threshold from data already in clinical pipelines |
| **Discussion** | Clinical implication → meaning for each field → scope/limits → open problems |
| **Structure** | Abstract → Intro → **Results** (not “Theory section 2…”) → Discussion → Methods |

---

## What Volume II does today

| Element | Volume II status | Aligned? |
|---------|------------------|----------|
| **Opening hook** | Theory-first abstract (“Volume I established…”) | ⚠️ Needs ecological stakes hook |
| **One-line thesis** | Structured ERM across space / nested units / niche support | ✅ |
| **Dual audience** | Mentioned in outline; not in `.tex` intro | ⚠️ Add like Vol I |
| **Prior-work gap** | Scattered cites (Roberts CV, Araújo SDM); no single “X left open” paragraph | ⚠️ Sharpen |
| **Core artifact** | Bridge table in §7 only; **no Vol I-style Table 1** in main text | ❌ Add early |
| **Formal results** | 9 propositions P1–P9; appendix proofs started | ✅ (consider “Theorem” naming for Interface parity) |
| **Empirical punchline** | 84% sim rank-reversal + *Stator* LOPO table | ⚠️ Good illustration, not yet flagship validation |
| **Computability claim** | “Use LOPO not individual k-fold” — right but soft vs \(N_e^\*\) | ⚠️ Sharpen to one operational rule |
| **Discussion** | Short; missing clinical/ecological policy implication block | ⚠️ Expand |
| **Structure** | Theory sections first; sim/vignette late | ⚠️ Reframe as **Results** like Vol I |

---

## Coordinate transform (the program is consistent)

| | **Volume I (`1.docx`)** | **Volume II (Project 55)** |
|--|-------------------------|----------------------------|
| **Question** | When does a population *learn* (adapt)? | When does a model *generalize* across sites? |
| **Axis** | Generations / time | Geography / space |
| **Core object** | Genotype → phenotype → fitness | Environment → trait / distribution |
| **Capacity** | \(V_A\), **G**, \(N_e\) | Niche support, collinearity, hidden context |
| **Failure modes** | Drift, overcapacity, negative transfer | Wrong CV unit, proxy traps, label noise |
| **ML objects** | PAC, Rademacher, natural gradient | Group CV, domain shift, OOD, IRM |
| **Empirical anchor** | 9 cancer types | Sim + *Stator* (+ literature SDM cites) |

**Single sentence (both volumes):** Same ERM backbone — Volume I = **update** reliability; Volume II = **transfer** reliability.

---

## Recommended adjustments so Volume II “feels like” `1.docx`

### 1. Reframe the abstract (significance first)

**Volume I opens:** drug resistance is predictable from \(V_A\) and \(N_e\).  
**Volume II should open:** geographic/climate prediction fails routinely because ecologists optimize the wrong risk functional — then introduce structured ERM.

Example lead: macroecological models rank latitude/temperature in-sample but fail at new sites (cite Ploton et al. 2020; your LOPO result).

### 2. Add **Table 1: Ecological inference ↔ ML** (early, in Results)

Mirror Vol I’s correspondence table. Draft rows:

| Ecology | ML |
|---------|-----|
| Population mean at site | Group-level target |
| Individual within site | i.i.d. sample |
| LOPO / block CV | Group / domain CV |
| Latitude on a cline | Spurious correlate / proxy feature |
| Grinnellian envelope | Training support |
| Realized niche / biotic context | Hidden variable / label shift |
| Field cline slope | Composite label (genetic + plastic) |
| Common garden | Correct target / deconfounded supervision |
| Manipulative interaction test | Required interaction for mechanism |

### 3. Restructure sections to match Volume I

```
Abstract
Introduction  (hook + dual audience + contributions list)
Results
  The formal correspondence (Table 1)
  Theorem/Proposition block (compressed main text)
  Empirical validation (sim + vignette + 1 external literature anchor)
Discussion
Methods / ESM
```

Not: eight theory sections before any “result.”

### 4. One flagship quantitative claim

Volume I has \(r = 0.96\). Volume II needs one equally crisp headline, e.g.:

- “In 84% of semi-synthetic clines, strongest in-sample \(|r|\) mis-ranks models vs LOPO under known ecology-driven generating process”; **plus**
- “On *Stator* (93 populations), temperature-only LOPO RMSE 0.112 vs ecology 0.104 — proxy wins in-sample, loses on structured holdout.”

Package as **Figure 1 = sim, Figure 2 = vignette** (Vol I has multi-panel cancer figures).

### 5. Operational rule (Volume II’s \(N_e^\*\))

Volume I’s power is a **computable threshold**. Volume II equivalent:

> **Default rule:** If the scientific claim is prediction at a **new site/population**, the estimand is E₂ and holdout must be LOPO (or spatial block), not individual *k*-fold.

Make this a named corollary or boxed recommendation — the ecology field’s actionable output.

### 6. Dual-audience intro paragraphs (copy Vol I pattern)

- *For ecologists:* LOPO is the across-site generalization functional; in-sample \(R^2\) optimizes the wrong estimand.
- *For ML readers:* geographic surveys are domain-generalization problems with structured group structure; niche support is training-set support.

### 7. Prior-work gap paragraph

Volume I: “Valiant left open measurable \(V_A, N_e\)…”  
Volume II: “Spatial CV literature (Roberts et al.) prescribes holdout geometry but lacks a unified ERM/niche-support framework connecting clines, SDMs, and plasticity bias.”

---

## What **not** to change

- Nine propositions are the right granularity (ecology has more failure modes than temporal learning).
- *Stator* vignette is appropriate — Vol I also uses author-linked empirical threads; keep it short (~2–3 pages / one figure panel).
- Interface + ESM split matches where Volume I sits.
- Do **not** inflate into JMLR-length monograph.
- Do **not** make Project 50 JAE paper the core — methods companion only (already correct).

---

## Checklist: on same track?

| Criterion | Status |
|-----------|--------|
| Same ERM / Fisher backbone as Vol I | ✅ |
| Different axis (space vs time) | ✅ |
| Formal theorems/propositions | ✅ (draft) |
| Empirical validation section | ⚠️ needs Results framing |
| Table 1 correspondence | ❌ add |
| Significance-first abstract | ❌ rewrite |
| Computable/actionable output | ⚠️ sharpen LOPO default rule |
| Interface length + ESM proofs | ✅ planned |
| Matches `1.docx` rhetorical arc | ⚠️ restructure intro/Results |

**Bottom line:** Conceptually aligned. Restructured `.tex` (June 2026) follows `1.docx` rhetoric: significance abstract, Table 1, Results-first layout, dual-audience intro, operational corollary, expanded Discussion.

## Post-restructure status

| Element | Status |
|---------|--------|
| Significance-first abstract | ✅ |
| Dual-audience intro | ✅ |
| Table 1 correspondence | ✅ (`tab:correspondence`) |
| Results section | ✅ |
| Operational corollary (LOPO default) | ✅ |
| Empirical validation subsection | ✅ |
| Expanded Discussion | ✅ |
| Methods section | ✅ |
| Figure 2 composite | ✅ `outputs/figures/stator_empirical_summary_composite.png` |
| Media summary (Interface) | ✅ `stillwell2026b_media_summary.md` + § in `.tex` |
