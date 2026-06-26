#!/usr/bin/env python3
"""
Figure 2 composite for Volume II: *Stator limbatus* empirical validation.

Panel A: in-sample |r| vs LOPO RMSE rank reversal (2007 survey, n=93).
Panel B: estimand mismatch — individual 10-fold vs LOPO (ecology vs temperature).

Numbers from Project 50 outputs/tables (2007_proxy_trap_cv.json,
cv_unit_comparison.json); embedded here for standalone Project 55 builds.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "outputs" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

# Matched ecology-complete populations (n = 93)
MODELS = ["Latitude", "Temperature", "Ecology\nmultivariate"]
ABS_R = [0.416, 0.219, np.nan]
LOPO_RMSE = [0.106, 0.112, 0.104]
COLORS = ["#92c5de", "#f4a582", "#1b7837"]

CV_SCHEMES = ["10-fold\nindividual", "LOPO\npopulation"]
ECO_RMSE = [0.150, 0.104]
TEMP_RMSE = [0.158, 0.112]


def panel_proxy_vs_lopo(ax_left, ax_right) -> None:
    """Dual ranking: strongest in-sample correlate vs best LOPO model."""
    # Left: univariate |r| (ecology is multivariate — not comparable)
    uni_labels = ["Latitude", "Temperature"]
    uni_r = [ABS_R[0], ABS_R[1]]
    bars = ax_left.bar(
        uni_labels,
        uni_r,
        color=COLORS[:2],
        edgecolor="k",
        linewidth=0.6,
        width=0.55,
    )
    bars[0].set_edgecolor("#2166ac")
    bars[0].set_linewidth(2.0)
    ax_left.set_ylabel("In-sample $|r|$ with body-size PC1")
    ax_left.set_ylim(0, 0.48)
    ax_left.set_title("In-sample correlate\n(strongest: latitude)", fontsize=10)
    for bar, val in zip(bars, uni_r):
        ax_left.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.012,
            f"{val:.3f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )
    ax_left.text(
        0.5,
        -0.22,
        "Ecology multivariate: no single $|r|$",
        transform=ax_left.transAxes,
        ha="center",
        fontsize=7.5,
        style="italic",
    )

    # Right: LOPO RMSE (all three models)
    bars = ax_right.bar(
        MODELS,
        LOPO_RMSE,
        color=COLORS,
        edgecolor="k",
        linewidth=0.6,
        width=0.55,
    )
    best_idx = int(np.argmin(LOPO_RMSE))
    bars[best_idx].set_edgecolor("#1b7837")
    bars[best_idx].set_linewidth(2.5)
    ax_right.set_ylabel("LOPO RMSE")
    ax_right.set_ylim(0, 0.13)
    ax_right.set_title("Held-out population means\n(best: ecology)", fontsize=10)
    for bar, val in zip(bars, LOPO_RMSE):
        ax_right.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.002,
            f"{val:.3f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )


def panel_cv_unit(ax) -> None:
    x = np.arange(len(CV_SCHEMES))
    width = 0.35
    ax.bar(
        x - width / 2,
        TEMP_RMSE,
        width,
        label="Temperature only",
        color="#f4a582",
        edgecolor="k",
        linewidth=0.6,
    )
    ax.bar(
        x + width / 2,
        ECO_RMSE,
        width,
        label="Ecology multivariate",
        color="#1b7837",
        edgecolor="k",
        linewidth=0.6,
    )
    ax.set_xticks(x)
    ax.set_xticklabels(CV_SCHEMES)
    ax.set_ylabel("Cross-validated RMSE")
    ax.set_ylim(0, 0.18)
    ax.set_title(
        "Estimand mismatch\n(ecology RMSE +45% under individual $k$-fold)",
        fontsize=10,
    )
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    for i, (t, e) in enumerate(zip(TEMP_RMSE, ECO_RMSE)):
        ax.text(i - width / 2, t + 0.004, f"{t:.3f}", ha="center", fontsize=7.5)
        ax.text(i + width / 2, e + 0.004, f"{e:.3f}", ha="center", fontsize=7.5)


def main() -> None:
    fig = plt.figure(figsize=(7.2, 3.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 0.85], wspace=0.38)

    gs_a = gs[0].subgridspec(1, 2, wspace=0.35)
    ax_a1 = fig.add_subplot(gs_a[0, 0])
    ax_a2 = fig.add_subplot(gs_a[0, 1])
    panel_proxy_vs_lopo(ax_a1, ax_a2)

    ax_b = fig.add_subplot(gs[1])
    panel_cv_unit(ax_b)

    ax_a1.text(
        0.5,
        -0.30,
        "A. Proxy vs holdout ranking ($n=93$)",
        transform=ax_a1.transAxes,
        ha="center",
        fontsize=10,
    )
    ax_b.text(
        0.5,
        -0.22,
        "B. Cross-validation unit",
        transform=ax_b.transAxes,
        ha="center",
        fontsize=10,
    )

    fig.suptitle(
        "Stator limbatus geographic cline (Stillwell et al. 2007)",
        fontsize=11,
        y=1.02,
    )
    out = FIG / "stator_empirical_summary_composite.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
