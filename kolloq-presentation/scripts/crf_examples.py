"""Category response functions of fitted raters (GRM parameters).

Reads results/main/rater_parameters.csv (GRM) and the M1 severities from
results/supplement/rater_parameters_by_model.csv and draws, for each rater,
the probability of each rating category as a function of the action's
creativity theta, plus the expected rating.

Writes to img/:
  crf_three_raters.{svg,png}   lenient, strict, low-discrimination rater (JRT slide)
  crf_four_raters.{svg,png}    the four raters of the two example actions (2 x 2)
  crf_all_raters.{svg,png}     all retained raters, sorted from lenient to strict (grid)

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/crf_examples.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
RES = HERE.parent.parent / "data-analysis" / "creativity-ratings-psychometrics" / "results"
NAVY = "#002855"
BLUE = "#619CFF"
ORANGE = "#E69F00"

THREE = [("R19", "most lenient"), ("R06", "most strict"), ("R18", "lowest discrimination")]
# (rater, action label, marker colour) in reading order of a 2 x 2 grid
FOUR = [
    ("R19", "Dribble A (Bale)", NAVY),
    ("R02", "Dribble A (Bale)", NAVY),
    ("R01", "Dribble B (Danilo)", ORANGE),
    ("R06", "Dribble B (Danilo)", ORANGE),
]
CMAP = plt.get_cmap("viridis", 7)
BCOLS = [f"b{k}" for k in range(1, 7)]


def used_categories(boundaries):
    """'1|2;2|3;3|4;4|6' -> [1, 2, 3, 4, 6]: the categories the rater actually used."""
    pairs = [tuple(int(x) for x in p.split("|")) for p in boundaries.split(";")]
    return [p[0] for p in pairs] + [pairs[-1][1]]


def grm_probs(theta, a, b):
    """Return P(X = k) for the K used categories (columns in increasing category order)."""
    b = np.asarray([x for x in b if pd.notna(x)], dtype=float)
    p_ge = 1.0 / (1.0 + np.exp(-a * (theta[:, None] - b[None, :])))  # P(X >= k+1)
    p_ge = np.hstack([np.ones((len(theta), 1)), p_ge, np.zeros((len(theta), 1))])
    return p_ge[:, :-1] - p_ge[:, 1:]


def load():
    params = pd.read_csv(RES / "main" / "rater_parameters.csv").set_index("rater_id")
    sev = pd.read_csv(RES / "supplement" / "rater_parameters_by_model.csv")
    sev = sev[(sev.model == "M1_RSM") & (sev.parameter == "b_rater")].set_index("rater_id")["estimate"]
    return params, sev


def draw_rater(ax, rid, params, theta, show_exp_ticks, lw=2, exp_lw=1.6):
    """Draw category curves and expected rating of one rater; return (handles, labels)."""
    a = params.loc[rid, "a"]
    cats = used_categories(params.loc[rid, "category_boundaries"])
    P = grm_probs(theta, a, params.loc[rid, BCOLS].values)
    handles, labels = [], []
    for col, cat in enumerate(cats):
        (h,) = ax.plot(theta, P[:, col], color=CMAP(cat - 1), linewidth=lw, label=str(cat))
        handles.append(h)
        labels.append(str(cat))
    exp_r = (P * np.asarray(cats)[None, :]).sum(axis=1)
    ax2 = ax.twinx()
    ax2.plot(theta, exp_r, color=NAVY, linestyle="--", linewidth=exp_lw)
    ax2.set_ylim(1, 7)
    ax2.set_yticks(range(1, 8) if show_exp_ticks else [])
    ax.set_ylim(0, 1)
    ax.grid(color="#e6ecfa")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
        ax2.spines[sp].set_visible(False)
    return ax2, handles, labels


def legend_7(fig, y=1.02, fontsize=9):
    handles = [plt.Line2D([], [], color=CMAP(k), linewidth=2) for k in range(7)]
    fig.legend(handles, [str(k + 1) for k in range(7)], title="Rating", loc="upper center",
               ncol=7, frameon=False, bbox_to_anchor=(0.5, y), fontsize=fontsize, title_fontsize=fontsize)


def three_raters(params, theta):
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.9), sharey=True)
    for ax, (rid, desc) in zip(axes, THREE):
        ax2, _, _ = draw_rater(ax, rid, params, theta, show_exp_ticks=ax is axes[-1])
        if ax is axes[-1]:
            ax2.set_ylabel("Expected rating (dashed)", color=NAVY)
        ax.set_title(f"{rid}: {desc}\n(a = {params.loc[rid, 'a']:.2f})", fontsize=11, color=NAVY)
        ax.set_xlabel("Creativity of the action (θ)")
    axes[0].set_ylabel("P(rating category)")
    legend_7(fig)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(IMG / "crf_three_raters.svg")
    fig.savefig(IMG / "crf_three_raters.png", dpi=200)
    print("wrote crf_three_raters")


def four_raters(params, sev, theta):
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.6), sharex=True)
    axes = axes.ravel()
    for i, (ax, (rid, action, col)) in enumerate(zip(axes, FOUR)):
        right = i % 2 == 1
        ax2, _, _ = draw_rater(ax, rid, params, theta, show_exp_ticks=right)
        if right:
            ax2.set_ylabel("Expected rating (dashed)", color=NAVY, fontsize=10)
        marker = "●" if "Bale" in action else "■"
        ax.set_title(f"{marker} {action}: {rid}\na = {params.loc[rid, 'a']:.2f}   severity (M1) = {sev[rid]:+.2f}",
                     fontsize=11, color=col)
        if i >= 2:
            ax.set_xlabel("Creativity of the action (θ)")
        if not right:
            ax.set_ylabel("P(rating category)")
    legend_7(fig, y=1.0)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(IMG / "crf_four_raters.svg")
    fig.savefig(IMG / "crf_four_raters.png", dpi=200)
    print("wrote crf_four_raters")


def all_raters(params, sev, theta):
    order = sev.sort_values().index.tolist()  # lenient -> strict
    ncol = 6 if len(order) % 6 == 0 else 5  # 24 raters -> 4 x 6, 25 raters -> 5 x 5
    nrow = -(-len(order) // ncol)
    fig, axes = plt.subplots(nrow, ncol, figsize=(16, 9), sharex=True, sharey=True)
    for i, (ax, rid) in enumerate(zip(axes.ravel(), order)):
        r, c = divmod(i, ncol)
        ax2, _, _ = draw_rater(ax, rid, params, theta, show_exp_ticks=c == ncol - 1, lw=1.5, exp_lw=1.2)
        ax2.tick_params(labelsize=8)
        ax.set_title(f"{rid}   a = {params.loc[rid, 'a']:.2f}   sev = {sev[rid]:+.2f}", fontsize=9.5, color=NAVY)
        ax.tick_params(labelsize=8)
        if r == nrow - 1 or i + ncol >= len(order):
            ax.set_xlabel("θ", fontsize=9)
        if c == 0:
            ax.set_ylabel("P(category)", fontsize=9)
    for ax in axes.ravel()[len(order):]:
        ax.set_visible(False)
    legend_7(fig, y=1.0, fontsize=10)
    fig.text(0.5, 0.005, "Raters sorted from most lenient (top left) to most strict (bottom right), M1 severity. "
             "Dashed: expected rating (right axis).", ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.02, 1, 0.96))
    fig.savefig(IMG / "crf_all_raters.svg")
    fig.savefig(IMG / "crf_all_raters.png", dpi=170)
    print("wrote crf_all_raters")


def main():
    params, sev = load()
    theta = np.linspace(-4, 4, 400)
    three_raters(params, theta)
    four_raters(params, sev, theta)
    all_raters(params, sev, theta)


if __name__ == "__main__":
    main()
