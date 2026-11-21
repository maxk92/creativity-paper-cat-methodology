# Findings (revision 2026-11-21, data freeze 2026-11-17)

Results-interpreter output, Phase 4 of the revision run. Every value below was read from the stored outputs of notebooks 00–03, in the precision and format printed there. Nothing was rounded, derived or carried over from the previous findings file. Where a statement compares printed numbers (for example "lowest", "above 1" or "inside the range"), it is marked *(read off printed values)*: the notebook does not print the comparison itself.

Sources:
- **N0** = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- **N1** = `.../notebooks/01_data_overview.ipynb`
- **N2** = `.../notebooks/02_jrt_results.ipynb` (main-paper objects)
- **N3** = `.../notebooks/03_jrt_supplement.ipynb` (supplementary objects)

Labels found: N0 has 1 (`tbl-cleaning-log`), N1 has 6, N2 has 14, N3 has 32, for 53 in total. Every label below has at least one finding. None of the N2/N3 objects shows the "placeholder line" for a missing source file.

Formatting as printed:
- N0: the `to_markdown` output of a raw data frame, with no thousands separators.
- N1 `show_table`: no thousands separators; any column with a non-integer prints 3 decimals. The `fb6df84b` output uses `round(3)`.
- N2/N3: thousands separators. Columns with non-integers print 3 decimals. p prints as "< .001". Missing values print as "–".
- `est_se`: estimate (SE) with 2 decimals.
- `est_ci`: estimate [low, high].
- `tbl-sensitivity-rater-exclusion`: 5 decimals.
- `tbl-rater-overview`: hand-formatted, 2 decimals, no thousands separator.

---

## Headline numbers

| Quantity | Value as printed | Source label |
|---|---|---|
| Ratings / products / raters (analysed) | 9,831 / 3,841 / 25 | `tbl-design-summary` (N2) |
| Empirical marginal reliability of the obtained GRM scores | 0.695, 95% CI [0.673, 0.711] (200 parameter draws) | `tbl-grm-reliability-ci`, `tbl-reliability-overview` (N3) |
| Model-based marginal reliability, hypothetical full panel | 0.970, 95% CI [0.966, 0.973] (200 parameter draws) | `tbl-grm-reliability-ci`, `tbl-reliability-overview` (N3) |
| Krippendorff's alpha (ordinal) | 0.402, 95% bootstrap CI [0.375, 0.427], 1,000 replications; 25 raters, 2,984 products | `tbl-naive-indices`, `tbl-reliability-overview` (N3) |
| Cronbach's alpha, pairwise covariances | 0.959, 95% CI [0.931, 0.970] (bootstrap, 513 of 1,000 replications computable, approximate); 18 raters, 1,948 products; removed: R26;R12;R19;R14;R02;R27;R17 | `tbl-naive-indices`, `tbl-reliability-overview` (N3) |
| Cronbach's alpha, fully crossed block | 0.785, 95% CI [0.736, 0.823] (1,000 replications); 3 raters, 270 products (rater IDs **not printed**) | same |
| BIC, M1 vs GRM | M1 30,617.021 (ΔBIC 0.000); GRM 30,617.437 (ΔBIC 0.416) | `tbl-model-fit` (N2) |
| BIC, M1 vs M2 | M1 30,617.021; M2 30,646.324 (ΔBIC to best 29.303) | `tbl-model-fit` (N2) |
| BIC, M2 vs M3 | M2 30,646.324; M3 30,666.967 (ΔBIC to best 49.946) | `tbl-model-fit` (N2) |
| M1 severity range | −1.005 (SE 0.059, R19) to 1.383 (SE 0.058, R06); span 2.388 logits | N2 stdout of cell `f52ad063` (below `fig-m1-rater-severity`) |
| GRM discrimination range | R18 0.65 (0.26) to R26 4.17 (1.49) | `tbl-grm-rater-parameters` (N2) |
| M3 discrimination range | R18 0.298 (SE 0.138) to R26 3.056 (SE 1.372); ratio max/min 10.254 | `tbl-discrimination-m3`, `tbl-discrimination-summary` (N3) |
| Smallest k with simulated reliability ≥ .80 | 4 | N2 stdout of cell `49c2492b` |
| Simulated actual design topped up to at least 4 ratings per product | 0.837 [0.832, 0.842] | `tbl-grm-reliability-min-ratings`, `tbl-reliability-overview` (N3) |

---

## N0: Data loading and preprocessing

**F0.1 Raw export and pseudonymisation**
- **Finding:** The sheet export was downloaded with 11323 rows. The pseudonym key holds 30 raters, 1 of them new in this download.
- **Linked object:** none. These are stdout lines of cells `520638b8` and `fdbdb3b4`.
- **Numbers:** "Downloaded 11323 rows." and "Raters in the key: 30; new in this download: 1 (key saved to data/raw/rater_pseudonym_key.csv)". The event lookup cell `722729d7` printed "Event details saved: … (4284 actions)".
- **Direction/comparison:** —
- **Caveats in data:** The 4284 event rows refer to all action ids in the raw export, before any cleaning.

**F0.2 Cleaning steps**
- **Finding:** Five cleaning steps reduced 11323 raw rows to 9863 rows.
- **Linked object:** `tbl-cleaning-log`
- **Numbers (as printed):**

  | step | n_rows_before | n_rows_after | n_rows_affected | description |
  |---|---|---|---|---|
  | drop_action_not_recognized | 11323 | 9891 | 1432 | Rows where the rater flagged the action as not recognized were excluded |
  | drop_missing_id | 9891 | 9891 | 0 | Rows with missing action_id/rater_id removed |
  | drop_out_of_range | 9891 | 9890 | 1 | Rating values outside {1,...,7} or non-integer removed |
  | drop_missing_rating | 9890 | 9890 | 0 | Rows with missing or non-convertible rating removed |
  | resolve_duplicates | 9890 | 9863 | 27 | Duplicates resolved: latest entry per (action_id, rater_id) kept |

- **Direction/comparison:** —
- **Caveats in data:**
  - Stdout of `fb9eaf36`: "Rows flagged as action_not_recognized: 1432".
  - Stdout of `36dd5cb3`: missing action_id 0, missing rater_id 0, non-convertible values 0.
  - The single out-of-range value was a rating of 0.0 by R04 (cell `793192b4`).
  - Rule for duplicates (markdown `6ad60c29`): "the entry with the latest timestamp is kept". Sheet order is not used.

**F0.3 Duplicates**
- **Finding:** 53 rows had a duplicated (action_id, rater_id) combination, and resolving them removed 27 rows.
- **Linked object:** none (stdout of `72468670`). The pair count is printed in N2 `tbl-design-summary`.
- **Numbers:**
  - "Rows with a duplicate (action_id, rater_id) combination: 53"
  - "Cleaning complete: 9891 -> 9863 rows." (`n0` was set after the not-recognised step.)
  - N2 `tbl-design-summary`: "duplicate pairs resolved in 00: 26" and "duplicate pairs conflicting: 1".
- **Direction/comparison:**
  - In the printed listing, one combination (R22) appears three times. *(read off printed values)*
  - The one conflicting pair is R14 with ratings 1.0 and 2.0. All other duplicates carry identical ratings. *(read off printed values)*
- **Caveats in data:** —

**F0.4 Cleaned data before exclusion**
- **Finding:** The cleaned file has 9863 rows from 30 raters and 3842 actions.
- **Linked object:** none (stdout of `dd37b3ec`).
- **Numbers:** "Cleaned data saved: … (9863 rows)", "Raters: 30", "Actions: 3842", "Warnings collected: 3".
- **Direction/comparison:** —
- **Caveats in data:** The counts are before the exclusion of raters with fewer than 15 ratings.

---

## N1: Data overview (after exclusion)

**F1.1 Exclusion and sample size**
- **Finding:** Of 9863 loaded ratings, 32 ratings from 5 raters with fewer than 15 ratings were excluded. 9831 ratings of 3841 products by 25 raters remain.
- **Linked object:** none (stdout of `f6039400` and `981d6824`). The same counts appear in `tbl-overview-ratings-per-action`.
- **Numbers:**
  - "Loaded 9863 ratings; excluded 32 ratings from 5 raters with fewer than 15 ratings (R20, R21, R22, R28, R29); 9831 ratings remain."
  - "Total ratings: 9831", "Distinct products: 3841", "Distinct raters: 25"
  - "Average ratings per product: 2.56", "Average ratings per rater: 393.2"
- **Direction/comparison:** —
- **Caveats in data:** —

**F1.2 Ratings per product and per rater**
- **Finding:** 857 products have 1 rating, 2227 have 2 and 757 have 3 or more. The maximum is 14 ratings per product. Raters gave between 47 and 1174 ratings.
- **Linked object:** `tbl-overview-ratings-per-action`
- **Numbers (as printed):**

  | quantity | value |
  |---|---|
  | n_ratings | 9831 |
  | n_products | 3841 |
  | n_raters | 25 |
  | n_products_1_rating | 857 |
  | n_products_2_ratings | 2227 |
  | n_products_3plus_ratings | 757 |
  | share_products_1_rating | 0.223 |
  | share_products_2_ratings | 0.580 |
  | share_products_3plus_ratings | 0.197 |
  | max_ratings_per_product | 14 |
  | mean_ratings_per_product | 2.559 |
  | harmonic_mean_ratings_per_product | 1.819 |
  | median_ratings_per_rater | 369 |
  | min_ratings_per_rater | 47 |
  | max_ratings_per_rater | 1174 |

- **Full distribution of products by number of ratings** (stdout of `3b12b8bf`):

  | Ratings per product | Products |
  |---|---|
  | 1 | 857 |
  | 2 | 2227 |
  | 3 | 73 |
  | 4 | 93 |
  | 5 | 143 |
  | 6 | 185 |
  | 7 | 124 |
  | 8 | 77 |
  | 9 | 25 |
  | 10 | 22 |
  | 11 | 8 |
  | 12 | 5 |
  | 13 | 1 |
  | 14 | 1 |

- **Cumulative counts ("k or more ratings"):** 1: 3841; 2: 2984; 3: 757; 4: 684; 5: 591; 6: 448; 7: 263; 8: 139; 9: 62; 10: 37; 11: 15; 12: 7; 13: 2; 14: 1.
- **Ratings per rater (ascending):**

  | Rater | Ratings | Rater | Ratings | Rater | Ratings |
  |---|---|---|---|---|---|
  | R30 | 47 | R12 | 264 | R07 | 547 |
  | R27 | 47 | R14 | 327 | R23 | 589 |
  | R17 | 52 | R16 | 357 | R04 | 620 |
  | R18 | 55 | R11 | 369 | R05 | 633 |
  | R15 | 73 | R10 | 383 | R03 | 720 |
  | R26 | 136 | R09 | 400 | R02 | 873 |
  | R25 | 138 | R24 | 481 | R01 | 1174 |
  | R19 | 250 | R06 | 520 | R08 | 522 |
  | R13 | 254 | | | | |

- **Direction/comparison:**
  - Four raters have about 50 ratings: R17 (52), R18 (55), R27 (47) and R30 (47). *(read off printed values)*
  - R26 has 136 ratings and R24 has 481. *(read off printed values)*
- **Caveats in data:** Rows from 10 ratings up rest on 22, 8, 5, 1 and 1 products.

**F1.3 Connectivity and rater overlap**
- **Finding:** The rater–product graph forms one connected component (3841 products, 25 raters). A rater's overlap with their best-connected partner ranges from 41 (R30) to 416 (R23, R24).
- **Linked object:** `fig-overview-rater-overlap`. The values come from the stdout of `bacf60d8` and `aa371443`.
- **Numbers:**
  - "Number of connected components: 1"
  - Best-partner overlap (ascending): R30 41, R27 42, R17 44, R19 47, R26 49, R18 50, R15 64, R14 114, R25 125, R12 145, R09 147, R13 154, R10 157, R05 190, R08 191, R06 240, R02 257, R04 257, R16 307, R01 329, R03 329, R11 357, R07 371, R23 416, R24 416.
- **Direction/comparison:** —
- **Caveats in data:** The figure itself prints no numbers (a heat map of jointly rated products).

**F1.4 Distribution of all ratings**
- **Finding:** Categories 1 and 2 hold the largest shares of all ratings. Category 7 holds the smallest.
- **Linked object:** `fig-overview-rating-distribution`. The values come from the stdout of `31873726`.
- **Numbers:**

  | Category | n | share |
  |---|---|---|
  | 1 | 2278 | 0.231716 |
  | 2 | 2501 | 0.254399 |
  | 3 | 1940 | 0.197335 |
  | 4 | 1455 | 0.148001 |
  | 5 | 1032 | 0.104974 |
  | 6 | 476 | 0.048418 |
  | 7 | 149 | 0.015156 |

- **Direction/comparison:** Frequencies decrease from category 2 to category 7. *(read off printed values)*
- **Caveats in data:** —

**F1.5 Rater response styles**
- **Finding:** Rater mean ratings range from 1.760 (R06) to 4.012 (R19). Eight raters used fewer than 7 categories.
- **Linked object:** `tbl-overview-rater-response-styles` and `fig-overview-rater-response-styles` (panels A–D).
- **Numbers (`tbl-overview-rater-response-styles`, as printed; sorted by mean):**

  | Rater | Ratings | Mean | Median | SD | IQR | Categories used | Entropy | Share 1 | Share 7 | Share extreme | Share middle |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | R06 | 520 | 1.760 | 1 | 1.111 | 1 | 6 | 1.191 | 0.579 | 0.000 | 0.579 | 0.192 |
  | R27 | 47 | 2.064 | 2 | 1.241 | 2 | 5 | 1.337 | 0.447 | 0.000 | 0.447 | 0.277 |
  | R17 | 52 | 2.077 | 2 | 1.296 | 2 | 5 | 1.367 | 0.481 | 0.000 | 0.481 | 0.327 |
  | R01 | 1174 | 2.164 | 2 | 1.022 | 2 | 6 | 1.358 | 0.287 | 0.000 | 0.287 | 0.315 |
  | R14 | 327 | 2.223 | 2 | 1.364 | 2 | 7 | 1.494 | 0.413 | 0.006 | 0.419 | 0.318 |
  | R11 | 369 | 2.333 | 2 | 1.397 | 2 | 7 | 1.532 | 0.344 | 0.003 | 0.347 | 0.309 |
  | R07 | 547 | 2.404 | 2 | 1.406 | 2 | 7 | 1.580 | 0.335 | 0.004 | 0.338 | 0.353 |
  | R30 | 47 | 2.638 | 2 | 1.750 | 3 | 7 | 1.670 | 0.383 | 0.043 | 0.426 | 0.383 |
  | R05 | 633 | 2.716 | 2 | 1.554 | 3 | 7 | 1.700 | 0.251 | 0.019 | 0.270 | 0.382 |
  | R03 | 720 | 2.750 | 3 | 1.402 | 2 | 6 | 1.643 | 0.224 | 0.000 | 0.224 | 0.493 |
  | R04 | 620 | 2.821 | 2 | 1.628 | 3 | 7 | 1.715 | 0.265 | 0.008 | 0.273 | 0.405 |
  | R26 | 136 | 2.853 | 3 | 1.353 | 2 | 6 | 1.648 | 0.169 | 0.000 | 0.169 | 0.507 |
  | R10 | 383 | 2.997 | 3 | 1.311 | 2 | 7 | 1.564 | 0.065 | 0.005 | 0.070 | 0.488 |
  | R08 | 522 | 3.000 | 3 | 1.545 | 2 | 7 | 1.761 | 0.193 | 0.013 | 0.207 | 0.492 |
  | R25 | 138 | 3.029 | 3 | 1.249 | 2 | 6 | 1.602 | 0.130 | 0.000 | 0.130 | 0.638 |
  | R02 | 873 | 3.032 | 3 | 1.841 | 3 | 7 | 1.822 | 0.276 | 0.052 | 0.328 | 0.391 |
  | R16 | 357 | 3.084 | 3 | 1.285 | 2 | 7 | 1.639 | 0.104 | 0.008 | 0.112 | 0.622 |
  | R12 | 264 | 3.360 | 3 | 1.152 | 1 | 7 | 1.547 | 0.042 | 0.004 | 0.045 | 0.735 |
  | R15 | 73 | 3.466 | 3 | 1.700 | 3 | 7 | 1.793 | 0.096 | 0.027 | 0.123 | 0.452 |
  | R23 | 589 | 3.469 | 3 | 1.531 | 3 | 7 | 1.799 | 0.110 | 0.029 | 0.139 | 0.625 |
  | R09 | 400 | 3.643 | 4 | 1.819 | 3 | 7 | 1.903 | 0.158 | 0.055 | 0.212 | 0.495 |
  | R13 | 254 | 3.681 | 4 | 1.116 | 1 | 7 | 1.520 | 0.016 | 0.004 | 0.020 | 0.799 |
  | R24 | 481 | 3.715 | 4 | 1.504 | 2 | 7 | 1.787 | 0.071 | 0.019 | 0.089 | 0.630 |
  | R18 | 55 | 3.836 | 4 | 1.259 | 2 | 6 | 1.584 | 0.018 | 0.000 | 0.018 | 0.764 |
  | R19 | 250 | 4.012 | 4 | 1.646 | 2 | 7 | 1.865 | 0.068 | 0.064 | 0.132 | 0.580 |

- **Direction/comparison:**
  - R19 has the highest raw mean and R06 the lowest. *(read off printed values)*
  - SD ranges from 1.022 (R01) to 1.841 (R02). *(read off printed values)*
  - Raters using fewer than 7 categories: R27 and R17 (5 categories each); R06, R01, R03, R26, R25 and R18 (6 categories each). *(read off printed values)*
- **Caveats in data:** R09's mean prints as 3.642 in the `round(3)` output of `fb6df84b` and as 3.643 in the labelled table (see Flags).

**F1.6 Degree distributions**
- **Finding:** No rater rated 2 or fewer products.
- **Linked object:** `fig-overview-degree-distributions`. The value is in the stdout of `9f03e286`.
- **Numbers:** "Raters with <= 2 rated products: 0". The figure shows the same distributions as F1.2.
- **Direction/comparison:** —
- **Caveats in data:** —

---

## N2: Main-paper objects

### Data basis

**F2.1 Design summary**
- **Finding:** All models use 9,831 ratings of 3,841 products by 25 raters. The design matrix fill is 0.102, with one connected component. 23 of 300 rater pairs share no products.
- **Linked object:** `tbl-design-summary`
- **Numbers (as printed):**

  | Quantity | Value |
  |---|---|
  | n ratings | 9,831 |
  | n products | 3,841 |
  | n raters | 25 |
  | min ratings per rater (exclusion cut-off) | 15 |
  | raters excluded | R20;R21;R22;R28;R29 |
  | ratings excluded | 32 |
  | products dropped | 1 |
  | n categories | 7 |
  | scale | 1-7 |
  | internal coding | rating - 1 (0-6) |
  | ratings per product mean | 2.559 |
  | ratings per product median | 2 |
  | ratings per product min | 1 |
  | ratings per product max | 14 |
  | ratings per product harmonic mean | 1.819 |
  | products with 1 rating | 857 |
  | ratings per rater min | 47 |
  | ratings per rater max | 1,174 |
  | matrix fill | 0.102 |
  | n components | 1 |
  | rater pairs total | 300 |
  | rater pairs without overlap | 23 |
  | rater pairs overlap median | 22.500 |
  | raters with category gaps | 8 |
  | raters with internal gap | 1 |
  | duplicate pairs resolved in 00 | 26 |
  | duplicate pairs conflicting | 1 |

- **Direction/comparison:** —
- **Caveats in data:**
  - Note `65dd75e4`: "missing ratings are left out of the likelihood, not imputed."
  - Retained raters in every rater table: R01–R19, R23–R27, R30.

**F2.2 Category use per rater (figure)**
- **Finding:** The figure shows each rater's share of ratings per category, sorted by raw mean. Labels give the number of ratings and any unused categories.
- **Linked object:** `fig-category-usage-shares`
- **Numbers:** The figure labels are drawn from the same data as `tbl-category-usage` (F3.4). No separate numbers are printed.
- **Direction/comparison:** —
- **Caveats in data:** The note says raters who never use a category "get fewer thresholds in mirt".

### Scoring model

**F2.3 Information criteria**
- **Finding:** The GRM has the lowest AIC and SABIC. M1 has the lowest BIC, and the GRM's BIC is 0.416 higher.
- **Linked object:** `tbl-model-fit`
- **Numbers (as printed):**

  | Model | Software | Family | Log-likelihood | Parameters | AIC | BIC | SABIC | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | sirt::rm.facets | adjacent category | -15,180.581 | 31 | 30,423.163 | 30,617.021 | 30,518.517 | 837.551 | 0.000 | 425.373 |
  | M2 (partial-credit MFRM) | mirt | adjacent category | -14,741.291 | 141 | 29,764.582 | 30,646.324 | 30,198.292 | 178.970 | 29.303 | 105.147 |
  | M3 (GPCM) | mirt | adjacent category | -14,652.571 | 165 | 29,635.141 | 30,666.967 | 30,142.674 | 49.530 | 49.946 | 49.530 |
  | GRM | mirt | cumulative (not in LR ladder) | -14,627.806 | 165 | 29,585.612 | 30,617.437 | 30,093.144 | 0.000 | 0.416 | 0.000 |

- **Direction/comparison** *(read off printed values)*:
  - AIC ranks the models GRM < M3 < M2 < M1. SABIC gives the same order.
  - BIC ranks them M1 < GRM < M2 < M3.
  - Within the ladder, BIC is lower for M1 than for M2, and lower for M2 than for M3.
  - M3 and the GRM both have 165 parameters.
- **Caveats in data:**
  - Note `e9c5d61f`: the GRM "belongs to the cumulative family, so it is compared with the ladder by information criteria only".
  - Pairwise BIC differences other than Δ-to-best (for example M3 − M2) are **not printed; not quotable**.

### Reliability and number of ratings

**F2.4 Product-level reliability by number of ratings**
- **Finding:** Mean rel_post rises from 0.526 (1 rating, 857 products) to 0.955 (14 ratings, 1 product). The mean decreases once, from 0.917 at 9 ratings to 0.915 at 10 ratings.
- **Linked object:** `tbl-grm-reliability-by-n`
- **Numbers (as printed):**

  | Ratings per product | Products | Mean rel_post | Median rel_post | Mean rel_info | Mean PSD |
  |---|---|---|---|---|---|
  | 1 | 857 | 0.526 | 0.541 | 0.546 | 0.683 |
  | 2 | 2,227 | 0.703 | 0.713 | 0.717 | 0.540 |
  | 3 | 73 | 0.770 | 0.777 | 0.791 | 0.472 |
  | 4 | 93 | 0.815 | 0.834 | 0.817 | 0.425 |
  | 5 | 143 | 0.852 | 0.860 | 0.858 | 0.382 |
  | 6 | 185 | 0.879 | 0.886 | 0.882 | 0.346 |
  | 7 | 124 | 0.891 | 0.897 | 0.897 | 0.328 |
  | 8 | 77 | 0.904 | 0.908 | 0.907 | 0.308 |
  | 9 | 25 | 0.917 | 0.923 | 0.916 | 0.286 |
  | 10 | 22 | 0.915 | 0.926 | 0.917 | 0.286 |
  | 11 | 8 | 0.919 | 0.925 | 0.921 | 0.282 |
  | 12 | 5 | 0.931 | 0.928 | 0.930 | 0.261 |
  | 13 | 1 | 0.944 | 0.944 | 0.945 | 0.237 |
  | 14 | 1 | 0.955 | 0.955 | 0.954 | 0.211 |

- **Direction/comparison** *(read off printed values)*:
  - Mean rel_post has one dip, at 10 ratings (0.915 against 0.917 at 9).
  - Median rel_post has one dip, at 11 ratings (0.925 against 0.926 at 10).
  - Mean PSD is equal at 9 and 10 ratings (0.286).
  - Mean rel_post first reaches at least 0.80 at 4 ratings (0.815).
- **Caveats in data:** The rows for 10, 11, 12, 13 and 14 ratings rest on 22, 8, 5, 1 and 1 products. Rows 9–14 have fewer than 30 products each.

**F2.5 Observed vs simulated reliability (figure) and smallest k reaching .80**
- **Finding:** In the projection, k = 4 is the smallest number of ratings per product with simulated empirical reliability of at least .80.
- **Linked object:** `fig-grm-reliability-observed-vs-simulated`, with the stdout of cell `49c2492b`.
- **Numbers:**
  - "50 replications of 2000 simulated products per k; seed 20260713."
  - "Smallest k with simulated empirical reliability of at least .80: 4."
  - The figure's annotation lines are computed from `reliability_min_ratings.csv` (at least 4 per product) and the "GRM: model-based marginal reliability" row of `reliability_overview.csv`. Their values are printed in N3: 0.837 and 0.970 (F3.9, F3.10).
- **Direction/comparison:** See F3.15 for the observed vs simulated comparison per k.
- **Caveats in data:** In the figure, dots for fewer than 10 products are faded (caption).
- **Simulation assumptions, VERBATIM** (N2 markdown `16431696`): "Line and band: the projection from the fitted GRM, in which simulated products with θ ~ N(0, 1) each receive k ratings from k raters of the panel drawn at random (equal probability), with ratings generated and scored by the fitted GRM (parameters treated as known; 50 replications of 2,000 products per k). Dashed lines: the actual design topped up so that every product has at least 4 ratings (simulated the same way), and the model-based reliability of the hypothetical full panel."

### Raters

**F2.6 M1 severity**
- **Finding:** M1 severity ranges from −1.005 for R19 (most lenient) to 1.383 for R06 (most severe), a span of 2.388 logits.
- **Linked object:** `fig-m1-rater-severity`, with the stdout of cell `f52ad063`.
- **Numbers:** "M1 severity ranges from -1.005 (SE 0.059, R19) to 1.383 (SE 0.058, R06): a span of 2.388 logits." Severity for every rater (2 decimals) is in `tbl-rater-overview` (F3.16).
- **Direction/comparison:** R19 also has the highest raw mean (4.012) and R06 the lowest (1.760) (F1.5). *(read off printed values)*
- **Caveats in data:** SEs of the other raters' M1 severities are drawn in the figure only and are **not printed**.

**F2.7 GRM rater parameters**
- **Finding:** GRM discrimination a ranges from 0.65 (R18, SE 0.26) to 4.17 (R26, SE 1.49). Raters who did not use the top categories have fewer thresholds.
- **Linked object:** `tbl-grm-rater-parameters`
- **Numbers (as printed; estimate (SE)):**

  | Rater | Ratings | a | b1 | b2 | b3 | b4 | b5 | b6 |
  |---|---|---|---|---|---|---|---|---|
  | R01 | 1,174 | 1.79 (0.13) | -0.83 (0.06) | 0.59 (0.05) | 1.79 (0.10) | 2.86 (0.16) | 3.94 (0.29) | – |
  | R02 | 873 | 2.60 (0.30) | -0.68 (0.06) | -0.02 (0.05) | 0.40 (0.05) | 0.90 (0.06) | 1.40 (0.08) | 2.02 (0.12) |
  | R03 | 720 | 1.85 (0.17) | -1.11 (0.08) | -0.16 (0.06) | 0.76 (0.07) | 1.29 (0.10) | 2.49 (0.19) | – |
  | R04 | 620 | 2.05 (0.22) | -0.76 (0.08) | 0.17 (0.06) | 0.67 (0.07) | 1.11 (0.08) | 2.06 (0.14) | 3.43 (0.30) |
  | R05 | 633 | 2.36 (0.22) | -0.84 (0.07) | 0.12 (0.05) | 0.66 (0.06) | 1.27 (0.08) | 1.85 (0.12) | 2.68 (0.19) |
  | R06 | 520 | 3.15 (0.45) | 0.24 (0.05) | 0.97 (0.07) | 1.52 (0.10) | 2.17 (0.15) | 2.59 (0.21) | – |
  | R07 | 547 | 1.91 (0.16) | -0.52 (0.07) | 0.45 (0.07) | 1.14 (0.09) | 1.80 (0.12) | 2.58 (0.18) | 3.99 (0.44) |
  | R08 | 522 | 2.11 (0.24) | -1.19 (0.10) | -0.30 (0.06) | 0.39 (0.07) | 1.11 (0.09) | 1.91 (0.14) | 3.03 (0.26) |
  | R09 | 400 | 0.95 (0.15) | -1.99 (0.30) | -0.96 (0.18) | -0.04 (0.12) | 0.72 (0.15) | 1.78 (0.25) | 3.44 (0.48) |
  | R10 | 383 | 2.37 (0.32) | -2.01 (0.16) | -0.20 (0.07) | 0.44 (0.08) | 1.08 (0.11) | 2.03 (0.19) | 3.21 (0.40) |
  | R11 | 369 | 1.95 (0.20) | -0.47 (0.08) | 0.61 (0.08) | 1.18 (0.10) | 1.67 (0.13) | 2.69 (0.24) | 4.04 (0.59) |
  | R12 | 264 | 2.91 (0.50) | -2.01 (0.20) | -0.88 (0.10) | 0.20 (0.08) | 1.32 (0.12) | 2.19 (0.19) | 3.50 (0.46) |
  | R13 | 254 | 1.49 (0.21) | -3.43 (0.49) | -1.56 (0.19) | -0.32 (0.11) | 1.14 (0.16) | 2.59 (0.32) | 4.39 (0.82) |
  | R14 | 327 | 2.45 (0.45) | -0.17 (0.08) | 0.56 (0.08) | 1.09 (0.11) | 1.91 (0.18) | 2.56 (0.26) | 3.35 (0.42) |
  | R15 | 73 | 2.71 (0.52) | -1.67 (0.24) | -0.23 (0.14) | 0.26 (0.13) | 0.64 (0.14) | 1.31 (0.19) | 2.66 (0.42) |
  | R16 | 357 | 2.37 (0.21) | -1.56 (0.12) | -0.53 (0.07) | 0.46 (0.07) | 1.38 (0.10) | 2.41 (0.18) | 3.28 (0.31) |
  | R17 | 52 | 1.73 (0.51) | -0.19 (0.20) | 0.45 (0.23) | 1.15 (0.35) | 1.73 (0.50) | – | – |
  | R18 | 55 | 0.65 (0.26) | -6.39 (2.92) | -2.66 (1.15) | -0.53 (0.48) | 0.96 (0.57) | 4.34 (1.72) | – |
  | R19 | 250 | 1.97 (0.39) | -1.97 (0.25) | -1.02 (0.15) | -0.40 (0.11) | 0.33 (0.10) | 1.10 (0.15) | 2.10 (0.26) |
  | R23 | 589 | 1.71 (0.13) | -1.77 (0.12) | -0.93 (0.08) | 0.01 (0.06) | 0.81 (0.08) | 1.85 (0.13) | 2.87 (0.20) |
  | R24 | 481 | 2.56 (0.20) | -1.78 (0.11) | -0.83 (0.07) | -0.17 (0.06) | 0.51 (0.06) | 1.41 (0.09) | 2.72 (0.19) |
  | R25 | 138 | 3.03 (0.45) | -1.28 (0.14) | -0.46 (0.10) | 0.35 (0.09) | 1.28 (0.14) | 2.42 (0.34) | – |
  | R26 | 136 | 4.17 (1.49) | -0.98 (0.14) | -0.12 (0.09) | 0.53 (0.11) | 1.32 (0.16) | 2.12 (0.25) | – |
  | R27 | 47 | 2.85 (0.82) | -0.24 (0.16) | 0.48 (0.17) | 0.95 (0.22) | 2.23 (0.51) | – | – |
  | R30 | 47 | 2.69 (0.69) | -0.27 (0.17) | 0.21 (0.16) | 0.63 (0.18) | 1.16 (0.25) | 2.11 (0.39) | 2.56 (0.48) |

- **Direction/comparison** *(read off printed values)*:
  - R17 and R27 have four thresholds (b1–b4).
  - R01, R03, R06, R18, R25 and R26 have five thresholds (b1–b5).
  - The largest SE of a is R26's (1.49). The SEs of the four low-count raters are R17 0.51, R18 0.26, R27 0.82 and R30 0.69.
  - The second-lowest a is R09's: 0.95 (0.15).
- **Caveats in data:**
  - Note `c934c8c9`: for a rater with an internal gap (R27; F3.4), "the thresholds separate other category boundaries and are not directly comparable with those of the other raters."
  - R18's b1 has an SE of 2.92.

**F2.8 GRM discrimination with 95% intervals (figure)**
- **Finding:** The figure shows a per rater ± 1.96 SE, sorted by a, with a dashed line at the median.
- **Linked object:** `fig-grm-rater-discrimination-ci`
- **Numbers:** As in F2.7. The median of a is drawn as a line but **not printed**.
- **Direction/comparison:** —
- **Caveats in data:** —

**F2.9 Category response functions (figure)**
- **Finding:** The figure shows the category response functions per rater.
- **Linked object:** `fig-grm-category-response-functions`
- **Numbers:** No numbers printed (PNG from the R pipeline).
- **Direction/comparison:** —
- **Caveats in data:** —

**F2.10 Rater information with intervals (figures)**
- **Finding:** The first figure shows average information per rating with 95% intervals from 200 accepted parameter draws. The second shows the full information functions.
- **Linked object:** `fig-grm-rater-information-ci` and `fig-grm-rater-information`
- **Numbers:** The values are printed in N3 `tbl-grm-rater-information-ci` (F3.17).
- **Direction/comparison:** —
- **Caveats in data:** The note says wide intervals are "typically for raters with few ratings".

### Scores

**F2.11 Raw mean vs GRM score**
- **Finding:** Kendall's τ-b between raw mean and GRM score is 0.773 for products with 1 rating, 0.818 for 2 ratings and 0.861 for 3+ ratings. Shares of pairs in reversed order are 0.076, 0.066 and 0.065.
- **Linked object:** `tbl-raw-mean-vs-grm` and `fig-raw-mean-vs-theta`
- **Numbers (as printed):**

  | Ratings per product | Products | Kendall's τ-b | Share of pairs in reversed order | Mean θ̂ range at equal raw mean | Maximum θ̂ range at equal raw mean |
  |---|---|---|---|---|---|
  | 1 | 857 | 0.773 | 0.076 | 1.240 | 1.420 |
  | 2 | 2,227 | 0.818 | 0.066 | 1.558 | 2.129 |
  | 3+ | 757 | 0.861 | 0.065 | 0.507 | 1.306 |

- **Direction/comparison** *(read off printed values)*:
  - τ-b increases from 1 to 2 to 3+ ratings.
  - The reversed share is highest at 1 rating (0.076) and lower at 2 (0.066) and 3+ (0.065).
  - The largest maximum θ̂ range at equal raw mean is at 2 ratings (2.129).
- **Caveats in data:** Note `aa174433`: "The raw mean is tied for almost all products (with one rating it takes only 7 values)". The θ̂ range is printed without a unit label.

**F2.12 Change of product ranking relative to the GRM**
- **Finding:** Spearman ρ with the GRM scores is 0.980 (M1), 0.984 (M2) and 0.997 (M3).
- **Linked object:** `tbl-score-agreement`
- **Numbers (as printed):**

  | Model | Pearson r | Spearman ρ | Mean percentile shift | 95th percentile of shift | Maximum shift | Share changing quintile | Share changing ≥ 2 quintiles |
  |---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | 0.978 | 0.980 | 0.040 | 0.123 | 0.432 | 0.188 | 0.003 |
  | M2 (partial-credit MFRM) | 0.986 | 0.984 | 0.032 | 0.111 | 0.404 | 0.155 | 0.005 |
  | M3 (GPCM) | 0.996 | 0.997 | 0.016 | 0.046 | 0.225 | 0.073 | 0.000 |

- **Direction/comparison:** Agreement with the GRM is highest for M3 and lowest for M1 on every column. *(read off printed values)*
- **Caveats in data:** The percentile shift is on a 0–1 scale (caption).

---

## N3: Supplementary objects

### Data and exclusion

**F3.1 Excluded raters**
- **Finding:** Five raters with fewer than 15 ratings were excluded.
- **Linked object:** `tbl-excluded-raters`
- **Numbers:** R20 13; R21 9; R22 2; R28 7; R29 1. Reason for each: "fewer than 15 ratings".
- **Direction/comparison:** —
- **Caveats in data:** The total of 32 is printed in `tbl-design-summary` and N1.

**F3.2 Exclusion sensitivity refit**
- **Finding:** Refitting the GRM on all raters gives 29 raters, because R29 was not estimable. Empirical reliability is 0.69453 against 0.69490, and θ̂ correlates at r = 0.99997 over the 3,841 common products. The largest absolute θ̂ change is 0.16518.
- **Linked object:** `tbl-sensitivity-rater-exclusion`
- **Numbers (as printed):**

  | Quantity | Final data | All raters | Note |
  |---|---|---|---|
  | n raters | 25 | 29 | – |
  | n ratings | 9,831 | 9,862 | – |
  | n products | 3,841 | 3,842 | – |
  | excluded raters | – | R20;R21;R22;R28;R29;R29 (one category, not estimable) | – |
  | empirical marginal reliability | 0.69490 | 0.69453 | Var(theta)/(Var(theta)+mean(PSD^2)) |
  | model based marginal reliability | 0.97008 | 0.97207 | mirt::marginal rxx (hypothetical full panel) |
  | theta pearson common products | 0.99997 | – | all-raters vs final GRM, 3,841 common products |
  | theta spearman common products | 0.99996 | – | same |
  | theta mean abs diff | 0.00187 | – | same |
  | theta max abs diff | 0.16518 | – | same |
  | share products changing quintile | 0.00364 | – | same |
  | a max abs diff common raters | 0.21451 | – | all-raters vs final GRM, 25 common raters |
  | a pearson common raters | 0.99796 | – | same |

- **Direction/comparison:** —
- **Caveats in data:** The "excluded raters" cell lists R29 twice (see Flags).

**F3.3 Ratings per product (figure)**
- **Finding:** Bar chart of products by number of ratings, with count labels.
- **Linked object:** `fig-design-ratings-per-product`
- **Numbers:** Same counts as F1.2 / F2.4 (857, 2,227, 73, 93, 143, 185, 124, 77, 25, 22, 8, 5, 1, 1).
- **Direction/comparison:** —
- **Caveats in data:** —

**F3.4 Category use per rater**
- **Finding:** Eight raters left at least one category unused. R17 left 6 and 7 unused; R27 left 5 and 7 unused, which gives R27 an internal gap.
- **Linked object:** `tbl-category-usage`
- **Numbers (as printed; counts per category 1–7, total, missing categories, internal gap):**

  | Rater | Cat 1 | Cat 2 | Cat 3 | Cat 4 | Cat 5 | Cat 6 | Cat 7 | Ratings | Missing | Internal gap |
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
  | R14 | 135 | 80 | 48 | 42 | 14 | 6 | 2 | 327 | – | False |
  | R15 | 7 | 22 | 11 | 9 | 13 | 9 | 2 | 73 | – | False |
  | R16 | 37 | 85 | 111 | 75 | 36 | 10 | 3 | 357 | – | False |
  | R17 | 25 | 10 | 9 | 4 | 4 | 0 | 0 | 52 | 6;7 | False |
  | R18 | 1 | 8 | 14 | 12 | 16 | 4 | 0 | 55 | 7 | False |
  | R19 | 17 | 37 | 40 | 55 | 50 | 35 | 16 | 250 | – | False |
  | R23 | 65 | 99 | 151 | 117 | 100 | 40 | 17 | 589 | – | False |
  | R24 | 34 | 84 | 97 | 105 | 101 | 51 | 9 | 481 | – | False |
  | R25 | 18 | 30 | 39 | 34 | 15 | 2 | 0 | 138 | 7 | False |
  | R26 | 23 | 39 | 31 | 26 | 12 | 5 | 0 | 136 | 7 | False |
  | R27 | 21 | 12 | 6 | 7 | 0 | 1 | 0 | 47 | 5;7 | True |
  | R30 | 18 | 8 | 7 | 6 | 5 | 1 | 2 | 47 | – | False |

- **Direction/comparison:** The raters with missing categories are R01, R03, R06, R17, R18, R25, R26 and R27. *(read off printed values; the count 8 is printed in `tbl-design-summary`)*
- **Caveats in data:** R18 used category 1 once.

### Estimation and fit (GRM)

**F3.5 Convergence**
- **Finding:** The GRM converged after 550 EM iterations, and the information matrix is positive definite.
- **Linked object:** `tbl-grm-convergence`
- **Numbers:** Method EM; Quadrature points 61; SE type Oakes; Tolerance 10⁻⁴; Converged True; Iterations 550; Information matrix positive definite True; Log-likelihood -14,627.806; Parameters 165; AIC 29,585.612; BIC 30,617.437; SABIC 30,093.144; Products 3,841; Ratings (total) 9,831.
- **Direction/comparison:** —
- **Caveats in data:** —

**F3.6 Rater fit (GRM): infit, outfit, S-X²**
- **Finding:** All GRM infit and outfit values are below 1, ranging from 0.315/0.303 (R26) to 0.983/0.973 (R18). All S-X² p values lie between 0.362 and 0.601.
- **Linked object:** `tbl-grm-rater-fit`
- **Numbers (as printed):**

  | Rater | Ratings | Infit | Outfit | S-X² | df | p | Imputations |
  |---|---|---|---|---|---|---|---|
  | R01 | 1,174 | 0.727 | 0.698 | 276.211 | 271.950 | 0.417 | 20 |
  | R02 | 873 | 0.472 | 0.439 | 368.246 | 369.700 | 0.512 | 20 |
  | R03 | 720 | 0.754 | 0.748 | 352.199 | 356.700 | 0.557 | 20 |
  | R04 | 620 | 0.616 | 0.577 | 375.216 | 366.250 | 0.362 | 20 |
  | R05 | 633 | 0.623 | 0.616 | 350.331 | 357.800 | 0.601 | 20 |
  | R06 | 520 | 0.586 | 0.449 | 220.221 | 222.850 | 0.537 | 20 |
  | R07 | 547 | 0.820 | 0.721 | 355.990 | 360.000 | 0.550 | 20 |
  | R08 | 522 | 0.594 | 0.582 | 361.903 | 356.750 | 0.414 | 20 |
  | R09 | 400 | 0.875 | 0.872 | 546.126 | 549.250 | 0.530 | 20 |
  | R10 | 383 | 0.628 | 0.612 | 300.552 | 304.000 | 0.545 | 20 |
  | R11 | 369 | 0.873 | 0.833 | 350.459 | 344.750 | 0.405 | 20 |
  | R12 | 264 | 0.521 | 0.518 | 237.786 | 238.550 | 0.502 | 20 |
  | R13 | 254 | 0.850 | 0.853 | 332.963 | 334.000 | 0.506 | 20 |
  | R14 | 327 | 0.543 | 0.462 | 304.957 | 298.750 | 0.390 | 20 |
  | R15 | 73 | 0.775 | 0.697 | 309.445 | 311.050 | 0.515 | 20 |
  | R16 | 357 | 0.828 | 0.820 | 286.520 | 292.600 | 0.589 | 20 |
  | R17 | 52 | 0.927 | 0.873 | 329.705 | 332.550 | 0.534 | 20 |
  | R18 | 55 | 0.983 | 0.973 | 428.288 | 427.050 | 0.474 | 20 |
  | R19 | 250 | 0.544 | 0.567 | 403.243 | 397.700 | 0.413 | 20 |
  | R23 | 589 | 0.875 | 0.862 | 420.134 | 411.700 | 0.376 | 20 |
  | R24 | 481 | 0.761 | 0.768 | 307.662 | 306.400 | 0.469 | 20 |
  | R25 | 138 | 0.751 | 0.738 | 248.519 | 242.300 | 0.378 | 20 |
  | R26 | 136 | 0.315 | 0.303 | 201.364 | 206.050 | 0.579 | 20 |
  | R27 | 47 | 0.675 | 0.676 | 236.936 | 231.100 | 0.382 | 20 |
  | R30 | 47 | 0.841 | 0.676 | 323.239 | 325.300 | 0.522 | 20 |

- **Direction/comparison** *(read off printed values)*:
  - No S-X² p is below .05. The lowest is 0.362 (R04) and the highest 0.601 (R05).
  - No infit or outfit is above 1.3.
  - Raters marked † in `tbl-rater-overview` (infit or outfit outside 0.7–1.3): R19, R15, R12, R10, R08, R02, R26, R04, R05, R30, R01, R27, R14 and R06. All of these are values below 0.7. The count of 14 is **not printed**.
- **Caveats in data:** Note `80860554`, VERBATIM: "With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked. S-X² … needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative. The flags in the rater-fit output (flag_infit, flag_outfit; R/01_grm.R) mark values outside 0.7–1.3; with this design they mostly mark values below 0.7, which is expected rather than misfit."

**F3.7 Local dependence (Q3)**
- **Finding:** Mean Q3 over 256 computable rater pairs is −0.188, and 36 pairs are flagged. The largest deviation from the mean is for R02–R26 (Q3 −0.806; minus mean −0.618).
- **Linked object:** `tbl-grm-q3-flagged`, with the stdout of cell `42f0ab09`.
- **Numbers:** "Mean Q3 over 256 computable rater pairs: -0.188; pairs flagged (flag_q3): 36". Top 10 pairs among those with ≥ 30 shared products:

  | Rater 1 | Rater 2 | Shared products | Q3 | Q3 minus mean Q3 | Flagged |
  |---|---|---|---|---|---|
  | R02 | R26 | 49 | -0.806 | -0.618 | True |
  | R08 | R12 | 51 | -0.645 | -0.457 | True |
  | R02 | R04 | 257 | -0.638 | -0.450 | True |
  | R09 | R23 | 130 | 0.220 | 0.408 | True |
  | R04 | R26 | 34 | -0.591 | -0.403 | True |
  | R02 | R14 | 114 | -0.577 | -0.389 | True |
  | R02 | R08 | 72 | -0.545 | -0.357 | True |
  | R03 | R10 | 49 | -0.534 | -0.346 | True |
  | R17 | R24 | 37 | 0.157 | 0.345 | True |
  | R02 | R05 | 57 | -0.531 | -0.343 | True |

- **Direction/comparison:** Eight of the ten listed deviations are negative and two are positive (R09–R23, R17–R24). *(read off printed values)*
- **Caveats in data:**
  - Note `8869ac3e`: Q3 is computed for pairs with ≥ 3 jointly rated products. "With few raters per product, Q3 is biased negatively". The flag marks pairs with ≥ 30 shared products and a deviation > 0.2.
  - R02 appears in five of the ten listed pairs. *(read off printed values)*

**F3.8 Global fit (C2)**
- **Finding:** C2 could not be computed.
- **Linked object:** `tbl-grm-global-fit`
- **Numbers:** Computable False; Rater pairs 300; Rater pairs without shared products 23; Note: "Not computable: 23 of 300 rater pairs share no products, so their bivariate moments and hence C2 are undefined."
- **Direction/comparison:** —
- **Caveats in data:** —

### Reliability (observed)

**F3.9 Reliability overview**
- **Finding:** The overview table lists the reliability and agreement indices side by side. Krippendorff's α is 0.402, pairwise Cronbach's α 0.959, crossed-block α 0.785, GRM empirical 0.695, simulated at-least-4 design 0.837 and GRM model-based 0.970.
- **Linked object:** `tbl-reliability-overview`
- **Numbers (as printed):**

  | Index | Refers to | Value | CI or note |
  |---|---|---|---|
  | Krippendorff's alpha (ordinal) | consensus of single ratings | 0.402 | 95% bootstrap CI [0.375, 0.427], 1,000 replications |
  | Cronbach's alpha (pairwise covariances) | consistency of the unweighted rater mean | 0.959 | 95% CI [0.931, 0.970] (bootstrap, 513 of 1,000 replications computable, approximate); 18 raters; removed: R26;R12;R19;R14;R02;R27;R17 |
  | Cronbach's alpha (fully crossed block) | consistency of the unweighted rater mean (crossed subset) | 0.785 | 95% CI [0.736, 0.823] (bootstrap, 1,000 replications); 3 raters, 270 products |
  | GRM: empirical marginal reliability | actual theta hat (primary) | 0.695 | 95% CI [0.673, 0.711] (200 parameter draws); Var(theta)/(Var(theta)+mean(PSD^2)) |
  | GRM: empirical marginal reliability, at least 4 ratings per product (simulated) | actual design topped up to at least 4 ratings per product | 0.837 | 95% range [0.832, 0.842], 50 replications; 7,098 ratings added to 3,157 products |
  | GRM: model-based marginal reliability | hypothetical full panel | 0.970 | 95% CI [0.966, 0.973] (200 parameter draws); mirt::marginal rxx, all raters |
  | GRM: median rel post | precision per product | 0.706 | first quartile 0.601, third quartile 0.796 |
  | GRM: IQR rel post | precision per product | 0.195 | – |
  | M1 (rating-scale MFRM): marginal reliability | comparison | 0.960 | – |
  | M2 (partial-credit MFRM): marginal reliability | comparison | 0.959 | – |
  | M3 (GPCM): marginal reliability | comparison | 0.966 | – |

- **Direction/comparison:** —
- **Caveats in data:** The note above the table (`a045416a`) says the indices "answer different questions … They are not interchangeable."

**F3.10 Top-up simulation (at least 4 ratings per product)**
- **Finding:** The simulated actual design gives 0.691 [0.684, 0.699]. The design topped up to at least 4 ratings per product gives 0.837 [0.832, 0.842] (3,157 products topped up, 7,098 ratings added, 16,929 ratings in total).
- **Linked object:** `tbl-grm-reliability-min-ratings`
- **Numbers (as printed):**

  | Design | Products topped up | Ratings added | Ratings (total) | Empirical reliability [95% range] | Mean rel_post | Replications |
  |---|---|---|---|---|---|---|
  | Actual design | 0 | 0 | 9,831 | 0.691 [0.684, 0.699] | 0.693 | 50 |
  | At least 4 ratings per product | 3,157 | 7,098 | 16,929 | 0.837 [0.832, 0.842] | 0.837 | 50 |

- **Direction/comparison:** The observed empirical reliability (0.695, F3.12) lies inside the simulated actual-design range [0.684, 0.699]. *(read off printed values)*
- **Caveats in data:** none beyond the note.
- **Simulation assumptions, VERBATIM** (N3 markdown `bad7fbeb`): "A projection built on the actual design (R/03_simulations.R). Two designs are simulated with the same machinery. In the design labelled actual, each product keeps exactly the raters who rated it. In the design labelled at least 4 ratings per product, each product keeps its raters, and every product with fewer than 4 ratings is assigned additional raters, drawn at random with equal probability and without replacement from the panel raters who had not rated it, until it has 4; products with 4 or more ratings are unchanged. In each of the 50 replications, every real product receives a creativity value θ drawn from N(0, 1), all ratings in the design (kept and added rater–product pairs alike) are generated from the fitted GRM, and the products are scored by EAP with the fitted parameters treated as known. The real ratings themselves are not reused; the actual-design row is a validation that should reproduce the observed empirical reliability of the real scores."

**F3.11 rel_post by number of ratings (figure)**
- **Finding:** Figure version of `tbl-grm-reliability-by-n`.
- **Linked object:** `fig-grm-rel-post-by-n`
- **Numbers:** See F2.4.
- **Direction/comparison:** —
- **Caveats in data:** —

**F3.12 Reliability with intervals**
- **Finding:** Empirical marginal reliability is 0.695 [0.673, 0.711] and model-based marginal reliability 0.970 [0.966, 0.973]. 200 draws were accepted and 53 rejected.
- **Linked object:** `tbl-grm-reliability-ci`
- **Numbers:**
  - empirical marginal reliability 0.695 (0.673–0.711), Draws 200, Draws rejected 53
  - model based marginal reliability 0.970 (0.966–0.973), Draws 200, Draws rejected 53
- **Direction/comparison:** —
- **Caveats in data:** Note `6b94d19e`, VERBATIM: "95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. … A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order".

**F3.13 Reliability summary**
- **Finding:** rel_post ranges from 0.071 to 0.955 across products (median 0.706). rel_post and rel_info correlate at 0.947.
- **Linked object:** `tbl-grm-reliability-summary`
- **Numbers (as printed):**
  - empirical marginal reliability (primary; actual scores) 0.695
  - model based marginal reliability mirt (hypothetical full panel) 0.970; grid (check) 0.970
  - var theta eap 0.695; mean psd squared 0.305
  - rel post: min 0.071, p10 0.507, q1 0.601, median 0.706, q3 0.796, p90 0.879, max 0.955, mean 0.695, iqr 0.195
  - consistency cor rel post rel info 0.947; consistency mean diff rel info minus rel post 0.014; consistency max abs diff 0.365; products abs diff gt 0.1: 274
- **Direction/comparison:** —
- **Caveats in data:** —

**F3.14 Naive indices: Cronbach's α and Krippendorff's α**
- **Finding:** Pairwise Cronbach's α is 0.959 (18 raters, 1,948 products; 487 of 1,000 bootstrap replications failed). Crossed-block α is 0.785 (3 raters, 270 products). Krippendorff's α (ordinal) is 0.402 (25 raters, 2,984 products).
- **Linked object:** `tbl-naive-indices`
- **Numbers (as printed):**

  | Index | Value | 95% CI lower | 95% CI upper | Raters | Products | Bootstrap replications | Failed replications |
  |---|---|---|---|---|---|---|---|
  | Cronbach's alpha: pairwise covariances, all usable raters | 0.959 | 0.931 | 0.970 | 18 | 1,948 | 1,000 | 487 |
  | Cronbach's alpha: fully crossed block (listwise complete) | 0.785 | 0.736 | 0.823 | 3 | 270 | 1,000 | 0 |
  | Krippendorff's alpha (ordinal) | 0.402 | 0.375 | 0.427 | 25 | 2,984 | 1,000 | 0 |

- **Direction/comparison:** —
- **Caveats in data:**
  - The seven raters dropped from the pairwise α are printed in `tbl-reliability-overview`: R26;R12;R19;R14;R02;R27;R17.
  - The **IDs of the 3 crossed-block raters are not printed**.
  - The pairwise-α CI is "approximate" (note `a8b49d80`).
  - The 2,984 products match the count of products with 2 or more ratings (N1 cumulative). *(read off printed values)*
- Further figures in this section, with no numbers printed beyond the tables above:
  - `fig-grm-rel-post-histogram`: distribution of rel_post.
  - `fig-grm-rel-post-by-theta`: rel_post by EAP, coloured by number of ratings.
  - `fig-grm-rel-consistency`: rel_info vs rel_post.
  - `fig-grm-panel-information`: full-panel information and I/(I+1). The caption says "The curve is hypothetical: it applies to a product rated by all raters."

### Simulated reliability by number of ratings

**F3.15 Projection by k and observed vs simulated**
- **Finding:** Simulated empirical reliability rises from 0.526 at k = 1 to 0.928 at k = 10. It first reaches at least .80 at k = 4 (0.832).
- **Linked object:** `tbl-grm-reliability-projection`, `fig-grm-reliability-projection` and `tbl-grm-reliability-observed-vs-simulated`
- **Numbers (as printed):**

  | k | Products (observed) | Observed mean rel_post | Simulated empirical reliability [95% range] | Simulated mean rel_post |
  |---|---|---|---|---|
  | 1 | 857 | 0.526 | 0.526 [0.511, 0.538] | 0.527 |
  | 2 | 2,227 | 0.703 | 0.702 [0.691, 0.712] | 0.703 |
  | 3 | 73 | 0.770 | 0.785 [0.776, 0.793] | 0.785 |
  | 4 | 93 | 0.815 | 0.832 [0.825, 0.838] | 0.832 |
  | 5 | 143 | 0.852 | 0.862 [0.857, 0.867] | 0.862 |
  | 6 | 185 | 0.879 | 0.883 [0.879, 0.889] | 0.883 |
  | 7 | 124 | 0.891 | 0.898 [0.892, 0.903] | 0.899 |
  | 8 | 77 | 0.904 | 0.911 [0.907, 0.914] | 0.911 |
  | 9 | 25 | 0.917 | 0.920 [0.916, 0.923] | 0.920 |
  | 10 | 22 | 0.915 | 0.928 [0.925, 0.932] | 0.928 |
  | 11 | 8 | 0.919 | – | – |
  | 12 | 5 | 0.931 | – | – |
  | 13 | 1 | 0.944 | – | – |
  | 14 | 1 | 0.955 | – | – |

  The last column comes from `tbl-grm-reliability-projection`. The other columns come from `tbl-grm-reliability-observed-vs-simulated`.
- **Direction/comparison** *(read off printed values)*:
  - The observed mean lies **inside** the simulated 95% range at k = 1, 2 and 9.
  - It lies **below** the range at k = 3, 4, 5, 7, 8 and 10.
  - At k = 6 the observed 0.879 **equals** the printed lower bound 0.879, so it is not distinguishable at printed precision (see Flags B5).
  - At every k from 3 to 10 the observed mean is below the simulated point estimate.
  - No simulation exists for k = 11–14.
- **Caveats in data:** As in F2.4, k ≥ 9 rests on 25 or fewer products.
- **Projection assumptions, VERBATIM** (N3 markdown `ab9edce2`): "A model-based gauge of the value of adding ratings, complementing the observed values. Products with θ ~ N(0, 1) are simulated; each gets k ratings from k raters of the actual panel, drawn at random, with ratings generated from the fitted GRM and scored with its parameters (treated as known). The table gives the empirical marginal reliability (mean and 95% range over replications) and the mean product-level reliability rel_post." The caption of `tbl-grm-reliability-projection` adds: "raters of the panel drawn at random (each equally likely) … 50 replications of 2,000 products". The seed is printed in N2 (F2.5): 20260713.

### Rater parameters, information, category use

**F3.16 Rater overview**
- **Finding:** The overview table combines raw mean, M1 severity, GRM a, information share, GRM fit and unused categories per rater, sorted by M1 severity.
- **Linked object:** `tbl-rater-overview`
- **Numbers (as printed):**

  | Rater | Ratings | Mean rating | Severity (M1) | a (GRM) | Share of panel information [95% interval] | Infit / outfit (GRM) | Unused categories |
  |---|---|---|---|---|---|---|---|
  | R19 | 250 | 4.01 | -1.00 | 1.97 | 3.3% [1.4, 5.8] | 0.54 / 0.57 † | – |
  | R18 | 55 | 3.84 | -0.82 | 0.65 | 0.4% [0.0, 1.1] | 0.98 / 0.97 | 7 |
  | R24 | 481 | 3.72 | -0.78 | 2.56 | 5.3% [3.8, 6.4] | 0.76 / 0.77 | – |
  | R13 | 254 | 3.68 | -0.71 | 1.49 | 1.8% [1.0, 2.7] | 0.85 / 0.85 | – |
  | R23 | 589 | 3.47 | -0.59 | 1.71 | 2.5% [1.8, 3.2] | 0.87 / 0.86 | – |
  | R09 | 400 | 3.64 | -0.59 | 0.95 | 0.8% [0.4, 1.3] | 0.87 / 0.87 | – |
  | R15 | 73 | 3.47 | -0.48 | 2.71 | 5.5% [2.8, 9.0] | 0.77 / 0.70 † | – |
  | R12 | 264 | 3.36 | -0.42 | 2.91 | 6.0% [3.3, 9.3] | 0.52 / 0.52 † | – |
  | R10 | 383 | 3.00 | -0.24 | 2.37 | 4.2% [2.2, 6.1] | 0.63 / 0.61 † | – |
  | R16 | 357 | 3.08 | -0.21 | 2.37 | 4.4% [3.2, 5.9] | 0.83 / 0.82 | – |
  | R25 | 138 | 3.03 | -0.20 | 3.03 | 6.7% [3.9, 9.6] | 0.75 / 0.74 | 7 |
  | R08 | 522 | 3.00 | -0.15 | 2.11 | 3.7% [2.3, 5.0] | 0.59 / 0.58 † | – |
  | R02 | 873 | 3.03 | -0.07 | 2.60 | 5.1% [2.8, 7.0] | 0.47 / 0.44 † | – |
  | R03 | 720 | 2.75 | 0.00 | 1.85 | 2.8% [1.8, 3.8] | 0.75 / 0.75 | 7 |
  | R26 | 136 | 2.85 | 0.11 | 4.17 | 11.2% [2.1, 20.5] | 0.31 / 0.30 † | 7 |
  | R04 | 620 | 2.82 | 0.16 | 2.05 | 3.3% [2.1, 4.5] | 0.62 / 0.58 † | – |
  | R05 | 633 | 2.72 | 0.17 | 2.36 | 4.3% [2.7, 6.2] | 0.62 / 0.62 † | – |
  | R30 | 47 | 2.64 | 0.25 | 2.69 | 4.9% [1.6, 9.4] | 0.84 / 0.68 † | – |
  | R07 | 547 | 2.40 | 0.53 | 1.91 | 2.7% [2.1, 3.8] | 0.82 / 0.72 | – |
  | R11 | 369 | 2.33 | 0.58 | 1.95 | 2.8% [1.9, 3.9] | 0.87 / 0.83 | – |
  | R17 | 52 | 2.08 | 0.68 | 1.73 | 2.1% [0.5, 4.3] | 0.93 / 0.87 | 6,7 |
  | R01 | 1174 | 2.16 | 0.76 | 1.79 | 2.4% [1.7, 3.2] | 0.73 / 0.70 † | 7 |
  | R27 | 47 | 2.06 | 0.80 | 2.85 | 5.0% [1.6, 10.3] | 0.67 / 0.68 † | 5,7 |
  | R14 | 327 | 2.22 | 0.84 | 2.45 | 3.9% [1.9, 6.6] | 0.54 / 0.46 † | – |
  | R06 | 520 | 1.76 | 1.38 | 3.15 | 4.9% [3.1, 7.5] | 0.59 / 0.45 † | 7 |

- **Direction/comparison: places where the raw-mean order and the M1 severity order disagree** *(read off printed values; offered to replace the old R18 illustration, which no longer holds)*:
  - **R14** has a raw mean of 2.22, higher than R01 (2.16), R17 (2.08) and R27 (2.06). Its M1 severity of 0.84 is higher (stricter) than theirs (0.76, 0.68, 0.80), and it is the second-strictest rater after R06.
  - **R09** has a raw mean of 3.64, higher than R23 (3.47), but both have an M1 severity of -0.59.
  - **R03** has a raw mean of 2.75, lower than R26 (2.85) and R04 (2.82), yet its severity of 0.00 is more lenient than theirs (0.11, 0.16).
  - **R17** has a raw mean of 2.08, lower than R01 (2.16), but a more lenient severity (0.68 against 0.76).
  - The top two match in both orders: R19 has the highest raw mean and the lowest severity, and R18 is second on both (3.84; -0.82).
- **Caveats in data:**
  - The table's † rule: "infit or outfit outside 0.7–1.3".
  - R15 ("0.77 / 0.70 †") and R01 ("0.73 / 0.70 †") print an outfit of 0.70 but carry †. Their unrounded outfits are 0.697 and 0.698 in `tbl-grm-rater-fit` (see Flags).

**F3.17 Rater information with intervals**
- **Finding:** Information per rating ranges from 0.13 (R18) to 3.96 (R26). R26's share of panel information is 0.112 [0.021, 0.205].
- **Linked object:** `tbl-grm-rater-information-ci`
- **Numbers (as printed; information per rating [95% interval] | share [95% interval]):**
  - R01 0.84 [0.61, 1.09] | 0.024 [0.017, 0.032]
  - R02 1.83 [1.09, 2.48] | 0.051 [0.028, 0.070]
  - R03 0.99 [0.61, 1.32] | 0.028 [0.018, 0.038]
  - R04 1.17 [0.75, 1.61] | 0.033 [0.021, 0.045]
  - R05 1.52 [1.07, 2.09] | 0.043 [0.027, 0.062]
  - R06 1.75 [1.04, 2.61] | 0.049 [0.031, 0.075]
  - R07 0.97 [0.75, 1.29] | 0.027 [0.021, 0.038]
  - R08 1.30 [0.86, 1.73] | 0.037 [0.023, 0.050]
  - R09 0.29 [0.16, 0.49] | 0.008 [0.004, 0.013]
  - R10 1.48 [0.80, 2.20] | 0.042 [0.022, 0.061]
  - R11 0.99 [0.63, 1.33] | 0.028 [0.019, 0.039]
  - R12 2.11 [1.14, 3.37] | 0.060 [0.033, 0.093]
  - R13 0.65 [0.36, 1.00] | 0.018 [0.010, 0.027]
  - R14 1.40 [0.68, 2.32] | 0.039 [0.019, 0.066]
  - R15 1.95 [0.99, 3.33] | 0.055 [0.028, 0.090]
  - R16 1.56 [1.10, 2.10] | 0.044 [0.032, 0.059]
  - R17 0.75 [0.15, 1.62] | 0.021 [0.005, 0.043]
  - R18 0.13 [0.00, 0.37] | 0.004 [0.000, 0.011]
  - R19 1.18 [0.51, 2.05] | 0.033 [0.014, 0.058]
  - R23 0.89 [0.66, 1.14] | 0.025 [0.018, 0.032]
  - R24 1.87 [1.35, 2.30] | 0.053 [0.038, 0.064]
  - R25 2.38 [1.43, 3.54] | 0.067 [0.039, 0.096]
  - R26 3.96 [0.66, 8.40] | 0.112 [0.021, 0.205]
  - R27 1.78 [0.57, 3.68] | 0.050 [0.016, 0.103]
  - R30 1.74 [0.57, 3.52] | 0.049 [0.016, 0.094]
- **Direction/comparison:** R26 has the widest interval. *(read off printed values)*
- **Caveats in data:** Intervals are from 200 accepted parameter draws (caption).

**F3.18 Information shares along θ (figure) and information summary**
- **Finding:** For each rater, the summary gives information per rating, the θ at maximum information, the maximum, and the share of panel information overall and at θ = −2 to 2.
- **Linked object:** `fig-grm-information-shares` (figure, no numbers printed) and `tbl-grm-information-summary`
- **Numbers (as printed; Information per rating | θ at max | Max information | Share | Share at θ = −2 / −1 / 0 / 1 / 2):**
  - R01 0.839 | 2.850 | 0.954 | 0.024 | 0.022/0.028/0.022/0.023/0.025
  - R02 1.826 | 0.400 | 2.141 | 0.051 | 0.014/0.050/0.053/0.053/0.050
  - R03 0.990 | 0.900 | 1.068 | 0.028 | 0.032/0.033/0.026/0.027/0.026
  - R04 1.167 | 0.650 | 1.340 | 0.033 | 0.020/0.035/0.032/0.033/0.032
  - R05 1.521 | 0.700 | 1.739 | 0.043 | 0.022/0.047/0.041/0.043/0.044
  - R06 1.755 | 2.300 | 3.026 | 0.049 | 0.001/0.007/0.055/0.074/0.078
  - R07 0.971 | 1.300 | 1.147 | 0.027 | 0.013/0.026/0.027/0.029/0.030
  - R08 1.296 | 0.350 | 1.383 | 0.037 | 0.040/0.044/0.034/0.034/0.034
  - R09 0.290 | 0.100 | 0.295 | 0.008 | 0.018/0.010/0.007/0.007/0.008
  - R10 1.479 | 0.500 | 1.727 | 0.042 | 0.098/0.033/0.042/0.042/0.042
  - R11 0.986 | 1.200 | 1.204 | 0.028 | 0.012/0.025/0.027/0.030/0.030
  - R12 2.114 | 1.400 | 2.328 | 0.060 | 0.151/0.076/0.055/0.052/0.061
  - R13 0.647 | -0.600 | 0.661 | 0.018 | 0.042/0.022/0.016/0.016/0.017
  - R14 1.397 | 0.800 | 1.856 | 0.039 | 0.005/0.021/0.043/0.046/0.048
  - R15 1.954 | 0.350 | 2.314 | 0.055 | 0.105/0.048/0.056/0.055/0.040
  - R16 1.561 | 2.550 | 1.635 | 0.044 | 0.076/0.052/0.039/0.040/0.041
  - R17 0.755 | 0.800 | 0.953 | 0.021 | 0.008/0.016/0.023/0.024/0.020
  - R18 0.130 | -0.450 | 0.132 | 0.004 | 0.009/0.004/0.003/0.003/0.003
  - R19 1.175 | -0.450 | 1.215 | 0.033 | 0.073/0.041/0.030/0.029/0.029
  - R23 0.891 | 0.300 | 0.911 | 0.025 | 0.052/0.031/0.023/0.022/0.023
  - R24 1.868 | -0.200 | 1.985 | 0.053 | 0.107/0.064/0.050/0.046/0.039
  - R25 2.378 | -0.450 | 2.603 | 0.067 | 0.057/0.085/0.063/0.060/0.055
  - R26 3.963 | 0.500 | 4.741 | 0.112 | 0.017/0.151/0.117/0.099/0.117
  - R27 1.784 | 0.600 | 2.482 | 0.050 | 0.004/0.025/0.058/0.057/0.053
  - R30 1.735 | 0.400 | 2.286 | 0.049 | 0.005/0.027/0.056/0.055/0.055
- **Direction/comparison:** —
- **Caveats in data:** —

### Adjacent-category ladder

**F3.19 Likelihood-ratio tests**
- **Finding:** M2 fits better than M1, χ²(110) = 878.581, p < .001, where the formula gives df 120. M3 fits better than M2, χ²(24) = 177.440, p < .001.
- **Linked object:** `tbl-lr-tests`
- **Numbers (as printed):**

  | Comparison | χ² | df | df if all categories used | df equal | p |
  |---|---|---|---|---|---|
  | M1 vs M2: rater-specific thresholds | 878.581 | 110 | 120 | False | < .001 |
  | M2 vs M3: rater-specific discriminations | 177.440 | 24 | 24 | True | < .001 |

- **Direction/comparison:** —
- **Caveats in data:** Note `ac96ef6d`, VERBATIM: "'df if all categories used' is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of categories raters never used (unused end categories and any internal gap)." The parameter counts are 31 / 141 / 165 / 165 (F2.3).

**F3.20 M3 discriminations**
- **Finding:** M3 discriminations range from 0.298 (R18) to 3.056 (R26), a max/min ratio of 10.254.
- **Linked object:** `tbl-discrimination-m3` and `tbl-discrimination-summary`
- **Numbers (estimate, SE, ascending):**
  - R18 0.298 (0.138); R09 0.316 (0.056); R17 0.775 (0.265); R23 0.824 (0.077)
  - R13 0.866 (0.150); R03 0.903 (0.113); R19 0.930 (0.252); R11 0.990 (0.133)
  - R07 1.021 (0.112); R04 1.037 (0.161); R08 1.088 (0.169); R05 1.211 (0.155)
  - R01 1.213 (0.106); R02 1.239 (0.220); R14 1.240 (0.306); R30 1.307 (0.474)
  - R10 1.395 (0.268); R16 1.504 (0.178); R24 1.588 (0.169); R15 1.606 (0.414)
  - R25 2.018 (0.399); R27 2.061 (0.760); R06 2.162 (0.393); R12 2.421 (0.592)
  - R26 3.056 (1.372)
  - Summary: min 0.298; q1 0.930; median 1.213; q3 1.588; max 3.056; ratio max min 10.254; sd 0.634.
- **Direction/comparison:** The lowest (R18) and highest (R26) raters are the same in M3 and the GRM (F2.7). *(read off printed values)*
- **Caveats in data:** —

**F3.21 Unordered step parameters**
- **Finding:** Nine raters have unordered steps in M2 and eight in M3.
- **Linked object:** `tbl-threshold-order`
- **Numbers (as printed):**
  - M2 (partial-credit MFRM):
    - R03 (5 steps, 1 reversal; -0.92;-0.24;1.10;0.69;2.68)
    - R04 (6, 1; -0.57;0.59;0.71;0.59;2.28;3.93)
    - R05 (6, 1; -0.80;0.59;0.57;1.46;1.82;2.75)
    - R06 (5, 1; 0.88;1.25;1.61;2.89;2.42)
    - R11 (6, 1; -0.33;1.02;1.15;1.05;2.81;4.36)
    - R15 (6, 1; -2.28;0.35;0.38;0.20;1.38;3.31)
    - R17 (4, 2; 0.47;0.17;1.31;1.08)
    - R27 (4, 1; 0.25;0.90;0.50;3.07)
    - R30 (6, 2; 0.33;0.11;0.52;0.99;3.15;1.81)
  - M3 (GPCM):
    - R03 (5, 1; -0.82;-0.21;1.15;0.60;2.67)
    - R04 (6, 1; -0.53;0.56;0.66;0.51;2.12;3.66)
    - R09 (6, 2; -0.42;-0.70;0.59;-0.04;1.09;3.66)
    - R11 (6, 1; -0.26;1.05;1.13;0.98;2.70;4.18)
    - R15 (6, 1; -1.85;0.16;0.33;0.31;1.18;2.76)
    - R17 (4, 2; 0.80;0.19;1.48;0.89)
    - R18 (5, 1; -7.55;-2.20;0.45;-0.74;5.21)
    - R30 (6, 2; 0.21;0.16;0.53;0.94;2.64;1.73)
- **Direction/comparison:** The counts 9 and 8 are *(read off printed values)*; they are not printed as numbers.
- **Caveats in data:** Note `d84db9cb`: "In the GRM, thresholds are ordered by construction."

**F3.22 M1 rater fit**
- **Finding:** Under M1, infit is above 1 for R09, R11, R17, R18 and R30, and outfit is above 1 for R09, R17, R18 and R30.
- **Linked object:** `tbl-rater-fit-m1`
- **Numbers (infit / outfit, as printed):**
  - R01 0.500/0.514; R02 0.853/0.840; R03 0.677/0.672; R04 0.737/0.700; R05 0.756/0.726
  - R06 0.893/0.700; R07 0.927/0.828; R08 0.585/0.590; R09 1.147/1.123; R10 0.450/0.430
  - R11 1.011/0.954; R12 0.259/0.276; R13 0.469/0.474; R14 0.772/0.716; R15 0.812/0.760
  - R16 0.552/0.576; R17 1.371/1.182; R18 1.233/1.307; R19 0.509/0.546; R23 0.814/0.806
  - R24 0.606/0.609; R25 0.457/0.486; R26 0.366/0.385; R27 0.768/0.743; R30 1.136/1.051
- **Direction/comparison** *(read off printed values)*:
  - The highest infit is R17's (1.371) and the highest outfit R18's (1.307).
  - The lowest infit/outfit is R12's (0.259 / 0.276).
  - R11's outfit (0.954) is below 1 while its infit (1.011) is above.
- **Caveats in data:** —

**F3.23 Correlations of scores between models**
- **Finding:** Pearson correlations between model scores range from 0.978 (M1–GRM) to 0.996 (M3–GRM). Spearman correlations range from 0.980 (M1–GRM) to 0.997 (M3–GRM).
- **Linked object:** `tbl-theta-correlations`
- **Numbers (as printed, off-diagonal):**
  - Pearson: M1–M2 0.993; M1–M3 0.982; M1–GRM 0.978; M2–M3 0.990; M2–GRM 0.986; M3–GRM 0.996.
  - Spearman: M1–M2 0.996; M1–M3 0.985; M1–GRM 0.980; M2–M3 0.988; M2–GRM 0.984; M3–GRM 0.997.
  - "M1, sirt default grid": 1.000 with M1 (Pearson and Spearman). Its other entries equal M1's.
- **Direction/comparison:** —
- **Caveats in data:** The sirt default-grid row is a software check (caption).

**F3.24 Marginal and empirical reliability per model**
- **Finding:** Empirical reliability of the obtained scores is 0.663 (M1), 0.669 (M2), 0.682 (M3) and 0.695 (GRM). Marginal (full-panel) reliability is 0.960, 0.959, 0.966 and 0.970.
- **Linked object:** `tbl-marginal-reliability-models`
- **Numbers (as printed):**

  | Model | Latent variance | Marginal reliability | marginal_rxx (mirt) | Empirical reliability |
  |---|---|---|---|---|
  | M1 (rating-scale MFRM) | 1.109 | 0.960 | – | 0.663 |
  | M2 (partial-credit MFRM) | 1.192 | 0.959 | – | 0.669 |
  | M3 (GPCM) | 1.000 | 0.966 | 0.966 | 0.682 |
  | GRM | 1.000 | 0.970 | 0.970 | 0.695 |

- **Direction/comparison:** Empirical reliability increases in the order M1 < M2 < M3 < GRM. *(read off printed values)*
- **Caveats in data:** —

---

## Flags

**Differences from, and checks against, the revision brief (section B)**

- **Freeze facts:**
  - 11,323 rows ✓ (N0 "11323").
  - 9,863 cleaned ratings by 30 raters ✓ (N0).
  - 9,831 ratings of 3,841 products by 25 raters ✓.
  - Excluded R20, R21, R22, R28, R29 ✓.
  - Retained R01–R19, R23–R27, R30 ✓.
  - No deviation.
- **B1:** ΔBIC of the GRM is 0.416 ✓ ("about 0.4"). Within the ladder, BIC is lower for M1 than M2 and lower for M2 than M3, so BIC favours the constrained model in both comparisons. A direct M2–M3 BIC difference is not printed.
- **B2:**
  - R19 is the most lenient rater at −1.005 ✓, and the span is 2.388 ✓.
  - R19 has the highest raw mean ✓.
  - The old R18 illustration does not hold: R18 is second on both the raw-mean and severity orders. Candidate replacements are in F3.16, with R14 as the clearest case.
- **B3:**
  - R26 has 136 ratings ✓ and a = 4.17 (SE 1.49) ✓. R24 has 481 ✓.
  - R17 (52), R18 (55), R27 (47) and R30 (47) ✓.
  - R16 has 357 ✓. R15 has 73, between the ~50 group and the rest (not named in the brief).
- **B4:** At one rating, τ-b is 0.773 ✓ and the reversed share 0.076 ✓. At two ratings the reversed share is 0.066 ✓.
- **B5:**
  - One dip at 10 ratings (22 products) ✓ for mean rel_post. Median rel_post has a separate dip at 11 ratings (0.925 < 0.926); the brief does not mention it.
  - **Difference:** the brief says observed means lie below the simulated range at 3–8 and 10. At k = 6 the observed 0.879 equals the printed lower bound 0.879, so "below" cannot be stated at printed precision. Below the range at printed precision: k = 3, 4, 5, 7, 8 and 10. Inside: 1, 2 and 9.
  - Products from 10 ratings up: 22, 8, 5, 1, 1 ✓.
- **B6:**
  - The pairwise α drops seven raters including R17 ✓ (R26;R12;R19;R14;R02;R27;R17).
  - The crossed block has 3 raters × 270 products, α 0.785 ✓.
  - **Difference:** the crossed-block rater IDs "R07, R23, R24" are **not printed in any notebook** and so are not quotable.
- **B7:**
  - χ²(110) = 878.581, formula df 120 ✓. χ²(24) = 177.440 ✓.
  - Parameter counts 31/141/165/165 ✓. M3 ratio 10.254 ✓, R26 3.056 ✓.
  - Under M1, values above 1 occur for R09 (both), R11 (infit only), R17 (both), R18 (both) and R30 (both) ✓.
- **B8:** All-raters refit has 29 raters ✓ (R29 "one category, not estimable"). r = 0.99997 ✓ and the largest θ change is 0.16518 ✓.
- **B9:**
  - All design counts ✓: raw 11323; not recognised 1432; 26 pairs / 27 rows; 9863 by 30; 32 excluded; 1 product dropped; ratings per rater 47–1,174; mean 2.559, median 2, range 1–14; fill 0.102; 23 of 300; median overlap 22.500.
  - 8 raters with category gaps, 1 with an internal gap (R27) ✓. R17 and R27 have four thresholds ✓.
  - The 53 rows involved in duplicates (N0) is an additional printed value.
- **C4 (brief, storytelling):** the brief writes "spread over up to about 2 logits". The notebook prints "Maximum θ̂ range at equal raw mean" 2.129 on the GRM θ̂ scale and gives no unit; "logits" is the brief's wording.

**Notebook inconsistencies and display issues that affect quoting**

1. **R09 raw mean:**
   - N1 `fb6df84b` (`round(3)`) prints 3.642.
   - The labelled `tbl-overview-rater-response-styles` prints 3.643.
   - `tbl-rater-overview` prints 3.64.
   - Quote the labelled-table value 3.643, or 3.64.
2. **† flags at a printed 0.70** in `tbl-rater-overview`: R15 ("0.77 / 0.70 †") and R01 ("0.73 / 0.70 †") look inside 0.7–1.3 at 2 decimals. Their unrounded outfits in `tbl-grm-rater-fit` are 0.697 and 0.698.
3. **`tbl-sensitivity-rater-exclusion`** prints "R20;R21;R22;R28;R29;R29 (one category, not estimable)", with R29 listed twice. The "excluded raters" row in the "All raters" column lists the included low-count raters, and R29 is marked not estimable, so "29 raters" = 25 + R20, R21, R22, R28.
4. **Precision varies across objects:**
   - Average ratings per product: N1 stdout prints 2.56, the tables print 2.559.
   - Median ratings per rater is 369 (N1 table). Median ratings per *product* is 2 (N2 table). Do not confuse the two.
5. **Thousands separators:** N1 and `tbl-rater-overview` print "1174"; the other N2/N3 tables print "1,174".
6. **Stale note in N0** (markdown cells `64b27fc9` and `73ef4dcd`): it refers to analysis notebooks "`02a`–`02d`, `03`, and `02_creativity_ratings_R.qmd`", which are not the current pipeline. The note has no numbers. No stale counts and no "four excluded raters" wording were found in N0–N3.
7. **N3 `tbl-grm-q3-flagged`** lists the top 10 pairs. The stdout reports 36 flagged pairs over 256 computable pairs. The other 26 flagged pairs are not listed.
8. **Bootstrap counts for the pairwise Cronbach's α:** `tbl-reliability-overview` says "513 of 1,000 replications computable" and `tbl-naive-indices` says "Failed replications 487". These are consistent.

---

## Not found (expected by the brief or the old findings, but printed by no notebook)

- IDs of the 3 raters in the fully crossed Cronbach block (brief: R07, R23, R24).
- Data fingerprint (md5) of the analysed data.
- M1 severity SEs for raters other than R19 (0.059) and R06 (0.058). The others appear only as error bars in `fig-m1-rater-severity`.
- Median GRM discrimination (drawn as a dashed line in `fig-grm-rater-discrimination-ci` only), and a GRM max/min discrimination ratio.
- The number of raters flagged by GRM infit/outfit (14 daggers can be counted, but no count is printed).
- Direct pairwise BIC/AIC differences between non-best models (for example M2 − M3). Only Δ to the best model is printed.
- Simulated reliability for k > 10.
- Krippendorff's α by number of ratings per product.
- Per-rater non-recognition counts or rates. Only the total of 1432 is printed.
- The data-collection period. Only five timestamps of 2026-10-23 appear in a `head()` preview.
- Rater background, recruitment and allocation rule.
- Any significance test of differences in reliability between models.

## Not quotable (not sources per brief section B; values existing only there must not be used)

- `notebooks/01_data_overview_new_ratings.ipynb`: not opened.
- `notebooks/04_score_analysis.ipynb`: not opened (exploratory, unlabelled).
- `notebooks/local_rater_lookup.ipynb`: private, not opened.
- `results/krippendorff_by_n_ratings.csv` and `R/krippendorff_by_n_ratings.R`: standalone. **No Krippendorff-by-n value is quotable.**
- `results/figures/rating_progress.png`, `reports/`, `kolloq-presentation/` and its `scripts/`, `AUDIT.md`, and any archived data.
- The README "Data behind the committed results" freeze facts. They coincide with the notebook values listed above; quote the notebooks.
- The crossed-block rater IDs (R07, R23, R24) exist only in the brief, not in notebooks 00–03.
- Any value in the previous `manuscript/03_findings.md` (old freeze), including 9,046 / 3,669 / 24 raters / 4.161 and the other stale strings in brief section B.
