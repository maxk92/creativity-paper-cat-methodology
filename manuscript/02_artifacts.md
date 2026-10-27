# 02_artifacts.md: Object inventory (Phase 3 re-run, after commit 0411801)

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

- The label set is the same as in the previous inventory. **No label was added, removed or renamed.**
- All 42 labels are unique, and every label prefix matches its object type.
- Every labelled cell has a caption, so I did not have to draft any.
- **Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error output.
  - Tables are one Markdown `execute_result`.
  - NB02 figures are one `display_data` (PNG).
  - NB01 figures are one `execute_result` (PNG).
- NB02 now has no stderr output in any cell.

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

## NB02: 02_jrt_results.ipynb (main; all cell ids regenerated)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 7 | tbl-design-summary | tbl | 475838c2 | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 8 | tbl-excluded-raters | tbl | 1475b88b | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 9 | tbl-category-usage | tbl | ff66593c | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 10 | tbl-grm-convergence | tbl | 47b97fbe | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 11 | tbl-grm-rater-parameters (caption changed) | tbl | 3b9d3f35 | 1 / clean | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 12 | fig-grm-category-response-functions | fig | fe48d532 | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 13 | tbl-grm-rater-fit (caption changed) | tbl | 917fee86 | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X² pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 14 | tbl-grm-q3-flagged | tbl | 7bb634a8 | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 15 | tbl-grm-global-fit | tbl | 5fdc553b | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 16 | fig-grm-rater-information | fig | 00420963 | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 17 | fig-grm-information-shares | fig | 1ffe1c91 | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 18 | tbl-grm-information-summary (caption changed) | tbl | 11b00860 | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ). Ratings (n) is the number of ratings the rater gave. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 19 | tbl-grm-rater-information-ci (caption changed) | tbl | 67f02093 | 1 / clean | Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws. Ratings (n) is the number of ratings the rater gave. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 20 | fig-grm-panel-information | fig | bdeadff4 | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 21 | tbl-grm-reliability-summary | tbl | 11c2b168 | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 22 | tbl-grm-reliability-ci (caption changed) | tbl | 83060b39 | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 23 | tbl-grm-reliability-by-n | tbl | 1d4d6b6f | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 24 | fig-grm-rel-post-histogram (caption changed) | fig | 798a494e | 1 / clean | Distribution of the product-level reliability (1 − PSD²) across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 25 | fig-grm-rel-post-by-n (caption changed) | fig | 0d41b887 | 1 / clean | Product-level reliability (1 − PSD²) by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 26 | tbl-grm-reliability-projection (caption changed) | tbl | 5fa6455c | 1 / clean | Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-projection >}}` | @tbl-grm-reliability-projection |
| 27 | fig-grm-reliability-projection | fig | 95d35bde | 1 / clean | Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-projection >}}` | @fig-grm-reliability-projection |
| 28 | fig-grm-rel-post-by-theta (caption changed) | fig | 73767051 | 1 / clean | Product-level reliability (1 − PSD²) by EAP estimate, coloured by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 29 | fig-grm-rel-consistency (caption changed) | fig | 5cfe0ae5 | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 30 | tbl-model-fit | tbl | 92631058 | 1 / clean | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 31 | tbl-lr-tests (caption changed) | tbl | abee45ba | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 32 | tbl-theta-correlations (caption changed) | tbl | e5337bbd | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). 'M1, sirt default grid' is M1 re-estimated with the default quadrature grid of sirt, as a software check. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 33 | tbl-score-agreement | tbl | 3375b00b | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 34 | tbl-raw-mean-vs-grm | tbl | 8006093d | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 35 | fig-raw-mean-vs-theta | fig | 0978db51 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 36 | tbl-sensitivity-rater-exclusion | tbl | 645f0860 | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 37 | tbl-discrimination-m3 | tbl | c971e20c | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 38 | tbl-threshold-order | tbl | 50ad0312 | 1 / clean | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 39 | tbl-rater-fit-m1 | tbl | 72e651dc | 1 / clean | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 40 | tbl-marginal-reliability-models | tbl | 08cda119 | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 41 | tbl-naive-indices (caption changed) | tbl | 688365f2 | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 42 | tbl-reliability-overview | tbl | f3cb7139 | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

---

## Changes since previous inventory (commit 62f7d8e, 42 labels → 42)

- **No label was added, removed or renamed.** Every label the manuscript cites still exists.
- **NB02 cell ids were regenerated again.** None of the previous NB02 ids remain. Embeds use labels, so nothing breaks.
  - The unlabelled stdout cells are now 5e8e7334 (mean Q3 / number flagged) and 71be63e4 (replications / seed; was 671c94b4).
  - NB00 and NB01 are unchanged: same ids, captions and outputs.
- **13 captions changed (all in NB02):**
  - tbl-grm-rater-parameters: "b_k" became "b1 to b6 (bk ...)".
  - tbl-grm-rater-fit: "S-X2" became "S-X²".
  - tbl-grm-information-summary: "theta" became "values of θ". It also gained the sentence defining "Ratings (n)".
  - tbl-grm-rater-information-ci: the code name "(info_weighted_area)" is gone. The caption now names the integration over θ ~ N(0, 1), states the number of accepted draws and defines "Ratings (n)".
  - tbl-grm-reliability-ci: now explains accepted and rejected draws, which covers the Draws and Draws rejected columns.
  - fig-grm-rel-post-histogram and fig-grm-rel-post-by-n: "rel_post" became "(1 − PSD²)".
  - tbl-grm-reliability-projection: now names the 95% range, the replications and products per replication, and the mean product-level reliability column.
  - fig-grm-rel-post-by-theta: "rel_post" became "(1 − PSD²)". It now mentions the colouring by number of ratings.
  - fig-grm-rel-consistency: "1 - PSD^2" became "1 − PSD²". rel_info and rel_post are still named.
  - tbl-lr-tests: now explains "df if all categories used".
  - tbl-theta-correlations: now explains the "M1, sirt default grid" row and column.
  - tbl-naive-indices: now states the replication count and explains Failed replications and the approximate pairwise CI.
- **Changes to displayed values (formatting only; no estimates were copied here):**
  - Integer cells in NB02 tables now have thousands separators (`fmt_cell` uses `{:,}` and `{:,.Nf}`).
  - The tiny-value `:g` branch was removed. tbl-score-agreement "Share changing ≥ 2 quintiles" now shows fixed decimals.
  - Model codes are mapped by `VALUES` / `pretty_values()`: "M1 (RSM/MFRM)", "M2 (PCM)", "M3 (GPCM)" and "M1, sirt default grid". Method values are now "Pearson" / "Spearman".
  - Single-token snake_case cell values now show spaces instead of underscores.
  - The header "Ratings" became "Ratings (n)" in all NB02 tables.
  - tbl-reliability-overview: the "CI or note" text for the pairwise Cronbach CI now gives the number of computable replications and says "approximate". It now agrees with Failed replications in tbl-naive-indices.
- **Figures (I checked the PNGs):**
  - fig-grm-panel-information: the strip titles are now parsed ("Information I(θ)", "Reliability I/(I+1)"). The x-axis shows θ and the shared y-axis is labelled "Value".
  - fig-grm-rel-post-by-theta: the legend is now titled "Ratings per product" with levels 1–4 and 5+.
- **SyntaxWarning resolved.** Setup cell e6102738 uses `r"\|"`, and NB02 has no stderr anywhere.
- **Manuscript coverage is unchanged.**
  - 37 of the 42 labels are embedded in `manuscript/manuscript.qmd`.
  - All embeds and `@` cross-references resolve.
- **Resolved items from the previous list:**
  - the escape-sequence warning;
  - the tbl-score-agreement long-value bug;
  - Model and Method code values;
  - the "(info_weighted_area)" caption code name;
  - the caption gaps in tbl-naive-indices, tbl-grm-reliability-ci, tbl-theta-correlations, tbl-lr-tests and tbl-grm-reliability-projection;
  - the Cronbach-CI inconsistency between tbl-reliability-overview and tbl-naive-indices;
  - the fig-grm-rel-post-by-theta legend not being mentioned in the caption;
  - the panel-information strip titles.

---

## Remaining mechanical problems

1. **Mixed integer/decimal display.** The `is_integer()` branch of `fmt_cell` causes all four cases:
   - tbl-theta-correlations: the diagonal shows `1` while near-1 cells show `1.000`.
   - tbl-marginal-reliability-models: Latent variance shows `1` next to 3-decimal values.
   - tbl-model-fit: the GRM Δ row shows `0`.
   - tbl-grm-rater-fit: one `df` value has no decimals.
2. **Raw code text in multi-word cells.** `pretty_values` skips strings that contain a space, so these are untouched:
   - tbl-design-summary: "min_ratings_per_rater (exclusion cut-off)" and "duplicate pairs resolved in 00".
   - tbl-grm-reliability-summary: "empirical_marginal_reliability (primary; ...)", "model_based_marginal_reliability_mirt/_grid", "var theta eap", "rel post p10" and "consistency cor rel post rel info".
   - tbl-sensitivity-rater-exclusion: Quantity values such as "theta pearson common products"; the Note contains "Var(theta)/(...)" and "mirt::marginal_rxx".
   - tbl-reliability-overview: "actual theta_hat", "Var(theta)/(...)" and "mirt::marginal_rxx".
   - the header "marginal_rxx (mirt)".
3. **Missing thousands separators in free-text cells.** The Note column of tbl-sensitivity-rater-exclusion and "CI or note" in tbl-reliability-overview have none. `fmt_cell` only formats numeric cells.
4. **Inconsistent decimals.**
   - tbl-sensitivity-rater-exclusion still uses `digits=5`.
   - tbl-grm-rater-parameters and the information column of tbl-grm-rater-information-ci use 2 decimals.
   - Everything else uses 3.
5. **Ambiguous "Ratings (n)".** In the rater tables it means ratings given per rater. In tbl-grm-reliability-by-n and tbl-raw-mean-vs-grm it means ratings received per product, and neither caption defines it. tbl-raw-mean-vs-grm also does not name its Products column.
6. **Caption notation is inconsistent.**
   - tbl-grm-reliability-summary still has "rel_post = 1 - PSD^2" (ASCII), while other captions use "1 − PSD²".
   - fig-grm-rel-consistency and the table headers "Mean/Median rel_post" and "Mean rel_info" use code names.
   - tbl-raw-mean-vs-grm says "tau-b" while its header says "τ-b".
   - tbl-design-summary says "product x rater".
   - "bk" has no subscript.
   - tbl-reliability-overview uses "M1 (RSM)" while other tables use "M1 (RSM/MFRM)".
7. **Constant columns and semicolon lists.**
   - tbl-grm-q3-flagged: Overlap is all "–" and Flagged is all True.
   - tbl-threshold-order: Ordered is all False, and Step parameters is a semicolon-joined string.
   - tbl-category-usage: Internal gap is constant, and Missing categories is semicolon-joined.
   - tbl-design-summary and tbl-sensitivity-rater-exclusion list raters as "R20;R21;R22".
8. **fig-grm-rel-consistency** has two opacity levels and no legend, and the caption does not explain them. **fig-grm-rater-information / fig-grm-information-shares:** the 19-colour viridis scale makes neighbouring raters hard to tell apart.
9. **Seed not embedded.** The projection seed is printed only in the unlabelled stdout cell 71be63e4, so it is not in any embedded object.
10. **NB02 notes still sit above the wrong objects:**
    - 710bd8d0 ("Full panel") sits above the rater-information-CI block instead of fig-grm-panel-information.
    - e321b693 ("Reliability by number of ratings") sits above the reliability-CI block instead of tbl-grm-reliability-by-n.
    - 43b1e0b3 ("Rater discriminations in M3") sits above tbl-score-agreement.
11. **Wide tables:**
    - tbl-grm-convergence has 14 columns.
    - tbl-category-usage, tbl-grm-information-summary and tbl-model-fit have 11 each.
    - There are long text columns in tbl-reliability-overview, tbl-grm-global-fit and tbl-sensitivity-rater-exclusion.
12. **Duplicated content between objects:**
    - tbl- and fig-grm-reliability-projection;
    - tbl-grm-reliability-by-n and fig-grm-rel-post-by-n;
    - tbl-raw-mean-vs-grm and fig-raw-mean-vs-theta;
    - tbl-grm-information-summary and tbl-grm-rater-information-ci;
    - four overlapping reliability tables;
    - tbl-theta-correlations and tbl-score-agreement;
    - tbl-grm-convergence and the GRM row of tbl-model-fit.
13. **Not embedded and not cross-referenced (5):** tbl-cleaning-log, tbl-overview-ratings-per-action, fig-overview-rater-overlap, tbl-grm-global-fit and tbl-marginal-reliability-models. Including them is a writer / author decision.
14. **NB00/NB01 were not touched by the display fixes:**
    - tbl-cleaning-log and tbl-overview-ratings-per-action still have snake_case headers and values, with no thousands separators.
    - tbl-overview-ratings-per-action is a quantity/value list.
    - The label `...-per-action` and the "action" wording remain. Renaming is the author's decision.
    - NB01 figures are embedded at 110 dpi.
    - The NB00 intro markdown (64b27fc9, 73ef4dcd) still refers to `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd`.
    - UserWarnings remain on stderr in the unlabelled NB00 cells fb9eaf36, 793192b4 and 72468670.
15. **Privacy (no change):**
    - The Google Sheet URL is in NB00 cell 520638b8.
    - Absolute paths containing the username appear in NB00 stdout.
    - Action UUIDs appear in unlabelled NB00 and NB01 cells.
    - None of these are embedded. Embedded tables show only the pseudonyms R01–R22.
