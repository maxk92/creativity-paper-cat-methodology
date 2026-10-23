# 02_artifacts.md: Embeddable objects (results-embedder, Phase 3)

Paper type: imrad-apa (Creativity Research Journal). Manuscript location: `manuscript/manuscript.qmd`. All embed paths below are relative to `manuscript/`.

Notebooks inventoried:
- N0 = `../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- N1 = `../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb`
- N2 = `../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb` (main)

There are 39 labelled objects: N0 has 1, N1 has 5 and N2 has 33. Every label prefix matches its object type. Tables give `text/markdown` output and figures give `image/png`. No label is duplicated within a notebook or across notebooks. Each labelled cell stores exactly one output, so none has stdout or stderr that could leak into an embed. Captions are the authors' existing `fig-cap`/`tbl-cap` text, and I did not need to draft any.

## A. Privacy issue: fix before any render (does not affect embeds directly)
Two cells print the original, non-pseudonymised rater IDs from `data/raw/rater_pseudonym_key.csv` into stored outputs:
- N2 cell `ad422588` (unlabelled). It merges the pseudonym key into the rater information summary, and its output lists `original_rater_id` for R01–R19.
- N1 cell `b1510393` (unlabelled). It prints the `to_orig` dictionary R01–R22 → original IDs.

N1 cell `0036cba5` and N2 cell `5479a668` load the key but print nothing. N0 says these IDs "are derived from personal data" and the key file is "gitignored and never published", yet both notebooks are tracked by git and currently modified. These cells are not embedded. Still, the stored outputs are in the `.ipynb` files, and Quarto's manuscript project can publish notebook previews that include them. I recommend deleting the cells or clearing their outputs before committing or rendering. This is the author's decision.

## B. Artifact table

### Main notebook N2 (post-exclusion R pipeline outputs)

| label | type | notebook / cell id | output stored | caption draft (existing cap) | embed snippet | cross-ref |
|---|---|---|---|---|---|---|
| tbl-design-summary | tbl | N2 / 6139f51b | yes (markdown) | Data basis shared by all models: ratings, products, raters, coverage of the product x rater matrix and connectivity of the design. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-design-summary >}}` | @tbl-design-summary |
| tbl-excluded-raters | tbl | N2 / 3ecd1ea9 | yes | Raters excluded from all analyses because they gave fewer than 15 ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-excluded-raters >}}` | @tbl-excluded-raters |
| tbl-category-usage | tbl | N2 / ad41df98 | yes | Category use per rater (counts of ratings 1-7). Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-category-usage >}}` | @tbl-category-usage |
| tbl-grm-convergence | tbl | N2 / ddcec9c7 | yes | Estimation and convergence of the graded response model (marginal maximum likelihood, EM algorithm, fixed quadrature). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-convergence >}}` | @tbl-grm-convergence |
| tbl-grm-rater-parameters | tbl | N2 / 0864d752 | yes | Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k with standard errors; category_boundaries states which rating categories each threshold separates. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-parameters >}}` | @tbl-grm-rater-parameters |
| fig-grm-category-response-functions | fig | N2 / 7f6b17ca | yes (png) | Category response functions of the graded response model for each rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-category-response-functions >}}` | @fig-grm-category-response-functions |
| tbl-grm-rater-fit | tbl | N2 / bcf04132 | yes | Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X2 pooled over multiple imputations of the missing ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-rater-fit >}}` | @tbl-grm-rater-fit |
| tbl-grm-q3-flagged | tbl | N2 / 13829fea | yes | Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-q3-flagged >}}` | @tbl-grm-q3-flagged |
| tbl-grm-global-fit | tbl | N2 / 1092b747 | yes, but holds an error message (see C3) | Limited-information absolute fit of the graded response model (C2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-global-fit >}}` | @tbl-grm-global-fit |
| fig-grm-rater-information | fig | N2 / b591d2c9 | yes (png) | Rater information functions of the graded response model. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rater-information >}}` | @fig-grm-rater-information |
| fig-grm-information-shares | fig | N2 / f37bccfe | yes (png) | Share of each rater in the information of the full panel across the latent continuum. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-information-shares >}}` | @fig-grm-information-shares |
| tbl-grm-information-summary | tbl | N2 / 024656ba | yes | Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected theta). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-information-summary >}}` | @tbl-grm-information-summary |
| fig-grm-panel-information | fig | N2 / 2415165a | yes (png) | Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-panel-information >}}` | @fig-grm-panel-information |
| tbl-grm-reliability-summary | tbl | N2 / 1c039bcd | yes | Reliability of the GRM scores: empirical marginal reliability of the actual EAP scores (primary), model-based marginal reliability of the hypothetical full panel, distribution of the product-level reliability rel_post = 1 - PSD^2, and its agreement with the information-based rel_info. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-summary >}}` | @tbl-grm-reliability-summary |
| tbl-grm-reliability-by-n | tbl | N2 / f242573e | yes | Product-level reliability and posterior SD by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-grm-reliability-by-n >}}` | @tbl-grm-reliability-by-n |
| fig-grm-rel-post-histogram | fig | N2 / 609dce88 | yes (png) | Distribution of the product-level reliability rel_post across all products. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-histogram >}}` | @fig-grm-rel-post-histogram |
| fig-grm-rel-post-by-n | fig | N2 / e64833fa | yes (png) | Product-level reliability rel_post by number of ratings per product. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-n >}}` | @fig-grm-rel-post-by-n |
| fig-grm-rel-post-by-theta | fig | N2 / fa9b0260 | yes (png) | Product-level reliability rel_post by EAP estimate. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-post-by-theta >}}` | @fig-grm-rel-post-by-theta |
| fig-grm-rel-consistency | fig | N2 / 52fbd3a5 | yes (png) | Agreement of the two product-level reliability indices: rel_info (information of the product's own raters at the EAP estimate) and rel_post (1 - PSD^2). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#fig-grm-rel-consistency >}}` | @fig-grm-rel-consistency |
| tbl-model-fit | tbl | N2 / 290e7399 | yes | Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters and information criteria. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-model-fit >}}` | @tbl-model-fit |
| tbl-lr-tests | tbl | N2 / e783ceee | yes | Likelihood-ratio tests within the adjacent-category ladder. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-lr-tests >}}` | @tbl-lr-tests |
| tbl-theta-correlations | tbl | N2 / 2be45de3 | yes | Correlations of the EAP estimates between models (Pearson and Spearman). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-theta-correlations >}}` | @tbl-theta-correlations |
| tbl-discrimination-m3 | tbl | N2 / 3a2c335e | yes | Rater discriminations in the generalized partial credit model (M3). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-discrimination-m3 >}}` | @tbl-discrimination-m3 |
| tbl-threshold-order | tbl | N2 / fa64bb53 | yes | Raters with unordered step parameters in M2 (PCM) and M3 (GPCM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-threshold-order >}}` | @tbl-threshold-order |
| tbl-rater-fit-m1 | tbl | N2 / 769b0edd | yes | Rater infit and outfit mean squares under M1 (rating scale model / MFRM). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-rater-fit-m1 >}}` | @tbl-rater-fit-m1 |
| tbl-marginal-reliability-models | tbl | N2 / 672f8fa4 | yes | Marginal and empirical reliability by model, for comparison. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-marginal-reliability-models >}}` | @tbl-marginal-reliability-models |
| tbl-naive-indices | tbl | N2 / 0cd6dfa8 | yes | Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings, 95% bootstrap CI over products). | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-naive-indices >}}` | @tbl-naive-indices |
| tbl-reliability-overview | tbl | N2 / 87f4e2ec | yes | Overview of the reliability and agreement indices and what each refers to. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb#tbl-reliability-overview >}}` | @tbl-reliability-overview |

### Notebook N1: descriptive overview (PRE-EXCLUSION data, see C1)

| label | type | notebook / cell id | output stored | caption draft (existing cap) | embed snippet | cross-ref |
|---|---|---|---|---|---|---|
| tbl-overview-ratings-per-action | tbl | N1 / ovtbl01 | yes (markdown) | Number of actions by number of ratings received, with the mean and harmonic mean number of ratings per action. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-ratings-per-action >}}` | @tbl-overview-ratings-per-action |
| fig-overview-rater-overlap | fig | N1 / ovfig01 | yes (png) | Number of jointly rated actions for each pair of raters. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-overlap >}}` | @fig-overview-rater-overlap |
| fig-overview-rating-distribution | fig | N1 / ovfig02 | yes (png) | Frequency of the seven rating categories across all ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rating-distribution >}}` | @fig-overview-rating-distribution |
| fig-overview-rater-response-styles | fig | N1 / ovfig03 | yes (png) | Descriptive rater response styles: (A) rater means, (B) rater standard deviations, (C) number of rating categories used, (D) share of extreme (1, 7) versus middle (3-5) categories; point size is proportional to the number of ratings. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-rater-response-styles >}}` | @fig-overview-rater-response-styles |
| fig-overview-degree-distributions | fig | N1 / ovfig04 | yes (png) | Degree distributions of the bipartite rater-action design: (A) number of raters per action, (B) number of actions per rater. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#fig-overview-degree-distributions >}}` | @fig-overview-degree-distributions |

### Notebook N0: preprocessing

| label | type | notebook / cell id | output stored | caption draft (existing cap) | embed snippet | cross-ref |
|---|---|---|---|---|---|---|
| tbl-cleaning-log | tbl | N0 / bbcbf730 | yes (markdown) | Data cleaning steps with the number of rows before and after each step. | `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb#tbl-cleaning-log >}}` | @tbl-cleaning-log |

## C. Problems for the user

C1. N1 objects use pre-exclusion data and still include R20, R21 and R22.
N1 reads `data/processed/ratings_long_clean.csv`, which N0 writes before the rater exclusion. The exclusion happens only in the R pipeline. N1's stored stdout reports 22 raters, a rating total and an action total that do not match the final 7,820 / 3,668 / 19. Its rater tables and overlap lists explicitly contain R20–R22. All 5 labelled N1 objects are affected:
- `fig-overview-rater-overlap`: the heatmap axes come from all raters in `df`, so this figure includes R20–R22.
- `fig-overview-rating-distribution`: built from all pre-exclusion ratings.
- `fig-overview-rater-response-styles`: built from `rater_desc`, which has rows for R20–R22.
- `fig-overview-degree-distributions`: pre-exclusion rater and action degrees.
- `tbl-overview-ratings-per-action`: pre-exclusion counts, and its n_raters is 22.

Do not embed these as-is next to the N2 objects. Either filter N1 to the 19 retained raters, or use the R design outputs instead (`results/data/design_summary*.csv`, `rater_overlap.csv`, `category_usage.csv`). The R outputs are already partly embedded via `tbl-design-summary` and `tbl-category-usage`.

C2. `tbl-cleaning-log` (N0) ends before the rater exclusion. Its final row count is the pre-exclusion total, so it does not reach the final 7,820. The rater-exclusion step is documented only in `tbl-excluded-raters` and `tbl-design-summary` (N2). If both tables appear, the manuscript should bridge them, or a rater-exclusion row should be added to the log. The N0 intro markdown also still refers to deleted notebooks (`02a`–`02d`, `03`, `02_creativity_ratings_R.qmd`). This is not embedded.

C3. `tbl-grm-global-fit` contains an R error string rather than a statistic. The stored output is one row: statistic "C2", note "Not computable: missing value where TRUE/FALSE needed". As it stands, embedding it would put a raw R error message into the manuscript. Either fix it in the pipeline or leave it out and mention it in the text.

C4. Formatting problems that will show up in embedded tables (cosmetic, not data):
- Literal `nan` cells: `tbl-category-usage` (missing_categories), `tbl-grm-rater-parameters` (b6 for raters with fewer thresholds), `tbl-grm-q3-flagged` (overlap_flag column, apparently all `nan`), `tbl-marginal-reliability-models` (marginal_rxx_mirt).
- The global `floatfmt=".3f"` turns integer columns into floats: in `tbl-grm-reliability-by-n` the n_ratings and n_products columns show as "1.000", "897.000" and so on; in `tbl-model-fit`, npar shows as "25.000" and so on.
- `tbl-design-summary` includes a `raters_excluded` row with the value "R20;R21;R22". This is intended and is the only N2 table, apart from `tbl-excluded-raters`, that names the excluded raters.
- Column headers are raw snake_case or R names (e.g. `info_weighted_area`, `S_X2`, `share_at_theta_+0`, `rm_facets_default_grid`, `M1_RSM`). APA tables will need display names.
- Some tables are very wide for a portrait APA page: `tbl-grm-convergence` (14 columns), `tbl-grm-rater-parameters` (12), `tbl-category-usage` (11), `tbl-grm-information-summary` (11).
- `tbl-theta-correlations` has an extra `rm_facets_default_grid` column, which is a software-check model and not one of M1–M3/GRM. The caption does not mention it.
- `tbl-overview-ratings-per-action`: the caption does not match the content. The table is a quantity/value list that also includes n_ratings, n_raters and per-rater min/median/max. It is not just "actions by number of ratings".

C5. Figure rendering (N2).
`show_png` reloads the R-generated PNGs into matplotlib with `imshow` at the default figure dpi. The embedded image is therefore a resampled raster, lower in resolution than the source (the source CRF PNG is 3300x2700). The R PNGs also have an in-figure title (e.g. "GRM category response functions per rater", "Share of each rater in the full-panel information"), which duplicates the Quarto caption and is non-APA. I spot-checked two source PNGs (`results/grm/figures/grm_category_response_functions.png`, `grm_rater_information_shares.png`): both show only R01–R19. I could not check the images stored inside the notebook outputs directly. They come from the same files and the notebook was re-executed after the exclusion run.

C6. Unlabelled but potentially important objects:
- N2 `ad422588`: the raw DataFrame merge of the pseudonym key with the rater information summary. It duplicates `tbl-grm-information-summary` and exposes original IDs (see A). Delete it; do not label it.
- N1 `3b12b8bf`: an unlabelled two-panel figure (ratings per action, ratings per rater) plus long stdout. It overlaps `fig-overview-degree-distributions` and is pre-exclusion.
- N1 `bacf60d8` (connected-component table) and `fb6df84b` (full rater descriptive statistics table): unlabelled and pre-exclusion. The post-exclusion connectivity is in `tbl-design-summary`.
- Duplicated content within N2 (not duplicated labels): `fig-grm-rel-post-by-n` and `tbl-grm-reliability-by-n` show the same information, as the notebook itself notes. `tbl-naive-indices` and `tbl-reliability-overview` repeat the same index values. `tbl-marginal-reliability-models` overlaps `tbl-grm-reliability-summary` for the GRM. The outline-architect should choose one of each pair for the main text.
- Some R outputs are not shown in any notebook cell: `grm/rater_parameters_slope_intercept.csv`, `grm/reliability_consistency_largest_differences.csv`, `comparison/rater_parameters_by_model.csv`, `comparison/discrimination_summary.csv`, `comparison/software_crosscheck.csv`, `comparison/mfrm_equivalence.md`, `naive/cronbach_crossed_blocks.csv`. Add a labelled cell to N2 if any of them is needed.

C7. Terminology differs between notebooks. N0, N1 and their labels and captions say "actions"; N2 says "products". Captions should be harmonised before embedding (author's decision; I did not rename any labels).

C8. No labels are malformed or duplicated, and every label resolved. The old Bayesian-notebook artifacts were not reused.
