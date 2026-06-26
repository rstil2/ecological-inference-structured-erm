#!/usr/bin/env python3
"""
Volume II simulation (Proposition 3--4): collinear geographic gradient.

Ecology generates population mean trait; latitude is a correlated proxy.
In-sample |r| often favours latitude; LOPO favours ecology multivariate.

Ported from Project 50 scripts/08_lopo_simulation.py for theory-paper reproducibility.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cv_common import MODELS, in_sample_aic

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "outputs" / "figures"
TAB = ROOT / "outputs" / "tables"
FIG.mkdir(parents=True, exist_ok=True)
TAB.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(42)
N_REPS = 500
N_POP = 95


def fast_lopo_rmse(df: pd.DataFrame, features: list[str]) -> float:
    sub = df[["pc1_mean"] + features].dropna().copy()
    y = sub["pc1_mean"].to_numpy()
    x = sub[features].to_numpy()
    n = len(y)
    preds = np.empty(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        x_train = x[mask]
        y_train = y[mask]
        x_test = x[i]
        mu = x_train.mean(axis=0)
        sd = x_train.std(axis=0, ddof=0)
        sd[sd == 0] = 1.0
        x_train_s = (x_train - mu) / sd
        x_test_s = (x_test - mu) / sd
        x_train_s = np.column_stack([np.ones(len(y_train)), x_train_s])
        x_test_s = np.concatenate([[1.0], x_test_s])
        beta, *_ = np.linalg.lstsq(x_train_s, y_train, rcond=None)
        preds[i] = float(x_test_s @ beta)
    return float(np.sqrt(np.mean((y - preds) ** 2)))


def simulate_population_table(
    n_pop: int,
    rng: np.random.Generator,
    *,
    ecology_lat_corr: float = 0.55,
    temp_lat_corr: float = -0.35,
    noise_sd: float = 0.10,
) -> pd.DataFrame:
    lat = rng.normal(0, 1, n_pop)
    lat = (lat - lat.mean()) / lat.std()

    seedsize = ecology_lat_corr * lat + rng.normal(0, 1, n_pop) * np.sqrt(1 - ecology_lat_corr**2)
    moist_pc1 = 0.45 * lat + rng.normal(0, 1, n_pop) * 0.75
    season_pc1 = 0.50 * lat + rng.normal(0, 1, n_pop) * 0.70

    seedsize = (seedsize - seedsize.mean()) / seedsize.std()
    moist_pc1 = (moist_pc1 - moist_pc1.mean()) / moist_pc1.std()
    season_pc1 = (season_pc1 - season_pc1.mean()) / season_pc1.std()

    annmeantemp = temp_lat_corr * lat + rng.normal(0, 1, n_pop) * np.sqrt(1 - temp_lat_corr**2)
    annmeantemp = (annmeantemp - annmeantemp.mean()) / annmeantemp.std()

    pc1_mean = (
        0.35 * seedsize
        + 0.30 * moist_pc1
        + 0.25 * season_pc1
        + rng.normal(0, noise_sd, n_pop)
    )
    pc1_mean = (pc1_mean - pc1_mean.mean()) / pc1_mean.std()

    return pd.DataFrame({
        "pop": np.arange(1, n_pop + 1),
        "pc1_mean": pc1_mean,
        "lat": lat,
        "annmeantemp": annmeantemp,
        "seedsize": seedsize,
        "moist_pc1": moist_pc1,
        "season_pc1": season_pc1,
    })


def univariate_r(df: pd.DataFrame, col: str) -> float:
    sub = df[["pc1_mean", col]].dropna()
    return float(sub["pc1_mean"].corr(sub[col]))


def model_rank_by_lopo(df: pd.DataFrame) -> list[str]:
    scores = {name: fast_lopo_rmse(df, feats) for name, feats in MODELS.items()}
    return sorted(scores, key=scores.get)


def model_rank_by_aic(df: pd.DataFrame) -> list[str]:
    scores = {name: in_sample_aic(df, feats)["aic"] for name, feats in MODELS.items()}
    return sorted(scores, key=scores.get)


def strongest_univariate(df: pd.DataFrame) -> str:
    cols = {"lat": "latitude_only", "annmeantemp": "temperature_only"}
    corrs = {cols[c]: abs(univariate_r(df, c)) for c in cols}
    return max(corrs, key=corrs.get)


def run_replicate(rng: np.random.Generator) -> dict:
    df = simulate_population_table(N_POP, rng)
    lopo_rank = model_rank_by_lopo(df)
    aic_rank = model_rank_by_aic(df)
    strongest = strongest_univariate(df)
    ecology_best_lopo = lopo_rank[0] == "ecology_multivariate"
    lat_strongest_r = strongest == "latitude_only"
    aic_prefers_lat_over_ecology = (
        aic_rank.index("latitude_only") < aic_rank.index("ecology_multivariate")
    )
    return {
        "ecology_best_lopo": ecology_best_lopo,
        "lat_strongest_r": lat_strongest_r,
        "mismatch_lat_r_but_ecology_lopo": lat_strongest_r and ecology_best_lopo,
        "aic_prefers_lat_over_ecology": aic_prefers_lat_over_ecology,
        "mismatch_aic_lat_but_ecology_lopo": aic_prefers_lat_over_ecology and ecology_best_lopo,
    }


def plot_mismatch_rates(summary: dict) -> Path:
    labels = [
        "Latitude strongest $|r|$,\necology best LOPO",
        "Ecology best LOPO",
    ]
    rates = [
        summary["rate_lat_r_mismatch"] * 100,
        summary["rate_ecology_best_lopo"] * 100,
    ]
    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    bars = ax.bar(labels, rates, color=["#d73027", "#1b7837"], edgecolor="k", linewidth=0.6)
    for bar, val in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.2, f"{val:.1f}%", ha="center", fontsize=10)
    ax.set_ylabel("Frequency across simulations (%)")
    ax.set_ylim(0, max(rates) * 1.25)
    ax.set_title(
        f"Gradient confounding: in-sample vs LOPO model rank\n"
        f"({summary['n_replicates']} replicates, $n={summary['n_populations']}$ populations)"
    )
    fig.tight_layout()
    out = FIG / "simulation_lopo_mismatch_rates.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def plot_aic_lopo_example(rng: np.random.Generator) -> Path:
    """Single-replicate bar chart: AIC vs LOPO ranks (illustrative)."""
    df = simulate_population_table(N_POP, rng)
    names = list(MODELS.keys())
    labels = ["Latitude", "Temperature", "Ecology", "Temp + ecology"]
    aic = {n: in_sample_aic(df, feats)["aic"] for n, feats in MODELS.items()}
    lopo = {n: fast_lopo_rmse(df, feats) for n, feats in MODELS.items()}

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), sharey=False)
    axes[0].barh(labels, [aic[n] for n in names], color="#756bb1", edgecolor="k")
    axes[0].set_xlabel("In-sample AIC (lower better)")
    axes[0].set_title("In-sample fit")
    axes[0].invert_xaxis()

    axes[1].barh(labels, [lopo[n] for n in names], color="#1b7837", edgecolor="k")
    axes[1].set_xlabel("LOPO RMSE (lower better)")
    axes[1].set_title("Held-out populations")
    fig.suptitle("Semi-synthetic cline: AIC vs LOPO ranking")
    fig.tight_layout()
    out = FIG / "simulation_aic_vs_lopo_example.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def main() -> None:
    rows = [run_replicate(RNG) for _ in range(N_REPS)]
    rep_df = pd.DataFrame(rows)

    summary = {
        "n_replicates": N_REPS,
        "n_populations": N_POP,
        "generating_process": (
            "pc1 ~ seedsize + moist_pc1 + season_pc1 + noise; "
            "predictors correlated with latitude; temperature weakly correlated with latitude"
        ),
        "rate_ecology_best_lopo": float(rep_df["ecology_best_lopo"].mean()),
        "rate_lat_strongest_r": float(rep_df["lat_strongest_r"].mean()),
        "rate_lat_r_mismatch": float(rep_df["mismatch_lat_r_but_ecology_lopo"].mean()),
        "rate_aic_lat_mismatch": float(rep_df["mismatch_aic_lat_but_ecology_lopo"].mean()),
        "rate_aic_prefers_lat_over_ecology": float(rep_df["aic_prefers_lat_over_ecology"].mean()),
        "volume_ii_claim": "Proposition 3--4 (gradient confounding / rank reversal)",
        "project_50_source": "scripts/08_lopo_simulation.py",
    }

    out_json = TAB / "simulation_lopo_mismatch.json"
    out_json.write_text(json.dumps(summary, indent=2))
    fig1 = plot_mismatch_rates(summary)
    fig2 = plot_aic_lopo_example(RNG)

    print(json.dumps(summary, indent=2))
    print(f"Wrote {out_json}")
    print(f"Wrote {fig1}")
    print(f"Wrote {fig2}")


if __name__ == "__main__":
    main()
