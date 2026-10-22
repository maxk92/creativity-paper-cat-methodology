# 02 Artifacts: embeddable objects (regenerated)

Scope: the three in-scope notebooks only:
- `00_data_loading_preprocessing.ipynb`
- `01_data_overview.ipynb`
- `02d_judge_response_theory.ipynb`

All live in `data-analysis/creativity-ratings-psychometrics/notebooks/`. Excluded and not used: 02a, 02b, 02c, 03_approach_comparison, `02_creativity_ratings_R.qmd`, and all `classical_*`, `lmm_*`, `mfrm_*`, `comparison_*` and `sample_description_summary*` outputs.

**Embed path base.** Paths are relative to `manuscript/manuscript.qmd`, so the prefix is `../data-analysis/creativity-ratings-psychometrics/notebooks/`. This resolves because `manuscript/` and `data-analysis/` are siblings under the project root.

**Notation.** `R/T` stands for `results/tables/` and `R/F` for `results/figures/`. Every figure listed has `.png` and `.svg` versions. "Stored output" means a rendered output is saved in the `.ipynb`: an image for figures, an execute_result for tables.

**Placement column (mechanical).**
- **Main** = descriptive or core result object.
- **Supp** = diagnostic, convergence, model-check or data-processing object.
- **Internal** = a values table meant to feed in-text numbers, not to be displayed.

## 1. Inventory

| # | label | type | source notebook | source cell id | exported file(s) | caption (verbatim from cell) | stored output | placement | embed snippet |
|---|---|---|---|---|---|---|---|---|---|
| 1 | tbl-cleaning-log | tbl | 00_data_loading_preprocessing | bbcbf730 | R/T/cleaning_log.csv (saved in the preceding cell dd37b3ec) | Data cleaning steps with the number of rows before and after each step. | yes | Supp (or Method) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` |
| 2 | tbl-overview-ratings-per-action | tbl | 01_data_overview | 9307f652 | R/T/sample_ratings_per_action.csv | Number of actions by number of ratings received, with the mean and harmonic mean number of ratings per action. | yes | Main (sample/design) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-ratings-per-action >}}` |
| 3 | fig-overview-rater-overlap | fig | 01_data_overview | aa371443 | R/F/fig_overview_rater_overlap.png/.svg (no _caption.txt) | Number of jointly rated actions for each pair of raters. | yes | Supp (design diagnostic) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-overlap >}}` |
| 4 | fig-overview-rating-distribution | fig | 01_data_overview | 31873726 | R/F/fig_overview_rating_distribution.png/.svg/_caption.txt; the same cell also saves R/T/overview_category_frequencies.csv | Frequency of the seven rating categories across all ratings. | yes | Main (descriptive) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rating-distribution >}}` |
| 5 | fig-overview-rater-response-styles | fig | 01_data_overview | 374f3c3d | R/F/fig_overview_rater_response_styles.png/.svg/_caption.txt (underlying data: R/T/rater_descriptive_statistics.csv, from unlabelled cell fb6df84b) | Descriptive rater response styles: (A) rater means, (B) rater standard deviations, (C) number of rating categories used, (D) share of extreme (1, 7) versus middle (3-5) categories; point size is proportional to the number of ratings. | yes | Main or Supp (descriptive) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-response-styles >}}` |
| 6 | fig-overview-degree-distributions | fig | 01_data_overview | 9f03e286 | R/F/fig_overview_degree_distributions.png/.svg/_caption.txt; the same cell saves R/T/connectivity_component_summary.csv | Degree distributions of the bipartite rater-action design: (A) number of raters per action, (B) number of actions per rater. | yes | Supp (design diagnostic; overlaps item 2) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-degree-distributions >}}` |
| 7 | tbl-jrt-convergence | tbl | 02d_judge_response_theory | c82c7804 | R/T/jrt_convergence_by_group.csv (this cell also saves R/T/jrt_model_summary.csv) | Convergence diagnostics of the JRT model by parameter group: largest split R-hat, smallest bulk and tail effective sample size, and number of parameters. | yes | Supp (convergence) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-convergence >}}` |
| 8 | tbl-jrt-model-summary | tbl | 02d_judge_response_theory | jrtsum01 | R/T/jrt_model_summary.csv (written by cell c82c7804) | Posterior summaries of the JRT thresholds and hyperparameters. | yes | Supp (parameter summary) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-model-summary >}}` |
| 9 | tbl-jrt-rater-parameters | tbl | 02d_judge_response_theory | jrtrat01 | R/T/jrt_rater_table.csv | Rater parameters of the JRT model: posterior mean and 95% credible interval of discrimination a_j and leniency lambda_j (relative to the average rater), with the number of ratings per rater. | yes | Supp (22-row table that duplicates item 10) or Main | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-rater-parameters >}}` |
| 10 | fig-jrt-rater-parameters | fig | 02d_judge_response_theory | jrtfig01 | R/F/fig_jrt_rater_parameters.png/.svg/_caption.txt (rater caterpillar plot) | Rater parameters of the JRT model with 95% credible intervals: (A) discrimination a_j (dashed line: pool discrimination exp(mu_log_a)), (B) leniency lambda_j relative to the average rater (dashed line: 0). Raters are sorted by discrimination. | yes | Main | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#fig-jrt-rater-parameters >}}` |
| 11 | fig-jrt-traceplots | fig | 02d_judge_response_theory | jrttrc01 | R/F/fig_jrt_traceplots.png/.svg/_caption.txt | Trace plots (left) and per-chain posterior densities (right) of the JRT thresholds and hyperparameters; colours denote the four chains. | yes | Supp (convergence) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#fig-jrt-traceplots >}}` |
| 12 | fig-jrt-ppc | fig | 02d_judge_response_theory | jrtppc01 | R/F/fig_jrt_ppc.png/.svg/_caption.txt; the same cell saves R/T/jrt_ppc_category_shares.csv and R/T/jrt_ppc_rater_means.csv | Posterior predictive check of the JRT model: (A) observed share of each rating category (points) with the 95% posterior predictive interval (bars); (B) observed versus posterior predictive mean rating per rater, with 95% intervals (diagonal: perfect agreement). | yes | Supp (model check) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#fig-jrt-ppc >}}` |
| 13 | tbl-jrt-equal-discrimination-loo | tbl | 02d_judge_response_theory | e6164b08 | R/T/jrt_loo_comparison.csv; the same cell saves R/T/jrt_equal_discrimination_convergence.csv | PSIS-LOO comparison of the JRT model with rater-specific discrimination and the nested equal-discrimination model. | yes | Main (model comparison) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-equal-discrimination-loo >}}` |
| 14 | fig-jrt-category-curves-information | fig | 02d_judge_response_theory | 015e75b6 | R/F/fig_jrt_category_curves_information.png/.svg/_caption.txt; the same cell saves and displays R/T/jrt_information_by_rater.csv | Category probabilities (top) and graded-response Fisher information (bottom) for the raters with the lowest (A), median (B) and highest (C) JRT discrimination. | yes (figure plus a table execute_result) | Main | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#fig-jrt-category-curves-information >}}` |
| 15 | fig-jrt-information-reliability | fig | 02d_judge_response_theory | e72f0b74 | R/F/fig_jrt_information_reliability.png/.svg/_caption.txt; the same cell saves R/T/jrt_marginal_reliability.csv (D-study figure) | (A) Information of the rater pool across the latent creativity continuum (sum over all raters and mean per rating). (B) Marginal reliability of theta as a function of the number of judges per action (IRT D-study); the dashed line marks the realised harmonic-mean number of ratings per action. | yes | Main | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#fig-jrt-information-reliability >}}` |
| 16 | tbl-jrt-d-study | tbl | 02d_judge_response_theory | jrtdst01 | R/T/jrt_marginal_reliability.csv (written by cell e72f0b74) | Marginal reliability of the JRT scores by number of judges per action (IRT D-study). | yes | Main (or Supp; duplicates item 15 panel B) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-d-study >}}` |
| 17 | tbl-jrt-score-precision | tbl | 02d_judge_response_theory | jrtprc01 | R/T/jrt_score_precision_by_n.csv | Precision of the JRT action scores by number of ratings per action: number of actions, mean and range of the posterior SD of theta, and mean width of the 95% credible interval. | yes | Main | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-score-precision >}}` |
| 18 | tbl-jrt-derived-counts | tbl | 02d_judge_response_theory | jrtder01 | R/T/jrt_derived_counts.csv | Derived quantities of the JRT model used in the text. | yes | Internal (source of in-text numbers; Supp at most) | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02d_judge_response_theory.ipynb#tbl-jrt-derived-counts >}}` |

**Totals:** 9 figures and 9 tables (18 labelled objects). 00: 1 table. 01: 1 table and 4 figures. 02d: 7 tables and 5 figures.

## 2. Exported outputs WITHOUT their own label (cannot be embedded as standalone objects)

| exported file | where produced | status |
|---|---|---|
| R/T/overview_krippendorff_alpha.csv | 01, unlabelled cell 2d38a684 | Only print output; nothing to embed. Values must reach the text through the results-interpreter. To embed it as a table, the author would need to add a labelled display cell. |
| R/T/overview_category_frequencies.csv | 01, inside the `fig-overview-rating-distribution` cell (31873726) | Printed as plain text only; there is no table display. |
| R/T/rater_descriptive_statistics.csv | 01, unlabelled cell fb6df84b (displays a DataFrame) | Has a rich output but no `tbl-` label. |
| R/T/overview_drift_correlation_by_rater.csv | 01, unlabelled cell 4e8b9214 | Print output only. |
| R/T/connectivity_component_summary.csv | 01, inside the `fig-overview-degree-distributions` cell | Saved only. |
| R/T/rater_by_action_type_contingency.csv | 01, unlabelled cell 976a6f9b (displays a percentage crosstab) | No label. |
| R/T/jrt_ppc_category_shares.csv, R/T/jrt_ppc_rater_means.csv | 02d, inside the `fig-jrt-ppc` cell | Saved only; not displayed as tables. |
| R/T/jrt_information_by_rater.csv | 02d, inside the `fig-jrt-category-curves-information` cell | Displayed as an execute_result, so it will appear together with the figure when embedded (see Problem 5). |
| R/T/jrt_equal_discrimination_convergence.csv | 02d, inside the `tbl-jrt-equal-discrimination-loo` cell | Saved only. |
| R/T/scores_jrt.csv, R/T/raters_jrt.csv, R/T/model_diagnostics_jrt.csv, R/T/warnings_log_jrt.csv | 02d, later unlabelled cells | Data and log exports; not display objects. |
| R/T/flagged_action_not_recognized.csv, R/T/flagged_out_of_range_ratings.csv, R/T/flagged_duplicate_rater_action_pairs.csv | 00 | Row-level audit files; not display objects. |

These figures are stored in the notebook but are unlabelled and not exported, so they can't be embedded: in 01, cell 3b12b8bf (bar chart of ratings per action and histogram of ratings per rater), cell 01a61b19 (rater-tendency scatter/line plot) and cell a3a60c1e (PairGrid of the secondary rating dimensions).

## 3. Problems for the user

1. **Malformed labels or prefix mismatches:** none. All `fig-` labels are on figure cells and all `tbl-` labels are on table-display cells.
2. **Duplicate labels:** none, across the three notebooks or anywhere under `data-analysis/creativity-ratings-psychometrics`.
3. **Missing stored output:** none. All 18 labelled cells have a stored figure image or table execute_result.
4. **Missing captions:** none. All 18 cells carry `fig-cap`/`tbl-cap`, so no captions were drafted.
5. **Mixed outputs in a figure cell:** `fig-jrt-category-curves-information` (015e75b6) ends with `info_table.round(3)`. Its embed will render the figure plus a 22-row table. Author option: move the table display to its own labelled cell (for example a `tbl-` label of the author's choosing). Labels were not changed here.
6. **Text that will appear in embeds.** Quarto embeds every output of a cell. The following labelled cells will also show this text, which is not part of the figure or table:
   - stdout: `fig-overview-rater-overlap` (per-rater best-partner overlap list), `fig-overview-rating-distribution` ("Table saved" line plus the category table as text), `fig-overview-degree-distributions`, `tbl-jrt-convergence`, `tbl-jrt-rater-parameters`, `fig-jrt-rater-parameters`, `fig-jrt-traceplots`, `fig-jrt-ppc`, `tbl-jrt-equal-discrimination-loo`, `fig-jrt-category-curves-information`, `fig-jrt-information-reliability`, `tbl-jrt-score-precision`, `tbl-jrt-derived-counts`.
   - stderr: `fig-jrt-ppc` ("Sampling: [y_obs]"); `tbl-jrt-equal-discrimination-loo` (NUTS sampler progress lines and the Pareto-k UserWarning, twice).
   - Author option: put the display in a separate final cell, or use cell options such as `#| warning: false` in the notebook.
7. **Requested artifacts without their own embeddable object:**
   - `overview_krippendorff_alpha` and `overview_category_frequencies`: print-only (Section 2).
   - The posterior predictive check tables: saved only. The PPC is embeddable only as `fig-jrt-ppc`.
   - Information by rater: only embeddable inside `fig-jrt-category-curves-information`.
   - `sample_ratings_per_action` = `tbl-overview-ratings-per-action`. Convergence-by-group = `tbl-jrt-convergence`. D-study table = `tbl-jrt-d-study`; D-study figure = `fig-jrt-information-reliability` panel B. PSIS-LOO = `tbl-jrt-equal-discrimination-loo`. Rater caterpillar = `fig-jrt-rater-parameters`. Score precision = `tbl-jrt-score-precision`. Derived counts = `tbl-jrt-derived-counts`.
8. **Cosmetic:** `fig-overview-rater-overlap` has no `_caption.txt` in `results/figures/`, because the cell calls `fig.savefig` directly instead of `save_fig`. The embed is unaffected.
9. **Paths:** all snippets use `../data-analysis/creativity-ratings-psychometrics/notebooks/<nb>.ipynb#<label>` relative to `manuscript/manuscript.qmd`. They resolve: `manuscript/` exists alongside `data-analysis/` under the project root.
