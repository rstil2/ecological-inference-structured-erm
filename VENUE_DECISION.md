# Volume II — Venue decision and manuscript spec

**Decision date:** June 2026  
**Last updated:** June 2026 — PNAS rejected; Volume I at *Interface*  
**Status:** Locked for drafting (paired with Volume I trajectory)

---

## Submission history (Volume I → Volume II)

| Stage | Venue | Status |
|-------|--------|--------|
| Early draft target | JMLR | Superseded |
| First submission | PNAS | **Rejected** |
| **Current (Volume I)** | ***Journal of the Royal Society Interface*** | **In submission / under review** |
| **Volume II target** | ***Journal of the Royal Society Interface*** | Draft toward companion paper |

Volume II follows Volume I to **Interface** so the two-volume ERM program stays in one cross-disciplinary home.

---

## Primary venue: *Journal of the Royal Society Interface*

**Why Interface (not PNAS retry, not JMLR)**

| Factor | Interface | PNAS (rejected) | JMLR |
|--------|-----------|-----------------|------|
| Pairs with Volume I (current submission) | ✅ | ❌ rejected | ❌ splits program |
| Biology ↔ maths / computation framing | ✅ native remit | was fit | ML-only |
| Formal propositions + electronic SI | ✅ standard | SI pattern | long main text |
| Main text length | **~4,000–6,000 words + ESM** | ~6 pp | ~40 pp |
| Ecology + evolution + ML audience | ✅ | broad | narrow |

**Submission strategy**

1. **Do not submit Volume II until Volume I outcome is clear** — or submit as companion with cover letter cross-reference if editor invites paired work.
2. Cover letter states **two-volume program**: Vol I = temporal learning / selection; Vol II = spatial generalization / structured ERM.
3. **Main text:** significance, framework, core propositions (compressed), simulation + vignette figure, pointer to ESM.
4. **Electronic supplementary material (ESM):** full proofs (P1–P9), LOPO tables, simulation protocol (Project 55 + Project 50 cite).
5. **arXiv** (`q-bio.PE` + `cs.LG`) optional; not a substitute for journal.
6. **Fallback** if Interface declines Vol II: *Ecological Monographs* (long-form ecology theory) or *Methods in Ecology and Evolution* (only if theory stays rigorous — not a methods note).

---

## Open questions — resolved defaults

| Question | Decision |
|----------|----------|
| **Title** | Keep **“structured ERM”** |
| **Proof standards** | Main = statements + intuition; **ESM = full proofs** |
| **Simulation** | Ecology semi-synthetic only (500-rep cline + *Stator* vignette) |
| **Coauthor** | Solo unless Interface revision requests specialist |

---

## Proof depth matrix (Interface tier)

| Claim | Main text | ESM |
|-------|-----------|-----|
| P1 Estimand–CV mismatch | Statement + paragraph | Full proof |
| P2 Three estimands | Definition box | — |
| P3–P4 Confounding / rank reversal | Statements + sim figure | Full / constructive proofs |
| P5–P9 Niche, plasticity, mechanism | Statements (+ lemma cite) | Proofs |
| Empirical | 1 table + 1 figure | Full LOPO tables (Project 50) |

---

## Target length (Interface)

| Component | Target |
|-----------|--------|
| **Main text** | **4,000–6,000 words** (~8–10 pages formatted) |
| **Abstract** | ≤ 200 words (Interface guideline) |
| **Figures (main)** | 2–4 |
| **ESM** | Proofs + supplementary tables + code note |
| **Current LaTeX draft** | ~9 pp in `jmlr2e` — **draft scaffold only**; reformat to Interface template before submission |

Before submission: migrate from `jmlr2e.sty` to Royal Society / Interface LaTeX class; split `stillwell2026b_SI.tex` for ESM.

---

## Checklist item 5

- [x] Venue: **Journal of the Royal Society Interface** (paired with Volume I)
- [x] Length: main ~5k words + ESM
- [x] Proof depth: main statements / ESM proofs
- [x] Fallback: Eco Monographs
