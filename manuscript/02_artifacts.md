# 02_artifacts.md: Object inventory (Phase 3 re-run, after commit 91c2e6d)

Paper type: imrad-apa (Creativity Research Journal). Embed paths are relative to `manuscript/`.
Notebook prefix: `../data-analysis/creativity-ratings-psychometrics/notebooks/`

## Label counts

I counted the `#| label:` lines in each notebook with grep. The counts match the table rows below.

| Notebook | Labels | tbl | fig |
|---|---|---|---|
| 00_data_loading_preprocessing.ipynb | 1 | 1 | 0 |
| 01_data_overview.ipynb | 5 | 1 | 4 |
| 02_jrt_results.ipynb | 36 | 26 | 10 |
| **Total** | **42** | **28** | **14** |

- All 42 labels are unique across the three notebooks.
- Every label prefix matches its object type.
- Every labelled cell has a caption, so I did not need to draft any.

**Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error output.
- Tables are one Markdown `execute_result`.
- NB02 figures are one `display_data` (PNG).
- NB01 figures are one `execute_result` (PNG).

## NB00: 00_data_loading_preprocessing.ipynb (unchanged)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 1 | tbl-cleaning-log | tbl | bbcbf730 | 1 / clean | Data cleaning steps with the number of rows before and after each step. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` | @tbl-cleaning-log |

## NB01: 01_data_overview.ipynb (unchanged)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 2 | tbl-overview-ratings-per-action | tbl | ovtbl01 | 1 / clean | Number of products by number of ratings received, with the mean and harmonic mean number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-ratings-per-action >}}` | @tbl-overview-ratings-per-action |
| 3 | fig-overview-rater-overlap | fig | ovfig01 | 1 / clean | Number of jointly rated products for each pair of raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-overlap >}}` | @fig-overview-rater-overlap |
| 4 | fig-overview-rating-distribution | fig | ovfig02 | 1 / clean | Frequency of the seven rating categories across all ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rating-distribution >}}` | @fig-overview-rating-distribution |
| 5 | fig-overview-rater-response-styles | fig | ovfig03 | 1 / clean | Descriptive rater response styles: (A) rater means, (B) rater standard deviations, (C) number of rating categories used, (D) share of extreme (1, 7) versus middle (3-5) categories; point size is proportional to the number of ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-response-styles >}}` | @fig-overview-rater-response-styles |
| 6 | fig-overview-degree-distributions | fig | ovfig04 | 1 / clean | Degree distributions of the bipartite rater-product design: (A) number of raters per product, (B) number of products per rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-degree-distributions >}}` | @fig-overview-degree-distributions |

## NB02: 02_jrt_results.ipynb (main)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 7 | tbl-design-summary | tbl | 58e32d41 | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 8 | tbl-excluded-raters | tbl | dd078799 | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 9 | tbl-category-usage | tbl | 2483aa59 | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 10 | tbl-grm-convergence | tbl | 3f6972c2 | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 11 | tbl-grm-rater-parameters (changed) | tbl | cfb04715 | 1 / clean | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k (b_k separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 12 | fig-grm-category-response-functions | fig | 7ff3ea30 | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 13 | tbl-grm-rater-fit | tbl | 56dabacd | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X2 pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 14 | tbl-grm-q3-flagged | tbl | 10d62633 | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 15 | tbl-grm-global-fit | tbl | d525daa8 | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 16 | fig-grm-rater-information | fig | 0885cfe1 | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 17 | fig-grm-information-shares | fig | bfd8bc26 | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 18 | tbl-grm-information-summary | tbl | fb982f3a | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected theta). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 19 | tbl-grm-rater-information-ci | tbl | f222f444 | 1 / clean | Average information per rating (info_weighted_area) and share of the full-panel information for each rater, with 95% intervals from parameter draws. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 20 | fig-grm-panel-information | fig | 8f5ffbd6 | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 21 | tbl-grm-reliability-summary | tbl | 05a28f9c | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 22 | tbl-grm-reliability-ci | tbl | 2de37f81 | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 23 | tbl-grm-reliability-by-n | tbl | 69e27411 | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 24 | fig-grm-rel-post-histogram | fig | 0a74217e | 1 / clean | Distribution of the product-level reliability rel_post across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 25 | fig-grm-rel-post-by-n | fig | 2e3801ac | 1 / clean | Product-level reliability rel_post by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 26 | tbl-grm-reliability-projection (NEW) | tbl | 2ea36634 | 1 / clean | Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model, for randomly drawn, the most informative and the least informative raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-projection >}}` | @tbl-grm-reliability-projection |
| 27 | fig-grm-reliability-projection (NEW) | fig | 40072a98 | 1 / clean | Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM. Bands: 2.5% to 97.5% of the replications. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-projection >}}` | @fig-grm-reliability-projection |
| 28 | fig-grm-rel-post-by-theta | fig | 9186727e | 1 / clean | Product-level reliability rel_post by EAP estimate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 29 | fig-grm-rel-consistency | fig | 5d51fe9a | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 - PSD^2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 30 | tbl-model-fit | tbl | 041cba7a | 1 / clean | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 31 | tbl-lr-tests | tbl | b3034a4d | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 32 | tbl-theta-correlations | tbl | 2974492e | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 33 | tbl-score-agreement | tbl | ec338994 | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 34 | tbl-raw-mean-vs-grm (changed) | tbl | ec765a18 | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: correlations, absolute shift in percentile rank (0-1 scale), share of products changing quintile, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 35 | fig-raw-mean-vs-theta | fig | 04843757 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 36 | tbl-sensitivity-rater-exclusion | tbl | 79738d4b | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 37 | tbl-discrimination-m3 | tbl | 91d95b1b | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 38 | tbl-threshold-order | tbl | 7b051cef | 1 / clean | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 39 | tbl-rater-fit-m1 | tbl | 1f422649 | 1 / clean | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 40 | tbl-marginal-reliability-models | tbl | f76232d2 | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 41 | tbl-naive-indices | tbl | ff18cda5 | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 42 | tbl-reliability-overview | tbl | d78d2f68 | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

---

## Changes since previous inventory (commit a97e51d, 40 labels → 42)

- **New labels (2), both present and executed.** They sit between fig-grm-rel-post-by-n and fig-grm-rel-post-by-theta.
  - **tbl-grm-reliability-projection** (2ea36634): 11 columns.
    - `scheme` has three values (random / most_informative / least_informative), with one row per k for each.
    - Three measures, each with q025/q975 columns: `empirical`, `true_r2` and `mean_rel_post`.
    - `n_products_per_rep`, `n_reps` and `seed` are dropped from the table. They are printed instead by the new unlabelled stdout cell 368bd615, which is not embedded.
  - **fig-grm-reliability-projection** (40072a98): plots only the `empirical` measure.
    - It has three coloured lines with ribbons, x = k, and a plain-English bottom legend (Least / Most informative raters, Random raters).
    - The caption matches what is plotted.
- **tbl-raw-mean-vs-grm:** now 15 columns (was 11). The four new tie-aware columns are `share_products_changing_quintile_ties_resolved`, `share_discordant_pairs`, `kendall_tau_b` and `share_products_with_tied_raw_mean`. The markdown cell 8620cb46 explains them. The caption is unchanged.
- **tbl-grm-rater-parameters:** now compact, with 9 columns (was 17): `rater_id`, `n_ratings`, `a`, `b1`–`b6`.
  - Each cell reads "estimate (SE)" with 2 decimals, and a dash marks thresholds that do not exist.
  - `category_boundaries` is gone.
  - The caption was rewritten to match. **Resolved.**
- **Pipe bug: resolved.** I checked every Markdown table row in NB02.
  - No cell contains a `|`, escaped or unescaped.
  - In every table, each row has the same number of cells as its header.
  - `fmt_cell` now escapes `|` in string cells (but see problem 1).
- **NB02 cell ids were regenerated again.** None of the previous NB02 ids remain. Embeds use labels, so nothing breaks. NB00 and NB01 ids and captions are unchanged.
  - The unlabelled Q3 stdout cell is now be50ab41 (was 45a09376).
- **New stderr output in the NB02 setup cell 5001e347:** a SyntaxWarning (see problem 1). This cell is not embedded.
- **The manuscript now uses NB02:**
  - All `02d_judge_response_theory.ipynb` embeds and `@*-jrt-*` cross-references are gone.
  - Every cross-reference and embed in `manuscript/manuscript.qmd` resolves to an existing label. **Previous blocker resolved.**

---

## Remaining mechanical problems

### 1. Code hygiene (NEW, low priority)
- **Invalid escape sequence in the setup cell (5001e347).** The cell's source contains `"\|"`, which triggers a stored `SyntaxWarning: invalid escape sequence '\|'` on stderr.
  - Python currently keeps the backslash, so the escape still works. Future Python versions will turn this into an error.
  - The cause is `notebooks/build_02_jrt_results.py` line 52. Its `"\\|"` is written into the notebook source as `"\|"`.
  - Fix: write `r"\|"` or `"\\\\|"` in the generator.
  - No table currently contains a pipe, so this escape is not exercised by the current outputs.

### 2. Display: formatting
**Still open:**
- **Mixed integer/decimal display:**
  - tbl-grm-rater-fit: one `df_S_X2` value has no decimals.
  - tbl-theta-correlations: the diagonal shows `1` while near-1 cells show `1.000`.
  - tbl-marginal-reliability-models: `latent_variance` mixes `1` with 3-decimal values.
  - tbl-model-fit: the GRM delta row shows `0`.
- **tbl-grm-convergence:** `tol` renders as `0.000`.
- **tbl-sensitivity-rater-exclusion:** uses `digits=5`, while other tables use 3 decimals.
- **Constant or empty columns:**
  - tbl-grm-q3-flagged: `overlap_flag` is all `–` and `flag_q3` is constant.
  - tbl-threshold-order: `ordered` is constant False, and `steps` is a raw semicolon-joined string.
  - tbl-category-usage: `internal_gap` is constant.

**New:**
- tbl-raw-mean-vs-grm: `share_products_with_tied_raw_mean` mixes `1` with 3-decimal values.
- tbl-grm-rater-parameters uses 2 decimals (`est_se(digits=2)`), while the parameter tables tbl-discrimination-m3 and tbl-threshold-order and all other tables use 3 or a different style. This is intentional but inconsistent.

### 3. Captions vs. content
**New or changed:**
- **tbl-raw-mean-vs-grm:**
  - The caption does not mention the overall (`all`) row (still open).
  - It also does not mention the four new tie-aware columns: quintile change with ties resolved, discordant pairs, Kendall's τ-b, and share of products with a tied raw mean.
- **tbl-grm-reliability-projection (new):**
  - The caption does not name the three measures (empirical marginal reliability, squared correlation with true θ, mean rel_post) or the 2.5%/97.5% columns.
  - It does not say that model parameters are treated as known.
  - The number of replications and the seed appear only in the unlabelled stdout cell 368bd615.
- **tbl-grm-rater-parameters:** the caption now matches the table. **Resolved.**

**Still open:**
- tbl-naive-indices: `n_raters`, `n_products`, `n_boot` and `n_boot_failed` are not in the caption, and the caption does not say the pairwise CI is approximate.
- tbl-grm-reliability-ci: `n_draws` and `n_draws_rejected` are not in the caption.
- tbl-theta-correlations: the `rm_facets_default_grid` row and column are not in the caption.
- tbl-lr-tests: `df_expected_formula` and `df_matches_formula` are not in the caption.
- fig-grm-rel-consistency: two opacity levels with no legend.
- fig-grm-rel-post-by-theta: the "Ratings" colour legend is not mentioned in the caption.
- fig-grm-panel-information: strip titles spell out "theta" while the axis uses θ, and there are no y-axis labels.
- **Mechanical inconsistency:** tbl-reliability-overview (`ci_or_note`) describes the pairwise Cronbach CI as based on the full number of bootstrap replications. tbl-naive-indices shows a non-zero `n_boot_failed` for the same interval.

### 4. Wide tables (column counts)
- tbl-raw-mean-vs-grm: now **15 columns** (widest), with very long headers such as `share_products_changing_quintile_ties_resolved`.
- tbl-grm-convergence: 14 columns.
- 11 columns each: tbl-category-usage, tbl-grm-information-summary, tbl-model-fit and **tbl-grm-reliability-projection (new, 30 data rows)**.
- 8 columns each: tbl-score-agreement, tbl-grm-rater-information-ci, tbl-grm-rater-fit and tbl-naive-indices.
- tbl-grm-rater-parameters: now 9 columns (was 17). **Resolved.**
- Long text columns: tbl-reliability-overview (`ci_or_note`), tbl-grm-global-fit (`note`) and tbl-sensitivity-rater-exclusion (`note`).

### 5. Terminology
- **Raw snake_case headers and values remain throughout NB02.**
  - New examples: `true_r2`, `mean_rel_post_q025`, `kendall_tau_b` and `share_discordant_pairs`.
  - The `scheme` values `most_informative` / `least_informative` do not match the figure legend ("Most informative raters", etc.).
- **Code names in table cells:** `mirt::marginal_rxx` and `Var(theta)/(Var(theta)+mean(PSD^2))` appear in tbl-sensitivity-rater-exclusion and tbl-reliability-overview.
- **Raw names in captions:** rel_post, rel_info, info_weighted_area, b_k, S-X2, PSD^2, "product x rater".
- **"theta" vs θ:** "theta" is spelled out in captions and headers, while figures use θ. All of this needs APA relabelling.
- **actions vs products:** the label `tbl-overview-ratings-per-action` is not renamed; that is the author's decision. tbl-cleaning-log still uses `action_id` and "action".

### 6. Privacy (no change)
- **Google Sheet URL:** still in NB00 cell 520638b8. The author handles it.
- **Absolute local paths with the username** appear in the NB00 stdout of cells dbc48755, 283330ea, 722729d7 and dd37b3ec. Not embedded.
- **Action UUIDs and timestamps** appear in unlabelled cells: NB00 793192b4, 72468670 and dd37b3ec; NB01 f6039400. Not embedded.
- **The new NB02 stderr** shows only a `/tmp/ipykernel_…` path, with no username.
- **Only pseudonyms (R01–R22)** appear in embedded tables.

### 7. Duplicated content between objects
- **New:**
  - fig-grm-reliability-projection shows the `empirical` columns of tbl-grm-reliability-projection.
  - The projection pair also sits beside the observed tbl-grm-reliability-by-n / fig-grm-rel-post-by-n, which have a different basis (observed vs simulated).
- **Still present:**
  - tbl-raw-mean-vs-grm vs fig-raw-mean-vs-theta.
  - tbl-design-summary vs tbl-overview-ratings-per-action.
  - The excluded-rater list appears in 3 tables.
  - tbl-grm-information-summary vs tbl-grm-rater-information-ci.
  - Four reliability tables overlap: summary, ci, overview and marginal-reliability-models.
  - tbl-grm-reliability-by-n vs fig-grm-rel-post-by-n.
  - tbl-grm-convergence vs the GRM row of tbl-model-fit.
  - tbl-theta-correlations vs tbl-score-agreement.

### 8. Other
- **Manuscript coverage.**
  - All cross-references resolve.
  - 35 of the 42 labels are embedded. These 7 are neither embedded nor cross-referenced:
    - tbl-cleaning-log
    - tbl-overview-ratings-per-action
    - fig-overview-rater-overlap
    - tbl-grm-global-fit
    - tbl-marginal-reliability-models
    - **tbl-grm-reliability-projection (new)**
    - **fig-grm-reliability-projection (new)**
  - Whether to include them is a manuscript-writer / author decision.
- **NB02 notes sit above the wrong objects (still open, new ids):**
  - 5ef1f60a ("Full panel") sits above the rater-information-CI block instead of fig-grm-panel-information.
  - 8c5abdd7 ("Reliability by number of ratings") sits above the reliability-CI block instead of tbl-grm-reliability-by-n.
  - a47f5ab0 ("Rater discriminations in M3") sits above tbl-score-agreement.
- **fig-grm-rater-information / fig-grm-information-shares:** the 19-colour viridis scale still makes neighbouring raters hard to tell apart.
- **NB01 figures:** embedded at 110 dpi; the 200-dpi copies exist only in `results/figures/` (still open).
- **NB00:** the intro markdown (64b27fc9, 73ef4dcd) still refers to `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd` (still open).
- **NB00 stderr:** UserWarnings in the unlabelled cells fb9eaf36, 793192b4 and 72468670. The embedded table is clean.
