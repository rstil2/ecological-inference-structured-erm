# §2 Vignette — *Stator limbatus* LOPO tables (2007 survey)

**Source:** Project 50 reanalysis of Stillwell et al. (2007); scripts `03_proxy_vs_multivariate_2007.py`, `09_cv_unit_comparison.py`, `10_aic_vs_lopo.py`, `11_lopo_bootstrap.py`.  
**Response:** population mean body-size PC1 (pooled sexes).  
**Claims illustrated:** P1 (estimand–CV mismatch), P3–P4 (confounded gradient / proxy trap).

---

## Table 1 — In-sample correlate vs LOPO holdout (matched *n* = 93 populations)

Primary paired comparison. Populations 17 and 61 excluded (missing host seed size). All models fit on standardised predictors; LOPO = leave-one-population-out on population means.

| Model | Predictors | In-sample \|*r*\| with PC1 | In-sample AIC | In-sample *R*² | LOPO RMSE | LOPO *R*² | LOPO rank |
|-------|------------|----------------------------|---------------|------------------|-----------|----------|-----------|
| Latitude | `lat` | **0.416** (strongest) | −155.7 | 0.173 | 0.106 | 0.121 | 3 |
| Mean annual temperature | `annmeantemp` | 0.219 | −142.6 | 0.048 | **0.112** (worst) | 0.009 | 4 |
| Ecology multivariate | seed size, moisture PC1, seasonality PC1 | — | **−156.7** (best) | **0.217** | **0.104** (best) | **0.157** | **1** |
| Temperature + ecology | all four | — | −155.0 | 0.219 | 0.106 | 0.124 | 2 |

**Relative LOPO improvement (ecology vs):** temperature −7.7% RMSE; latitude −2.1% RMSE.

**Takeaway for §2:** Latitude is the strongest univariate correlate and nearly as good as ecology on LOPO, but **temperature-only is a poor holdout predictor** despite being a standard Bergmann proxy. Ecology multivariate wins LOPO on the fair common set; in-sample \|*r*\| alone would mislead toward latitude and away from rejecting temperature.

---

## Table 2 — Estimand mismatch: individual *k*-fold vs LOPO (P1)

Same predictors; different cross-validation unit. Individual 10-fold CV on beetles; LOPO on population means (*n* = 93 for ecology-complete models).

| Model | 10-fold individual RMSE | 10-fold *R*² | LOPO population RMSE | LOPO *R*² | RMSE inflation (k-fold / LOPO) |
|-------|-------------------------|--------------|----------------------|----------|--------------------------------|
| Ecology multivariate | 0.150 | 0.117 | 0.104 | 0.157 | **+45%** |
| Mean annual temperature | 0.158 | 0.017 | 0.112 | 0.009 | +41% |

Both schemes rank ecology above temperature, but individual *k*-fold reports substantially higher RMSE on a **different estimand** (E₁: new individuals at known sites) than LOPO (E₂: new population means).

---

## Table 3 — Bootstrap paired LOPO comparisons (*B* = 10,000)

Population resampling; negative difference favours first model in pair (lower RMSE).

| Comparison | *n* | Observed ΔRMSE | 95% CI | *P*(first model lower) |
|------------|-----|----------------|--------|-------------------------|
| Ecology − latitude | 93 | −0.002 | [−0.011, +0.006] | 0.68 |
| Ecology − temperature | 93 | −0.009 | [−0.017, 0.000] | **0.97** |
| Latitude − temperature | 95 | −0.007 | [−0.018, +0.006] | 0.85 |

Ecology vs temperature is the clear separation; ecology vs latitude is a **thin margin** (0.002 on PC1 scale) — report with bootstrap, do not over-interpret ranking.

---

## Table 4 — Sample composition: why AIC and LOPO can disagree (P4)

On the **full 95-population survey**, ecology covariates are missing for two sites; AIC on `n` = 95 favours latitude even though ecology is not comparable on the same rows.

| Sample | Model | *n* | In-sample AIC | AIC rank | LOPO RMSE | LOPO rank |
|--------|-------|-----|---------------|----------|-----------|-----------|
| Full survey | Latitude | 95 | **−161.1** | **1** | 0.105 | 2 |
| Full survey | Temperature | 95 | −147.5 | 3 | 0.111 | 3 |
| Full survey | Ecology multivariate | 93† | −156.7† | — | 0.104† | **1** |
| Matched ecology-complete | Latitude | 93 | −155.7 | 2 | 0.106 | 3 |
| Matched ecology-complete | Ecology multivariate | 93 | **−156.7** | **1** | **0.104** | **1** |

†Ecology fit and LOPO use 93 populations with seed-size data; latitude/temperature use 95 on full-survey rows. Comparing AIC on 95 populations with LOPO on ecology-complete 93 can reverse latitude vs ecology conclusions.

---

## Table 5 — Simulation anchor (confounded gradient; not *Stator* data)

Semi-synthetic clines (`08_lopo_simulation.py`; 500 replicates × 95 populations). Generating process: ecology drives size; latitude is a correlated proxy.

| Criterion | Best model | Rate |
|-----------|------------|------|
| Strongest in-sample univariate \|*r*\| | Latitude (proxy) | 100% |
| Lowest LOPO RMSE | Ecology multivariate | 84% |
| In-sample \|*r*\| rank ≠ LOPO rank | — | **84%** |

Pairs with Table 1: empirical case shows ecology ≈ latitude on LOPO (thin margin) but temperature clearly fails; simulation shows the **correlation–LOPO gap** under known generating structure.

---

## Manuscript caption (draft)

> **Table X.** Geographic body-size cline in *Stator limbatus* (Stillwell et al. 2007): in-sample correlates and information criteria compared with leave-one-population-out (LOPO) prediction of held-out population means. Macroecological Bergmann hypotheses concern E₂ (across-site transfer); LOPO is the appropriate default estimand. On matched populations (*n* = 93), ecology multivariate minimises LOPO error; latitude has the highest univariate \|*r*\|; mean annual temperature is the worst holdout predictor. Individual-level *k*-fold cross-validation (Table 2) answers a different question and inflates reported RMSE. Bootstrap intervals (Table 3) and sample-composition sensitivity (Table 4) follow Project 50 protocol. Simulation (Table 5) shows rank reversal between in-sample correlation and LOPO is expected under gradient confounding.

---

## Notes for Volume II vs Project 50

| | **Volume II (theory)** | **Project 50 (JAE methods)** |
|--|------------------------|------------------------------|
| Role | Illustrate P1, P3–P4 (~2–3 pages) | Full protocol, figures, reproducible pipeline |
| Emphasis | Estimand geometry, proxy logic | Workflow, bootstrap, Test B pointer |
| Table use | Tables 1–2 + one row from Table 5 | All tables + sex-stratified SI |

**Citation path:** Stillwell et al. (2007) original data → Project 50 methods preprint for numbers → Volume II cites both, does not duplicate Project 50 figures.

---

## Data provenance

```
Project 50/outputs/tables/2007_proxy_trap_cv.json
Project 50/outputs/tables/aic_vs_lopo.json
Project 50/outputs/tables/lopo_rmse_bootstrap.json
Project 50/outputs/tables/cv_unit_comparison.json
Project 50/outputs/tables/simulation_lopo_mismatch.json
Project 50/data/processed/2007_population_means.csv
```
