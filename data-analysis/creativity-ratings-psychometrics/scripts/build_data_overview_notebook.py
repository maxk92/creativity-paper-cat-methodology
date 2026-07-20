"""Builds notebooks/01_data_overview.ipynb from cell contents.

This script is run once to generate the notebook. Afterwards the notebook
itself is executed with `jupyter nbconvert --execute`. Changes to the
notebook content are made here in this script (not directly in the .ipynb
JSON file).
"""
import nbformat as nbf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "01_data_overview.ipynb"

nb = nbf.v4.new_notebook()
cells = []

def md(text):
    cells.append(nbf.v4.new_markdown_cell(text.strip("\n")))

def code(text):
    cells.append(nbf.v4.new_code_cell(text.strip("\n")))

# ====================================================================
# 0. TITLE AND CONTEXT
# ====================================================================
md(r"""
# Data Overview

A quick, non-technical look at the creativity ratings before running the
full psychometric analysis: how much data there is, how it is
distributed across actions and raters, a rough sense of how much raters
agree with each other, and how well-connected the rater-action design
currently is.

This notebook reads the preprocessed data produced by
`00_data_loading_preprocessing.ipynb` (`data/processed/ratings_long_clean.csv`).
It does not repeat or replace the formal reliability analysis in
`01_creativity_ratings_python.ipynb` / `01_creativity_ratings_R.qmd` — the
agreement figure here is a single quick estimate, not the fuller
subset/uncertainty treatment done there. The purpose of this notebook is
to inform decisions about future data collection: whether more ratings
are needed, and if so, from which raters on which actions.
""")

# ====================================================================
# 1. SETUP AND LOAD
# ====================================================================
md(r"""
## 1. Load the preprocessed data
""")

code(r"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import krippendorff

plt.rcParams["figure.dpi"] = 110
plt.rcParams["font.size"] = 10
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

PROJECT_ROOT = Path("..").resolve()
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

df = pd.read_csv(DATA_PROCESSED / "ratings_long_clean.csv")
df["action_id"] = df["action_id"].astype(str)
df["rater_id"] = df["rater_id"].astype(str)

print(f"Loaded {len(df)} ratings.")
df.head()
""")

# ====================================================================
# 2. HOW MUCH DATA
# ====================================================================
md(r"""
## 2. How much data do we have

Total number of ratings, and how many distinct actions and raters they
cover.
""")

code(r"""
n_ratings = len(df)
n_actions = df["action_id"].nunique()
n_raters = df["rater_id"].nunique()

print(f"Total ratings:   {n_ratings}")
print(f"Distinct actions: {n_actions}")
print(f"Distinct raters:  {n_raters}")
print(f"Average ratings per action: {n_ratings / n_actions:.2f}")
print(f"Average ratings per rater:  {n_ratings / n_raters:.1f}")
""")

# ====================================================================
# 3. DISTRIBUTION OF RATINGS PER ACTION AND PER RATER
# ====================================================================
md(r"""
## 3. Distribution of the number of ratings

Some actions have only one rating and contribute no within-action
agreement information; some raters have rated far more actions than
others. Both matter for how much we can trust the eventual reliability
estimates.
""")

code(r"""
ratings_per_action = df.groupby("action_id").size().rename("n_ratings")
ratings_per_rater = df.groupby("rater_id").size().rename("n_actions_rated")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
ratings_per_action.value_counts().sort_index().plot(kind="bar", ax=axes[0], color="#4C72B0")
axes[0].set_title("Number of ratings per action")
axes[0].set_xlabel("Ratings per action")
axes[0].set_ylabel("Number of actions")
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)

axes[1].hist(ratings_per_rater.values, bins=min(20, n_raters), color="#DD8452", edgecolor="white")
axes[1].set_title("Number of rated actions per rater")
axes[1].set_xlabel("Rated actions")
axes[1].set_ylabel("Number of raters")
fig.tight_layout()
plt.show()

print("Ratings per action:")
print(ratings_per_action.describe())
print(f"\nShare of actions with exactly 1 rating: {(ratings_per_action == 1).mean():.1%}")
print(f"Share of actions with exactly 2 ratings: {(ratings_per_action == 2).mean():.1%}")

print("\nRatings per rater:")
print(ratings_per_rater.sort_values())
""")

# ====================================================================
# 4. ROUGH AGREEMENT
# ====================================================================
md(r"""
## 4. Rough agreement across raters

A single overall Krippendorff's alpha (interval level), computed
directly on the full incomplete rater-action design — the coefficient
handles the unequal, incomplete overlap between raters natively, so no
subsetting is needed for a quick read. This is a rough, one-number
summary; the full analysis notebooks compute alpha with uncertainty
intervals and on relevant subsets of the data.
""")

code(r"""
reliability_matrix = (
    df.pivot_table(index="rater_id", columns="action_id", values="rating_numeric")
    .to_numpy()
)
alpha = krippendorff.alpha(reliability_data=reliability_matrix, level_of_measurement="interval")
print(f"Krippendorff's alpha (interval, rough overall estimate): {alpha:.3f}")

pairable_actions = (ratings_per_action >= 2).sum()
print(f"Actions with >=2 ratings (contributing to this estimate): {pairable_actions} "
      f"of {n_actions} ({pairable_actions / n_actions:.1%})")
""")

# ====================================================================
# 5. CONNECTIVITY OF THE RATER-ACTION DESIGN
# ====================================================================
md(r"""
## 5. Connectivity of the rater-action design

Rater severity/leniency can only be told apart from true differences
between actions if raters are linked, directly or indirectly, through
shared actions. We build the rater-action bipartite graph and check how
connected it currently is, and how much overlap each pair of raters has.
""")

code(r"""
B = nx.Graph()
B.add_nodes_from(df["action_id"].unique(), bipartite="action")
B.add_nodes_from(("R::" + df["rater_id"]).unique(), bipartite="rater")
B.add_edges_from(zip(df["action_id"], "R::" + df["rater_id"]))

components = sorted(nx.connected_components(B), key=len, reverse=True)
comp_summary = []
for i, comp in enumerate(components):
    action_nodes = [n for n in comp if not str(n).startswith("R::")]
    rater_nodes = [str(n)[3:] for n in comp if str(n).startswith("R::")]
    comp_summary.append({
        "component_id": i, "n_actions": len(action_nodes),
        "n_raters": len(rater_nodes), "raters": ", ".join(sorted(rater_nodes)),
    })
comp_summary_df = pd.DataFrame(comp_summary)
print(f"Number of connected components: {len(components)}")
comp_summary_df
""")

code(r"""
rater_ids_sorted = sorted(df["rater_id"].unique())
n = len(rater_ids_sorted)
rater_idx = {r: i for i, r in enumerate(rater_ids_sorted)}

overlap = np.zeros((n, n), dtype=int)
for raters_for_action in df.groupby("action_id")["rater_id"].apply(list):
    idxs = sorted(set(rater_idx[r] for r in raters_for_action))
    for a in range(len(idxs)):
        for b in range(a + 1, len(idxs)):
            overlap[idxs[a], idxs[b]] += 1
            overlap[idxs[b], idxs[a]] += 1

overlap_df = pd.DataFrame(overlap, index=rater_ids_sorted, columns=rater_ids_sorted)

# For each rater: overlap with their single best-connected partner.
best_partner_overlap = pd.Series(
    {r: overlap_df.loc[r].drop(r).max() for r in rater_ids_sorted},
    name="best_partner_overlap",
).sort_values()

fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(overlap, cmap="viridis")
ax.set_title("Jointly rated actions per rater pair")
ax.set_xticks(range(n)); ax.set_xticklabels(rater_ids_sorted, rotation=90, fontsize=7)
ax.set_yticks(range(n)); ax.set_yticklabels(rater_ids_sorted, fontsize=7)
fig.colorbar(im, ax=ax, shrink=0.8, label="joint actions")
fig.tight_layout()
plt.show()

print("Best-connected-partner overlap per rater (lower = more isolated):")
print(best_partner_overlap)
""")

# ====================================================================
# 6. RECOMMENDATIONS
# ====================================================================
md(r"""
## 6. Recommendations for future rater-action assignment

Grounded in the numbers computed above. A commonly used rule of thumb
for this kind of design is at least 15-20 shared actions between a rater
and at least one well-connected "bridge" rater, so that relative rater
strictness can be calibrated; actions rated by (nearly) all raters
("anchor actions") further stabilize this.
""")

code(r"""
OVERLAP_TARGET = 15

recommendations = []

if len(components) > 1:
    recommendations.append(
        f"The rater-action graph currently has {len(components)} disconnected "
        "components. Raters in different components cannot be compared on the "
        "same severity scale at all. Priority: assign at least a few shared "
        "actions between the largest component and each of the others."
    )

low_overlap_raters = best_partner_overlap[best_partner_overlap < OVERLAP_TARGET]
if len(low_overlap_raters) > 0:
    recommendations.append(
        f"{len(low_overlap_raters)} of {n_raters} raters have fewer than "
        f"{OVERLAP_TARGET} shared actions with their best-connected partner: "
        f"{', '.join(low_overlap_raters.index)}. Assigning more overlapping "
        "actions between these raters and the rest of the pool would improve "
        "how reliably their severity can be calibrated."
    )

single_rating_share = (ratings_per_action == 1).mean()
if single_rating_share > 0.1:
    recommendations.append(
        f"{single_rating_share:.0%} of actions currently have only one rating "
        "and contribute no within-action agreement information. Adding a "
        "second rater to a sample of these would materially improve the "
        "precision of the overall agreement estimate."
    )

thin_raters = ratings_per_rater[ratings_per_rater < ratings_per_rater.median() / 2]
if len(thin_raters) > 0:
    recommendations.append(
        f"{len(thin_raters)} raters have rated notably fewer actions than the "
        f"median rater ({ratings_per_rater.median():.0f}): "
        f"{', '.join(thin_raters.index)}. More ratings from these raters would "
        "make their individual severity/leniency estimates more precise."
    )

if not recommendations:
    recommendations.append(
        "No major coverage gaps found by these quick checks: the design is a "
        "single connected component, no rater falls far short of the overlap "
        "target, and only a small share of actions have a single rating."
    )

for i, rec in enumerate(recommendations, start=1):
    print(f"{i}. {rec}")
""")

if __name__ == "__main__":
    nb["cells"] = cells
    OUT.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, OUT)
    print(f"Notebook written with {len(cells)} cells: {OUT}")
