# 02_artifacts.md: Object inventory (Phase 3 re-run, after commit a97e51d)

Paper type: imrad-apa (Creativity Research Journal). Embed paths are relative to `manuscript/`.
Notebook prefix: `../data-analysis/creativity-ratings-psychometrics/notebooks/`

## Label counts

I counted `#| label:` lines in each notebook with grep. The counts match the table rows below.

| Notebook | Labels | tbl | fig |
|---|---|---|---|
| 00_data_loading_preprocessing.ipynb | 1 | 1 | 0 |
| 01_data_overview.ipynb | 5 | 1 | 4 |
| 02_jrt_results.ipynb | 34 | 25 | 9 |
| **Total** | **40** | **27** | **13** |

- All 40 labels are unique across the three notebooks.
- Every label prefix matches its object type.
- Every labelled cell has a caption, so I did not need to draft any.

**Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error.
- Tables are one Markdown `execute_result`.
- NB02 figures are one `display_data` (PNG).
- NB01 figures are one `execute_result` (PNG).
- NB02 now has one stream output, in the unlabelled cell 45a09376 (see Changes).

## NB00: 00_data_loading_preprocessing.ipynb

| # | label | type | cell id | output | caption | embed | xref |
|---|---|---|---|---|---|---|---|
| 1 | tbl-cleaning-log | tbl | bbcbf730 | 1 / clean | Data cleaning steps with the number of rows before and after each step. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` | @tbl-cleaning-log |

## NB01: 01_data_overview.ipynb

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
| 7 | tbl-design-summary | tbl | df7c3ef8 | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 8 | tbl-excluded-raters | tbl | 4ea63630 | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 9 | tbl-category-usage | tbl | 04cfa54c | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 10 | tbl-grm-convergence | tbl | 4e362adc | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 11 | tbl-grm-rater-parameters | tbl | 3a022217 | 1 / clean (but see problem 1) | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k, each with its standard error (_se); category_boundaries states which rating categories each threshold separates. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 12 | fig-grm-category-response-functions | fig | 03bdead3 | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 13 | tbl-grm-rater-fit | tbl | 384472bb | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X2 pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 14 | tbl-grm-q3-flagged | tbl | e9f26568 | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 15 | tbl-grm-global-fit (changed) | tbl | ad703efe | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 16 | fig-grm-rater-information (changed) | fig | 4e14d399 | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 17 | fig-grm-information-shares (changed) | fig | 3f898de6 | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 18 | tbl-grm-information-summary | tbl | 2f813fa2 | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected theta). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 19 | tbl-grm-rater-information-ci | tbl | 576aa9dd | 1 / clean | Average information per rating (info_weighted_area) and share of the full-panel information for each rater, with 95% intervals from parameter draws. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 20 | fig-grm-panel-information | fig | 8d439457 | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 21 | tbl-grm-reliability-summary | tbl | 5a310d42 | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 22 | tbl-grm-reliability-ci | tbl | a64b92ff | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 23 | tbl-grm-reliability-by-n | tbl | 34f1c2e9 | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 24 | fig-grm-rel-post-histogram | fig | 3a59d7aa | 1 / clean | Distribution of the product-level reliability rel_post across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 25 | fig-grm-rel-post-by-n | fig | 65b7803c | 1 / clean | Product-level reliability rel_post by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 26 | fig-grm-rel-post-by-theta | fig | d6abb0c2 | 1 / clean | Product-level reliability rel_post by EAP estimate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 27 | fig-grm-rel-consistency | fig | 4a02b519 | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 - PSD^2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 28 | tbl-model-fit | tbl | 8e90c3cf | 1 / clean | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 29 | tbl-lr-tests | tbl | 03634f53 | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 30 | tbl-theta-correlations | tbl | 13de7e91 | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 31 | tbl-score-agreement | tbl | 01cbb81c | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 32 | tbl-raw-mean-vs-grm (NEW) | tbl | 05caf58b | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: correlations, absolute shift in percentile rank (0-1 scale), share of products changing quintile, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 33 | fig-raw-mean-vs-theta (NEW) | fig | 908bda73 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 34 | tbl-sensitivity-rater-exclusion | tbl | 2d575a27 | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 35 | tbl-discrimination-m3 | tbl | ccd54c69 | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 36 | tbl-threshold-order | tbl | bb004476 | 1 / clean | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 37 | tbl-rater-fit-m1 | tbl | 1a76176f | 1 / clean | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 38 | tbl-marginal-reliability-models | tbl | 779e727a | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 39 | tbl-naive-indices (changed) | tbl | f657f9a9 | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 40 | tbl-reliability-overview | tbl | bd97e06a | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

---

## Changes since previous inventory (commit 8a93d0f, 38 labels → 40)

- **New labels (2), both present and executed:**
  - **tbl-raw-mean-vs-grm** (05caf58b): 11 columns. It has an overall row plus one row per ratings group (1, 2, 3+).
  - **fig-raw-mean-vs-theta** (908bda73): three facets (1 / 2 / 3+ ratings).
- **tbl-grm-global-fit:** the raw R error is gone. The table now has the columns statistic, computable, rater_pairs, rater_pairs_without_overlap and note, and the note states the C2 cause (rater pairs that share no products). It still reports no C2 statistic. That is by design and is now explained.
- **tbl-naive-indices:** now has `n_boot` and `n_boot_failed` columns (8 columns in total). The markdown cell 07c0e468 explains n_boot_failed.
- **Two-column legends:**
  - fig-grm-rater-information and fig-grm-information-shares now have two-column "Rater" legends.
  - The legend title "Rater" is no longer clipped. **Resolved.**
- **NB01:**
  - All three captions now say "products". So does the figure axis text: "Jointly rated products", "Raters per product", "Number of products", "Products per rater", "Rated products".
  - tbl-overview-ratings-per-action now shows integers without decimals. **Resolved.**
  - The unlabelled response-styles output (fb6df84b) is rounded to 3 decimals. Its integer columns still print as `520.0` etc. in the plain DataFrame repr. It is not embedded, so this is harmless.
- **NB02 cell ids were all regenerated.** None of the 32 previous NB02 cell ids remain; the new ids are in the table above. Embeds use labels, not ids, so nothing breaks. NB00 and NB01 cell ids are unchanged.
- **New stream output in NB02:** the unlabelled cell 45a09376 prints the mean Q3 and the number of flagged pairs. The markdown above tbl-grm-q3-flagged (b055ec99) says this value is "printed below the table". It is not part of any embeddable object.

---

## Remaining mechanical problems

### 1. Display (NEW, high priority): unescaped pipes inside a table cell
- **tbl-grm-rater-parameters**, column `category_boundaries`: the values are of the form `1|2;2|3;…`. The `|` characters are not escaped in the Markdown pipe table, so Pandoc/Quarto will split or truncate this column when rendering.
- Fix upstream: escape them as `\|` in `tidy()`, or use another separator such as `1/2` or `1–2`.
- The previous inventory did not flag this.

### 2. Display: formatting (all still open unless marked)
**Mixed integer/decimal display from the integer check:**
- tbl-grm-rater-fit: one `df_S_X2` value has no decimals.
- tbl-theta-correlations: the diagonal shows `1` while near-1 cells show `1.000`.
- tbl-marginal-reliability-models: `latent_variance` mixes `1` and 3-decimal values.
- tbl-model-fit: the GRM delta row shows `0`.

**Other formatting issues:**
- **tbl-grm-convergence:** `tol` renders as `0.000`, so the value is lost.
- **tbl-sensitivity-rater-exclusion:** uses `digits=5`, while every other table uses 3 decimals. This is intentional in the code, but it is inconsistent across tables.

**Empty or constant columns:**
- tbl-grm-q3-flagged: `overlap_flag` is all `–` and `flag_q3` is constant.
- tbl-threshold-order: `ordered` is constant False because of the filter, and `steps` is a raw semicolon-joined string.
- tbl-category-usage: `internal_gap` is constant.

### 3. Captions vs. content
- **tbl-raw-mean-vs-grm:** the caption says "by number of ratings per product", but the table also has an overall (`all`) row. The caption should mention it.
- **tbl-naive-indices:** the caption does not mention the columns `n_raters`, `n_products`, `n_boot` or `n_boot_failed`. It also does not say that the pairwise-alpha CI is approximate; the notebook markdown says so, the caption does not.
- **tbl-grm-reliability-ci:** the caption does not mention `n_draws` or `n_draws_rejected`.
- **tbl-theta-correlations:** the `rm_facets_default_grid` row and column are not mentioned in the caption (still open).
- **tbl-lr-tests:** `df_expected_formula` and `df_matches_formula` are not in the caption. The markdown above explains them.
- **fig-grm-rel-consistency:** two opacity levels with no legend, not explained in the caption (still open).
- **fig-grm-rel-post-by-theta:** has a "Ratings" colour legend (1–5+) that the caption does not mention (still open).
- **fig-grm-panel-information:** facet strip titles say "Information I(theta)" with theta spelled out, while the axis uses θ. There are no y-axis labels (still open).
- **Mechanical inconsistency (new):**
  - tbl-reliability-overview (`ci_or_note`) describes the pairwise Cronbach CI as based on the full number of bootstrap replications.
  - tbl-naive-indices now shows a non-zero `n_boot_failed` for that same row.
  - The two tables describe the same interval differently, so the overview note should mention the failed replications.

### 4. Wide tables (column counts)
- tbl-grm-rater-parameters: 17 columns.
- tbl-grm-convergence: 14 columns.
- 11 columns each: tbl-category-usage, tbl-grm-information-summary, tbl-model-fit and **tbl-raw-mean-vs-grm (new)**. The new table also has very long headers, e.g. `share_products_changing_quintile_by_2_or_more` and `mean_theta_range_same_raw_mean`.
- 8 columns each: tbl-score-agreement, tbl-grm-rater-information-ci, tbl-grm-rater-fit and **tbl-naive-indices (now 8)**.
- tbl-theta-correlations: 7 columns.
- One very long text column: tbl-reliability-overview (`ci_or_note`), **tbl-grm-global-fit (`note`, new)** and tbl-sensitivity-rater-exclusion (`note`).

### 5. Terminology
- **Raw names:** NB02 headers and row labels are still raw snake_case (e.g. `info_weighted_area`, `rel_post`, `consistency_cor_rel_post_rel_info`, `duplicate_pairs_resolved_in_00`, `mean_theta_range_same_raw_mean`).
- **Code names in table cells:** `mirt::marginal_rxx` and `Var(theta)/(Var(theta)+mean(PSD^2))` appear in tbl-sensitivity-rater-exclusion and tbl-reliability-overview.
- **Raw names in captions:** rel_post, rel_info, info_weighted_area, b_k, _se, category_boundaries, S-X2, PSD^2, "product x rater".
- **"theta" vs θ:** "theta" is spelled out in captions and headers (`share_at_theta_-2`, "selected theta"), but figures use θ. All of this needs APA relabelling before submission.
- **actions vs products, NB01:** resolved in captions and axis text. The only remaining instance is the label `tbl-overview-ratings-per-action`, which I have not renamed; that is the author's decision. The word "action" also survives in variable names and unlabelled outputs, which are not embedded.
- **actions vs products, NB00:** tbl-cleaning-log still uses `action_id` and "action" in its step descriptions (still open).

### 6. Privacy (no change)
- **Google Sheet URL:** still in NB00 cell 520638b8 (known; the author handles it).
- **Absolute local paths with the username** appear in the NB00 stdout of cells dbc48755, 283330ea, 722729d7 and dd37b3ec. These cells are not embedded.
- **Action UUIDs and timestamps** appear in unlabelled cells: NB00 793192b4, 72468670 and dd37b3ec; NB01 f6039400. Not embedded.
- **Pseudonyms only:** R20–R22 appear in tbl-excluded-raters, tbl-design-summary and tbl-sensitivity-rater-exclusion. The removed-rater list in tbl-reliability-overview also contains only pseudonyms.
- No original IDs or pseudonym key are printed anywhere.

### 7. Duplicated content between objects
- **tbl-raw-mean-vs-grm and fig-raw-mean-vs-theta (new):** the figure shows the same comparison; the notebook's own note says so.
  - The table's layout matches tbl-score-agreement (the same correlation, shift and quintile columns).
  - Its product counts per ratings group repeat tbl-overview-ratings-per-action and tbl-grm-reliability-by-n.
- **Still present:**
  - tbl-design-summary vs tbl-overview-ratings-per-action (heavy overlap).
  - The excluded-rater list appears in 3 tables.
  - tbl-grm-information-summary vs tbl-grm-rater-information-ci.
  - Four reliability tables overlap: summary, ci, overview and marginal-reliability-models.
  - tbl-grm-reliability-by-n vs fig-grm-rel-post-by-n.
  - tbl-grm-convergence vs the GRM row of tbl-model-fit.
  - tbl-theta-correlations vs tbl-score-agreement.
  - The unlabelled NB01 figure in cell 3b12b8bf vs fig-overview-degree-distributions (harmless, not embedded).

### 8. Other
- **The manuscript still embeds a notebook that does not exist (still open, a blocker for rendering).** `manuscript/manuscript.qmd` embeds `02d_judge_response_theory.ipynb#…` at lines 177–322. That notebook is not in `notebooks/`.
  - Dead cross-references: @tbl-jrt-convergence, @fig-jrt-traceplots, @fig-jrt-ppc, @tbl-jrt-model-summary, @tbl-jrt-derived-counts, @fig-jrt-rater-parameters, @tbl-jrt-rater-parameters, @tbl-jrt-equal-discrimination-loo, @fig-jrt-category-curves-information, @tbl-jrt-score-precision, @fig-jrt-information-reliability, @tbl-jrt-d-study.
  - Only the NB00 and NB01 references resolve.
  - None of the 34 NB02 labels is referenced yet. This needs a manuscript-writer pass.
- **NB02 notes sit above the wrong objects (still open; affects only how the notebook reads):**
  - 85552663 ("Full panel") sits above the rater-information-CI block instead of fig-grm-panel-information.
  - 7e22d705 ("Reliability by number of ratings") sits above the reliability-CI block instead of tbl-grm-reliability-by-n.
  - d3d7cec4 ("Rater discriminations in M3") sits above tbl-score-agreement. tbl-discrimination-m3 now follows tbl-sensitivity-rater-exclusion with no note of its own.
- **fig-grm-rater-information / fig-grm-information-shares:** the legend is fixed, but the 19-colour viridis scale still makes neighbouring raters hard to tell apart (e.g. the R10–R13 shades).
- **NB01 figures:** embedded at 110 dpi; the 200-dpi copies exist only in `results/figures/` (still open).
- **NB00:** the intro markdown (64b27fc9, 73ef4dcd) still refers to `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd` (still open).
- **NB00 stderr:** UserWarnings in cells fb9eaf36, 793192b4 and 72468670. These cells are not labelled, so the embedded table is clean.
