"""Four hypothetical raters under the graded response model, to show what the parameters do.

Writes img/jrt_parameter_demo.{svg,png} (category response curves and expected rating of
each rater) and scripts/jrt_parameter_demo.csv (expected rating of each rater at four
values of theta, for the table on the slide).

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/jrt_parameter_demo.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
NAVY = "#002855"
CMAP = plt.get_cmap("viridis", 7)

BASE = np.array([-2.5, -1.5, -0.5, 0.5, 1.5, 2.5])  # evenly spaced thresholds, centred at 0
RATERS = [
    ("A · reference", 2.0, BASE),
    ("B · strict (thresholds +1.5)", 2.0, BASE + 1.5),
    ("C · flat (a = 0.6)", 0.6, BASE),
    ("D · compressed thresholds", 2.0, BASE * 0.4),
]
THETAS = [-1.0, 0.0, 1.0, 2.0]


def probs(theta, a, b):
    p_ge = 1.0 / (1.0 + np.exp(-a * (theta[:, None] - b[None, :])))
    p_ge = np.hstack([np.ones((len(theta), 1)), p_ge, np.zeros((len(theta), 1))])
    return p_ge[:, :-1] - p_ge[:, 1:]


def expected(theta, a, b):
    return (probs(theta, a, b) * np.arange(1, 8)[None, :]).sum(axis=1)


def main():
    theta = np.linspace(-4, 4, 400)
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.4), sharey=True)
    for i, (ax, (name, a, b)) in enumerate(zip(axes, RATERS)):
        P = probs(theta, a, b)
        for k in range(7):
            ax.plot(theta, P[:, k], color=CMAP(k), linewidth=1.8)
        ax2 = ax.twinx()
        ax2.plot(theta, expected(theta, a, b), color=NAVY, linestyle="--", linewidth=1.6)
        ax2.set_ylim(1, 7)
        ax2.set_yticks(range(1, 8) if i == 3 else [])
        if i == 3:
            ax2.set_ylabel("Expected rating (dashed)", color=NAVY, fontsize=10)
        for t in THETAS:
            ax.axvline(t, color="#9aa3ad", lw=0.8, ls=":")
        bt = ", ".join(f"{x:+.1f}" for x in b)
        ax.set_title(f"{name}\na = {a:.1f}   b = ({bt})", fontsize=9.5, color=NAVY)
        ax.set_xlabel("θ (creativity of the action)", fontsize=10)
        ax.set_ylim(0, 1)
        ax.tick_params(labelsize=9)
        ax.grid(color="#e6ecfa")
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
            ax2.spines[sp].set_visible(False)
    axes[0].set_ylabel("P(rating category)")
    handles = [plt.Line2D([], [], color=CMAP(k), linewidth=2) for k in range(7)]
    fig.legend(handles, [str(k + 1) for k in range(7)], title="Rating", loc="upper center", ncol=7,
               frameon=False, bbox_to_anchor=(0.5, 1.04), fontsize=9, title_fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.9))
    fig.savefig(IMG / "jrt_parameter_demo.svg")
    fig.savefig(IMG / "jrt_parameter_demo.png", dpi=200)

    rows = []
    for name, a, b in RATERS:
        e = expected(np.array(THETAS), a, b)
        rows.append({"rater": name, **{f"theta={t:+.0f}": round(v, 2) for t, v in zip(THETAS, e)}})
    df = pd.DataFrame(rows)
    df.to_csv(HERE / "jrt_parameter_demo.csv", index=False)
    print(df.to_string(index=False))
    print("wrote jrt_parameter_demo")


if __name__ == "__main__":
    main()
