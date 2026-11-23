"""Rating distributions of the four raters behind the two example actions.

Writes to img/:
  rater_hist_bale.{svg,png}         R19 and R02: share of ratings per category, given rating highlighted
  rater_hist_danilo.{svg,png}       R01 and R06: same
  category_usage_highlight.{svg,png} all retained raters (as notebook fig-category-usage-shares), four raters highlighted
  category_usage_zoom.{svg,png}     the four raters only, with n, mean and median
and scripts/example_rater_percentiles.csv (where each given rating sits in its rater's distribution).

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/rater_distributions.py
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
GREY = "#c3c9d1"

# action -> [(rater, given rating)]
EXAMPLES = {
    "bale": {"label": "Dribble A (Bale)", "marker": "●", "colour": NAVY, "raters": [("R19", 6), ("R02", 5)]},
    "danilo": {"label": "Dribble B (Danilo)", "marker": "■", "colour": ORANGE, "raters": [("R01", 3), ("R06", 4)]},
}
CATS = np.arange(1, 8)


def load():
    wide = pd.read_csv(RES / "data" / "ratings_wide.csv").set_index("product_id") + 1  # internal 0-6 -> 1-7
    cu = pd.read_csv(RES / "supplement" / "category_usage.csv")
    summ = pd.read_csv(RES / "main" / "design_summary_raters.csv").set_index("rater_id")
    return wide, cu, summ


def shares(wide, rid):
    col = wide[rid].dropna().astype(int)
    return np.array([(col == k).mean() for k in CATS]), col


def ordinal(n):
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def percentile_rank(col, value):
    """Mid-rank percentile of `value` within the rater's own ratings."""
    return ((col < value).mean() + 0.5 * (col == value).mean()) * 100


def hist_pair(wide, key, rows):
    spec = EXAMPLES[key]
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.6), sharey=True)
    for ax, (rid, given) in zip(axes, spec["raters"]):
        sh, col = shares(wide, rid)
        pr = percentile_rank(col, given)
        colours = [BLUE if k == given else GREY for k in CATS]
        ax.bar(CATS, sh, color=colours, edgecolor=NAVY, linewidth=0.6)
        ax.set_xticks(CATS)
        ax.set_title(f"{rid}  (n = {len(col)})", fontsize=11, color=NAVY)
        ax.annotate(f"given: {given}\n{ordinal(round(pr))} percentile\nof {rid}'s ratings", xy=(given, sh[given - 1]),
                    xytext=(0.97, 0.95), textcoords="axes fraction", ha="right", va="top", fontsize=9, color=NAVY,
                    arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.8))
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
        ax.set_ylim(0, max(0.62, sh.max() * 1.15))
        ax.grid(axis="y", color="#e6ecfa")
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        rows.append(dict(action=key, rater=rid, given=given, n=len(col), percentile=round(pr, 1),
                         mean=round(col.mean(), 2), median=col.median(),
                         share_at_or_below=round((col <= given).mean(), 3)))
    axes[0].set_ylabel("Share of the rater's ratings")
    fig.supxlabel("Rating category", fontsize=10, y=0.02)
    fig.tight_layout()
    fig.savefig(IMG / f"rater_hist_{key}.svg")
    fig.savefig(IMG / f"rater_hist_{key}.png", dpi=200)
    print("wrote rater_hist_" + key)


def usage_matrix(cu, summ):
    cc = [f"cat_{i}" for i in range(1, 8)]
    cu = cu.merge(summ[["mean", "median"]], left_on="rater_id", right_index=True).sort_values("mean", ascending=False)
    sh = cu[cc].div(cu[cc].sum(axis=1), axis=0).to_numpy()
    return cu.reset_index(drop=True), cc, sh


def stacked_bars(ax, cu, cc, sh, focus, height=0.78, label_fs=7.5):
    cm = plt.get_cmap("viridis_r")
    y = np.arange(len(cu))
    left = np.zeros(len(cu))
    is_focus = cu["rater_id"].isin(focus).to_numpy()
    for j in range(7):
        for mask, alpha in ((is_focus, 1.0), (~is_focus, 0.22)):
            ax.barh(y[mask], sh[mask, j], left=left[mask], color=cm(0.08 + 0.84 * j / 6), height=height,
                    edgecolor="white", lw=0.3, alpha=alpha)
        left += sh[:, j]
    for i, (_, r) in enumerate(cu.iterrows()):
        un = ",".join(str(j + 1) for j in range(7) if r[cc[j]] == 0)
        txt = f"n={int(r['n_ratings'])}" + (f"  unused: {un}" if un else "")
        ax.text(1.01, i, txt, va="center", fontsize=label_fs,
                color="#222222" if r["rater_id"] in focus else "#999999")
    ax.set_yticks(y, cu["rater_id"], fontsize=8)
    ax.set_xlim(0, 1)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xlabel("Share of ratings")
    ax.grid(False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


def focus_map():
    return {rid: spec for spec in EXAMPLES.values() for rid, _ in spec["raters"]}


def usage_highlight(cu, summ):
    cu, cc, sh = usage_matrix(cu, summ)
    fm = focus_map()
    fig, ax = plt.subplots(figsize=(7, 5.2))
    stacked_bars(ax, cu, cc, sh, set(fm))
    for lab in ax.get_yticklabels():
        rid = lab.get_text()
        if rid in fm:
            lab.set_fontweight("bold")
            lab.set_color(fm[rid]["colour"])
            lab.set_fontsize(9.5)
    for i, rid in enumerate(cu["rater_id"]):
        if rid in fm:
            ax.text(-0.075, i, fm[rid]["marker"], ha="right", va="center",
                    color=fm[rid]["colour"], fontsize=9, transform=ax.get_yaxis_transform())
    handles = [plt.Line2D([], [], marker="o", color=NAVY, linestyle="", label="rated dribble A (Bale)"),
               plt.Line2D([], [], marker="s", color=ORANGE, linestyle="", label="rated dribble B (Danilo)")]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.995), ncol=2, fontsize=8.5,
               frameon=False)
    cm = plt.get_cmap("viridis_r")
    cat_handles = [plt.Rectangle((0, 0), 1, 1, color=cm(0.08 + 0.84 * j / 6)) for j in range(7)]
    ax.legend(cat_handles, [str(j + 1) for j in range(7)], title="Category", ncol=7, loc="upper center",
              bbox_to_anchor=(0.5, -0.1), fontsize=8, title_fontsize=8)
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    fig.savefig(IMG / "category_usage_highlight.svg")
    fig.savefig(IMG / "category_usage_highlight.png", dpi=200)
    print("wrote category_usage_highlight")


def usage_plain(cu, summ):
    """Same layout as usage_highlight, all raters at full colour, no markers (first step of the animation)."""
    cu, cc, sh = usage_matrix(cu, summ)
    fig, ax = plt.subplots(figsize=(7, 5.2))
    stacked_bars(ax, cu, cc, sh, set(cu["rater_id"]))
    for lab in ax.get_yticklabels():
        lab.set_fontsize(9.5)
    cm = plt.get_cmap("viridis_r")
    cat_handles = [plt.Rectangle((0, 0), 1, 1, color=cm(0.08 + 0.84 * j / 6)) for j in range(7)]
    ax.legend(cat_handles, [str(j + 1) for j in range(7)], title="Category", ncol=7, loc="upper center",
              bbox_to_anchor=(0.5, -0.1), fontsize=8, title_fontsize=8)
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    fig.savefig(IMG / "category_usage_plain.svg")
    fig.savefig(IMG / "category_usage_plain.png", dpi=200)
    print("wrote category_usage_plain")


def usage_zoom(cu, summ):
    cu, cc, sh = usage_matrix(cu, summ)
    fm = focus_map()
    order = [rid for spec in EXAMPLES.values() for rid, _ in spec["raters"]]  # R02 R19 | R01 R06
    idx = [int(cu.index[cu["rater_id"] == r][0]) for r in order]
    sub = cu.loc[idx].reset_index(drop=True)
    subsh = sh[idx]
    cm = plt.get_cmap("viridis_r")
    fig, ax = plt.subplots(figsize=(7.2, 3.1))
    ypos = np.array([3.3, 2.3, 0.9, -0.1])  # gap between the two actions
    left = np.zeros(4)
    for j in range(7):
        ax.barh(ypos, subsh[:, j], left=left, color=cm(0.08 + 0.84 * j / 6), height=0.8, edgecolor="white", lw=0.4)
        left += subsh[:, j]
    for yi, (_, r) in zip(ypos, sub.iterrows()):
        rid = r["rater_id"]
        ax.text(1.01, yi, f"n = {int(r['n_ratings'])}   mean {r['mean']:.2f}   median {r['median']:.0f}",
                va="center", fontsize=9, color="#222222")
    ax.set_yticks(ypos, [f"{fm[r]['marker']} {r}" for r in order], fontsize=10)
    for lab, rid in zip(ax.get_yticklabels(), order):
        lab.set_color(fm[rid]["colour"])
        lab.set_fontweight("bold")
    ax.text(-0.24, 2.8, "Dribble A\n(Bale)", rotation=90, va="center", ha="center", color=NAVY, fontsize=9,
            transform=ax.get_yaxis_transform())
    ax.text(-0.24, 0.4, "Dribble B\n(Danilo)", rotation=90, va="center", ha="center", color=ORANGE, fontsize=9,
            transform=ax.get_yaxis_transform())
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.7, 3.9)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xlabel("Share of ratings")
    ax.grid(False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    cat_handles = [plt.Rectangle((0, 0), 1, 1, color=cm(0.08 + 0.84 * j / 6)) for j in range(7)]
    ax.legend(cat_handles, [str(j + 1) for j in range(7)], title="Category", ncol=7, loc="upper center",
              bbox_to_anchor=(0.5, -0.22), fontsize=8, title_fontsize=8)
    fig.tight_layout()
    fig.subplots_adjust(left=0.2)
    fig.savefig(IMG / "category_usage_zoom.svg")
    fig.savefig(IMG / "category_usage_zoom.png", dpi=200)
    print("wrote category_usage_zoom")


def main():
    wide, cu, summ = load()
    rows = []
    hist_pair(wide, "bale", rows)
    hist_pair(wide, "danilo", rows)
    df = pd.DataFrame(rows)
    df.to_csv(HERE / "example_rater_percentiles.csv", index=False)
    print(df.to_string(index=False))
    usage_plain(cu, summ)
    usage_highlight(cu, summ)
    usage_zoom(cu, summ)


if __name__ == "__main__":
    main()
