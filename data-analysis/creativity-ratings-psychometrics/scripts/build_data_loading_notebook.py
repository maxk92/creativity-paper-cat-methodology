"""Builds notebooks/00_data_loading_preprocessing.ipynb from cell contents.

This script is run once to generate the notebook. Afterwards the notebook
itself is executed with `jupyter nbconvert --execute`. Changes to the
notebook content are made here in this script (not directly in the .ipynb
JSON file).
"""
import nbformat as nbf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "00_data_loading_preprocessing.ipynb"

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
# Data Loading and Preprocessing

This notebook is the single entry point for the creativity-ratings data.
It downloads the current rating export from Google Sheets, optionally
attaches the matching StatsBomb event details from the local event
database, and then applies every step that turns the raw export into an
analysis-ready dataset: schema checks, type conversion, out-of-range and
duplicate handling, and exclusion of ratings where the action could not
be recognized.

Both `01_creativity_ratings_python.ipynb` and `01_creativity_ratings_R.qmd`
read the result of this notebook (`data/processed/ratings_long_clean.csv`)
directly and do not repeat any of these steps themselves. Running this
notebook is therefore a prerequisite for both of the language-specific
analysis notebooks. `01_data_overview.ipynb` also reads the same file for
a quick, non-technical look at the data before the full analysis is run.

Two files are produced:

- `data/raw/ratings_long_raw.csv` — the sheet export, saved immediately
  and never modified afterwards.
- `data/processed/ratings_long_clean.csv` — the cleaned, analysis-ready
  dataset.

Every row removed or changed along the way is recorded in
`results/tables/cleaning_log.csv`, together with the affected rows saved
separately under `results/tables/flagged_*.csv`.
""")

# ====================================================================
# 1. SETUP
# ====================================================================
md(r"""
## 1. Setup
""")

code(r"""
import warnings
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# Project paths (relative to the notebook folder "notebooks/")
# ------------------------------------------------------------------
PROJECT_ROOT = Path("..").resolve()
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
RESULTS_TABLES = PROJECT_ROOT / "results" / "tables"

for d in [DATA_RAW, DATA_PROCESSED, RESULTS_TABLES]:
    d.mkdir(parents=True, exist_ok=True)

# The shared StatsBomb event database lives one level above this project,
# alongside the other numbered project folders (00-data, 01-rating-study, ...).
EVENT_DB_PATH = PROJECT_ROOT.parents[2] / "00-data" / "statsbomb_event_data.duckdb"

def save_table(df_table, name, index=False):
    # Saves a table as CSV under results/tables/.
    path = RESULTS_TABLES / f"{name}.csv"
    df_table.to_csv(path, index=index)
    print(f"Table saved: {path.relative_to(PROJECT_ROOT)} "
          f"({df_table.shape[0]} rows x {df_table.shape[1]} columns)")
    return path

WARNINGS_LOG = []
def log_warning(msg):
    WARNINGS_LOG.append({"timestamp": datetime.now(timezone.utc).isoformat(),
                          "message": msg})
    warnings.warn(msg)

cleaning_log = []
def log_clean_step(step, n_before, n_after, description):
    cleaning_log.append({
        "step": step, "n_rows_before": n_before, "n_rows_after": n_after,
        "n_rows_affected": n_before - n_after, "description": description,
    })

print(f"Project root: {PROJECT_ROOT}")
""")

# ====================================================================
# 2. GOOGLE SHEETS IMPORT
# ====================================================================
md(r"""
## 2. Load ratings from Google Sheets

The rating export is a shared Google Sheet, downloaded here via its
public XLSX export URL (the sheet is shared as "anyone with the link");
no authentication is required.
""")

code(r"""
sheet_url = "https://docs.google.com/spreadsheets/d/1KUcLAxm5g-zz9myrTcQOLH5L09JmFCRaIJ0woCzY1TA/edit?usp=sharing"
sheet_id = sheet_url.split("/d/")[1].split("/")[0]
url_template = "https://docs.google.com/spreadsheets/d/{}/export?format=xlsx"

ratings_raw = pd.read_excel(url_template.format(sheet_id), sheet_name=0)
print(f"Downloaded {len(ratings_raw)} rows.")
print(f"Columns: {list(ratings_raw.columns)}")
ratings_raw.head()
""")

code(r"""
# Save the raw data immediately after downloading it, and do NOT modify
# this file afterwards.
RAW_PATH = DATA_RAW / "ratings_long_raw.csv"
ratings_raw.to_csv(RAW_PATH, index=False)
print(f"Raw data saved: {RAW_PATH} ({len(ratings_raw)} rows)")
""")

# ====================================================================
# 3. OPTIONAL: MATCHING STATSBOMB EVENT DATA
# ====================================================================
md(r"""
## 3. Event details from the StatsBomb event database (optional)

Each rated action corresponds to a StatsBomb event. If the local event
database is reachable, we look up the matching events here and save them
as a separate table, keyed by action id, alongside the ratings. This is
supplementary context (action type, players, teams, ...); it is not
required by — and not merged into — the ratings used for the
psychometric analysis.
""")

code(r"""
try:
    import duckdb

    if not EVENT_DB_PATH.exists():
        raise FileNotFoundError(EVENT_DB_PATH)

    action_ids = ratings_raw["id"].unique().tolist()
    id_list = "', '".join(str(a) for a in action_ids)

    conn = duckdb.connect(str(EVENT_DB_PATH))
    action_events_raw = conn.execute(
        f"SELECT * FROM events WHERE id IN ('{id_list}')"
    ).fetchdf()
    conn.close()

    EVENTS_PATH = DATA_RAW / "action_events_raw.csv"
    action_events_raw.to_csv(EVENTS_PATH, index=False)
    print(f"Event details saved: {EVENTS_PATH} ({len(action_events_raw)} actions)")
except Exception as exc:
    log_warning(
        f"Could not load event details from {EVENT_DB_PATH} ({exc}). "
        "Continuing without event data - it is optional and not used "
        "by the psychometric analysis."
    )
""")

# ====================================================================
# 4. MAP TO THE CANONICAL SCHEMA
# ====================================================================
md(r"""
## 4. Map columns to the analysis schema

The exported sheet uses its own column names. We map them onto the
schema the analysis notebooks expect (`action_id`, `rater_id`, `rating`),
keep the two additional rating dimensions the sheet also collects
(`technical_correctness`, `aesthetic_appeal`) as unused extra columns for
possible future analyses, and drop purely technical export metadata
(device/OS/browser) that has no analytical use here — it remains
available in the raw file if ever needed.
""")

code(r"""
df = ratings_raw.rename(columns={
    "id": "action_id",
    "user_id": "rater_id",
    "creativity_rating": "rating",
}).copy()

df["action_id"] = df["action_id"].astype(str)
df["rater_id"] = df["rater_id"].astype(str)

for extra_col in ["technical_correctness", "aesthetic_appeal"]:
    if extra_col in df.columns:
        df[extra_col] = pd.to_numeric(df[extra_col], errors="coerce")

metadata_cols = ["device_type", "os", "os_version", "browser", "browser_version", "user_agent"]
df = df.drop(columns=[c for c in metadata_cols if c in df.columns])

print(f"Columns after mapping: {list(df.columns)}")
""")

# ====================================================================
# 5. EXCLUDE UNRECOGNIZED ACTIONS
# ====================================================================
md(r"""
## 5. Exclude ratings where the action was not recognized

Raters could flag an action as not recognizable (`action_not_recognized`).
Those rows carry no real creativity judgment, so they are excluded from
the analyzed dataset here rather than passed downstream. As with every
other exclusion in this notebook, the affected rows are saved separately
and the exclusion is recorded in the cleaning log.
""")

code(r"""
n0 = len(df)

if "action_not_recognized" in df.columns:
    not_recognized_mask = df["action_not_recognized"].fillna(False).astype(bool)
    tbl_not_recognized = df.loc[not_recognized_mask]
    print(f"Rows flagged as action_not_recognized: {len(tbl_not_recognized)}")
    if len(tbl_not_recognized) > 0:
        save_table(tbl_not_recognized, "flagged_action_not_recognized")
        log_warning(f"{len(tbl_not_recognized)} rows excluded: action_not_recognized was set.")

    n_before = len(df)
    df = df.loc[~not_recognized_mask].drop(columns=["action_not_recognized"]).copy()
    log_clean_step("drop_action_not_recognized", n_before, len(df),
                    "Rows where the rater flagged the action as not recognized were excluded")
else:
    log_warning("No action_not_recognized column found - skipping this exclusion step.")
""")

# ====================================================================
# 6. SCHEMA, TYPES, RANGE
# ====================================================================
md(r"""
## 6. Schema check and type conversion

We check that the required variables exist, that IDs are not missing,
that `rating` is numeric or safely convertible to numeric, and that
values fall within the allowed range \(\{1, \dots, 7\}\).
""")

code(r"""
required_cols = ["action_id", "rater_id", "rating"]
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    raise ValueError(f"Required variables missing from the raw dataset: {missing_cols}")

n0 = len(df)

# --- missing IDs ------------------------------------------------------
n_missing_action_id = df["action_id"].isna().sum()
n_missing_rater_id = df["rater_id"].isna().sum()
print(f"Missing action_id: {n_missing_action_id}")
print(f"Missing rater_id:  {n_missing_rater_id}")
if n_missing_action_id or n_missing_rater_id:
    log_warning(f"{n_missing_action_id + n_missing_rater_id} rows with a missing ID found.")
n_before = len(df)
df = df.dropna(subset=["action_id", "rater_id"]).copy()
log_clean_step("drop_missing_id", n_before, len(df), "Rows with missing action_id/rater_id removed")

# --- convert rating to numeric (robust against " 4 ", "n/a", etc.) -----
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

# ====================================================================
# 7. DUPLICATES
# ====================================================================
md(r"""
## 7. Duplicate (`action_id` x `rater_id`) combinations

**Documented resolution rule:** repeated occurrences of the same
rater-action combination are first listed in full in a table. Since
there is no reliable way to tell which of the repeated entries is the
intended one, we apply an explicit, conservative rule: *the row that
appears last in the sheet is kept* (a later entry in the export
typically reflects a correction). This assumption should be revisited
if the actual cause of duplicates in the sheet becomes known.
""")

code(r"""
dup_mask = df.duplicated(subset=["action_id", "rater_id"], keep=False)
tbl_duplicates = df.loc[dup_mask,
                          ["action_id", "rater_id", "rating", "rating_numeric_raw"]].sort_values(
    ["action_id", "rater_id"])
print(f"Rows with a duplicate (action_id, rater_id) combination: {len(tbl_duplicates)}")
if len(tbl_duplicates) > 0:
    print(tbl_duplicates)
    save_table(tbl_duplicates, "flagged_duplicate_rater_action_pairs")
    log_warning(
        f"{len(tbl_duplicates)} rows with duplicate (action_id, rater_id) "
        "combinations found. Resolution rule: the last entry is kept "
        "(see the markdown cell above)."
    )

n_before = len(df)
df = df.drop_duplicates(subset=["action_id", "rater_id"], keep="last").copy()
log_clean_step("resolve_duplicates", n_before, len(df),
                "Duplicates resolved: last entry per (action_id, rater_id) kept")

# --- final rating variables --------------------------------------------
df["rating_numeric"] = df["rating_numeric_raw"].astype(int)
df["rating_ordinal"] = pd.Categorical(df["rating_numeric"], categories=list(range(1, 8)),
                                        ordered=True)
df = df.drop(columns=["rating_numeric_raw"])

assert df["rating_numeric"].between(1, 7).all(), "Ratings outside 1-7 after cleaning!"
assert not df.duplicated(subset=["action_id", "rater_id"]).any(), "Duplicates remain after cleaning!"
assert df["action_id"].notna().all() and df["rater_id"].notna().all()

print(f"\nCleaning complete: {n0} -> {len(df)} rows.")
""")

# ====================================================================
# 8. RATING ORDER FROM TIMESTAMP
# ====================================================================
md(r"""
## 8. Rating order within each rater's session

The sheet records a `timestamp` for every rating but not an explicit
`rating_order`. We derive `rating_order` by ranking each rater's ratings
chronologically, so the temporal-drift check in the analysis notebooks
(which looks for a `rating_order` column) can run on the real data.
""")

code(r"""
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["rating_order"] = (
        df.sort_values("timestamp")
        .groupby("rater_id")
        .cumcount() + 1
    )
    df = df.sort_index()
else:
    log_warning("No timestamp column found - rating_order could not be derived.")
""")

# ====================================================================
# 9. SAVE THE CLEAN FILE
# ====================================================================
md(r"""
## 9. Save the preprocessed data

This is the file both analysis notebooks (`01_creativity_ratings_python.ipynb`,
`01_creativity_ratings_R.qmd`) and the overview notebook
(`01_data_overview.ipynb`) read as their starting point.
""")

code(r"""
CLEAN_PATH = DATA_PROCESSED / "ratings_long_clean.csv"
df.to_csv(CLEAN_PATH, index=False)
print(f"Cleaned data saved: {CLEAN_PATH} ({len(df)} rows)")

cleaning_log_df = pd.DataFrame(cleaning_log)
save_table(cleaning_log_df, "cleaning_log")
print(cleaning_log_df)

print(f"\nRaters: {df['rater_id'].nunique()}")
print(f"Actions: {df['action_id'].nunique()}")
print(f"Warnings collected: {len(WARNINGS_LOG)}")
df.head()
""")

if __name__ == "__main__":
    nb["cells"] = cells
    OUT.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, OUT)
    print(f"Notebook written with {len(cells)} cells: {OUT}")
