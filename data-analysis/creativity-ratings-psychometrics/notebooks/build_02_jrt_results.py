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
outputs of the R pipeline in `../R/` (`01_data_design.R` … `06_summary.R`, see
`../server/README.md` and `../AUDIT.md`) as labelled tables and figures,
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

def fmt_cell(v, digits=3, p_value=False):
    # Display formatting only: whole numbers without decimals, p-values in
    # scientific notation below .001, missing values as an en dash.
    if v is None or (isinstance(v, float) and pd.isna(v)) or (isinstance(v, str) and v in ("", "NA", "nan")):
        return "–"
    if isinstance(v, (bool, np.bool_)):
        return str(v)
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v)
    if p_value:
        return f"{x:.2e}" if x < 0.001 else f"{x:.3f}"
    return f"{int(x)}" if x.is_integer() else f"{x:.{digits}f}"

def tidy(df, digits=3):
    out = df.copy().astype(object)
    for col in out.columns:
        is_p = col == "p" or col.startswith("p_")
        out[col] = [fmt_cell(v, digits, is_p) for v in df[col]]
    return out

def show_table(path, fn=None, digits=3):
    # Markdown table without the index column, for embedding in the manuscript.
    df = read_res(path)
    if df is None:
        return _missing(path)
    if fn is not None:
        df = fn(df)
    return Markdown(tidy(df, digits).to_markdown(index=False, disable_numparse=True))

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

md("## 1. Data and design")
note('**Design.** Size and coverage of the products × raters matrix that every model uses. The design is incomplete: each product is rated by a few raters only, and missing ratings are left out of the likelihood, not imputed. A connected design (one component) is required so that all raters and products lie on one scale (Eckes, 2015).')
tbl("tbl-design-summary", "Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design.",
    'show_table("data/design_summary.csv", lambda d: d[d["quantity"] != "data_fingerprint"])')
tbl("tbl-excluded-raters", "Raters excluded from all analyses because they gave fewer than 15 ratings.",
    'show_table("data/excluded_raters.csv")')
note('**Category use.** How often each rater used each of the 7 categories. Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used.')
tbl("tbl-category-usage", "Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters.",
    'show_table("data/category_usage.csv", lambda d: d[["rater_id"] + [c for c in d if c.startswith("cat_")] + ["n_ratings", "missing_categories", "internal_gap"]])')

md("## 2. Graded response model (central model)")
note('**Central model.** Judge response theory treats raters as items and products as persons (Myszkowski & Storme, 2019). It is fitted here as a graded response model (Samejima, 1969) by marginal maximum likelihood in `mirt` (Chalmers, 2012). The table shows whether estimation converged and gives the information criteria.')
tbl("tbl-grm-convergence", "Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature).",
    'show_table("grm/convergence.csv", lambda d: d[["method", "quadpts", "se_type", "tol", "converged", "iterations", "information_matrix_pd", "logLik", "npar", "AIC", "BIC", "SABIC", "n_products", "n_ratings"]])')
note("**Rater parameters.** a is the rater's discrimination: how sharply the ratings separate products of different creativity. b_k is the θ at which a rating at or above the k-th boundary becomes more likely than not; higher b means a stricter rater.")
tbl("tbl-grm-rater-parameters", "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k, each with its standard error (_se); category_boundaries states which rating categories each threshold separates.",
    'show_table("grm/rater_parameters.csv", lambda d: d[["rater_id", "n_ratings", "a", "a_se"] + [c for k in range(1, 7) for c in (f"b{k}", f"b{k}_se") if c in d] + ["category_boundaries"]])')
note('**Category response functions.** The probability of each rating category as a function of θ, one panel per rater.')
fig("fig-grm-category-response-functions", "Category response functions of the graded response model for each rater.",
    'show_png("grm/figures/grm_category_response_functions.png", width=11)')
note('**Rater fit.** Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982). With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked. S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative. No misfit cut-offs for infit and outfit are applied in this notebook.')
tbl("tbl-grm-rater-fit", "Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X2 pooled over multiple imputations of the missing ratings.",
    'show_table("grm/rater_fit.csv", lambda d: d[["rater_id", "n_ratings", "infit", "outfit", "S_X2", "df_S_X2", "p_S_X2", "n_imputations"]])')
note("**Local dependence.** Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). flag_q3 marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2.")
tbl("tbl-grm-q3-flagged", "Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products.",
    'show_table("grm/q3.csv", lambda d: d[d["n_common"] >= 30].assign(_a=lambda x: x["q3_minus_mean"].abs()).sort_values("_a", ascending=False).drop(columns="_a").head(10))')
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
tbl("tbl-grm-information-summary", "Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected theta).",
    'show_table("grm/rater_information_summary.csv")')
note('**Full panel.** Information and conditional reliability I/(I+1) if every rater rated a product. This is a hypothetical upper bound, not the precision of the actual scores.')
note("**Uncertainty of rater information.** 95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings.")
tbl("tbl-grm-rater-information-ci", "Average information per rating (info_weighted_area) and share of the full-panel information for each rater, with 95% intervals from parameter draws.",
    'show_table("grm/rater_information_ci.csv", lambda d: d.drop(columns=["n_draws"]))')
fig("fig-grm-panel-information", "Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters.",
    'show_png("grm/figures/grm_panel_information_reliability.png")')
note("**Reliability of the actual scores.** The empirical marginal reliability Var(θ̂)/(Var(θ̂) + mean PSD²) refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure. The model-based marginal reliability (Green et al., 1984) refers to the hypothetical full panel. rel_post = 1 − PSD² gives each product's reliability from its own raters.")
tbl("tbl-grm-reliability-summary", "Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info.",
    'show_table("grm/reliability_summary.csv")')
note('**Reliability by number of ratings.** How product-level precision grows with the number of ratings a product received.')
note("**Uncertainty of the marginal reliabilities.** 95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. n_draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; n_draws_rejected counts these.")
tbl("tbl-grm-reliability-ci", "Empirical and model-based marginal reliability of the GRM with 95% intervals.",
    'show_table("grm/reliability_ci.csv", lambda d: d[["quantity", "estimate", "ci_low", "ci_high", "n_draws", "n_draws_rejected"]])')
tbl("tbl-grm-reliability-by-n", "Product-level reliability and posterior SD by number of ratings per product.",
    'show_table("grm/reliability_by_n_ratings.csv")')
note('Distribution of product-level reliability across products.')
fig("fig-grm-rel-post-histogram", "Distribution of the product-level reliability rel_post across all products.",
    'show_png("grm/figures/grm_rel_post_histogram.png")')
note('Product-level reliability by number of ratings (the same information as the table above, as a figure).')
fig("fig-grm-rel-post-by-n", "Product-level reliability rel_post by number of ratings per product.",
    'show_png("grm/figures/grm_rel_post_by_n_ratings.png")')
note("Product-level reliability by estimated creativity. Precision depends on where a product lies relative to its raters' thresholds.")
fig("fig-grm-rel-post-by-theta", "Product-level reliability rel_post by EAP estimate.",
    'show_png("grm/figures/grm_rel_post_by_theta.png")')
note("**Check.** Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree.")
fig("fig-grm-rel-consistency", "Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 - PSD^2).",
    'show_png("grm/figures/grm_rel_consistency.png", width=6)')

md("## 4. Comparison: model ladder and MFRM")
note('**Model comparison.** The adjacent-category models form a ladder:\n- M1, the rating scale model with a rater shift (Andrich, 1978). This is the many-facet Rasch model (Linacre, 1989; Primi et al., 2019), fitted with `sirt::rm.facets`.\n- M2, the partial credit model (Masters, 1982): adds rater-specific thresholds.\n- M3, the generalized partial credit model (Muraki, 1992): adds rater-specific discriminations.\n\nThe GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better).')
tbl("tbl-model-fit", "Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion.",
    'show_table("comparison/model_fit.csv", lambda d: d[d["status"] == "estimated"][["model", "software", "family", "logLik", "npar", "AIC", "BIC", "SABIC", "delta_AIC", "delta_BIC", "delta_SABIC"]])')
note('**Likelihood-ratio tests.** Each test checks whether the next step up the ladder improves fit: rater-specific thresholds (M1 vs M2), then rater-specific discriminations (M2 vs M3). df_expected_formula is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories.')
tbl("tbl-lr-tests", "Likelihood-ratio tests within the adjacent-category ladder.",
    'show_table("comparison/lr_tests.csv", lambda d: d[["comparison", "X2", "df", "df_expected_formula", "df_matches_formula", "p"]])')
note('**Agreement of scores.** Correlations of the product scores between models. High values mean the ranking of products hardly depends on the model.')
tbl("tbl-theta-correlations", "Correlations of the EAP estimates between models (Pearson and Spearman).",
    'show_table("comparison/theta_correlations.csv")')
note('Rater discriminations in M3. Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data.')
note("**Change in product ranking.** How far products move in the ranking when another model replaces the GRM: the mean and 95th-percentile shift in percentile rank, and the share of products that change quintile.")
tbl("tbl-score-agreement", "Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes.",
    'show_table("comparison/score_agreement.csv", lambda d: d.drop(columns=["reference"]))')
note("**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, overall and by number of ratings per product: correlations, shift in percentile rank, share of products changing quintile, and how far apart the GRM scores of products with the same raw mean lie (mean and maximum range of θ̂ within groups of equal raw mean). Products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination.")
tbl("tbl-raw-mean-vs-grm", "Raw mean rating versus GRM score by number of ratings per product: correlations, absolute shift in percentile rank (0-1 scale), share of products changing quintile, and range of GRM scores among products with the same raw mean.",
    'show_table("grm/raw_mean_vs_grm.csv")')
note("The same comparison as a figure. Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal.")
fig("fig-raw-mean-vs-theta", "GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally.",
    'show_png("grm/figures/grm_raw_mean_vs_theta.png", width=9)')
note("**Sensitivity to the rater exclusion.** The GRM refitted on all raters, including the three with fewer than 15 ratings, compared with the final GRM: reliability, agreement of the product scores, and the discriminations of the common raters.")
tbl("tbl-sensitivity-rater-exclusion", "Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters.",
    'show_table("comparison/sensitivity_rater_exclusion.csv", digits=5)')
tbl("tbl-discrimination-m3", "Rater discriminations in the generalized partial credit model (M3).",
    'show_table("comparison/discrimination_m3.csv", lambda d: d[["rater_id", "n_ratings", "estimate", "se"]])')
note('Raters whose adjacent-category step parameters are out of order. In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction.')
tbl("tbl-threshold-order", "Raters with unordered step parameters in M2 (PCM) and M3 (GPCM).",
    'show_table("comparison/threshold_order.csv", lambda d: d[~d["ordered"]])')
note('Infit and outfit under M1, the fit statistics usually reported for many-facet Rasch models (Eckes, 2015).')
tbl("tbl-rater-fit-m1", "Rater infit and outfit mean squares under M1 (rating scale model / MFRM).",
    'show_table("comparison/rater_fit_m1.csv", lambda d: d[["rater_id", "n_ratings", "infit", "outfit"]])')
note('Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model.')
tbl("tbl-marginal-reliability-models", "Marginal and empirical reliability by model, for comparison.",
    'show_table("comparison/marginal_reliability.csv")')

md("## 5. Naive indices and overview")
note("**Naive indices** are reference values for common practice. They are not used downstream.\n- **Cronbach's α** (Cronbach, 1951) measures the consistency of the unweighted rater mean. It assumes τ-equivalent raters and complete data, so here it is computed from pairwise covariances and on the largest fully crossed block.\n- **Krippendorff's α** (ordinal; Hayes & Krippendorff, 2007) measures the agreement of single ratings, treating raters as interchangeable. Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (n_boot_failed in the table).")
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
tbl("tbl-naive-indices", "Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products.",
    '_naive = naive_indices()\n_missing("naive/*.csv") if _naive is None else Markdown(tidy(_naive).to_markdown(index=False, disable_numparse=True))')
note('**Overview.** All indices side by side, with what each refers to. They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable.')
tbl("tbl-reliability-overview", "Overview of the reliability and agreement indices and what each refers to.",
    'show_table("summary/reliability_overview.csv")')

md("## References\n\n- Andrich, D. (1978). A rating formulation for ordered response categories. *Psychometrika, 43*(4), 561–573.\n- Cai, L., & Monroe, S. (2014). *A new statistic for evaluating item response theory models for ordinal data* (CRESST Report 839). University of California, Los Angeles.\n- Chalmers, R. P. (2012). mirt: A multidimensional item response theory package for the R environment. *Journal of Statistical Software, 48*(6), 1–29.\n- Christensen, K. B., Makransky, G., & Horton, M. (2017). Critical values for Yen's Q3: Identification of local dependence in the Rasch model using residual correlations. *Applied Psychological Measurement, 41*(3), 178–194.\n- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika, 16*(3), 297–334.\n- Eckes, T. (2015). *Introduction to many-facet Rasch measurement* (2nd ed.). Peter Lang.\n- Green, B. F., Bock, R. D., Humphreys, L. G., Linn, R. L., & Reckase, M. D. (1984). Technical guidelines for assessing computerized adaptive tests. *Journal of Educational Measurement, 21*(4), 347–360.\n- Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89.\n- Kang, T., & Chen, T. T. (2008). Performance of the generalized S-X² item fit index for polytomous IRT models. *Journal of Educational Measurement, 45*(4), 391–406.\n- Linacre, J. M. (1989). *Many-facet Rasch measurement*. MESA Press.\n- Masters, G. N. (1982). A Rasch model for partial credit scoring. *Psychometrika, 47*(2), 149–174.\n- Muraki, E. (1992). A generalized partial credit model: Application of an EM algorithm. *Applied Psychological Measurement, 16*(2), 159–176.\n- Myszkowski, N., & Storme, M. (2019). Judge response theory? A call to upgrade our psychometrical account of creativity judgments. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175.\n- Orlando, M., & Thissen, D. (2000). Likelihood-based item-fit indices for dichotomous item response theory models. *Applied Psychological Measurement, 24*(1), 50–64.\n- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 176–186.\n- Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement*, No. 17.\n- Wright, B. D., & Masters, G. N. (1982). *Rating scale analysis*. MESA Press.\n- Yen, W. M. (1984). Effects of local item dependence on the fit and equating performance of the three-parameter logistic model. *Applied Psychological Measurement, 8*(2), 125–145.")

nb["cells"] = cells
nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, out)
