#!/usr/bin/env python3
"""
Figure 2 composite for Volume II: *Stator limbatus* empirical validation.

Panel A: in-sample |r| vs LOPO RMSE rank reversal (2007 survey, n=93).
Panel B: estimand mismatch — individual 10-fold vs LOPO (ecology vs temperature).
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

LOPO_MODELS = ["Latitude", "Temperature", "Ecology"]
LOPO_RMSE = [0.106, 0.112, 0.104]
UNI_MODELS = ["Latitude", "Temperature"]
UNI_R = [0.416, 0.219]
COLORS = ["#92c5de", "#f4a582", "#1b7837"]

CV_SCHEMES = ["10-fold individual", "LOPO population"]
ECO_RMSE = [0.150, 0.104]
TEMP_RMSE = [0.158, 0.112]


def _style_axes(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", which="major", labelsize=9, pad=3)


def panel_a_insample(ax) -> None:
    y = np.arange(len(UNI_MODELS))
    bars = ax.barh(
        y,
        UNI_R,
        color=COLORS[:2],
        edgecolor="k",
        linewidth=0.6,
        height=0.55,
    )
    bars[0].set_edgecolor("#2166ac")
    bars[0].set_linewidth(2.0)
    ax.set_yticks(y)
    ax.set_yticklabels(UNI_MODELS)
    ax.set_xlim(0, 0.48)
    ax.set_title("In-sample correlate (strongest: latitude)", fontsize=10, pad=8)
    ax.set_xlabel("In-sample $|r|$ with PC1", labelpad=8)
    ax.invert_yaxis()
    for bar, val in zip(bars, UNI_R):
        ax.text(val + 0.012, bar.get_y() + bar.get_height() / 2, f"{val:.3f}", va="center", fontsize=8)
    _style_axes(ax)


def panel_a_lopo(ax) -> None:
    y = np.arange(len(LOPO_MODELS))
    bars = ax.barh(
        y,
        LOPO_RMSE,
        color=COLORS,
        edgecolor="k",
        linewidth=0.6,
        height=0.55,
    )
    best_idx = int(np.argmin(LOPO_RMSE))
    bars[best_idx].set_edgecolor("#1b7837")
    bars[best_idx].set_linewidth(2.5)
    ax.set_yticks(y)
    ax.set_yticklabels(LOPO_MODELS)
    ax.set_xlim(0, 0.13)
    ax.set_title("Held-out population means (best: ecology)", fontsize=10, pad=8)
    ax.set_xlabel("LOPO RMSE", labelpad=8)
    ax.invert_yaxis()
    for bar, val in zip(bars, LOPO_RMSE):
        ax.text(val + 0.002, bar.get_y() + bar.get_height() / 2, f"{val:.3f}", va="center", fontsize=8)
    _style_axes(ax)


def panel_b_cv(ax) -> None:
    x = np.arange(len(CV_SCHEMES))
    width = 0.34
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
    ax.set_ylabel("Cross-validated RMSE", labelpad=10)
    ax.set_ylim(0, 0.19)
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    for i, (t, e) in enumerate(zip(TEMP_RMSE, ECO_RMSE)):
        ax.text(i - width / 2, t + 0.005, f"{t:.3f}", ha="center", va="bottom", fontsize=7.5)
        ax.text(i + width / 2, e + 0.005, f"{e:.3f}", ha="center", va="bottom", fontsize=7.5)
    ax.tick_params(axis="x", pad=6)
    _style_axes(ax)


def _fill_spacer(fig, ax_spacer) -> None:
    """Whitespace between Panel A and Panel B: Panel B header only."""
    ax_spacer.axis("off")
    ps = ax_spacer.get_position()

    y_title = ps.y0 + 0.72 * (ps.y1 - ps.y0)
    y_subtitle = ps.y0 + 0.28 * (ps.y1 - ps.y0)

    fig.text(
        0.5,
        y_title,
        "B. Cross-validation unit",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )
    fig.text(
        0.5,
        y_subtitle,
        "Estimand mismatch (ecology RMSE +45% under individual $k$-fold)",
        ha="center",
        va="center",
        fontsize=9,
    )


def main() -> None:
    fig = plt.figure(figsize=(7.6, 7.4))
    gs = fig.add_gridspec(
        4,
        2,
        height_ratios=[0.045, 0.88, 0.16, 1.0],
        hspace=0.52,
        wspace=0.42,
        left=0.20,
        right=0.97,
        top=0.93,
        bottom=0.10,
    )

    ax_a_header = fig.add_subplot(gs[0, :])
    ax_a_header.axis("off")
    ax_a_header.text(
        0.5,
        0.5,
        "A. Proxy vs holdout ranking ($n=93$)",
        ha="center",
        va="center",
        fontsize=10,
        transform=ax_a_header.transAxes,
    )

    ax_a1 = fig.add_subplot(gs[1, 0])
    ax_a2 = fig.add_subplot(gs[1, 1])
    ax_spacer = fig.add_subplot(gs[2, :])
    ax_b = fig.add_subplot(gs[3, :])

    panel_a_insample(ax_a1)
    panel_a_lopo(ax_a2)
    panel_b_cv(ax_b)

    fig.canvas.draw()
    _fill_spacer(fig, ax_spacer)

    fig.suptitle(
        "Stator limbatus geographic cline (Stillwell et al. 2007)",
        fontsize=11,
        y=0.98,
    )

    out = FIG / "stator_empirical_summary_composite.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
