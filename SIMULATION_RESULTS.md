# Simulation results — gradient confounding (§3)

**Script:** [`scripts/simulation_lopo_confounding.py`](scripts/simulation_lopo_confounding.py)  
**Source port:** Project 50 `scripts/08_lopo_simulation.py`  
**Claims:** Proposition 3 (gradient confounding), Proposition 4 (rank reversal)

---

## Generating process

Each replicate simulates **95 populations** with:

- `pc1_mean ~ 0.35·seedsize + 0.30·moist_pc1 + 0.25·season_pc1 + noise`
- Ecology predictors correlated with latitude (`ecology_lat_corr = 0.55`)
- Mean annual temperature weakly correlated with latitude (`temp_lat_corr = -0.35`)

Models compared (OLS, standardised predictors):

| Key | Predictors |
|-----|------------|
| `latitude_only` | lat |
| `temperature_only` | annmeantemp |
| `ecology_multivariate` | seedsize, moist_pc1, season_pc1 |
| `temperature_plus_ecology` | all four |

**LOPO:** leave-one-population-out RMSE on population means.  
**In-sample:** strongest univariate \|r\| (lat vs temp); AIC on full sample.

---

## Results (500 replicates, seed 42)

| Metric | Rate |
|--------|------|
| Latitude strongest in-sample \|r\| | **100%** |
| Ecology best LOPO model | **84%** |
| \|r\| rank ≠ LOPO rank (lat wins \|r\|, ecology wins LOPO) | **84%** |
| AIC prefers latitude over ecology (this parameter regime) | 0% |

In this regime, in-sample AIC usually agrees with ecology because multivariate fit is genuinely better on the pooled sample; the simulation **isolates the correlation–LOPO gap** under known truth. The empirical *Stator* vignette (Table 1) shows AIC–LOPO disagreement can also arise from **sample composition** (n=95 vs n=93).

---

## Outputs

| File | Description |
|------|-------------|
| [`outputs/tables/simulation_lopo_mismatch.json`](outputs/tables/simulation_lopo_mismatch.json) | Summary rates |
| [`outputs/figures/simulation_lopo_mismatch_rates.png`](outputs/figures/simulation_lopo_mismatch_rates.png) | Main figure for §3 / LaTeX Fig. 1 |
| [`outputs/figures/simulation_aic_vs_lopo_example.png`](outputs/figures/simulation_aic_vs_lopo_example.png) | Single-replicate ranking example |

---

## Run

```bash
cd "Project 55 - Ecology:ML"
pip install -r requirements.txt
python3 scripts/simulation_lopo_confounding.py
```

---

## LaTeX inclusion

Figure included in `stillwell2026b_ecological_inference_structured_erm.tex` §6 (`\ref{fig:sim-mismatch}`).
