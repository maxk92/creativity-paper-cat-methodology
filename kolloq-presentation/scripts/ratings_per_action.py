"""Distribution of the number of ratings per action, from the current product scores.

Reads results/supplement/product_scores.csv (column n_ratings) and writes
img/ratings_per_action.{svg,png}. Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/ratings_per_action.py
"""

from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
RES = HERE.parent.parent / "data-analysis" / "creativity-ratings-psychometrics" / "results"
NAVY = "#002855"
BLUE = "#619CFF"


def main():
    scores = pd.read_csv(RES / "supplement" / "product_scores.csv")
    n_raters = len(pd.read_csv(RES / "data" / "ratings_wide.csv", nrows=1).columns) - 1
    counts = scores["n_ratings"].value_counts().sort_index()
    print(counts.to_dict(), "total", int(counts.sum()), "ratings", int((counts.index * counts).sum()))
    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ax.bar(counts.index, counts.values, color=BLUE, edgecolor=NAVY, linewidth=0.6)
    for k, v in counts.items():
        ax.text(k, v + counts.max() * 0.015, f"{v:,}", ha="center", va="bottom", fontsize=8.5, color=NAVY)
    ax.set_xticks(counts.index)
    ax.set_xlabel("Ratings per action")
    ax.set_ylabel("Actions")
    ax.set_ylim(0, counts.max() * 1.15)
    ax.grid(axis="y", color="#e6ecfa")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_title(f"{int(counts.sum()):,} actions, {int((counts.index * counts).sum()):,} ratings, {n_raters} raters",
                 fontsize=11, color=NAVY)
    fig.tight_layout()
    fig.savefig(IMG / "ratings_per_action.svg")
    fig.savefig(IMG / "ratings_per_action.png", dpi=200)
    print("wrote ratings_per_action")


if __name__ == "__main__":
    main()
