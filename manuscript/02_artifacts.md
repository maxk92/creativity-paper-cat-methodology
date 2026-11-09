# 02_artifacts.md: Object inventory (Phase 3 re-run, revision run 2026-11-09)

Phase 3 re-run, revision run 2026-11-09 (new data: 9,046 ratings / 3,669 products / 24 raters; data freeze commit 33c08f9, notebook extension commit 45e49ac).

Paper type: imrad-apa (Creativity Research Journal). Embed paths are relative to `manuscript/`.
Notebook prefix: `../data-analysis/creativity-ratings-psychometrics/notebooks/`

Sources inventoried (and nothing else): `00_data_loading_preprocessing.ipynb`, `01_data_overview.ipynb`, `02_jrt_results.ipynb`. Not used: `01_data_overview_new_ratings.ipynb`, `data/archive_pre_rerun_20261103/`, `reports/jrt_results_summary.qmd`.

## Label counts

I counted the `#| label: (tbl|fig)-` lines in each notebook with grep. The counts match the expected 1 / 6 / 45 and the table rows below.

| Notebook | Labels | tbl | fig |
|---|---|---|---|
| 00_data_loading_preprocessing.ipynb | 1 | 1 | 0 |
| 01_data_overview.ipynb | 6 | 2 | 4 |
| 02_jrt_results.ipynb | 45 | 29 | 16 |
| **Total** | **52** | **32** | **20** |

- **9 new labels**, all in NB02 (marked NEW below): fig-design-ratings-per-product, fig-category-usage-shares, fig-grm-rater-discrimination-ci, fig-grm-rater-information-ci, tbl-grm-reliability-min-ratings, tbl-grm-reliability-observed-vs-simulated, fig-grm-reliability-observed-vs-simulated, fig-m1-rater-severity, tbl-rater-overview.
- All 43 labels of the previous inventory still exist. **No label was removed or renamed.**
- All 52 labels are unique, and every label prefix matches its object type.
- Every labelled cell has a caption, so I did not have to draft any.
- **Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error output.
  - Tables are one Markdown `execute_result`.
  - NB02 figures are one `display_data` (PNG + `<Figure size …>` text/plain).
  - NB01 figures are one `execute_result` (PNG).
- No labelled cell in any of the three notebooks has stream output, a warning or an error string.

## NB00: 00_data_loading_preprocessing.ipynb (unchanged)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 1 | tbl-cleaning-log | tbl | bbcbf730 | 1 / clean | Data cleaning steps with the number of rows before and after each step. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` | @tbl-cleaning-log |

## NB01: 01_data_overview.ipynb (unchanged labels, re-run on new data)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 2 | tbl-overview-ratings-per-action | tbl | ovtbl01 | 1 / clean | Number of products by number of ratings received, with the mean and harmonic mean number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-ratings-per-action >}}` | @tbl-overview-ratings-per-action |
| 3 | fig-overview-rater-overlap | fig | ovfig01 | 1 / clean | Number of jointly rated products for each pair of raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-overlap >}}` | @fig-overview-rater-overlap |
| 4 | fig-overview-rating-distribution | fig | ovfig02 | 1 / clean | Frequency of the seven rating categories across all ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rating-distribution >}}` | @fig-overview-rating-distribution |
| 5 | tbl-overview-rater-response-styles | tbl | ovtbl02 | 1 / clean | Descriptive response styles per rater: number of ratings, mean, median, standard deviation and interquartile range of the ratings, number of categories used (of 7), entropy of the category distribution, and the shares of ratings in the lowest category (1), the highest category (7), the extreme categories (1 or 7) and the middle categories (3 to 5). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-rater-response-styles >}}` | @tbl-overview-rater-response-styles |
| 6 | fig-overview-rater-response-styles | fig | ovfig03 | 1 / clean | Descriptive rater response styles: (A) rater means, (B) rater standard deviations, (C) number of rating categories used, (D) share of extreme (1, 7) versus middle (3-5) categories; point size is proportional to the number of ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-response-styles >}}` | @fig-overview-rater-response-styles |
| 7 | fig-overview-degree-distributions | fig | ovfig04 | 1 / clean | Degree distributions of the bipartite rater-product design: (A) number of raters per product, (B) number of products per rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-degree-distributions >}}` | @fig-overview-degree-distributions |

## NB02: 02_jrt_results.ipynb (main; 9 labels added; all cell ids regenerated)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 8 | tbl-design-summary | tbl | c37b4a38 | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 9 | **fig-design-ratings-per-product (NEW)** | fig | e14aa571 | 1 / clean | Number of products by number of ratings received. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-design-ratings-per-product >}}` | @fig-design-ratings-per-product |
| 10 | tbl-excluded-raters | tbl | 43fb15c3 | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 11 | tbl-category-usage | tbl | 49d9be87 | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 12 | **fig-category-usage-shares (NEW)** | fig | c39bf61e | 1 / clean | Share of each rater's ratings in each of the 7 categories, sorted by the rater's mean rating; n = number of ratings; ✕ = category never used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-category-usage-shares >}}` | @fig-category-usage-shares |
| 13 | tbl-grm-convergence | tbl | d2a66a75 | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 14 | tbl-grm-rater-parameters | tbl | 2dd874d8 | 1 / clean | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 15 | **fig-grm-rater-discrimination-ci (NEW)** | fig | 053aebab | 1 / clean | Discrimination a per rater in the graded response model with 95% intervals (estimate ± 1.96 SE), sorted by a. Dashed line: median. Under the Rasch-family models M1 and M2 all raters share one value. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-discrimination-ci >}}` | @fig-grm-rater-discrimination-ci |
| 16 | fig-grm-category-response-functions | fig | 6ad574ba | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 17 | tbl-grm-rater-fit | tbl | f2cf3d5c | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X² pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 18 | tbl-grm-q3-flagged | tbl | e1768cfb | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 19 | tbl-grm-global-fit | tbl | 895cb79a | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 20 | fig-grm-rater-information | fig | bff96842 | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 21 | fig-grm-information-shares | fig | 347ba06c | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 22 | tbl-grm-information-summary | tbl | 31b650f2 | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 23 | tbl-grm-rater-information-ci | tbl | bedab482 | 1 / clean | Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 24 | **fig-grm-rater-information-ci (NEW)** | fig | f2df62dc | 1 / clean | Average information per rating (information integrated over θ ~ N(0, 1)) for each rater with 95% intervals from 200 accepted parameter draws, sorted by information. Point size is proportional to the square root of the rater's number of ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information-ci >}}` | @fig-grm-rater-information-ci |
| 25 | fig-grm-panel-information | fig | 715f5154 | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 26 | tbl-grm-reliability-summary | tbl | 59a029f6 | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 27 | tbl-grm-reliability-ci | tbl | 9cd2a054 | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 28 | tbl-grm-reliability-by-n | tbl | 657292d8 | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 29 | fig-grm-rel-post-histogram | fig | 25a35b26 | 1 / clean | Distribution of the product-level reliability (1 − PSD²) across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 30 | fig-grm-rel-post-by-n | fig | cf6ef810 | 1 / clean | Product-level reliability (1 − PSD²) by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 31 | tbl-grm-reliability-projection | tbl | b7cae78d | 1 / clean | Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-projection >}}` | @tbl-grm-reliability-projection |
| 32 | fig-grm-reliability-projection | fig | 4f64ac77 | 1 / clean | Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-projection >}}` | @fig-grm-reliability-projection |
| 33 | **tbl-grm-reliability-min-ratings (NEW)** | tbl | 26c01033 | 1 / clean | Simulated reliability of the actual design (check) and of the actual design topped up so that every product has at least 4 ratings: empirical marginal reliability with its 95% range over 50 replications, mean product-level reliability (1 − PSD²), and the number of products topped up and ratings added. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-min-ratings >}}` | @tbl-grm-reliability-min-ratings |
| 34 | **tbl-grm-reliability-observed-vs-simulated (NEW)** | tbl | 00aeab14 | 1 / clean | Reliability by number of ratings per product: observed mean product-level reliability (1 − PSD²) of the actual products, and simulated empirical marginal reliability with its 95% range over 50 replications (projection with randomly drawn raters). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-observed-vs-simulated >}}` | @tbl-grm-reliability-observed-vs-simulated |
| 35 | **fig-grm-reliability-observed-vs-simulated (NEW)** | fig | 7297874b | 1 / clean | Reliability by number of ratings per product. Dots: observed mean product-level reliability (1 − PSD²) of the actual products with that many ratings (dot size = number of products; faded = fewer than 10 products). Line and band: simulated empirical marginal reliability (mean and 95% range over 50 replications) for products that each receive exactly k ratings from k raters drawn at random from the panel with equal probability, with ratings generated and scored by the fitted GRM. Dashed lines: simulated reliability of the actual design topped up to at least 4 ratings per product, and model-based reliability of the hypothetical full panel. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-observed-vs-simulated >}}` | @fig-grm-reliability-observed-vs-simulated |
| 36 | fig-grm-rel-post-by-theta | fig | 1fceb3c7 | 1 / clean | Product-level reliability (1 − PSD²) by EAP estimate, coloured by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 37 | fig-grm-rel-consistency | fig | 40422b1f | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 − PSD²). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 38 | tbl-model-fit (caption changed) | tbl | 36fafae5 | 1 / clean | Fit of the adjacent-category ladder (M1 rating-scale MFRM, M2 partial-credit MFRM, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 39 | tbl-lr-tests | tbl | ebf910f0 | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 40 | tbl-theta-correlations | tbl | 06919dea | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). 'M1, sirt default grid' is M1 re-estimated with the default quadrature grid of sirt, as a software check. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 41 | tbl-score-agreement | tbl | 2071b243 | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 42 | tbl-raw-mean-vs-grm | tbl | 81a153de | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 43 | fig-raw-mean-vs-theta | fig | a45de2f9 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 44 | tbl-sensitivity-rater-exclusion | tbl | d89f7935 | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 45 | tbl-discrimination-m3 | tbl | a5fa5502 | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 46 | tbl-threshold-order (caption changed) | tbl | 276c901a | 1 / clean | Raters with unordered step parameters in M2 (partial-credit MFRM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 47 | tbl-rater-fit-m1 (caption changed) | tbl | fcb695cf | 1 / clean | Rater infit and outfit mean squares under M1 (rating-scale MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 48 | **fig-m1-rater-severity (NEW)** | fig | b55889a1 | 1 / clean | Left: rater severity in M1 (rating-scale MFRM) with 95% intervals (estimate ± 1.96 SE); 0 = average rater, higher = stricter. Right: the rater's raw mean rating (1–7). Raters sorted by severity. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-m1-rater-severity >}}` | @fig-m1-rater-severity |
| 49 | tbl-marginal-reliability-models | tbl | 79072096 | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 50 | tbl-naive-indices | tbl | 301d57ec | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 51 | tbl-reliability-overview | tbl | eee39e77 | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |
| 52 | **tbl-rater-overview (NEW)** | tbl | 55fbc1ec | 1 / clean | Rater overview sorted by severity: number of ratings, raw mean rating, severity in M1 (rating-scale MFRM), discrimination a in the GRM, share of the full-panel information with 95% interval, GRM infit and outfit mean squares (⚑ = flagged), and categories never used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-overview >}}` | @tbl-rater-overview |

Note on #35: the caption line of fig-grm-reliability-observed-vs-simulated is too long for the grep/read tools to show from the notebook JSON; the text above is taken verbatim from the `fig(...)` call in `notebooks/build_02_jrt_results.py` (line 373), which generates that cell.

---

## What each NEW object displays (from caption, column headers and plotting code only; no values)

- **fig-design-ratings-per-product** (e14aa571): bar chart, x = ratings per product, y = number of products, each bar annotated with its count.
- **fig-category-usage-shares** (c39bf61e): one horizontal stacked bar per rater (y ticks = pseudonymised rater ids, sorted by rater mean rating), segments = share of the rater's ratings in categories 1–7 (viridis colours, legend "Category" below the axes); right-margin text per bar gives n and, where applicable, "✕" followed by the never-used categories.
- **fig-grm-rater-discrimination-ci** (053aebab): dot-and-interval plot, one row per rater sorted by GRM discrimination a; horizontal error bars = ±1.96 SE; vertical dashed line = median a.
- **fig-grm-rater-information-ci** (f2df62dc): dot-and-interval plot, one row per rater sorted by average information per rating; grey horizontal line = 95% interval from parameter draws; point size proportional to the square root of the rater's number of ratings.
- **tbl-grm-reliability-min-ratings** (26c01033): 2 rows (Actual design; At least 4 ratings per product); columns: Design, Products topped up, Ratings added, Ratings (total), Empirical reliability [95% range], Mean rel_post, Replications.
- **tbl-grm-reliability-observed-vs-simulated** (00aeab14): one row per value of k (ratings per product, from 1 up to the observed maximum); columns: Ratings per product (k), Products, Observed mean rel_post, Simulated empirical reliability [95% range]. The simulated column shows "–" for the largest k, beyond the range of the projection.
- **fig-grm-reliability-observed-vs-simulated** (7297874b): x = ratings per product, y = reliability; blue dots = observed mean rel_post per k (size = number of products; faded if fewer than 10 products), orange line with band = simulated empirical reliability and 95% range, two dashed horizontal reference lines (min-4 design; full panel) with in-plot text labels, two dotted horizontal guide lines at conventional reliability levels, legend.
- **fig-m1-rater-severity** (b55889a1): two panels sharing the y axis (raters sorted by severity). Left: M1 severity estimate with ±1.96 SE bars and a vertical reference line at 0; x label "Severity (logits): lenient ← 0 → strict". Right: horizontal bars of the rater's raw mean rating on a 1–7 axis. Points and bars are coloured by the sign of the severity estimate.
- **tbl-rater-overview** (55fbc1ec): one row per analysed rater (24 rows) sorted by severity; columns: Rater, Ratings, Mean rating, Severity (M1), a (GRM), Share of panel information [95% interval], Infit / outfit (GRM) (with ⚑ on flagged raters), Unused categories.

---

## Checks and flags

### Structural checks (all pass)
- **Duplicate labels:** none across the three notebooks.
- **Label/type prefix mismatches:** none. All `tbl-` cells produce a Markdown table (`execute_result`); all `fig-` cells produce a PNG.
- **Missing captions:** none; no DRAFT captions were needed.
- **Multiple outputs / stdout / stderr / warnings / errors in labelled cells:** none. Every labelled cell has exactly one stored output.
- **Stale or empty outputs:** none. NB02 execution counts run 1–50 without gaps and all execution timestamps are from the same run on 2026-11-09; the totals shown in tbl-design-summary, tbl-grm-convergence and tbl-overview-ratings-per-action agree with the stated data freeze (9,046 ratings / 3,669 products / 24 raters). No labelled cell has an empty output list.
- **Rater identifiers:** every rater cell in every labelled table (NB01 ovtbl02; NB02 tbl-excluded-raters, tbl-category-usage, tbl-grm-rater-parameters, tbl-grm-rater-fit, tbl-grm-q3-flagged, tbl-grm-information-summary, tbl-grm-rater-information-ci, tbl-discrimination-m3, tbl-threshold-order, tbl-rater-fit-m1, tbl-rater-overview) uses the pseudonym form R##. The new figure cells take their y-tick labels from the same `rater_id` column of the result CSVs, so they show the same pseudonyms. No original rater identifiers appear in any labelled output. (The pseudonym sequence has gaps; the excluded raters carry pseudonyms outside the analysed range.)
- **Removed or renamed labels since the previous inventory:** none. All 43 previous labels are present with the same spelling.
- **Caption changes since the previous inventory (3):** tbl-model-fit, tbl-threshold-order and tbl-rater-fit-m1 now use the display names "M1 (rating-scale MFRM)" / "M2 (partial-credit MFRM)". All other previous captions are identical.
- **Cell ids:** NB02 ids were regenerated again (none of the previous NB02 ids remain). NB00 (bbcbf730) and NB01 (ovtbl01, ovfig01, ovfig02, ovtbl02, ovfig03, ovfig04) are unchanged. Embeds use labels, so nothing breaks.

### Unlabelled cells with stream output (not embeddable; for information)
- NB02 ccbeaf11: stdout line with the mean Q3 over computable rater pairs and the number of flagged pairs (sits between tbl-grm-q3-flagged and tbl-grm-global-fit).
- NB02 64142953: stdout line with the number of replications, simulated products per k and the seed (sits between fig-grm-reliability-projection and tbl-grm-reliability-min-ratings).
- NB00 fb9eaf36, 793192b4, 72468670: UserWarnings on stderr (cleaning steps); NB00 and NB01 have several unlabelled stdout cells. None of this is part of an embedded object.

### Display issues (list only, not fixed)
1. **snake_case / code names in NB00 and NB01 tables (unchanged from before).** tbl-cleaning-log: headers `step`, `n_rows_before`, `n_rows_after`, `n_rows_affected`, `description`; step values are code names (`drop_action_not_recognized`, `resolve_duplicates`, …) and the description text mentions `action_id/rater_id`; no thousands separators. tbl-overview-ratings-per-action: headers `quantity`/`value`, row labels `n_ratings`, `n_products_3plus_ratings`, `harmonic_mean_ratings_per_product`, …; no thousands separators; the label still uses the "action" wording.
2. **Code names in NB02 headers:** "Mean rel_post", "Median rel_post", "Mean rel_info" (tbl-grm-reliability-by-n); "Mean rel_post" (tbl-grm-reliability-projection, tbl-grm-reliability-min-ratings); "Observed mean rel_post" (tbl-grm-reliability-observed-vs-simulated); "marginal_rxx (mirt)" (tbl-marginal-reliability-models).
3. **Code-like row labels in NB02 quantity tables:** tbl-grm-reliability-summary ("var theta eap", "mean psd squared", "rel post p10", "consistency cor rel post rel info", "products abs diff gt 0.1", …); tbl-sensitivity-rater-exclusion ("theta pearson common products", "a max abs diff common raters", …); tbl-design-summary ("internal coding", "matrix fill", "n components", "duplicate pairs resolved in 00"); tbl-reliability-overview ("GRM: median rel post", "GRM: IQR rel post").
4. **Caption notation:** tbl-grm-reliability-summary writes "rel_post = 1 - PSD^2" in ASCII while other captions use "1 − PSD²"; tbl-raw-mean-vs-grm says "tau-b" while its header says "τ-b"; tbl-design-summary says "product x rater"; "bk", "b1 to b6" have no subscripts (tbl-grm-rater-parameters); fig-grm-rel-consistency uses the code names rel_info and rel_post.
5. **Model naming:** now consistent ("M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)", "GRM") in all table values and in the captions of tbl-model-fit, tbl-threshold-order, tbl-rater-fit-m1, fig-m1-rater-severity and tbl-rater-overview; tbl-reliability-overview no longer shows "M1 (RSM)". Previous problem 1 is resolved. Minor residue: tbl-model-fit's caption spells out "M3 generalized partial credit model" while the table value is "M3 (GPCM)".
6. **Mixed integer/decimal display:** resolved. The diagonal of tbl-theta-correlations, the GRM Δ cells of tbl-model-fit, Latent variance in tbl-marginal-reliability-models and the df column of tbl-grm-rater-fit now all show three decimals.
7. **Number formatting across tables:** tbl-rater-overview uses 2 decimals throughout while the per-topic tables (tbl-grm-rater-fit, tbl-grm-information-summary, …) use 3; its "Ratings" column has no thousands separator while "Ratings by rater" elsewhere does; its "Share of panel information [95% interval]" gives the estimate with a % sign but the interval bounds without; tbl-grm-rater-parameters and the information column of tbl-grm-rater-information-ci use 2 decimals. tbl-grm-convergence shows the tolerance as "10⁻⁴". No scientific-notation p values, NaN, None or inf strings were found in any stored output; p values appear as "< .001" or three decimals.
8. **Inconsistent list separators:** tbl-rater-overview "Unused categories" is comma-joined ("6,7") while tbl-category-usage "Missing categories" is semicolon-joined ("6;7"); tbl-threshold-order "Step parameters" is semicolon-joined.
9. **Constant or boolean columns:** tbl-grm-q3-flagged "Flagged" is all True (the former "Overlap" column is gone; it is now "Shared products"); tbl-threshold-order "Ordered" is all False; tbl-grm-reliability-min-ratings "Replications" and tbl-grm-rater-fit "Imputations" are constant; raw True/False strings appear in tbl-grm-convergence (Converged, Information matrix positive definite), tbl-grm-global-fit (Computable), tbl-lr-tests (df equal), tbl-category-usage (Internal gap; no longer constant, one rater is True), tbl-grm-q3-flagged and tbl-threshold-order.
10. **Dash cells:** tbl-grm-reliability-observed-vs-simulated shows "–" in the simulated column for the largest values of k (the projection stops earlier than the observed maximum); tbl-marginal-reliability-models shows "–" for marginal_rxx under M1 and M2; tbl-grm-rater-parameters uses "–" for thresholds above a rater's highest used category (explained in the caption).
11. **Glyphs in captions and cells:** "✕" (fig-category-usage-shares caption and in-figure text) and "⚑" (tbl-rater-overview caption and cells). Rendering depends on the PDF font; check in the rendered output.
12. **Figure legibility (from captions and plotting code; images not viewed):** fig-grm-category-response-functions is a 24-panel grid (3300×2700 px) with small text when scaled to column width; the single-colour-scale line plots fig-grm-rater-information / fig-grm-information-shares now carry 24 rater lines and are hard to tell apart; fig-category-usage-shares places its 7-entry legend below the axes (`bbox_to_anchor=(.5, -.1)`), which can clip under `tight_layout`; fig-m1-rater-severity colours points and bars by the sign of the severity estimate but the caption does not mention the colours; fig-grm-rel-consistency still has two opacity levels that the caption does not explain; fig-grm-reliability-observed-vs-simulated bakes two numeric labels (min-4 design and full-panel reliability) into the image as text, so these values exist in the figure but the writer must take them from 03_findings.md, not from the picture.
13. **Wide or long tables:** tbl-grm-convergence (14 columns); tbl-overview-rater-response-styles (12); tbl-category-usage, tbl-grm-information-summary, tbl-model-fit (11); tbl-score-agreement, tbl-naive-indices, tbl-rater-overview (8 columns × 24 rows); tbl-grm-reliability-summary (18 quantity rows); tbl-reliability-overview has a long free-text "CI or note" column.
14. **Overlapping objects (writer/author decision, not a defect):** fig-design-ratings-per-product shows the same distribution as tbl-overview-ratings-per-action (NB01) and panel A of fig-overview-degree-distributions; fig-grm-rater-information-ci plots the information column of tbl-grm-rater-information-ci; fig-grm-rater-discrimination-ci plots the a column of tbl-grm-rater-parameters; tbl-grm-reliability-observed-vs-simulated / fig-grm-reliability-observed-vs-simulated combine tbl-grm-reliability-by-n with tbl-grm-reliability-projection; tbl-rater-overview collects columns from tbl-overview-rater-response-styles, tbl-grm-rater-parameters, tbl-grm-rater-information-ci, tbl-grm-rater-fit, tbl-category-usage and the M1 severities (which are otherwise only shown in fig-m1-rater-severity).
15. **Information shown only in unlabelled stdout cells (unchanged):** projection seed (64142953) and the mean Q3 / number of computable pairs (ccbeaf11).

### Manuscript coverage (current manuscript/manuscript.qmd, before the revision pass)
- 38 of the 52 labels are embedded; all existing `{{< embed >}}` paths and `@` cross-references resolve to labels that still exist.
- **Not embedded (14):** the 9 NEW labels, plus tbl-cleaning-log, tbl-overview-ratings-per-action, fig-overview-rater-overlap, tbl-grm-global-fit and tbl-marginal-reliability-models. Whether to include them is a writer/author decision.

---

## Delta 2026-11-09 (commit 164c146): one new label, note fixes

Mechanical delta against the inventory above. Only NB02 changed. NB00 and NB01 were not re-inventoried (their label counts were re-confirmed by grep).

### Label counts (re-confirmed with grep `#\| label: (tbl|fig)-`)

| Notebook | Labels | tbl | fig |
|---|---|---|---|
| 00_data_loading_preprocessing.ipynb | 1 | 1 | 0 |
| 01_data_overview.ipynb | 6 | 2 | 4 |
| 02_jrt_results.ipynb | 46 | 30 | 16 |
| **Total** | **53** | **33** | **20** |

Counts match the expected 1 / 6 / 46 = 53. All 53 labels are unique; every label prefix matches its object type (the new `tbl-` cell emits a Markdown table).

### New row (insert after #45 tbl-discrimination-m3; renumber #46–#52 to #47–#53)

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 46 | **tbl-discrimination-summary (NEW)** | tbl | 5ef7276b | 1 / clean | Spread of the rater discriminations in M3 (GPCM): minimum, quartiles, median, maximum, ratio of the largest to the smallest discrimination, and standard deviation across raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-summary >}}` | @tbl-discrimination-summary |

What it displays (headers and row labels only, no values): a two-column table, header `Statistic | Value`, seven rows labelled `min`, `q1`, `median`, `q3`, `max`, `ratio max min`, `sd`; source `comparison/discrimination_summary.csv` via `show_table(...)`. One `execute_result` (text/markdown), no stdout/stderr/error. Execution timestamp 2026-11-09 (same run as the rest of NB02). It sits between tbl-discrimination-m3 (67fca3da) and tbl-threshold-order (912f094e).

### Change report for the 45 previous NB02 labels

- **Removed or renamed labels: none.** All 45 previous labels are present with the same spelling, in the same order.
- **Caption changes: 1.** tbl-rater-overview (row #52, now #53): the parenthesis changed from "(⚑ = flagged)" to "(⚑ = infit or outfit outside 0.7–1.3)". New caption verbatim: "Rater overview sorted by severity: number of ratings, raw mean rating, severity in M1 (rating-scale MFRM), discrimination a in the GRM, share of the full-panel information with 95% interval, GRM infit and outfit mean squares (⚑ = infit or outfit outside 0.7–1.3), and categories never used." All other 44 captions are byte-identical to the inventory (the long caption of fig-grm-reliability-observed-vs-simulated was checked in three pieces and is unchanged).
- **Cell ids: all 46 NB02 ids were regenerated again** (the notebook is rebuilt by `build_02_jrt_results.py`). None of the ids in the NB02 table above remain valid. Embeds use labels, so nothing breaks, but the cell-id column should be replaced as follows (old → new):

| label | old id | new id |
|---|---|---|
| tbl-design-summary | c37b4a38 | 8bef5ef1 |
| fig-design-ratings-per-product | e14aa571 | 1feae083 |
| tbl-excluded-raters | 43fb15c3 | f04b368b |
| tbl-category-usage | 49d9be87 | b8206201 |
| fig-category-usage-shares | c39bf61e | 9b3e9c87 |
| tbl-grm-convergence | d2a66a75 | 41214c12 |
| tbl-grm-rater-parameters | 2dd874d8 | dcf2dbe7 |
| fig-grm-rater-discrimination-ci | 053aebab | 975c4bd2 |
| fig-grm-category-response-functions | 6ad574ba | df44e2f1 |
| tbl-grm-rater-fit | f2cf3d5c | 23a684b4 |
| tbl-grm-q3-flagged | e1768cfb | 4e107cd2 |
| tbl-grm-global-fit | 895cb79a | d871f2cb |
| fig-grm-rater-information | bff96842 | ea3647da |
| fig-grm-information-shares | 347ba06c | 4a8621d4 |
| tbl-grm-information-summary | 31b650f2 | b12adc7f |
| tbl-grm-rater-information-ci | bedab482 | 9114a074 |
| fig-grm-rater-information-ci | f2df62dc | 12b424bb |
| fig-grm-panel-information | 715f5154 | c595bfe9 |
| tbl-grm-reliability-summary | 59a029f6 | cc359438 |
| tbl-grm-reliability-ci | 9cd2a054 | a230cacd |
| tbl-grm-reliability-by-n | 657292d8 | 2c343131 |
| fig-grm-rel-post-histogram | 25a35b26 | 31ca2a8d |
| fig-grm-rel-post-by-n | cf6ef810 | 2e4eaed0 |
| tbl-grm-reliability-projection | b7cae78d | 4021099f |
| fig-grm-reliability-projection | 4f64ac77 | 01e757f0 |
| tbl-grm-reliability-min-ratings | 26c01033 | 4d41e2d0 |
| tbl-grm-reliability-observed-vs-simulated | 00aeab14 | 7ffb7f06 |
| fig-grm-reliability-observed-vs-simulated | 7297874b | 8428c02b |
| fig-grm-rel-post-by-theta | 1fceb3c7 | 218e8c8d |
| fig-grm-rel-consistency | 40422b1f | 00d5d5e0 |
| tbl-model-fit | 36fafae5 | 6b99df62 |
| tbl-lr-tests | ebf910f0 | fcbab35d |
| tbl-theta-correlations | 06919dea | 15a36a9a |
| tbl-score-agreement | 2071b243 | c94bf286 |
| tbl-raw-mean-vs-grm | 81a153de | 25978c27 |
| fig-raw-mean-vs-theta | a45de2f9 | c0fd0f97 |
| tbl-sensitivity-rater-exclusion | d89f7935 | adbcdb13 |
| tbl-discrimination-m3 | a5fa5502 | 67fca3da |
| tbl-discrimination-summary (NEW) | – | 5ef7276b |
| tbl-threshold-order | 276c901a | 912f094e |
| tbl-rater-fit-m1 | fcb695cf | b315c83a |
| fig-m1-rater-severity | b55889a1 | 470979b6 |
| tbl-marginal-reliability-models | 79072096 | 5eb903e3 |
| tbl-naive-indices | 301d57ec | 68159a62 |
| tbl-reliability-overview | eee39e77 | e5c791df |
| tbl-rater-overview | 55fbc1ec | bd1ee008 |

(Ids were assigned by taking, for each `#| label:` line, the `"id"` key of the enclosing cell; the new cell was verified directly.) The ids quoted in "What each NEW object displays" and "Checks and flags" above are likewise stale and map per this table.

### Unlabelled cells with stream output in NB02 (not embeddable; for information)

NB02 now has three stdout cells and no stderr, warning or error output in any cell:

- **c7a7fe2a** (was 64142953): now two printed lines. Line 1 (unchanged content): number of replications, simulated products per k, seed. Line 2 (NEW): the smallest k at which the simulated empirical reliability reaches at least .80. Position: directly after fig-grm-reliability-projection (01e757f0), before the markdown cell and tbl-grm-reliability-min-ratings (4d41e2d0), i.e. after the projection figure rather than immediately after the projection table.
- **411ec44f** (NEW cell): one printed line giving the range of the M1 severities: lowest and highest estimate, each with its SE and rater pseudonym, and the span in logits. Position: directly after fig-m1-rater-severity (470979b6), before the markdown cell 60050d5a and tbl-marginal-reliability-models (5eb903e3).
- **30b8685b** (was ccbeaf11): unchanged content (mean Q3 over computable pairs and number of flagged pairs), between tbl-grm-q3-flagged (4e107cd2) and tbl-grm-global-fit (d871f2cb).

As before, these values exist only in stdout; the writer must take them from 03_findings.md.

### Flag rule (⚑) now stated in the notebook texts

- **Rater-fit note, markdown cell 38b48261** (directly before tbl-grm-rater-fit, 23a684b4): now states that the flags in the rater-fit output (`flag_infit`, `flag_outfit`; R/02_grm.R) mark values outside 0.7–1.3, that with this design they mostly mark values below 0.7, and that no further cut-offs are applied in the notebook.
- **Rater-overview note, markdown cell d321faa3** (directly before tbl-rater-overview): "⚑ = infit or outfit outside 0.7–1.3, the flag rule of the rater-fit output".
- **tbl-rater-overview caption, code cell bd1ee008**: "⚑ = infit or outfit outside 0.7–1.3" (caption change recorded above). The ⚑ is attached in code from the `flag_infit` / `flag_outfit` columns.

### Additions to the display-issue list (new table only)

- tbl-discrimination-summary uses a generic header (`Statistic | Value`) and code-like row labels (`q1`, `q3`, `ratio max min`, `sd`); same class as display issue 3.
- Overlap (writer/author decision): tbl-discrimination-summary summarises the discrimination column of tbl-discrimination-m3 (and, indirectly, the M3 side of the model comparison); same class as display issue 14.

### Manuscript coverage

`tbl-discrimination-summary` is not yet embedded or cross-referenced anywhere in manuscript/ (0 matches). Coverage is now 38 of 53 labels; the "Not embedded" list grows to 15.

### Status of the rest of the inventory

All other entries of this inventory stand (labels, types, output cleanliness, captions, embed snippets, xrefs, NB00/NB01 ids), with the two exceptions recorded above: the NB02 cell-id column (all 46 regenerated; mapping given) and the caption of tbl-rater-overview.
