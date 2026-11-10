"""Display helpers for the results notebooks 02_jrt_results and 03_jrt_supplement.

The notebooks fit nothing: they show the CSV and figure outputs of the R pipeline
(../R/) as labelled tables and figures for the manuscript. `read_res(name)` looks
for a CSV in results/main, results/supplement and results/data, so the folder
split (main-paper vs supplementary objects) is a reporting classification only.
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Markdown

RES = Path(__file__).resolve().parent.parent / "results"
CSV_DIRS = [RES / "main", RES / "supplement", RES / "data"]
FIG_DIRS = [RES / "main" / "figures", RES / "supplement" / "figures"]


def _missing(name):
    return Markdown(f"_Not available yet: `{name}` (run the R pipeline)._")


def find_res(name, dirs=CSV_DIRS):
    for d in dirs:
        if (d / name).exists():
            return d / name
    return None


def read_res(name):
    f = find_res(name)
    return pd.read_csv(f) if f is not None else None


# --- number and header formatting (display only; the CSVs keep the raw values) ----
def fmt_cell(v, digits=3, p_value=False, decimals=False):
    # Whole numbers without decimals (unless the column holds non-integer values:
    # decimals=True), p-values below .001 as "< .001" (APA), missing values as an en dash.
    if v is None or (isinstance(v, float) and pd.isna(v)) or (isinstance(v, str) and v in ("", "NA", "nan")):
        return "–"
    if isinstance(v, (bool, np.bool_)):
        return str(v)
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v).replace("|", r"\|")  # a bare | would split the Markdown cell
    if p_value:
        return "< .001" if x < 0.001 else f"{x:.3f}"
    if x.is_integer() and not decimals:
        return f"{int(x):,}"
    return f"{x:,.{digits}f}"


# Columns that mix counts and fractions row by row (quantity/value tables) are
# formatted cell by cell; other columns with any non-integer value show decimals throughout.
MIXED_COLUMNS = {"value", "final_data", "all_raters", "estimate"}


def tidy(df, digits=3):
    out = df.copy().astype(object)
    for col in out.columns:
        is_p = col == "p" or col.startswith("p_")
        num = pd.to_numeric(df[col], errors="coerce") if df[col].dtype != bool else None
        decimals = (col not in MIXED_COLUMNS and num is not None and num.notna().any()
                    and not (num.dropna() % 1 == 0).all())
        out[col] = [fmt_cell(v, digits, is_p, decimals) for v in df[col]]
    return out


HEADERS = {
    "rater_id": "Rater", "n_ratings": "Ratings by rater", "ratings_per_product": "Ratings per product",
    "ratings_total": "Ratings (total)", "n_products": "Products", "n_raters": "Raters",
    "reason": "Reason", "quantity": "Quantity", "value": "Value", "estimate": "Estimate", "se": "SE",
    "ci_low": "95% CI lower", "ci_high": "95% CI upper", "note": "Note", "model": "Model",
    "n_categories_used": "Categories used", "missing_categories": "Missing categories",
    "internal_gap": "Internal gap", "method": "Method", "quadpts": "Quadrature points",
    "se_type": "SE type", "tol": "Tolerance", "converged": "Converged", "iterations": "Iterations",
    "information_matrix_pd": "Information matrix positive definite", "logLik": "Log-likelihood",
    "npar": "Parameters", "infit": "Infit", "outfit": "Outfit", "S_X2": "S-X²", "df_S_X2": "df",
    "p_S_X2": "p", "n_imputations": "Imputations", "rater_1": "Rater 1", "rater_2": "Rater 2",
    "n_common": "Shared products", "q3": "Q3", "q3_minus_mean": "Q3 minus mean Q3",
    "overlap_flag": "Overlap", "flag_q3": "Flagged", "statistic": "Statistic", "computable": "Computable",
    "rater_pairs": "Rater pairs", "rater_pairs_without_overlap": "Rater pairs without shared products",
    "info_weighted_area": "Information per rating", "theta_at_max": "θ at maximum",
    "info_max": "Maximum information", "share_weighted": "Share of panel information",
    "share_at_theta_-2": "Share at θ = −2", "share_at_theta_-1": "Share at θ = −1",
    "share_at_theta_+0": "Share at θ = 0", "share_at_theta_+1": "Share at θ = 1",
    "share_at_theta_+2": "Share at θ = 2", "n_draws": "Draws", "n_draws_rejected": "Draws rejected",
    "rel_post_mean": "Mean rel_post", "rel_post_median": "Median rel_post",
    "rel_info_mean": "Mean rel_info", "psd_mean": "Mean PSD", "software": "Software", "family": "Family",
    "delta_AIC": "ΔAIC", "delta_BIC": "ΔBIC", "delta_SABIC": "ΔSABIC", "comparison": "Comparison",
    "X2": "χ²", "df_expected_formula": "df if all categories used",
    "df_matches_formula": "df equal", "pearson": "Pearson r", "spearman": "Spearman ρ",
    "mean_abs_percentile_shift": "Mean percentile shift",
    "p95_abs_percentile_shift": "95th percentile of shift", "max_abs_percentile_shift": "Maximum shift",
    "share_products_changing_quintile": "Share changing quintile",
    "share_products_changing_quintile_by_2_or_more": "Share changing ≥ 2 quintiles",
    "final_data": "Final data", "all_raters": "All raters", "n_steps": "Steps", "ordered": "Ordered",
    "n_reversals": "Reversals", "steps": "Step parameters", "latent_variance": "Latent variance",
    "marginal_reliability": "Marginal reliability", "marginal_rxx_mirt": "marginal_rxx (mirt)",
    "empirical_rxx": "Empirical reliability", "index": "Index", "refers_to": "Refers to",
    "ci_or_note": "CI or note", "n_boot": "Bootstrap replications", "n_boot_failed": "Failed replications",
    "kendall_tau_b": "Kendall's τ-b", "share_discordant_pairs": "Share of pairs in reversed order",
    "mean_theta_range_same_raw_mean": "Mean θ̂ range at equal raw mean",
    "max_theta_range_same_raw_mean": "Maximum θ̂ range at equal raw mean",
    "k": "Ratings per product (k)", "empirical": "Empirical reliability [95% range]",
    "true_r2": "Squared correlation with true θ", "mean_rel_post": "Mean rel_post",
    "index_value": "Value", "design": "Design", "n_products_topped_up": "Products topped up",
    "n_ratings_added": "Ratings added", "n_reps": "Replications", "observed_mean_rel_post": "Observed mean rel_post",
    "simulated_empirical": "Simulated empirical reliability [95% range]",
}
for _k in range(1, 8):
    HEADERS[f"cat_{_k}"] = f"Category {_k}"

# Readable values for code names in table cells (display only).
VALUES = {"M1_RSM": "M1 (rating-scale MFRM)", "M2_PCM": "M2 (partial-credit MFRM)", "M3_GPCM": "M3 (GPCM)", "GRM": "GRM",
          "rm_facets_default_grid": "M1, sirt default grid", "pearson": "Pearson", "spearman": "Spearman"}


def readable_text(v):
    # code names in cells -> words; thousands separators in counts inside notes
    v = v.replace("_", " ")
    return re.sub(r"(?<![\d.,])(\d{1,3})(\d{3})(?= (common|replications|products|ratings))", r"\1,\2", v)


def pretty_values(df):
    out = df.copy()
    for col in out.columns:
        out[col] = [VALUES.get(v, readable_text(v)) if isinstance(v, str) else v for v in out[col]]
    return out


def pretty_headers(df):
    return df.rename(columns=lambda c: HEADERS.get(c, VALUES.get(c, c.replace("_", " "))))


def power_of_ten(x):
    # e.g. 1e-4 -> "10⁻⁴" (a string, so the number formatting leaves it alone)
    return "10" + str(int(round(np.log10(x)))).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))


def est_ci(d, est, low, high, digits=2):
    # "estimate [low, high]" in one cell, for compact tables.
    return [f"{e:.{digits}f} [{l:.{digits}f}, {h:.{digits}f}]" for e, l, h in zip(d[est], d[low], d[high])]


def est_se(d, cols, digits=2):
    # "estimate (SE)" in one cell, for compact parameter tables.
    out = d.copy()
    for c in cols:
        out[c] = [("–" if pd.isna(e) else f"{e:.{digits}f} ({s:.{digits}f})") for e, s in zip(d[c], d[f"{c}_se"])]
    return out.drop(columns=[f"{c}_se" for c in cols])


def r3(x):
    # three decimals without the leading zero for bounded statistics (display only)
    t = f"{x:.3f}"
    return t.replace("0.", ".", 1) if abs(x) < 1 else t


def md_table(df):
    return Markdown(df.to_markdown(index=False, disable_numparse=True))


def show_table(name, fn=None, digits=3):
    # Markdown table without the index column, for embedding in the manuscript.
    df = read_res(name)
    if df is None:
        return _missing(name)
    if fn is not None:
        df = fn(df)
    return md_table(pretty_headers(pretty_values(tidy(df, digits))))


def show_png(name, width=8):
    f = find_res(name, FIG_DIRS)
    if f is None:
        return _missing(name)
    img = mpimg.imread(f)
    dpi = img.shape[1] / width  # one figure pixel per image pixel: no resampling of the R figure
    fig, ax = plt.subplots(figsize=(width, width * img.shape[0] / img.shape[1]), dpi=dpi)
    ax.imshow(img)
    ax.axis("off")
    fig.tight_layout(pad=0)
    plt.show()


# --- plot style for the figures drawn in the notebooks (Okabe-Ito, colour-blind safe) ----
C = dict(blue="#0072B2", orange="#E69F00", green="#009E73", red="#D55E00",
         sky="#56B4E9", purple="#CC79A7", grey="#7F7F7F", ink="#222222")
PLOT_STYLE = {
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#E5E5E5", "grid.linewidth": 0.6,
    "axes.axisbelow": True, "axes.edgecolor": "#888888",
    "axes.labelcolor": C["ink"], "xtick.color": "#444444", "ytick.color": "#444444",
    "font.size": 9.5, "axes.titlesize": 10.5, "legend.frameon": False,
}


# --- composite tables --------------------------------------------------------------
def naive_indices():
    cr, ka = read_res("cronbach_alpha.csv"), read_res("krippendorff_alpha.csv")
    if cr is None or ka is None:
        return None
    return pd.concat([
        pd.DataFrame({"index": "Cronbach's alpha: " + cr["variant"], "value": cr["raw_alpha"],
                      "ci_low": cr.get("ci_low"), "ci_high": cr.get("ci_high"), "n_raters": cr["n_raters"],
                      "n_products": cr["n_products_contributing"],
                      "n_boot": cr.get("n_boot"), "n_boot_failed": cr.get("n_boot_failed")}),
        pd.DataFrame({"index": "Krippendorff's alpha (ordinal)", "value": ka["alpha"],
                      "ci_low": ka["ci_low"], "ci_high": ka["ci_high"], "n_raters": ka["n_raters"],
                      "n_products": ka["n_pairable_units"],
                      "n_boot": ka.get("n_boot"), "n_boot_failed": ka.get("n_boot_failed")}),
    ], ignore_index=True)


def with_min4_row(d):
    # Adds the simulated "at least 4 ratings per product" design (reliability_min_ratings.csv)
    # below the empirical reliability of the actual scores. Display only.
    m = read_res("reliability_min_ratings.csv")
    if m is None or "min_4" not in set(m["design"]):
        return d
    r = m.set_index("design").loc["min_4"]
    row = pd.DataFrame([{"index": "GRM: empirical marginal reliability, at least 4 ratings per product (simulated)",
                         "refers_to": "actual design topped up to at least 4 ratings per product",
                         "value": r["empirical"],
                         "ci_or_note": f"95% range [{r['empirical_q025']:.3f}, {r['empirical_q975']:.3f}], {int(r['n_reps'])} replications; "
                                       f"{int(r['n_ratings_added']):,} ratings added to {int(r['n_products_topped_up']):,} products"}])
    i = d.index[d["index"] == "GRM: empirical marginal reliability"]
    pos = (int(i[0]) + 1) if len(i) else len(d)
    return pd.concat([d.iloc[:pos], row, d.iloc[pos:]], ignore_index=True)
