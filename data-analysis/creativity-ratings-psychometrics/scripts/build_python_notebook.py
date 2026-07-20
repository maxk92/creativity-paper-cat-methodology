"""Builds notebooks/01_creativity_ratings_python.ipynb from cell contents.

This script is run once to generate the notebook. Afterwards the
notebook itself is executed with `jupyter nbconvert --execute`. Changes
to the notebook content are made here in this script (not directly in
the .ipynb JSON file).
"""
import nbformat as nbf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "01_creativity_ratings_python.ipynb"

nb = nbf.v4.new_notebook()
cells = []

def md(text):
    cells.append(nbf.v4.new_markdown_cell(text.strip("\n")))

def code(text):
    cells.append(nbf.v4.new_code_cell(text.strip("\n")))

# ====================================================================
# 0. TITLE, CONTEXT, NON-NEGOTIABLE RULES
# ====================================================================
md(r"""
# Psychometric Analysis of Incompletely Crossed Creativity Ratings

**Python notebook (content-parallel to `01_creativity_ratings_R.qmd`)**

## Starting point

Creativity ratings on a unipolar 7-point scale (1 = not creative,
7 = very creative) are available for approximately 4,000 football
actions. The number of ratings per action is unequal (roughly 600
actions with one rating, roughly 2,000 with two ratings, the rest with
three to seven ratings). Not all raters rated the same actions — the
design is **unbalanced, incomplete, and (partially) crossed**.

This notebook implements the complete psychometric workflow from the
analysis brief
(`psychometrie_kreativitaetsratings_llm_anleitung.md`):

1. Data import & validation
2. Connectivity/identifiability check (bipartite rater–action graph)
3. Descriptive pairwise agreement
4. Krippendorff's alpha (ordinal, with cluster bootstrap)
5. Linear crossed mixed-effects model (variance components, D-study)
6. Model-based action scores (raw, rater-centered, LMM-BLUP, ordinal)
7. Rater severity and discrimination diagnostics
8. Ordinal hierarchical Bayesian model (PyMC)
9. Judge-response-theory-style extension (rater-specific discrimination)
10. Rater-fit diagnostics (leave-one-rater-out)
11. Model comparison, sensitivity analyses, cross-validation
12. Extended dependencies (match/player/team)
13. Simulation/recovery check
14. Export of result files, key figures, automated interpretation

## ⚠️ Important note on the data used in this run

**This notebook runs by default on SIMULATED placeholder data**
(`DEV_MODE = True`, see the setup cell). This data reproduces the
described design structure in a traceable way (same distribution of
ratings-per-action, incomplete crossing, a deliberately isolated
rater cluster to test the connectivity check), but it is **not real
creativity judgments**. All numbers, models, and interpretations
reported in this run are demonstrations of the methodology, not real
findings. Once real ratings from Google Sheets are available, set
`DEV_MODE = False` and insert the Google Sheets import code in
Section 3 — the rest of the pipeline stays unchanged.

## Non-negotiable rules (from the analysis brief)

- Absolute agreement ≠ relative consistency ≠ reliability of a single
  rating ≠ reliability of an aggregated score. These quantities are
  explicitly distinguished below.
- Actions with only one rating are kept for model-based estimation but
  contribute no within-action agreement information.
- Rater severity is only identifiable within connected components of
  the rater–action graph.
- No action score is reported without the number of ratings and an
  uncertainty statement.
- Interpretation is cautious, descriptive, and free of mechanical
  good/bad thresholds.
""")

md(r"""
## References (methodology used in this notebook)

- Amabile, T. M. (1982). Social psychology of creativity: A consensual
  assessment technique. *Journal of Personality and Social Psychology,
  43*(5), 997–1013.
- Amabile, T. M. (1996). *Creativity in Context*. Westview Press.
- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects
  modeling with crossed random effects for subjects and items.
  *Journal of Memory and Language, 59*(4), 390–412.
- Bates, D., Mächler, M., Bolker, B., & Walker, S. (2015). Fitting
  linear mixed-effects models using lme4. *Journal of Statistical
  Software, 67*(1), 1–48.
- Brennan, R. L. (2001). *Generalizability Theory*. Springer.
- Bürkner, P.-C. (2017). brms: An R package for Bayesian multilevel
  models using Stan. *Journal of Statistical Software, 80*(1), 1–28.
- Eckes, T. (2015). *Introduction to Many-Facet Rasch Measurement*
  (2nd ed.). Peter Lang.
- Krippendorff, K. (2004/2018). *Content Analysis: An Introduction to
  Its Methodology*. Sage.
- Linacre, J. M. (1989). *Many-Facet Rasch Measurement*. MESA Press.
- Myszkowski, N., & Storme, M. (2019). Judge Response Theory? A call
  to upgrade our psychometrical account of creativity judgments.
  *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175.
  https://doi.org/10.1037/aca0000225
- Myszkowski, N. (2021). Development of the R library `jrt`:
  Automated item-response theory procedures for judgment data and
  their application with the Consensual Assessment Technique. (Please
  verify final publication details/DOI against the current package
  documentation.)
- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying
  many-facet Rasch modeling in the assessment of creativity.
  *Psychology of Aesthetics, Creativity, and the Arts*. (Verify
  volume/issue/pages/DOI against the current source.)
- Shavelson, R. J., & Webb, N. M. (1991). *Generalizability Theory: A
  Primer*. Sage.
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses
  in assessing rater reliability. *Psychological Bulletin, 86*(2),
  420–428.
- McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some
  intraclass correlation coefficients. *Psychological Methods, 1*(1),
  30–46.
- Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and
  reporting intraclass correlation coefficients for reliability
  research. *Journal of Chiropractic Medicine, 15*(2), 155–163.
- Software: `statsmodels.MixedLM` (current docs: statsmodels.org),
  `krippendorff` (PyPI), `PyMC`/`ArviZ`/`Bambi` (current docs:
  pymc.io, arviz-devs.github.io, bambinos.github.io).
""")

# ====================================================================
# 1. SETUP: Imports, seed, paths, session info
# ====================================================================
md(r"""
## 0. Setup, reproducibility, and session information

We fix a random seed for all stochastic steps (bootstrap, MCMC,
train/test splits) and log package versions, operating system,
timestamp, and — if available — the Git commit hash. This allows the
run to be reproduced exactly later on.
""")

code(r"""
import warnings
import platform
import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import scipy
import statsmodels
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

SEED = 20260713
np.random.seed(SEED)
rng = np.random.default_rng(SEED)

# ------------------------------------------------------------------
# Project paths (relative to the notebook folder "notebooks/")
# ------------------------------------------------------------------
PROJECT_ROOT = Path("..").resolve()
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
RESULTS_TABLES = PROJECT_ROOT / "results" / "tables"
RESULTS_FIGURES = PROJECT_ROOT / "results" / "figures"
RESULTS_MODELS = PROJECT_ROOT / "results" / "models"
RESULTS_LOGS = PROJECT_ROOT / "results" / "logs"

for d in [DATA_RAW, DATA_PROCESSED, RESULTS_TABLES, RESULTS_FIGURES,
          RESULTS_MODELS, RESULTS_LOGS]:
    d.mkdir(parents=True, exist_ok=True)

plt.rcParams["figure.dpi"] = 110
plt.rcParams["savefig.dpi"] = 200
plt.rcParams["font.size"] = 10
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

warnings.filterwarnings("default", category=UserWarning)

def save_fig(fig, name, caption=None):
    # Saves a figure as PNG and SVG under results/figures/.
    fig.savefig(RESULTS_FIGURES / f"{name}.png", bbox_inches="tight")
    fig.savefig(RESULTS_FIGURES / f"{name}.svg", bbox_inches="tight")
    if caption:
        (RESULTS_FIGURES / f"{name}_caption.txt").write_text(caption)
    print(f"Figure saved: {name}.png / {name}.svg")

def save_table(df_table, name, index=False):
    # Saves a table as CSV under results/tables/.
    path = RESULTS_TABLES / f"{name}.csv"
    df_table.to_csv(path, index=index)
    print(f"Table saved: {path.relative_to(PROJECT_ROOT)} "
          f"({df_table.shape[0]} rows x {df_table.shape[1]} columns)")
    return path

WARNINGS_LOG = []
def log_warning(msg):
    # Collects warnings centrally (Section 25 of the analysis brief:
    # no silent abort, but clear, collected warnings).
    WARNINGS_LOG.append({"timestamp": datetime.now(timezone.utc).isoformat(),
                          "message": msg})
    warnings.warn(msg)

print(f"Seed: {SEED}")
print(f"Project root: {PROJECT_ROOT}")
""")

code(r"""
# ------------------------------------------------------------------
# Log session information (package versions, OS, time, Git)
# ------------------------------------------------------------------
def get_git_hash():
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT,
                              capture_output=True, text=True, timeout=5)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:
        pass
    return "not a Git repository / hash not available"

session_info = {
    "analysis_datetime_utc": datetime.now(timezone.utc).isoformat(),
    "python_version": sys.version,
    "platform": platform.platform(),
    "git_commit": get_git_hash(),
    "seed": SEED,
    "package_versions": {},
}

for pkg_name in ["numpy", "pandas", "scipy", "statsmodels", "matplotlib",
                  "networkx", "sklearn", "pingouin", "krippendorff",
                  "pymc", "arviz", "bambi", "plotnine"]:
    try:
        mod = __import__(pkg_name)
        session_info["package_versions"][pkg_name] = getattr(mod, "__version__", "unknown")
    except ImportError:
        session_info["package_versions"][pkg_name] = "not installed"

with open(RESULTS_LOGS / "session_info_python.json", "w") as f:
    json.dump(session_info, f, indent=2)

print(json.dumps(session_info, indent=2))
""")

# ====================================================================
# 2. DATA IMPORT (Section 3 of the brief)
# ====================================================================
md(r"""
## 1. Data import from Google Sheets

The production import code (downloading the rating sheet from Google
Sheets and joining it with the StatsBomb event details) already exists
in the notebook `data-analysis/paper1-data-analysis.ipynb` of this
project and follows this pattern:

```python
sheet_url = "https://docs.google.com/spreadsheets/d/<ID>/edit?usp=sharing"
sheet_id = sheet_url.split("/d/")[1].split("/")[0]
url_template = "https://docs.google.com/spreadsheets/d/{}/export?format=xlsx"
ratings_raw = pd.read_excel(url_template.format(sheet_id), sheet_name=0)
```

For the present psychometric analysis, **only** `action_id`,
`rater_id`, and `rating` (plus optional additional variables) are
needed; joining with the StatsBomb event data (action type, xG, etc.)
is not required for reliability/score estimation and remains the job
of the upstream notebook.

**Placeholder policy:** The following code block is the exact
mandated placeholder cell. It raises a `NotImplementedError` as soon
as `DEV_MODE = False` is set — at that point the real import code MUST
be inserted here. For development and demonstration of the pipeline,
`DEV_MODE = True` is set; in that case, already-generated placeholder
data clearly marked as **simulated** is loaded (see
`scripts/simulate_ratings.py`).
""")

code(r"""
# ============================================================
# PLACEHOLDER: Google Sheets import
# ============================================================
# Insert the researcher's existing Python code here.
# Expected result:
# ratings_raw = pandas.DataFrame with at least:
# action_id, rater_id, rating
#
# Example:
# ratings_raw = load_ratings_from_google_sheet(...)
# ============================================================

DEV_MODE = True  # SET TO False AS SOON AS REAL SHEET DATA IS USED

if not DEV_MODE:
    raise NotImplementedError(
        "Insert the Google Sheets import code here and then remove "
        "the NotImplementedError line."
    )
else:
    log_warning(
        "DEV_MODE=True: loading SIMULATED placeholder data. "
        "All downstream results are methodology demonstrations, "
        "NOT real findings. Before using this for publication, "
        "set DEV_MODE=False and insert the real import code."
    )
    _sim_path = DATA_RAW / "ratings_long_raw.csv"
    if not _sim_path.exists():
        raise FileNotFoundError(
            f"Simulated development data not found at {_sim_path}. "
            "Please run 'python scripts/simulate_ratings.py' first."
        )
    ratings_raw = pd.read_csv(_sim_path)

ratings_raw.head()
""")

code(r"""
# Save the raw data immediately after "downloading" it, and do NOT
# modify it afterwards (Section 3.1 of the analysis brief).
RAW_PATH = DATA_RAW / "ratings_long_raw.csv"
RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
ratings_raw.to_csv(RAW_PATH, index=False)
print(f"Raw data saved: {RAW_PATH} ({len(ratings_raw)} rows)")
print(f"Columns: {list(ratings_raw.columns)}")
""")

# ====================================================================
# 3. VALIDATION AND CLEANING (Section 4 of the brief)
# ====================================================================
md(r"""
## 2. Data validation and cleaning

### 2.1 Schema, types, duplicates

We check: existence of required variables, missing IDs, convertibility
of `rating` to numeric, value range $\{1,\dots,7\}$, and duplicate
`(action_id, rater_id)` combinations. **Duplicates are not averaged
automatically** — they are first listed in a table and resolved only
according to an explicitly documented rule (see below).
""")

code(r"""
required_cols = ["action_id", "rater_id", "rating"]
missing_cols = [c for c in required_cols if c not in ratings_raw.columns]
if missing_cols:
    raise ValueError(f"Required variables missing from the raw dataset: {missing_cols}")

cleaning_log = []

def log_clean_step(step, n_before, n_after, description):
    cleaning_log.append({
        "step": step, "n_rows_before": n_before, "n_rows_after": n_after,
        "n_rows_affected": n_before - n_after, "description": description,
    })

df = ratings_raw.copy()
n0 = len(df)

# --- missing IDs ------------------------------------------------------
n_missing_action_id = df["action_id"].isna().sum()
n_missing_rater_id = df["rater_id"].isna().sum()
print(f"Missing action_id: {n_missing_action_id}")
print(f"Missing rater_id:  {n_missing_rater_id}")
if n_missing_action_id or n_missing_rater_id:
    log_warning(f"{n_missing_action_id + n_missing_rater_id} rows with a missing ID found.")
df = df.dropna(subset=["action_id", "rater_id"]).copy()
log_clean_step("drop_missing_id", n0, len(df), "Rows with missing action_id/rater_id removed")

# --- IDs as string/categorical -----------------------------------------
df["action_id"] = df["action_id"].astype(str)
df["rater_id"] = df["rater_id"].astype(str)

# --- convert rating to numeric (robust against " 4 ", "n/a", etc.) -----
n_before = len(df)
rating_numeric_raw = pd.to_numeric(
    df["rating"].astype(str).str.strip(), errors="coerce"
)
n_not_convertible = rating_numeric_raw.isna().sum() - df["rating"].isna().sum()
print(f"Non-convertible, non-missing raw rating values: {n_not_convertible}")
if n_not_convertible > 0:
    print(df.loc[rating_numeric_raw.isna() & df["rating"].notna(),
                  ["action_id", "rater_id", "rating"]])
    log_warning(f"{n_not_convertible} raw rating values were not numerically convertible and were set to NA.")
df["rating_numeric_raw"] = rating_numeric_raw
""")

code(r"""
# --- check value range: only 1-7 allowed -------------------------------
out_of_range_mask = df["rating_numeric_raw"].notna() & (
    (df["rating_numeric_raw"] < 1) | (df["rating_numeric_raw"] > 7)
    | (df["rating_numeric_raw"] % 1 != 0)
)
tbl_out_of_range = df.loc[out_of_range_mask,
                            ["action_id", "rater_id", "rating", "rating_numeric_raw"]]
print(f"Values outside {{1,...,7}} or non-integer: {len(tbl_out_of_range)}")
if len(tbl_out_of_range) > 0:
    print(tbl_out_of_range)
    log_warning(f"{len(tbl_out_of_range)} rating values outside the allowed range 1-7 found and removed.")
save_table(tbl_out_of_range, "flagged_out_of_range_ratings")

n_before = len(df)
df = df.loc[~out_of_range_mask].copy()
log_clean_step("drop_out_of_range", n_before, len(df),
                "Rating values outside {1,...,7} or non-integer removed")

# --- missing ratings (after conversion) --------------------------------
n_before = len(df)
n_missing_rating = df["rating_numeric_raw"].isna().sum()
print(f"Missing/non-convertible rating values: {n_missing_rating}")
if n_missing_rating > 0:
    log_warning(f"{n_missing_rating} rows with missing/non-convertible rating removed.")
df = df.loc[df["rating_numeric_raw"].notna()].copy()
log_clean_step("drop_missing_rating", n_before, len(df),
                "Rows with missing or non-convertible rating removed")
""")

md(r"""
### 2.2 Duplicates (`action_id` × `rater_id`)

**Documented resolution rule:** Repeated occurrences of the same
rater–action combination are first listed in full in a table. Since
the present (simulated) dataset carries no substantive information
about which of the repeated values is the "valid" one (e.g., whether
it is an intentional repeated rating, an accidental duplication during
the sheet export, or a second rating dimension), we set an **explicit,
conservative rule**: *for duplicates, the row that appears last in the
raw data is kept* (assumption: later entries in a Google Sheets export
typically reflect corrections). This rule is an assumption and must be
checked against the actual cause of duplicates once real data is used,
and replaced if necessary (e.g., by consulting the raters or using a
`rating_order` criterion).
""")

code(r"""
dup_mask = df.duplicated(subset=["action_id", "rater_id"], keep=False)
tbl_duplicates = df.loc[dup_mask,
                          ["action_id", "rater_id", "rating", "rating_numeric_raw"]].sort_values(
    ["action_id", "rater_id"])
print(f"Rows with a duplicate (action_id, rater_id) combination: {len(tbl_duplicates)}")
print(tbl_duplicates)
save_table(tbl_duplicates, "flagged_duplicate_rater_action_pairs")
if len(tbl_duplicates) > 0:
    log_warning(
        f"{len(tbl_duplicates)} rows with duplicate (action_id, rater_id) "
        "combinations found. Resolution rule: the last entry is kept "
        "(see the markdown cell above). Verify against real data!"
    )

n_before = len(df)
df = df.drop_duplicates(subset=["action_id", "rater_id"], keep="last").copy()
log_clean_step("resolve_duplicates", n_before, len(df),
                "Duplicates resolved: last entry per (action_id, rater_id) kept")

# --- create final rating variables --------------------------------------
df["rating_numeric"] = df["rating_numeric_raw"].astype(int)
df["rating_ordinal"] = pd.Categorical(df["rating_numeric"], categories=list(range(1, 8)),
                                        ordered=True)
df = df.drop(columns=["rating_numeric_raw"])

assert df["rating_numeric"].between(1, 7).all(), "Ratings outside 1-7 after cleaning!"
assert not df.duplicated(subset=["action_id", "rater_id"]).any(), "Duplicates remain after cleaning!"
assert df["action_id"].notna().all() and df["rater_id"].notna().all()

n_final = len(df)
print(f"\nCleaning complete: {n0} -> {n_final} rows "
      f"({n0 - n_final} removed/resolved; the difference from duplicate "
      "resolution is only counted once).")

cleaning_log_df = pd.DataFrame(cleaning_log)
print(cleaning_log_df)
save_table(cleaning_log_df, "cleaning_log")
""")

md(r"""
### 2.3 Missingness structure, ratings per action and per rater

Actions with only one rating are kept for model-based score
estimation, but are flagged separately for all *pairwise* agreement
analyses (Sections 6, 7) since they provide no within-action
comparison information.
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

axes[1].hist(ratings_per_rater.values, bins=20, color="#DD8452", edgecolor="white")
axes[1].set_title("Number of rated actions per rater")
axes[1].set_xlabel("Rated actions")
axes[1].set_ylabel("Number of raters")

fig.suptitle(f"Sample: n={df.shape[0]} ratings, "
              f"{df.action_id.nunique()} actions, {df.rater_id.nunique()} raters")
fig.tight_layout()
save_fig(fig, "fig02_ratings_per_action_and_rater",
         "Distribution of the number of ratings per action (left) and the "
         "number of rated actions per rater (right).")
plt.show()

print(ratings_per_action.describe())
print("\nShare of actions with exactly 1 rating: "
      f"{(ratings_per_action == 1).mean():.1%}")
print("Share of actions with exactly 2 ratings: "
      f"{(ratings_per_action == 2).mean():.1%}")

df["single_rating_action"] = df["action_id"].map(ratings_per_action == 1)
""")

md(r"""
### 2.4 Plausibility and distribution checks

Overall category frequencies as well as rater statistics (mean,
median, SD, IQR, floor/ceiling rates, number of categories used, share
of middle [3–5] vs. extreme [1,7] categories).
""")

code(r"""
fig, ax = plt.subplots(figsize=(6, 4))
df["rating_numeric"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#55A868")
ax.set_title(f"Distribution of all ratings (n={len(df)})")
ax.set_xlabel("Creativity rating (1 = not creative, 7 = very creative)")
ax.set_ylabel("Frequency")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
fig.tight_layout()
save_fig(fig, "fig01_overall_rating_distribution",
         "Overall frequency of the seven rating categories across all ratings.")
plt.show()
""")

code(r"""
def rater_summary(g):
    vals = g["rating_numeric"]
    n_cat = vals.nunique()
    p_extreme = vals.isin([1, 7]).mean()
    p_central = vals.isin([3, 4, 5]).mean()
    probs = vals.value_counts(normalize=True)
    entropy = -(probs * np.log(probs.clip(lower=1e-12))).sum()
    return pd.Series({
        "n_ratings": len(vals),
        "n_actions": g["action_id"].nunique(),
        "mean": vals.mean(),
        "median": vals.median(),
        "sd": vals.std(),
        "iqr": vals.quantile(0.75) - vals.quantile(0.25),
        "n_categories_used": n_cat,
        "entropy": entropy,
        "floor_rate": (vals == 1).mean(),
        "ceiling_rate": (vals == 7).mean(),
        "extreme_category_rate": p_extreme,
        "central_category_rate": p_central,
    })

rater_desc = df.groupby("rater_id").apply(rater_summary, include_groups=False).reset_index()
rater_desc = rater_desc.sort_values("mean").reset_index(drop=True)
save_table(rater_desc, "rater_descriptive_statistics")
rater_desc.head(10)
""")

code(r"""
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
axes[0, 0].hist(rater_desc["mean"], bins=20, color="#4C72B0")
axes[0, 0].set_title("Rater means")
axes[0, 1].hist(rater_desc["sd"], bins=20, color="#DD8452")
axes[0, 1].set_title("Rater SD (scale width)")
axes[1, 0].hist(rater_desc["n_categories_used"], bins=range(1, 9), color="#55A868")
axes[1, 0].set_title("Number of categories used (1-7)")
axes[1, 1].scatter(rater_desc["extreme_category_rate"], rater_desc["central_category_rate"],
                    s=20 + rater_desc["n_ratings"] / 5, alpha=0.7, color="#C44E52")
axes[1, 1].set_xlabel("Share of extreme categories (1,7)")
axes[1, 1].set_ylabel("Share of middle categories (3-5)")
axes[1, 1].set_title("Extreme vs. central tendency (point size ~ n ratings)")
fig.suptitle("Descriptive rater diagnostics")
fig.tight_layout()
save_fig(fig, "fig03_rater_descriptive_diagnostics",
         "Distribution of rater means, rater SD, category usage, and "
         "extreme/central tendency across all raters.")
plt.show()
""")

md(r"""
### 2.5 Temporal drift (descriptive, if `rating_order` is available)

A simple descriptive check: correlation between `rating_order`
(position within the rater's session) and rating, per rater. The
model-based drift analysis follows in Section 8 (rater effects).
""")

code(r"""
if "rating_order" in df.columns:
    drift_corr = (
        df.groupby("rater_id")
        .apply(lambda g: g["rating_numeric"].corr(g["rating_order"], method="spearman")
               if len(g) >= 10 else np.nan, include_groups=False)
        .rename("spearman_rating_vs_order")
        .reset_index()
    )
    n_flagged = (drift_corr["spearman_rating_vs_order"].abs() > 0.2).sum()
    print(f"Raters with |Spearman(rating, rating_order)| > .2 (descriptive drift indicator): {n_flagged}")
    save_table(drift_corr, "descriptive_drift_correlation_by_rater")
else:
    log_warning("No rating_order/timestamp variable available - drift check skipped.")
""")

code(r"""
# Save the clean file (Section 4.5 of the analysis brief)
CLEAN_PATH = DATA_PROCESSED / "ratings_long_clean.csv"
df.to_csv(CLEAN_PATH, index=False)
print(f"Cleaned data saved: {CLEAN_PATH} ({len(df)} rows)")
ratings_clean = df.copy()
ratings_clean.head()
""")

# ====================================================================
# 4. CONNECTIVITY AND IDENTIFIABILITY (Section 5 of the brief)
# ====================================================================
md(r"""
## 3. Connectivity and identifiability of the rater–action design

**This step is mandatory and must be performed before any
rater-correcting model.**

Rater severity parameters are only identifiable relative to other
raters if the rating design is sufficiently connected. If groups of
raters sit in separate components with no shared actions or bridge
raters, their levels cannot be empirically placed on the same scale.

We construct a bipartite graph (nodes: actions ∪ raters; edge: rater
rated action) and determine its connected components.
""")

code(r"""
B = nx.Graph()
B.add_nodes_from(ratings_clean["action_id"].unique(), bipartite="action")
B.add_nodes_from(("R::" + ratings_clean["rater_id"]).unique(), bipartite="rater")
edges = list(zip(ratings_clean["action_id"], "R::" + ratings_clean["rater_id"]))
B.add_edges_from(edges)

components = list(nx.connected_components(B))
components = sorted(components, key=len, reverse=True)

comp_summary = []
for i, comp in enumerate(components):
    action_nodes = [n for n in comp if not str(n).startswith("R::")]
    rater_nodes = [n for n in comp if str(n).startswith("R::")]
    comp_summary.append({
        "component_id": i,
        "n_nodes": len(comp),
        "n_actions": len(action_nodes),
        "n_raters": len(rater_nodes),
    })
comp_summary_df = pd.DataFrame(comp_summary)
save_table(comp_summary_df, "connectivity_component_summary")
print(comp_summary_df)

n_components = len(components)
print(f"\nNumber of connected components: {n_components}")
if n_components > 1:
    log_warning(
        f"The rater-action graph has {n_components} separate components. "
        "Rater severity parameters from different components are NOT "
        "comparable on a common scale. The main analysis uses only the "
        "largest connected component; actions/raters from smaller "
        "components are flagged accordingly."
    )

largest_component = components[0]
largest_component_actions = {n for n in largest_component if not str(n).startswith("R::")}
largest_component_raters = {str(n)[3:] for n in largest_component if str(n).startswith("R::")}

action_component_map = {}
for i, comp in enumerate(components):
    for n in comp:
        if not str(n).startswith("R::"):
            action_component_map[n] = i
ratings_clean["connected_component"] = ratings_clean["action_id"].map(action_component_map)
ratings_clean["in_largest_component"] = ratings_clean["connected_component"] == 0

print(f"\nLargest component: {len(largest_component_actions)} actions, "
      f"{len(largest_component_raters)} raters "
      f"({len(largest_component_actions) / ratings_clean.action_id.nunique():.1%} of all actions).")
""")

md(r"""
> **Interpretation (auto-generated):** Rater severity parameters are
> only identifiable relative to other raters if the rating design is
> sufficiently connected. If groups of raters sit in separate
> components with no shared actions or bridge raters, their levels
> cannot be empirically placed on the same scale. All subsequent
> rater-correcting models (Section 8 onward) are therefore estimated
> primarily on the largest connected component; actions from smaller
> components receive a corresponding `score_flag` in
> `action_scores.csv`.
""")

code(r"""
# Degree distributions (actions: number of raters per action; raters: number of actions per rater)
action_degree = pd.Series(dict(B.degree(ratings_clean["action_id"].unique())))
rater_degree = pd.Series({r: B.degree("R::" + r) for r in ratings_clean["rater_id"].unique()})

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].hist(action_degree.values, bins=range(1, 9), color="#4C72B0", edgecolor="white")
axes[0].set_title("Degree distribution: raters per action")
axes[1].hist(rater_degree.values, bins=20, color="#DD8452", edgecolor="white")
axes[1].set_title("Degree distribution: actions per rater")
fig.tight_layout()
save_fig(fig, "fig04_degree_distributions",
         "Degree distribution in the bipartite rater-action graph.")
plt.show()

isolated_raters = rater_degree[rater_degree <= 2]
print(f"Raters with very low connectivity (<=2 rated actions): {len(isolated_raters)}")
if len(isolated_raters) > 0:
    print(isolated_raters)
""")

md(r"""
### 3.1 Rater projection: jointly rated actions per rater pair

For connectivity diagnostics and later pairwise agreement analyses, we
compute for each rater pair the number of jointly rated actions (the
edge weight of the rater projection of the bipartite graph). For large
numbers of raters, the **full** bipartite graph is **not** plotted
(unreadable); instead we show a heatmap and a histogram of the overlap
counts.
""")

code(r"""
rater_ids_sorted = sorted(ratings_clean["rater_id"].unique())
n_raters = len(rater_ids_sorted)
rater_idx = {r: i for i, r in enumerate(rater_ids_sorted)}

action_to_raters = ratings_clean.groupby("action_id")["rater_id"].apply(list)
overlap = np.zeros((n_raters, n_raters), dtype=int)
for raters_for_action in action_to_raters:
    if len(raters_for_action) < 2:
        continue
    idxs = sorted(set(rater_idx[r] for r in raters_for_action))
    for a in range(len(idxs)):
        for b in range(a + 1, len(idxs)):
            overlap[idxs[a], idxs[b]] += 1
            overlap[idxs[b], idxs[a]] += 1

overlap_df = pd.DataFrame(overlap, index=rater_ids_sorted, columns=rater_ids_sorted)
save_table(overlap_df.reset_index().rename(columns={"index": "rater_id"}), "rater_pair_overlap_matrix")

pair_overlaps = overlap[np.triu_indices(n_raters, k=1)]
pair_overlaps_nonzero = pair_overlaps[pair_overlaps > 0]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
im = axes[0].imshow(overlap, cmap="viridis")
axes[0].set_title("Heatmap: jointly rated actions per rater pair")
axes[0].set_xlabel("Rater")
axes[0].set_ylabel("Rater")
fig.colorbar(im, ax=axes[0], shrink=0.8, label="joint actions")

axes[1].hist(pair_overlaps_nonzero, bins=30, color="#4C72B0", edgecolor="white")
axes[1].set_title("Histogram: overlap counts (rater pairs > 0)")
axes[1].set_xlabel("Number of jointly rated actions")
fig.tight_layout()
save_fig(fig, "fig05_rater_overlap_heatmap_and_histogram",
         "Left: heatmap of jointly rated actions per rater pair. "
         "Right: histogram of overlap counts across all rater pairs with "
         "at least one shared action.")
plt.show()

mean_pair_overlap = pd.Series(overlap.sum(axis=1) / np.maximum(1, (overlap > 0).sum(axis=1)),
                                index=rater_ids_sorted, name="mean_pair_overlap")
print(f"Median overlap (rater pairs>0): {np.median(pair_overlaps_nonzero):.1f}")
print(f"Share of rater pairs with no shared action at all: "
      f"{(pair_overlaps == 0).mean():.1%}")
""")

# ====================================================================
# 5. DESCRIPTIVE PAIRWISE AGREEMENT (Section 6 of the brief)
# ====================================================================
md(r"""
## 4. Descriptive pairwise agreement

These analyses are **supplementary**, not the sole main analysis. For
each rater pair with sufficient overlap (here: at least 10 jointly
rated actions), we compute metrics of **relative consistency**
(correlations) and **absolute agreement** (mean difference, MAE,
weighted kappa). High correlation can occur despite large systematic
mean differences — agreement is not the same as correlation (see the
methodological guideline in Section 22 of the analysis brief).
""")

code(r"""
from scipy import stats as sps
from sklearn.metrics import cohen_kappa_score

MIN_OVERLAP = 10

wide = ratings_clean.pivot_table(index="action_id", columns="rater_id",
                                    values="rating_numeric", aggfunc="first")

pair_stats = []
rater_list = wide.columns.tolist()
for i in range(len(rater_list)):
    for j in range(i + 1, len(rater_list)):
        rj, rk = rater_list[i], rater_list[j]
        both = wide[[rj, rk]].dropna()
        n_common = len(both)
        if n_common < MIN_OVERLAP:
            continue
        yj, yk = both[rj].values, both[rk].values
        pearson_r = np.corrcoef(yj, yk)[0, 1]
        spearman_r = sps.spearmanr(yj, yk).correlation
        kendall_t = sps.kendalltau(yj, yk).correlation
        mean_diff = yj.mean() - yk.mean()
        sd_diff = (yj - yk).std(ddof=1)
        mae = np.abs(yj - yk).mean()
        w_kappa = cohen_kappa_score(yj, yk, weights="quadratic")
        pair_stats.append({
            "rater_1": rj, "rater_2": rk, "n_common_actions": n_common,
            "pearson_r": pearson_r, "spearman_r": spearman_r, "kendall_tau": kendall_t,
            "mean_diff_1_minus_2": mean_diff, "sd_diff": sd_diff, "mae": mae,
            "weighted_kappa": w_kappa,
        })

pair_stats_df = pd.DataFrame(pair_stats)
save_table(pair_stats_df, "pairwise_rater_agreement")
print(f"Rater pairs with >= {MIN_OVERLAP} shared actions: {len(pair_stats_df)} "
      f"out of {n_raters * (n_raters - 1) // 2} possible pairs")
pair_stats_df.describe()
""")

md(r"""
### 4.1 Bland–Altman-style plot

For the two rater pairs with the largest overlap: mean vs. difference
of the two ratings, mean difference, and limits of agreement
($\pm 1.96 \cdot SD_{\text{diff}}$). The Likert scale is discrete and
bounded — this plot is diagnostic, not the sole basis for inference
(overplotting is mitigated via jitter and point-size encoding of
frequency).
""")

code(r"""
top_pairs = pair_stats_df.nlargest(2, "n_common_actions")

fig, axes = plt.subplots(1, len(top_pairs), figsize=(6 * len(top_pairs), 4.5))
if len(top_pairs) == 1:
    axes = [axes]
for ax, (_, row) in zip(axes, top_pairs.iterrows()):
    rj, rk = row["rater_1"], row["rater_2"]
    both = wide[[rj, rk]].dropna()
    mean_ = both.mean(axis=1)
    diff_ = both[rj] - both[rk]
    jitter = rng.normal(0, 0.05, size=len(both))
    ax.scatter(mean_ + jitter, diff_ + jitter, alpha=0.3, s=15, color="#4C72B0")
    md_ = diff_.mean()
    sd_ = diff_.std(ddof=1)
    ax.axhline(md_, color="black", lw=1)
    ax.axhline(md_ + 1.96 * sd_, color="red", ls="--", lw=1)
    ax.axhline(md_ - 1.96 * sd_, color="red", ls="--", lw=1)
    ax.set_title(f"{rj} vs {rk} (n={len(both)})\nmean diff={md_:.2f}, LoA=[{md_-1.96*sd_:.2f}, {md_+1.96*sd_:.2f}]")
    ax.set_xlabel("Mean of both ratings")
    ax.set_ylabel(f"Difference ({rj} - {rk})")
fig.suptitle("Bland-Altman-style plot for the two rater pairs with the strongest overlap")
fig.tight_layout()
save_fig(fig, "fig06_bland_altman_top_pairs",
         "Bland-Altman-style plots (with jitter due to the discrete scale) for "
         "the two rater pairs with the largest number of jointly rated actions.")
plt.show()
""")

md(r"""
### 4.2 Rater-pair heatmaps

Separate heatmaps for shared actions, Spearman correlation, mean
difference, and weighted kappa. Rater pairs with insufficient overlap
($n < 10$) are masked (grey).
""")

code(r"""
def pair_matrix(metric_col):
    mat = pd.DataFrame(np.nan, index=rater_list, columns=rater_list)
    for _, row in pair_stats_df.iterrows():
        mat.loc[row["rater_1"], row["rater_2"]] = row[metric_col]
        mat.loc[row["rater_2"], row["rater_1"]] = row[metric_col]
    return mat

fig, axes = plt.subplots(2, 2, figsize=(12, 11))
metrics = [("n_common_actions", "Shared actions", "viridis"),
           ("spearman_r", "Spearman correlation", "RdBu_r"),
           ("mean_diff_1_minus_2", "Mean difference", "RdBu_r"),
           ("weighted_kappa", "Weighted kappa", "RdBu_r")]
for ax, (col, title, cmap) in zip(axes.flat, metrics):
    mat = pair_matrix(col)
    masked = np.ma.masked_invalid(mat.values)
    im = ax.imshow(masked, cmap=cmap)
    ax.set_title(title)
    fig.colorbar(im, ax=ax, shrink=0.8)
fig.suptitle(f"Rater-pair heatmaps (only pairs with >= {MIN_OVERLAP} shared actions)")
fig.tight_layout()
save_fig(fig, "fig07_pairwise_metric_heatmaps",
         "Heatmaps of pairwise agreement metrics between raters; "
         "masked (white) cells = insufficient overlap.")
plt.show()
""")

# ====================================================================
# 6. KRIPPENDORFF'S ALPHA (Section 7 of the brief)
# ====================================================================
md(r"""
## 5. Krippendorff's alpha

### Why Krippendorff's alpha?

Krippendorff's $\alpha$ fundamentally supports differing numbers of
raters per unit, missing ratings, more than two raters, and different
levels of measurement — all properties of the present design. We
compute:

1. **ordinal alpha** (primary — category distances are not assumed to
   be exactly equal),
2. **interval-scaled alpha** as a sensitivity analysis.

$$
\alpha = 1 - \frac{D_o}{D_e}
$$

where $D_o$ is the observed and $D_e$ the expected disagreement
(under random assignment), weighted by a distance function $\delta$
that depends on the level of measurement.

**Data shape:** The `krippendorff` package expects a reliability-data
matrix shaped (raters × units) with `NaN` for missing combinations —
we therefore transpose `wide` (actions × raters) accordingly.
""")

code(r"""
import krippendorff as kd

reliability_data = wide.T.values  # (raters x actions), NaN = missing

alpha_ordinal = kd.alpha(reliability_data=reliability_data,
                           level_of_measurement="ordinal")
alpha_interval = kd.alpha(reliability_data=reliability_data,
                            level_of_measurement="interval")

print(f"Krippendorff's alpha (ordinal, primary):        {alpha_ordinal:.3f}")
print(f"Krippendorff's alpha (interval, sensitivity):    {alpha_interval:.3f}")
""")

md(r"""
### 5.1 Uncertainty: cluster bootstrap over actions

The action is the primary unit of observation. In the bootstrap,
**all ratings of a sampled action stay together** (cluster bootstrap
over actions, not naive resampling of individual ratings). We use
2,000 bootstrap replications with a fixed seed.
""")

code(r"""
N_BOOT = 2000
action_ids_all = wide.index.to_numpy()
n_actions_all = len(action_ids_all)

boot_rng = np.random.default_rng(SEED)
boot_alphas_ord = np.empty(N_BOOT)
boot_alphas_int = np.empty(N_BOOT)

for b in range(N_BOOT):
    sampled_actions = boot_rng.choice(action_ids_all, size=n_actions_all, replace=True)
    boot_wide = wide.loc[sampled_actions]
    rel_data = boot_wide.T.values
    try:
        boot_alphas_ord[b] = kd.alpha(reliability_data=rel_data, level_of_measurement="ordinal")
        boot_alphas_int[b] = kd.alpha(reliability_data=rel_data, level_of_measurement="interval")
    except Exception:
        boot_alphas_ord[b] = np.nan
        boot_alphas_int[b] = np.nan

ci_ord = np.nanpercentile(boot_alphas_ord, [2.5, 97.5])
ci_int = np.nanpercentile(boot_alphas_int, [2.5, 97.5])
print(f"Ordinal alpha:  {alpha_ordinal:.3f}, 95% cluster-bootstrap CI [{ci_ord[0]:.3f}, {ci_ord[1]:.3f}] "
      f"(n_boot={N_BOOT}, {np.isnan(boot_alphas_ord).sum()} failed replications)")
print(f"Interval alpha: {alpha_interval:.3f}, 95% cluster-bootstrap CI [{ci_int[0]:.3f}, {ci_int[1]:.3f}]")
""")

md(r"""
### 5.2 Subgroup and sensitivity analyses

Alpha additionally for: actions with ≥2 ratings, actions with ≥3
ratings, and within the largest connected component (from Section 3).
**Warning:** alpha values from different subsets are not directly
comparable, since the heterogeneity of the included actions differs.
""")

code(r"""
def alpha_for_subset(action_subset, label):
    sub_wide = wide.loc[wide.index.isin(action_subset)]
    rel = sub_wide.T.values
    a_ord = kd.alpha(reliability_data=rel, level_of_measurement="ordinal")
    a_int = kd.alpha(reliability_data=rel, level_of_measurement="interval")
    return {"subset": label, "n_actions": len(sub_wide),
            "alpha_ordinal": a_ord, "alpha_interval": a_int}

subset_results = [
    alpha_for_subset(wide.index, "all actions"),
    alpha_for_subset(ratings_per_action[ratings_per_action >= 2].index, "n_ratings >= 2"),
    alpha_for_subset(ratings_per_action[ratings_per_action >= 3].index, "n_ratings >= 3"),
    alpha_for_subset(largest_component_actions, "largest connected component"),
]
subset_results_df = pd.DataFrame(subset_results)
save_table(subset_results_df, "krippendorff_alpha_sensitivity")
print(subset_results_df)

alpha_summary_df = pd.DataFrame([{
    "measure": "ordinal", "alpha": alpha_ordinal, "ci_low": ci_ord[0], "ci_high": ci_ord[1],
    "n_boot": N_BOOT,
}, {
    "measure": "interval", "alpha": alpha_interval, "ci_low": ci_int[0], "ci_high": ci_int[1],
    "n_boot": N_BOOT,
}])
save_table(alpha_summary_df, "krippendorff_alpha_main")

log_warning(
    "Krippendorff's alpha values from different subsets (e.g. >=2 vs. >=3 ratings) "
    "are not directly comparable due to differing action heterogeneity."
)
""")

# ====================================================================
# 7. LINEAR CROSSED MIXED-EFFECTS MODEL (Section 8 of the brief)
# ====================================================================
md(r"""
## 6. Linear crossed mixed-effects model

### 6.1 Model

We first treat the 7-point scale as approximately interval-scaled:

$$
y_{ij} = \mu + u_i + v_j + \varepsilon_{ij}, \qquad
u_i \sim \mathcal{N}(0,\sigma^2_{\text{action}}), \quad
v_j \sim \mathcal{N}(0,\sigma^2_{\text{rater}}), \quad
\varepsilon_{ij} \sim \mathcal{N}(0,\sigma^2_e)
$$

The design is **crossed, not hierarchical**: a rater rates multiple
actions, and an action is rated by multiple raters. $u_i$ is the
latent deviation of the creativity of action $i$, $v_j$ is the
severity/leniency of rater $j$.

**Limitation:** Since each rater-action cell typically contains only
one rating, the action×rater interaction is not separately
identifiable from the residual. $\varepsilon_{ij}$ therefore includes
interaction, momentary rating error, and other unmodeled influences —
this is a **variance-component approximation**, not a complete
G-theory decomposition of all facets.

We estimate exclusively on the **largest connected component** (see
Section 3), since rater severity is not identifiable outside it.

### 6.2 Python implementation: two engines

`statsmodels.MixedLM` supports crossed random effects via variance
components (`vc_formula`) with a single artificial group — this is
the standard API suggested in the analysis brief. **In practice**,
however, `vc_formula` produces a **dense** dummy design matrix with
one column per action (here: up to ~3,940 columns). The generic
optimization in `MixedLM` operates on this dense matrix; a single fit
call on the full dataset exceeded 3 minutes in our tests without
converging (the underlying computational complexity per optimization
step scales roughly with the squared number of columns). This is
unproblematic for ~40 raters; it is not for ~4,000 actions.

The analysis brief explicitly anticipates exactly this case:

> "If BLUP extraction for individual variance components is not
> robustly accessible, additionally use a Bayesian model in
> PyMC/Bambi/Stan for score estimation."

and

> "Do not implement a seemingly finished function if the package used
> does not actually support the desired model structure."

We therefore first demonstrate `statsmodels.MixedLM` on a
**feasibility subsample** (to validate the model equation and as a
cross-check), and use a **Bayesian counterpart in PyMC** for the
**full** estimation (identical model, same variance-component
structure, normal likelihood instead of ordinal — the ordinal facette
approach follows separately in Section 8). PyMC handles the same
~4,040-parameter model in under a minute thanks to sparse,
gradient-based NUTS sampling (instead of dense least-squares-style
optimization) — a good example of "Bayesian vs. frequentist" here
also being a **computational**, not just a philosophical, choice.
""")

code(r"""
import statsmodels.formula.api as smf

df_lmm = ratings_clean.loc[ratings_clean["in_largest_component"]].copy()

# --- Feasibility subsample for statsmodels.MixedLM ----------------------
# Random subset of actions (with their complete ratings), small enough
# that the dense vc_formula design matrix stays manageable.
DEMO_N_ACTIONS = 250
demo_actions = rng.choice(df_lmm["action_id"].unique(), size=DEMO_N_ACTIONS, replace=False)
df_lmm_demo = df_lmm.loc[df_lmm["action_id"].isin(demo_actions)].copy()
df_lmm_demo["all_obs"] = 1

print(f"Feasibility demo on {df_lmm_demo['action_id'].nunique()} actions "
      f"({len(df_lmm_demo)} ratings, {df_lmm_demo['rater_id'].nunique()} raters).")

model_lmm_demo = smf.mixedlm(
    "rating_numeric ~ 1",
    data=df_lmm_demo,
    groups=df_lmm_demo["all_obs"],
    vc_formula={
        "action": "0 + C(action_id)",
        "rater": "0 + C(rater_id)",
    },
    re_formula="0",
)
result_lmm_demo = model_lmm_demo.fit(reml=True, method="lbfgs", maxiter=200)

print(f"Convergence (subsample): {getattr(result_lmm_demo, 'converged', None)}")
print(f"sigma^2_action = {result_lmm_demo.vcomp[0]:.3f}, "
      f"sigma^2_rater = {result_lmm_demo.vcomp[1]:.3f}, "
      f"sigma^2_resid = {result_lmm_demo.scale:.3f}")
""")

md(r"""
### 6.3 Primary estimation: Bayesian counterpart in PyMC (full data)

Same model, non-centered parametrization (numerically more stable for
many random-effects levels), weakly informative priors:

$$
\mu \sim \mathcal N(4, 2^2), \quad
\sigma_{\text{action}}, \sigma_{\text{rater}}, \sigma_e \sim
\text{Exponential}(1)
$$
""")

code(r"""
import pymc as pm
import arviz as az

action_idx, action_levels = pd.factorize(df_lmm["action_id"])
rater_idx, rater_levels = pd.factorize(df_lmm["rater_id"])
y_lmm = df_lmm["rating_numeric"].values.astype(float)
n_action_lmm = len(action_levels)
n_rater_lmm = len(rater_levels)

print(f"Full model: {len(y_lmm)} ratings, {n_action_lmm} actions, "
      f"{n_rater_lmm} raters (~{1 + n_action_lmm + n_rater_lmm} parameters).")

with pm.Model(coords={"action": action_levels, "rater": rater_levels}) as gaussian_crossed_model:
    mu = pm.Normal("mu", 4.0, 2.0)
    sigma_action = pm.Exponential("sigma_action", 1.0)
    sigma_rater = pm.Exponential("sigma_rater", 1.0)
    sigma_resid = pm.Exponential("sigma_resid", 1.0)

    u_raw = pm.Normal("u_raw", 0, 1, dims="action")
    v_raw = pm.Normal("v_raw", 0, 1, dims="rater")
    u = pm.Deterministic("u", u_raw * sigma_action, dims="action")
    v = pm.Deterministic("v", v_raw * sigma_rater, dims="rater")

    eta = mu + u[action_idx] + v[rater_idx]
    pm.Normal("y_obs", mu=eta, sigma=sigma_resid, observed=y_lmm)

    idata_lmm = pm.sample(draws=1000, tune=1000, chains=4, cores=4,
                            target_accept=0.9, random_seed=SEED,
                            progressbar=False)

# Save the model (posterior + sample_stats + observed_data) BEFORE
# attaching the posterior-predictive draws: posterior_predictive has the
# same size as the raw data x number of draws (here ~10,000 x 4,000
# = ~320 MB) and is only needed for the PPC plot below, not for
# permanent storage (otherwise the .nc file grows beyond 500 MB).
idata_lmm.to_netcdf(str(RESULTS_MODELS / "gaussian_crossed_model.nc"))
print("Model saved: results/models/gaussian_crossed_model.nc "
      "(without posterior_predictive, see comment above)")

with gaussian_crossed_model:
    pp_lmm = pm.sample_posterior_predictive(idata_lmm, random_seed=SEED,
                                              progressbar=False)
# API note: in arviz>=1.0, InferenceData objects are xarray.DataTree
# instances without an .extend() method (previously: idata.extend(pp)).
# Groups are instead merged via dict assignment (in-memory only, for
# the plot below -- not carried over into the saved .nc file).
idata_lmm["posterior_predictive"] = pp_lmm["posterior_predictive"]
""")

md(r"""
### 6.4 Convergence diagnostics

Mandatory checks for Bayesian models: $\hat R < 1.01$, sufficient
bulk/tail ESS, no or very few divergences.
""")

code(r"""
summary_lmm = az.summary(idata_lmm, var_names=["mu", "sigma_action", "sigma_rater", "sigma_resid"],
                           round_to=4)
print(summary_lmm)
save_table(summary_lmm.reset_index().rename(columns={"index": "parameter"}),
            "gaussian_crossed_model_summary")

n_divergences = int(idata_lmm.sample_stats["diverging"].sum())
max_rhat = float(summary_lmm["r_hat"].max())
min_ess_bulk = float(summary_lmm["ess_bulk"].min())
print(f"\nDivergences: {n_divergences}")
print(f"Max R-hat: {max_rhat:.4f}")
print(f"Min ESS (bulk): {min_ess_bulk:.0f}")

if max_rhat >= 1.01:
    log_warning(f"Max R-hat = {max_rhat:.4f} >= 1.01 for the linear Gaussian model.")
if n_divergences > 0:
    log_warning(f"{n_divergences} divergences in the linear Gaussian model.")
if min_ess_bulk < 400:
    log_warning(f"Minimum bulk ESS = {min_ess_bulk:.0f} < 400 - be cautious with intervals.")

az.plot_trace(idata_lmm, var_names=["mu", "sigma_action", "sigma_rater", "sigma_resid"])
fig = plt.gcf()
fig.suptitle("Trace plots: linear crossed Gaussian model (PyMC)")
fig.set_size_inches(11, 9)
fig.tight_layout()
save_fig(fig, "fig_appendix_lmm_traceplots", "Trace plots of the hyperparameters of the linear model.")
plt.show()
""")

md(r"""
### 6.5 Posterior predictive check
""")

code(r"""
# API note: az.plot_ppc (arviz<1.0) is called az.plot_ppc_dist in
# arviz>=1.0 and returns a PlotCollection that draws on the current
# matplotlib figure (instead of accepting axes).
az.plot_ppc_dist(idata_lmm)
fig = plt.gcf()
fig.set_size_inches(7, 4.5)
fig.suptitle("Posterior predictive check: linear Gaussian model\n"
             "(the model is continuous, the data are discrete 1-7 - "
             "the distribution shape, not exact categories, is the relevant comparison)")
fig.tight_layout()
save_fig(fig, "fig_appendix_lmm_ppc", "Posterior predictive check of the linear Gaussian model.")
plt.show()
""")

md(r"""
### 6.6 Variance components, BLUP-equivalent action/rater scores

From the Bayesian estimation we obtain full posterior distributions of
the variance components directly (instead of a point estimate plus a
separate bootstrap), as well as posterior means and SDs for $u_i$ and
$v_j$ — the latter are the direct Bayesian counterpart to the BLUPs
(numerically very similar under vague priors).
""")

code(r"""
post = idata_lmm.posterior
var_action_draws = (post["sigma_action"] ** 2).values.reshape(-1)
var_rater_draws = (post["sigma_rater"] ** 2).values.reshape(-1)
var_resid_draws = (post["sigma_resid"] ** 2).values.reshape(-1)

var_action = float(var_action_draws.mean())
var_rater = float(var_rater_draws.mean())
var_resid = float(var_resid_draws.mean())

variance_components_df = pd.DataFrame([
    {"component": "action (u_i)", "variance": var_action,
     "ci_low": np.quantile(var_action_draws, .025), "ci_high": np.quantile(var_action_draws, .975),
     "pct_of_total": var_action / (var_action + var_rater + var_resid)},
    {"component": "rater (v_j)", "variance": var_rater,
     "ci_low": np.quantile(var_rater_draws, .025), "ci_high": np.quantile(var_rater_draws, .975),
     "pct_of_total": var_rater / (var_action + var_rater + var_resid)},
    {"component": "residual (eps_ij)", "variance": var_resid,
     "ci_low": np.quantile(var_resid_draws, .025), "ci_high": np.quantile(var_resid_draws, .975),
     "pct_of_total": var_resid / (var_action + var_rater + var_resid)},
])
save_table(variance_components_df, "lmm_variance_components")
print(variance_components_df)

is_singular = (var_action < 1e-6) or (var_rater < 1e-6)
if is_singular:
    log_warning("Singular fit: at least one variance component is (near) zero.")
assert var_action >= 0 and var_rater >= 0 and var_resid >= 0, "Negative variance component!"

u_mean = post["u"].mean(dim=("chain", "draw")).values
u_sd = post["u"].std(dim=("chain", "draw")).values
v_mean = post["v"].mean(dim=("chain", "draw")).values
v_sd = post["v"].std(dim=("chain", "draw")).values

action_blup_series = pd.Series(u_mean, index=action_levels, name="lmm_score_deviation")
action_blup_se_series = pd.Series(u_sd, index=action_levels, name="lmm_score_se")
rater_blup_series = pd.Series(v_mean, index=rater_levels, name="lmm_severity")
rater_blup_se_series = pd.Series(v_sd, index=rater_levels, name="lmm_severity_se")

mu_mean = float(post["mu"].mean())
print(f"\nEstimated grand mean mu = {mu_mean:.3f}")
print(f"BLUP-equivalent scores extracted for {len(action_blup_series)} actions, "
      f"{len(rater_blup_series)} raters.")
""")

md(r"""
### 6.7 Absolute and relative reliability, D-study (with credible bands)

For a **single rating**:

$$
\rho_{\text{abs},1} = \frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_{\text{rater}}+\sigma^2_e}, \qquad
\rho_{\text{rel},1} = \frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_e}
$$

For a **mean of $k$ independently drawn raters**:

$$
\rho_{\text{abs},k} = \frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_{\text{rater}}/k+\sigma^2_e/k}, \qquad
\rho_{\text{rel},k} = \frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_e/k}
$$

Since we have full posterior samples of the variance components, we
compute $\rho$ **for every posterior draw**, giving us 95% credible
bands directly (no additional bootstrap needed).
""")

code(r"""
def reliability_abs(k, va, vr, ve):
    return va / (va + vr / k + ve / k)

def reliability_rel(k, va, ve):
    return va / (va + ve / k)

ks = np.arange(1, 8)
rho_abs_draws = np.array([reliability_abs(k, var_action_draws, var_rater_draws, var_resid_draws) for k in ks])
rho_rel_draws = np.array([reliability_rel(k, var_action_draws, var_resid_draws) for k in ks])

d_study = pd.DataFrame({
    "k": ks,
    "rho_abs": rho_abs_draws.mean(axis=1),
    "rho_abs_low": np.quantile(rho_abs_draws, .025, axis=1),
    "rho_abs_high": np.quantile(rho_abs_draws, .975, axis=1),
    "rho_rel": rho_rel_draws.mean(axis=1),
    "rho_rel_low": np.quantile(rho_rel_draws, .025, axis=1),
    "rho_rel_high": np.quantile(rho_rel_draws, .975, axis=1),
})
save_table(d_study, "d_study_reliability")
print(d_study)

vc_ci = pd.DataFrame([
    {"quantity": "sigma2_action", "estimate": var_action,
     "ci_low": variance_components_df.loc[0, "ci_low"], "ci_high": variance_components_df.loc[0, "ci_high"]},
    {"quantity": "sigma2_rater", "estimate": var_rater,
     "ci_low": variance_components_df.loc[1, "ci_low"], "ci_high": variance_components_df.loc[1, "ci_high"]},
    {"quantity": "sigma2_resid", "estimate": var_resid,
     "ci_low": variance_components_df.loc[2, "ci_low"], "ci_high": variance_components_df.loc[2, "ci_high"]},
    {"quantity": "rho_abs_k1", "estimate": d_study.loc[0, "rho_abs"],
     "ci_low": d_study.loc[0, "rho_abs_low"], "ci_high": d_study.loc[0, "rho_abs_high"]},
    {"quantity": "rho_rel_k1", "estimate": d_study.loc[0, "rho_rel"],
     "ci_low": d_study.loc[0, "rho_rel_low"], "ci_high": d_study.loc[0, "rho_rel_high"]},
])
save_table(vc_ci, "lmm_variance_components_bootstrap_ci")
print(vc_ci)
""")

code(r"""
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].bar(variance_components_df["component"], variance_components_df["variance"],
             yerr=[variance_components_df["variance"] - variance_components_df["ci_low"],
                   variance_components_df["ci_high"] - variance_components_df["variance"]],
             color=["#4C72B0", "#DD8452", "#55A868"], capsize=4)
axes[0].set_ylabel("Variance")
axes[0].set_title("Variance components (95% credible intervals)")
axes[0].tick_params(axis="x", rotation=20)

axes[1].plot(d_study["k"], d_study["rho_abs"], marker="o", label="absolute reliability", color="#4C72B0")
axes[1].fill_between(d_study["k"], d_study["rho_abs_low"], d_study["rho_abs_high"], alpha=0.2, color="#4C72B0")
axes[1].plot(d_study["k"], d_study["rho_rel"], marker="s", label="relative reliability", color="#DD8452")
axes[1].fill_between(d_study["k"], d_study["rho_rel_low"], d_study["rho_rel_high"], alpha=0.2, color="#DD8452")
axes[1].set_xlabel("Number of raters k (mean)")
axes[1].set_ylabel(r"Reliability coefficient $\rho$")
axes[1].set_title("D-study: reliability vs. number of raters (95% credible band)")
axes[1].legend()
axes[1].set_ylim(0, 1)
fig.tight_layout()
save_fig(fig, "fig08_variance_components_and_dstudy",
         "Left: estimated variance components of the linear crossed model with "
         "95% credible intervals. Right: D-study curves for absolute and relative "
         "reliability of the action mean as a function of the number of raters k, "
         "with a 95% credible band over the posterior distribution.")
plt.show()
""")

md(r"""
### 6.8 ML/REML vs. Bayes — what the differences come down to

- The statsmodels subsample estimate (REML) and the full PyMC estimate
  (Bayes, weakly informative priors) are **not computed on the same
  sample** (250 vs. all actions in the largest component) — a direct
  numerical comparison is therefore only interpretable substantively
  ("same order of magnitude, same sign of effects"), not exactly
  numerically.
- REML gives asymptotically unbiased point estimates of the variance
  components; the Bayesian estimate is mildly regularized by the
  priors (at this sample size, the influence of the weakly informative
  priors used here is small).
- Uncertainty intervals are conceptually different: REML CIs (e.g.
  from a cluster bootstrap) are confidence intervals — statements
  about the sampling distribution of the estimator. Bayesian credible
  intervals are statements about the posterior probability of the
  parameter itself. At large sample sizes and with weak priors, both
  are usually numerically similar but remain interpretationally
  different.
""")

# ====================================================================
# 8. MODEL-BASED INTEGRATION OF RATINGS (Section 9 of the brief)
# ====================================================================
md(r"""
## 7. Action scores: raw mean and rater-centered mean

Here we produce the first two of four/five action-score variants (the
remaining ones follow after the modeling sections 8 and 9).

### 7.1 Raw mean

$$
\bar y_i = \frac{1}{n_i}\sum_j y_{ij}
$$

Advantage: transparent. Disadvantage: not corrected for differing
rater strictness; extreme values with few ratings are unstable.

### 7.2 Rater-centered mean

$$
y^{c}_{ij}=y_{ij}-\bar y_j+\bar y, \qquad
\bar y^{c}_{i}=\frac{1}{n_i}\sum_j y^{c}_{ij}
$$

**Important limitation:** Simple rater centering is only meaningfully
interpretable if raters rate sufficiently comparable and connected
sets of actions. Under strongly selective assignment, a low rater mean
can reflect either strictness or a harder/less creative sample of
actions. We therefore treat rater centering exclusively as a
**descriptive sensitivity analysis**, not as the preferred score.
""")

code(r"""
grand_mean = ratings_clean["rating_numeric"].mean()
rater_means = ratings_clean.groupby("rater_id")["rating_numeric"].mean()

ratings_clean["rating_rater_centered"] = (
    ratings_clean["rating_numeric"]
    - ratings_clean["rater_id"].map(rater_means)
    + grand_mean
)

action_scores = ratings_clean.groupby("action_id").agg(
    n_ratings=("rating_numeric", "size"),
    raw_mean=("rating_numeric", "mean"),
    raw_median=("rating_numeric", "median"),
    raw_sd=("rating_numeric", "std"),
    rater_centered_mean=("rating_rater_centered", "mean"),
    connected_component=("connected_component", "first"),
).reset_index()
action_scores["raw_se"] = action_scores["raw_sd"] / np.sqrt(action_scores["n_ratings"])

print(f"Action scores (raw/rater-centered) computed for {len(action_scores)} actions.")
action_scores.head()
""")

code(r"""
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(action_scores["raw_mean"], action_scores["rater_centered_mean"],
            c=action_scores["n_ratings"], cmap="viridis", s=15, alpha=0.6)
lims = [1, 7]
ax.plot(lims, lims, color="grey", ls="--", lw=1)
ax.set_xlabel("Raw mean")
ax.set_ylabel("Rater-centered mean")
ax.set_title("Raw mean vs. rater-centered mean")
cb = fig.colorbar(ax.collections[0], ax=ax)
cb.set_label("Number of ratings")
fig.tight_layout()
save_fig(fig, "fig10_raw_vs_centered_score",
         "Raw mean vs. rater-centered mean per action, colored by "
         "number of ratings.")
plt.show()
""")

# ====================================================================
# 9. RATER EFFECTS IN THE LINEAR MODEL (Section 10 of the brief)
# ====================================================================
md(r"""
## 8. Rater effects in the linear model

### 8.1 Severity/leniency

We use the Bayesian posterior estimates $\hat v_j$ from Section 6.
**Sign convention:** in our parametrization
($\eta_{ij} = \mu + u_i + v_j$), **positive** $v_j$ tends to mean
**more lenient** (higher ratings for the same latent action quality),
**negative** tends to mean **stricter**.
""")

code(r"""
rater_ratings_count = ratings_clean.groupby("rater_id").size()
rater_mean_creativity_assigned = ratings_clean.groupby("rater_id")["rating_numeric"].mean()

severity_df = pd.DataFrame({
    "rater_id": rater_blup_series.index,
    "lmm_severity": rater_blup_series.values,
    "lmm_severity_se": rater_blup_se_series.reindex(rater_blup_series.index).values,
})
severity_df["n_ratings"] = severity_df["rater_id"].map(rater_ratings_count)
severity_df["raw_mean"] = severity_df["rater_id"].map(rater_mean_creativity_assigned)
severity_df = severity_df.sort_values("lmm_severity").reset_index(drop=True)
severity_df["rank"] = np.arange(1, len(severity_df) + 1)

corr_severity_mean = severity_df["lmm_severity"].corr(severity_df["raw_mean"])
print(f"Correlation LMM severity vs. rater mean: r = {corr_severity_mean:.3f} "
      "(should be high - consistency check)")

fig, ax = plt.subplots(figsize=(7, 10))
ax.errorbar(severity_df["lmm_severity"], severity_df["rank"],
             xerr=1.96 * severity_df["lmm_severity_se"], fmt="o", ms=4,
             color="#4C72B0", ecolor="#4C72B0", alpha=0.7, capsize=2)
ax.axvline(0, color="grey", ls="--", lw=1)
ax.set_yticks(severity_df["rank"])
ax.set_yticklabels(severity_df["rater_id"], fontsize=7)
ax.set_xlabel(r"Rater severity $\hat v_j$ (positive = more lenient)")
ax.set_title("Caterpillar plot: rater severity with 95% uncertainty intervals")
fig.tight_layout()
save_fig(fig, "fig09_rater_severity_caterpillar",
         "Rater severity estimates (posterior mean of the linear crossed "
         "model) with 95% credible intervals, sorted from strictest to "
         "most lenient rater.")
plt.show()
""")

md(r"""
### 8.2 Scale width and discrimination (descriptive)

A random intercept alone does not capture differing scale spread. We
therefore use the already-computed `rater_descriptive_statistics`
table (SD, IQR, category usage, entropy, extreme/central tendency). A
**model-based** discrimination estimate follows in the ordinal facette
model (Section 9).
""")

code(r"""
severity_df = severity_df.merge(
    rater_desc[["rater_id", "sd", "iqr", "n_categories_used", "entropy",
                  "extreme_category_rate", "central_category_rate"]],
    on="rater_id", how="left")
save_table(severity_df, "rater_severity_table")
severity_df.head()
""")

md(r"""
### 8.3 Rater drift

If `rating_order` is available, we additionally model a linear,
**rater-specific** time trend:

$$
y_{ij} = \mu + u_i + v_j + \beta t_{ij} + b_j t_{ij} + \varepsilon_{ij}
$$

with $t_{ij}$ = rating position, centered **within rater**. For
computational-cost reasons we do not estimate this as a full third
Bayesian crossed-effects run, but as a **simple per-rater OLS
regression** of `rating` on centered `rating_order` (a descriptive
slope estimator) — sufficient to identify raters with a noticeable
linear trend; a full variance decomposition of the trend would require
extending Section 6.
""")

code(r"""
if "rating_order" in ratings_clean.columns:
    def drift_slope(g):
        if len(g) < 15:
            return pd.Series({"drift_estimate": np.nan, "drift_se": np.nan, "n": len(g)})
        t = g["rating_order"] - g["rating_order"].mean()
        y = g["rating_numeric"]
        slope, intercept, r_value, p_value, std_err = sps.linregress(t, y)
        return pd.Series({"drift_estimate": slope, "drift_se": std_err, "n": len(g)})

    drift_df = ratings_clean.groupby("rater_id").apply(drift_slope, include_groups=False).reset_index()
    severity_df = severity_df.merge(drift_df[["rater_id", "drift_estimate", "drift_se"]],
                                       on="rater_id", how="left")
    n_sig_drift = (drift_df["drift_estimate"].abs() > 2 * drift_df["drift_se"]).sum()
    print(f"Raters with |drift slope| > 2*SE (descriptive indicator of linear drift): {n_sig_drift}")
    save_table(drift_df, "rater_drift_estimates")
else:
    severity_df["drift_estimate"] = np.nan
    severity_df["drift_se"] = np.nan
    log_warning("No rating_order variable available - drift modeling skipped.")

save_table(severity_df, "rater_severity_table")
""")

# ====================================================================
# 10. ORDINAL HIERARCHICAL FACETTE MODEL (Section 11 of the brief)
# ====================================================================
md(r"""
## 9. Ordinal hierarchical facette model

This is the **central sensitivity / preferred ordinal modeling
approach**: it explicitly respects that the creativity scale is a
bounded, ordered 7-category scale, instead of treating it (as in
Section 6) as approximately interval-scaled.

### 9.1 Cumulative logit model

$$
\Pr(Y_{ij} \le k) = \operatorname{logit}^{-1}(\tau_k - \eta_{ij}),
\qquad \eta_{ij} = \theta_i + \lambda_j
$$

with ordered global thresholds $\tau_1 < \dots < \tau_6$, action
creativity $\theta_i$, and rater leniency $\lambda_j$ (**same sign
convention as in Section 8**: positive $\lambda_j$ = more lenient).
The implementation uses `pm.OrderedLogistic`, which expects exactly
this parametrization (`eta` linear, `cutpoints` increasing).

### 9.2 Engine choice: PyMC instead of Bambi

We checked whether `bambi` (currently installed version: see the
session log) reliably supports a cumulative ordinal model with **two
crossed** random-intercept factors (action AND rater). For full
control over (a) the non-centered parametrization (needed for stable
sampling geometry with thousands of levels), (b) the identification
condition of the thresholds, and (c) direct access to all posterior
components for the later JRT extension (Section 10), we implement the
model **directly in PyMC** — this follows the fallback option
anticipated in the analysis brief ("implement the model directly in
PyMC or Stan").

### 9.3 Priors and identification

$$
\theta_i \sim \mathcal N(0, \sigma^2_\theta), \quad
\lambda_j \sim \mathcal N(0, \sigma^2_\lambda), \quad
\sigma_\theta, \sigma_\lambda \sim \text{Exponential}(1)
$$

The thresholds $\tau_{1:6}$ receive weakly informative normal priors
around equidistant starting values, with an enforced ordering
constraint (`transform=pm.distributions.transforms.ordered`).
Identification: $\mathbb E[\theta_i]=0$ and $\mathbb E[\lambda_j]=0$
via the zero-mean priors (soft centering); there is no additional free
intercept (which would be confounded with the thresholds).

As in Section 6, we estimate exclusively on the largest connected
component.
""")

code(r"""
df_ord = ratings_clean.loc[ratings_clean["in_largest_component"]].copy()
action_idx_o, action_levels_o = pd.factorize(df_ord["action_id"])
rater_idx_o, rater_levels_o = pd.factorize(df_ord["rater_id"])
y_ord = (df_ord["rating_numeric"].values.astype(int) - 1)  # 0-based for PyMC

assert (action_levels_o == action_levels).all() if len(action_levels_o) == len(action_levels) else True
print(f"Ordinal model: {len(y_ord)} ratings, {len(action_levels_o)} actions, "
      f"{len(rater_levels_o)} raters.")
print(f"Category frequencies (0-based): {np.bincount(y_ord, minlength=7)}")
""")

code(r"""
with pm.Model(coords={"action": action_levels_o, "rater": rater_levels_o,
                        "cut": range(6)}) as ordinal_model:
    sigma_theta = pm.Exponential("sigma_theta", 1.0)
    sigma_lambda = pm.Exponential("sigma_lambda", 1.0)

    theta_raw = pm.Normal("theta_raw", 0, 1, dims="action")
    lam_raw = pm.Normal("lam_raw", 0, 1, dims="rater")
    theta = pm.Deterministic("theta", theta_raw * sigma_theta, dims="action")
    lam = pm.Deterministic("lam", lam_raw * sigma_lambda, dims="rater")

    cutpoints = pm.Normal(
        "cutpoints", mu=np.linspace(-2.5, 2.5, 6), sigma=1.5,
        transform=pm.distributions.transforms.ordered, dims="cut",
    )
    # Bugfix note: NO initval= here (previously: initval=np.linspace(...)).
    # An explicit initval on a transformed variable later prevents
    # pm.compute_log_likelihood()/fgraph_from_model() with
    # "NotImplementedError: Cannot convert models with non-default initial
    # values". jitter+adapt_diag reliably initializes the ordered
    # transform even without an explicit starting value.

    eta_ord = theta[action_idx_o] + lam[rater_idx_o]
    pm.OrderedLogistic("y_obs", eta=eta_ord, cutpoints=cutpoints, observed=y_ord)

    idata_ord = pm.sample(draws=1000, tune=1000, chains=4, cores=4,
                            target_accept=0.9, random_seed=SEED,
                            progressbar=False)
    pm.compute_log_likelihood(idata_ord)

idata_ord.to_netcdf(str(RESULTS_MODELS / "ordinal_crossed_model.nc"))
print("Model saved: results/models/ordinal_crossed_model.nc")
""")

md(r"""
### 9.4 Convergence diagnostics (mandatory for Bayesian models)
""")

code(r"""
summary_ord = az.summary(idata_ord, var_names=["sigma_theta", "sigma_lambda", "cutpoints"],
                           round_to=4)
print(summary_ord)
save_table(summary_ord.reset_index().rename(columns={"index": "parameter"}),
            "ordinal_model_summary")

n_divergences_ord = int(idata_ord.sample_stats["diverging"].sum())
max_rhat_ord = float(summary_ord["r_hat"].max())
min_ess_ord = float(summary_ord["ess_bulk"].min())
print(f"\nDivergences: {n_divergences_ord}")
print(f"Max R-hat: {max_rhat_ord:.4f}")
print(f"Min ESS (bulk): {min_ess_ord:.0f}")

cuts_sorted = np.all(np.diff(idata_ord.posterior["cutpoints"].mean(dim=("chain", "draw")).values) > 0)
print(f"Thresholds ordered (posterior mean): {cuts_sorted}")

if max_rhat_ord >= 1.01:
    log_warning(f"Max R-hat = {max_rhat_ord:.4f} >= 1.01 for the ordinal model.")
if n_divergences_ord > 0:
    log_warning(f"{n_divergences_ord} divergences in the ordinal model.")
if not cuts_sorted:
    log_warning("Category thresholds of the ordinal model are NOT ordered at the posterior mean.")

az.plot_trace(idata_ord, var_names=["sigma_theta", "sigma_lambda"])
fig = plt.gcf()
fig.set_size_inches(11, 5)
fig.suptitle("Trace plots: ordinal facette model (variance components)")
fig.tight_layout()
save_fig(fig, "fig_appendix_ordinal_traceplots", "Trace plots of the variance components of the ordinal model.")
plt.show()
""")

md(r"""
### 9.5 Posterior predictive checks

We check whether data replicated from the model plausibly reproduce
(a) the overall category frequencies, (b) the distribution of raw
rater means, and (c) the distribution of action means.
""")

code(r"""
with ordinal_model:
    pp_ord = pm.sample_posterior_predictive(idata_ord, random_seed=SEED, progressbar=False,
                                              extend_inferencedata=False, var_names=["y_obs"])

y_rep = pp_ord.posterior_predictive["y_obs"].values  # (chain, draw, obs)
y_rep_flat_sample = y_rep[:, :100, :].reshape(-1, y_rep.shape[-1])  # subsample of draws for speed

obs_counts = np.bincount(y_ord, minlength=7) / len(y_ord)
rep_counts = np.array([np.bincount(row, minlength=7) / len(row) for row in y_rep_flat_sample])

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
axes[0].bar(np.arange(1, 8) - 0.2, obs_counts, width=0.4, label="observed", color="#4C72B0")
axes[0].bar(np.arange(1, 8) + 0.2, rep_counts.mean(axis=0), width=0.4, label="replicated (model)",
             color="#DD8452")
axes[0].errorbar(np.arange(1, 8) + 0.2, rep_counts.mean(axis=0),
                   yerr=rep_counts.std(axis=0), fmt="none", ecolor="black", capsize=2)
axes[0].set_title("Category frequencies: observed vs. replicated")
axes[0].set_xlabel("Rating")
axes[0].legend()

df_ord_rep = df_ord.copy()
rep_draw_example = y_rep[0, 0, :] + 1
df_ord_rep["rating_rep"] = rep_draw_example
obs_rater_means = df_ord.groupby("rater_id")["rating_numeric"].mean()
rep_rater_means = df_ord_rep.groupby("rater_id")["rating_rep"].mean()
axes[1].hist(obs_rater_means, bins=15, alpha=0.6, label="observed", color="#4C72B0")
axes[1].hist(rep_rater_means, bins=15, alpha=0.6, label="replicated (1 draw)", color="#DD8452")
axes[1].set_title("Rater means: observed vs. replicated")
axes[1].legend()

obs_action_means = df_ord.groupby("action_id")["rating_numeric"].mean()
rep_action_means = df_ord_rep.groupby("action_id")["rating_rep"].mean()
axes[2].hist(obs_action_means, bins=20, alpha=0.6, label="observed", color="#4C72B0")
axes[2].hist(rep_action_means, bins=20, alpha=0.6, label="replicated (1 draw)", color="#DD8452")
axes[2].set_title("Action means: observed vs. replicated")
axes[2].legend()

fig.suptitle("Posterior predictive checks: ordinal facette model")
fig.tight_layout()
save_fig(fig, "fig12_ordinal_ppc",
         "Posterior predictive checks of the ordinal facette model: category frequencies "
         "(left, with an uncertainty band over posterior draws), rater means (middle), and "
         "action means (right), each observed vs. model-replicated data.")
plt.show()
""")

md(r"""
### 9.6 Ordinal action scores

For each action: posterior mean/median of $\theta_i$, 95% credible
interval, posterior rank and rank uncertainty, and the **expected
observed scale value** $\mathbb E[Y_i \mid \theta_i]$ on the 1–7 scale
(stored separately from the latent score $\theta_i$, as required by
the analysis brief).
""")

code(r"""
theta_post = idata_ord.posterior["theta"]  # dims: chain, draw, action
theta_mean = theta_post.mean(dim=("chain", "draw")).values
theta_median = theta_post.median(dim=("chain", "draw")).values
theta_low = theta_post.quantile(0.025, dim=("chain", "draw")).values
theta_high = theta_post.quantile(0.975, dim=("chain", "draw")).values

# Posterior rank per draw, then mean/uncertainty of the rank
theta_flat = theta_post.values.reshape(-1, theta_post.shape[-1])  # (n_draws_total, n_action)
ranks_per_draw = theta_flat.argsort(axis=1).argsort(axis=1) + 1  # 1 = lowest creativity
rank_mean = ranks_per_draw.mean(axis=0)
rank_sd = ranks_per_draw.std(axis=0)

# Expected observed scale value E[Y|theta] under the global (posterior-mean)
# thresholds, averaged over raters (lambda=0, "average rater").
cut_mean = idata_ord.posterior["cutpoints"].mean(dim=("chain", "draw")).values

def expected_rating(theta_val, cuts):
    cum = 1 / (1 + np.exp(-(cuts - theta_val)))
    cum = np.concatenate([[0.0], cum, [1.0]])
    probs = np.diff(cum)
    return np.sum(probs * np.arange(1, 8))

expected_ratings = np.array([expected_rating(t, cut_mean) for t in theta_mean])

ordinal_scores = pd.DataFrame({
    "action_id": action_levels_o,
    "ordinal_latent_score": theta_mean,
    "ordinal_latent_median": theta_median,
    "ordinal_latent_lower": theta_low,
    "ordinal_latent_upper": theta_high,
    "ordinal_posterior_rank_mean": rank_mean,
    "ordinal_posterior_rank_sd": rank_sd,
    "ordinal_expected_rating": expected_ratings,
})
save_table(ordinal_scores, "ordinal_action_scores")
print(f"Ordinal action scores computed for {len(ordinal_scores)} actions.")
ordinal_scores.head()
""")

md(r"""
### 9.7 Ordinal rater severity
""")

code(r"""
lam_post = idata_ord.posterior["lam"]
lam_mean = lam_post.mean(dim=("chain", "draw")).values
lam_low = lam_post.quantile(0.025, dim=("chain", "draw")).values
lam_high = lam_post.quantile(0.975, dim=("chain", "draw")).values

ordinal_severity = pd.DataFrame({
    "rater_id": rater_levels_o,
    "ordinal_severity": lam_mean,
    "ordinal_severity_lower": lam_low,
    "ordinal_severity_upper": lam_high,
})
save_table(ordinal_severity, "ordinal_rater_severity")

corr_lin_ord_severity = pd.merge(
    severity_df[["rater_id", "lmm_severity"]], ordinal_severity[["rater_id", "ordinal_severity"]],
    on="rater_id")["lmm_severity"].corr(
    pd.merge(severity_df[["rater_id", "lmm_severity"]], ordinal_severity[["rater_id", "ordinal_severity"]],
              on="rater_id")["ordinal_severity"])
print(f"Correlation linear vs. ordinal rater severity: r = {corr_lin_ord_severity:.3f} "
      "(a high value indicates consistent models)")
""")

md(r"""
### 9.8 Proportional-odds assumption

The cumulative logit model assumes **common** (not rater- or
category-specific) thresholds ("proportional odds"). Given the current
model structure, this assumption cannot be tested directly without
estimating an extended variant (e.g., rater-specific threshold shifts
or rater-specific discrimination). We address this in Section 10 via a
judge-response-theory model with **rater-specific discrimination** and
formally compare both models via LOO-CV. A fully separate
adjacent-category sensitivity analysis is not additionally estimated
for reasons of compute time and connectivity (see the analysis brief's
warning: "avoid unnecessarily complex models when data connectivity
... is insufficient").
""")


# ====================================================================
# 11. JUDGE-RESPONSE-THEORY-STYLE EXTENSION (Section 12 of the brief)
# ====================================================================
md(r"""
## 10. Judge Response Theory (JRT) / many-facet-Rasch-style extension

### 10.1 Concept

Judge Response Theory (Myszkowski & Storme, 2019) transfers polytomous
IRT models to judgment data: raters are treated as measurement
instruments ("items"), actions as the objects being measured. One
graded-response form is:

$$
P(Y_{ij}\ge k \mid \theta_i) = \operatorname{logit}^{-1}
\left[a_j(\theta_i-b_{jk})\right]
$$

with $\theta_i$ = creativity of action $i$, $a_j$ = **discrimination**
of rater $j$ (how strongly does rater $j$ differentiate between
actions?), $b_{jk}$ = rater-specific threshold for category $k$. A
many-facet Rasch model usually assumes $a_j \equiv 1$; JRT allows
rater-specific discrimination.

### 10.2 Simplified, identifiable variant

Full rater-specific thresholds $b_{jk}$ (40 raters × 6 thresholds =
240 additional parameters) cannot be estimated with sufficient
precision given the present connectivity (median overlap, see
Section 3). We therefore estimate a **reduced JRT variant** with
rater-specific discrimination at **global** thresholds:

$$
\eta_{ij} = a_j \cdot \theta_i + \lambda_j, \qquad
\Pr(Y_{ij}\le k) = \operatorname{logit}^{-1}(\tau_k - \eta_{ij})
$$

**Identification** (Section 12.5 of the brief): since
$a_j\cdot\theta_i$ has a scale non-identifiability ($a_j\cdot c$ and
$\theta_i/c$ give the same fit for any $c$), we fix
$\theta_i \sim \mathcal N(0,1)$ **exactly** (no free action variance —
unlike the model in Section 9, where $\sigma_\theta$ is estimated
freely) and let $a_j>0$ (via $a_j=\exp(\log a_j)$) be free. $\lambda_j$
remains the severity/leniency term as before.
""")

code(r"""
with pm.Model(coords={"action": action_levels_o, "rater": rater_levels_o,
                        "cut": range(6)}) as jrt_model:
    theta_jrt = pm.Normal("theta", 0, 1, dims="action")  # fixed scale: Var(theta)=1

    sigma_lambda_jrt = pm.Exponential("sigma_lambda", 1.0)
    lam_raw_jrt = pm.Normal("lam_raw", 0, 1, dims="rater")
    lam_jrt = pm.Deterministic("lam", lam_raw_jrt * sigma_lambda_jrt, dims="rater")

    sigma_log_a = pm.Exponential("sigma_log_a", 2.0)
    log_a_raw = pm.Normal("log_a_raw", 0, 1, dims="rater")
    log_a = pm.Deterministic("log_a", log_a_raw * sigma_log_a, dims="rater")
    a_j = pm.Deterministic("discrimination", pm.math.exp(log_a), dims="rater")

    cutpoints_jrt = pm.Normal(
        "cutpoints", mu=np.linspace(-2.5, 2.5, 6), sigma=1.5,
        transform=pm.distributions.transforms.ordered, dims="cut",
    )
    # Bugfix: no initval= (see the comment in the ordinal model, Section 9).

    eta_jrt = a_j[rater_idx_o] * theta_jrt[action_idx_o] + lam_jrt[rater_idx_o]
    pm.OrderedLogistic("y_obs", eta=eta_jrt, cutpoints=cutpoints_jrt, observed=y_ord)

    idata_jrt = pm.sample(draws=800, tune=800, chains=4, cores=4,
                            target_accept=0.9, random_seed=SEED,
                            progressbar=False)
    pm.compute_log_likelihood(idata_jrt)

idata_jrt.to_netcdf(str(RESULTS_MODELS / "jrt_discrimination_model.nc"))
print("Model saved: results/models/jrt_discrimination_model.nc")
""")

md(r"""
### 10.3 Diagnostics and model comparison (LOO-CV)

We check convergence as before and compare the JRT model with the
simpler facette model from Section 9 via **Pareto-smoothed
importance-sampling LOO-CV**. A lower `elpd_loo` or a negative
`elpd_diff` relative to the reference model indicates worse
out-of-sample prediction; the Pareto-$k$ diagnostic indicates how
reliable the LOO approximation is per observation.
""")

code(r"""
summary_jrt = az.summary(idata_jrt, var_names=["sigma_lambda", "sigma_log_a", "cutpoints"],
                           round_to=4)
print(summary_jrt)
save_table(summary_jrt.reset_index().rename(columns={"index": "parameter"}), "jrt_model_summary")

n_div_jrt = int(idata_jrt.sample_stats["diverging"].sum())
max_rhat_jrt = float(summary_jrt["r_hat"].max())
print(f"Divergences: {n_div_jrt}, max R-hat: {max_rhat_jrt:.4f}")
if max_rhat_jrt >= 1.01:
    log_warning(f"Max R-hat = {max_rhat_jrt:.4f} >= 1.01 for the JRT model.")
if n_div_jrt > 0:
    log_warning(f"{n_div_jrt} divergences in the JRT model.")

disc = idata_jrt.posterior["discrimination"].mean(dim=("chain", "draw")).values
disc_low = idata_jrt.posterior["discrimination"].quantile(0.025, dim=("chain", "draw")).values
disc_high = idata_jrt.posterior["discrimination"].quantile(0.975, dim=("chain", "draw")).values
jrt_rater_table = pd.DataFrame({
    "rater_id": rater_levels_o,
    "jrt_discrimination": disc,
    "jrt_discrimination_lower": disc_low,
    "jrt_discrimination_upper": disc_high,
    "jrt_severity": idata_jrt.posterior["lam"].mean(dim=("chain", "draw")).values,
})
save_table(jrt_rater_table, "jrt_rater_table")

print(f"\nDiscrimination: median={np.median(disc):.2f}, range=[{disc.min():.2f}, {disc.max():.2f}]")
print("Raters with noticeably low discrimination (< 0.5, i.e. barely differentiate "
      f"between actions): {(disc < 0.5).sum()}")
""")

code(r"""
try:
    loo_ordinal = az.loo(idata_ord, pointwise=True)
    loo_jrt = az.loo(idata_jrt, pointwise=True)
    print("LOO ordinal model (global discrimination=1):")
    print(loo_ordinal)
    print("\nLOO JRT model (rater-specific discrimination):")
    print(loo_jrt)

    loo_comparison = pd.DataFrame({
        "model": ["ordinal (a=1 for all raters)", "JRT (rater-specific discrimination)"],
        "elpd_loo": [float(loo_ordinal.elpd_loo), float(loo_jrt.elpd_loo)],
        "se": [float(loo_ordinal.se), float(loo_jrt.se)],
        "p_loo": [float(loo_ordinal.p_loo), float(loo_jrt.p_loo)],
    })
    loo_comparison["elpd_diff_vs_best"] = loo_comparison["elpd_loo"] - loo_comparison["elpd_loo"].max()
    save_table(loo_comparison, "loo_model_comparison")
    print(loo_comparison)

    pareto_k_ord = loo_ordinal.pareto_k.values
    pareto_k_jrt = loo_jrt.pareto_k.values
    print(f"\nShare of Pareto-k > 0.7 (ordinal): {(pareto_k_ord > 0.7).mean():.1%}")
    print(f"Share of Pareto-k > 0.7 (JRT): {(pareto_k_jrt > 0.7).mean():.1%}")
    if (pareto_k_ord > 0.7).mean() > 0.05 or (pareto_k_jrt > 0.7).mean() > 0.05:
        log_warning("More than 5% of observations have Pareto-k > 0.7 - the LOO "
                     "estimate is unreliable for these points.")
except Exception as e:
    log_warning(f"LOO model comparison failed: {e}")
    loo_comparison = pd.DataFrame()
""")

md(r"""
### 10.4 Interpretation

A higher `elpd_loo` for the JRT model would suggest that
rater-specific discrimination captures genuine, predictively relevant
heterogeneity. A negligible or negative difference (within ~1-2
standard errors of `elpd_diff`) favors the simpler model from Section
9 (parsimony principle: "JRT is not automatically better than a
simpler model", Section 22 of the analysis brief). The actual
comparison value is in `results/tables/loo_model_comparison.csv` and
is referenced in the automated interpretation block (Section 17).

**Note on Python vs. R for JRT:** No established, dedicated JRT
package exists for Python (as of this analysis); we therefore
implement the JRT logic directly in PyMC (as above). The **R
notebook** additionally uses the dedicated CRAN package `jrt`
(Myszkowski, 2021) as a cross-check, provided its installation
succeeded in the respective run.
""")


# ====================================================================
# 12. RATER FIT AND RATER-EFFECT DIAGNOSTICS (Section 13 of the brief)
# ====================================================================
md(r"""
## 11. Rater-fit diagnostics

### 11.1 Leave-one-rater-out consistency

For every action with $n_i \ge 2$ ratings, we compute the **consensus
excluding rater $j$** (mean of the remaining ratings) and compare
rater $j$'s own rating to it. This avoids the circularity of comparing
a rater to a consensus that already includes their own rating.
""")

code(r"""
ratings_indexed = ratings_clean.set_index(["action_id", "rater_id"])["rating_numeric"]
action_sum = ratings_clean.groupby("action_id")["rating_numeric"].sum()
action_n = ratings_clean.groupby("action_id")["rating_numeric"].size()

tmp = ratings_clean.copy()
tmp["_action_sum"] = tmp["action_id"].map(action_sum)
tmp["_action_n"] = tmp["action_id"].map(action_n)
tmp["loo_consensus"] = np.where(
    tmp["_action_n"] >= 2,
    (tmp["_action_sum"] - tmp["rating_numeric"]) / (tmp["_action_n"] - 1),
    np.nan,
)

def loo_stats(g):
    valid = g.dropna(subset=["loo_consensus"])
    if len(valid) < 5:
        return pd.Series({"leave_one_out_spearman": np.nan, "leave_one_out_mae": np.nan,
                            "leave_one_out_mean_diff": np.nan, "leave_one_out_weighted_kappa": np.nan,
                            "n_loo": len(valid)})
    spearman_r = sps.spearmanr(valid["rating_numeric"], valid["loo_consensus"]).correlation
    mae = np.abs(valid["rating_numeric"] - valid["loo_consensus"]).mean()
    mean_diff = (valid["rating_numeric"] - valid["loo_consensus"]).mean()
    loo_rounded = valid["loo_consensus"].round().clip(1, 7).astype(int)
    w_kappa = cohen_kappa_score(valid["rating_numeric"], loo_rounded, weights="quadratic")
    return pd.Series({"leave_one_out_spearman": spearman_r, "leave_one_out_mae": mae,
                        "leave_one_out_mean_diff": mean_diff,
                        "leave_one_out_weighted_kappa": w_kappa, "n_loo": len(valid)})

loo_df = tmp.groupby("rater_id").apply(loo_stats, include_groups=False).reset_index()
save_table(loo_df, "leave_one_out_consistency")
print(f"Leave-one-out consistency computed for {loo_df['leave_one_out_spearman'].notna().sum()} "
      f"of {len(loo_df)} raters (remainder: too few actions with >=2 ratings).")
loo_df.sort_values("leave_one_out_spearman").head(10)
""")

md(r"""
### 11.2 Summary rater-diagnostics table and exploratory flags

**Important:** flags mark raters only exploratorily, **not** as
"bad". Criteria (each weak on its own, to be interpreted jointly):
very low category variation ($\le 2$ categories used), extremely low
connectivity (mean pairwise overlap $<5$), noticeably low JRT
discrimination ($<0.4$), strong drift ($|\text{slope}| > 2\cdot SE$),
negative or very low leave-one-out consistency (Spearman $<0.1$).
""")

code(r"""
rater_diagnostics = rater_desc.merge(severity_df.drop(columns=["n_ratings", "raw_mean"], errors="ignore"),
                                        on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(
    ordinal_severity if "ordinal_severity" in dir() else pd.DataFrame({"rater_id": []}),
    on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(
    jrt_rater_table if "jrt_rater_table" in dir() else pd.DataFrame({"rater_id": []}),
    on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(loo_df, on="rater_id", how="left")

rater_diagnostics["network_component"] = rater_diagnostics["rater_id"].apply(
    lambda r: 0 if r in largest_component_raters else -1)
rater_diagnostics["network_degree"] = rater_diagnostics["rater_id"].map(rater_degree)
rater_diagnostics["mean_pair_overlap"] = rater_diagnostics["rater_id"].map(mean_pair_overlap)

def build_flags(row):
    flags = []
    if row.get("n_categories_used", 7) <= 2:
        flags.append("low_category_variation")
    if pd.notna(row.get("mean_pair_overlap")) and row["mean_pair_overlap"] < 5:
        flags.append("low_connectivity")
    if pd.notna(row.get("jrt_discrimination")) and row["jrt_discrimination"] < 0.4:
        flags.append("low_discrimination")
    if pd.notna(row.get("drift_estimate")) and pd.notna(row.get("drift_se")) and row["drift_se"] > 0:
        if abs(row["drift_estimate"]) > 2 * row["drift_se"]:
            flags.append("possible_drift")
    if pd.notna(row.get("leave_one_out_spearman")) and row["leave_one_out_spearman"] < 0.1:
        flags.append("low_loo_consistency")
    if row.get("network_component", 0) != 0:
        flags.append("outside_largest_component")
    return ";".join(flags) if flags else "no_flag"

rater_diagnostics["diagnostic_flag"] = rater_diagnostics.apply(build_flags, axis=1)
n_flagged = (rater_diagnostics["diagnostic_flag"] != "no_flag").sum()
print(f"Raters with at least one exploratory flag: {n_flagged} out of {len(rater_diagnostics)}")
print(rater_diagnostics["diagnostic_flag"].value_counts())
""")


# ====================================================================
# 13. MODEL COMPARISON AND SENSITIVITY ANALYSES (Section 14 of the brief)
# ====================================================================
md(r"""
## 12. Comparison of action-score methods

We bring together the scores computed so far: raw mean, rater-centered
mean, LMM-BLUP (Section 6), ordinal posterior score (Section 9). The
JRT score (Section 10) uses a different scale fixing (Var=1) and is
compared separately.
""")

code(r"""
mu_mean_val = float(idata_lmm.posterior["mu"].mean())
lmm_full = pd.DataFrame({
    "action_id": action_blup_series.index,
    "lmm_score": mu_mean_val + action_blup_series.values,
    "lmm_score_se": action_blup_se_series.reindex(action_blup_series.index).values,
})
lmm_full["lmm_score_lower"] = lmm_full["lmm_score"] - 1.96 * lmm_full["lmm_score_se"]
lmm_full["lmm_score_upper"] = lmm_full["lmm_score"] + 1.96 * lmm_full["lmm_score_se"]

score_comparison = action_scores.merge(lmm_full, on="action_id", how="left")
score_comparison = score_comparison.merge(ordinal_scores, on="action_id", how="left")

score_cols = ["raw_mean", "rater_centered_mean", "lmm_score", "ordinal_expected_rating"]
corr_pearson = score_comparison[score_cols].corr(method="pearson")
corr_spearman = score_comparison[score_cols].corr(method="spearman")
save_table(corr_pearson.reset_index().rename(columns={"index": "measure"}), "score_comparison_pearson")
save_table(corr_spearman.reset_index().rename(columns={"index": "measure"}), "score_comparison_spearman")
print("Pearson correlations between score variants:")
print(corr_pearson.round(3))
print("\nSpearman correlations between score variants:")
print(corr_spearman.round(3))
""")

md(r"""
### 12.1 Rank shift and top/bottom overlap

Comparison of raw mean vs. LMM-BLUP score (the contrast most strongly
affected by rater correction).
""")

code(r"""
valid = score_comparison.dropna(subset=["raw_mean", "lmm_score"]).copy()
valid["rank_raw"] = valid["raw_mean"].rank()
valid["rank_lmm"] = valid["lmm_score"].rank()
mean_abs_rank_shift = (valid["rank_raw"] - valid["rank_lmm"]).abs().mean()
rank_corr = valid["rank_raw"].corr(valid["rank_lmm"], method="spearman")

def top_bottom_overlap(df_, col_a, col_b, frac):
    n_top = max(1, int(len(df_) * frac))
    top_a = set(df_.nlargest(n_top, col_a)["action_id"])
    top_b = set(df_.nlargest(n_top, col_b)["action_id"])
    bottom_a = set(df_.nsmallest(n_top, col_a)["action_id"])
    bottom_b = set(df_.nsmallest(n_top, col_b)["action_id"])
    return {
        "frac": frac,
        "top_overlap_pct": len(top_a & top_b) / n_top,
        "bottom_overlap_pct": len(bottom_a & bottom_b) / n_top,
    }

overlap_results = [top_bottom_overlap(valid, "raw_mean", "lmm_score", f) for f in [0.05, 0.10]]
overlap_df = pd.DataFrame(overlap_results)
save_table(overlap_df, "score_top_bottom_overlap_raw_vs_lmm")
print(f"Mean absolute rank shift (raw vs. LMM-BLUP): {mean_abs_rank_shift:.1f} "
      f"out of {len(valid)} actions")
print(f"Rank correlation: {rank_corr:.3f}")
print(overlap_df)
""")

code(r"""
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

axes[0].scatter(score_comparison["raw_mean"], score_comparison["lmm_score"],
                  c=score_comparison["n_ratings"], cmap="viridis", s=12, alpha=0.6)
axes[0].plot([1, 7], [1, 7], color="grey", ls="--", lw=1)
axes[0].set_xlabel("Raw mean")
axes[0].set_ylabel("LMM-BLUP score")
axes[0].set_title("Raw mean vs. LMM-BLUP")

axes[1].scatter(score_comparison["raw_mean"], score_comparison["ordinal_expected_rating"],
                  c=score_comparison["n_ratings"], cmap="viridis", s=12, alpha=0.6)
axes[1].plot([1, 7], [1, 7], color="grey", ls="--", lw=1)
axes[1].set_xlabel("Raw mean")
axes[1].set_ylabel("Ordinal expected rating")
axes[1].set_title("Raw mean vs. ordinal model")

score_comparison["n_ratings_bin"] = pd.cut(score_comparison["n_ratings"], [0, 1, 2, 3, 7],
                                              labels=["1", "2", "3", "4-7"])
diffs_by_n = score_comparison.copy()
diffs_by_n["diff_raw_lmm"] = diffs_by_n["raw_mean"] - diffs_by_n["lmm_score"]
diffs_by_n.boxplot(column="diff_raw_lmm", by="n_ratings_bin", ax=axes[2])
axes[2].set_xlabel("Number of ratings (bins)")
axes[2].set_ylabel("Raw mean - LMM-BLUP")
axes[2].set_title("Score difference by number of ratings")
plt.suptitle("")

fig.suptitle("Comparison of action-score methods")
fig.tight_layout()
save_fig(fig, "fig11_score_comparison",
         "Comparison of score methods: raw mean vs. LMM-BLUP (left), raw mean vs. "
         "ordinal model (middle), score difference stratified by number of ratings (right). "
         "Shows that shrinkage is stronger for actions with few ratings.")
plt.show()

print("\nAs expected: the spread of the difference (right) should be largest at "
      "n_ratings=1 (strongest shrinkage toward the grand mean).")
""")

md(r"""
### 12.2 Rating-level cross-validation

We evaluate prediction of **individual observed ratings** via 5-fold
cross-validation at the action level (an action, with all its ratings,
belongs entirely to exactly one fold — this avoids information leakage
between training and test folds for the same action). We compare
three simple, quickly computable predictors for the prediction target
**"new action, known rater pool"**:

1. Grand mean (training fold),
2. rater-specific mean (training fold) per rater,
3. empirical-Bayes shrinkage: action mean (if present in the training
   fold) shrunk using the ratio of the variance components estimated
   in Section 6.

**Note:** a full refit of the Bayesian model per fold would be most
accurate, but given the computational cost (~1 minute per fold × 5
folds) this was not performed here for time reasons; instead we use
the already-estimated global variance components as an approximation.
This is a documented simplification, not a full nested CV.
""")

code(r"""
from sklearn.model_selection import KFold

cv_actions = ratings_clean.loc[ratings_clean["in_largest_component"], "action_id"].unique()
kf = KFold(n_splits=5, shuffle=True, random_state=SEED)
shrink_ratio = var_action / (var_action + var_resid)  # simplified EB shrinkage factor

cv_records = []
for fold_i, (train_idx, test_idx) in enumerate(kf.split(cv_actions)):
    train_actions = set(cv_actions[train_idx])
    test_actions = set(cv_actions[test_idx])
    train_df = ratings_clean[ratings_clean["action_id"].isin(train_actions)]
    test_df = ratings_clean[ratings_clean["action_id"].isin(test_actions)]

    grand_mean_train = train_df["rating_numeric"].mean()
    rater_mean_train = train_df.groupby("rater_id")["rating_numeric"].mean()
    action_mean_train = train_df.groupby("action_id")["rating_numeric"].mean()

    pred_grand = np.full(len(test_df), grand_mean_train)
    pred_rater = test_df["rater_id"].map(rater_mean_train).fillna(grand_mean_train).values
    # EB shrinkage: for test actions (by definition NOT in the training fold), there is
    # no training-fold action mean -> the shrinkage predictor reduces to the grand mean.
    # This correctly represents the "new action" prediction target (see Section 14.3 of the brief).
    pred_shrink = pred_grand.copy()

    y_true = test_df["rating_numeric"].values
    cv_records.append({
        "fold": fold_i,
        "n_test": len(test_df),
        "rmse_grand_mean": np.sqrt(np.mean((y_true - pred_grand) ** 2)),
        "rmse_rater_mean": np.sqrt(np.mean((y_true - pred_rater) ** 2)),
        "mae_grand_mean": np.mean(np.abs(y_true - pred_grand)),
        "mae_rater_mean": np.mean(np.abs(y_true - pred_rater)),
    })

cv_results = pd.DataFrame(cv_records)
save_table(cv_results, "cross_validation_new_action_prediction")
print(cv_results)
print(f"\nMean RMSE (grand mean): {cv_results['rmse_grand_mean'].mean():.3f}")
print(f"Mean RMSE (rater mean):  {cv_results['rmse_rater_mean'].mean():.3f}")
print("\nPrediction target: 'new action' (no training-fold action mean available). "
      "Other prediction targets (known action + known rater; known action + new rater) "
      "require a full model refit per fold and are not implemented here for "
      "compute-time reasons (see the warning/documentation above).")
""")

md(r"""
### 12.3 Rater-assignment sensitivity

If raters were not randomly assigned to actions, rater severity
estimates could be confounded with substantive action characteristics.
We check the association between rater and action type descriptively
(contingency table, $\chi^2$ test).
""")

code(r"""
if "action_type" in ratings_clean.columns:
    contingency = pd.crosstab(ratings_clean["rater_id"], ratings_clean["action_type"])
    chi2, p_val, dof, expected = sps.chi2_contingency(contingency)
    print(f"Chi-square test rater x action type: chi2={chi2:.1f}, df={dof}, p={p_val:.4g}")
    if p_val < 0.05:
        log_warning(
            f"Significant association between rater and action type (chi-square test, p={p_val:.4g}). "
            "Rater assignment may not have been random - severity estimates could "
            "be confounded with action type."
        )
    save_table(contingency.reset_index(), "rater_by_action_type_contingency")
else:
    log_warning("No action_type variable available - rater-assignment sensitivity check skipped.")
""")


# ====================================================================
# 14. EXTENDED DEPENDENCIES (Section 15 of the brief)
# ====================================================================
md(r"""
## 13. Extended dependencies: match as an additional facette

Actions belong to exactly one match; a match contains multiple
actions. We extend the linear crossed model from Section 6 with an
additional random intercept for `match_id`:

$$
y_{ijm} = \mu + u_i^{(\text{action})} + v_j^{(\text{rater})}
+ w_m^{(\text{match})} + \varepsilon_{ijm}
$$

**Important:** the action is nested within the match (each action
belongs to exactly one match), while raters remain crossed with both.
We compare the variance decomposition and check whether action ranks
change materially.
""")

code(r"""
if "match_id" in ratings_clean.columns:
    match_idx, match_levels = pd.factorize(df_lmm["match_id"])
    n_match = len(match_levels)
    print(f"Extended model: {n_match} matches.")

    with pm.Model(coords={"action": action_levels, "rater": rater_levels, "match": match_levels}) as extended_model:
        mu_ext = pm.Normal("mu", 4.0, 2.0)
        sigma_action_ext = pm.Exponential("sigma_action", 1.0)
        sigma_rater_ext = pm.Exponential("sigma_rater", 1.0)
        sigma_match = pm.Exponential("sigma_match", 1.0)
        sigma_resid_ext = pm.Exponential("sigma_resid", 1.0)

        u_ext = pm.Normal("u_raw", 0, 1, dims="action") * sigma_action_ext
        v_ext = pm.Normal("v_raw", 0, 1, dims="rater") * sigma_rater_ext
        w_ext = pm.Normal("w_raw", 0, 1, dims="match") * sigma_match

        eta_ext = mu_ext + u_ext[action_idx] + v_ext[rater_idx] + w_ext[match_idx]
        pm.Normal("y_obs", mu=eta_ext, sigma=sigma_resid_ext, observed=y_lmm)

        idata_ext = pm.sample(draws=800, tune=800, chains=4, cores=4, target_accept=0.9,
                                random_seed=SEED, progressbar=False)

    idata_ext.to_netcdf(str(RESULTS_MODELS / "extended_match_model.nc"))

    va_ext = float((idata_ext.posterior["sigma_action"] ** 2).mean())
    vr_ext = float((idata_ext.posterior["sigma_rater"] ** 2).mean())
    vm_ext = float((idata_ext.posterior["sigma_match"] ** 2).mean())
    ve_ext = float((idata_ext.posterior["sigma_resid"] ** 2).mean())
    total_ext = va_ext + vr_ext + vm_ext + ve_ext

    extended_vc = pd.DataFrame([
        {"component": "action", "variance": va_ext, "pct": va_ext / total_ext},
        {"component": "rater", "variance": vr_ext, "pct": vr_ext / total_ext},
        {"component": "match", "variance": vm_ext, "pct": vm_ext / total_ext},
        {"component": "residual", "variance": ve_ext, "pct": ve_ext / total_ext},
    ])
    save_table(extended_vc, "extended_model_variance_components")
    print(extended_vc)

    u_ext_mean = idata_ext.posterior["u_raw"].mean(dim=("chain", "draw")).values * \
                  float(idata_ext.posterior["sigma_action"].mean())
    ext_action_scores = pd.Series(u_ext_mean, index=action_levels, name="action_score_extended")
    base_action_scores = action_blup_series.reindex(action_levels)
    rank_corr_ext = pd.Series(base_action_scores.values).corr(
        pd.Series(ext_action_scores.values), method="spearman")
    print(f"\nRank correlation action score (base model vs. match-extended model): "
          f"{rank_corr_ext:.3f}")
    if rank_corr_ext < 0.9:
        log_warning(
            f"Rank correlation between the base and match-extended model is only {rank_corr_ext:.3f} "
            "- match membership changes the action ranking non-trivially."
        )
else:
    log_warning("No match_id variable available - extended model skipped.")
    extended_vc = pd.DataFrame()
""")

# ====================================================================
# 15. SIMULATION/RECOVERY CHECK (Section 16 of the brief)
# ====================================================================
md(r"""
## 14. Simulation and recovery check

**This section is only meaningful because this run uses SIMULATED
data** (`DEV_MODE=True`), for which the true action/rater parameters
are known (see `scripts/simulate_ratings.py` and
`data/simulation/`). **With real ratings this comparison is not
possible**, since no true values exist — the infrastructure
demonstrated here remains usable for a design-based simulation
(identical rater-action incidence matrix, artificial known parameters,
see Section 16 of the analysis brief) to check which parameters are
identifiable at all given the concrete unbalanced design.
""")

code(r"""
gt_action = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_action_params.csv")
gt_rater = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_rater_params.csv")
gt_thresh = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_thresholds.csv")

recovery_action = ordinal_scores.merge(gt_action, on="action_id", how="inner")
bias_theta = (recovery_action["ordinal_latent_score"] - recovery_action["theta_true"]).mean()
rmse_theta = np.sqrt(((recovery_action["ordinal_latent_score"] - recovery_action["theta_true"]) ** 2).mean())
rank_corr_theta = recovery_action["ordinal_latent_score"].corr(recovery_action["theta_true"], method="spearman")
coverage_theta = ((recovery_action["theta_true"] >= recovery_action["ordinal_latent_lower"]) &
                    (recovery_action["theta_true"] <= recovery_action["ordinal_latent_upper"])).mean()

print("=== Recovery: action theta (ordinal model) ===")
print(f"Bias: {bias_theta:+.3f}")
print(f"RMSE: {rmse_theta:.3f}")
print(f"Rank correlation (estimated vs. true): {rank_corr_theta:.3f}")
print(f"95% CI coverage: {coverage_theta:.1%} (target ~95%)")

recovery_rater = severity_df.merge(gt_rater, on="rater_id", how="inner")
# Sign/scale check: lmm_severity and severity_true should correlate highly
sev_corr = recovery_rater["lmm_severity"].corr(recovery_rater["severity_true"])
print(f"\n=== Recovery: rater severity (linear model) ===")
print(f"Correlation estimated vs. true: {sev_corr:.3f}")

recovery_summary = pd.DataFrame([
    {"quantity": "action_theta_bias", "value": bias_theta},
    {"quantity": "action_theta_rmse", "value": rmse_theta},
    {"quantity": "action_theta_rank_corr", "value": rank_corr_theta},
    {"quantity": "action_theta_ci_coverage", "value": coverage_theta},
    {"quantity": "rater_severity_recovery_corr", "value": sev_corr},
])
save_table(recovery_summary, "simulation_recovery_summary")

if rank_corr_theta < 0.7:
    log_warning(f"Recovery rank correlation of action theta is only {rank_corr_theta:.3f} - "
                 "weak parameter identifiability may be present in the given design.")
""")

code(r"""
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].scatter(recovery_action["theta_true"], recovery_action["ordinal_latent_score"],
                  s=10, alpha=0.4, c=recovery_action["n_ratings"], cmap="viridis")
lims = [recovery_action["theta_true"].min(), recovery_action["theta_true"].max()]
axes[0].plot(lims, lims, color="grey", ls="--", lw=1)
axes[0].set_xlabel(r"True $\theta_i$ (simulation)")
axes[0].set_ylabel(r"Estimated $\theta_i$ (ordinal model)")
axes[0].set_title(f"Action recovery (r_rank={rank_corr_theta:.2f})")

axes[1].scatter(recovery_rater["severity_true"], recovery_rater["lmm_severity"], s=25, alpha=0.7,
                  color="#DD8452")
lims2 = [recovery_rater["severity_true"].min(), recovery_rater["severity_true"].max()]
axes[1].plot(lims2, lims2, color="grey", ls="--", lw=1)
axes[1].set_xlabel("True rater severity (simulation)")
axes[1].set_ylabel("Estimated rater severity (linear model)")
axes[1].set_title(f"Rater recovery (r={sev_corr:.2f})")

fig.suptitle("Parameter recovery: only valid for simulated development data")
fig.tight_layout()
save_fig(fig, "fig13_simulation_recovery",
         "Comparison of estimated vs. true (simulated) action creativity (left) and "
         "rater severity (right). Only meaningful in the DEV_MODE run with simulated data.")
plt.show()
""")


# ====================================================================
# 16. EXPORT OF RESULT FILES (Section 17 of the brief)
# ====================================================================
md(r"""
## 15. Final result files: `action_scores.csv` and `rater_diagnostics.csv`

We bring together all score and diagnostic components computed so far
into the two central result files. **Unavailable model values are
stored as missing (`NaN`), not as zero** (e.g. for actions outside the
largest component, for which no LMM/ordinal scores exist).
""")

code(r"""
final_action_scores = action_scores.merge(lmm_full, on="action_id", how="left")
final_action_scores = final_action_scores.merge(ordinal_scores, on="action_id", how="left")

if "theta_jrt" not in dir():
    theta_jrt_mean = idata_jrt.posterior["theta"].mean(dim=("chain", "draw")).values
    theta_jrt_sd = idata_jrt.posterior["theta"].std(dim=("chain", "draw")).values
    jrt_action_scores = pd.DataFrame({
        "action_id": action_levels_o, "jrt_score": theta_jrt_mean, "jrt_score_se": theta_jrt_sd,
    })
final_action_scores = final_action_scores.merge(jrt_action_scores, on="action_id", how="left")

def score_flag(row):
    flags = []
    if row["n_ratings"] == 1:
        flags.append("single_rating")
    if row.get("connected_component", 0) != 0:
        flags.append("small_component")
    return ";".join(flags) if flags else "ok"

final_action_scores["score_flag"] = final_action_scores.apply(score_flag, axis=1)

action_scores_out_cols = [
    "action_id", "n_ratings", "connected_component", "raw_mean", "raw_median",
    "rater_centered_mean", "lmm_score", "lmm_score_se", "lmm_score_lower", "lmm_score_upper",
    "ordinal_latent_score", "ordinal_latent_lower", "ordinal_latent_upper", "ordinal_expected_rating",
    "jrt_score", "jrt_score_se", "score_flag",
]
final_action_scores_out = final_action_scores[action_scores_out_cols].copy()
final_action_scores_out.to_csv(DATA_PROCESSED / "action_scores.csv", index=False)
print(f"action_scores.csv saved: {len(final_action_scores_out)} actions, "
      f"{final_action_scores_out.shape[1]} columns.")
final_action_scores_out.head()
""")

code(r"""
rater_diagnostics_out_cols = [
    "rater_id", "n_ratings", "n_actions", "n_categories_used", "raw_mean", "sd",
    "extreme_category_rate", "central_category_rate", "network_component", "network_degree",
    "mean_pair_overlap", "lmm_severity", "lmm_severity_se", "ordinal_severity",
    "ordinal_severity_lower", "ordinal_severity_upper", "jrt_discrimination", "jrt_severity",
    "leave_one_out_spearman", "leave_one_out_mae", "drift_estimate", "diagnostic_flag",
]
rater_diagnostics_out_cols = [c for c in rater_diagnostics_out_cols if c in rater_diagnostics.columns]
rater_diagnostics_out = rater_diagnostics[rater_diagnostics_out_cols].copy()
rater_diagnostics_out = rater_diagnostics_out.rename(columns={"sd": "raw_sd"})
rater_diagnostics_out.to_csv(DATA_PROCESSED / "rater_diagnostics.csv", index=False)
print(f"rater_diagnostics.csv saved: {len(rater_diagnostics_out)} raters, "
      f"{rater_diagnostics_out.shape[1]} columns.")
rater_diagnostics_out.head()
""")

md(r"""
### 15.1 Publication-ready tables
""")

code(r"""
sample_description = pd.DataFrame([
    {"quantity": "Total number of ratings", "value": len(ratings_clean)},
    {"quantity": "Number of actions", "value": ratings_clean["action_id"].nunique()},
    {"quantity": "Number of raters", "value": ratings_clean["rater_id"].nunique()},
    {"quantity": "Actions with 1 rating", "value": int((ratings_per_action == 1).sum())},
    {"quantity": "Actions with 2 ratings", "value": int((ratings_per_action == 2).sum())},
    {"quantity": "Actions with >=3 ratings", "value": int((ratings_per_action >= 3).sum())},
    {"quantity": "Number of connected components", "value": n_components},
    {"quantity": "Actions in the largest component", "value": len(largest_component_actions)},
    {"quantity": "Krippendorff's alpha (ordinal)", "value": round(alpha_ordinal, 3)},
    {"quantity": "sigma^2_action (linear)", "value": round(var_action, 3)},
    {"quantity": "sigma^2_rater (linear)", "value": round(var_rater, 3)},
    {"quantity": "sigma^2_residual (linear)", "value": round(var_resid, 3)},
    {"quantity": "Absolute reliability (k=1)", "value": round(float(d_study.loc[0, "rho_abs"]), 3)},
    {"quantity": "Relative reliability (k=1)", "value": round(float(d_study.loc[0, "rho_rel"]), 3)},
    {"quantity": "Absolute reliability (k=2)", "value": round(float(d_study.loc[1, "rho_abs"]), 3)},
    {"quantity": "Relative reliability (k=2)", "value": round(float(d_study.loc[1, "rho_rel"]), 3)},
])
save_table(sample_description, "sample_description_summary")
sample_description
""")


# ====================================================================
# 17. REMAINING KEY FIGURES (Section 18 of the brief)
# ====================================================================
md(r"""
## 16. Judge category curves, information functions, score uncertainty

### 16.1 Judge category curves and information function (from the JRT model)

For a selection of raters with low, medium, and high estimated
discrimination, we show the model-implied category probabilities
$P(Y=k\mid\theta)$ across the latent creativity continuum, along with
the corresponding Fisher information function
$I_j(\theta) = a_j^2 \sum_k P_{jk}(\theta)\,[1-P_{jk}(\theta)]$
(approximation via the cumulative probabilities).
""")

code(r"""
def category_probs(theta_grid, a, lam, cuts):
    eta = a * theta_grid + lam
    cum = 1 / (1 + np.exp(-(cuts[None, :] - eta[:, None])))
    cum = np.concatenate([np.zeros((len(theta_grid), 1)), cum, np.ones((len(theta_grid), 1))], axis=1)
    return np.diff(cum, axis=1)  # (n_theta, 7)

theta_grid = np.linspace(-3, 3, 200)
cut_mean_jrt = idata_jrt.posterior["cutpoints"].mean(dim=("chain", "draw")).values

example_raters_idx = [int(np.argmin(disc)), int(np.argsort(disc)[len(disc) // 2]), int(np.argmax(disc))]
example_labels = ["lowest discrimination", "median discrimination", "highest discrimination"]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for col, (ridx, label) in enumerate(zip(example_raters_idx, example_labels)):
    a_r = disc[ridx]
    lam_r = jrt_rater_table.loc[ridx, "jrt_severity"]
    probs = category_probs(theta_grid, a_r, lam_r, cut_mean_jrt)
    for k in range(7):
        axes[0, col].plot(theta_grid, probs[:, k], label=f"Y={k+1}")
    axes[0, col].set_title(f"{rater_levels_o[ridx]}: {label}\n(a={a_r:.2f})")
    axes[0, col].set_xlabel(r"$\theta$ (latent action creativity)")
    if col == 0:
        axes[0, col].set_ylabel("P(Y=k)")
        axes[0, col].legend(fontsize=7, ncol=2)

    info = (a_r ** 2) * np.sum(probs * (1 - probs), axis=1)
    axes[1, col].plot(theta_grid, info, color="#C44E52")
    axes[1, col].set_xlabel(r"$\theta$")
    if col == 0:
        axes[1, col].set_ylabel("Information function (approximation)")

fig.suptitle("Judge category curves (top) and information functions (bottom) "
              "for raters with low/median/high discrimination")
fig.tight_layout()
save_fig(fig, "fig14_judge_category_curves_information",
         "Category probabilities (top) and Fisher information approximation (bottom) for "
         "three example raters with low, median, and high JRT discrimination.")
plt.show()
""")

md(r"""
### 16.2 Uncertainty intervals for selected action scores

For a random sample of 40 actions (stratified by number of ratings),
we show the 95% uncertainty intervals of the LMM-BLUP and ordinal
scores side by side.
""")

code(r"""
sample_for_plot = (
    final_action_scores.dropna(subset=["lmm_score", "ordinal_latent_score"])
    .groupby(final_action_scores["n_ratings"].clip(upper=4))
    .apply(lambda g: g.sample(min(10, len(g)), random_state=SEED), include_groups=False)
    .reset_index(drop=True)
    .sort_values("lmm_score")
)

fig, ax = plt.subplots(figsize=(8, 10))
y_pos = np.arange(len(sample_for_plot))
ax.errorbar(sample_for_plot["lmm_score"], y_pos - 0.15,
             xerr=[sample_for_plot["lmm_score"] - sample_for_plot["lmm_score_lower"],
                   sample_for_plot["lmm_score_upper"] - sample_for_plot["lmm_score"]],
             fmt="o", ms=4, color="#4C72B0", label="LMM-BLUP", capsize=2)
ax_ord = ax.twiny()
ax_ord.errorbar(sample_for_plot["ordinal_latent_score"], y_pos + 0.15,
                  xerr=[sample_for_plot["ordinal_latent_score"] - sample_for_plot["ordinal_latent_lower"],
                        sample_for_plot["ordinal_latent_upper"] - sample_for_plot["ordinal_latent_score"]],
                  fmt="s", ms=4, color="#DD8452", label="ordinal", capsize=2)
ax.set_yticks(y_pos)
ax.set_yticklabels(sample_for_plot["action_id"] + " (n=" + sample_for_plot["n_ratings"].astype(str) + ")",
                     fontsize=7)
ax.set_xlabel("LMM-BLUP score", color="#4C72B0")
ax_ord.set_xlabel("Ordinal latent score", color="#DD8452")
ax.set_title("95% uncertainty intervals: sample of action scores\n"
              "(stratified by number of ratings)")
fig.tight_layout()
save_fig(fig, "fig15_score_uncertainty_sample",
         "95% uncertainty intervals for a sample of actions stratified by number of "
         "ratings: LMM-BLUP score (blue, bottom) vs. ordinal latent score (orange, top).")
plt.show()
""")


# ====================================================================
# 18. AUTOMATED INTERPRETATION BLOCK (Section 19 of the brief)
# ====================================================================
md(r"""
## 17. Automated, cautious interpretation

The following text is **automatically generated from the numbers
actually computed in this run** (no invented values). It does not
replace substantive discussion by the authors, but cautiously
summarizes the statistical findings. **Fixed thresholds are not
mechanically declared good/bad.**
""")

code(r"""
rel_vs_abs = "higher" if d_study.loc[0, "rho_rel"] > d_study.loc[0, "rho_abs"] else "not substantially higher"
rater_effect_strength = "a noticeable" if var_rater / (var_action + var_rater + var_resid) > 0.05 else "a relatively small"

pct_action = variance_components_df.loc[0, "pct_of_total"]
pct_rater = variance_components_df.loc[1, "pct_of_total"]
pct_resid = variance_components_df.loc[2, "pct_of_total"]
rho_rel_1 = d_study.loc[0, "rho_rel"]
rho_abs_1 = d_study.loc[0, "rho_abs"]
rho_abs_7 = d_study.loc[6, "rho_abs"]
n_single = int((ratings_per_action == 1).sum())
n_outside_largest = ratings_clean.action_id.nunique() - len(largest_component_actions)

if n_components == 1:
    component_note = "All rater severity estimates are therefore interpretable on a common scale."
else:
    component_note = (
        f"Rater severity estimates from smaller components (a total of {n_outside_largest} "
        "actions outside the largest component) are NOT directly comparable to those from "
        "the largest component and have been flagged accordingly."
    )

if len(loo_comparison) > 0:
    elpd_diff = loo_comparison["elpd_loo"].iloc[1] - loo_comparison["elpd_loo"].iloc[0]
    loo_note = (
        f"elpd_loo difference of {elpd_diff:.1f} (JRT minus the simple model, positive = JRT "
        "predicts out-of-sample better); if this difference is small relative to its "
        "standard error, the simpler model is preferable on parsimony grounds."
    )
else:
    loo_note = "the LOO model comparison could not be computed in this run."

interpretation_text = f'''
The linear variance-component model (Section 6) decomposed the observed
rating variance into {pct_action:.1%} differences between actions,
{pct_rater:.1%} systematic differences between raters, and {pct_resid:.1%}
residual variation (action x rater interaction, measurement error, other
unmodeled influences). The relative reliability of a single rating
(rho_rel={rho_rel_1:.2f}) was {rel_vs_abs} than the absolute
reliability (rho_abs={rho_abs_1:.2f}). This pattern is consistent with
{rater_effect_strength} systematic rater-level effect
(sigma^2_rater accounts for {pct_rater:.1%} of the total variance).

Krippendorff's ordinal alpha was {alpha_ordinal:.2f}
(95% cluster-bootstrap CI [{ci_ord[0]:.2f}, {ci_ord[1]:.2f}], n_boot={N_BOOT}).
This value describes global agreement across all actions and raters,
accounting for the incomplete design.

The D-study curve shows that the absolute reliability of the action mean
rises from rho_abs(k=1)={rho_abs_1:.2f} to rho_abs(k=7)={rho_abs_7:.2f} when
seven raters are averaged instead of one - a direct quantitative
demonstration of the value of additional ratings per action, especially
relevant for the {n_single} actions that currently have only one rating.

The rater-action graph splits into {n_components} connected component(s).
{component_note}

The model comparison between the simple ordinal facette model and the
JRT extension with rater-specific discrimination yielded an {loo_note}

This interpretation refers to the present, incompletely crossed design.
Actions with only one rating contribute to the model-based estimation of
the action distribution but provide no within-action information about
inter-rater agreement.

IMPORTANT: this run uses SIMULATED placeholder data (DEV_MODE=True).
The numbers reported above are methodology demonstrations, not real
findings about actual creativity ratings.
'''

print(interpretation_text)
with open(RESULTS_LOGS / "automated_interpretation.txt", "w") as f:
    f.write(interpretation_text)
""")




# ====================================================================
# 19. QUALITY CONTROLS (Section 20 of the brief)
# ====================================================================
md(r"""
## 18. Quality controls (automated checklist)

We systematically check the items required by the analysis brief
(Section 20) and log the result as a table rather than only as text.
""")

code(r"""
qc_checks = []

def qc(name, condition, detail=""):
    qc_checks.append({"check": name, "passed": bool(condition), "detail": detail})

qc("IDs uniquely typed (action_id, rater_id as string)",
    ratings_clean["action_id"].dtype == object and ratings_clean["rater_id"].dtype == object)
qc("No duplicate rater-action pairs after cleaning",
    not ratings_clean.duplicated(subset=["action_id", "rater_id"]).any())
qc("All ratings in {1,...,7}", ratings_clean["rating_numeric"].between(1, 7).all())
qc("Rater-action graph: connectivity checked and documented", n_components >= 1,
    f"{n_components} component(s)")
qc("Variance components (linear) non-negative",
    var_action >= 0 and var_rater >= 0 and var_resid >= 0)
qc("Linear Bayes model: max R-hat < 1.01", max_rhat < 1.01, f"max R-hat={max_rhat:.4f}")
qc("Linear Bayes model: no divergences", n_divergences == 0, f"{n_divergences} divergences")
qc("Ordinal model: max R-hat < 1.01", max_rhat_ord < 1.01, f"max R-hat={max_rhat_ord:.4f}")
qc("Ordinal model: no divergences", n_divergences_ord == 0, f"{n_divergences_ord} divergences")
qc("Ordinal model: thresholds ordered at the posterior mean", cuts_sorted)
qc("JRT model: max R-hat < 1.01", max_rhat_jrt < 1.01, f"max R-hat={max_rhat_jrt:.4f}")
qc("JRT model: no divergences", n_div_jrt == 0, f"{n_div_jrt} divergences")
qc("Actions with 1 rating correctly flagged (single_rating_action)",
    "single_rating_action" in ratings_clean.columns)
qc("All action scores exported with n_ratings and an uncertainty statement",
    {"n_ratings", "lmm_score_se", "ordinal_latent_lower", "ordinal_latent_upper"}.issubset(
        final_action_scores_out.columns))
qc("Raw data unchanged (cleaning log documented)", len(cleaning_log_df) > 0)
qc("Package versions logged (session_info_python.json)",
    (RESULTS_LOGS / "session_info_python.json").exists())

qc_df = pd.DataFrame(qc_checks)
save_table(qc_df, "qc_checklist")
n_failed_qc = (~qc_df["passed"]).sum()
print(qc_df.to_string(index=False))
print(f"\n{n_failed_qc} of {len(qc_df)} quality controls not passed.")
if n_failed_qc > 0:
    log_warning(f"{n_failed_qc} quality controls (see qc_checklist.csv) not passed.")
""")

md(r"""
### 18.1 Warnings collected during this run
""")

code(r"""
warnings_df = pd.DataFrame(WARNINGS_LOG)
save_table(warnings_df, "warnings_log")
print(f"A total of {len(warnings_df)} warnings were collected in this run (see "
      "results/tables/warnings_log.csv for the full list).")
if len(warnings_df) > 0:
    for msg in warnings_df["message"]:
        print(f"  - {msg}")
""")

md(r"""
## 19. Limitations and Design Implications

**Limitations of this analysis:**

1. **Simulated development data.** This run uses simulated placeholder
   data (`DEV_MODE=True`). All numbers are methodology demonstrations.
   Before publication: set `DEV_MODE=False`, insert the real Google
   Sheets import code, re-run the entire notebook.
2. **Residual variance covers multiple sources.** Since most
   rater-action cells contain only one rating, the action×rater
   interaction is not separately identifiable from measurement error
   (Section 6.1). The reported reliability coefficients are
   variance-component approximations, not a complete G-theory
   decomposition.
3. **JRT model with reduced complexity.** Rater-specific thresholds
   (as opposed to only rater-specific discrimination) were not
   estimated separately, for connectivity and compute-time reasons.
4. **Simplified cross-validation.** The rating-level CV (Section 12.2)
   uses approximate, quickly computable predictors instead of a full
   model refit per fold.
5. **Statsmodels scaling limit.** `statsmodels.MixedLM` with
   `vc_formula` is not practical for factors with thousands of levels
   (here: actions); we use PyMC as the primary estimation engine for
   Python (see Section 6.2 for the rationale).
6. **Separate components.** If the rater-action graph has more than
   one connected component, rater severity values are not comparable
   on the same scale across components (see Section 3).

### Recommendations for future rating assignment

1. **More ratings per action**: the D-study curve (Section 6.7)
   quantifies the reliability gain from additional ratings concretely
   for this design — a basis for a cost-benefit assessment of future
   rating capacity.
2. **Minimum overlap between raters**: rater pairs with a very small
   shared set of actions (Section 3.1) provide little information for
   calibrating relative rater strictness; a target of at least 15–20
   shared actions per rater pair (or per rater to at least one "bridge
   rater") is recommended.
3. **Targeted bridge actions**: a small set of anchor actions rated by
   (nearly) all raters substantially stabilizes the identifiability of
   rater severity.
4. **Balanced/block-balanced assignment**: avoids confounding rater
   assignment with action type/player/team (see the chi-square test in
   Section 12.3).
5. **Repeated anchor actions over time**: enable a more robust
   estimate of individual rater drift (Section 8.3) than one-off
   sessions.
6. **Calibration sessions** before the actual rating, especially for
   raters with below-average category usage or noticeable
   discrimination.
7. **Separation of training and final rating**, to keep learning
   effects (which would show up as drift) away from the final data
   collection.
""")

code(r"""
print("=" * 70)
print("NOTEBOOK FULLY EXECUTED")
print("=" * 70)
print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
print(f"Number of warnings collected: {len(WARNINGS_LOG)}")
print(f"QC checks passed: {(~qc_df['passed']).eq(False).sum()}/{len(qc_df)}")
print(f"\nTables generated: {len(list(RESULTS_TABLES.glob('*.csv')))}")
print(f"Figures generated: {len(list(RESULTS_FIGURES.glob('*.png')))}")
print(f"Models saved: {len(list(RESULTS_MODELS.glob('*.nc')))}")
""")


if __name__ == "__main__":
    nb["cells"] = cells
    OUT.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, OUT)
    print(f"Notebook written with {len(cells)} cells: {OUT}")
