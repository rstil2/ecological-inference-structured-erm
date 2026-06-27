# Volume II — Venue decision

**Decision date:** June 2026  
**Status:** **Locked — *Journal of the Royal Society Interface***

---

## Primary venue: *Journal of the Royal Society Interface*

Volume II is submitted as the **spatial companion** to Volume I (*Natural Selection Is Empirical Risk Minimization*), also at Interface (Project 42).

| Factor | Interface |
|--------|-----------|
| Pairs with Volume I | Yes |
| Biology ↔ maths / computation | Native remit |
| Formal results + ESM | Standard |
| Initial submission format | **ScholarOne requires `.docx` main** + ESM PDF (see `build_interface_submission.sh`) |
| Main text target | ~4,000–6,000 words + ESM |
| Abstract | ≤200 words, no references |
| Media summary | ≤100 words at **final files** (draft in manuscript + `stillwell2026b_media_summary.md`) |

**Fallback:** *Ecological Monographs* or *Methods in Ecology and Evolution* if Interface declines.

---

## Submission bundle

Build:

```bash
bash scripts/build_interface_submission.sh
```

Output: `submission/interface/` — main PDF, ESM PDF, figures, LaTeX source, cover letter, upload checklist.

---

## Pre-submission checklist

- [x] Theorem reframing (Lemma + rank reversal; propositions unbundled)
- [x] Scope language (simulation rates design-specific; Stator illustrative)
- [x] No load-bearing unpublished methods companion cites
- [x] Code URL in Methods (not “on request”)
- [ ] **Public GitHub repo live** + Zenodo DOI at submission
- [ ] Cover letter updated; Volume I status current
- [ ] ScholarOne upload (`https://mc.manuscriptcentral.com/rsif`)

---

## Volume I contingency

| Volume I outcome | Volume II action |
|------------------|------------------|
| Accepted at Interface | Submit II as companion; cross-reference published I |
| Under review | Submit II with cover letter noting paired program |
| Rejected elsewhere | Revise intro; II can stand alone on spatial ERM framework |

Spatial claims in Table 1 and Theorems 1–2 do **not** require Volume I acceptance.
