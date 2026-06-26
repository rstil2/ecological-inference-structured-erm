# Volume II — Ecological Inference Is Structured Empirical Risk Minimization

**Working title:** *Ecological Inference Is Structured Empirical Risk Minimization: Generalization Across Space, Nested Units, and Niche Support*

**Author:** R. Craig Stillwell  
**Status:** Outline draft (June 2026)  
**Companion to:** Stillwell (2026a) — *Natural Selection Is Empirical Risk Minimization* (Volume I, Project 42)

---

## One-sentence thesis

Ecological inference is empirical risk minimization on **structured** data—where the unit of generalization, spatial confounding, and niche support define the geometry of holdout risk—not a metaphorical extension of population-genetic ERM along a latitude axis.

---

## What this paper is / is not

| It is | It is not |
|-------|-----------|
| A theory paper with formal propositions and proofs (or proof sketches) | Another Stillwell et al. reanalysis of *Stator limbatus* |
| Ecology's missing half of the ERM program | A metaphor essay ("clines are like features") |
| Citable by macroecologists, spatial ecologists, and ML theorists | A JAE methods guide (that is Project 50) |
| Supported by 1–2 short case illustrations per claim | Dependent on one beetle system |
| A coordinate transform of the same Fisher/ERM backbone as Volume I | Kawecki reframed as ecology |

---

## Relationship to Volume I

| | **Volume I — Evolution / ML** | **Volume II — Ecology / ML** |
|---|---|---|
| **Question** | When does a population *learn* (adapt) reliably? | When does an ecological model *generalize* across space? |
| **Primary axis** | Generations (time) | Geography / environmental gradients (space) |
| **Core object** | Genotype → phenotype → fitness across environments | Environment → trait / distribution across populations & sites |
| **Main failure mode** | Overcapacity, drift, negative transfer | Confounding, wrong CV unit, spurious correlates |
| **Canonical ML object** | Multi-task learner | Domain generalization, covariate shift, structured CV |
| **Ecological canon** | Quantitative genetics, selection | Niche theory, macroecology, spatial stats, hierarchy |

**Bridge propositions (§7):** local adaptation = fine-tuning on a spatial subdomain; cline in reaction-norm slope = non-stationary conditional model; range limits = support boundary / extrapolation failure.

---

## Notation (aligned with Volume I)

- **Units:** individual $i$, population $p$, region $r$
- **Predictor:** environmental vector $\mathbf{x}_p \in \mathcal{X}$ (climate, resources, geography)
- **Response:** population mean trait $y_p$, distribution presence $z_p$, or individual $y_{ip}$
- **Hypothesis class:** $\mathcal{H}$ (linear, GAM, RF, mechanistic submodels)
- **Empirical risk:** $\hat{R}_n(h) = \frac{1}{n}\sum \ell(h(\mathbf{x}), y)$
- **Structured risk:** $\hat{R}^{\mathrm{unit}}(h)$ where the holdout set respects the estimand (LOPO, LOGO, block CV)
- **Support:** $\mathrm{supp}(P_{\mathbf{x}})$ — Grinnellian niche as training distribution support
- **Confounded gradient:** $\mathbf{x}$ varies smoothly along geographic axis $g$; univariate correlate $x_j$ is not an intervention

---

## Paper architecture (target ~4,000–6,000 words main + ESM at *Journal of the Royal Society Interface*)

### §1 Introduction — Two coordinate systems, one geometry

- Volume I established ERM on the Fisher manifold for **temporal** learning (selection across generations).
- Ecology's central problem is **spatial** generalization: predict trait or distribution at unseen sites under structured sampling.
- Preview: three estimands, confounded gradients, niche as support, plasticity as label noise, mechanism as interaction.
- Honest scope: ERM-style ecology addresses **predictive** adequacy and **generalization geometry**; it does not replace conservation ethics, process-based simulation, or full causal discovery.

### §2 Structured ERM: the estimand hierarchy

**Ecological theories imported:** hierarchical models (Gelman & Hill); spatial autocorrelation (Legendre); macroecological prediction (Jetz et al., Araújo & Guisan).

**Formal claims:**

**Proposition 1 (Estimand–CV mismatch).**  
Let data be nested $y_{ip}$ with population means $\bar{y}_p$. Standard $k$-fold CV on individuals estimates expected loss for **within-population interpolation** at observed sites. Macroecological hypotheses about clines concern **population-level** function $f: \mathcal{X} \to \mathbb{R}$. Unless holdout sets partition at the population (or region) level, reported CV risk is a biased estimator of the scientific estimand.

*Proof sketch:* Show $\mathbb{E}[\hat{R}^{\mathrm{kfold}}] \neq \mathbb{E}[\hat{R}^{\mathrm{LOPO}}]$ when $\mathrm{Var}(\bar{y}_p \mid \mathbf{x}_p) \ll \mathrm{Var}(y_{ip} \mid p)$ and spatial correlation among $\mathbf{x}_p$ is high.

**Proposition 2 (Three estimands).**  
Define:
1. **E₁ — Within-site:** new individuals at known populations → individual CV OK.
2. **E₂ — Across-site:** new population means at new coordinates → LOPO / LOGO required.
3. **E₃ — Across-environment:** new regions of niche space (extrapolation) → support-aware risk; OOD.

Map each to ML: i.i.d. test, group CV / domain generalization, covariate shift / extrapolation.

**Empirical vignettes (illustration only):**
- **Stillwell et al. 2007** (*Stator*): temperature wins in-sample; ecology wins LOPO (Project 50).
- **Jetz & Rahbek 2002** / **Araújo et al.** species distribution: spatial block CV changes AUC rankings.
- **Kingsolver & Huey** cline reviews: pattern ≠ predictive mechanism.

---

### §3 Confounded gradients as a first-class object

**Ecological theories imported:** ecological collinearity; macroecological correlate traps (Blackburn & Gaston Bergmann program); causal ecology (Pearl-style vs Rubin-style); Hutchinson / Grinnell niche axes.

**Formal claims:**

**Proposition 3 (Gradient confounding inequality).**  
Along a smooth geographic gradient $g$, suppose $\mathbf{x} = \phi(g) + \boldsymbol{\epsilon}$ with $\phi$ monotone and correlated predictors. Let $h_j(x_j)$ be the best univariate predictor of $y$ in-sample. Then for holdout populations at new sites:
$$\mathbb{E}[\ell(h_j, y)]_{\mathrm{LOPO}} \;\geq\; \mathbb{E}[\ell(h^\star, y)]_{\mathrm{LOPO}}$$
where $h^\star$ uses the true (or multivariate) generating set—even when $\mathrm{AIC}(h_j) < \mathrm{AIC}(h^\star)$ in-sample.

*Interpretation:* Latitude/temperature is not "a bad feature"; it is a **structured confounder** along a manifold. In-sample model selection optimizes the wrong functional.

**Proposition 4 (Proxy dominance).**  
The correlate with highest in-sample $R^2$ need not maximize LOPO predictive score when predictors co-vary by construction. Rank reversal between IS and OOS is expected, not pathological.

**Empirical vignettes:**
- **Stillwell et al. 2007** — Bergmann cline, temperature vs moisture/seed/seasonality.
- **Blackburn et al.** Bergmann rule meta-analyses — latitude as weak causal claim.
- **Optional:** marine SST vs chlorophyll along coastlines (literature proxy trap).

---

### §4 Niche as support and domain shift

**Ecological theories imported:** Grinnellian niche (environmental envelope); Eltonian / realized niche (biotic interactions); Hutchinson $n$-dimensional hypervolume; species distribution models; range limits.

**Formal claims:**

**Proposition 5 (Grinnellian support bound).**  
Let training environments $\mathbf{x}_p \in \mathcal{S}_{\mathrm{train}} \subset \mathcal{X}$. For any Lipschitz predictor $h$, extrapolation error outside the convex hull (or learned support estimator) of $\mathcal{S}_{\mathrm{train}}$ grows with distance to support unless invariance assumptions hold. **Range limit** = boundary where $P(y=1 \mid \mathbf{x})$ crosses threshold outside $\mathcal{S}_{\mathrm{train}}$.

**Proposition 6 (Realized niche as hidden context).**  
Biotic interactions enter as unobserved context $u_p$. Observational niche model $P(y \mid \mathbf{x})$ marginalizes $u$; transfer to sites where $P(u \mid \mathbf{x})$ shifts induces **context-dependent label noise**—analogous to covariate shift in $P(\mathbf{x})$ plus label shift in $P(y \mid \mathbf{x})$.

**Empirical vignettes:**
- **Araújo & Guisan 2006** — SDM transfer across regions.
- **Stillwell et al. 2007** — realized niche (host plants) vs climate envelope.
- **Optional:** invasive species OOD (species introduced outside native support).

---

### §5 Plasticity vs adaptation: misleading supervision along clines

**Ecological theories imported:** reaction norms; phenotypic plasticity (Via & Lande); common-garden vs field cline logic; Baldwin effect.

**Formal claims:**

**Proposition 7 (Plasticity as label noise).**  
Observed field cline $y^{\mathrm{field}}_{ip} = g^{\mathrm{gen}}_p + g^{\mathrm{plast}}(\mathbf{x}_p) + \epsilon$. Fitting $h(\mathbf{x})$ to $y^{\mathrm{field}}$ without separating components estimates a **composite target**, not the genetic cline $g^{\mathrm{gen}}$. Under plasticity, $\mathrm{sign}(\partial h / \partial x_j)$ can disagree with $\mathrm{sign}(\partial g^{\mathrm{gen}} / \partial x_j)$—spurious supervision.

*Lemma (Stillwell 2010 Oikos):* Plasticity along a gradient can generate phenotypic clines without genetic differentiation; ERM on phenotypes minimizes the wrong risk for an adaptation estimand.

**Empirical vignettes:**
- **Stillwell 2010** — plasticity confounds adaptive inference (*Manduca* / general argument).
- **Gienapp et al.** — climate tracking via plasticity vs microevolution.
- **Common-garden reanalysis** (literature): field slope ≠ genetic slope.

---

### §6 Mechanism requires interaction tests

**Ecological theories imported:** experimental ecology epistemology; genotype × environment; Kingsolver & Gomulkiewicz selection-gradient framework; manipulative vs observational inference.

**Formal claims:**

**Proposition 8 (Mechanistic adequacy).**  
A mechanistic hypothesis $M$ asserting "environment $e$ modulates selection on trait $z$" implies an **interaction** in the conditional model for fitness or trait change: $\Delta W \sim z \times e$. Observational correlational ERM that fits additive $W \sim z + e$ can achieve low predictive loss along a cline while **falsifying** $M$ under cross-environment holdout or experiment.

**Proposition 9 (Two-test logic).**  
Ecological mechanism certification requires: (i) predict across sites (structured CV), and (ii) test the **required interaction** under manipulation or natural experiment. Passing (i) alone does not certify (ii).

**Empirical vignettes:**
- **Stillwell et al. 2008** — thermal selection on body size; failed Large×Cold interaction.
- **Stillwell et al. 2007 + 2008 pair** — observe then experiment (Bergmann program).
- **Kingsolver et al.** selection gradient experiments (literature anchor).

---

### §7 Bridge to Volume I — where ecology meets evolution

**Unified claims (no new proofs; coordinate transforms):**

| Ecology (Volume II) | Evolution (Volume I) |
|---------------------|----------------------|
| Local adaptation at a site | Fine-tuning / specialization on spatial subdomain |
| Cline in reaction-norm slope | Non-stationary $P(y \mid \mathbf{x}, g)$; task distribution shift |
| Range limit | Support boundary; extrapolation failure / regime collapse |
| Plasticity bias | Label noise; wrong target in ERM |
| Population-level trade-offs across sites | Multi-task conflict across environments (links to Kawecki / Project 48) |
| $\mathbf{G}$-matrix across cline | Effective dimensionality varies with $\mathbf{x}$ |

**Single sentence:** Evolution asks whether the population **updates** reliably; ecology asks whether the fitted mapping **transfers** reliably—same ERM backbone, different axes and failure modes.

---

### §8 Discussion

- What structured ERM does **not** claim (conservation, ethics, full causal graphs).
- Open problems: optimal block size for spatial CV; invariant prediction under confounded gradients; connecting Fisher geometry to spatial Gaussian processes.
- Companion empirics cite Volume I & II; umbrella review deferred until both volumes exist.

---

## Formal claims summary (7 + 2 bridge)

| # | Claim | Ecological canon | ML canon |
|---|-------|------------------|----------|
| P1 | Estimand–CV mismatch | Hierarchy, mixed models | Group / nested CV |
| P2 | Three estimands (E₁, E₂, E₃) | Macroecology, SDMs | DG, covariate shift, OOD |
| P3 | Gradient confounding inequality | Collinearity, clines | Structured confounding |
| P4 | Proxy rank reversal IS vs LOPO | Blackburn Bergmann program | Spurious correlates |
| P5 | Grinnellian support bound | Niche envelope, range limits | Support, extrapolation risk |
| P6 | Realized niche = hidden context | Biotic interactions | Hidden variables, label shift |
| P7 | Plasticity as label noise | Reaction norms, common garden | Misspecified target |
| P8 | Mechanism ⇒ interaction | G×E, selection gradients | Interaction terms |
| P9 | Two-test logic | Manipulative ecology | OOD + causal adequacy |

---

## Empirical vignette allocation (not paper cargo)

| Vignette | Claims illustrated | Role |
|----------|-------------------|------|
| Stillwell 2007 *Am Nat* (Bergmann / LOPO) | P1, P3, P4, P5 | Primary worked example (~3 pages) |
| Stillwell 2008 *Evolution* (selection lines) | P8, P9 | Mechanism / interaction (~2 pages) |
| Stillwell 2010 *Oikos* (plasticity) | P7 | Lemma / box (~1 page) |
| Kawecki 2021 (Project 48) | §7 bridge only | Cross-volume pointer, not ecology payload |
| SDM / Jetz–Araújo literature | P2, P5, P6 | External validation of propositions |
| Blackburn Bergmann meta-analysis | P3, P4 | Macroecology anchor |

**Project 50 (JAE LOPO methods)** feeds P1/P3/P4 as a **protocol citation**, not as the theory paper's empirical core.

---

## Target venues (ranked)

1. **Journal of the Royal Society Interface** — paired with Volume I (PNAS rejected; Vol I at Interface).
2. **Ecological Monographs** — fallback if Interface declines; long-form ecology theory.
3. **Methods in Ecology and Evolution** — only if formal section stays rigorous (not a methods note).
4. **arXiv q-bio.PE + cs.LG** — optional preprint.

---

## Program map (updated)

```
Stillwell 2026a — Natural selection is ERM          [Volume I — Project 42]
Stillwell 2026b — Ecological inference is structured ERM  [Volume II — Project 55] ← THIS DOC

Companion empirics (cite I & II):
  - Kawecki negative transfer (Project 48)
  - Bergmann LOPO + interaction (Project 50 → JAE methods)
  - SSD / allometry modularity (future)

Umbrella review (much later):
  - "Ecology and evolution meet machine learning"
```

---

## Next writing steps

1. [x] Draft §2–3 proofs (estimand mismatch + confounding inequality) — see [`stillwell2026b_section2_3_proofs.md`](stillwell2026b_section2_3_proofs.md)
2. [x] Build minimal simulation: collinear gradient → IS \|r\| favors proxy, LOPO favors multivariate — [`scripts/simulation_lopo_confounding.py`](scripts/simulation_lopo_confounding.py), [`SIMULATION_RESULTS.md`](SIMULATION_RESULTS.md)
3. [x] Pull 2007 LOPO numbers from Project 50 into one table for §2 vignette — see [`stillwell2026b_table_2007_lopo_vignette.md`](stillwell2026b_table_2007_lopo_vignette.md)
4. [x] Literature bib: Grinnell, Hutchinson, Araújo & Guisan, Jetz, Blackburn, Kingsolver & Huey, Gelman & Hill, Arjovsky (IRM), Koh et al. (WILDS) — see [`stillwell2026b.bib`](stillwell2026b.bib) and [`stillwell2026b_bibliography.md`](stillwell2026b_bibliography.md)
5. [x] Decide venue → **Interface** (paired with Vol I); see [`VENUE_DECISION.md`](VENUE_DECISION.md), [`stillwell2026b_coverletter_interface.md`](stillwell2026b_coverletter_interface.md)
6. [x] `\tex` scaffold: [`stillwell2026b_ecological_inference_structured_erm.tex`](stillwell2026b_ecological_inference_structured_erm.tex) (+ [`jmlr2e.sty`](jmlr2e.sty); compiles to PDF)

---

## Open questions for author — resolved (June 2026)

See [`VENUE_DECISION.md`](VENUE_DECISION.md) for full rationale.

- [x] **Title:** keep *structured ERM* (subtitle carries space/niche)
- [x] **Proof standards:** tiered — full P1 in appendix; sketches P2–P8 in main; P9 definitional
- [x] **Simulation:** ecology-motivated semi-synthetic only (no CIFAR benchmark)
- [x] **Coauthor:** solo first submission; optional at revision
