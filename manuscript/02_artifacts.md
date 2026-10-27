# 02_artifacts.md: Object inventory (Phase 3 re-run, after commit 62f7d8e)

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

- The set of labels is identical to the previous inventory. **No label was added, removed or renamed.**
- All 42 labels are unique.
- Every label prefix matches its object type.
- Every labelled cell has a caption, so none had to be drafted.
- **Output column.** "1 / clean" means the cell has exactly one stored output and no stdout, stderr or error output.
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
| 7 | tbl-design-summary | tbl | 29e46234 | 1 / clean | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| 8 | tbl-excluded-raters | tbl | 04106685 | 1 / clean | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| 9 | tbl-category-usage | tbl | 6c70958c | 1 / clean | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| 10 | tbl-grm-convergence | tbl | 9b9f3a39 | 1 / clean | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| 11 | tbl-grm-rater-parameters | tbl | ca0fcf9e | 1 / clean | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k (b_k separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| 12 | fig-grm-category-response-functions | fig | 2b952965 | 1 / clean | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| 13 | tbl-grm-rater-fit | tbl | 101a6ef4 | 1 / clean | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X2 pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| 14 | tbl-grm-q3-flagged | tbl | 3ce8db2c | 1 / clean | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| 15 | tbl-grm-global-fit | tbl | 01b5aa3b | 1 / clean | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| 16 | fig-grm-rater-information | fig | 92feb5ec | 1 / clean | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| 17 | fig-grm-information-shares | fig | e8d92949 | 1 / clean | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| 18 | tbl-grm-information-summary | tbl | 1aa54232 | 1 / clean | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected theta). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| 19 | tbl-grm-rater-information-ci (changed: compact) | tbl | f53233fc | 1 / clean | Average information per rating (info_weighted_area) and share of the full-panel information for each rater, with 95% intervals from parameter draws. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-information-ci >}}` | @tbl-grm-rater-information-ci |
| 20 | fig-grm-panel-information | fig | d6dd3f4b | 1 / clean | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| 21 | tbl-grm-reliability-summary | tbl | 3ec42ae8 | 1 / clean | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| 22 | tbl-grm-reliability-ci | tbl | 78c901eb | 1 / clean | Empirical and model-based marginal reliability of the GRM with 95% intervals. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-ci >}}` | @tbl-grm-reliability-ci |
| 23 | tbl-grm-reliability-by-n | tbl | da273cfc | 1 / clean | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| 24 | fig-grm-rel-post-histogram | fig | ed8ce9b2 | 1 / clean | Distribution of the product-level reliability rel_post across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| 25 | fig-grm-rel-post-by-n | fig | 5676a4f5 | 1 / clean | Product-level reliability rel_post by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| 26 | tbl-grm-reliability-projection (changed) | tbl | 50451ca9 | 1 / clean | Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with randomly drawn raters of the panel. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-projection >}}` | @tbl-grm-reliability-projection |
| 27 | fig-grm-reliability-projection (changed) | fig | dc626412 | 1 / clean | Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-reliability-projection >}}` | @fig-grm-reliability-projection |
| 28 | fig-grm-rel-post-by-theta | fig | 62ef7bc2 | 1 / clean | Product-level reliability rel_post by EAP estimate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| 29 | fig-grm-rel-consistency | fig | ddaf9bcb | 1 / clean | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 - PSD^2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| 30 | tbl-model-fit | tbl | 11829625 | 1 / clean | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| 31 | tbl-lr-tests | tbl | 6f450a48 | 1 / clean | Likelihood-ratio tests within the adjacent-category ladder. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| 32 | tbl-theta-correlations | tbl | b3df5651 | 1 / clean | Correlations of the EAP estimates between models (Pearson and Spearman). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| 33 | tbl-score-agreement | tbl | 61aa822d | 1 / clean | Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-score-agreement >}}` | @tbl-score-agreement |
| 34 | tbl-raw-mean-vs-grm (changed) | tbl | a4e2ce6a | 1 / clean | Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-raw-mean-vs-grm >}}` | @tbl-raw-mean-vs-grm |
| 35 | fig-raw-mean-vs-theta | fig | 12200102 | 1 / clean | GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-raw-mean-vs-theta >}}` | @fig-raw-mean-vs-theta |
| 36 | tbl-sensitivity-rater-exclusion | tbl | f64e1585 | 1 / clean | Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-sensitivity-rater-exclusion >}}` | @tbl-sensitivity-rater-exclusion |
| 37 | tbl-discrimination-m3 | tbl | 5c8f4eb4 | 1 / clean | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| 38 | tbl-threshold-order | tbl | 83e56b00 | 1 / clean | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| 39 | tbl-rater-fit-m1 | tbl | b3c28f2d | 1 / clean | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| 40 | tbl-marginal-reliability-models | tbl | e2ac2e25 | 1 / clean | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| 41 | tbl-naive-indices | tbl | f9ba4461 | 1 / clean | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| 42 | tbl-reliability-overview | tbl | 6631fb18 | 1 / clean | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

---

## Changes since previous inventory (commit 91c2e6d, 42 labels → 42)

- **No labels added, removed or renamed.** Every label the manuscript cites still exists.
- **The compact rater-information table keeps its old label, `tbl-grm-rater-information-ci` (cell f53233fc).** There is no new label.
  - It now has 4 columns: Rater, Ratings, "Information per rating [95% interval]" and "Share of panel information [95% interval]".
  - Each cell reads "estimate [low, high]". Information uses 2 decimals and the share uses 3.
  - The caption is unchanged.
- **tbl-grm-reliability-projection (50451ca9):** now 3 columns and one row per k (k = 1–10). It shows randomly drawn raters only.
  - The columns are "Ratings per product (k)", "Empirical reliability [95% range]" (as "estimate [low, high]") and "Mean rel_post".
  - The most- and least-informative schemes and the `true_r2` column are gone.
  - The caption was rewritten to "randomly drawn raters" and now matches the table.
- **fig-grm-reliability-projection (dc626412):** I checked the PNG. It shows a single black line with a grey band and no legend, so random raters only. The caption was updated to match.
- **The replications/seed stdout cell has a new id, 671c94b4** (was 368bd615). It is still unlabelled and not embedded.
- **tbl-raw-mean-vs-grm (a4e2ce6a):** now 6 columns (was 15) and 3 rows (1 / 2 / 3+).
  - The columns are Ratings, Products, Kendall's τ-b, "Share of pairs in reversed order", and "Mean θ̂ range at equal raw mean" / "Maximum θ̂ range at equal raw mean".
  - The overall row is gone.
  - The caption was rewritten and now matches. Products is the only column it does not name.
  - Markdown cell b3a9b483 explains the table.
- **Readable column headers in all NB02 tables.**
  - A `HEADERS` map plus `pretty_headers()` in setup cell b5d0a8de produce headers such as "Rater", "Ratings", "S-X²", "ΔAIC", "Pearson r", "Spearman ρ" and "95% CI lower". Unmapped names only have their underscores replaced by spaces.
  - No snake_case header remains except the deliberate `marginal_rxx (mirt)` and the "rel_post" / "rel_info" headers.
- **NB02 cell ids were regenerated again.** None of the previous NB02 ids remain. Embeds use labels, so nothing breaks. NB00 and NB01 ids and captions are unchanged.
- **Manuscript coverage.**
  - All `@` cross-references and all embeds in `manuscript/manuscript.qmd` resolve to existing labels.
  - 37 of the 42 labels are now embedded (was 35). tbl-grm-reliability-projection and fig-grm-reliability-projection are both embedded and cross-referenced.
- **Resolved:**
  - the old raw-mean caption gaps (the `all` row, the tie-aware columns);
  - the 15-column raw-mean width;
  - mixed formatting in `share_products_with_tied_raw_mean`;
  - the `scheme` value / legend mismatch;
  - the projection caption not naming its measures;
  - the snake_case column headers.

---

## Remaining mechanical problems

1. **Escape sequence (still open).** Setup cell b5d0a8de still stores a `SyntaxWarning: invalid escape sequence '\|'` on stderr.
   - The source is `notebooks/build_02_jrt_results.py` line 52 (`"\\|"`). Fix: write `r"\\|"` or `"\\\\|"` in the generator.
   - The setup cell is not embedded.
2. **New formatting bug in tbl-score-agreement.** In the M3_GPCM row, "Share changing ≥ 2 quintiles" prints a long unrounded value.
   - Cause: the tiny-value `:g` branch in `fmt_cell` (meant for a tolerance) catches any value below 10^-3.
   - Fix: limit that branch to `tol`, or use a fixed number of significant digits.
3. **Mixed integer/decimal display (still open):**
   - tbl-theta-correlations: the diagonal shows `1` while near-1 cells show `1.000`.
   - tbl-marginal-reliability-models: Latent variance mixes `1` with 3-decimal values.
   - tbl-model-fit: the GRM Δ row shows `0`.
   - tbl-grm-rater-fit: `df` has one value with no decimals.
4. **Inconsistent decimals.** tbl-sensitivity-rater-exclusion uses `digits=5`. tbl-grm-rater-parameters and the information column of tbl-grm-rater-information-ci use 2 decimals. Everything else uses 3.
5. **Constant or empty columns:**
   - tbl-grm-q3-flagged: Overlap is all `–` and Flagged is all True.
   - tbl-threshold-order: Ordered is all False, and Step parameters is a semicolon-joined string.
   - tbl-category-usage: Internal gap is constant.
6. **Raw code values in table cells (not headers):**
   - the Quantity column in tbl-design-summary, tbl-grm-reliability-summary and tbl-sensitivity-rater-exclusion;
   - Model values `M1_RSM` / `M2_PCM` / `M3_GPCM`;
   - Method values `pearson` / `spearman`;
   - the auto-generated header "rm facets default grid";
   - `theta_hat`, `Var(theta)/(...)` and `mirt::marginal_rxx` in tbl-reliability-overview.
7. **Ambiguous header "Ratings".** In the rater tables it means ratings given per rater. In tbl-grm-reliability-by-n and tbl-raw-mean-vs-grm it means ratings received per product.
8. **tbl-grm-rater-information-ci caption** still contains the code name "(info_weighted_area)". The header now reads "Information per rating".
9. **tbl-grm-reliability-projection:**
   - The caption does not mention the "Mean rel_post" column or the 95% range in the empirical column.
   - The replication count and seed are printed only in the unlabelled stdout cell 671c94b4, so they are not in any embedded object.
10. **Caption gaps (still open):**
    - tbl-naive-indices: Raters, Products, Bootstrap replications and Failed replications, plus the approximate pairwise CI.
    - tbl-grm-reliability-ci: Draws and Draws rejected.
    - tbl-theta-correlations: the rm-facets-default-grid row and column.
    - tbl-lr-tests: "df if all categories used" and "df equal".
11. **Figure captions (still open):**
    - fig-grm-rel-consistency: two opacity levels with no legend.
    - fig-grm-rel-post-by-theta: the "Ratings" colour legend is not mentioned.
    - fig-grm-panel-information: strip titles spell out "theta" while the axis uses θ, and there are no y-axis labels.
12. **Mechanical inconsistency (still open).** tbl-reliability-overview ("CI or note") describes the pairwise Cronbach CI as "bootstrap, 1000 replications". tbl-naive-indices shows a non-zero "Failed replications" for the same interval.
13. **Raw names in captions:** rel_post, rel_info, b_k, S-X2, PSD^2, "product x rater", and "theta" vs θ. These need APA relabelling.
14. **actions vs products:** the label `tbl-overview-ratings-per-action` and the `action_id` / "action" wording in tbl-cleaning-log are unchanged. Renaming the label is the author's decision.
15. **Wide tables:**
    - tbl-grm-convergence has 14 columns.
    - tbl-category-usage, tbl-grm-information-summary and tbl-model-fit have 11 each.
    - There are long text columns in tbl-reliability-overview, tbl-grm-global-fit and tbl-sensitivity-rater-exclusion.
16. **NB02 notes sit above the wrong objects (still open, new ids):**
    - 6d7075a0 ("Full panel") sits above the rater-information-CI block instead of fig-grm-panel-information.
    - ecf20bc0 ("Reliability by number of ratings") sits above the reliability-CI block instead of tbl-grm-reliability-by-n.
    - 5ed1ef92 ("Rater discriminations in M3") sits above tbl-score-agreement.
17. **Duplicated content between objects:**
    - tbl- and fig-grm-reliability-projection;
    - tbl-grm-reliability-by-n and fig-grm-rel-post-by-n;
    - tbl-raw-mean-vs-grm and fig-raw-mean-vs-theta;
    - tbl-grm-information-summary and tbl-grm-rater-information-ci (both show information per rating and share);
    - four overlapping reliability tables;
    - tbl-theta-correlations and tbl-score-agreement;
    - tbl-grm-convergence and the GRM row of tbl-model-fit.
18. **Not embedded and not cross-referenced (5):** tbl-cleaning-log, tbl-overview-ratings-per-action, fig-overview-rater-overlap, tbl-grm-global-fit and tbl-marginal-reliability-models. Including them is a writer / author decision.
19. **fig-grm-rater-information / fig-grm-information-shares:** the 19-colour viridis scale makes neighbouring raters hard to tell apart.
20. **NB01 figures** are embedded at 110 dpi. The 200-dpi copies exist only in `results/figures/`.
21. **NB00:**
    - The intro markdown (64b27fc9, 73ef4dcd) still refers to `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd`.
    - UserWarnings appear in the unlabelled cells fb9eaf36, 793192b4 and 72468670.
22. **Privacy (no change):**
    - The Google Sheet URL is in NB00 cell 520638b8.
    - Absolute paths containing the username appear in NB00 stdout (dbc48755, 283330ea, 722729d7, dd37b3ec).
    - Action UUIDs appear in unlabelled cells (NB00 793192b4, 72468670, dd37b3ec; NB01 f6039400).
    - None of these are embedded. Embedded tables show only the pseudonyms R01–R22.
