"""Shared helpers for Volume II collinearity / LOPO simulation."""

from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm

MODELS = {
    "latitude_only": ["lat"],
    "temperature_only": ["annmeantemp"],
    "ecology_multivariate": ["seedsize", "moist_pc1", "season_pc1"],
    "temperature_plus_ecology": ["annmeantemp", "seedsize", "moist_pc1", "season_pc1"],
}


def in_sample_aic(df: pd.DataFrame, features: list[str]) -> dict:
    sub = df[["pc1_mean"] + features].dropna()
    if len(sub) < len(features) + 2:
        return {"n": len(sub), "aic": None, "r2": None}

    y = sub["pc1_mean"].values
    x = sm.add_constant(sub[features].astype(float))
    fit = sm.OLS(y, x).fit()
    return {
        "n": int(len(sub)),
        "aic": float(fit.aic),
        "r2": float(fit.rsquared),
        "k": int(len(features) + 1),
    }
