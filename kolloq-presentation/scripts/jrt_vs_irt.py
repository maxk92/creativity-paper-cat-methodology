"""IRT with a binary item versus JRT with a rater and seven ordered categories.

Left panel: one item characteristic curve (one difficulty, one slope).
Right panel: the six cumulative curves P(X >= k) of one hypothetical rater under the
graded response model (one slope, six thresholds), with the category probabilities faint.

Writes img/jrt_vs_irt.{svg,png}. Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/jrt_vs_irt.py
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
NAVY = "#002855"
BLUE = "#619CFF"
ORANGE = "#E69F00"
GREY = "#9aa3ad"
CMAP = plt.get_cmap("viridis", 7)


def main():
    theta = np.linspace(-4, 4, 400)
    a, b = 1.8, 0.0
    thresholds = np.array([-2.2, -1.2, -0.3, 0.6, 1.5, 2.6])
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.6), sharey=True)

    ax = axes[0]
    ax.plot(theta, 1 / (1 + np.exp(-a * (theta - b))), color=BLUE, lw=2.8)
    ax.axvline(b, color=ORANGE, lw=1.2, ls=":")
    ax.axhline(0.5, color=GREY, lw=0.8, ls=":")
    ax.text(b + 0.15, 0.08, "difficulty b", color=ORANGE, fontsize=10)
    ax.set_title("IRT: a binary item\none curve, P(solved | θ)", fontsize=11, color=NAVY)
    ax.set_xlabel("latent trait θ (ability)")
    ax.set_ylabel("Probability")

    ax = axes[1]
    p_ge = 1 / (1 + np.exp(-a * (theta[:, None] - thresholds[None, :])))
    full = np.hstack([np.ones((len(theta), 1)), p_ge, np.zeros((len(theta), 1))])
    p_k = full[:, :-1] - full[:, 1:]
    for k in range(7):
        ax.plot(theta, p_k[:, k], color=CMAP(k), lw=1.2, alpha=0.35)
    for j, t in enumerate(thresholds):
        ax.plot(theta, p_ge[:, j], color=CMAP(j + 1), lw=2.4, label=f"P(X ≥ {j + 2})")
        ax.axvline(t, color=ORANGE, lw=0.9, ls=":")
    ax.axhline(0.5, color=GREY, lw=0.8, ls=":")
    ax.text(thresholds[0] - 0.1, 0.08, "thresholds b₂ … b₇", color=ORANGE, fontsize=10, ha="left")
    ax.set_title("JRT: a rater with a 1–7 scale\nsix cumulative curves P(rating ≥ k | θ), one slope", fontsize=11, color=NAVY)
    ax.set_xlabel("latent trait θ (creativity of the action)")
    ax.legend(fontsize=8, loc="center right", frameon=False, bbox_to_anchor=(1.02, 0.55))

    for ax in axes:
        ax.set_ylim(0, 1)
        ax.grid(color="#e6ecfa")
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    fig.text(0.5, 0.005, "Same model family: the binary item has one threshold, the rater has six. Faint curves: probability of each single rating.",
             ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(IMG / "jrt_vs_irt.svg")
    fig.savefig(IMG / "jrt_vs_irt.png", dpi=200)
    print("wrote jrt_vs_irt")


if __name__ == "__main__":
    main()
