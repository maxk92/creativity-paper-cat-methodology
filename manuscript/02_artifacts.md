# 02_artifacts.md: Object inventory (Phase 3 re-run, after commit 04aefc5)

Paper type: imrad-apa (Creativity Research Journal). Embed paths are relative to `manuscript/`.
Notebook prefix: `../data-analysis/creativity-ratings-psychometrics/notebooks/`

## Label counts

I counted the `#| label:` lines in each notebook with grep. The counts match the table rows below.

| Notebook | Labels | tbl | fig |
|---|---|---|---|
| 00_data_loading_preprocessing.ipynb | 1 | 1 | 0 |
| 01_data_overview.ipynb | 6 | 2 | 4 |
| 02_jrt_results.ipynb | 36 | 26 | 10 |
| **Total** | **43** | **29** | **14** |

- There is **one new label**, `tbl-overview-rater-response-styles` (NB01). No label was removed or renamed.
- All 43 labels are unique, and every label prefix matches its object type.
- Every labelled cell has a caption, so I did not have to draft any.
- **Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error output.
  - Tables are one Markdown `execute_result`.
  - NB02 figures are one `display_data` (PNG).
  - NB01 figures are one `execute_result` (PNG).
- NB02 has no stderr output in any cell.

## NB00: 00_data_loading_preprocessing.ipynb (unchanged)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 1 | tbl-cleaning-log | tbl | bbcbf730 | 1 / clean | Data cleaning steps with the number of rows before and after each step. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` | @tbl-cleaning-log |

## NB01: 01_data_overview.ipynb (one label added)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 2 | tbl-overview-ratings-per-action | tbl | ovtbl01 | 1 / clean | Number of products by number of ratings received, with the mean and harmonic mean number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-ratings-per-action >}}` | @tbl-overview-ratings-per-action |
| 3 | fig-overview-rater-overlap | fig | ovfig01 | 1 / clean | Number of jointly rated products for each pair of raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-overlap >}}` | @fig-overview-rater-overlap |
| 4 | fig-overview-rating-distribution | fig | ovfig02 | 1 / clean | Frequency of the seven rating categories across all ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rating-distribution >}}` | @fig-overview-rating-distribution |
| 5 | **tbl-overview-rater-response-styles (NEW)** | tbl | ovtbl02 | 1 / clean | Descriptive response styles per rater: number of ratings, mean, median, standard deviation and interquartile range of the ratings, number of categories used (of 7), entropy of the category distribution, and the shares of ratings in the lowest category (1), the highest category (7), the extreme categories (1 or 7) and the middle categories (3 to 5). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-rater-response-styles >}}` | @tbl-overview-rater-response-styles |
| 6 | fig-overview-rater-response-styles | fig | ovfig03 | 1 / clean | Descriptive rater response styles: (A) rater means, (B) rater standard deviations, (C) number of rating categories used, (D) share of extreme (1, 7) versus middle (3-5) categories; point size is proportional to the number of ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-response-styles >}}` | @fig-overview-rater-response-styles |
| 7 | fig-overview-degree-distributions | fig | ovfig04 | 1 / clean | Degree distributions of the bipartite rater-product design: (A) number of raters per product, (B) number of products per rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-degree-distributions >}}` | @fig-overview-degree-distributions |

## NB02: 02_jrt_results.ipynb (main; all cell ids regenerated)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 8 | tbl-design-summary | tbl | 28af567a | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 9 | tbl-excluded-raters | tbl | 118a628a | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 10 | tbl-category-usage | tbl | 08803894 | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 11 | tbl-grm-convergence | tbl | 849e3d5b | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 12 | tbl-grm-rater-parameters | tbl | 82eaadcc | 1 / clean | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 13 | fig-grm-category-response-functions | fig | 81cf428c | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 14 | tbl-grm-rater-fit | tbl | 7770df1a | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X² pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 15 | tbl-grm-q3-flagged | tbl | ec97f9fb | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 16 | tbl-grm-global-fit | tbl | 6629724c | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 17 | fig-grm-rater-information | fig | 0974fb2e | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 18 | fig-grm-information-shares | fig | c6c942e1 | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 19 | tbl-grm-information-summary (caption changed) | tbl | 54f2a9ef | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 20 | tbl-grm-rater-information-ci (caption changed) | tbl | c43a5551 | 1 / clean | Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 21 | fig-grm-panel-information | fig | 006409e7 | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 22 | tbl-grm-reliability-summary | tbl | 9b1a9699 | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 23 | tbl-grm-reliability-ci | tbl | af96509f | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 24 | tbl-grm-reliability-by-n | tbl | 4c835603 | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 25 | fig-grm-rel-post-histogram | fig | f54bf904 | 1 / clean | Distribution of the product-level reliability (1 − PSD²) across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 26 | fig-grm-rel-post-by-n | fig | 9cba007d | 1 / clean | Product-level reliability (1 − PSD²) by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 27 | tbl-grm-reliability-projection | tbl | 6ed27c6c | 1 / clean | Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-projection >}}` | @tbl-grm-reliability-projection |
| 28 | fig-grm-reliability-projection | fig | 21696dce | 1 / clean | Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-projection >}}` | @fig-grm-reliability-projection |
| 29 | fig-grm-rel-post-by-theta | fig | c517e631 | 1 / clean | Product-level reliability (1 − PSD²) by EAP estimate, coloured by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 30 | fig-grm-rel-consistency | fig | 0b6eedd3 | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 31 | tbl-model-fit | tbl | 52299a6b | 1 / clean | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 32 | tbl-lr-tests | tbl | 48b49851 | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 33 | tbl-theta-correlations | tbl | 9f614151 | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). 'M1, sirt default grid' is M1 re-estimated with the default quadrature grid of sirt, as a software check. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 34 | tbl-score-agreement | tbl | 9c290637 | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 35 | tbl-raw-mean-vs-grm | tbl | eb1111f4 | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 36 | fig-raw-mean-vs-theta | fig | 813b9af4 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 37 | tbl-sensitivity-rater-exclusion | tbl | e46ff49c | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 38 | tbl-discrimination-m3 | tbl | 293a100e | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 39 | tbl-threshold-order | tbl | 2ea683db | 1 / clean | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 40 | tbl-rater-fit-m1 | tbl | db3fa7b1 | 1 / clean | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 41 | tbl-marginal-reliability-models | tbl | 392a5197 | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 42 | tbl-naive-indices | tbl | dc02d388 | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 43 | tbl-reliability-overview | tbl | 93e117eb | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

---

## Changes since previous inventory (commit 0411801, 42 labels → 43)

- **New label:** `tbl-overview-rater-response-styles` (NB01, cell ovtbl02). It is a per-rater response-style table placed directly above fig-overview-rater-response-styles.
  - Its headers: Rater, Ratings by rater, Mean, Median, SD, IQR, Categories used, Entropy, Share lowest (1), Share highest (7), Share extreme (1, 7), Share middle (3-5).
  - It has a caption, one Markdown output and no stream output.
- **No label was removed or renamed.** Every label the manuscript cites still exists.
- **NB02 cell ids were regenerated again.** None of the previous NB02 ids remain. Embeds use labels, so nothing breaks.
  - The unlabelled stdout cells are now 3907a470 (mean Q3 / computable pairs / flagged count) and 86e9fe64 (replications / seed).
  - NB00 is unchanged. NB01's existing ids are unchanged; ovtbl02 was added.
- **Model display values renamed.** `VALUES` now maps the codes to "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)" and "M3 (GPCM)". This affects:
  - row values in tbl-model-fit, tbl-score-agreement, tbl-threshold-order and tbl-marginal-reliability-models;
  - both the rows and the column headers of tbl-theta-correlations.
- **The ratings column is now named by context** (the "Ratings (n)" header is gone):
  - "Ratings by rater": tbl-excluded-raters, tbl-category-usage, tbl-grm-rater-parameters, tbl-grm-rater-fit, tbl-grm-information-summary, tbl-grm-rater-information-ci, tbl-discrimination-m3, tbl-rater-fit-m1 and the new NB01 table.
  - "Ratings per product": tbl-grm-reliability-by-n and tbl-raw-mean-vs-grm. This resolves the old ambiguity item.
  - "Ratings (total)": tbl-grm-convergence.
- **2 captions changed:** tbl-grm-information-summary and tbl-grm-rater-information-ci dropped the sentence "Ratings (n) is the number of ratings the rater gave." The header now explains itself. All other captions are identical.
- **Q3 note:** the markdown cell ef6ed18f now defines computable pairs:
  - at least 3 jointly rated products and residual variance in both raters;
  - other pairs are not computable;
  - the mean Q3 is taken over all computable pairs.

  The stdout line in 3907a470 now reads "Mean Q3 over … computable rater pairs". Neither the note nor the stdout line is part of an embedded object.
- **Manuscript coverage:**
  - 37 of the 43 labels are embedded in `manuscript/manuscript.qmd`: 10 in the main text and 27 in the appendix.
  - All embeds and `@` cross-references resolve.
  - The new label is not embedded and not cross-referenced.
- **Resolved from the previous list:**
  - item 5, the ambiguous "Ratings (n)";
  - the part of item 6 about "M1 (RSM)" vs "M1 (RSM/MFRM)" between tables. It is only partly resolved; see problem 1.

---

## Remaining mechanical problems

1. **Model naming is still inconsistent with the new display values.**
   - tbl-reliability-overview still shows "M1 (RSM)". It is raw CSV text in a multi-word cell, so `pretty_values` skips it.
   - The tbl-threshold-order caption says "M2 (PCM) and M3 (GPCM)".
   - tbl-rater-fit-m1 says "M1 (rating scale model / MFRM)".
   - tbl-model-fit says "M1 rating scale model / MFRM, M2 partial credit model".
   - None of these match "M1 (rating-scale MFRM)" / "M2 (partial-credit MFRM)".
2. **New table not used.** tbl-overview-rater-response-styles is neither embedded nor cross-referenced. It shows the same per-rater response-style statistics as fig-overview-rater-response-styles, which is embedded. Choosing table, figure or both is a writer / author decision.
3. **Mixed integer/decimal display.** The `is_integer()` branch of `fmt_cell` is unchanged. It affects the diagonal of tbl-theta-correlations, Latent variance in tbl-marginal-reliability-models, the GRM Δ row of tbl-model-fit and one `df` in tbl-grm-rater-fit.
4. **Raw code text remains in cells and headers:**
   - tbl-design-summary: "min_ratings_per_rater …" and "duplicate pairs resolved in 00".
   - tbl-grm-reliability-summary: "empirical_marginal_reliability …", "var theta eap", "rel post p10" etc. and "consistency cor rel post rel info".
   - tbl-sensitivity-rater-exclusion: "theta pearson …", "Var(theta)/(…)" and "mirt::marginal_rxx".
   - tbl-reliability-overview: "actual theta_hat", "Var(theta)" and "marginal_rxx".
   - Headers: "marginal_rxx (mirt)" and "Mean/Median rel_post" / "Mean rel_info".
5. **Number formatting is inconsistent.**
   - The Note column of tbl-sensitivity-rater-exclusion and "CI or note" in tbl-reliability-overview have no thousands separators.
   - tbl-sensitivity-rater-exclusion uses `digits=5`.
   - tbl-grm-rater-parameters and the information column of tbl-grm-rater-information-ci use 2 decimals; everything else uses 3.
6. **Caption notation is inconsistent.**
   - tbl-grm-reliability-summary has "rel_post = 1 - PSD^2" (ASCII).
   - tbl-raw-mean-vs-grm says "tau-b" while its header says "τ-b".
   - tbl-design-summary says "product x rater".
   - "bk" has no subscript.
   - fig-grm-rel-consistency uses the code names rel_info and rel_post.
7. **Constant columns and semicolon lists.**
   - tbl-grm-q3-flagged: Overlap is all "–" and Flagged is all True.
   - tbl-threshold-order: Ordered is all False, and Step parameters is semicolon-joined.
   - tbl-category-usage: Internal gap is constant, and Missing categories is semicolon-joined.
   - tbl-design-summary and tbl-sensitivity-rater-exclusion list raters as "R20;R21;R22".
8. **Information shown only in unlabelled stdout cells.** The projection seed (86e9fe64) and the mean Q3 / number of computable pairs (3907a470) are not in any embedded object. The computable-pair definition sits only in markdown cell ef6ed18f.
9. **NB02 notes still sit above the wrong objects (new ids):**
   - 5afe758e ("Full panel") sits above the rater-information-CI block instead of fig-grm-panel-information.
   - a326c3f5 ("Reliability by number of ratings") sits above the reliability-CI block instead of tbl-grm-reliability-by-n.
   - 8307cc03 ("Rater discriminations in M3") sits above tbl-score-agreement.
10. **Figure legibility and table width.**
    - fig-grm-rel-consistency has two opacity levels that the caption does not explain.
    - The 19-colour viridis scale in fig-grm-rater-information / fig-grm-information-shares makes neighbouring raters hard to tell apart.
    - Wide tables: tbl-grm-convergence (14 columns); tbl-category-usage, tbl-grm-information-summary, tbl-model-fit and the new NB01 table (11–12 columns).
11. **Not embedded and not cross-referenced (6):** tbl-cleaning-log, tbl-overview-ratings-per-action, fig-overview-rater-overlap, tbl-overview-rater-response-styles, tbl-grm-global-fit and tbl-marginal-reliability-models. Including them is a writer / author decision.
12. **NB00/NB01 leftovers (unchanged):**
    - tbl-cleaning-log and tbl-overview-ratings-per-action still have snake_case headers and no thousands separators.
    - The label `...-per-action` still uses the "action" wording.
    - UserWarnings remain on stderr in the unlabelled NB00 cells fb9eaf36, 793192b4 and 72468670.
    - Privacy (none of it embedded): the Google Sheet URL in NB00 cell 520638b8, absolute paths containing the username in NB00 stdout, and action UUIDs in unlabelled cells.
