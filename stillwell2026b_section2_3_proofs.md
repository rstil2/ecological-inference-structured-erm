# Volume II — §2–3 Proof Drafts

**Status:** Working draft (June 2026)  
**Companion:** `stillwell2026b_ecological_inference_structured_erm_outline.md`  
**Empirical anchors:** Project 50 LOPO workflow; `08_lopo_simulation.py`, `09_cv_unit_comparison.py`

---

## §2 Structured ERM: estimand hierarchy

### Setup (shared)

Data are nested: individual $i \in \{1,\ldots,n_p\}$ in population (site) $p \in \{1,\ldots,P\}$.

- Individual response: $y_{ip}$
- Population mean: $\bar{y}_p = n_p^{-1}\sum_i y_{ip}$
- Site covariates: $\mathbf{x}_p \in \mathcal{X} \subset \mathbb{R}^d$ (climate, resources, geography)
- Hypothesis class $\mathcal{H}$; loss $\ell(\hat{y}, y)$ (squared error unless noted)
- Predictor $h \in \mathcal{H}$; fitted by ERM on a training subset

Write population-level targets as
$$y_{ip} = \mu(\mathbf{x}_p) + u_p + \varepsilon_{ip}, \qquad u_p \perp \varepsilon_{ip}, \quad \mathbb{E}[u_p \mid \mathbf{x}_p]=0,$$
with $\mu(\mathbf{x}_p) = \mathbb{E}[\bar{y}_p \mid \mathbf{x}_p]$ and $\varepsilon_{ip}$ within-population noise. Macroecological cline hypotheses concern $\mu(\cdot)$, not individual residuals.

---

### Proposition 1 (Estimand–CV mismatch)

**Statement.** Let $\hat{R}^{\mathrm{kfold-ind}}(h)$ denote $K$-fold cross-validation with folds over **individuals** (standard random split). Let $\hat{R}^{\mathrm{LOPO}}(h)$ denote leave-one-population-out CV on **population means** $(\bar{y}_p, \mathbf{x}_p)$. Then

$$\mathbb{E}\big[\hat{R}^{\mathrm{kfold-ind}}(h)\big] \;\neq\; \mathbb{E}\big[\hat{R}^{\mathrm{LOPO}}(h)\big]$$

whenever (i) $\mathrm{Var}(\varepsilon_{ip} \mid p) > 0$ and (ii) the scientific estimand is prediction of $\bar{y}_{p^\star}$ at a **new** site $p^\star$ given $\mathbf{x}_{p^\star}$.

**Interpretation.** Individual $k$-fold estimates risk for **E₁** (new individuals at observed sites). LOPO estimates risk for **E₂** (new site means). Reporting $\hat{R}^{\mathrm{kfold-ind}}$ as if it validated a macroecological cline claim is an estimand error, not a small-sample nuisance.

---

#### Proof

Partition risk by estimand.

**E₁ (within-site):** predict a new individual at a population already represented in training:
$$R_1(h) = \mathbb{E}\Big[\ell\big(h(\mathbf{x}_p), y_{i^\star p}\big) \;\Big|\; p \in \mathcal{P}_{\mathrm{train}}\Big].$$

**E₂ (across-site):** predict the population mean at a held-out site:
$$R_2(h) = \mathbb{E}\Big[\ell\big(h(\mathbf{x}_{p^\star}), \bar{y}_{p^\star}\big)\Big].$$

Under the generative model above, for squared loss at the population mean,
$$R_2(h) = \mathbb{E}\Big[\big(h(\mathbf{x}_{p^\star}) - \mu(\mathbf{x}_{p^\star})\big)^2\Big] + \mathrm{Var}(\bar{u}_{p^\star}),$$
where $\bar{u}_{p^\star} = n_{p^\star}^{-1}\sum_i u_{p^\star}$. The irreducible term $\mathrm{Var}(\bar{u}_{p^\star})$ vanishes as $n_{p^\star}\to\infty$; the target is $\mu(\cdot)$.

For **E₁**, decompose
$$\mathbb{E}\big[(h(\mathbf{x}_p) - y_{i^\star p})^2 \mid p\big] = \big(h(\mathbf{x}_p) - \mu(\mathbf{x}_p)\big)^2 + \mathrm{Var}(u_p \mid \mathbf{x}_p) + \mathrm{Var}(\varepsilon_{ip}).$$

Thus $R_1(h) = R_2(h) + \mathbb{E}[\mathrm{Var}(\varepsilon_{ip}\mid p)] + \text{(within-site bias terms)}$ whenever folds place test individuals from populations also present in training.

**Key leakage.** In individual $k$-fold with multiple individuals per population, training and test sets share site identity $p$. Any model class rich enough to absorb site-level structure (random intercepts, high-dimensional individual features, or implicit memorization of $\bar{y}_p$ through repeated draws from the same $\mathbf{x}_p$) reduces apparent error on test individuals at **known** sites without improving prediction at **new** sites.

**LOPO** removes site identity from training when predicting $\bar{y}_p$; its expectation targets $R_2(h)$ (up to finite-$P$ variance).

**Strict inequality.** If $\mathrm{Var}(\varepsilon_{ip}\mid p) > 0$, then $R_1(h) > R_2(h)$ for any $h$ with identical population-level fit. Individual $k$-fold risk averages within-population noise into the reported CV metric; LOPO does not. Hence the two estimators converge to different targets.

**Corollary (ranking bias).** Model ranking by $\hat{R}^{\mathrm{kfold-ind}}$ need not agree with ranking by $\hat{R}^{\mathrm{LOPO}}$ when models differ in within-site flexibility. Example: a model that fits population-specific intercepts can win E₁ while losing E₂.

**Empirical illustration (Project 50).** On *Stator limbatus* (2007 survey), ecology multivariate LOPO RMSE = 0.104 vs individual 10-fold RMSE = 0.150 (+45% inflation on the same predictors; `cv_unit_comparison.json`). Both schemes rank ecology above temperature-only, but the absolute CV risk answers different questions.

$\square$

---

### Proposition 2 (Three estimands)

**Statement.** Ecological prediction problems decompose into three distinct estimands:

| Estimand | Question | Holdout unit | ML analogue |
|----------|----------|--------------|-------------|
| **E₁ — Within-site** | New individuals at **known** populations | Individual (or within-population) | i.i.d. test set |
| **E₂ — Across-site** | New **population means** at new coordinates | Population / site (LOPO, LOGO) | Group CV, domain generalization |
| **E₃ — Across-environment** | New regions of niche space (extrapolation) | Domain / region outside training support | Covariate shift, OOD |

**Proof sketch.** This is a classification of prediction targets by the distribution of the test point relative to training support.

- E₁: $p \in \mathcal{P}_{\mathrm{train}}$, new $i$ — conditional distribution $P(y \mid \mathbf{x}_p, p)$ shifts only through individual noise.
- E₂: new $p^\star$ with $\mathbf{x}_{p^\star}$ from the same geographic process as training sites but $p^\star \notin \mathcal{P}_{\mathrm{train}}$ — requires transfer of $\mu(\mathbf{x})$ across sites; site-specific random effects must not leak into training.
- E₃: $\mathbf{x}_{p^\star} \notin \mathcal{S}_{\mathrm{train}} = \mathrm{supp}(P_{\mathbf{x}} \mid \text{training})$ — support mismatch; no CV scheme on observed sites alone certifies extrapolation without invariance assumptions (see §4, Proposition 5).

Proposition 1 shows E₁ and E₂ are not interchangeable; conflating them is the most common estimand error in cline and SDM work.

$\square$

---

## §3 Confounded gradients

### Setup (shared)

Populations are ordered along a geographic axis $g_p \in \mathbb{R}$ (latitude, elevation transect, etc.). Environmental predictors satisfy
$$\mathbf{x}_p = \boldsymbol{\phi}(g_p) + \boldsymbol{\epsilon}_p, \qquad \boldsymbol{\phi}\ \text{monotone/co-monotone across coordinates},$$
so predictors are **structurally collinear** along the gradient. The generating regression is
$$y_p = \mathbf{x}_p^\top \boldsymbol{\beta}^\star + \eta_p, \qquad \eta_p \sim (0, \sigma_\eta^2),$$
with $\boldsymbol{\beta}^\star$ sparse or low-dimensional in the ecological variables that actually drive $\mu(\mathbf{x})$.

Let $h_j$ be the **best in-sample univariate** linear predictor using coordinate $x_j$:
$$h_j(g_p) = \hat{\alpha}_j x_{j,p}, \qquad \hat{\alpha}_j = \arg\min_\alpha \sum_{p=1}^P (y_p - \alpha x_{j,p})^2.$$

Let $h^\star$ be the **population-level OLS** predictor using the true support $\mathcal{S}^\star = \{k : \beta_k^\star \neq 0\}$:
$$h^\star(\mathbf{x}_p) = \mathbf{x}_{p,\mathcal{S}^\star}^\top \hat{\boldsymbol{\beta}}_{\mathcal{S}^\star}.$$

Define LOPO risk for squared error:
$$R_{\mathrm{LOPO}}(h) = \frac{1}{P}\sum_{p=1}^P \Big(y_p - \hat{h}^{(-p)}(\mathbf{x}_p)\Big)^2,$$
where $\hat{h}^{(-p)}$ is fit on all populations except $p$.

---

### Proposition 3 (Gradient confounding inequality)

**Statement.** Under the generating model above with $|\mathcal{S}^\star| \geq 2$ and non-degenerate collinearity along $g$,

$$R_{\mathrm{LOPO}}(h_j) \;\geq\; R_{\mathrm{LOPO}}(h^\star),$$

with strict inequality when $x_j$ is a **proxy** for the true drivers (i.e., $\beta_j^\star = 0$ but $\mathrm{Corr}(x_j, \mathbf{x}_{\mathcal{S}^\star}) \neq 0$).

Moreover, the **in-sample** univariate fit can appear superior by information criteria even when LOPO favors $h^\star$ (Proposition 4).

**Interpretation.** Along a smooth geographic manifold, a visible correlate (latitude, temperature) is not an intervention; it is a **structured confounder**. In-sample ERM on $x_j$ absorbs variation from unmeasured or omitted components of $\mathbf{x}$ that co-vary along $g$. LOPO at held-out sites breaks that absorption when the proxy–ecology relationship at site $p$ deviates from the training manifold.

---

#### Proof

**Step 1 — Oracle inequality (model class).**  
$h^\star$ is the population-level least-squares estimator on the true support. For any linear $h_j$ using only $x_j$,
$$\mathbb{E}\Big[(y_p - h_j(\mathbf{x}_p))^2\Big] \geq \mathbb{E}\Big[(y_p - h^\star(\mathbf{x}_p))^2\Big]$$
at each fixed $p$, with equality iff $x_j$ carries the same information as $\mathbf{x}_{\mathcal{S}^\star}$ for predicting $y_p$ (i.e., the proxy is sufficient). Averaging over $p$ and replacing in-sample fit with LOPO out-of-fold predictions preserves the inequality up to finite-sample estimation variance; LOPO is an unbiased leave-out estimator of per-site generalization for population means under standard linear-model assumptions.

**Step 2 — Proxy case ($\beta_j^\star = 0$).**  
Write the true model as
$$y_p = \mathbf{x}_{p,\mathcal{S}^\star}^\top \boldsymbol{\beta}^\star_{\mathcal{S}^\star} + \eta_p.$$
Because $\mathbf{x}_p = \boldsymbol{\phi}(g_p) + \boldsymbol{\epsilon}_p$, along the gradient we have $x_{j,p} = \phi_j(g_p) + \epsilon_{j,p}$ with $\phi_j$ monotone. The in-sample univariate slope $\hat{\alpha}_j$ solves
$$\hat{\alpha}_j = \frac{\sum_p x_{j,p} y_p}{\sum_p x_{j,p}^2} \approx \frac{\mathrm{Cov}(x_j, \mathbf{x}_{\mathcal{S}^\star}^\top \boldsymbol{\beta}^\star)}{\mathrm{Var}(x_j)}.$$
Thus $\hat{\alpha}_j$ is a **conflated** blend of direct and indirect paths: latitude/temperature inherits predictive power from ecology variables that co-vary along $g$, even when $\beta_j^\star = 0$.

**Step 3 — Why LOPO exposes the gap.**  
For held-out population $p$, LOPO prediction uses $\hat{\alpha}_j^{(-p)}$ fit without site $p$. The prediction error at $p$ is
$$\big(\hat{\alpha}_j^{(-p)} x_{j,p} - \mathbf{x}_{p,\mathcal{S}^\star}^\top \boldsymbol{\beta}^\star_{\mathcal{S}^\star}\big)^2.$$
When $(x_{j,p}, \mathbf{x}_{p,\mathcal{S}^\star})$ lies off the training collinearity manifold — i.e., ecology at site $p$ is not what latitude alone would predict — the univariate extrapolation along the proxy axis fails. The multivariate $h^\star$, using ecological drivers directly, remains stable provided those variables are observed.

**Step 4 — Strict inequality condition.**  
If there exists at least one held-out site where
$$\mathbf{x}_{p,\mathcal{S}^\star} \not\approx \mathbb{E}[\mathbf{x}_{\mathcal{S}^\star} \mid x_j = x_{j,p}],$$
then univariate proxy prediction incurs excess error relative to $h^\star$. Along continental clines with local ecological heterogeneity, such sites exist with positive probability; strict inequality follows.

**Connection to simulation (Project 50).** In `08_lopo_simulation.py`, ecology generates $y$ while latitude is the strongest univariate $|r|$ in 100% of 500 replicates, yet ecology wins LOPO in 84%; in 84% of replicates in-sample best-univariate and best-LOPO models **disagree**. This is the finite-sample manifestation of Propositions 3–4.

$\square$

---

### Proposition 4 (Proxy dominance / rank reversal)

**Statement.** Define in-sample AIC for nested linear models on population means (Gaussian log-likelihood with parameter penalty). There exist data-generating processes with collinear $\mathbf{x}_p$ such that, with positive probability,

1. $\mathrm{AIC}(h_j) < \mathrm{AIC}(h^\star)$ (proxy wins in-sample), but  
2. $R_{\mathrm{LOPO}}(h_j) > R_{\mathrm{LOPO}}(h^\star)$ (structural model wins holdout).

Similarly, the univariate predictor with largest in-sample $|r|$ need not minimize LOPO RMSE.

**Interpretation.** Rank reversal between in-sample criteria and LOPO is **expected** under gradient confounding, not pathological. Macroecological surveys that rank correlates by in-sample $R^2$ or AIC on the full pooled sample optimize the wrong functional for E₂.

---

#### Proof sketch

Consider $P$ populations with
$$y_p = \beta_1 x_{1,p} + \beta_2 x_{2,p} + \eta_p, \quad \beta_1, \beta_2 \neq 0,$$
and $x_{2,p} = \rho x_{1,p} + \nu_p$ with $\rho \neq 0$ and $\nu_p$ small along the training transect (high collinearity).

**In-sample:** the univariate model on $x_1$ achieves high $R^2$ because $x_1$ proxies for $x_2$. With penalty $2k$, AIC may favor the parsimonious proxy when the multivariate gain is small on the pooled sample — especially if $P$ is moderate or if missing covariates shrink the multivariate sample (see *Stator*: AIC on all 95 populations ranks latitude best when ecology covariates are incomplete on two sites).

**LOPO:** at site $p$ where $\nu_p$ is large (ecology deviates from latitude expectation), univariate prediction along $x_1$ errors by approximately $(\beta_2 \nu_p)^2$ while the bivariate model retains $\beta_2 x_{2,p}$. Averaging across held-out sites yields $R_{\mathrm{LOPO}}(h_j) > R_{\mathrm{LOPO}}(h^\star)$.

**Constructive existence:** Project 50 simulation with `ecology_lat_corr=0.55`, true coefficients on seed/moisture/seasonality, and latitude a correlated proxy yields 84% rank disagreement — sufficient for a constructive proof sketch. A fully analytic proof can be completed for the linear-Gaussian $P\to\infty$ limit using standard results on omitted-variable bias in partial vs marginal regression, with LOPO replacing in-sample LOO.

**Empirical illustration (*Stator*, Table 1 Project 50).** On matched $n=93$ populations: temperature-only has highest in-sample $|r|$ with size yet worst LOPO RMSE (0.112); ecology multivariate best LOPO (0.104). Latitude wins in-sample AIC on the full 95-population survey while ecology wins on the ecology-complete matched set — demonstrating that **both** confounding and **sample composition** can reverse ranks between in-sample and holdout criteria.

$\square$

---

## Remarks for manuscript integration

1. **Proof depth:** Propositions 1 and 3 are ready for appendix full proofs; Proposition 4 may remain proof sketch + simulation unless venue demands measure-theoretic form.
2. **Lemma to add in §2:** Finite-$n_p$ correction linking $\bar{y}_p$ to $\mu(\mathbf{x}_p)$ — when $n_p$ is large (as in 2007 survey), individual-noise term in E₁ is small but non-zero; LOPO remains the correct unit for E₂.
3. **Figure pairing:** Fig A = Prop 1 (k-fold vs LOPO bars from Project 50); Fig B = Prop 3–4 (simulation mismatch rate + 2007 rank table).
4. **Volume I cross-link:** Prop 1 is the spatial analogue of training-set / capacity confounds: wrong **unit of generalization** inflates apparent performance the same way $N_e$ inflation does for temporal learning.

---

## Checklist update

- [x] Draft §2–3 proofs (estimand mismatch + confounding inequality)
- [x] Build minimal simulation (exists in Project 50 — cite or port to Project 55) — see [`SIMULATION_RESULTS.md`](SIMULATION_RESULTS.md)
- [x] Pull 2007 LOPO numbers into one table for §2 vignette — [`stillwell2026b_table_2007_lopo_vignette.md`](stillwell2026b_table_2007_lopo_vignette.md)
- [x] Literature bib
- [x] Decide venue → **Interface**; see [`VENUE_DECISION.md`](VENUE_DECISION.md)
- [x] LaTeX scaffold
