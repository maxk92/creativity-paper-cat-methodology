> **Orchestrator note (2026-10-27, re-run after commit 0411801).** The interpreter's output below is copied byte for byte. 02_artifacts.md was regenerated in parallel (42 labels, unchanged set), so any flag calling it stale is resolved.
> Values listed as removed or NOT IN NOTEBOOK must not be quoted. Bibliography: phd_library.bib is now the single source of citekeys (web_references.bib removed from the manuscript YAML).

# 03_findings.md: Results findings (results-interpreter, Phase 4 re-run after commit 0411801)

## Changes vs previous findings

1. **Values are unchanged.** I compared every printed cell of every N2 table with the previous file, and also N0 `tbl-cleaning-log` and the N1 stdout and tables. Apart from formatting, every value matches. **No real difference was found.** The checked N2 tables are:
   - tbl-design-summary, tbl-excluded-raters, tbl-category-usage;
   - tbl-grm-convergence, tbl-grm-rater-parameters, tbl-grm-rater-fit, tbl-grm-q3-flagged (and the mean-Q3 stdout), tbl-grm-global-fit;
   - tbl-grm-information-summary, tbl-grm-rater-information-ci;
   - tbl-grm-reliability-summary, tbl-grm-reliability-ci, tbl-grm-reliability-by-n, tbl-grm-reliability-projection (and its stdout);
   - tbl-model-fit, tbl-lr-tests, tbl-theta-correlations, tbl-score-agreement, tbl-raw-mean-vs-grm;
   - tbl-sensitivity-rater-exclusion, tbl-discrimination-m3, tbl-threshold-order, tbl-rater-fit-m1;
   - tbl-marginal-reliability-models, tbl-naive-indices, tbl-reliability-overview.
2. **Thousands separators in N2.** These are now in every N2 numeric cell of 1,000 or more. The writer should quote the printed forms:
   - 7,820; 3,668; 1,174; 2,080; 1,900; 2,771; 1,000 (bootstrap replications); 7,844; 3,669;
   - -11,733.227; 23,720.455; 24,508.795; 24,105.251; and every other log-likelihood, AIC, BIC and SABIC value in `tbl-model-fit`.
   - **Exceptions printed without separators** (they are text, or come from N0 or N1): the N1 tables and stdout (for example "7820", "1174"); N0; the `tbl-reliability-overview` notes ("1000 replications", "639 of 1000"); the `tbl-sensitivity-rater-exclusion` notes ("3668 common products"); and the N2 projection stdout ("2000 simulated products").
3. **Readable cell values in N2.**
   - Model labels: "M1 (RSM/MFRM)", "M2 (PCM)", "M3 (GPCM)" and "GRM". In `tbl-threshold-order`: "M2 (PCM)" and "M3 (GPCM)".
   - In `tbl-theta-correlations`, the Method values are "Pearson" and "Spearman". The check column and row are "M1, sirt default grid".
   - In `tbl-reliability-overview`, the row labels now read "M1 (RSM): marginal reliability" and so on.
   - Quantity row labels made of a single code name now print with spaces, for example "n ratings", "ratings per product mean", "var theta eap", "rel post median", "empirical marginal reliability", "theta pearson common products".
   - Labels that already contained a space are unchanged, for example "min_ratings_per_rater (exclusion cut-off)" and "empirical_marginal_reliability (primary; actual scores)".
4. **Header change.** "Ratings" is now "Ratings (n)" in these tables: tbl-excluded-raters, tbl-category-usage, tbl-grm-convergence, tbl-grm-rater-parameters, tbl-grm-rater-fit, tbl-grm-information-summary, tbl-grm-rater-information-ci, tbl-discrimination-m3, tbl-rater-fit-m1, tbl-grm-reliability-by-n and tbl-raw-mean-vs-grm.
   - In the last two tables, "Ratings (n)" is the number of ratings **per product**.
   - In the others, it is the number of ratings **per rater**.
5. **`tbl-grm-convergence`.** Tolerance now prints "10⁻⁴". **"0.0001" and "0.000" are no longer printed.**
6. **`tbl-score-agreement`.** The M3 (GPCM) value of "Share changing ≥ 2 quintiles" now prints "0.001". **"0.000545256" is no longer printed. Do not quote it.** The `%g` rule for small values has been removed from `fmt_cell`.
7. **Captions changed** (verbatim forms are under each finding):
   - tbl-grm-rater-parameters ("b1 to b6 (bk separates …)");
   - tbl-grm-information-summary (adds "Ratings (n) is the number of ratings the rater gave.");
   - tbl-grm-rater-information-ci (no more "info_weighted_area"; now says "200 accepted parameter draws");
   - tbl-grm-reliability-projection (now says "drawn at random (each equally likely)", "50 replications of 2,000 products");
   - tbl-naive-indices (now says "1,000 replications" and "Failed replications"; its CI is approximate);
   - tbl-theta-correlations (now explains "M1, sirt default grid").
8. **`tbl-reliability-overview` note.** The pairwise Cronbach's α note now reads "95% CI [0.891, 0.943] (bootstrap, 639 of 1000 replications computable, approximate); 14 raters; removed: R19;R14;R02;R16;R12". This matches 1,000 − 361 failed in `tbl-naive-indices`. Former Flag 5 is resolved.
9. **Q3 "computable".** No notebook cell says which pairs count as computable. **The expected "at least 3 shared products" is NOT in the notebook.**
   - It appears only in the R pipeline (context, not quotable): `R/02_grm.R` line 21, `Q3_MIN_OVERLAP <- 3L   # below this, a pairwise Q3 is not computed`.
   - Lines 168–170 also require non-zero residual SDs for both raters.
   - The only notebook evidence is the stdout "Mean Q3 over 137 computable rater pairs" and the code `_ok = _q3["q3"].notna()`.
10. **SyntaxWarning gone.** The N2 setup cell (`e6102738`) no longer emits a SyntaxWarning (former Flag 7 item).
11. **All N2 cell ids have changed again.** The new ids are given in each finding. N0 and N1 cell ids and outputs are unchanged. `02_artifacts.md` still lists the old N2 ids (for example `tbl-design-summary` 29e46234, now `475838c2`; projection 50451ca9, now `5fa6455c`) and the old projection caption. The results-embedder should be re-run.
12. **Removed values: still NOT quotable** (carried over from the previous Changes items 2–4 and Flag 13):
    - Projection with most/least-informative raters:
      - most_informative 0.754 (k = 1) to 0.947 (k = 10); least_informative 0.108 (k = 1) to 0.884 (k = 10);
      - all intermediate values (for example .859, .920, .260, .701);
      - all between-scheme comparisons ("most > random > least", "gap narrows with k", "k = 1: 0.754 / 0.508 / 0.108").
    - `true_r2` and its quantiles (for example 0.508 [0.480, 0.542]), and the quantiles of mean_rel_post (for example 0.500, 0.517).
    - Pooled raw-mean "all" row: 3668 as a row, Pearson .906, Spearman .932, mean shift .080, p95 shift .216, max shift .551, share changing quintile .350, ≥ 2 quintiles .022, ties-resolved .237, discordant pairs .083, τ-b .796, tied raw mean .995, mean θ̂ range .814, max θ̂ range 2.252.
    - Raw-mean subgroup columns:
      - Pearson (.921 / .922 / .954) and Spearman (.940 / .933 / .959);
      - percentile shifts (.074 / .075 / .060; .203 / .234 / .177; .334 / .562 / .400);
      - share changing quintile (.385 / .319 / .266) and ≥ 2 quintiles (.004 / .028 / .006);
      - ties-resolved (.104 / .220 / .220); tied raw mean (1 / 1 / .971).
    - 3-decimal rater-information CI bounds (for example [0.410, 11.017], [0.728, 6.489]) and 3-decimal GRM rater parameters (for example 3.709 (2.220)).
    - The sentence "The observed relation above is confounded …"; the phrase "which brackets the effect of who rates"; and "overstates the disagreement and is not comparable with the model comparison above".
    - Tolerance "0.000" or "0.0001", and M3 ≥ 2 quintiles "0.000545256".
    - AUDIT.md's "6 unused end categories" and REPORT.md's infit/outfit range 0.7–1.3.

---

Notebooks (the only quotable sources):
- **N0** = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- **N1** = `.../notebooks/01_data_overview.ipynb`
- **N2** = `.../notebooks/02_jrt_results.ipynb` (main)

How to read this file:
- **Values** are copied exactly as printed.
- **N2 formatting.** N2 tables go through `tidy()` / `fmt_cell`:
  - 3 decimals with thousands separators, except `tbl-sensitivity-rater-exclusion`, which has 5;
  - `tbl-grm-rater-parameters` is formatted by `est_se()` as "estimate (SE)" at 2 decimals;
  - `tbl-grm-rater-information-ci` and `tbl-grm-reliability-projection` are formatted by `est_ci()` as "estimate [low, high]": information at 2 decimals; share and projection at 3;
  - whole numbers have no decimals but do have separators;
  - p-values below .001 are in scientific notation;
  - missing values show as "–".
- **Headers and labels.** N2 headers come from `HEADERS`, and cell labels from `VALUES` / `pretty_values`.
- **N1 formatting.** N1 uses its own `fmt_cell`, without separators. N1 `fb6df84b` prints counts as floats ("520.0").
- **Context files.** AUDIT.md, REPORT.md, ANALYSIS_TODO.md and the R scripts were read for definitions only. Any value that appears only there is marked **NOT IN NOTEBOOK — not quotable**.

**Post-exclusion check.** N1 and N2 both report the final data: 7,820 ratings, 3,668 products and 19 raters.
- N1 `f6039400` stdout: "Loaded 7844 ratings; excluded 24 ratings from 3 raters with fewer than 15 ratings (R20, R21, R22); 7820 ratings remain."
- N1 `981d6824`: Total ratings 7820; Distinct products 3668; Distinct raters 19.
- N2 `tbl-design-summary`: n ratings 7,820; n products 3,668; n raters 19.
- N0 is pre-exclusion, as expected: 22 raters, 7844 rows, 3669 actions.

---

## (a) Descriptives and design

**F0.1 Raw data and cleaning (pre-exclusion, N0)** *(unchanged)*
- **Finding:** The sheet export had 9148 rows. After cleaning, 7844 rows remained, from 22 raters and 3669 actions.
- **Linked object:** `tbl-cleaning-log` (N0, `bbcbf730`). Supporting stdout is in `520638b8`, `fb9eaf36`, `793192b4`, `72468670` and `dd37b3ec`.
- **Numbers:**

  | step | n_rows_before | n_rows_after | n_rows_affected |
  |---|---|---|---|
  | drop_action_not_recognized | 9148 | 7858 | 1290 |
  | drop_missing_id | 7858 | 7858 | 0 |
  | drop_out_of_range | 7858 | 7857 | 1 |
  | drop_missing_rating | 7857 | 7857 | 0 |
  | resolve_duplicates | 7857 | 7844 | 13 |

  Other printed values:
  - The out-of-range row had value 0.0 (rater R04).
  - "Rows with a duplicate (action_id, rater_id) combination: 25". One pair conflicts: R14 gave 2.0 and 1.0. The rule "last entry kept" was applied.
  - Stdout also prints "Raters pseudonymised: 22", "Raters: 22", "Actions: 3669" and "Warnings collected: 3".
- **Caveats:**
  - These are pre-exclusion values.
  - The cleaning log has no rater-exclusion row and stops at 7844.

**F0.2 Rater exclusion** *(values unchanged; new cell ids; header "Ratings (n)")*
- **Finding:** Three raters with fewer than 15 ratings were excluded. Together they gave 24 ratings, and their exclusion dropped 1 product.
- **Linked object:** `tbl-excluded-raters` (N2, `1475b88b`; headers: Rater | Ratings (n) | Reason) and `tbl-design-summary` (N2, `475838c2`; headers: Quantity | Value).
- **Numbers:**
  - Ratings per excluded rater: R20 13, R21 9, R22 2. The reason given for each is "fewer than 15 ratings".
  - From the design summary: min_ratings_per_rater (exclusion cut-off) 15; raters excluded R20;R21;R22; ratings excluded 24; products dropped 1.

**F0.3 Final design** *(values unchanged; new N2 cell id; separators; row labels with spaces)*
- **Finding:** The final design has 7,820 ratings of 3,668 products by 19 raters. It is sparse but forms one connected component.
- **Linked object:** `tbl-design-summary` (N2, `475838c2`). The same numbers appear in `tbl-overview-ratings-per-action` (N1, `ovtbl01`) and in N1 `981d6824` and `bacf60d8`.
- **Numbers (N2, row labels as printed):**
  - n ratings 7,820; n products 3,668; n raters 19.
  - n categories 7; scale 1-7; internal coding "rating - 1 (0-6)".
  - ratings per product: mean 2.132, median 2, min 1, max 10, harmonic mean 1.726.
  - products with 1 rating 897.
  - ratings per rater: min 50, max 1,174.
  - matrix fill 0.112; n components 1.
  - Rater pairs: total 171, without overlap 17, overlap median 13.
  - raters with category gaps 5; raters with internal gap 0.
  - duplicate pairs resolved in 00 12; duplicate pairs conflicting 1.
- **Numbers (N1 `ovtbl01`, without separators):**
  - n_ratings 7820; n_products 3668; n_raters 19.
  - n_products_1_rating 897; n_products_2_ratings 2080; n_products_3plus_ratings 691.
  - share_products_1_rating 0.245; share_products_2_ratings 0.567; share_products_3plus_ratings 0.188.
  - max_ratings_per_product 10; mean_ratings_per_product 2.132; harmonic_mean_ratings_per_product 1.726.
  - median_ratings_per_rater 383; min_ratings_per_rater 50; max_ratings_per_rater 1174.
  - N1 `981d6824`: "Average ratings per product: 2.13"; "Average ratings per rater: 411.6".
  - N1 `bacf60d8`: "Number of connected components: 1"; the component has 3668 products and 19 raters.
- **Notebook statement (`b0b9f66b`):** "A connected design (one component) is required so that all raters and products lie on one scale (Eckes, 2015)."
- **Caveats:** 17 of 171 rater pairs share no product. 897 products have a single rating.

**F0.4 Distribution of ratings per product** *(unchanged)*
- **Finding:** Most products have 2 ratings, and the counts fall off steeply above 2.
- **Linked object:** `fig-overview-degree-distributions` (N1, `ovfig04`). The numbers come from unlabelled N1 `3b12b8bf` (stdout).
- **Numbers:**

  | ratings per product | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | products | 897 | 2080 | 357 | 125 | 125 | 47 | 20 | 11 | 3 | 3 |

  Cumulative counts: 1 or more 3668; 2 or more 2771; 3 or more 691; 4 or more 334; 5 or more 209; 6 or more 84; 7 or more 37; 8 or more 17; 9 or more 6; 10 or more 3.
- **Caveats:** Only 3 products have 9 ratings, and only 3 have 10.

**F0.5 Ratings per rater and pairwise overlap** *(unchanged)*
- **Finding:** Raters gave between 50 and 1174 ratings each. The five raters with the fewest ratings also have the lowest overlap with their best-connected partner.
- **Linked object:** `fig-overview-rater-overlap` (N1, `ovfig01`). The numbers come from unlabelled N1 `3b12b8bf` and `aa371443`.
- **Numbers:**
  - Ratings per rater: R19 50, R16 52, R17 52, R18 55, R15 73, R13 254, R14 259, R12 264, R11 369, R10 383, R09 400, R06 520, R08 522, R07 547, R04 620, R05 633, R03 720, R02 873, R01 1174.
  - Best-partner overlap: R17 44, R18 46, R19 46, R16 52, R15 61, R14 108, R12 145, R09 147, R13 154, R10 157, R05 190, R08 191, R06 240, R02 257, R04 257, R01 329, R03 329, R07 357, R11 357.

**F0.6 Category frequencies across all ratings** *(unchanged)*
- **Finding:** Ratings are concentrated at the low end of the scale, and category 7 is the rarest.
- **Linked object:** `fig-overview-rating-distribution` (N1, `ovfig02`). The numbers come from N1 `31873726` (stdout).
- **Numbers:**

  | category | n | share |
  |---|---|---|
  | 1 | 2029 | 0.259463 |
  | 2 | 2113 | 0.270205 |
  | 3 | 1467 | 0.187596 |
  | 4 | 1039 | 0.132864 |
  | 5 | 724 | 0.092583 |
  | 6 | 339 | 0.043350 |
  | 7 | 109 | 0.013939 |

**F0.7 Category use per rater** *(values unchanged; new cell id; "Ratings (n)"; R01 prints 1,174)*
- **Finding:** Five raters left at least one category unused, always at the top end of the scale. No rater has an internal gap.
- **Linked object:** `tbl-category-usage` (N2, `ff66593c`).
- **Numbers (headers as printed):**

  | Rater | Category 1 | Category 2 | Category 3 | Category 4 | Category 5 | Category 6 | Category 7 | Ratings (n) | Missing categories | Internal gap |
  |---|---|---|---|---|---|---|---|---|---|---|
  | R01 | 337 | 461 | 259 | 87 | 24 | 6 | 0 | 1,174 | 7 | False |
  | R02 | 241 | 179 | 124 | 126 | 91 | 67 | 45 | 873 | – | False |
  | R03 | 161 | 182 | 185 | 82 | 88 | 22 | 0 | 720 | 7 | False |
  | R04 | 164 | 164 | 90 | 69 | 92 | 36 | 5 | 620 | – | False |
  | R05 | 159 | 190 | 102 | 90 | 50 | 30 | 12 | 633 | – | False |
  | R06 | 301 | 113 | 57 | 34 | 9 | 6 | 0 | 520 | 7 | False |
  | R07 | 183 | 152 | 96 | 61 | 36 | 17 | 2 | 547 | – | False |
  | R08 | 101 | 127 | 106 | 91 | 60 | 30 | 7 | 522 | – | False |
  | R09 | 63 | 62 | 72 | 60 | 66 | 55 | 22 | 400 | – | False |
  | R10 | 25 | 156 | 76 | 64 | 47 | 13 | 2 | 383 | – | False |
  | R11 | 127 | 118 | 51 | 31 | 32 | 9 | 1 | 369 | – | False |
  | R12 | 11 | 48 | 90 | 77 | 27 | 10 | 1 | 264 | – | False |
  | R13 | 4 | 35 | 68 | 91 | 44 | 11 | 1 | 254 | – | False |
  | R14 | 105 | 66 | 40 | 31 | 10 | 5 | 2 | 259 | – | False |
  | R15 | 7 | 22 | 11 | 9 | 13 | 9 | 2 | 73 | – | False |
  | R16 | 4 | 14 | 9 | 14 | 5 | 3 | 3 | 52 | – | False |
  | R17 | 25 | 10 | 9 | 4 | 4 | 0 | 0 | 52 | 6;7 | False |
  | R18 | 1 | 8 | 14 | 12 | 16 | 4 | 0 | 55 | 7 | False |
  | R19 | 10 | 6 | 8 | 6 | 10 | 6 | 4 | 50 | – | False |

- **Caveat (notebook, `9b26fefd`):** "Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used."

**F0.8 Rater response styles (descriptive)** *(unchanged)*
- **Finding:** Rater means range from 1.760 (R06) to 3.836 (R18). Raters also differ in SD, entropy, floor and ceiling rates, and in how often they use the extreme and middle categories.
- **Linked object:** `fig-overview-rater-response-styles` (N1, `ovfig03`). The numbers come from unlabelled N1 cell `fb6df84b`, which is post-exclusion and has 19 rows. The cell prints `rater_desc.round(3)`, with rows sorted by mean.
- **Numbers (exactly as printed):**

  | rater | n_ratings | n_products | mean | median | sd | iqr | n_categories_used | entropy | floor_rate | ceiling_rate | extreme_category_rate | central_category_rate |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | R06 | 520.0 | 520.0 | 1.760 | 1.0 | 1.111 | 1.0 | 6.0 | 1.191 | 0.579 | 0.000 | 0.579 | 0.192 |
  | R17 | 52.0 | 52.0 | 2.077 | 2.0 | 1.296 | 2.0 | 5.0 | 1.367 | 0.481 | 0.000 | 0.481 | 0.327 |
  | R01 | 1174.0 | 1174.0 | 2.164 | 2.0 | 1.022 | 2.0 | 6.0 | 1.358 | 0.287 | 0.000 | 0.287 | 0.315 |
  | R14 | 259.0 | 259.0 | 2.220 | 2.0 | 1.359 | 2.0 | 7.0 | 1.496 | 0.405 | 0.008 | 0.413 | 0.313 |
  | R11 | 369.0 | 369.0 | 2.333 | 2.0 | 1.397 | 2.0 | 7.0 | 1.532 | 0.344 | 0.003 | 0.347 | 0.309 |
  | R07 | 547.0 | 547.0 | 2.404 | 2.0 | 1.406 | 2.0 | 7.0 | 1.580 | 0.335 | 0.004 | 0.338 | 0.353 |
  | R05 | 633.0 | 633.0 | 2.716 | 2.0 | 1.554 | 3.0 | 7.0 | 1.700 | 0.251 | 0.019 | 0.270 | 0.382 |
  | R03 | 720.0 | 720.0 | 2.750 | 3.0 | 1.402 | 2.0 | 6.0 | 1.643 | 0.224 | 0.000 | 0.224 | 0.493 |
  | R04 | 620.0 | 620.0 | 2.821 | 2.0 | 1.628 | 3.0 | 7.0 | 1.715 | 0.265 | 0.008 | 0.273 | 0.405 |
  | R10 | 383.0 | 383.0 | 2.997 | 3.0 | 1.311 | 2.0 | 7.0 | 1.564 | 0.065 | 0.005 | 0.070 | 0.488 |
  | R08 | 522.0 | 522.0 | 3.000 | 3.0 | 1.545 | 2.0 | 7.0 | 1.761 | 0.193 | 0.013 | 0.207 | 0.492 |
  | R02 | 873.0 | 873.0 | 3.032 | 3.0 | 1.841 | 3.0 | 7.0 | 1.822 | 0.276 | 0.052 | 0.328 | 0.391 |
  | R12 | 264.0 | 264.0 | 3.360 | 3.0 | 1.152 | 1.0 | 7.0 | 1.547 | 0.042 | 0.004 | 0.045 | 0.735 |
  | R16 | 52.0 | 52.0 | 3.442 | 3.0 | 1.589 | 2.0 | 7.0 | 1.762 | 0.077 | 0.058 | 0.135 | 0.538 |
  | R15 | 73.0 | 73.0 | 3.466 | 3.0 | 1.700 | 3.0 | 7.0 | 1.793 | 0.096 | 0.027 | 0.123 | 0.452 |
  | R09 | 400.0 | 400.0 | 3.642 | 4.0 | 1.819 | 3.0 | 7.0 | 1.903 | 0.158 | 0.055 | 0.212 | 0.495 |
  | R19 | 50.0 | 50.0 | 3.680 | 4.0 | 1.953 | 3.0 | 7.0 | 1.902 | 0.200 | 0.080 | 0.280 | 0.480 |
  | R13 | 254.0 | 254.0 | 3.681 | 4.0 | 1.116 | 1.0 | 7.0 | 1.520 | 0.016 | 0.004 | 0.020 | 0.799 |
  | R18 | 55.0 | 55.0 | 3.836 | 4.0 | 1.259 | 2.0 | 6.0 | 1.584 | 0.018 | 0.000 | 0.018 | 0.764 |

- **Direction (read off the printed values):**
  - SD: lowest R01 1.022, highest R19 1.953.
  - Entropy: lowest R06 1.191, highest R09 1.903.
  - Floor rate: highest R06 0.579, lowest R13 0.016.
  - Ceiling rate: highest R19 0.080. Five raters print 0.000: R06, R17, R01, R03 and R18.
  - Extreme-category rate: highest R06 0.579, lowest R18 0.018.
  - Central (3–5) rate: highest R13 0.799, lowest R06 0.192.
- **Definitions (notebook, `f3482d97` and the `fb6df84b` code):**
  - extreme categories are 1 and 7; middle categories are 3–5;
  - floor = share of ratings equal to 1; ceiling = share equal to 7;
  - entropy is computed with natural logarithms.
  - The markdown in `f3482d97` says these descriptives "anticipate what the models estimate formally". That is the notebook's own framing.
- **Caveats:**
  - The cell is unlabelled, so the table cannot be embedded.
  - The values are on the raw 1–7 scale and are not adjusted for which products each rater saw.
  - Counts print as floats ("520.0").
  - N1 `9f03e286` prints "Raters with <= 2 rated products: 0".

## (b) Model comparison

**F1.1 Information criteria** *(values unchanged; new cell id; separators; readable model labels)*
- **Finding:** The GRM has the lowest AIC, BIC and SABIC of the four estimated models. Among the adjacent-category models, M3 has the lowest AIC and SABIC, and M2 has the lowest BIC.
- **Linked object:** `tbl-model-fit` (N2, `92631058`).
- **Numbers (as printed):**

  | Model | Software | Family | Log-likelihood | Parameters | AIC | BIC | SABIC | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|---|---|---|---|---|---|---|
  | M1 (RSM/MFRM) | sirt::rm.facets | adjacent category | -12,186.218 | 25 | 24,422.435 | 24,577.620 | 24,498.183 | 701.980 | 68.825 | 392.931 |
  | M2 (PCM) | mirt | adjacent category | -11,817.489 | 109 | 23,852.978 | 24,529.585 | 24,183.237 | 132.524 | 20.790 | 77.985 |
  | M3 (GPCM) | mirt | adjacent category | -11,756.510 | 127 | 23,767.020 | 24,555.360 | 24,151.817 | 46.566 | 46.566 | 46.566 |
  | GRM | mirt | cumulative (not in LR ladder) | -11,733.227 | 127 | 23,720.455 | 24,508.795 | 24,105.251 | 0 | 0 | 0 |

- **Caption:** "Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion."
- **Caveat (notebook, `4e602b13`):** "The GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better)."

**F1.2 Likelihood-ratio tests** *(values unchanged; new cell ids)*
- **Finding:** Both steps up the adjacent-category ladder give significant LR tests.
- **Linked object:** `tbl-lr-tests` (N2, `abee45ba`).
- **Numbers:**

  | Comparison | χ² | df | df if all categories used | df equal | p |
  |---|---|---|---|---|---|
  | M1 vs M2: rater-specific thresholds | 737.457 | 84 | 90 | False | 4.22e-105 |
  | M2 vs M3: rater-specific discriminations | 121.958 | 18 | 18 | True | 1.79e-17 |

- **Notebook explanation (verbatim, `97a578bb`):** "\"df if all categories used\" is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories."
- **Caption:** "Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2."
- **Caveats:**
  - The count of unused end categories is not printed as a single figure. The unused categories are listed per rater in `tbl-category-usage` (F0.7).
  - AUDIT.md's "6" is NOT IN NOTEBOOK — not quotable.
  - As printed in `tbl-model-fit`, M1 was fitted with sirt::rm.facets and M2 with mirt.

**F1.3 GRM estimation** *(values unchanged; new cell id; Tolerance now "10⁻⁴"; separators)*
- **Finding:** The GRM converged, and its information matrix is positive definite.
- **Linked object:** `tbl-grm-convergence` (N2, `47b97fbe`).
- **Numbers:**
  - Method EM; Quadrature points 61; SE type Oakes; Tolerance 10⁻⁴.
  - Converged True; Iterations 165; Information matrix positive definite True.
  - Log-likelihood -11,733.227; Parameters 127; AIC 23,720.455; BIC 24,508.795; SABIC 24,105.251.
  - Products 3,668; Ratings (n) 7,820.

**F1.4 Discriminations in M3 (GPCM)** *(values unchanged; new cell id; "Ratings (n)")*
- **Finding:** Rater discriminations in M3 range from 0.283 (R09) to 2.606 (R16).
- **Linked object:** `tbl-discrimination-m3` (N2, `c971e20c`). The headers are Rater | Ratings (n) | Estimate | SE.
- **Numbers** (Rater, Ratings (n), Estimate (SE), in the printed order): R09 400 0.283 (0.055); R18 55 0.312 (0.145); R17 52 0.616 (0.235); R13 254 0.863 (0.159); R11 369 0.896 (0.145); R03 720 0.984 (0.142); R04 620 0.992 (0.184); R07 547 1.025 (0.138); R05 633 1.096 (0.154); R08 522 1.102 (0.195); R02 873 1.209 (0.272); R01 1,174 1.304 (0.131); R10 383 1.370 (0.320); R15 73 1.389 (0.412); R14 259 1.390 (0.433); R06 520 1.942 (0.385); R19 50 2.327 (1.866); R12 264 2.383 (0.680); R16 52 2.606 (1.419).
- **Caveats:**
  - The largest SEs belong to raters with about 50 ratings: R19 1.866 and R16 1.419.
  - Notebook framing (`43b1e0b3`): "Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data."

**F1.5 Unordered step parameters in M2/M3** *(values unchanged; new cell id; model labels "M2 (PCM)" / "M3 (GPCM)")*
- **Finding:** Nine raters have unordered steps in M2 (PCM), and nine raters do in M3 (GPCM).
- **Linked object:** `tbl-threshold-order` (N2, `50ad0312`). The headers are Model | Rater | Steps | Ordered | Reversals | Step parameters. Ordered is False in every row.
- **Numbers (Rater, Steps, Reversals, Step parameters):**
  - M2 (PCM):
    - R03 5, 1, -0.87;-0.21;1.11;0.69;2.64
    - R04 6, 1, -0.54;0.58;0.68;0.52;2.18;3.77
    - R05 6, 1, -0.74;0.62;0.58;1.46;1.81;2.72
    - R06 5, 1, 0.92;1.26;1.60;2.85;2.38
    - R11 6, 1, -0.36;0.96;1.06;0.93;2.65;4.15
    - R15 6, 2, -2.18;0.35;0.35;0.15;1.29;3.12
    - R16 6, 1, -2.09;0.18;-0.19;1.81;1.87;1.99
    - R17 4, 2, 0.49;0.18;1.30;0.98
    - R19 6, 2, -0.43;-0.85;0.10;-0.29;1.21;1.76
  - M3 (GPCM):
    - R03 5, 1, -0.82;-0.19;1.11;0.65;2.59
    - R04 6, 1, -0.53;0.58;0.66;0.48;2.13;3.69
    - R05 6, 1, -0.69;0.57;0.56;1.38;1.72;2.57
    - R06 5, 1, 0.51;1.06;1.46;2.30;2.27
    - R09 6, 2, -0.43;-0.78;0.63;-0.12;1.10;3.92
    - R11 6, 1, -0.29;1.09;1.14;0.94;2.78;4.31
    - R15 6, 1, -1.90;0.21;0.34;0.28;1.20;2.81
    - R17 4, 2, 1.12;0.22;1.74;0.83
    - R18 5, 1, -7.29;-2.14;0.42;-0.70;5.02
- **Caveat (notebook, `05c2d754`):** "In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction."

**F1.6 Marginal and empirical reliability by model** *(values unchanged; new cell id; readable model labels)*
- **Linked object:** `tbl-marginal-reliability-models` (N2, `08cda119`).
- **Numbers:**

  | Model | Latent variance | Marginal reliability | marginal_rxx (mirt) | Empirical reliability |
  |---|---|---|---|---|
  | M1 (RSM/MFRM) | 0.962 | 0.943 | – | 0.626 |
  | M2 (PCM) | 1.087 | 0.944 | – | 0.637 |
  | M3 (GPCM) | 1 | 0.955 | 0.955 | 0.657 |
  | GRM | 1 | 0.960 | 0.960 | 0.672 |

- **Direction:** Both the marginal and the empirical reliability increase in the order M1 < M2 < M3 < GRM.
- **Caveat (notebook, `6a2b68e5`):** "Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model."

## (c) Fit evidence and its stated limitations

**F1.7 GRM rater infit/outfit** *(values unchanged; new cell id; "Ratings (n)")*
- **Finding:** Under the GRM, every rater's infit and outfit is below 1. Infit ranges from 0.334 (R19) to 0.971 (R18), and outfit from 0.322 (R19) to 0.961 (R18).
- **Linked object:** `tbl-grm-rater-fit` (N2, `917fee86`). The headers are Rater | Ratings (n) | Infit | Outfit | S-X² | df | p | Imputations. R01's Ratings (n) prints "1,174".
- **Numbers (Infit / Outfit):** R01 0.680/0.650; R02 0.450/0.423; R03 0.699/0.687; R04 0.588/0.554; R05 0.617/0.576; R06 0.604/0.469; R07 0.724/0.645; R08 0.585/0.571; R09 0.871/0.870; R10 0.624/0.603; R11 0.829/0.784; R12 0.507/0.505; R13 0.831/0.834; R14 0.483/0.398; R15 0.754/0.663; R16 0.508/0.480; R17 0.926/0.824; R18 0.971/0.961; R19 0.334/0.322.
- **Caveats (notebook, `e967043f`, verbatim):**
  - "Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982)."
  - "With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked."
  - "No misfit cut-offs for infit and outfit are applied in this notebook."

**F1.8 S-X² (multiple imputation)** *(values unchanged; new cell id)*
- **Finding:** All S-X² p-values lie between 0.294 (R12) and 0.671 (R02).
- **Linked object:** `tbl-grm-rater-fit` (N2, `917fee86`).
- **Numbers** (S-X² / df / p; Imputations is 20 for every rater): R01 218.569/213.550/0.392; R02 289.502/300.850/0.671; R03 277.954/280.450/0.531; R04 280.793/290.200/0.643; R05 291.511/293.850/0.528; R06 193.853/190.100/0.411; R07 282.598/285.850/0.543; R08 282.277/285/0.534; R09 440.411/433.550/0.400; R10 247.751/250.600/0.539; R11 298.249/295.100/0.438; R12 207.049/196.800/0.294; R13 263.892/264.200/0.494; R14 224.935/234.450/0.661; R15 265.749/260.900/0.405; R16 200.549/205.150/0.578; R17 279.802/280.350/0.498; R18 342.054/335.700/0.394; R19 223.516/228.400/0.579.
- **Caveat (notebook, `e967043f`):** "S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative."

**F1.9 Local dependence (Q3)** *(values unchanged; new cell ids; "computable" definition checked)*
- **Finding:** The mean Q3 over 137 computable rater pairs is -0.238, and 20 pairs are flagged. The table shows the ten pairs with the largest |Q3 − mean Q3| among pairs with at least 30 shared products. Nine of them deviate negatively and one, R10–R11, positively. All ten are Flagged True.
- **Linked object:** `tbl-grm-q3-flagged` (N2, `7bb634a8`). The summary line comes from unlabelled N2 cell `5e8e7334` (stdout).
- **Numbers:**
  - `5e8e7334` stdout, verbatim: "Mean Q3 over 137 computable rater pairs: -0.238; pairs flagged (flag_q3): 20".
  - The ten pairs:

    | Rater 1 | Rater 2 | Shared products | Q3 | Q3 minus mean Q3 | Overlap | Flagged |
    |---|---|---|---|---|---|---|
    | R08 | R19 | 46 | -0.761 | -0.524 | – | True |
    | R08 | R12 | 51 | -0.743 | -0.506 | – | True |
    | R02 | R14 | 108 | -0.621 | -0.383 | – | True |
    | R03 | R10 | 49 | -0.616 | -0.379 | – | True |
    | R01 | R10 | 157 | -0.613 | -0.376 | – | True |
    | R02 | R04 | 257 | -0.611 | -0.373 | – | True |
    | R02 | R08 | 72 | -0.589 | -0.352 | – | True |
    | R10 | R11 | 32 | 0.105 | 0.343 | – | True |
    | R01 | R08 | 191 | -0.565 | -0.327 | – | True |
    | R04 | R14 | 47 | -0.560 | -0.322 | – | True |

- **Notebook explanation (verbatim, `ee672a5b`):** "Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). Flagged marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2."
- **Caption:** "Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products."
- **Caveats:**
  - **"Computable" is not defined in the notebook.** There is no notebook statement about "at least 3 shared products". The stdout code counts pairs with a non-missing Q3 (`_q3["q3"].notna()`).
    - The threshold exists only in the R pipeline (context, NOT IN NOTEBOOK — not quotable): `R/02_grm.R`, `Q3_MIN_OVERLAP <- 3L   # below this, a pairwise Q3 is not computed`.
    - The pipeline also requires non-zero residual SDs for both raters.
  - The table shows only 10 of the 20 flagged pairs.
  - "Overlap" is "–" in every row, and the notebook does not define it.
  - The stdout still uses the code name "flag_q3", while the table header says "Flagged".

**F1.10 Global fit (C2)** *(values unchanged; new cell id)*
- **Finding:** C2 was not computable, because 17 of 171 rater pairs share no products.
- **Linked object:** `tbl-grm-global-fit` (N2, `5fdc553b`). The headers are Statistic | Computable | Rater pairs | Rater pairs without shared products | Note.
- **Numbers:** C2; Computable False; Rater pairs 171; Rater pairs without shared products 17. The Note reads: "Not computable: 17 of 171 rater pairs share no products, so their bivariate moments and hence C2 are undefined."
- **Notebook explanation (verbatim, `410e2d66`):** "C2 is a limited-information test of overall model fit (Cai & Monroe, 2014). The table reports either the statistic or the reason it could not be computed: C2 needs the joint distribution of every pair of raters, which is undefined for rater pairs that share no products."
- **Caveat:** The notebook reports no other global fit index.

**F1.11 M1 (MFRM) rater fit** *(values unchanged; new cell id; "Ratings (n)")*
- **Finding:** Under M1, R17 (infit 1.328, outfit 1.190) and R18 (infit 1.009, outfit 1.071) are the only raters with values at or above 1. All other raters are below 1. R12 has the lowest values: infit 0.238, outfit 0.255.
- **Linked object:** `tbl-rater-fit-m1` (N2, `72e651dc`). The headers are Rater | Ratings (n) | Infit | Outfit.
- **Numbers (Infit / Outfit):** R01 0.466/0.481; R02 0.786/0.782; R03 0.579/0.579; R04 0.687/0.660; R05 0.701/0.669; R06 0.909/0.705; R07 0.826/0.751; R08 0.540/0.548; R09 0.978/0.958; R10 0.407/0.389; R11 0.938/0.874; R12 0.238/0.255; R13 0.405/0.406; R14 0.747/0.695; R15 0.753/0.698; R16 0.452/0.457; R17 1.328/1.190; R18 1.009/1.071; R19 0.654/0.701.
- **Caption:** "Rater infit and outfit mean squares under M1 (rating scale model / MFRM)."
- **Caveats:**
  - `e967043f`: "No misfit cut-offs for infit and outfit are applied in this notebook."
  - `3a6131be`: these are "the fit statistics usually reported for many-facet Rasch models (Eckes, 2015)."
  - REPORT.md uses 0.7–1.3. This range is NOT IN NOTEBOOK — not quotable.

## (d) Reliability, including by number of ratings and CIs

**F1.12 Marginal reliabilities with 95% intervals** *(values unchanged; new cell ids; Quantity labels with spaces)*
- **Finding:** The empirical marginal reliability of the actual GRM scores is 0.672 [0.649, 0.687]. The model-based marginal reliability for the hypothetical full panel is 0.960 [0.953, 0.968].
- **Linked object:** `tbl-grm-reliability-ci` (N2, `83060b39`). The same values appear in `tbl-grm-reliability-summary` (`11c2b168`) and `tbl-reliability-overview` (`f3cb7139`).
- **Numbers:**

  | Quantity | Estimate | 95% CI lower | 95% CI upper | Draws | Draws rejected |
  |---|---|---|---|---|---|
  | empirical marginal reliability | 0.672 | 0.649 | 0.687 | 200 | 87 |
  | model based marginal reliability | 0.960 | 0.953 | 0.968 | 200 | 87 |

  - In the summary table (Quantity | Value), the rows print as:
    - "empirical_marginal_reliability (primary; actual scores)" 0.672;
    - "model_based_marginal_reliability_mirt (hypothetical full panel)" 0.960;
    - "model_based_marginal_reliability_grid (check)" 0.960;
    - "var theta eap" 0.672; "mean psd squared" 0.328.
  - Overview table, verbatim: "95% CI [0.649, 0.687] (200 parameter draws); Var(theta)/(Var(theta)+mean(PSD^2))" and "95% CI [0.953, 0.968] (200 parameter draws); mirt::marginal_rxx, all raters".
- **Caption (CI table):** "Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced."
- **Notebook explanation (verbatim, `bef799a0`):** "95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. Draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; Draws rejected counts these."
- **Caveat (notebook, `fa4304b5`):** The empirical value "refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure". The model-based value "refers to the hypothetical full panel".

**F1.13 Distribution of product-level reliability rel_post** *(values unchanged; new cell ids; labels with spaces)*
- **Finding:** Product-level reliability rel_post = 1 − PSD² has a median of 0.698 and ranges from 0.057 to 0.929.
- **Linked object:** `tbl-grm-reliability-summary` (N2, `11c2b168`) and `fig-grm-rel-post-histogram` (`798a494e`).
- **Numbers (labels as printed):** rel post min 0.057; rel post p10 0.485; rel post q1 0.596; rel post median 0.698; rel post q3 0.769; rel post p90 0.813; rel post max 0.929; rel post mean 0.672; rel post iqr 0.173.

**F1.14 Reliability by number of ratings per product (observed)** *(values unchanged; new cell ids; "Ratings (n)"; 2,080)*
- **Finding:** Mean rel_post rises steadily from 0.520 for products with 1 rating to 0.919 for products with 10 ratings. Mean PSD falls from 0.686 to 0.285.
- **Linked object:** `tbl-grm-reliability-by-n` (N2, `1d4d6b6f`) and `fig-grm-rel-post-by-n` (`0d41b887`).
- **Numbers ("Ratings (n)" here = ratings per product):**

  | Ratings (n) | Products | Mean rel_post | Median rel_post | Mean rel_info | Mean PSD |
  |---|---|---|---|---|---|
  | 1 | 897 | 0.520 | 0.553 | 0.544 | 0.686 |
  | 2 | 2,080 | 0.698 | 0.714 | 0.713 | 0.545 |
  | 3 | 357 | 0.757 | 0.768 | 0.767 | 0.488 |
  | 4 | 125 | 0.810 | 0.826 | 0.818 | 0.430 |
  | 5 | 125 | 0.820 | 0.831 | 0.831 | 0.420 |
  | 6 | 47 | 0.847 | 0.856 | 0.851 | 0.387 |
  | 7 | 20 | 0.869 | 0.880 | 0.874 | 0.358 |
  | 8 | 11 | 0.875 | 0.885 | 0.879 | 0.347 |
  | 9 | 3 | 0.879 | 0.920 | 0.883 | 0.338 |
  | 10 | 3 | 0.919 | 0.920 | 0.917 | 0.285 |

- **Notebook statement (`e321b693`):** "How product-level precision grows with the number of ratings a product received." This is a description of the table, not a test.
- **Caveats:**
  - The 9- and 10-rating rows rest on 3 products each.
  - No CIs are printed.
  - No n reaches the model-based full-panel value of 0.960.
  - The "confounded" sentence is not in the notebook; see the removed values in Changes item 12.

**F1.15 Full-panel (hypothetical) information and reliability** *(unchanged; new cell ids)*
- **Linked object:** `fig-grm-panel-information` (N2, `bdeadff4`).
- **Numbers:** None are printed beyond the model-based value of 0.960 (F1.12).
- **Caveats:**
  - Notebook (`710bd8d0`): "This is a hypothetical upper bound, not the precision of the actual scores."
  - Caption: "it applies to a product rated by all raters."

**F1.16 Consistency of rel_post and rel_info** *(values unchanged; new cell ids; labels with spaces)*
- **Finding:** The two product-level reliability measures correlate at 0.935. Mean rel_info − rel_post is 0.016, and 320 products differ by more than 0.1.
- **Linked object:** `tbl-grm-reliability-summary` (N2, `11c2b168`) and `fig-grm-rel-consistency` (`5cfe0ae5`).
- **Numbers:** consistency cor rel post rel info 0.935; consistency mean diff rel info minus rel post 0.016; consistency max abs diff 0.413; products abs diff gt 0.1 320.
- **Notebook statement (`73a8b4e0`):** "Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree."

**F1.17 rel_post by θ̂** *(unchanged; new cell ids)*
- **Linked object:** `fig-grm-rel-post-by-theta` (N2, `73767051`). Figure only, with no printed numbers.
- **Notebook statement (`d354cbcf`):** "Precision depends on where a product lies relative to its raters' thresholds."

**F1.18 Naive indices with bootstrap CIs** *(values unchanged; new cell ids; separators; new caption; overview note now says "639 of 1000 replications computable")*
- **Finding:** The pairwise-covariance Cronbach's α is 0.928, the fully crossed-block Cronbach's α is 0.658, and Krippendorff's ordinal α is 0.392. For the pairwise Cronbach's α, 361 of 1,000 bootstrap replications failed, and 639 of 1000 were computable.
- **Linked object:** `tbl-naive-indices` (N2, `688365f2`) and `tbl-reliability-overview` (`f3cb7139`).
- **Numbers:**

  | Index | Value | 95% CI lower | 95% CI upper | Raters | Products | Bootstrap replications | Failed replications |
  |---|---|---|---|---|---|---|---|
  | Cronbach's alpha: pairwise covariances, all usable raters | 0.928 | 0.891 | 0.943 | 14 | 1,900 | 1,000 | 361 |
  | Cronbach's alpha: fully crossed block (listwise complete) | 0.658 | 0.526 | 0.756 | 3 | 139 | 1,000 | 0 |
  | Krippendorff's alpha (ordinal) | 0.392 | 0.362 | 0.417 | 19 | 2,771 | 1,000 | 0 |

  The overview table's "CI or note" column, verbatim:
  - Krippendorff: "95% bootstrap CI [0.362, 0.417], 1000 replications"
  - Pairwise Cronbach: "95% CI [0.891, 0.943] (bootstrap, 639 of 1000 replications computable, approximate); 14 raters; removed: R19;R14;R02;R16;R12"
  - Crossed block: "95% CI [0.526, 0.756] (bootstrap, 1000 replications); 3 raters, 139 products"
- **Caption (naive indices):** "Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate."
- **Notebook notes (verbatim, `78acc27d`):**
  - "Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (Failed replications in the table)."
  - Naive indices "are reference values for common practice. They are not used downstream."
  - Cronbach's α "assumes τ-equivalent raters and complete data".
  - Krippendorff's α "measures the agreement of single ratings, treating raters as interchangeable".

**F1.19 Overview of indices and what each refers to** *(values unchanged; new cell id; readable row labels)*
- **Linked object:** `tbl-reliability-overview` (N2, `f3cb7139`). The headers are Index | Refers to | Value | CI or note.
- **Numbers:** These repeat F1.12, F1.13, F1.6 and F1.18:
  - "GRM: median rel_post" 0.698 ("Q1 0.596, Q3 0.769"); "GRM: IQR rel_post" 0.173.
  - "M1 (RSM): marginal reliability" 0.943; "M2 (PCM): marginal reliability" 0.944; "M3 (GPCM): marginal reliability" 0.955.
  - "Refers to" column entries: "consensus of single ratings"; "consistency of the unweighted rater mean"; "consistency of the unweighted rater mean (crossed subset)"; "actual theta_hat (primary)"; "hypothetical full panel"; "precision per product" (twice); "comparison" (three times).
- **Notebook statement (`c8be1f2b`):** "They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable."

**F1.20 Projected reliability by number of ratings per product (simulation from the fitted GRM; side note)** *(values unchanged; new cell ids; new table caption)*
- **Finding:** In the simulation with randomly drawn raters, the projected empirical marginal reliability rises with every step in k:
  - 0.508 [0.495, 0.522] at k = 1;
  - 0.688 [0.676, 0.698] at k = 2;
  - 0.925 [0.922, 0.929] at k = 10.
- **Linked object:** `tbl-grm-reliability-projection` (N2, `5fa6455c`); `fig-grm-reliability-projection` (`95d35bde`); simulation settings from unlabelled stdout `71be63e4`; method note `ce0f3bbd`.
- **Numbers:**

  | Ratings per product (k) | Empirical reliability [95% range] | Mean rel_post |
  |---|---|---|
  | 1 | 0.508 [0.495, 0.522] | 0.508 |
  | 2 | 0.688 [0.676, 0.698] | 0.690 |
  | 3 | 0.775 [0.764, 0.784] | 0.776 |
  | 4 | 0.826 [0.817, 0.832] | 0.826 |
  | 5 | 0.857 [0.850, 0.864] | 0.857 |
  | 6 | 0.880 [0.872, 0.884] | 0.879 |
  | 7 | 0.896 [0.891, 0.901] | 0.896 |
  | 8 | 0.908 [0.903, 0.911] | 0.908 |
  | 9 | 0.918 [0.914, 0.921] | 0.918 |
  | 10 | 0.925 [0.922, 0.929] | 0.926 |

- **Simulation settings (stdout `71be63e4`, verbatim):** "50 replications of 2000 simulated products per k; seed 20260713."
- **Method note (verbatim, `ce0f3bbd`):** "**Side note: projected reliability with more ratings.** A simple gauge of the value of adding ratings, supplementary to the observed values above. Products with θ ~ N(0, 1) are simulated; each gets k ratings from k raters of the actual panel, drawn at random, with ratings generated from the fitted GRM and scored with its parameters (treated as known). The table gives the empirical marginal reliability (mean and 95% range over replications) and the mean product-level reliability rel_post."
- **Caption (table, NEW):** "Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²)."
- **Caption (figure, unchanged):** "Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications."
- **Direction (read off the printed values):**
  - The empirical reliability rises with every step in k from 1 to 10. The increments get smaller: +0.180 from k = 1 to 2, and +0.007 from k = 9 to 10. These differences are computed from the printed values; the notebook does not print them.
  - Empirical and Mean rel_post differ by at most 0.002 in any row (k = 2: 0.688 vs 0.690).
  - No projected value reaches the model-based full-panel value of 0.960 (F1.12). The highest is 0.925 / 0.926 at k = 10.
- **Caveats:**
  - The "95% range" is the range over 50 simulation replications. It does not include parameter uncertainty, because the parameters are "treated as known". It is not the same kind of interval as the parameter-draw CIs in F1.12.
  - The values are simulated (θ ~ N(0, 1), random raters), not observed. The notebook makes no direct numeric comparison with F1.14.
  - The table covers k = 1 to 10 only.
  - "A simple gauge of the value of adding ratings" and "Side note" are the notebook's own framing.
  - The caption's "each equally likely" is the notebook's description of the rater draw.

## (e) Rater parameters, information and uncertainty

**F2.1 GRM discrimination a with SE** *(values unchanged; new cell id; "Ratings (n)"; new caption)*
- **Finding:** GRM discriminations range from 0.63 (R18) to 3.71 (R19). The SEs are largest for raters with few ratings.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `3b9d3f35`). The headers are Rater | Ratings (n) | a | b1 | b2 | b3 | b4 | b5 | b6.
- **Numbers** (Rater, Ratings (n), a (SE)): R01 1,174 1.96 (0.16); R02 873 2.50 (0.33); R03 720 1.94 (0.20); R04 620 2.04 (0.24); R05 633 2.21 (0.23); R06 520 2.81 (0.42); R07 547 1.99 (0.20); R08 522 2.17 (0.28); R09 400 0.86 (0.15); R10 383 2.24 (0.34); R11 369 1.82 (0.21); R12 264 2.90 (0.57); R13 254 1.50 (0.22); R14 259 2.75 (0.66); R15 73 2.50 (0.52); R16 52 3.70 (1.36); R17 52 1.45 (0.46); R18 55 0.63 (0.26); R19 50 3.71 (2.22).
- **Caption (NEW):** "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used."
- **Caveats:**
  - R19 and R16 (50 and 52 ratings) have the two highest a values (3.71 and 3.70) and the two largest SEs (2.22 and 1.36).
  - Notebook (`ddaeea02`): "a is the rater's discrimination: how sharply the ratings separate products of different creativity."

**F2.2 GRM thresholds b_k with SE (severity)** *(values unchanged; new cell id)*
- **Finding:** First thresholds b1 range from -6.56 (R18) to 0.29 (R06). R06 is the only rater with a positive b1.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `3b9d3f35`).
- **Numbers:**

  | Rater | Ratings (n) | b1 | b2 | b3 | b4 | b5 | b6 |
  |---|---|---|---|---|---|---|---|
  | R01 | 1,174 | -0.77 (0.06) | 0.58 (0.05) | 1.73 (0.09) | 2.75 (0.16) | 3.79 (0.28) | – |
  | R02 | 873 | -0.71 (0.06) | -0.03 (0.05) | 0.40 (0.05) | 0.90 (0.07) | 1.40 (0.09) | 2.03 (0.13) |
  | R03 | 720 | -1.09 (0.08) | -0.15 (0.06) | 0.75 (0.07) | 1.27 (0.10) | 2.45 (0.19) | – |
  | R04 | 620 | -0.77 (0.08) | 0.17 (0.06) | 0.66 (0.07) | 1.10 (0.09) | 2.04 (0.15) | 3.41 (0.32) |
  | R05 | 633 | -0.83 (0.07) | 0.16 (0.06) | 0.72 (0.07) | 1.36 (0.09) | 1.96 (0.13) | 2.82 (0.21) |
  | R06 | 520 | 0.29 (0.06) | 1.05 (0.08) | 1.62 (0.11) | 2.31 (0.17) | 2.77 (0.24) | – |
  | R07 | 547 | -0.54 (0.07) | 0.40 (0.07) | 1.07 (0.09) | 1.71 (0.12) | 2.47 (0.19) | 3.87 (0.44) |
  | R08 | 522 | -1.16 (0.10) | -0.29 (0.06) | 0.37 (0.07) | 1.07 (0.10) | 1.85 (0.15) | 2.94 (0.27) |
  | R09 | 400 | -2.21 (0.36) | -1.08 (0.21) | -0.08 (0.13) | 0.75 (0.17) | 1.88 (0.31) | 3.68 (0.59) |
  | R10 | 383 | -2.04 (0.18) | -0.17 (0.07) | 0.48 (0.08) | 1.14 (0.12) | 2.12 (0.21) | 3.38 (0.45) |
  | R11 | 369 | -0.53 (0.09) | 0.60 (0.09) | 1.19 (0.12) | 1.70 (0.15) | 2.73 (0.27) | 4.17 (0.65) |
  | R12 | 264 | -2.01 (0.21) | -0.90 (0.10) | 0.16 (0.08) | 1.27 (0.12) | 2.13 (0.20) | 3.41 (0.47) |
  | R13 | 254 | -3.38 (0.49) | -1.50 (0.20) | -0.26 (0.11) | 1.20 (0.16) | 2.64 (0.33) | 4.43 (0.83) |
  | R14 | 259 | -0.20 (0.09) | 0.54 (0.09) | 1.08 (0.13) | 1.81 (0.20) | 2.35 (0.27) | 3.08 (0.42) |
  | R15 | 73 | -1.70 (0.27) | -0.25 (0.15) | 0.26 (0.14) | 0.66 (0.15) | 1.33 (0.21) | 2.66 (0.46) |
  | R16 | 52 | -1.37 (0.29) | -0.26 (0.15) | 0.21 (0.14) | 1.17 (0.20) | 1.74 (0.24) | 2.24 (0.31) |
  | R17 | 52 | -0.18 (0.23) | 0.55 (0.27) | 1.35 (0.44) | 2.01 (0.63) | – | – |
  | R18 | 55 | -6.56 (3.05) | -2.76 (1.20) | -0.58 (0.50) | 0.97 (0.59) | 4.44 (1.80) | – |
  | R19 | 50 | -0.94 (0.22) | -0.59 (0.18) | -0.14 (0.16) | 0.20 (0.17) | 0.93 (0.23) | 1.69 (0.35) |

  - R01, R03, R06 and R18 have no b6. R17 has no b5 or b6. All other raters have b1–b6.
- **Caveats:**
  - Notebook (`ddaeea02`, verbatim): "b_k is the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater. No rater has an internal category gap, so b_k always separates categories k and k + 1; raters who never used the top categories have no estimate for the highest thresholds."
  - R18 has the largest threshold SEs (b1 SE 3.05).

**F2.3 Rater information summary and shares** *(values unchanged; new cell id; "Ratings (n)"; new caption)*
- **Finding:** Information per rating ranges from 0.123 (R18) to 3.539 (R19). The share of panel information ranges from 0.005 (R18) to 0.135 (R19).
- **Linked object:** `tbl-grm-information-summary` (N2, `11b00860`), `fig-grm-rater-information` (`00420963`) and `fig-grm-information-shares` (`1ffe1c91`).
- **Headers:** Rater | Ratings (n) | Information per rating | θ at maximum | Maximum information | Share of panel information | Share at θ = −2 | Share at θ = −1 | Share at θ = 0 | Share at θ = 1 | Share at θ = 2.
- **Numbers** (Information per rating / θ at maximum / Maximum information / Share of panel information / shares at θ = −2, −1, 0, 1, 2):
  - R01 0.979 / 2.700 / 1.129 / 0.037 / 0.030, 0.043, 0.034, 0.036, 0.040
  - R02 1.705 / 0.450 / 1.981 / 0.065 / 0.023, 0.065, 0.065, 0.066, 0.063
  - R03 1.080 / 0.900 / 1.173 / 0.041 / 0.048, 0.049, 0.038, 0.039, 0.038
  - R04 1.155 / 0.650 / 1.326 / 0.044 / 0.029, 0.047, 0.043, 0.044, 0.043
  - R05 1.343 / 0.750 / 1.529 / 0.051 / 0.032, 0.056, 0.048, 0.051, 0.053
  - R06 1.410 / 2.400 / 2.406 / 0.054 / 0.001, 0.009, 0.057, 0.079, 0.083
  - R07 1.056 / 1.200 / 1.248 / 0.040 / 0.020, 0.038, 0.039, 0.042, 0.043
  - R08 1.359 / 0.300 / 1.456 / 0.052 / 0.058, 0.062, 0.049, 0.048, 0.048
  - R09 0.238 / 0.100 / 0.241 / 0.009 / 0.022, 0.011, 0.008, 0.008, 0.008
  - R10 1.330 / 0.550 / 1.549 / 0.051 / 0.129, 0.041, 0.050, 0.051, 0.051
  - R11 0.877 / 1.200 / 1.050 / 0.033 / 0.020, 0.032, 0.032, 0.035, 0.035
  - R12 2.120 / 1.350 / 2.324 / 0.081 / 0.221, 0.103, 0.074, 0.071, 0.082
  - R13 0.655 / -0.550 / 0.669 / 0.025 / 0.061, 0.031, 0.022, 0.022, 0.023
  - R14 1.722 / 0.800 / 2.311 / 0.066 / 0.005, 0.031, 0.072, 0.077, 0.082
  - R15 1.710 / 0.350 / 1.978 / 0.065 / 0.138, 0.060, 0.065, 0.063, 0.050
  - R16 3.300 / 1.850 / 4.069 / 0.126 / 0.111, 0.126, 0.135, 0.116, 0.143
  - R17 0.543 / 0.950 / 0.665 / 0.021 / 0.013, 0.018, 0.021, 0.022, 0.021
  - R18 0.123 / -0.500 / 0.125 / 0.005 / 0.012, 0.006, 0.004, 0.004, 0.004
  - R19 3.539 / -0.100 / 4.266 / 0.135 / 0.026, 0.171, 0.142, 0.126, 0.090
- **Caption (NEW):** "Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ). Ratings (n) is the number of ratings the rater gave."
- **Notebook statements:**
  - `5985f03f`: "Information from different raters adds up under local independence."
  - `beb46ce7`: "For each rater: information averaged over the N(0, 1) distribution of θ, where it peaks, and the rater's share of the full-panel information."

**F2.4 Intervals for rater information and share** *(values unchanged; new cell id; "Ratings (n)"; new caption)*
- **Finding:** The 95% intervals for information and share are widest for raters with few ratings:
  - R19: information 3.54 [0.41, 11.02], share 0.135 [0.017, 0.331].
  - R16: information 3.30 [0.73, 6.49], share 0.126 [0.026, 0.223].
- **Linked object:** `tbl-grm-rater-information-ci` (N2, `67f02093`).
- **Numbers:**

  | Rater | Ratings (n) | Information per rating [95% interval] | Share of panel information [95% interval] |
  |---|---|---|---|
  | R01 | 1,174 | 0.98 [0.72, 1.22] | 0.037 [0.022, 0.050] |
  | R02 | 873 | 1.70 [0.90, 2.56] | 0.065 [0.035, 0.098] |
  | R03 | 720 | 1.08 [0.75, 1.47] | 0.041 [0.023, 0.056] |
  | R04 | 620 | 1.16 [0.62, 1.74] | 0.044 [0.022, 0.064] |
  | R05 | 633 | 1.34 [0.91, 1.81] | 0.051 [0.031, 0.070] |
  | R06 | 520 | 1.41 [0.88, 2.09] | 0.054 [0.033, 0.080] |
  | R07 | 547 | 1.06 [0.69, 1.38] | 0.040 [0.026, 0.057] |
  | R08 | 522 | 1.36 [0.79, 1.96] | 0.052 [0.027, 0.077] |
  | R09 | 400 | 0.24 [0.11, 0.42] | 0.009 [0.004, 0.015] |
  | R10 | 383 | 1.33 [0.66, 2.03] | 0.051 [0.025, 0.081] |
  | R11 | 369 | 0.88 [0.56, 1.25] | 0.033 [0.020, 0.047] |
  | R12 | 264 | 2.12 [0.94, 3.29] | 0.081 [0.036, 0.131] |
  | R13 | 254 | 0.65 [0.31, 0.98] | 0.025 [0.010, 0.037] |
  | R14 | 259 | 1.72 [0.52, 3.13] | 0.066 [0.016, 0.112] |
  | R15 | 73 | 1.71 [0.70, 3.08] | 0.065 [0.029, 0.112] |
  | R16 | 52 | 3.30 [0.73, 6.49] | 0.126 [0.026, 0.223] |
  | R17 | 52 | 0.54 [0.11, 1.37] | 0.021 [0.004, 0.052] |
  | R18 | 55 | 0.12 [0.01, 0.35] | 0.005 [0.000, 0.013] |
  | R19 | 50 | 3.54 [0.41, 11.02] | 0.135 [0.017, 0.331] |

- **Caption (NEW):** "Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws. Ratings (n) is the number of ratings the rater gave."
- **Caveats:**
  - Notebook (`f2389ee8`): "95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings."
  - These are the same draws as in F1.12: 200 accepted, 87 rejected and replaced. The caption now states "200 accepted parameter draws".
  - Information is printed at 2 decimals here and at 3 decimals in F2.3. Three point estimates with a final 5 round down: R02 1.705 → 1.70 and R13 0.655 → 0.65. This is consistent with rounding the full-precision values.
  - The R18 share lower bound prints as 0.000.

**F2.5 Category response functions** *(unchanged; new cell id)*
- **Linked object:** `fig-grm-category-response-functions` (N2, `fe48d532`). Figure only, with no printed numbers.

## (f) Model dependence of scores and rankings

**F2.6 Correlations of EAP scores between models** *(values unchanged; new cell id; readable labels; new caption)*
- **Finding:** All correlations between models are 0.975 or higher. GRM–M3 is 0.996 on both Pearson and Spearman. GRM–M1 is the lowest, at Pearson 0.975 and Spearman 0.978.
- **Linked object:** `tbl-theta-correlations` (N2, `e5337bbd`).
  - Headers: Method | Model | M1 (RSM/MFRM) | M2 (PCM) | M3 (GPCM) | GRM | M1, sirt default grid.
  - Method values: "Pearson" and "Spearman".
- **Numbers:**
  - Pearson: M1–M2 0.993; M1–M3 0.980; M1–GRM 0.975; M2–M3 0.989; M2–GRM 0.985; M3–GRM 0.996.
  - Spearman: M1–M2 0.996; M1–M3 0.983; M1–GRM 0.978; M2–M3 0.987; M2–GRM 0.983; M3–GRM 0.996.
  - "M1, sirt default grid" correlates 1.000 with M1 (RSM/MFRM) on both coefficients.
- **Caption (NEW):** "Correlations of the EAP estimates between models (Pearson and Spearman). 'M1, sirt default grid' is M1 re-estimated with the default quadrature grid of sirt, as a software check."
- **Notebook framing (`cbe35366`):** "High values mean the ranking of products hardly depends on the model."

**F2.7 Ranking change relative to the GRM** *(values unchanged; M3 ≥ 2 quintiles now prints 0.001)*
- **Finding:** Relative to the GRM, the share of products changing quintile is 0.202 under M1, 0.150 under M2 and 0.075 under M3.
- **Linked object:** `tbl-score-agreement` (N2, `3375b00b`).
- **Numbers:**

  | Model | Pearson r | Spearman ρ | Mean percentile shift | 95th percentile of shift | Maximum shift | Share changing quintile | Share changing ≥ 2 quintiles |
  |---|---|---|---|---|---|---|---|
  | M1 (RSM/MFRM) | 0.975 | 0.978 | 0.042 | 0.130 | 0.432 | 0.202 | 0.004 |
  | M2 (PCM) | 0.985 | 0.983 | 0.033 | 0.117 | 0.413 | 0.150 | 0.003 |
  | M3 (GPCM) | 0.996 | 0.996 | 0.017 | 0.044 | 0.234 | 0.075 | 0.001 |

- **Caption:** "Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes."
- **Notebook statement (`04c0a49b`):** "How far products move in the ranking when another model replaces the GRM: the mean and 95th-percentile shift in percentile rank, and the share of products that change quintile."
- **Caveats:**
  - Percentile shifts are on a 0–1 scale (caption).
  - Quote M3's "Share changing ≥ 2 quintiles" as 0.001. "0.000545256" is no longer printed.

## (g) Sensitivity analyses

**F2.8 Sensitivity to the rater exclusion** *(values unchanged; new cell id; separators; row labels as printed)*
- **Finding:** Refitting the GRM with all 22 raters changes the empirical marginal reliability from 0.67199 to 0.67186, and the model-based reliability from 0.95986 to 0.96186. θ̂ from the two fits correlates at 0.99997 (Pearson).
- **Linked object:** `tbl-sensitivity-rater-exclusion` (N2, `645f0860`), printed with 5 decimals. The headers are Quantity | Final data | All raters | Note.
- **Numbers (Final data vs All raters; labels as printed):**
  - n raters 19 vs 22; n ratings 7,820 vs 7,844; n products 3,668 vs 3,669; excluded raters "–" vs R20;R21;R22.
  - empirical marginal reliability 0.67199 vs 0.67186 ("Var(theta)/(Var(theta)+mean(PSD^2))").
  - model based marginal reliability 0.95986 vs 0.96186 ("mirt::marginal_rxx (hypothetical full panel)").
  - Note "all-raters vs final GRM, 3668 common products":
    - theta pearson common products 0.99997;
    - theta spearman common products 0.99996;
    - theta mean abs diff 0.00171;
    - theta max abs diff 0.16246;
    - share products changing quintile 0.00491.
  - Note "all-raters vs final GRM, 19 common raters": a max abs diff common raters 0.19820; a pearson common raters 0.99880.
- **Caveat:** No CIs are given for the differences.

## (h) Raw mean vs model-based scores

**F2.9 Raw mean rating vs GRM score** *(values unchanged; new cell id; "Ratings (n)"; 2,080)*
- **Finding:** In each group of products with 1, 2 and 3 or more ratings, the raw mean rating and the GRM score agree with Kendall's τ-b between 0.815 and 0.842.
  - Between 0.042 and 0.070 of product pairs with different raw means are ordered the other way round by the GRM score.
  - Among products with the same raw mean, the GRM scores lie on average between 0.619 and 1.537 apart, and at most 2.196 apart (θ̂ range).
- **Linked object:** `tbl-raw-mean-vs-grm` (N2, `8006093d`).
- **Numbers ("Ratings (n)" here = ratings per product):**

  | Ratings (n) | Products | Kendall's τ-b | Share of pairs in reversed order | Mean θ̂ range at equal raw mean | Maximum θ̂ range at equal raw mean |
  |---|---|---|---|---|---|
  | 1 | 897 | 0.832 | 0.042 | 1.283 | 1.436 |
  | 2 | 2,080 | 0.815 | 0.067 | 1.537 | 2.196 |
  | 3+ | 691 | 0.842 | 0.070 | 0.619 | 1.396 |

- **Caption:** "Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean."
- **Notebook explanation (verbatim, `88cfc37f`):** "**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, separately for products with 1, 2 and 3 or more ratings. The raw mean is tied for almost all products (with one rating it takes only 7 values), so agreement is given as Kendall's τ-b and as the share of product pairs with different raw means that the GRM orders the other way round. The last two columns show how far apart the GRM scores of products with the same raw mean lie: products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination."
- **Direction (within this table):**
  - Kendall's τ-b: highest for 3+ (0.842), then 1 rating (0.832), lowest for 2 ratings (0.815).
  - Share of pairs in reversed order: lowest for 1 rating (0.042), then 2 (0.067) and 3+ (0.070).
  - Mean θ̂ range at equal raw mean: largest for 2 ratings (1.537), then 1 (1.283), smallest for 3+ (0.619).
  - Maximum θ̂ range at equal raw mean: largest for 2 ratings (2.196), then 1 (1.436) and 3+ (1.396).
  - Products sum to 3668 (897 + 2,080 + 691). This is computed from printed values; there is no pooled row.
- **Caveats:**
  - "The raw mean is tied for almost all products" is a notebook statement. The share of tied products is not printed.
  - The mechanism clause ("products with the same raw mean get different GRM scores when …") is not a tested result. Mark it for author confirmation if it is used.
  - The size of the equal-raw-mean groups and the number of pairs behind "Share of pairs in reversed order" are not printed.
  - No CIs are printed.
  - The notebook does not compare this table with `tbl-score-agreement` or `tbl-theta-correlations`.

**F2.10 Figure: GRM score against raw mean** *(unchanged; new cell ids)*
- **Linked object:** `fig-raw-mean-vs-theta` (N2, `0978db51`). Figure only, with no printed numbers.
- **Caption:** "GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally."
- **Notebook statement (`6de1a327`):** "The same comparison as a figure. Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal."

---

## Not found

These are absent from the notebooks. Do not invent them downstream.
- CIs for rel_post by number of ratings and for the per-n means (F1.14).
- CIs for the sensitivity differences (F2.8).
- CIs for the raw-mean vs GRM measures (F2.9).
- CIs or SEs for M1/M2 parameters and for the M1–M3 marginal and empirical reliabilities.
- Any global fit index other than the non-computable C2: no RMSEA, SRMSR or M2.
- **The definition of a "computable" Q3 pair (137 of 171).** The expected "at least 3 shared products" appears only in `R/02_grm.R` (`Q3_MIN_OVERLAP <- 3L`, plus non-zero residual SDs). NOT IN NOTEBOOK — not quotable.
- What "Overlap" in `tbl-grm-q3-flagged` means. In the R code it is "not computable" / "low overlap (unstable)" / empty, but that is context only.
- The full list of the 20 flagged Q3 pairs (the table shows 10).
- The number of unused end categories as a single printed figure. AUDIT.md says "6". That is NOT IN NOTEBOOK — not quotable.
- Numeric values for the figures (they are figures only): the full-panel information curve, rel_post by θ̂, the category response functions, the raw-mean-vs-θ̂ scatter, and the projection figure beyond its table.
- The latent θ̂ distribution (mean, SD) of products, and a single severity summary per rater.
- GRM rater parameters at 3 decimals, and rater-information CI bounds at 3 decimals.
- Infit/outfit misfit thresholds. The notebook explicitly applies none. The 0.7–1.3 range is in REPORT.md only: NOT IN NOTEBOOK — not quotable.
- A test of the trend of rel_post across n, or of the raw-mean agreement across n-groups.
- An ICC of any form.
- Per-rater uncertainty for the descriptive response-style indices.
- For F2.9 (raw mean vs GRM):
  - a pooled row;
  - correlations, percentile shifts and quintile measures;
  - the share of products with a tied raw mean;
  - the size of the equal-raw-mean groups;
  - the number of pairs behind "Share of pairs in reversed order".
- For F1.20 (projection):
  - selected rater sets (most or least informative);
  - `true_r2` (a header mapping exists in the code, but the column is not displayed);
  - quantiles of Mean rel_post;
  - k > 10;
  - parameter uncertainty in the projection;
  - the number of ratings needed for a target reliability (do not derive one).
- An M0 vs M1 severity test, a within-package M1 vs M2 LR test, a held-out predictive check, and diagnostics of the rejected parameter draws.
- The timespan of data collection, rater demographics and rater expertise.

**Possible extensions: context file only, NOT IN NOTEBOOK, not a result.** None of the three notebooks mentions possible extensions. ANALYSIS_TODO.md (context file) says, verbatim:

> "## Possible extensions (deliberately NOT in the paper, decision 2026-10-27)
> The paper sticks to the empirical findings of the actual rating study and keeps the analysis simple. Projections and what-if scenarios that need extra design choices are left out. Ideas that came up in the manuscript reviews and might be interesting later:
> - Projection with selected rater sets (e.g. the k most or least informative raters) or with rater draws weighted by each rater's workload. Such sets need to account for the uncertainty of the rater parameters (simulate from parameter draws), otherwise they favour raters with few ratings.
> - Number of ratings needed for a target reliability (.70, .80, .90) from the projection.
> - Severity test: model without any rater effect (M0) vs M1, to test rater severity on its own.
> - Likelihood-ratio test M1 vs M2 within one package (currently sirt vs mirt).
> - Held-out predictive check of the GRM against the adjacent-category models.
> - Diagnostics of the rejected parameter draws (which raters cause them)."

This is the author's planning note, not an analysis output. If the paper mentions future work, the wording is the author's to confirm.

**Resolved since the previous version:**
- Former Flag 5 (bootstrap-replication wording in the overview) is resolved: the overview now says "639 of 1000 replications computable, approximate".
- The SyntaxWarning in the N2 setup cell is gone.
- The `tbl-theta-correlations` caption now explains the check column.
- Model labels and single-code-name Quantity labels are now readable.

## Flags

1. **Pre-exclusion residue.** This is unchanged.
   - N0 is pre-exclusion, as expected. `tbl-cleaning-log` stops at 7844 and has no rater-exclusion row.
   - N1 is fully post-exclusion.
   - In N2, pre-exclusion values appear only where they are labelled as such: the "All raters" column of `tbl-sensitivity-rater-exclusion`, `tbl-excluded-raters`, and the raters excluded / duplicate rows of `tbl-design-summary`.
2. **`02_artifacts.md` is stale.**
   - It lists the old N2 cell ids (for example `tbl-design-summary` 29e46234, now `475838c2`; `tbl-grm-reliability-projection` 50451ca9, now `5fa6455c`).
   - It has the old projection caption ("… with randomly drawn raters of the panel.").
   - The results-embedder should be re-run.
3. **Privacy.**
   - No original rater IDs are printed.
   - N0 `520638b8` still contains the full Google Sheets URL, and the notebook says the sheet is shared as "anyone with the link".
   - N0 and N1 stdout print absolute local paths and action UUIDs. The UUIDs are not personal data.
4. **LR df wording vs AUDIT.** The notebook explains the mechanism (`97a578bb`) but does not print the count of unused end categories. Do not quote "6".
5. **Q3 "computable" is undefined in the notebook.** The threshold of at least 3 shared products is in the R code only (see F1.9). If the manuscript states it, it is either the writer's statement from a context file or it needs a notebook note added by the author.
6. **Parameter draws.** These are explained in `bef799a0`. `tbl-grm-rater-information-ci` does not show Draws, but its caption now says "200 accepted parameter draws".
7. **Display and formatting.**
   - Separators are mixed: N2 numeric cells use them (7,820). N1, N0, N2 text notes and N2 stdout do not (7820, 1000, 3668, 2000). Quote each value in the form printed at its source.
   - "Ratings (n)" means ratings per rater in most tables, but ratings per product in `tbl-grm-reliability-by-n` and `tbl-raw-mean-vs-grm`.
   - "Overlap" is "–" in every row of `tbl-grm-q3-flagged`.
   - In `tbl-theta-correlations`, the diagonal shows "1" while near-1 cells show "1.000".
   - Quantity labels that contained a space are still code names. Examples: "min_ratings_per_rater (exclusion cut-off)", "empirical_marginal_reliability (primary; actual scores)", "model_based_marginal_reliability_mirt (hypothetical full panel)".
   - The Q3 stdout still says "flag_q3".
   - The overview row labels use "M1 (RSM)", while the other tables use "M1 (RSM/MFRM)".
   - N1 `fb6df84b` prints counts as floats ("520.0").
   - Precision is mixed: 2 decimals for the GRM parameters and the information CIs, 3 decimals for most N2 tables, 5 decimals for the sensitivity table.
8. **Markdown order mismatches in N2 persist.**
   - The "Full panel" text (`710bd8d0`) is separated from `fig-grm-panel-information` (`bdeadff4`) by the information-CI block (`f2389ee8`, `67f02093`).
   - The "Reliability by number of ratings" text (`e321b693`) precedes the CI note (`bef799a0`) and `tbl-grm-reliability-ci`, not the by-n table (`1d4d6b6f`).
   - The M3 discrimination text (`43b1e0b3`) is separated from `tbl-discrimination-m3` (`c971e20c`) by `tbl-score-agreement`, `tbl-raw-mean-vs-grm`, `fig-raw-mean-vs-theta` and `tbl-sensitivity-rater-exclusion`.
9. **Unlabelled but cited sources.**
   - F0.4, F0.5 and F0.8 come from N1 `3b12b8bf`, `aa371443` and `fb6df84b`.
   - The mean Q3 line comes from N2 `5e8e7334`.
   - The projection settings come from N2 `71be63e4`.
   - These are quotable but cannot be embedded.
10. **Terminology.**
    - N1 and N2 say "products". The label `tbl-overview-ratings-per-action` still contains "action".
    - N0 uses "actions".
    - The N2 intro (`84ad0e04`) says "The rated products are the football actions".
11. **Stale reference.** The N0 intro markdown (`64b27fc9`, `73ef4dcd`) still refers to the deleted notebooks `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd`.
12. **Coinciding printed values.** "empirical_marginal_reliability (primary; actual scores)", "var theta eap" and "rel post mean" all print 0.672. This is reported as observed.
13. **Removed or no-longer-printed content that drafts may still quote.** The full list is in Changes item 12. Since this run, it also includes Tolerance "0.0001" and M3 ≥ 2 quintiles "0.000545256". Drafts written against the previous findings may contain these. Replace them with "10⁻⁴" and "0.001".
14. **Mechanism sentences in N2 markdown.** These are the notebook's framing, not results. Mark them for author confirmation if they are used:
    - `88cfc37f` ("products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination");
    - `43b1e0b3` ("Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data");
    - `cbe35366` ("High values mean the ranking of products hardly depends on the model");
    - `ce0f3bbd` ("A simple gauge of the value of adding ratings").
15. **Projection vs observed reliability (F1.20 vs F1.14).**
    - The projection simulates θ ~ N(0, 1) with randomly drawn raters ("each equally likely") and parameters treated as known.
    - The observed table uses the actual products and raters.
    - The notebook makes no numeric comparison. Any side-by-side statement (for example projected k = 2 Mean rel_post 0.690 vs observed n = 2 0.698) would be the writer's juxtaposition.

---

Files read:
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb` (all Markdown outputs checked in the raw JSON)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/R/02_grm.R` (context only: Q3 threshold)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/AUDIT.md` (context only)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/03_findings.md` (previous version)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/02_artifacts.md` (staleness check only)