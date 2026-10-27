> **Orchestrator note (2026-10-26, re-run after commit 91c2e6d).** The interpreter's output below is copied byte for byte. `02_artifacts.md` was regenerated in parallel (42 labels, incl. tbl-grm-reliability-projection and fig-grm-reliability-projection), so any flag calling it stale is resolved.
> Values marked NOT IN NOTEBOOK must not be quoted. Per the notebook, the plain share_products_changing_quintile in tbl-raw-mean-vs-grm overstates disagreement and must not be compared with tbl-score-agreement.

# 03_findings.md: Results findings (results-interpreter, Phase 4 re-run after commit 91c2e6d)

## Changes vs previous findings

1. **N2 values outside the changed objects are unchanged.** I compared every value in the stored N2 outputs with the previous file, not just a sample. All values match byte for byte in these tables:
   - tbl-design-summary, tbl-excluded-raters, tbl-category-usage, tbl-grm-convergence;
   - tbl-grm-rater-fit, tbl-grm-q3-flagged (and the mean-Q3 stdout), tbl-grm-global-fit;
   - tbl-grm-information-summary, tbl-grm-rater-information-ci;
   - tbl-grm-reliability-summary, tbl-grm-reliability-ci, tbl-grm-reliability-by-n;
   - tbl-model-fit, tbl-lr-tests, tbl-theta-correlations, tbl-score-agreement;
   - tbl-sensitivity-rater-exclusion, tbl-discrimination-m3, tbl-threshold-order, tbl-rater-fit-m1;
   - tbl-marginal-reliability-models, tbl-naive-indices, tbl-reliability-overview.

   In tbl-raw-mean-vs-grm, the 11 columns that were there before are also unchanged (item 4).
2. **N0 and N1 are unchanged.** The cell ids are the same. Spot checks of the printed values all match: `f6039400`, `981d6824`, `bacf60d8`, `9f03e286`, `ovtbl01`, the `fb6df84b` rows, and N0 `72468670` / `dd37b3ec`.
3. **All N2 cell ids have changed again.** The new ids are given in each finding below. Every markdown note quoted in this file has a new id, and its text is unchanged except for `a045a080` (item 5) and `8620cb46` (item 4).
4. **F2.9 / `tbl-raw-mean-vs-grm` (REVISED).**
   - The table now has 15 columns. The 4 new tie-aware columns are share_products_changing_quintile_ties_resolved, share_discordant_pairs, kendall_tau_b and share_products_with_tied_raw_mean.
   - The note `8620cb46` gained a second paragraph. It says that share_products_changing_quintile "overstates the disagreement and is not comparable with the model comparison above."
   - **I removed the previous cross-table comparison of 0.350 with `tbl-score-agreement` (M1 0.202, M2 0.150, M3 0.075).** The notebook's statement on comparability is recorded instead.
   - The previous FI-20 point is only partly resolved. The notebook now defines the tie-aware columns. It still does not say how equal-raw-mean groups are formed in the pooled "all" row, or whether percentiles and quintiles in the 1 / 2 / 3+ rows are computed within each subgroup (see Not found).
5. **F2.1 / F2.2 / `tbl-grm-rater-parameters` (REVISED format).**
   - The table now prints "estimate (SE)" at **2 decimals** and no longer has a category_boundaries column.
   - **The previous 3-decimal values (e.g., a = 3.709, b1 = -6.565) are no longer printed anywhere and must not be quoted.**
   - Every 2-decimal cell agrees with the previous 3-decimal value after rounding. A few cells ending in 5 at the third decimal round down rather than up (e.g., R06 b1 0.295 → 0.29; R15 a SE 0.525 → 0.52). This is consistent with rounding the full-precision source values, so it is not a data change.
   - The pattern of missing thresholds is unchanged: R01, R03, R06 and R18 have no b6; R17 has no b5 or b6.
   - The note (`a045a080`) now defines b_k differently and adds a sentence on internal gaps. The caption now explains the dash.
6. **NEW F1.20.** `tbl-grm-reliability-projection` (`2ea36634`), `fig-grm-reliability-projection` (`40072a98`), method note `94cdcfeb` and the stdout of the unlabelled cell `368bd615`.
7. **F1.14: notebook caveat added.** The new note `94cdcfeb` calls the observed relation in `tbl-grm-reliability-by-n` "confounded" (quoted under F1.14 and F1.20).
8. **New flags:**
   - `02_artifacts.md` is stale again. It has the old ids (e.g., `df7c3ef8` and `05caf58b`) and lacks the two projection labels.
   - The `tbl-raw-mean-vs-grm` caption does not mention the tie-aware columns.
   - The confounding sentence in `94cdcfeb` is notebook framing, not a tested result.

---

Notebooks used (the only quotable sources):
- **N0** = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- **N1** = `.../notebooks/01_data_overview.ipynb`
- **N2** = `.../notebooks/02_jrt_results.ipynb` (main)

How to read this file:
- **Values** are copied exactly as printed in the stored outputs.
- **N2 formatting.** N2 tables go through `tidy()`:
  - 3 decimals, except `tbl-sensitivity-rater-exclusion`, which has 5;
  - `tbl-grm-rater-parameters` is preformatted by `est_se()` at 2 decimals;
  - whole numbers have no decimals;
  - p-values below .001 are in scientific notation;
  - missing values show as "–".
- **N1 formatting.** N1 `fb6df84b` prints at 3 decimals, and its counts print as floats ("520.0").
- **Context files.** AUDIT.md and REPORT.md were read for definitions only. Any value that appears only there is marked **NOT IN NOTEBOOK — not quotable**.

**Post-exclusion check.** N1 and N2 both report the final data: 7820 ratings, 3668 products and 19 raters.
- N1 `f6039400` stdout: "Loaded 7844 ratings; excluded 24 ratings from 3 raters with fewer than 15 ratings (R20, R21, R22); 7820 ratings remain."
- N1 `981d6824`: Total ratings 7820; Distinct products 3668; Distinct raters 19.
- N2 `tbl-design-summary`: n_ratings 7820, n_products 3668, n_raters 19.
- N0 is pre-exclusion, as expected: 22 raters, 7844 rows, 3669 actions.

---

## (a) Descriptives and design

**F0.1 Raw data and cleaning (pre-exclusion, N0)** *(unchanged)*
- **Finding:** The sheet export had 9148 rows. After cleaning, 7844 rows remained, from 22 raters and 3669 actions.
- **Linked object:** `tbl-cleaning-log` (N0, cell `bbcbf730`). Supporting stdout is in `520638b8`, `fb9eaf36`, `793192b4`, `72468670` and `dd37b3ec`.
- **Numbers:**

  | step | rows before | rows after | rows affected |
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

**F0.2 Rater exclusion** *(unchanged; new cell ids)*
- **Finding:** Three raters with fewer than 15 ratings were excluded. Together they gave 24 ratings, and their exclusion dropped 1 product.
- **Linked object:** `tbl-excluded-raters` (N2, `dd078799`) and `tbl-design-summary` (N2, `58e32d41`).
- **Numbers:**
  - Ratings per excluded rater: R20 13, R21 9, R22 2. The reason given for each is "fewer than 15 ratings".
  - From the design summary: min_ratings_per_rater (exclusion cut-off) 15; raters_excluded R20;R21;R22; ratings_excluded 24; products_dropped 1.

**F0.3 Final design** *(unchanged; new N2 cell id)*
- **Finding:** The final design has 7820 ratings of 3668 products by 19 raters. It is sparse but forms one connected component.
- **Linked object:** `tbl-design-summary` (N2, `58e32d41`). The same numbers appear in `tbl-overview-ratings-per-action` (N1, `ovtbl01`) and in N1 `981d6824` and `bacf60d8`.
- **Numbers (N2):**
  - n_categories 7; scale 1-7; internal_coding rating - 1 (0-6).
  - ratings_per_product: mean 2.132, median 2, min 1, max 10, harmonic_mean 1.726.
  - products_with_1_rating 897.
  - ratings_per_rater: min 50, max 1174.
  - matrix_fill 0.112; n_components 1.
  - Rater pairs: total 171, without overlap 17, median overlap 13.
  - raters_with_category_gaps 5; raters_with_internal_gap 0.
  - duplicate_pairs_resolved_in_00 12; duplicate_pairs_conflicting 1.
- **Numbers (N1 `ovtbl01`):**
  - n_ratings 7820; n_products 3668; n_raters 19.
  - n_products_1_rating 897; n_products_2_ratings 2080; n_products_3plus_ratings 691.
  - share_products_1_rating 0.245; share_products_2_ratings 0.567; share_products_3plus_ratings 0.188.
  - max_ratings_per_product 10; mean_ratings_per_product 2.132; harmonic_mean_ratings_per_product 1.726.
  - median_ratings_per_rater 383; min_ratings_per_rater 50; max_ratings_per_rater 1174.
  - N1 `981d6824`: "Average ratings per product: 2.13"; "Average ratings per rater: 411.6".
  - N1 `bacf60d8`: "Number of connected components: 1"; the component has 3668 products and 19 raters.
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

**F0.7 Category use per rater** *(unchanged; new cell ids)*
- **Finding:** Five raters left at least one category unused, always at the top end of the scale. No rater has an internal gap.
- **Linked object:** `tbl-category-usage` (N2, `2483aa59`).
- **Numbers:**
  - Unused categories (missing_categories): R01 7; R03 7; R06 7; R17 6;7; R18 7. All other raters show "–".
  - internal_gap is False for all 19 raters.
  - Full counts per category, cat_1 to cat_7:

    | rater | cat_1 | cat_2 | cat_3 | cat_4 | cat_5 | cat_6 | cat_7 | n |
    |---|---|---|---|---|---|---|---|---|
    | R01 | 337 | 461 | 259 | 87 | 24 | 6 | 0 | 1174 |
    | R02 | 241 | 179 | 124 | 126 | 91 | 67 | 45 | 873 |
    | R03 | 161 | 182 | 185 | 82 | 88 | 22 | 0 | 720 |
    | R04 | 164 | 164 | 90 | 69 | 92 | 36 | 5 | 620 |
    | R05 | 159 | 190 | 102 | 90 | 50 | 30 | 12 | 633 |
    | R06 | 301 | 113 | 57 | 34 | 9 | 6 | 0 | 520 |
    | R07 | 183 | 152 | 96 | 61 | 36 | 17 | 2 | 547 |
    | R08 | 101 | 127 | 106 | 91 | 60 | 30 | 7 | 522 |
    | R09 | 63 | 62 | 72 | 60 | 66 | 55 | 22 | 400 |
    | R10 | 25 | 156 | 76 | 64 | 47 | 13 | 2 | 383 |
    | R11 | 127 | 118 | 51 | 31 | 32 | 9 | 1 | 369 |
    | R12 | 11 | 48 | 90 | 77 | 27 | 10 | 1 | 264 |
    | R13 | 4 | 35 | 68 | 91 | 44 | 11 | 1 | 254 |
    | R14 | 105 | 66 | 40 | 31 | 10 | 5 | 2 | 259 |
    | R15 | 7 | 22 | 11 | 9 | 13 | 9 | 2 | 73 |
    | R16 | 4 | 14 | 9 | 14 | 5 | 3 | 3 | 52 |
    | R17 | 25 | 10 | 9 | 4 | 4 | 0 | 0 | 52 |
    | R18 | 1 | 8 | 14 | 12 | 16 | 4 | 0 | 55 |
    | R19 | 10 | 6 | 8 | 6 | 10 | 6 | 4 | 50 |

- **Caveat (notebook, `8a34fd81`):** "Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used."

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
- **Definitions (notebook, `f3482d97` / `fb6df84b` code):**
  - extreme categories are 1 and 7; middle categories are 3–5;
  - floor = share of ratings equal to 1; ceiling = share equal to 7;
  - entropy is computed with natural logarithms.
  - The markdown in `f3482d97` says these descriptives "anticipate what the models estimate formally". That is the notebook's own framing.
- **Caveats:**
  - The cell is unlabelled, so the table cannot be embedded.
  - The values are on the raw 1–7 scale and are not adjusted for which products each rater saw.
  - Counts print as floats ("520.0").
  - N1 `9f03e286` prints "Raters with <= 2 rated products: 0".
  - Earlier 6-decimal values are not printed. Do not quote them.

## (b) Model comparison

**F1.1 Information criteria** *(unchanged; new cell ids)*
- **Finding:** The GRM has the lowest AIC, BIC and SABIC of the four estimated models. Among the adjacent-category models, M3 has the lowest AIC and SABIC, and M2 has the lowest BIC.
- **Linked object:** `tbl-model-fit` (N2, `041cba7a`).
- **Numbers:**

  | model | software | family | logLik | npar | AIC | BIC | SABIC | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|---|---|---|---|---|---|---|
  | M1_RSM | sirt::rm.facets | adjacent category | -12186.218 | 25 | 24422.435 | 24577.620 | 24498.183 | 701.980 | 68.825 | 392.931 |
  | M2_PCM | mirt | adjacent category | -11817.489 | 109 | 23852.978 | 24529.585 | 24183.237 | 132.524 | 20.790 | 77.985 |
  | M3_GPCM | mirt | adjacent category | -11756.510 | 127 | 23767.020 | 24555.360 | 24151.817 | 46.566 | 46.566 | 46.566 |
  | GRM | mirt | cumulative (not in LR ladder) | -11733.227 | 127 | 23720.455 | 24508.795 | 24105.251 | 0 | 0 | 0 |

- **Caveat (notebook, `18bef255`):** "The GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better)."

**F1.2 Likelihood-ratio tests** *(unchanged; new cell ids)*
- **Finding:** Both steps up the adjacent-category ladder give significant LR tests.
- **Linked object:** `tbl-lr-tests` (N2, `b3034a4d`).
- **Numbers:**
  - M1 vs M2 (rater-specific thresholds): X2 737.457, df 84, df_expected_formula 90, df_matches_formula False, p 4.22e-105.
  - M2 vs M3 (rater-specific discriminations): X2 121.958, df 18, df_expected_formula 18, df_matches_formula True, p 1.79e-17.
- **Notebook explanation (verbatim, `74a1629a`):** "df_expected_formula is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories."
- **Caveats:**
  - The notebook does not print the number of unused end categories as a single figure. The unused categories are listed per rater in `tbl-category-usage` (F0.7).
  - AUDIT.md's statement "6 unused end categories" is NOT IN NOTEBOOK — not quotable as a printed value.

**F1.3 GRM estimation** *(unchanged; new cell id)*
- **Finding:** The GRM converged, and its information matrix is positive definite.
- **Linked object:** `tbl-grm-convergence` (N2, `3f6972c2`).
- **Numbers:**
  - method EM; quadpts 61; se_type Oakes; tol 0.000 (display artifact).
  - converged True; iterations 165; information_matrix_pd True.
  - logLik -11733.227; npar 127; AIC 23720.455; BIC 24508.795; SABIC 24105.251.
  - n_products 3668; n_ratings 7820.

**F1.4 Discriminations in M3 (GPCM)** *(unchanged; new cell ids)*
- **Finding:** Rater discriminations in M3 range from 0.283 (R09) to 2.606 (R16).
- **Linked object:** `tbl-discrimination-m3` (N2, `91d95b1b`).
- **Numbers** (rater, n, estimate (se), in the printed order): R09 400 0.283 (0.055); R18 55 0.312 (0.145); R17 52 0.616 (0.235); R13 254 0.863 (0.159); R11 369 0.896 (0.145); R03 720 0.984 (0.142); R04 620 0.992 (0.184); R07 547 1.025 (0.138); R05 633 1.096 (0.154); R08 522 1.102 (0.195); R02 873 1.209 (0.272); R01 1174 1.304 (0.131); R10 383 1.370 (0.320); R15 73 1.389 (0.412); R14 259 1.390 (0.433); R06 520 1.942 (0.385); R19 50 2.327 (1.866); R12 264 2.383 (0.680); R16 52 2.606 (1.419).
- **Caveats:**
  - The largest SEs belong to raters with about 50 ratings: R19 1.866 and R16 1.419.
  - Notebook (`a47f5ab0`): "Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data."

**F1.5 Unordered step parameters in M2/M3** *(unchanged; new cell ids)*
- **Finding:** Nine raters have unordered steps in M2 (PCM), and nine raters do in M3 (GPCM).
- **Linked object:** `tbl-threshold-order` (N2, `7b051cef`).
- **Numbers (rater, n_steps, n_reversals, steps):**
  - M2_PCM:
    - R03 5, 1, -0.87;-0.21;1.11;0.69;2.64
    - R04 6, 1, -0.54;0.58;0.68;0.52;2.18;3.77
    - R05 6, 1, -0.74;0.62;0.58;1.46;1.81;2.72
    - R06 5, 1, 0.92;1.26;1.60;2.85;2.38
    - R11 6, 1, -0.36;0.96;1.06;0.93;2.65;4.15
    - R15 6, 2, -2.18;0.35;0.35;0.15;1.29;3.12
    - R16 6, 1, -2.09;0.18;-0.19;1.81;1.87;1.99
    - R17 4, 2, 0.49;0.18;1.30;0.98
    - R19 6, 2, -0.43;-0.85;0.10;-0.29;1.21;1.76
  - M3_GPCM:
    - R03 5, 1, -0.82;-0.19;1.11;0.65;2.59
    - R04 6, 1, -0.53;0.58;0.66;0.48;2.13;3.69
    - R05 6, 1, -0.69;0.57;0.56;1.38;1.72;2.57
    - R06 5, 1, 0.51;1.06;1.46;2.30;2.27
    - R09 6, 2, -0.43;-0.78;0.63;-0.12;1.10;3.92
    - R11 6, 1, -0.29;1.09;1.14;0.94;2.78;4.31
    - R15 6, 1, -1.90;0.21;0.34;0.28;1.20;2.81
    - R17 4, 2, 1.12;0.22;1.74;0.83
    - R18 5, 1, -7.29;-2.14;0.42;-0.70;5.02
- **Caveat (notebook, `30fd6005`):** "In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction."

**F1.6 Marginal and empirical reliability by model** *(unchanged; new cell ids)*
- **Linked object:** `tbl-marginal-reliability-models` (N2, `f76232d2`).
- **Numbers:**

  | model | latent_variance | marginal_reliability | marginal_rxx_mirt | empirical_rxx |
  |---|---|---|---|---|
  | M1_RSM | 0.962 | 0.943 | – | 0.626 |
  | M2_PCM | 1.087 | 0.944 | – | 0.637 |
  | M3_GPCM | 1 | 0.955 | 0.955 | 0.657 |
  | GRM | 1 | 0.960 | 0.960 | 0.672 |

- **Direction:** Both the marginal and the empirical reliability increase in the order M1 < M2 < M3 < GRM.
- **Caveat (notebook, `6be3f4c1`):** "Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model."

## (c) Fit evidence and its stated limitations

**F1.7 GRM rater infit/outfit** *(unchanged; new cell ids)*
- **Finding:** Under the GRM, every rater's infit and outfit is below 1. Infit ranges from 0.334 (R19) to 0.971 (R18), and outfit from 0.322 (R19) to 0.961 (R18).
- **Linked object:** `tbl-grm-rater-fit` (N2, `56dabacd`).
- **Numbers (infit / outfit):** R01 0.680/0.650; R02 0.450/0.423; R03 0.699/0.687; R04 0.588/0.554; R05 0.617/0.576; R06 0.604/0.469; R07 0.724/0.645; R08 0.585/0.571; R09 0.871/0.870; R10 0.624/0.603; R11 0.829/0.784; R12 0.507/0.505; R13 0.831/0.834; R14 0.483/0.398; R15 0.754/0.663; R16 0.508/0.480; R17 0.926/0.824; R18 0.971/0.961; R19 0.334/0.322.
- **Caveats (notebook, `7a2e0da9`, verbatim):**
  - "Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982)."
  - "With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked."
  - "No misfit cut-offs for infit and outfit are applied in this notebook."

**F1.8 S-X² (multiple imputation)** *(unchanged; new cell ids)*
- **Finding:** All S-X² p-values lie between 0.294 (R12) and 0.671 (R02).
- **Linked object:** `tbl-grm-rater-fit` (N2, `56dabacd`).
- **Numbers** (S_X2 / df_S_X2 / p_S_X2; n_imputations is 20 for every rater): R01 218.569/213.550/0.392; R02 289.502/300.850/0.671; R03 277.954/280.450/0.531; R04 280.793/290.200/0.643; R05 291.511/293.850/0.528; R06 193.853/190.100/0.411; R07 282.598/285.850/0.543; R08 282.277/285/0.534; R09 440.411/433.550/0.400; R10 247.751/250.600/0.539; R11 298.249/295.100/0.438; R12 207.049/196.800/0.294; R13 263.892/264.200/0.494; R14 224.935/234.450/0.661; R15 265.749/260.900/0.405; R16 200.549/205.150/0.578; R17 279.802/280.350/0.498; R18 342.054/335.700/0.394; R19 223.516/228.400/0.579.
- **Caveat (notebook, `7a2e0da9`):** "S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative."

**F1.9 Local dependence (Q3)** *(unchanged; new cell ids)*
- **Finding:** The mean Q3 over 137 computable rater pairs is -0.238, and 20 pairs are flagged. The table shows the ten pairs with the largest |Q3 − mean Q3| among pairs with at least 30 shared products. Nine of them deviate negatively and one, R10–R11, positively. All ten have flag_q3 True.
- **Linked object:** `tbl-grm-q3-flagged` (N2, `10d62633`). The summary line comes from unlabelled N2 cell `be50ab41` (stdout).
- **Numbers:**
  - `be50ab41` stdout, verbatim: "Mean Q3 over 137 computable rater pairs: -0.238; pairs flagged (flag_q3): 20".
  - The ten pairs:

    | pair | n_common | q3 | q3_minus_mean | overlap_flag | flag_q3 |
    |---|---|---|---|---|---|
    | R08–R19 | 46 | -0.761 | -0.524 | – | True |
    | R08–R12 | 51 | -0.743 | -0.506 | – | True |
    | R02–R14 | 108 | -0.621 | -0.383 | – | True |
    | R03–R10 | 49 | -0.616 | -0.379 | – | True |
    | R01–R10 | 157 | -0.613 | -0.376 | – | True |
    | R02–R04 | 257 | -0.611 | -0.373 | – | True |
    | R02–R08 | 72 | -0.589 | -0.352 | – | True |
    | R10–R11 | 32 | 0.105 | 0.343 | – | True |
    | R01–R08 | 191 | -0.565 | -0.327 | – | True |
    | R04–R14 | 47 | -0.560 | -0.322 | – | True |

- **Notebook explanation (verbatim, `67657dc2`):** "Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). flag_q3 marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2."
- **Caveats:**
  - The table shows only 10 of the 20 flagged pairs.
  - overlap_flag is "–" in every row, and the notebook does not define it.
  - The notebook does not define what makes a pair "computable" (137 of 171 pairs).

**F1.10 Global fit (C2)** *(unchanged; new cell ids)*
- **Finding:** C2 was not computable, because 17 of 171 rater pairs share no products.
- **Linked object:** `tbl-grm-global-fit` (N2, `d525daa8`).
- **Numbers:** statistic C2; computable False; rater_pairs 171; rater_pairs_without_overlap 17. The note reads: "Not computable: 17 of 171 rater pairs share no products, so their bivariate moments and hence C2 are undefined."
- **Notebook explanation (verbatim, `0ef27132`):** "C2 is a limited-information test of overall model fit (Cai & Monroe, 2014). The table reports either the statistic or the reason it could not be computed: C2 needs the joint distribution of every pair of raters, which is undefined for rater pairs that share no products."
- **Caveat:** The notebook reports no other global fit index.

**F1.11 M1 (MFRM) rater fit** *(unchanged; new cell ids)*
- **Finding:** Under M1, R17 (infit 1.328, outfit 1.190) and R18 (infit 1.009, outfit 1.071) are the only raters with values at or above 1. All other raters are below 1. R12 has the lowest values: infit 0.238, outfit 0.255.
- **Linked object:** `tbl-rater-fit-m1` (N2, `1f422649`).
- **Numbers (infit / outfit):** R01 0.466/0.481; R02 0.786/0.782; R03 0.579/0.579; R04 0.687/0.660; R05 0.701/0.669; R06 0.909/0.705; R07 0.826/0.751; R08 0.540/0.548; R09 0.978/0.958; R10 0.407/0.389; R11 0.938/0.874; R12 0.238/0.255; R13 0.405/0.406; R14 0.747/0.695; R15 0.753/0.698; R16 0.452/0.457; R17 1.328/1.190; R18 1.009/1.071; R19 0.654/0.701.
- **Caveats:**
  - `7a2e0da9`: "No misfit cut-offs for infit and outfit are applied in this notebook."
  - `eca6f27a`: these are "the fit statistics usually reported for many-facet Rasch models (Eckes, 2015)."
  - REPORT.md uses 0.7–1.3. This range is NOT IN NOTEBOOK — not quotable.

## (d) Reliability, including by number of ratings and CIs

**F1.12 Marginal reliabilities with 95% intervals** *(unchanged; new cell ids)*
- **Finding:** The empirical marginal reliability of the actual GRM scores is 0.672 [0.649, 0.687]. The model-based marginal reliability for the hypothetical full panel is 0.960 [0.953, 0.968].
- **Linked object:** `tbl-grm-reliability-ci` (N2, `2de37f81`). The same values appear in `tbl-grm-reliability-summary` (`05a28f9c`) and `tbl-reliability-overview` (`d78d2f68`).
- **Numbers:**
  - empirical_marginal_reliability: 0.672, ci_low 0.649, ci_high 0.687, n_draws 200, n_draws_rejected 87.
  - model_based_marginal_reliability: 0.960, ci_low 0.953, ci_high 0.968, n_draws 200, n_draws_rejected 87.
  - Summary table: model_based_marginal_reliability_grid (check) 0.960; var_theta_eap 0.672; mean_psd_squared 0.328.
  - Overview table, verbatim: "95% CI [0.649, 0.687] (200 parameter draws); Var(theta)/(Var(theta)+mean(PSD^2))" and "95% CI [0.953, 0.968] (200 parameter draws); mirt::marginal_rxx, all raters".
- **Notebook explanation (verbatim, `fdb7c615`):** "95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. n_draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; n_draws_rejected counts these."
- **Caveat (notebook, `c60e7cdd`):** the empirical value "refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure". The model-based value "refers to the hypothetical full panel".

**F1.13 Distribution of product-level reliability rel_post** *(unchanged; new cell ids)*
- **Finding:** Product-level reliability rel_post = 1 − PSD² has a median of 0.698 and ranges from 0.057 to 0.929.
- **Linked object:** `tbl-grm-reliability-summary` (N2, `05a28f9c`) and `fig-grm-rel-post-histogram` (`0a74217e`).
- **Numbers:** rel_post_min 0.057; p10 0.485; q1 0.596; median 0.698; q3 0.769; p90 0.813; max 0.929; mean 0.672; iqr 0.173.

**F1.14 Reliability by number of ratings per product (observed)** *(values unchanged; new cell ids; notebook caveat added)*
- **Finding:** Mean rel_post rises steadily from 0.520 for products with 1 rating to 0.919 for products with 10 ratings. Mean PSD falls from 0.686 to 0.285.
- **Linked object:** `tbl-grm-reliability-by-n` (N2, `69e27411`) and `fig-grm-rel-post-by-n` (`2e3801ac`).
- **Numbers:**

  | n_ratings | n_products | rel_post_mean | rel_post_median | rel_info_mean | psd_mean |
  |---|---|---|---|---|---|
  | 1 | 897 | 0.520 | 0.553 | 0.544 | 0.686 |
  | 2 | 2080 | 0.698 | 0.714 | 0.713 | 0.545 |
  | 3 | 357 | 0.757 | 0.768 | 0.767 | 0.488 |
  | 4 | 125 | 0.810 | 0.826 | 0.818 | 0.430 |
  | 5 | 125 | 0.820 | 0.831 | 0.831 | 0.420 |
  | 6 | 47 | 0.847 | 0.856 | 0.851 | 0.387 |
  | 7 | 20 | 0.869 | 0.880 | 0.874 | 0.358 |
  | 8 | 11 | 0.875 | 0.885 | 0.879 | 0.347 |
  | 9 | 3 | 0.879 | 0.920 | 0.883 | 0.338 |
  | 10 | 3 | 0.919 | 0.920 | 0.917 | 0.285 |

- **Caveats:**
  - The 9- and 10-rating rows rest on 3 products each.
  - No CIs are printed.
  - No n reaches the model-based full-panel value of 0.960.
  - NEW, notebook (`94cdcfeb`, verbatim): "The observed relation above is confounded, because products with more ratings were also rated by different raters." This is the notebook's framing, not a tested result. Mark it for author confirmation if it is used.

**F1.15 Full-panel (hypothetical) information and reliability** *(unchanged; new cell ids)*
- **Linked object:** `fig-grm-panel-information` (N2, `8f5ffbd6`).
- **Numbers:** None are printed beyond the model-based value of 0.960 (F1.12).
- **Caveats:**
  - Notebook (`5ef1f60a`): "This is a hypothetical upper bound, not the precision of the actual scores."
  - Caption: "it applies to a product rated by all raters."

**F1.16 Consistency of rel_post and rel_info** *(unchanged; new cell ids)*
- **Finding:** The two product-level reliability measures correlate at 0.935. Mean rel_info − rel_post is 0.016, and 320 products differ by more than 0.1.
- **Linked object:** `tbl-grm-reliability-summary` (N2, `05a28f9c`) and `fig-grm-rel-consistency` (`5d51fe9a`).
- **Numbers:** consistency_cor_rel_post_rel_info 0.935; consistency_mean_diff_rel_info_minus_rel_post 0.016; consistency_max_abs_diff 0.413; products_abs_diff_gt_0.1 320.
- **Notebook statement (`c356e58c`):** "Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree."

**F1.17 rel_post by θ̂** *(unchanged; new cell ids)*
- **Linked object:** `fig-grm-rel-post-by-theta` (N2, `9186727e`). Figure only, with no printed numbers.
- **Notebook statement (`617521d7`):** "Precision depends on where a product lies relative to its raters' thresholds."

**F1.18 Naive indices with bootstrap CIs** *(unchanged; new cell ids)*
- **Finding:** The pairwise-covariance Cronbach's α is 0.928, the fully crossed-block Cronbach's α is 0.658, and Krippendorff's ordinal α is 0.392. For the pairwise Cronbach's α, 361 of 1000 bootstrap replications failed.
- **Linked object:** `tbl-naive-indices` (N2, `ff18cda5`) and `tbl-reliability-overview` (`d78d2f68`).
- **Numbers:**

  | index | value | ci_low | ci_high | n_raters | n_products | n_boot | n_boot_failed |
  |---|---|---|---|---|---|---|---|
  | Cronbach's alpha: pairwise covariances, all usable raters | 0.928 | 0.891 | 0.943 | 14 | 1900 | 1000 | 361 |
  | Cronbach's alpha: fully crossed block (listwise complete) | 0.658 | 0.526 | 0.756 | 3 | 139 | 1000 | 0 |
  | Krippendorff's alpha (ordinal) | 0.392 | 0.362 | 0.417 | 19 | 2771 | 1000 | 0 |

  The overview table's ci_or_note column reads:
  - Krippendorff: "95% bootstrap CI [0.362, 0.417], 1000 replications"
  - Pairwise Cronbach: "95% CI [0.891, 0.943] (bootstrap, 1000 replications); 14 raters; removed: R19;R14;R02;R16;R12"
  - Crossed block: "95% CI [0.526, 0.756] (bootstrap, 1000 replications); 3 raters, 139 products"
- **Notebook notes (verbatim, `3f17a200`):**
  - "Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (n_boot_failed in the table)."
  - Naive indices "are reference values for common practice. They are not used downstream."
  - Cronbach's α "assumes τ-equivalent raters and complete data".
  - Krippendorff's α "measures the agreement of single ratings, treating raters as interchangeable".

**F1.19 Overview of indices and what each refers to** *(unchanged; new cell ids)*
- **Linked object:** `tbl-reliability-overview` (N2, `d78d2f68`).
- **Numbers:** These repeat F1.12, F1.13, F1.6 and F1.18:
  - GRM median rel_post 0.698 (ci_or_note "Q1 0.596, Q3 0.769"); IQR rel_post 0.173.
  - Marginal reliability: M1 0.943, M2 0.944, M3 0.955.
- **Notebook statement (`55f46636`):** "They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable."

**F1.20 Projected reliability by number of ratings per product (simulation from the fitted GRM)** *(NEW)*
- **Finding:** In the simulation, the projected empirical marginal reliability rises with k (ratings per product) for all three rater schemes:
  - random raters: 0.508 at k = 1 to 0.925 at k = 10;
  - the k most informative raters: 0.754 to 0.947;
  - the k least informative raters: 0.108 to 0.884.
- **Linked object:**
  - `tbl-grm-reliability-projection` (N2, `2ea36634`);
  - `fig-grm-reliability-projection` (N2, `40072a98`);
  - simulation settings from the stdout of the unlabelled N2 cell `368bd615`;
  - method note in `94cdcfeb`.
- **Numbers (exactly as printed; the n_products_per_rep, n_reps and seed columns are dropped from the display):**

  | scheme | k | empirical | empirical_q025 | empirical_q975 | true_r2 | true_r2_q025 | true_r2_q975 | mean_rel_post | mean_rel_post_q025 | mean_rel_post_q975 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | random | 1 | 0.508 | 0.495 | 0.522 | 0.508 | 0.480 | 0.542 | 0.508 | 0.500 | 0.517 |
  | random | 2 | 0.688 | 0.676 | 0.698 | 0.688 | 0.668 | 0.710 | 0.690 | 0.686 | 0.697 |
  | random | 3 | 0.775 | 0.764 | 0.784 | 0.773 | 0.751 | 0.789 | 0.776 | 0.772 | 0.779 |
  | random | 4 | 0.826 | 0.817 | 0.832 | 0.825 | 0.810 | 0.836 | 0.826 | 0.823 | 0.827 |
  | random | 5 | 0.857 | 0.850 | 0.864 | 0.857 | 0.848 | 0.868 | 0.857 | 0.856 | 0.859 |
  | random | 6 | 0.880 | 0.872 | 0.884 | 0.880 | 0.872 | 0.887 | 0.879 | 0.878 | 0.881 |
  | random | 7 | 0.896 | 0.891 | 0.901 | 0.896 | 0.889 | 0.903 | 0.896 | 0.894 | 0.897 |
  | random | 8 | 0.908 | 0.903 | 0.911 | 0.908 | 0.898 | 0.913 | 0.908 | 0.906 | 0.909 |
  | random | 9 | 0.918 | 0.914 | 0.921 | 0.918 | 0.912 | 0.924 | 0.918 | 0.917 | 0.919 |
  | random | 10 | 0.925 | 0.922 | 0.929 | 0.926 | 0.920 | 0.932 | 0.926 | 0.924 | 0.927 |
  | most_informative | 1 | 0.754 | 0.746 | 0.761 | 0.755 | 0.740 | 0.773 | 0.754 | 0.751 | 0.757 |
  | most_informative | 2 | 0.859 | 0.854 | 0.862 | 0.859 | 0.850 | 0.868 | 0.859 | 0.857 | 0.861 |
  | most_informative | 3 | 0.892 | 0.887 | 0.898 | 0.892 | 0.884 | 0.899 | 0.892 | 0.891 | 0.894 |
  | most_informative | 4 | 0.907 | 0.902 | 0.911 | 0.906 | 0.900 | 0.913 | 0.907 | 0.905 | 0.908 |
  | most_informative | 5 | 0.920 | 0.917 | 0.922 | 0.920 | 0.914 | 0.925 | 0.919 | 0.918 | 0.921 |
  | most_informative | 6 | 0.928 | 0.925 | 0.930 | 0.928 | 0.923 | 0.933 | 0.928 | 0.927 | 0.929 |
  | most_informative | 7 | 0.933 | 0.930 | 0.936 | 0.933 | 0.928 | 0.938 | 0.933 | 0.932 | 0.934 |
  | most_informative | 8 | 0.938 | 0.935 | 0.941 | 0.938 | 0.933 | 0.942 | 0.938 | 0.937 | 0.939 |
  | most_informative | 9 | 0.943 | 0.939 | 0.945 | 0.942 | 0.937 | 0.946 | 0.942 | 0.942 | 0.943 |
  | most_informative | 10 | 0.947 | 0.944 | 0.949 | 0.946 | 0.943 | 0.952 | 0.947 | 0.946 | 0.948 |
  | least_informative | 1 | 0.108 | 0.105 | 0.112 | 0.106 | 0.083 | 0.137 | 0.108 | 0.107 | 0.110 |
  | least_informative | 2 | 0.260 | 0.252 | 0.268 | 0.257 | 0.226 | 0.282 | 0.261 | 0.260 | 0.265 |
  | least_informative | 3 | 0.466 | 0.455 | 0.478 | 0.466 | 0.443 | 0.489 | 0.465 | 0.463 | 0.468 |
  | least_informative | 4 | 0.603 | 0.590 | 0.614 | 0.602 | 0.569 | 0.625 | 0.602 | 0.600 | 0.604 |
  | least_informative | 5 | 0.701 | 0.690 | 0.712 | 0.701 | 0.680 | 0.719 | 0.701 | 0.699 | 0.703 |
  | least_informative | 6 | 0.766 | 0.757 | 0.773 | 0.766 | 0.750 | 0.782 | 0.766 | 0.764 | 0.768 |
  | least_informative | 7 | 0.810 | 0.803 | 0.818 | 0.808 | 0.794 | 0.822 | 0.809 | 0.807 | 0.811 |
  | least_informative | 8 | 0.840 | 0.832 | 0.846 | 0.840 | 0.828 | 0.849 | 0.841 | 0.840 | 0.842 |
  | least_informative | 9 | 0.864 | 0.858 | 0.870 | 0.863 | 0.849 | 0.872 | 0.863 | 0.862 | 0.864 |
  | least_informative | 10 | 0.884 | 0.878 | 0.888 | 0.884 | 0.877 | 0.891 | 0.884 | 0.883 | 0.886 |

- **Simulation settings (stdout `368bd615`, verbatim):** "50 replications of 2000 simulated products per k and rater set; seed 20260713."
- **Method note (verbatim, `94cdcfeb`):** "**Projected reliability by number of ratings.** The observed relation above is confounded, because products with more ratings were also rated by different raters. The projection removes this: products with θ ~ N(0, 1) are simulated, each gets k ratings drawn from the fitted GRM, and they are scored with the fitted parameters. Raters are either drawn at random for each product, or fixed to the k most or the k least informative raters (information per rating, see the information summary), which brackets the effect of who rates. The table gives the mean over replications and the 2.5% and 97.5% quantiles: the empirical marginal reliability (as for the real scores), the squared correlation with the true θ, and the mean product-level reliability. Model parameters are treated as known."
  - **Reliability definitions (from the note):**
    - `empirical` = "the empirical marginal reliability (as for the real scores)";
    - `true_r2` = "the squared correlation with the true θ";
    - `mean_rel_post` = "the mean product-level reliability".
  - **Rater selection (from the note):** "drawn at random for each product, or fixed to the k most or the k least informative raters (information per rating, see the information summary)".
  - **Stated limitation (verbatim):** "Model parameters are treated as known."
- **Caption (table):** "Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model, for randomly drawn, the most informative and the least informative raters."
- **Caption (figure):** "Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM. Bands: 2.5% to 97.5% of the replications."
- **Direction/comparison (read off the printed values):**
  - Within each scheme, `empirical` increases with every step in k from 1 to 10.
  - At every k, most_informative > random > least_informative on `empirical`.
  - The gap between schemes narrows with k on `empirical`:
    - k = 1: 0.754 / 0.508 / 0.108;
    - k = 5: 0.920 / 0.857 / 0.701;
    - k = 10: 0.947 / 0.925 / 0.884.
  - In each row, `empirical`, `true_r2` and `mean_rel_post` agree to within 0.003. The largest difference is in least_informative k = 2: 0.260 / 0.257 / 0.261.
  - No projected value in the table reaches the model-based full-panel value of 0.960 (F1.12). The highest is 0.947 (most_informative, k = 10).
  - For random raters, the value at k = 2 is 0.688 (`empirical`) and 0.690 (`mean_rel_post`).
- **Caveats:**
  - The intervals are 2.5% and 97.5% quantiles over 50 simulation replications. They do not include uncertainty in the parameters, which the note says are "treated as known". They are not the same kind of interval as the parameter-draw CIs in F1.12.
  - The notebook does not print which raters form the "k most" and "k least informative" sets for each k. The note points to the information summary (F2.3, info_weighted_area) for the ranking. The selected sets themselves are not printed.
  - The table covers k = 1 to 10 only.
  - The values are simulated, not observed. The table's `mean_rel_post` is not the same quantity as the observed per-n `rel_post_mean` in F1.14, because the observed products have their actual raters and θ̂ distribution. The notebook makes no direct numeric comparison between the two tables.
  - The first sentence of `94cdcfeb` ("The observed relation above is confounded …") and the phrase "which brackets the effect of who rates" are the notebook's framing. Mark them for author confirmation if they are used.

## (e) Rater parameters, information and uncertainty

**F2.1 GRM discrimination a with SE** *(REVISED: now printed at 2 decimals as "estimate (SE)"; 3-decimal values no longer quotable)*
- **Finding:** GRM discriminations range from 0.63 (R18) to 3.71 (R19). The SEs are largest for raters with few ratings.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `cfb04715`).
- **Numbers** (rater, n, a (SE), exactly as printed): R01 1174 1.96 (0.16); R02 873 2.50 (0.33); R03 720 1.94 (0.20); R04 620 2.04 (0.24); R05 633 2.21 (0.23); R06 520 2.81 (0.42); R07 547 1.99 (0.20); R08 522 2.17 (0.28); R09 400 0.86 (0.15); R10 383 2.24 (0.34); R11 369 1.82 (0.21); R12 264 2.90 (0.57); R13 254 1.50 (0.22); R14 259 2.75 (0.66); R15 73 2.50 (0.52); R16 52 3.70 (1.36); R17 52 1.45 (0.46); R18 55 0.63 (0.26); R19 50 3.71 (2.22).
- **Caveats:**
  - R19 and R16 (50 and 52 ratings) have the two highest a values (3.71 and 3.70) and the two largest SEs (2.22 and 1.36).
  - Notebook (`a045a080`): "a is the rater's discrimination: how sharply the ratings separate products of different creativity."
  - Caption: "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b_k (b_k separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used."
  - Source note: the previous 3-decimal values (e.g., R19 3.709 (2.220)) are no longer printed in N2 and must not be quoted. Every 2-decimal value agrees with them after rounding (see Changes item 5).

**F2.2 GRM thresholds b_k with SE (severity)** *(REVISED: 2 decimals; no category_boundaries column; definition reworded)*
- **Finding:** First thresholds b1 range from -6.56 (R18) to 0.29 (R06). R06 is the only rater with a positive b1.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `cfb04715`).
- **Numbers** (b (SE) for b1 … b6, exactly as printed; "–" means the threshold does not exist):

  | rater | n | b1 | b2 | b3 | b4 | b5 | b6 |
  |---|---|---|---|---|---|---|---|
  | R01 | 1174 | -0.77 (0.06) | 0.58 (0.05) | 1.73 (0.09) | 2.75 (0.16) | 3.79 (0.28) | – |
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
  - The category_boundaries column has been removed from the display. The previous "1|2;…" strings are no longer printed.
- **Caveats:**
  - Notebook (`a045a080`, verbatim, REVISED wording): "b_k is the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater. No rater has an internal category gap, so b_k always separates categories k and k + 1; raters who never used the top categories have no estimate for the highest thresholds."
  - R18 has the largest threshold SEs (b1 SE 3.05).
  - The previous 3-decimal values are no longer printed. Do not quote them.

**F2.3 Rater information summary and shares** *(unchanged; new cell ids)*
- **Finding:** Weighted information per rater ranges from 0.123 (R18) to 3.539 (R19). Weighted shares range from 0.005 (R18) to 0.135 (R19).
- **Linked object:** `tbl-grm-information-summary` (N2, `fb982f3a`), `fig-grm-rater-information` (`0885cfe1`) and `fig-grm-information-shares` (`bfd8bc26`).
- **Numbers** (info_weighted_area / theta_at_max / info_max / share_weighted / shares at θ = −2, −1, 0, +1, +2):
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
- **Caveat (notebook, `63665ebe`):** "Information from different raters adds up under local independence."
- **Note:** F1.20 uses this table's "information per rating" ranking to select its most and least informative raters (`94cdcfeb`). The selected sets are not printed.

**F2.4 Intervals for rater information and share** *(unchanged; new cell ids)*
- **Finding:** The 95% intervals for information and share are widest for raters with few ratings. R19 has information [0.410, 11.017] and share [0.017, 0.331]. R16 has information [0.728, 6.489] and share [0.026, 0.223].
- **Linked object:** `tbl-grm-rater-information-ci` (N2, `f222f444`).
- **Numbers** (info [low, high]; share [low, high]): R01 0.979 [0.723, 1.219]; 0.037 [0.022, 0.050] · R02 1.705 [0.903, 2.558]; 0.065 [0.035, 0.098] · R03 1.080 [0.747, 1.466]; 0.041 [0.023, 0.056] · R04 1.155 [0.620, 1.739]; 0.044 [0.022, 0.064] · R05 1.343 [0.907, 1.808]; 0.051 [0.031, 0.070] · R06 1.410 [0.882, 2.088]; 0.054 [0.033, 0.080] · R07 1.056 [0.685, 1.383]; 0.040 [0.026, 0.057] · R08 1.359 [0.789, 1.958]; 0.052 [0.027, 0.077] · R09 0.238 [0.110, 0.419]; 0.009 [0.004, 0.015] · R10 1.330 [0.665, 2.026]; 0.051 [0.025, 0.081] · R11 0.877 [0.564, 1.253]; 0.033 [0.020, 0.047] · R12 2.120 [0.935, 3.290]; 0.081 [0.036, 0.131] · R13 0.655 [0.312, 0.980]; 0.025 [0.010, 0.037] · R14 1.722 [0.519, 3.131]; 0.066 [0.016, 0.112] · R15 1.710 [0.701, 3.081]; 0.065 [0.029, 0.112] · R16 3.300 [0.728, 6.489]; 0.126 [0.026, 0.223] · R17 0.543 [0.111, 1.373]; 0.021 [0.004, 0.052] · R18 0.123 [0.008, 0.352]; 0.005 [0.000, 0.013] · R19 3.539 [0.410, 11.017]; 0.135 [0.017, 0.331].
- **Caveats:**
  - Notebook (`37ecc203`): "95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings."
  - n_draws is dropped from the display. These are the same draws as in F1.12: 200 accepted, 87 rejected and replaced.

**F2.5 Category response functions** *(unchanged; new cell id)*
- **Linked object:** `fig-grm-category-response-functions` (N2, `7ff3ea30`). Figure only, with no printed numbers.

## (f) Model dependence of scores and rankings

**F2.6 Correlations of EAP scores between models** *(unchanged; new cell id)*
- **Finding:** All correlations between models are 0.975 or higher. GRM–M3 is 0.996 on both Pearson and Spearman. GRM–M1 is the lowest, at Pearson 0.975 and Spearman 0.978.
- **Linked object:** `tbl-theta-correlations` (N2, `2974492e`).
- **Numbers:**
  - Pearson: M1–M2 0.993; M1–M3 0.980; M1–GRM 0.975; M2–M3 0.989; M2–GRM 0.985; M3–GRM 0.996.
  - Spearman: M1–M2 0.996; M1–M3 0.983; M1–GRM 0.978; M2–M3 0.987; M2–GRM 0.983; M3–GRM 0.996.
  - The rm_facets_default_grid column correlates 1.000 with M1 on both coefficients.

**F2.7 Ranking change relative to the GRM** *(unchanged; new cell id)*
- **Finding:** Relative to the GRM, the share of products changing quintile is 0.202 under M1, 0.150 under M2 and 0.075 under M3.
- **Linked object:** `tbl-score-agreement` (N2, `ec338994`).
- **Numbers:**

  | model | pearson | spearman | mean abs pct shift | p95 abs pct shift | max abs pct shift | share changing quintile | share changing quintile by ≥2 |
  |---|---|---|---|---|---|---|---|
  | M1_RSM | 0.975 | 0.978 | 0.042 | 0.130 | 0.432 | 0.202 | 0.004 |
  | M2_PCM | 0.985 | 0.983 | 0.033 | 0.117 | 0.413 | 0.150 | 0.003 |
  | M3_GPCM | 0.996 | 0.996 | 0.017 | 0.044 | 0.234 | 0.075 | 0.001 |

- **Caveats:**
  - Percentile shifts are on a 0–1 scale (caption).
  - The notebook (`8620cb46`) states that share_products_changing_quintile in `tbl-raw-mean-vs-grm` "is not comparable with the model comparison above", meaning this table (see F2.9).

## (g) Sensitivity analyses

**F2.8 Sensitivity to the rater exclusion** *(unchanged; new cell id)*
- **Finding:** Refitting the GRM with all 22 raters changes the empirical marginal reliability from 0.67199 to 0.67186, and the model-based reliability from 0.95986 to 0.96186. θ̂ from the two fits correlates at 0.99997 (Pearson).
- **Linked object:** `tbl-sensitivity-rater-exclusion` (N2, `79738d4b`), printed with 5 decimals.
- **Numbers (final_data vs all_raters):**
  - n_raters 19 vs 22; n_ratings 7820 vs 7844; n_products 3668 vs 3669; excluded_raters "–" vs R20;R21;R22.
  - empirical_marginal_reliability 0.67199 vs 0.67186 ("Var(theta)/(Var(theta)+mean(PSD^2))").
  - model_based_marginal_reliability 0.95986 vs 0.96186 ("mirt::marginal_rxx (hypothetical full panel)").
  - Over 3668 common products: theta_pearson 0.99997; theta_spearman 0.99996; theta_mean_abs_diff 0.00171; theta_max_abs_diff 0.16246; share_products_changing_quintile 0.00491.
  - Over 19 common raters: a_max_abs_diff 0.19820; a_pearson 0.99880.
- **Caveat:** No CIs are given for the differences.

## (h) Raw mean vs model-based scores

**F2.9 Raw mean rating vs GRM score** *(REVISED: tie-aware columns added; cross-table quintile comparison removed)*
- **Finding:**
  - Over all 3668 products, the raw mean rating and the GRM score correlate at 0.906 (Pearson) and 0.932 (Spearman). Kendall's τ-b is 0.796.
  - A share of 0.083 of product pairs with different raw means are ordered the other way round by the GRM score.
  - With raw-mean ties ordered by the GRM score, a share of 0.237 of products change quintile. Without tie resolution the share is 0.350, and the notebook states that this plain share overstates the disagreement.
  - A share of 0.995 of products have a raw mean shared by another product.
  - Among products with the same raw mean, GRM scores lie up to 2.252 apart (maximum range of θ̂).
- **Linked object:** `tbl-raw-mean-vs-grm` (N2, `ec765a18`).
- **Numbers (every row and column, exactly as printed):**

  | n_ratings | n_products | pearson | spearman | mean_abs_percentile_shift | p95_abs_percentile_shift | max_abs_percentile_shift | share_products_changing_quintile | share_products_changing_quintile_by_2_or_more | share_products_changing_quintile_ties_resolved | share_discordant_pairs | kendall_tau_b | share_products_with_tied_raw_mean | mean_theta_range_same_raw_mean | max_theta_range_same_raw_mean |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | all | 3668 | 0.906 | 0.932 | 0.080 | 0.216 | 0.551 | 0.350 | 0.022 | 0.237 | 0.083 | 0.796 | 0.995 | 0.814 | 2.252 |
  | 1 | 897 | 0.921 | 0.940 | 0.074 | 0.203 | 0.334 | 0.385 | 0.004 | 0.104 | 0.042 | 0.832 | 1 | 1.283 | 1.436 |
  | 2 | 2080 | 0.922 | 0.933 | 0.075 | 0.234 | 0.562 | 0.319 | 0.028 | 0.220 | 0.067 | 0.815 | 1 | 1.537 | 2.196 |
  | 3+ | 691 | 0.954 | 0.959 | 0.060 | 0.177 | 0.400 | 0.266 | 0.006 | 0.220 | 0.070 | 0.842 | 0.971 | 0.619 | 1.396 |

- **Notebook explanation (verbatim, `8620cb46`, both paragraphs):**
  - "**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, overall and by number of ratings per product: correlations, shift in percentile rank, share of products changing quintile, and how far apart the GRM scores of products with the same raw mean lie (mean and maximum range of θ̂ within groups of equal raw mean). Products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination."
  - "The raw mean has many ties (with one rating it takes only 7 values), and tied products share one percentile rank, so share_products_changing_quintile overstates the disagreement and is not comparable with the model comparison above. The tie-aware columns are share_products_changing_quintile_ties_resolved (raw-mean ties ordered by the GRM score, the smallest change any tie-breaking can give), share_discordant_pairs (among product pairs with different raw means, the share the GRM orders the other way round) and Kendall's τ-b. share_products_with_tied_raw_mean gives the share of products whose raw mean is shared by another product."
- **Statement on comparability (notebook):** share_products_changing_quintile in this table "overstates the disagreement and is not comparable with the model comparison above" (`tbl-score-agreement`, F2.7). The notebook does not say whether share_products_changing_quintile_ties_resolved is comparable with `tbl-score-agreement`. It defines this column as "the smallest change any tie-breaking can give".
- **Direction (within this table):**
  - Tie-resolved share changing quintile: 0.237 (all), 0.104 (1 rating), 0.220 (2), 0.220 (3+). For every row it is lower than the plain share (0.350 / 0.385 / 0.319 / 0.266). The largest drop is in the 1-rating row (0.385 → 0.104).
  - Share of discordant pairs: 0.083 (all), 0.042 (1), 0.067 (2), 0.070 (3+).
  - Kendall's τ-b: 0.796 (all), 0.832 (1), 0.815 (2), 0.842 (3+). The pooled "all" value is lower than every subgroup value.
  - Share of products with a tied raw mean: 1 in the 1- and 2-rating rows, 0.971 in 3+, 0.995 overall.
  - Pearson / Spearman are highest in 3+ (0.954 / 0.959). They are 0.921 / 0.940 for 1 rating and 0.922 / 0.933 for 2.
  - The share changing by 2 or more quintiles is largest for 2 ratings (0.028). It is 0.022 overall. This column has no tie-aware counterpart.
  - Mean θ̂ range among products with the same raw mean: 1.283 (1), 1.537 (2), 0.619 (3+), 0.814 (all). Maximum range: 2.252 (all), 2.196 (2).
- **Caveats:**
  - The caption puts percentile shifts on a 0–1 scale. The caption has not been updated and does not mention the four tie-aware columns.
  - The notebook still does not say:
    - whether percentiles and quintiles in the 1 / 2 / 3+ rows are computed within each subgroup or over all products;
    - how equal-raw-mean groups are formed in the pooled "all" row (for example, whether equal raw means from different n are pooled);
    - how many equal-raw-mean groups enter the θ̂-range figures, or how large they are.
  - No CIs are printed.
  - The last sentence of the first paragraph ("Products with the same raw mean get different GRM scores when …") is the notebook's explanation of the mechanism. It is not a tested result in this table. Mark it for author confirmation if it is used.
  - The previous cross-table comparison (0.350 vs M1 0.202 / M2 0.150 / M3 0.075) has been removed, following the notebook's statement.
  - The previous juxtaposition of correlations with `tbl-theta-correlations` has also been dropped. The notebook makes no statement on comparing those two tables.

**F2.10 Figure: GRM score against raw mean** *(unchanged; new cell ids)*
- **Linked object:** `fig-raw-mean-vs-theta` (N2, `04843757`). Figure only, with no printed numbers.
- **Caption:** "GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally."
- **Notebook statement (`035c9318`):** "Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal."
- **Caveat:** Points are jittered horizontally (caption).

---

## Not found

These are absent from the notebooks. Do not invent them downstream.
- CIs for rel_post by number of ratings and for the per-n means (F1.14).
- CIs for the sensitivity differences (F2.8).
- CIs for the raw-mean vs GRM comparisons (F2.9), including the tie-aware columns.
- CIs or SEs for M1/M2 parameters and for the M1–M3 marginal and empirical reliabilities.
- Any global fit index other than the non-computable C2: no RMSEA, SRMSR or M2.
- What overlap_flag in `tbl-grm-q3-flagged` means, and what makes a Q3 pair "computable" (137 of 171).
- The full list of the 20 flag_q3 pairs (the table shows 10).
- The number of unused end categories as a single printed figure (the LR df gap). AUDIT.md says "6". That is NOT IN NOTEBOOK — not quotable. The per-rater unused categories are printed in `tbl-category-usage`.
- The number of successful bootstrap replications for the pairwise Cronbach's α. Only n_boot 1000 and n_boot_failed 361 are printed.
- Numeric values for the full-panel information curve, rel_post by θ̂, the category response functions, the raw-mean-vs-θ̂ scatter and the projection figure (beyond its table). These are figures only.
- The latent θ̂ distribution (mean, SD) of products, and a single severity summary per rater. Only thresholds are given.
- GRM rater parameters at 3 decimals. Only 2 decimals are now printed (F2.1, F2.2).
- Infit/outfit misfit thresholds. The notebook explicitly applies none. The 0.7–1.3 range is in REPORT.md only: NOT IN NOTEBOOK — not quotable.
- A test of the trend of rel_post across n, or of the raw-mean agreement across n-groups.
- An ICC of any form.
- Per-rater uncertainty for the descriptive response-style indices.
- For F2.9 (raw mean vs GRM):
  - the number and size of the equal-raw-mean groups;
  - whether percentiles and quintiles are computed within subgroups;
  - how the pooled "all" row forms equal-raw-mean groups (previous FI-20, still open);
  - the number of product pairs underlying share_discordant_pairs.
- For F1.20 (projection):
  - the identities of the raters in the "k most informative" and "k least informative" sets;
  - projections beyond k = 10;
  - projections that include parameter uncertainty (the note says parameters are "treated as known");
  - the number needed to reach any target reliability (not printed; do not derive one).
- The timespan of data collection (timestamps exist, but no summary is printed), rater demographics and rater expertise.

**Resolved since the previous version (removed from this list):** none fully. FI-20 is only partly addressed: the tie-aware columns are now defined, but group and subgroup formation is still undocumented.

## Flags

1. **Pre-exclusion residue.** This is unchanged.
   - All N0 output is pre-exclusion, which is expected for preprocessing. `tbl-cleaning-log` stops at 7844 and has no rater-exclusion row.
   - N1 is fully post-exclusion.
   - In N2, pre-exclusion values appear only where they are labelled as such:
     - the all_raters column of `tbl-sensitivity-rater-exclusion`;
     - `tbl-excluded-raters`;
     - the raters_excluded / duplicate rows of `tbl-design-summary`.
2. **`02_artifacts.md` is stale again.**
   - It lists the previous N2 cell ids. For example, `tbl-design-summary` is shown as `df7c3ef8` but is now `58e32d41`, and `tbl-raw-mean-vs-grm` is shown as `05caf58b` but is now `ec765a18`.
   - It describes `tbl-raw-mean-vs-grm` as having 11 columns. It now has 15.
   - It does not have `tbl-grm-reliability-projection` (`2ea36634`) or `fig-grm-reliability-projection` (`40072a98`).
   - `tbl-grm-rater-parameters` is now `cfb04715`, has a new format and no longer has a category_boundaries column.
   - The results-embedder should be re-run.
3. **Privacy.**
   - No original rater IDs are printed in N0, N1 or N2.
   - N0 cell `520638b8` still contains the full Google Sheets URL in its source, and the notebook says the sheet is shared as "anyone with the link".
   - N0 stdout prints absolute local paths and action UUIDs. N1 `f6039400` also prints action UUIDs in its head() output. The UUIDs are not personal data.
4. **LR df wording vs AUDIT.** The notebook explains the mechanism (`74a1629a`) but does not print the count of unused end categories. The writer must not quote "6" as a notebook value. They may refer to `tbl-category-usage`.
5. **Bootstrap-replication wording.** `tbl-reliability-overview` says "bootstrap, 1000 replications" for the pairwise Cronbach's α. `tbl-naive-indices` shows n_boot 1000 with n_boot_failed 361, and `3f17a200` says the interval uses the remaining replications. Both are printed and are not contradictory, but the overview wording alone could be misread.
6. **Parameter draws.** These are explained in `fdb7c615`. `tbl-grm-rater-information-ci` still drops n_draws from the display. Its note (`37ecc203`) says "from the same parameter draws".
7. **Display artifacts.**
   - `tbl-grm-convergence` prints tol as "0.000".
   - overlap_flag is "–" in every row of `tbl-grm-q3-flagged`.
   - `tbl-theta-correlations` has the `rm_facets_default_grid` check column, which the caption does not mention.
   - N1 `fb6df84b` prints counts as floats ("520.0").
   - `tbl-grm-rater-parameters` is now at 2 decimals, while the other N2 tables are at 3. A writer mixing F2.1/F2.2 with F2.3/F2.4 will see different precision.
   - The N2 code cell `5001e347` emits a Python SyntaxWarning (invalid escape sequence '\|') in stderr. This does not affect the values.
8. **Markdown order mismatches in N2 persist.**
   - The "Full panel" text (`5ef1f60a`) is separated from `fig-grm-panel-information` (`8f5ffbd6`) by the information-CI block (`37ecc203`, `f222f444`).
   - The "Reliability by number of ratings" text (`8c5abdd7`) precedes the CI note (`fdb7c615`) and `tbl-grm-reliability-ci`, not the by-n table (`69e27411`).
   - The M3 discrimination text (`a47f5ab0`) is separated from `tbl-discrimination-m3` (`91d95b1b`) by four labelled objects: `tbl-score-agreement`, `tbl-raw-mean-vs-grm`, `fig-raw-mean-vs-theta` and `tbl-sensitivity-rater-exclusion`.
9. **Unlabelled but cited sources.**
   - F0.4, F0.5 and F0.8 come from unlabelled N1 cells (`3b12b8bf`, `aa371443`, `fb6df84b`).
   - The mean Q3 line in F1.9 comes from unlabelled N2 cell `be50ab41`.
   - The F1.20 simulation settings (50 replications, 2000 products, seed 20260713) come from unlabelled N2 cell `368bd615`, because those columns are dropped from the labelled table.
   - These are quotable as notebook output but cannot be embedded as tables.
10. **Terminology.**
    - N1 prints, captions and axis labels say "products".
    - The label `tbl-overview-ratings-per-action` still contains "action".
    - N0 uses "actions" throughout.
    - N2 uses "products".
11. **Stale reference.** The N0 intro markdown (`64b27fc9`, `73ef4dcd`) still refers to the deleted notebooks `02a`–`02d`, `03` and `02_creativity_ratings_R.qmd`.
12. **Coinciding printed values.** empirical_marginal_reliability, var_theta_eap and rel_post_mean are all printed as 0.672 in `tbl-grm-reliability-summary`. This is reported as observed.
13. **Raw-mean table (F2.9), observed only.**
    - The "all" row's mean θ̂ range (0.814) is smaller than the 1-rating (1.283) and 2-rating (1.537) rows.
    - The "all" row's Kendall's τ-b (0.796) is lower than every subgroup value (0.832 / 0.815 / 0.842).
    - share_products_with_tied_raw_mean is 0.995 for "all" but 1 for both the 1- and 2-rating rows.
    - The notebook does not define how groups or ranks are formed in the pooled row. Ask the author or check the R source before describing these columns beyond their printed values.
    - The table caption does not mention the tie-aware columns.
14. **Mechanism sentences in N2 markdown.** These are the notebook's interpretive framing, not measured results. If they are used in the Discussion, mark them for author confirmation. Examples:
    - `8620cb46`: "Products with the same raw mean get different GRM scores when …";
    - `a47f5ab0`;
    - `d259af2b`: "High values mean the ranking of products hardly depends on the model";
    - NEW `94cdcfeb`: "The observed relation above is confounded …" and "which brackets the effect of who rates".
15. **Projection vs observed reliability (F1.20 vs F1.14).**
    - The projection simulates θ ~ N(0, 1) with parameters treated as known.
    - The observed table uses the actual products and raters.
    - The notebook makes no direct numeric comparison between the two tables. Any side-by-side statement (e.g., random k = 2 `mean_rel_post` 0.690 vs observed n = 2 `rel_post_mean` 0.698) would be the writer's juxtaposition, not a notebook result.

---

Files read:
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/03_findings.md` (previous version)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/02_artifacts.md` (staleness check only)