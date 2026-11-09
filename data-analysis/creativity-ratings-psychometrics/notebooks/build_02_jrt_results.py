# Builds notebooks/02_jrt_results.ipynb (display notebook for the manuscript).
# Usage (analysis folder, venv active): python notebooks/build_02_jrt_results.py notebooks/02_jrt_results.ipynb
# then execute it: jupyter nbconvert --to notebook --execute --inplace notebooks/02_jrt_results.ipynb
import nbformat as nbf, sys
out = sys.argv[1]
nb = nbf.v4.new_notebook()
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s))
code = lambda s: cells.append(nbf.v4.new_code_cell(s))

md("""# JRT results: graded response model, model ladder and reliability

Display notebook for the manuscript. It fits nothing: it shows the CSV and figure
outputs of the R pipeline in `../R/` (`01_data_design.R` … `08_reliability_min_ratings.R`, see
`../server/README.md` and `../AUDIT.md`) as labelled tables and figures (a few figures are drawn here from the CSVs),
so the manuscript can embed them. Re-execute it (seconds) after every pipeline run.
Objects whose source file does not exist yet show a placeholder line.

Numbers in the text come from these tables through the results-interpreter.

The rated products are the football actions; raters are the judges of judge response
theory. Raters with fewer than 15 ratings are excluded from the whole pipeline (decision
2026-10-22; see `results/data/excluded_raters.csv`). Short notes above each object say
what it shows; references are listed at the end.""")
code("""from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Markdown

RES = Path("..").resolve() / "results"

def _missing(path):
    return Markdown(f"_Not available yet: `results/{path}` (run the R pipeline)._")

def read_res(path):
    f = RES / path
    return pd.read_csv(f) if f.exists() else None

def fmt_cell(v, digits=3, p_value=False, decimals=False):
    # Display formatting only: whole numbers without decimals (unless the
    # column holds non-integer values: decimals=True), p-values below .001 as
    # "< .001" (APA), missing values as an en dash.
    if v is None or (isinstance(v, float) and pd.isna(v)) or (isinstance(v, str) and v in ("", "NA", "nan")):
        return "–"
    if isinstance(v, (bool, np.bool_)):
        return str(v)
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v).replace("|", r"\\|")  # a bare | would split the Markdown cell
    if p_value:
        return "< .001" if x < 0.001 else f"{x:.3f}"
    if x.is_integer() and not decimals:
        return f"{int(x):,}"
    return f"{x:,.{digits}f}"

# Columns that mix counts and fractions row by row (quantity/value tables):
# formatted cell by cell. All other columns with any non-integer value show
# every value with decimals (e.g. a correlation of 1 as 1.000).
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

# Readable column headers for the manuscript tables (display only; the CSVs keep
# the code names). Unlisted names: underscores become spaces.
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
    "index_value": "Value",
}
HEADERS.update({"design": "Design", "n_products_topped_up": "Products topped up", "n_ratings_added": "Ratings added",
                "n_reps": "Replications", "observed_mean_rel_post": "Observed mean rel_post",
                "simulated_empirical": "Simulated empirical reliability [95% range]"})
for _k in range(1, 8):
    HEADERS[f"cat_{_k}"] = f"Category {_k}"

# Readable values for code names in table cells (display only).
VALUES = {"M1_RSM": "M1 (rating-scale MFRM)", "M2_PCM": "M2 (partial-credit MFRM)", "M3_GPCM": "M3 (GPCM)", "GRM": "GRM",
          "rm_facets_default_grid": "M1, sirt default grid", "pearson": "Pearson", "spearman": "Spearman"}

import re

def readable_text(v):
    # code names in cells -> words; thousands separators in counts inside notes
    v = v.replace("_", " ")
    return re.sub(r"(?<![\\d.,])(\\d{1,3})(\\d{3})(?= (common|replications|products|ratings))", r"\\1,\\2", v)

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

def show_table(path, fn=None, digits=3):
    # Markdown table without the index column, for embedding in the manuscript.
    df = read_res(path)
    if df is None:
        return _missing(path)
    if fn is not None:
        df = fn(df)
    return Markdown(pretty_headers(pretty_values(tidy(df, digits))).to_markdown(index=False, disable_numparse=True))

def show_png(path, width=8):
    f = RES / path
    if not f.exists():
        return _missing(path)
    img = mpimg.imread(f)
    # One figure pixel per image pixel: no resampling of the R figure.
    dpi = img.shape[1] / width
    fig, ax = plt.subplots(figsize=(width, width * img.shape[0] / img.shape[1]), dpi=dpi)
    ax.imshow(img)
    ax.axis("off")
    fig.tight_layout(pad=0)
    plt.show()""")

def note(s):
    md(s)

def tbl(label, cap, call):
    code(f'#| label: {label}\n#| tbl-cap: "{cap}"\n{call}')
def fig(label, cap, call):
    code(f'#| label: {label}\n#| fig-cap: "{cap}"\n{call}')

code("""# Plot style for the figures drawn in this notebook (Okabe-Ito palette, colour-blind safe).
C = dict(blue="#0072B2", orange="#E69F00", green="#009E73", red="#D55E00",
         sky="#56B4E9", purple="#CC79A7", grey="#7F7F7F", ink="#222222")
PLOT_STYLE = {
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#E5E5E5", "grid.linewidth": 0.6,
    "axes.axisbelow": True, "axes.edgecolor": "#888888",
    "axes.labelcolor": C["ink"], "xtick.color": "#444444", "ytick.color": "#444444",
    "font.size": 9.5, "axes.titlesize": 10.5, "legend.frameon": False,
}

def r3(x):
    # three decimals without the leading zero for bounded statistics (display only)
    t = f"{x:.3f}"
    return t.replace("0.", ".", 1) if abs(x) < 1 else t

def _with_min4_row(d):
    # Adds the simulated "at least 4 ratings per product" design (grm/reliability_min_ratings.csv)
    # below the empirical reliability of the actual scores. Display only; the R output is unchanged.
    m = read_res("grm/reliability_min_ratings.csv")
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
    return pd.concat([d.iloc[:pos], row, d.iloc[pos:]], ignore_index=True)""")

md("## 1. Data and design")
note('**Design.** Size and coverage of the products × raters matrix that every model uses. The design is incomplete: each product is rated by a few raters only, and missing ratings are left out of the likelihood, not imputed. A connected design (one component) is required so that all raters and products lie on one scale (Eckes, 2015).')
tbl("tbl-design-summary", "Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design.",
    'show_table("data/design_summary.csv", lambda d: d[d["quantity"] != "data_fingerprint"])')
note("**Ratings per product.** Number of products by the number of ratings they received.")
fig("fig-design-ratings-per-product", "Number of products by number of ratings received.",
    '''_rpp = read_res("data/design_summary_ratings_per_product.csv")
with plt.rc_context(PLOT_STYLE):
    _f, _ax = plt.subplots(figsize=(7, 2.8))
    _ax.bar(_rpp["n_ratings"], _rpp["n_products"], color=C["blue"], width=0.75)
    for _x, _y in zip(_rpp["n_ratings"], _rpp["n_products"]):
        _ax.text(_x, _y, f"{_y:,}", ha="center", va="bottom", fontsize=8)
    _ax.set_xticks(_rpp["n_ratings"])
    _ax.set_xlabel("Ratings per product")
    _ax.set_ylabel("Products")
    _ax.grid(axis="x", visible=False)
    _f.tight_layout()
    plt.show()''')
tbl("tbl-excluded-raters", "Raters excluded from all analyses because they gave fewer than 15 ratings.",
    'show_table("data/excluded_raters.csv")')
note('**Category use.** How often each rater used each of the 7 categories. Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used.')
tbl("tbl-category-usage", "Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters.",
    'show_table("data/category_usage.csv", lambda d: d[["rater_id"] + [c for c in d if c.startswith("cat_")] + ["n_ratings", "missing_categories", "internal_gap"]])')
note("The same category use as shares of each rater's ratings. Raters sorted by mean rating; ✕ marks categories a rater never used.")
fig("fig-category-usage-shares", "Share of each rater's ratings in each of the 7 categories, sorted by the rater's mean rating; n = number of ratings; ✕ = category never used.",
    '''_cu = read_res("data/category_usage.csv").merge(read_res("data/design_summary_raters.csv")[["rater_id", "mean"]], on="rater_id").sort_values("mean", ascending=False)
_cc = [f"cat_{i}" for i in range(1, 8)]
_sh = _cu[_cc].div(_cu[_cc].sum(axis=1), axis=0).to_numpy()
_cm = plt.get_cmap("viridis_r")
with plt.rc_context(PLOT_STYLE):
    _f, _ax = plt.subplots(figsize=(7, 5.2))
    _y = np.arange(len(_cu))
    _left = np.zeros(len(_cu))
    for _j in range(7):
        _ax.barh(_y, _sh[:, _j], left=_left, color=_cm(.08 + .84 * _j / 6), height=.78, label=str(_j + 1), edgecolor="white", lw=.3)
        _left += _sh[:, _j]
    for _i, (_, _r) in enumerate(_cu.iterrows()):
        _un = ",".join(str(_j + 1) for _j in range(7) if _r[_cc[_j]] == 0)
        _ax.text(1.01, _i, f"n={int(_r['n_ratings'])}" + (f"  ✕ {_un}" if _un else ""), va="center", fontsize=7.5, color="#444444")
    _ax.set_yticks(_y, _cu["rater_id"], fontsize=8)
    _ax.set_xlim(0, 1)
    _ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    _ax.set_xlabel("Share of ratings")
    _ax.grid(False)
    _ax.legend(title="Category", ncol=7, loc="upper center", bbox_to_anchor=(.5, -.1), fontsize=8, title_fontsize=8)
    _f.tight_layout()
    plt.show()''')

md("## 2. Graded response model (central model)")
note('**Central model.** Judge response theory treats raters as items and products as persons (Myszkowski & Storme, 2019). It is fitted here as a graded response model (Samejima, 1969) by marginal maximum likelihood in `mirt` (Chalmers, 2012). The table shows whether estimation converged and gives the information criteria.')
tbl("tbl-grm-convergence", "Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature).",
    'show_table("grm/convergence.csv", lambda d: d.assign(tol=[power_of_ten(x) for x in d["tol"]])[["method", "quadpts", "se_type", "tol", "converged", "iterations", "information_matrix_pd", "logLik", "npar", "AIC", "BIC", "SABIC", "n_products", "n_ratings"]].rename(columns={"n_ratings": "ratings_total"}))')
note("**Rater parameters.** a is the rater's discrimination: how sharply the ratings separate products of different creativity. b_k is the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater. For a rater without an internal category gap, b_k separates categories k and k + 1; raters who never used the top categories have no estimate for the highest thresholds. For a rater with an internal gap (an unused category inside the observed range, see the category-use table), the thresholds separate other category boundaries and are not directly comparable with those of the other raters.")
tbl("tbl-grm-rater-parameters", "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used.",
    'show_table("grm/rater_parameters.csv", lambda d: est_se(d, ["a"] + [f"b{k}" for k in range(1, 7) if f"b{k}" in d])[["rater_id", "n_ratings", "a"] + [f"b{k}" for k in range(1, 7) if f"b{k}" in d]])')
note("Discrimination per rater as a figure, with 95% intervals (estimate ± 1.96 SE). Under M1 and M2 all raters would share one value.")
fig("fig-grm-rater-discrimination-ci", "Discrimination a per rater in the graded response model with 95% intervals (estimate ± 1.96 SE), sorted by a. Dashed line: median. Under the Rasch-family models M1 and M2 all raters share one value.",
    '''_g = read_res("grm/rater_parameters.csv").sort_values("a")
with plt.rc_context(PLOT_STYLE):
    _f, _ax = plt.subplots(figsize=(7, 4.4))
    _y = np.arange(len(_g))
    _ax.errorbar(_g["a"], _y, xerr=1.96 * _g["a_se"], fmt="o", color=C["blue"], ecolor="#9BBBD9", elinewidth=1.4, capsize=0, ms=5)
    _ax.axvline(_g["a"].median(), ls="--", color=C["grey"], lw=1)
    _ax.set_yticks(_y, _g["rater_id"], fontsize=8)
    _ax.set_xlabel("Discrimination a")
    _ax.grid(axis="y", visible=False)
    _f.tight_layout()
    plt.show()''')
note('**Category response functions.** The probability of each rating category as a function of θ, one panel per rater.')
fig("fig-grm-category-response-functions", "Category response functions of the graded response model for each rater.",
    'show_png("grm/figures/grm_category_response_functions.png", width=11)')
note('**Rater fit.** Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982). With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked. S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative. No misfit cut-offs for infit and outfit are applied in this notebook.')
tbl("tbl-grm-rater-fit", "Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X² pooled over multiple imputations of the missing ratings.",
    'show_table("grm/rater_fit.csv", lambda d: d[["rater_id", "n_ratings", "infit", "outfit", "S_X2", "df_S_X2", "p_S_X2", "n_imputations"]])')
note("**Local dependence.** Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. It is computed for rater pairs with at least 3 jointly rated products (and residual variance in both raters); other pairs are not computable. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). Flagged marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2.")
tbl("tbl-grm-q3-flagged", "Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products.",
    'show_table("grm/q3.csv", lambda d: d[d["n_common"] >= 30].assign(_a=lambda x: x["q3_minus_mean"].abs()).sort_values("_a", ascending=False).drop(columns=["_a", "overlap_flag"]).head(10))')
code('''_q3 = read_res("grm/q3.csv")
if _q3 is not None:
    _ok = _q3["q3"].notna()
    print(f"Mean Q3 over {int(_ok.sum())} computable rater pairs: {(_q3['q3'] - _q3['q3_minus_mean'])[_ok].iloc[0]:.3f}; "
          f"pairs flagged (flag_q3): {int(_q3['flag_q3'].sum())}")''')
note('**Global fit.** C2 is a limited-information test of overall model fit (Cai & Monroe, 2014). The table reports either the statistic or the reason it could not be computed: C2 needs the joint distribution of every pair of raters, which is undefined for rater pairs that share no products.')
tbl("tbl-grm-global-fit", "Limited-information absolute fit of the graded response model (C2).",
    'show_table("grm/global_fit.csv", lambda d: d.drop(columns=["q3_mirt_crosscheck_max_abs_diff"], errors="ignore"))')

md("## 3. Information and reliability")
note("**Rater information.** I_j(θ) shows how much a rater's rating tells about θ at each level of creativity. Information from different raters adds up under local independence.")
fig("fig-grm-rater-information", "Rater information functions of the graded response model.",
    'show_png("grm/figures/grm_rater_information.png")')
note("**Information shares.** Each rater's share of the total information of all raters, along θ.")
fig("fig-grm-information-shares", "Share of each rater in the information of the full panel across the latent continuum.",
    'show_png("grm/figures/grm_rater_information_shares.png")')
note("**Information summary.** For each rater: information averaged over the N(0, 1) distribution of θ, where it peaks, and the rater's share of the full-panel information.")
tbl("tbl-grm-information-summary", "Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ).",
    'show_table("grm/rater_information_summary.csv")')
note('**Full panel.** Information and conditional reliability I/(I+1) if every rater rated a product. This is a hypothetical upper bound, not the precision of the actual scores.')
note("**Uncertainty of rater information.** 95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings.")
tbl("tbl-grm-rater-information-ci", "Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws.",
    'show_table("grm/rater_information_ci.csv", lambda d: pd.DataFrame({"rater_id": d["rater_id"], "n_ratings": d["n_ratings"], "Information per rating [95% interval]": est_ci(d, "info_weighted_area", "info_ci_low", "info_ci_high"), "Share of panel information [95% interval]": est_ci(d, "share_weighted", "share_ci_low", "share_ci_high", digits=3)}))')
note("Average information per rating as a figure, with the same 95% intervals.")
fig("fig-grm-rater-information-ci", "Average information per rating (information integrated over θ ~ N(0, 1)) for each rater with 95% intervals from 200 accepted parameter draws, sorted by information. Point size is proportional to the square root of the rater's number of ratings.",
    '''_i = read_res("grm/rater_information_ci.csv").sort_values("info_weighted_area")
with plt.rc_context(PLOT_STYLE):
    _f, _ax = plt.subplots(figsize=(7, 4.4))
    _y = np.arange(len(_i))
    _ax.hlines(_y, _i["info_ci_low"], _i["info_ci_high"], color="#BBBBBB", lw=1.6)
    _ax.scatter(_i["info_weighted_area"], _y, s=10 + 120 * np.sqrt(_i["n_ratings"] / _i["n_ratings"].max()), color=C["green"], zorder=3)
    _ax.set_yticks(_y, _i["rater_id"], fontsize=8)
    _ax.set_xlabel("Information per rating")
    _ax.grid(axis="y", visible=False)
    _f.tight_layout()
    plt.show()''')
fig("fig-grm-panel-information", "Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters.",
    'show_png("grm/figures/grm_panel_information_reliability.png")')
note("**Reliability of the actual scores.** The empirical marginal reliability Var(θ̂)/(Var(θ̂) + mean PSD²) refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure. The model-based marginal reliability (Green et al., 1984) refers to the hypothetical full panel. rel_post = 1 − PSD² gives each product's reliability from its own raters.")
tbl("tbl-grm-reliability-summary", "Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info.",
    'show_table("grm/reliability_summary.csv")')
note('**Reliability by number of ratings.** How product-level precision grows with the number of ratings a product received.')
note("**Uncertainty of the marginal reliabilities.** 95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. Draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; Draws rejected counts these.")
tbl("tbl-grm-reliability-ci", "Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced.",
    'show_table("grm/reliability_ci.csv", lambda d: d[["quantity", "estimate", "ci_low", "ci_high", "n_draws", "n_draws_rejected"]])')
tbl("tbl-grm-reliability-by-n", "Product-level reliability and posterior SD by number of ratings per product.",
    'show_table("grm/reliability_by_n_ratings.csv", lambda d: d.rename(columns={"n_ratings": "ratings_per_product"}))')
note('Distribution of product-level reliability across products.')
fig("fig-grm-rel-post-histogram", "Distribution of the product-level reliability (1 − PSD²) across all products.",
    'show_png("grm/figures/grm_rel_post_histogram.png")')
note('Product-level reliability by number of ratings (the same information as the table above, as a figure).')
fig("fig-grm-rel-post-by-n", "Product-level reliability (1 − PSD²) by number of ratings per product.",
    'show_png("grm/figures/grm_rel_post_by_n_ratings.png")')
note("**Projected reliability with more ratings.** A model-based gauge of the value of adding ratings, complementing the observed values above. Products with θ ~ N(0, 1) are simulated; each gets k ratings from k raters of the actual panel, drawn at random, with ratings generated from the fitted GRM and scored with its parameters (treated as known). The table gives the empirical marginal reliability (mean and 95% range over replications) and the mean product-level reliability rel_post.")
tbl("tbl-grm-reliability-projection", "Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²).",
    'show_table("grm/reliability_projection.csv", lambda d: pd.DataFrame({"k": d["k"], "empirical": est_ci(d, "empirical", "empirical_q025", "empirical_q975", digits=3), "mean_rel_post": d["mean_rel_post"]}))')
fig("fig-grm-reliability-projection", "Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications.",
    'show_png("grm/figures/grm_reliability_projection.png", width=6)')
code('''_pr = read_res("grm/reliability_projection.csv")
if _pr is not None:
    print(f"{int(_pr['n_reps'].iloc[0])} replications of {int(_pr['n_products_per_rep'].iloc[0])} simulated products per k; seed {int(_pr['seed'].iloc[0])}.")''')
note("**Minimum number of ratings per product.** The actual design with every product topped up to at least 4 ratings: for each product with fewer than 4 ratings, the missing ratings are generated from the fitted GRM by raters of the panel drawn at random (equal probability), the real ratings are kept, and all products are rescored with the GRM (parameters treated as known). The row for the actual design repeats the simulation on the unchanged design, as a check against the observed empirical reliability.")
tbl("tbl-grm-reliability-min-ratings", "Simulated reliability of the actual design (check) and of the actual design topped up so that every product has at least 4 ratings: empirical marginal reliability with its 95% range over 50 replications, mean product-level reliability (1 − PSD²), and the number of products topped up and ratings added.",
    'show_table("grm/reliability_min_ratings.csv", lambda d: pd.DataFrame({"design": d["design"].map({"actual": "Actual design", "min_4": "At least 4 ratings per product"}).fillna(d["design"]), "n_products_topped_up": d["n_products_topped_up"], "n_ratings_added": d["n_ratings_added"], "ratings_total": d["n_ratings"], "empirical": est_ci(d, "empirical", "empirical_q025", "empirical_q975", digits=3), "mean_rel_post": d["mean_rel_post"], "n_reps": d["n_reps"]}))')
note("Observed and simulated reliability by number of ratings side by side. Observed: mean rel_post of the actual products with that many ratings. Simulated: the projection above (k raters drawn at random per simulated product).")
tbl("tbl-grm-reliability-observed-vs-simulated", "Reliability by number of ratings per product: observed mean product-level reliability (1 − PSD²) of the actual products, and simulated empirical marginal reliability with its 95% range over 50 replications (projection with randomly drawn raters).",
    '''_m = read_res("grm/reliability_projection.csv")[["k", "empirical", "empirical_q025", "empirical_q975"]].merge(
    read_res("grm/reliability_by_n_ratings.csv")[["n_ratings", "n_products", "rel_post_mean"]], left_on="k", right_on="n_ratings", how="outer")
_m["k"] = _m["k"].fillna(_m["n_ratings"]).astype(int)
_m = _m.sort_values("k")
Markdown(pretty_headers(pd.DataFrame({
    "k": _m["k"],
    "n_products": [("–" if pd.isna(v) else f"{int(v):,}") for v in _m["n_products"]],
    "observed_mean_rel_post": [("–" if pd.isna(v) else f"{v:.3f}") for v in _m["rel_post_mean"]],
    "simulated_empirical": [("–" if pd.isna(e) else f"{e:.3f} [{a:.3f}, {b:.3f}]") for e, a, b in zip(_m["empirical"], _m["empirical_q025"], _m["empirical_q975"])],
})).to_markdown(index=False, disable_numparse=True))''')
fig("fig-grm-reliability-observed-vs-simulated", "Reliability by number of ratings per product. Dots: observed mean product-level reliability (1 − PSD²) of the actual products with that many ratings (dot size = number of products; faded = fewer than 10 products). Line and band: simulated empirical marginal reliability (mean and 95% range over 50 replications) for products that each receive exactly k ratings from k raters drawn at random from the panel with equal probability, with ratings generated and scored by the fitted GRM. Dashed lines: simulated reliability of the actual design topped up to at least 4 ratings per product, and model-based reliability of the hypothetical full panel.",
    '''_pr = read_res("grm/reliability_projection.csv")
_bn = read_res("grm/reliability_by_n_ratings.csv")
_m4 = read_res("grm/reliability_min_ratings.csv").set_index("design").loc["min_4"]
_full = float(read_res("summary/reliability_overview.csv").set_index("index")["value"]["GRM: model-based marginal reliability"])
_nr = int(float(read_res("data/design_summary.csv").set_index("quantity")["value"]["n_raters"]))
with plt.rc_context(PLOT_STYLE):
    _f, _ax = plt.subplots(figsize=(7, 4))
    _ax.fill_between(_pr["k"], _pr["empirical_q025"], _pr["empirical_q975"], color=C["orange"], alpha=.25, lw=0)
    _ax.plot(_pr["k"], _pr["empirical"], color=C["orange"], lw=2, marker="s", ms=4, label="Simulated (k random raters)")
    _big = _bn["n_products"] >= 10
    _sz = 15 + 220 * np.sqrt(_bn["n_products"] / _bn["n_products"].max())
    _ax.scatter(_bn.loc[_big, "n_ratings"], _bn.loc[_big, "rel_post_mean"], s=_sz[_big], color=C["blue"], alpha=.85, zorder=3, label="Observed (actual products)")
    _ax.scatter(_bn.loc[~_big, "n_ratings"], _bn.loc[~_big, "rel_post_mean"], s=_sz[~_big], color=C["blue"], alpha=.25, zorder=3)
    _xmax = int(_bn["n_ratings"].max())
    for _lvl in (.70, .80):
        _ax.axhline(_lvl, color=C["grey"], ls=":", lw=1)
        _ax.text(_xmax + .2, _lvl, f"{_lvl:.2f}".lstrip("0"), va="center", fontsize=8, color=C["grey"])
    _ax.axhline(_m4["empirical"], color=C["purple"], ls="--", lw=1)
    _ax.text(_xmax + .3, _m4["empirical"] + .008, f"actual design, at least 4 ratings per product: {r3(_m4['empirical'])}", fontsize=8, color=C["purple"], ha="right")
    _ax.axhline(_full, color=C["green"], ls="--", lw=1)
    _ax.text(1, _full + .008, f"full panel of {_nr} raters: {r3(_full)}", fontsize=8, color=C["green"])
    _ax.set_xticks(range(1, _xmax + 1))
    _ax.set_xlim(.5, _xmax + .8)
    _ax.set_ylim(.45, 1.0)
    _ax.set_xlabel("Ratings per product")
    _ax.set_ylabel("Reliability")
    _ax.legend(loc="lower right")
    _f.tight_layout()
    plt.show()''')
note("Product-level reliability by estimated creativity. Precision depends on where a product lies relative to its raters' thresholds.")
fig("fig-grm-rel-post-by-theta", "Product-level reliability (1 − PSD²) by EAP estimate, coloured by number of ratings per product.",
    'show_png("grm/figures/grm_rel_post_by_theta.png")')
note("**Check.** Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree.")
fig("fig-grm-rel-consistency", "Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 − PSD²).",
    'show_png("grm/figures/grm_rel_consistency.png", width=6)')

md("## 4. Comparison: model ladder and MFRM")
note('**Model comparison.** The adjacent-category models form a ladder:\n- M1, the rating scale model with a rater shift (Andrich, 1978). This is the many-facet Rasch model (Linacre, 1989; Primi et al., 2019), fitted with `sirt::rm.facets`.\n- M2, the partial credit model (Masters, 1982): adds rater-specific thresholds.\n- M3, the generalized partial credit model (Muraki, 1992): adds rater-specific discriminations.\n\nThe GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better).')
tbl("tbl-model-fit", "Fit of the adjacent-category ladder (M1 rating-scale MFRM, M2 partial-credit MFRM, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion.",
    'show_table("comparison/model_fit.csv", lambda d: d[d["status"] == "estimated"][["model", "software", "family", "logLik", "npar", "AIC", "BIC", "SABIC", "delta_AIC", "delta_BIC", "delta_SABIC"]])')
note('**Likelihood-ratio tests.** Each test checks whether the next step up the ladder improves fit: rater-specific thresholds (M1 vs M2), then rater-specific discriminations (M2 vs M3). "df if all categories used" is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories.')
tbl("tbl-lr-tests", "Likelihood-ratio tests within the adjacent-category ladder. \'df if all categories used\' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2.",
    'show_table("comparison/lr_tests.csv", lambda d: d[["comparison", "X2", "df", "df_expected_formula", "df_matches_formula", "p"]])')
note('**Agreement of scores.** Correlations of the product scores between models. High values mean the ranking of products hardly depends on the model.')
tbl("tbl-theta-correlations", "Correlations of the EAP estimates between models (Pearson and Spearman). \'M1, sirt default grid\' is M1 re-estimated with the default quadrature grid of sirt, as a software check.",
    'show_table("comparison/theta_correlations.csv")')
note('Rater discriminations in M3. Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data.')
note("**Change in product ranking.** How far products move in the ranking when another model replaces the GRM: the mean and 95th-percentile shift in percentile rank, and the share of products that change quintile.")
tbl("tbl-score-agreement", "Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes.",
    'show_table("comparison/score_agreement.csv", lambda d: d.drop(columns=["reference"]))')
note("**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, separately for products with 1, 2 and 3 or more ratings. The raw mean is tied for almost all products (with one rating it takes only 7 values), so agreement is given as Kendall's τ-b and as the share of product pairs with different raw means that the GRM orders the other way round. The last two columns show how far apart the GRM scores of products with the same raw mean lie: products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination.")
tbl("tbl-raw-mean-vs-grm", "Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean.",
    'show_table("grm/raw_mean_vs_grm.csv", lambda d: d.rename(columns={"n_ratings": "ratings_per_product"}))')
note("The same comparison as a figure. Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal.")
fig("fig-raw-mean-vs-theta", "GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally.",
    'show_png("grm/figures/grm_raw_mean_vs_theta.png", width=9)')
note("**Sensitivity to the rater exclusion.** The GRM refitted on all raters, including the three with fewer than 15 ratings, compared with the final GRM: reliability, agreement of the product scores, and the discriminations of the common raters.")
tbl("tbl-sensitivity-rater-exclusion", "Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters.",
    'show_table("comparison/sensitivity_rater_exclusion.csv", digits=5)')
tbl("tbl-discrimination-m3", "Rater discriminations in the generalized partial credit model (M3).",
    'show_table("comparison/discrimination_m3.csv", lambda d: d[["rater_id", "n_ratings", "estimate", "se"]])')
note('Raters whose adjacent-category step parameters are out of order. In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction.')
tbl("tbl-threshold-order", "Raters with unordered step parameters in M2 (partial-credit MFRM) and M3 (GPCM).",
    'show_table("comparison/threshold_order.csv", lambda d: d[~d["ordered"]])')
note('Infit and outfit under M1, the fit statistics usually reported for many-facet Rasch models (Eckes, 2015).')
tbl("tbl-rater-fit-m1", "Rater infit and outfit mean squares under M1 (rating-scale MFRM).",
    'show_table("comparison/rater_fit_m1.csv", lambda d: d[["rater_id", "n_ratings", "infit", "outfit"]])')
note("**Rater severity under M1.** The rating-scale MFRM summarises each rater in one severity parameter (0 = average rater; higher = stricter), shown with 95% intervals next to the rater's raw mean rating.")
fig("fig-m1-rater-severity", "Left: rater severity in M1 (rating-scale MFRM) with 95% intervals (estimate ± 1.96 SE); 0 = average rater, higher = stricter. Right: the rater's raw mean rating (1–7). Raters sorted by severity.",
    '''_sv = read_res("comparison/rater_parameters_by_model.csv")
_sv = _sv[(_sv["model"] == "M1_RSM") & (_sv["parameter"] == "b_rater")][["rater_id", "estimate", "se"]].merge(
    read_res("data/design_summary_raters.csv")[["rater_id", "n_ratings", "mean"]], on="rater_id").sort_values("estimate")
with plt.rc_context(PLOT_STYLE):
    _f, (_a1, _a2) = plt.subplots(1, 2, figsize=(7, 4.8), sharey=True, gridspec_kw=dict(width_ratios=[1.6, 1]))
    _y = np.arange(len(_sv))
    _col = np.where(_sv["estimate"] > 0, C["red"], C["blue"])
    _a1.errorbar(_sv["estimate"], _y, xerr=1.96 * _sv["se"], fmt="none", ecolor="#BBBBBB", elinewidth=1.4)
    _a1.scatter(_sv["estimate"], _y, c=_col, s=28, zorder=3)
    _a1.axvline(0, color=C["grey"], lw=1)
    _a1.set_yticks(_y, _sv["rater_id"], fontsize=8)
    _a1.set_xlabel("Severity (logits): lenient ← 0 → strict")
    _a1.grid(axis="y", visible=False)
    _a2.barh(_y, _sv["mean"], color=_col, alpha=.75, height=.65)
    _a2.set_xlim(1, 7)
    _a2.set_xlabel("Raw mean rating")
    _a2.grid(axis="y", visible=False)
    _f.tight_layout()
    plt.show()''')
note('Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model.')
tbl("tbl-marginal-reliability-models", "Marginal and empirical reliability by model, for comparison.",
    'show_table("comparison/marginal_reliability.csv")')

md("## 5. Naive indices and overview")
note("**Naive indices** are reference values for common practice. They are not used downstream.\n- **Cronbach's α** (Cronbach, 1951) measures the consistency of the unweighted rater mean. It assumes τ-equivalent raters and complete data, so here it is computed from pairwise covariances and on the largest fully crossed block.\n- **Krippendorff's α** (ordinal; Hayes & Krippendorff, 2007) measures the agreement of single ratings, treating raters as interchangeable. Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (Failed replications in the table).")
code('''def naive_indices():
    cr, ka = read_res("naive/cronbach_alpha.csv"), read_res("naive/krippendorff_alpha.csv")
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
    ], ignore_index=True)''')
tbl("tbl-naive-indices", "Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate.",
    '_naive = naive_indices()\n_missing("naive/*.csv") if _naive is None else Markdown(pretty_headers(tidy(_naive)).to_markdown(index=False, disable_numparse=True))')
note('**Overview.** All indices side by side, with what each refers to. They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable.')
tbl("tbl-reliability-overview", "Overview of the reliability and agreement indices and what each refers to.",
    'show_table("summary/reliability_overview.csv", _with_min4_row)')
note("**Rater overview.** One row per rater: number of ratings, raw mean, M1 severity, GRM discrimination, share of the full-panel information with 95% interval, GRM infit and outfit (⚑ = flagged in the rater-fit output), and categories never used. Sorted by M1 severity.")
tbl("tbl-rater-overview", "Rater overview sorted by severity: number of ratings, raw mean rating, severity in M1 (rating-scale MFRM), discrimination a in the GRM, share of the full-panel information with 95% interval, GRM infit and outfit mean squares (⚑ = flagged), and categories never used.",
    '''_sv = read_res("comparison/rater_parameters_by_model.csv")
_sv = _sv[(_sv["model"] == "M1_RSM") & (_sv["parameter"] == "b_rater")][["rater_id", "estimate"]].rename(columns={"estimate": "severity_m1"})
_cc = [f"cat_{i}" for i in range(1, 8)]
_t = (read_res("data/design_summary_raters.csv")[["rater_id", "n_ratings", "mean"]]
      .merge(_sv, on="rater_id")
      .merge(read_res("grm/rater_parameters.csv")[["rater_id", "a"]], on="rater_id")
      .merge(read_res("grm/rater_information_ci.csv")[["rater_id", "share_weighted", "share_ci_low", "share_ci_high"]], on="rater_id")
      .merge(read_res("grm/rater_fit.csv")[["rater_id", "infit", "outfit", "flag_infit", "flag_outfit"]], on="rater_id")
      .merge(read_res("data/category_usage.csv")[["rater_id"] + _cc], on="rater_id")
      .sort_values("severity_m1"))
_unused = [",".join(str(j + 1) for j in range(7) if r[_cc[j]] == 0) or "–" for _, r in _t.iterrows()]
Markdown(pd.DataFrame({
    "Rater": _t["rater_id"], "Ratings": _t["n_ratings"].astype(int),
    "Mean rating": _t["mean"].map(lambda v: f"{v:.2f}"),
    "Severity (M1)": _t["severity_m1"].map(lambda v: f"{v:.2f}"),
    "a (GRM)": _t["a"].map(lambda v: f"{v:.2f}"),
    "Share of panel information [95% interval]": [f"{100 * s:.1f}% [{100 * l:.1f}, {100 * h:.1f}]" for s, l, h in zip(_t["share_weighted"], _t["share_ci_low"], _t["share_ci_high"])],
    "Infit / outfit (GRM)": [f"{i:.2f} / {o:.2f}" + (" ⚑" if (fi or fo) else "") for i, o, fi, fo in zip(_t["infit"], _t["outfit"], _t["flag_infit"], _t["flag_outfit"])],
    "Unused categories": _unused,
}).to_markdown(index=False, disable_numparse=True))''')

md("## References\n\n- Andrich, D. (1978). A rating formulation for ordered response categories. *Psychometrika, 43*(4), 561–573.\n- Cai, L., & Monroe, S. (2014). *A new statistic for evaluating item response theory models for ordinal data* (CRESST Report 839). University of California, Los Angeles.\n- Chalmers, R. P. (2012). mirt: A multidimensional item response theory package for the R environment. *Journal of Statistical Software, 48*(6), 1–29.\n- Christensen, K. B., Makransky, G., & Horton, M. (2017). Critical values for Yen's Q3: Identification of local dependence in the Rasch model using residual correlations. *Applied Psychological Measurement, 41*(3), 178–194.\n- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika, 16*(3), 297–334.\n- Eckes, T. (2015). *Introduction to many-facet Rasch measurement* (2nd ed.). Peter Lang.\n- Green, B. F., Bock, R. D., Humphreys, L. G., Linn, R. L., & Reckase, M. D. (1984). Technical guidelines for assessing computerized adaptive tests. *Journal of Educational Measurement, 21*(4), 347–360.\n- Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89.\n- Kang, T., & Chen, T. T. (2008). Performance of the generalized S-X² item fit index for polytomous IRT models. *Journal of Educational Measurement, 45*(4), 391–406.\n- Linacre, J. M. (1989). *Many-facet Rasch measurement*. MESA Press.\n- Masters, G. N. (1982). A Rasch model for partial credit scoring. *Psychometrika, 47*(2), 149–174.\n- Muraki, E. (1992). A generalized partial credit model: Application of an EM algorithm. *Applied Psychological Measurement, 16*(2), 159–176.\n- Myszkowski, N., & Storme, M. (2019). Judge response theory? A call to upgrade our psychometrical account of creativity judgments. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175.\n- Orlando, M., & Thissen, D. (2000). Likelihood-based item-fit indices for dichotomous item response theory models. *Applied Psychological Measurement, 24*(1), 50–64.\n- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 176–186.\n- Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement*, No. 17.\n- Wright, B. D., & Masters, G. N. (1982). *Rating scale analysis*. MESA Press.\n- Yen, W. M. (1984). Effects of local item dependence on the fit and equating performance of the three-parameter logistic model. *Applied Psychological Measurement, 8*(2), 125–145.")

nb["cells"] = cells
nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, out)
