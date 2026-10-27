> **Orchestrator note (2026-10-27, re-run after commit 04aefc5).** The interpreter's output below is copied byte for byte. 02_artifacts.md was regenerated in parallel (43 labels incl. tbl-overview-rater-response-styles), so any flag calling it stale is resolved.
> Values listed as removed or NOT IN NOTEBOOK must not be quoted. Quote R09's mean as printed in the embedded object being cited (3.643 in tbl-overview-rater-response-styles).

# 03_findings.md: Results findings (results-interpreter, Phase 4 re-run after commit 04aefc5)

## Changes vs previous findings

1. **Values are unchanged. The only real difference is one rounding: R09's mean.**
   - **What I compared.** Every printed cell in N0 `tbl-cleaning-log`, the N1 stdout, N1 `tbl-overview-ratings-per-action` and all 26 N2 tables, against the previous file. Apart from the display changes below, all values match.
   - **The R09 difference.** The R09 rater mean prints **3.643** in the new embedded table `tbl-overview-rater-response-styles` (N1 `ovtbl02`). The unlabelled cell `fb6df84b` still prints **3.642**.
   - **Why the two cells differ.** Both cells show the same `rater_desc` data frame:
     - `fb6df84b` uses pandas `.round(3)`;
     - `ovtbl02` uses `fmt_cell` (`f"{v:.3f}"`).
     - The difference comes only from these two display paths; the stored value is the same.
   - **Which form to quote.** Quote 3.643 when citing the embedded table, and 3.642 only when citing `fb6df84b`. Do not mix the two forms.
2. **New N1 table `tbl-overview-rater-response-styles`** (cell `ovtbl02`). This is now the linked object for F0.8.
   - The values and headers are under F0.8. Apart from R09's mean (item 1), every value matches the previous F0.8.
   - The new table drops the n_products column. Whole numbers now print without decimals: "520", "3", "1", "0".
   - N1 now has 6 labels (2 tables, 4 figures), so the total is 43 labels.
3. **Model labels in N2 cells.**
   - The cells now print "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)" and "GRM".
   - "M1 (RSM/MFRM)" and "M2 (PCM)" are **no longer printed in any table cell**.
   - Places that still use the old forms:
     - the `tbl-threshold-order` **caption** ("M2 (PCM) and M3 (GPCM)");
     - the `tbl-reliability-overview` row labels ("M1 (RSM): marginal reliability", "M2 (PCM): marginal reliability").
   - The `tbl-model-fit` and `tbl-rater-fit-m1` captions are unchanged ("M1 rating scale model / MFRM", "M1 (rating scale model / MFRM)").
4. **Ratings headers in N2.** The header "Ratings (n)" is **no longer printed**. It has three replacements:
   - "Ratings by rater": tbl-excluded-raters, tbl-category-usage, tbl-grm-rater-parameters, tbl-grm-rater-fit, tbl-grm-information-summary, tbl-grm-rater-information-ci, tbl-discrimination-m3, tbl-rater-fit-m1.
   - "Ratings per product": tbl-grm-reliability-by-n, tbl-raw-mean-vs-grm.
   - "Ratings (total)": tbl-grm-convergence.
5. **Two captions lost a sentence.** In the `tbl-grm-information-summary` and `tbl-grm-rater-information-ci` captions, the sentence "Ratings (n) is the number of ratings the rater gave." is gone. The current captions are under F2.3 and F2.4.
6. **The Q3 note now defines a computable pair.** The verbatim note is in F1.9. The former caveat, Not-found item and Flag 5 ("computable is not defined") are removed.
7. **All N2 cell ids changed again.** The new ids are given in each finding. N0 and N1 ids are unchanged; the only new N1 cell is `ovtbl02`. `02_artifacts.md` lists the old N2 ids and does not list `tbl-overview-rater-response-styles` (see Flag 2).
8. **Removed values: still NOT quotable.**
   - **Projection with most/least-informative raters:**
     - most_informative 0.754 (k = 1) to 0.947 (k = 10); least_informative 0.108 (k = 1) to 0.884 (k = 10);
     - every intermediate value (for example .859, .920, .260, .701);
     - every comparison between schemes ("most > random > least", "gap narrows with k", "k = 1: 0.754 / 0.508 / 0.108").
   - `true_r2` and its quantiles (for example 0.508 [0.480, 0.542]), and the quantiles of mean_rel_post (for example 0.500, 0.517).
   - **Pooled raw-mean "all" row:** 3668 as a row, Pearson .906, Spearman .932, mean shift .080, p95 shift .216, max shift .551, share changing quintile .350, ≥ 2 quintiles .022, ties-resolved .237, discordant pairs .083, τ-b .796, tied raw mean .995, mean θ̂ range .814, max θ̂ range 2.252.
   - **Raw-mean subgroup columns:**
     - Pearson (.921 / .922 / .954) and Spearman (.940 / .933 / .959);
     - percentile shifts (.074 / .075 / .060; .203 / .234 / .177; .334 / .562 / .400);
     - share changing quintile (.385 / .319 / .266) and ≥ 2 quintiles (.004 / .028 / .006);
     - ties-resolved (.104 / .220 / .220); tied raw mean (1 / 1 / .971).
   - **Precision not printed:** rater-information CI bounds at 3 decimals (for example [0.410, 11.017], [0.728, 6.489]) and GRM rater parameters at 3 decimals (for example 3.709 (2.220)).
   - **Removed sentences and phrases:**
     - "The observed relation above is confounded …";
     - "which brackets the effect of who rates";
     - "overstates the disagreement and is not comparable with the model comparison above".
   - **Old display forms:** Tolerance "0.000" or "0.0001"; M3 ≥ 2 quintiles "0.000545256".
   - **Headers and labels no longer printed (new this run):**
     - "Ratings (n)" as a header;
     - "M1 (RSM/MFRM)" and "M2 (PCM)" as table cell labels (they remain in the threshold-order caption and the overview rows, as noted in item 3);
     - the caption sentence "Ratings (n) is the number of ratings the rater gave."
   - **Context files only:** AUDIT.md's "6 unused end categories" and REPORT.md's infit/outfit range 0.7–1.3.

---

Notebooks (the only quotable sources):
- **N0** = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- **N1** = `.../notebooks/01_data_overview.ipynb`
- **N2** = `.../notebooks/02_jrt_results.ipynb` (main)

How to read this file:
- **Values** are copied exactly as printed.
- **N2 formatting:** N2 tables go through `tidy()` / `fmt_cell`.
  - Numbers have 3 decimals and thousands separators. `tbl-sensitivity-rater-exclusion` is the exception, with 5 decimals.
  - `est_se()` formats as "estimate (SE)" with 2 decimals.
  - `est_ci()` formats as "estimate [low, high]": 2 decimals for information, 3 for shares and the projection.
  - Whole numbers print without decimals.
  - p < .001 prints in scientific notation.
  - Missing values print as "–".
- **N1 formatting:**
  - `ovtbl01` and `ovtbl02` use N1's own `fmt_cell`: no separators, whole numbers without decimals.
  - `fb6df84b` prints with `round(3)`, so counts appear as floats ("520.0").
- **Context files:** AUDIT.md, REPORT.md, ANALYSIS_TODO.md and the R scripts were read for definitions only. A value found only there is marked **NOT IN NOTEBOOK — not quotable**.

**Post-exclusion check.** N1 and N2 both report the final data as 7,820 ratings, 3,668 products and 19 raters.
- N1 `f6039400` stdout: "Loaded 7844 ratings; excluded 24 ratings from 3 raters with fewer than 15 ratings (R20, R21, R22); 7820 ratings remain."
- N1 `981d6824`: Total ratings 7820; Distinct products 3668; Distinct raters 19.
- N2 `tbl-design-summary`: n ratings 7,820; n products 3,668; n raters 19.
- N0 is pre-exclusion, as expected (22 raters, 7844 rows, 3669 actions).

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

  - One out-of-range value was dropped: 0.0 (R04).
  - "Rows with a duplicate (action_id, rater_id) combination: 25". One pair conflicts: R14 gave 2.0 and 1.0. The rule is that the last entry is kept.
  - Stdout also prints: "Raters pseudonymised: 22", "Raters: 22", "Actions: 3669", "Warnings collected: 3".
- **Caveats:** These values are pre-exclusion. The cleaning log stops at 7844 and has no rater-exclusion row.

**F0.2 Rater exclusion** *(values unchanged; new N2 ids; header "Ratings by rater")*
- **Finding:** Three raters with fewer than 15 ratings were excluded. Together they gave 24 ratings, and their exclusion dropped 1 product.
- **Linked objects:**
  - `tbl-excluded-raters` (N2, `118a628a`). Headers: Rater | Ratings by rater | Reason.
  - `tbl-design-summary` (N2, `28af567a`). Headers: Quantity | Value.
- **Numbers:**
  - R20 13, R21 9, R22 2. Each has the reason "fewer than 15 ratings".
  - Design summary: min_ratings_per_rater (exclusion cut-off) 15; raters excluded R20;R21;R22; ratings excluded 24; products dropped 1.

**F0.3 Final design** *(values unchanged; new N2 id)*
- **Finding:** The final design has 7,820 ratings of 3,668 products by 19 raters. It is sparse but forms one connected component.
- **Linked objects:**
  - `tbl-design-summary` (N2, `28af567a`).
  - The same values appear in `tbl-overview-ratings-per-action` (N1, `ovtbl01`) and in N1 `981d6824` / `bacf60d8`.
- **Numbers (N2, as printed):**
  - n ratings 7,820; n products 3,668; n raters 19.
  - n categories 7; scale 1-7; internal coding "rating - 1 (0-6)".
  - ratings per product mean 2.132, median 2, min 1, max 10, harmonic mean 1.726; products with 1 rating 897.
  - ratings per rater min 50, max 1,174.
  - matrix fill 0.112; n components 1.
  - rater pairs total 171, without overlap 17, overlap median 13.
  - raters with category gaps 5; raters with internal gap 0.
  - duplicate pairs resolved in 00 12; duplicate pairs conflicting 1.
- **Numbers (N1 `ovtbl01`):**
  - n_ratings 7820; n_products 3668; n_raters 19.
  - n_products_1_rating 897; n_products_2_ratings 2080; n_products_3plus_ratings 691.
  - share_products_1_rating 0.245; share_products_2_ratings 0.567; share_products_3plus_ratings 0.188.
  - max_ratings_per_product 10; mean_ratings_per_product 2.132; harmonic_mean_ratings_per_product 1.726.
  - median_ratings_per_rater 383; min_ratings_per_rater 50; max_ratings_per_rater 1174.
- **N1 stdout:**
  - `981d6824`: "Average ratings per product: 2.13"; "Average ratings per rater: 411.6".
  - `bacf60d8`: "Number of connected components: 1"; that component has 3668 products and 19 raters.
- **Notebook statement (N2 `81bc0525`):** "A connected design (one component) is required so that all raters and products lie on one scale (Eckes, 2015)."
- **Caveats:** 17 of the 171 rater pairs share no product. 897 products have a single rating.

**F0.4 Distribution of ratings per product** *(unchanged)*
- **Finding:** Most products have 2 ratings, and the counts fall off steeply above 2.
- **Linked object:** `fig-overview-degree-distributions` (N1, `ovfig04`). The numbers come from unlabelled N1 `3b12b8bf` (stdout).
- **Numbers:**

  | ratings per product | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | products | 897 | 2080 | 357 | 125 | 125 | 47 | 20 | 11 | 3 | 3 |

  Cumulative: 1 or more 3668; 2 or more 2771; 3 or more 691; 4 or more 334; 5 or more 209; 6 or more 84; 7 or more 37; 8 or more 17; 9 or more 6; 10 or more 3.
- **Caveat:** Only 3 products have 9 ratings and only 3 have 10.

**F0.5 Ratings per rater and pairwise overlap** *(unchanged)*
- **Finding:** Raters gave between 50 and 1174 ratings each. The five raters with the fewest ratings also have the lowest overlap with their best-connected partner.
- **Linked object:** `fig-overview-rater-overlap` (N1, `ovfig01`). The numbers come from unlabelled N1 `3b12b8bf` and `aa371443`.
- **Numbers:**
  - Ratings per rater: R19 50, R16 52, R17 52, R18 55, R15 73, R13 254, R14 259, R12 264, R11 369, R10 383, R09 400, R06 520, R08 522, R07 547, R04 620, R05 633, R03 720, R02 873, R01 1174.
  - Best-partner overlap: R17 44, R18 46, R19 46, R16 52, R15 61, R14 108, R12 145, R09 147, R13 154, R10 157, R05 190, R08 191, R06 240, R02 257, R04 257, R01 329, R03 329, R07 357, R11 357.

**F0.6 Category frequencies across all ratings** *(unchanged)*
- **Finding:** Ratings concentrate at the low end of the scale, and category 7 is the rarest.
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

**F0.7 Category use per rater** *(values unchanged; new id; header "Ratings by rater")*
- **Finding:** Five raters left at least one category unused, always at the top of the scale. No rater has an internal gap.
- **Linked object:** `tbl-category-usage` (N2, `08803894`).
- **Numbers (headers as printed):**

  | Rater | Category 1 | Category 2 | Category 3 | Category 4 | Category 5 | Category 6 | Category 7 | Ratings by rater | Missing categories | Internal gap |
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

- **Caveat (notebook, `57860214`):** "Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used."

**F0.8 Rater response styles (descriptive)** *(UPDATED: now linked to a labelled table; values verified)*
- **Finding:** Rater means range from 1.760 (R06) to 3.836 (R18). Raters also differ in SD, entropy, the share of ratings in the lowest and highest category, and the use of extreme versus middle categories.
- **Linked objects:**
  - **`tbl-overview-rater-response-styles`** (N1, `ovtbl02`, NEW).
  - `fig-overview-rater-response-styles` (N1, `ovfig03`).
  - Source frame: unlabelled N1 `fb6df84b` (19 rows, post-exclusion, sorted by mean).
- **Caption (verbatim):** "Descriptive response styles per rater: number of ratings, mean, median, standard deviation and interquartile range of the ratings, number of categories used (of 7), entropy of the category distribution, and the shares of ratings in the lowest category (1), the highest category (7), the extreme categories (1 or 7) and the middle categories (3 to 5)."
- **Numbers (exactly as printed in `ovtbl02`, headers verbatim):**

  | Rater | Ratings by rater | Mean | Median | SD | IQR | Categories used | Entropy | Share lowest (1) | Share highest (7) | Share extreme (1, 7) | Share middle (3-5) |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | R06 | 520 | 1.760 | 1 | 1.111 | 1 | 6 | 1.191 | 0.579 | 0 | 0.579 | 0.192 |
  | R17 | 52 | 2.077 | 2 | 1.296 | 2 | 5 | 1.367 | 0.481 | 0 | 0.481 | 0.327 |
  | R01 | 1174 | 2.164 | 2 | 1.022 | 2 | 6 | 1.358 | 0.287 | 0 | 0.287 | 0.315 |
  | R14 | 259 | 2.220 | 2 | 1.359 | 2 | 7 | 1.496 | 0.405 | 0.008 | 0.413 | 0.313 |
  | R11 | 369 | 2.333 | 2 | 1.397 | 2 | 7 | 1.532 | 0.344 | 0.003 | 0.347 | 0.309 |
  | R07 | 547 | 2.404 | 2 | 1.406 | 2 | 7 | 1.580 | 0.335 | 0.004 | 0.338 | 0.353 |
  | R05 | 633 | 2.716 | 2 | 1.554 | 3 | 7 | 1.700 | 0.251 | 0.019 | 0.270 | 0.382 |
  | R03 | 720 | 2.750 | 3 | 1.402 | 2 | 6 | 1.643 | 0.224 | 0 | 0.224 | 0.493 |
  | R04 | 620 | 2.821 | 2 | 1.628 | 3 | 7 | 1.715 | 0.265 | 0.008 | 0.273 | 0.405 |
  | R10 | 383 | 2.997 | 3 | 1.311 | 2 | 7 | 1.564 | 0.065 | 0.005 | 0.070 | 0.488 |
  | R08 | 522 | 3 | 3 | 1.545 | 2 | 7 | 1.761 | 0.193 | 0.013 | 0.207 | 0.492 |
  | R02 | 873 | 3.032 | 3 | 1.841 | 3 | 7 | 1.822 | 0.276 | 0.052 | 0.328 | 0.391 |
  | R12 | 264 | 3.360 | 3 | 1.152 | 1 | 7 | 1.547 | 0.042 | 0.004 | 0.045 | 0.735 |
  | R16 | 52 | 3.442 | 3 | 1.589 | 2 | 7 | 1.762 | 0.077 | 0.058 | 0.135 | 0.538 |
  | R15 | 73 | 3.466 | 3 | 1.700 | 3 | 7 | 1.793 | 0.096 | 0.027 | 0.123 | 0.452 |
  | R09 | 400 | 3.643 | 4 | 1.819 | 3 | 7 | 1.903 | 0.158 | 0.055 | 0.212 | 0.495 |
  | R19 | 50 | 3.680 | 4 | 1.953 | 3 | 7 | 1.902 | 0.200 | 0.080 | 0.280 | 0.480 |
  | R13 | 254 | 3.681 | 4 | 1.116 | 1 | 7 | 1.520 | 0.016 | 0.004 | 0.020 | 0.799 |
  | R18 | 55 | 3.836 | 4 | 1.259 | 2 | 6 | 1.584 | 0.018 | 0 | 0.018 | 0.764 |

- **Check against the previous F0.8 (`fb6df84b`, `round(3)`):**
  - Every value matches **except R09's Mean: 3.643 here vs 3.642 in `fb6df84b`** (see Changes item 1).
  - The other differences are formatting only:
    - whole numbers now print without decimals (counts "520" instead of "520.0"; R08 Mean "3" instead of "3.000"; Median, IQR and Categories used as integers);
    - Share highest (7) prints "0" instead of "0.000" for R06, R17, R01, R03 and R18.
  - The n_products column is dropped. It equalled n_ratings for every rater in `fb6df84b`.
  - The headers are new. Old → new: n_ratings → Ratings by rater; floor_rate → Share lowest (1); ceiling_rate → Share highest (7); extreme_category_rate → Share extreme (1, 7); central_category_rate → Share middle (3-5).
- **Direction (read off the printed values):**
  - SD: lowest R01 (1.022), highest R19 (1.953).
  - Entropy: lowest R06 (1.191), highest R09 (1.903).
  - Share lowest (1): highest R06 (0.579), lowest R13 (0.016).
  - Share highest (7): highest R19 (0.080). Five raters print 0: R06, R17, R01, R03 and R18.
  - Share extreme (1, 7): highest R06 (0.579), lowest R18 (0.018).
  - Share middle (3-5): highest R13 (0.799), lowest R06 (0.192).
- **Definitions (notebook `f3482d97` and the `fb6df84b` code):**
  - Extreme means categories 1 and 7; middle means categories 3–5.
  - Entropy uses the natural logarithm.
  - Notebook framing in `f3482d97`: these descriptives "anticipate what the models estimate formally".
- **Caveats:**
  - These are raw 1–7 values, not adjusted for which products each rater saw.
  - R15, R16, R17, R18 and R19 have 50–73 ratings each.
  - N1 `9f03e286` prints "Raters with <= 2 rated products: 0".

## (b) Model comparison

**F1.1 Information criteria** *(values unchanged; new id; new model labels)*
- **Finding:** The GRM has the lowest AIC, BIC and SABIC of the four models. Within the adjacent-category ladder, M3 has the lowest AIC and SABIC, and M2 the lowest BIC.
- **Linked object:** `tbl-model-fit` (N2, `52299a6b`).
- **Numbers:**

  | Model | Software | Family | Log-likelihood | Parameters | AIC | BIC | SABIC | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | sirt::rm.facets | adjacent category | -12,186.218 | 25 | 24,422.435 | 24,577.620 | 24,498.183 | 701.980 | 68.825 | 392.931 |
  | M2 (partial-credit MFRM) | mirt | adjacent category | -11,817.489 | 109 | 23,852.978 | 24,529.585 | 24,183.237 | 132.524 | 20.790 | 77.985 |
  | M3 (GPCM) | mirt | adjacent category | -11,756.510 | 127 | 23,767.020 | 24,555.360 | 24,151.817 | 46.566 | 46.566 | 46.566 |
  | GRM | mirt | cumulative (not in LR ladder) | -11,733.227 | 127 | 23,720.455 | 24,508.795 | 24,105.251 | 0 | 0 | 0 |

- **Caption:** "Fit of the adjacent-category ladder (M1 rating scale model / MFRM, M2 partial credit model, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion."
- **Caveat (notebook, `20e48964`):** "The GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better)."

**F1.2 Likelihood-ratio tests** *(values unchanged; new ids)*
- **Finding:** Both steps up the adjacent-category ladder give significant LR tests.
- **Linked object:** `tbl-lr-tests` (N2, `48b49851`).
- **Numbers:**

  | Comparison | χ² | df | df if all categories used | df equal | p |
  |---|---|---|---|---|---|
  | M1 vs M2: rater-specific thresholds | 737.457 | 84 | 90 | False | 4.22e-105 |
  | M2 vs M3: rater-specific discriminations | 121.958 | 18 | 18 | True | 1.79e-17 |

- **Notebook explanation (verbatim, `2bf87a03`):** "\"df if all categories used\" is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories."
- **Caption:** "Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2."
- **Caveats:**
  - The number of unused end categories is not printed as a single figure. The per-rater pattern is in F0.7. AUDIT.md's "6" is NOT IN NOTEBOOK — not quotable.
  - M1 was fitted in sirt and M2 in mirt.

**F1.3 GRM estimation** *(values unchanged; new id; header "Ratings (total)")*
- **Finding:** The GRM converged, and its information matrix is positive definite.
- **Linked object:** `tbl-grm-convergence` (N2, `849e3d5b`).
- **Numbers:**
  - Method EM; Quadrature points 61; SE type Oakes; Tolerance 10⁻⁴.
  - Converged True; Iterations 165; Information matrix positive definite True.
  - Log-likelihood -11,733.227; Parameters 127; AIC 23,720.455; BIC 24,508.795; SABIC 24,105.251.
  - Products 3,668; Ratings (total) 7,820.

**F1.4 Discriminations in M3 (GPCM)** *(values unchanged; new id; "Ratings by rater")*
- **Finding:** M3 rater discriminations range from 0.283 (R09) to 2.606 (R16).
- **Linked object:** `tbl-discrimination-m3` (N2, `293a100e`). Headers: Rater | Ratings by rater | Estimate | SE.
- **Numbers (in printed order):** R09 400 0.283 (0.055); R18 55 0.312 (0.145); R17 52 0.616 (0.235); R13 254 0.863 (0.159); R11 369 0.896 (0.145); R03 720 0.984 (0.142); R04 620 0.992 (0.184); R07 547 1.025 (0.138); R05 633 1.096 (0.154); R08 522 1.102 (0.195); R02 873 1.209 (0.272); R01 1,174 1.304 (0.131); R10 383 1.370 (0.320); R15 73 1.389 (0.412); R14 259 1.390 (0.433); R06 520 1.942 (0.385); R19 50 2.327 (1.866); R12 264 2.383 (0.680); R16 52 2.606 (1.419).
- **Caveats:**
  - The largest SEs belong to R19 (1.866) and R16 (1.419). Both gave about 50 ratings.
  - Notebook framing (`8307cc03`): "Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data."

**F1.5 Unordered step parameters in M2/M3** *(values unchanged; new id; model label "M2 (partial-credit MFRM)")*
- **Finding:** Nine raters have unordered steps in M2, and nine in M3.
- **Linked object:** `tbl-threshold-order` (N2, `2ea683db`).
  - Headers: Model | Rater | Steps | Ordered | Reversals | Step parameters. Ordered is False in every row.
  - The caption still reads "Raters with unordered step parameters in M2 (PCM) and M3 (GPCM)." The cells print "M2 (partial-credit MFRM)".
- **Numbers (Rater, Steps, Reversals, Step parameters):**
  - M2 (partial-credit MFRM):
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
- **Caveat (notebook, `0540fce1`):** "In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction."

**F1.6 Marginal and empirical reliability by model** *(values unchanged; new id; new labels)*
- **Linked object:** `tbl-marginal-reliability-models` (N2, `392a5197`).
- **Numbers:**

  | Model | Latent variance | Marginal reliability | marginal_rxx (mirt) | Empirical reliability |
  |---|---|---|---|---|
  | M1 (rating-scale MFRM) | 0.962 | 0.943 | – | 0.626 |
  | M2 (partial-credit MFRM) | 1.087 | 0.944 | – | 0.637 |
  | M3 (GPCM) | 1 | 0.955 | 0.955 | 0.657 |
  | GRM | 1 | 0.960 | 0.960 | 0.672 |

- **Direction:** Both the marginal and the empirical reliability increase in the order M1 < M2 < M3 < GRM.
- **Caveat (notebook, `a4ed95b7`):** "Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model."

## (c) Fit evidence and its stated limitations

**F1.7 GRM rater infit/outfit** *(values unchanged; new id; "Ratings by rater")*
- **Finding:** Under the GRM, every rater's infit and outfit is below 1.
  - Infit ranges from 0.334 (R19) to 0.971 (R18).
  - Outfit ranges from 0.322 (R19) to 0.961 (R18).
- **Linked object:** `tbl-grm-rater-fit` (N2, `7770df1a`). Headers: Rater | Ratings by rater | Infit | Outfit | S-X² | df | p | Imputations.
- **Numbers (Infit / Outfit):** R01 0.680/0.650; R02 0.450/0.423; R03 0.699/0.687; R04 0.588/0.554; R05 0.617/0.576; R06 0.604/0.469; R07 0.724/0.645; R08 0.585/0.571; R09 0.871/0.870; R10 0.624/0.603; R11 0.829/0.784; R12 0.507/0.505; R13 0.831/0.834; R14 0.483/0.398; R15 0.754/0.663; R16 0.508/0.480; R17 0.926/0.824; R18 0.971/0.961; R19 0.334/0.322.
- **Caveats (verbatim, `10b621ea`):**
  - "Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982)."
  - "With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked."
  - "No misfit cut-offs for infit and outfit are applied in this notebook."

**F1.8 S-X² (multiple imputation)** *(values unchanged; new id)*
- **Finding:** All S-X² p-values lie between 0.294 (R12) and 0.671 (R02).
- **Linked object:** `tbl-grm-rater-fit` (N2, `7770df1a`).
- **Numbers (S-X² / df / p; Imputations = 20 for every rater):** R01 218.569/213.550/0.392; R02 289.502/300.850/0.671; R03 277.954/280.450/0.531; R04 280.793/290.200/0.643; R05 291.511/293.850/0.528; R06 193.853/190.100/0.411; R07 282.598/285.850/0.543; R08 282.277/285/0.534; R09 440.411/433.550/0.400; R10 247.751/250.600/0.539; R11 298.249/295.100/0.438; R12 207.049/196.800/0.294; R13 263.892/264.200/0.494; R14 224.935/234.450/0.661; R15 265.749/260.900/0.405; R16 200.549/205.150/0.578; R17 279.802/280.350/0.498; R18 342.054/335.700/0.394; R19 223.516/228.400/0.579.
- **Caveat (`10b621ea`):** "S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative."

**F1.9 Local dependence (Q3)** *(values unchanged; new ids; the "computable" definition is now in the notebook)*
- **Finding:** The mean Q3 over 137 computable rater pairs is -0.238, and 20 pairs are flagged.
  - The table shows the ten pairs with the largest |Q3 − mean Q3| among pairs with at least 30 shared products.
  - Nine of the ten deviate negatively and one (R10–R11) positively. All ten are Flagged True.
- **Linked object:** `tbl-grm-q3-flagged` (N2, `ec97f9fb`). The summary line comes from unlabelled N2 `3907a470` (stdout).
- **Numbers:**
  - Stdout, verbatim: "Mean Q3 over 137 computable rater pairs: -0.238; pairs flagged (flag_q3): 20".

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

- **Notebook note (verbatim, `ef6ed18f`, NEW):** "**Local dependence.** Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. It is computed for rater pairs with at least 3 jointly rated products (and residual variance in both raters); other pairs are not computable. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). Flagged marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2."
- **Caption:** "Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products."
- **Caveats:**
  - The table shows only 10 of the 20 flagged pairs.
  - "Overlap" is "–" in every row, and the notebook does not define it.
  - The stdout still uses the code name "flag_q3".
  - The number of non-computable pairs is not printed (see Not found).

**F1.10 Global fit (C2)** *(values unchanged; new id)*
- **Finding:** C2 was not computable, because 17 of 171 rater pairs share no products.
- **Linked object:** `tbl-grm-global-fit` (N2, `6629724c`).
- **Numbers:**
  - C2; Computable False; Rater pairs 171; Rater pairs without shared products 17.
  - Note: "Not computable: 17 of 171 rater pairs share no products, so their bivariate moments and hence C2 are undefined."
- **Notebook explanation (verbatim, `ac69bc26`):** "C2 is a limited-information test of overall model fit (Cai & Monroe, 2014). The table reports either the statistic or the reason it could not be computed: C2 needs the joint distribution of every pair of raters, which is undefined for rater pairs that share no products."
- **Caveat:** No other global fit index is reported.

**F1.11 M1 (MFRM) rater fit** *(values unchanged; new id; "Ratings by rater")*
- **Finding:** Under M1, only R17 (infit 1.328, outfit 1.190) and R18 (1.009, 1.071) are at or above 1. R12 is lowest (infit 0.238, outfit 0.255).
- **Linked object:** `tbl-rater-fit-m1` (N2, `db3fa7b1`). Headers: Rater | Ratings by rater | Infit | Outfit.
- **Numbers (Infit / Outfit):** R01 0.466/0.481; R02 0.786/0.782; R03 0.579/0.579; R04 0.687/0.660; R05 0.701/0.669; R06 0.909/0.705; R07 0.826/0.751; R08 0.540/0.548; R09 0.978/0.958; R10 0.407/0.389; R11 0.938/0.874; R12 0.238/0.255; R13 0.405/0.406; R14 0.747/0.695; R15 0.753/0.698; R16 0.452/0.457; R17 1.328/1.190; R18 1.009/1.071; R19 0.654/0.701.
- **Caption:** "Rater infit and outfit mean squares under M1 (rating scale model / MFRM)."
- **Caveats:**
  - `10b621ea`: "No misfit cut-offs for infit and outfit are applied in this notebook."
  - `a437fa66`: these are "the fit statistics usually reported for many-facet Rasch models (Eckes, 2015)".
  - REPORT.md's 0.7–1.3 is NOT IN NOTEBOOK — not quotable.

## (d) Reliability, including by number of ratings and CIs

**F1.12 Marginal reliabilities with 95% intervals** *(values unchanged; new ids)*
- **Finding:** The empirical marginal reliability of the actual GRM scores is 0.672 [0.649, 0.687]. The model-based marginal reliability, for a hypothetical full panel, is 0.960 [0.953, 0.968].
- **Linked object:** `tbl-grm-reliability-ci` (N2, `af96509f`). The same values appear in `tbl-grm-reliability-summary` (`9b1a9699`) and `tbl-reliability-overview` (`93e117eb`).
- **Numbers:**

  | Quantity | Estimate | 95% CI lower | 95% CI upper | Draws | Draws rejected |
  |---|---|---|---|---|---|
  | empirical marginal reliability | 0.672 | 0.649 | 0.687 | 200 | 87 |
  | model based marginal reliability | 0.960 | 0.953 | 0.968 | 200 | 87 |

  - **Summary table rows:**
    - "empirical_marginal_reliability (primary; actual scores)" 0.672;
    - "model_based_marginal_reliability_mirt (hypothetical full panel)" 0.960;
    - "model_based_marginal_reliability_grid (check)" 0.960;
    - "var theta eap" 0.672;
    - "mean psd squared" 0.328.
  - **Overview notes (verbatim):** "95% CI [0.649, 0.687] (200 parameter draws); Var(theta)/(Var(theta)+mean(PSD^2))" and "95% CI [0.953, 0.968] (200 parameter draws); mirt::marginal_rxx, all raters".
- **Caption:** "Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced."
- **Notebook explanation (verbatim, `09f9927b`):** "95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. Draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; Draws rejected counts these."
- **Caveat (`c4e73d64`):** The empirical value "refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure". The model-based value "refers to the hypothetical full panel".

**F1.13 Distribution of product-level reliability rel_post** *(values unchanged; new ids)*
- **Finding:** rel_post = 1 − PSD² has a median of 0.698 and ranges from 0.057 to 0.929.
- **Linked objects:** `tbl-grm-reliability-summary` (N2, `9b1a9699`) and `fig-grm-rel-post-histogram` (`f54bf904`).
- **Numbers:** rel post min 0.057; rel post p10 0.485; rel post q1 0.596; rel post median 0.698; rel post q3 0.769; rel post p90 0.813; rel post max 0.929; rel post mean 0.672; rel post iqr 0.173.

**F1.14 Reliability by number of ratings per product (observed)** *(values unchanged; new ids; header "Ratings per product")*
- **Finding:** Mean rel_post rises steadily from 0.520 (1 rating) to 0.919 (10 ratings). Mean PSD falls from 0.686 to 0.285.
- **Linked objects:** `tbl-grm-reliability-by-n` (N2, `4c835603`) and `fig-grm-rel-post-by-n` (`9cba007d`).
- **Numbers:**

  | Ratings per product | Products | Mean rel_post | Median rel_post | Mean rel_info | Mean PSD |
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

- **Notebook statement (`a326c3f5`):** "How product-level precision grows with the number of ratings a product received." This describes the table; it is not a test.
- **Caveats:**
  - The 9- and 10-rating rows rest on 3 products each.
  - No CIs are given.
  - No row reaches the full-panel value of 0.960.

**F1.15 Full-panel (hypothetical) information and reliability** *(unchanged; new ids)*
- **Linked object:** `fig-grm-panel-information` (N2, `006409e7`).
- **Numbers:** None printed beyond the model-based 0.960 (F1.12).
- **Caveats:**
  - `5afe758e`: "This is a hypothetical upper bound, not the precision of the actual scores."
  - The caption says the curve "applies to a product rated by all raters."

**F1.16 Consistency of rel_post and rel_info** *(values unchanged; new ids)*
- **Finding:** The two product-level measures correlate at 0.935. The mean of rel_info − rel_post is 0.016, and 320 products differ by more than 0.1.
- **Linked objects:** `tbl-grm-reliability-summary` (`9b1a9699`) and `fig-grm-rel-consistency` (`0b6eedd3`).
- **Numbers:** consistency cor rel post rel info 0.935; consistency mean diff rel info minus rel post 0.016; consistency max abs diff 0.413; products abs diff gt 0.1 320.
- **Notebook statement (`a0ad1048`):** "Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree."

**F1.17 rel_post by θ̂** *(unchanged; new ids)*
- **Linked object:** `fig-grm-rel-post-by-theta` (N2, `c517e631`). This is a figure only; no numbers are printed.
- **Notebook statement (`44ad82c5`):** "Precision depends on where a product lies relative to its raters' thresholds."

**F1.18 Naive indices with bootstrap CIs** *(values unchanged; new ids)*
- **Finding:** The pairwise-covariance Cronbach's α is 0.928, the Cronbach's α of the fully crossed block is 0.658, and Krippendorff's ordinal α is 0.392. For the pairwise Cronbach's α, 361 of 1,000 bootstrap replications failed (639 of 1000 computable).
- **Linked objects:** `tbl-naive-indices` (N2, `dc02d388`) and `tbl-reliability-overview` (`93e117eb`).
- **Numbers:**

  | Index | Value | 95% CI lower | 95% CI upper | Raters | Products | Bootstrap replications | Failed replications |
  |---|---|---|---|---|---|---|---|
  | Cronbach's alpha: pairwise covariances, all usable raters | 0.928 | 0.891 | 0.943 | 14 | 1,900 | 1,000 | 361 |
  | Cronbach's alpha: fully crossed block (listwise complete) | 0.658 | 0.526 | 0.756 | 3 | 139 | 1,000 | 0 |
  | Krippendorff's alpha (ordinal) | 0.392 | 0.362 | 0.417 | 19 | 2,771 | 1,000 | 0 |

  Overview "CI or note" entries, verbatim:
  - "95% bootstrap CI [0.362, 0.417], 1000 replications"
  - "95% CI [0.891, 0.943] (bootstrap, 639 of 1000 replications computable, approximate); 14 raters; removed: R19;R14;R02;R16;R12"
  - "95% CI [0.526, 0.756] (bootstrap, 1000 replications); 3 raters, 139 products"
- **Caption:** "Cronbach's alpha (consistency of the unweighted rater mean) and Krippendorff's alpha (ordinal agreement of single ratings), each with a 95% bootstrap CI over products (1,000 replications). For the pairwise Cronbach's alpha, replications in which a rater pair lost all shared products could not be computed (Failed replications); its CI is approximate."
- **Notebook notes (verbatim, `eeb18be9`):**
  - "Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (Failed replications in the table)."
  - Naive indices "are reference values for common practice. They are not used downstream."
  - Cronbach's α "assumes τ-equivalent raters and complete data".
  - Krippendorff's α "measures the agreement of single ratings, treating raters as interchangeable".

**F1.19 Overview of indices and what each refers to** *(values unchanged; new id)*
- **Linked object:** `tbl-reliability-overview` (N2, `93e117eb`). Headers: Index | Refers to | Value | CI or note.
- **Numbers (repeats of F1.6, F1.12, F1.13 and F1.18):**
  - "GRM: median rel_post" 0.698 ("Q1 0.596, Q3 0.769"); "GRM: IQR rel_post" 0.173.
  - "M1 (RSM): marginal reliability" 0.943; "M2 (PCM): marginal reliability" 0.944; "M3 (GPCM): marginal reliability" 0.955.
  - The "Refers to" entries are: "consensus of single ratings"; "consistency of the unweighted rater mean"; "consistency of the unweighted rater mean (crossed subset)"; "actual theta_hat (primary)"; "hypothetical full panel"; "precision per product" (×2); "comparison" (×3).
- **Notebook statement (`e0182ccc`):** "They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable."

**F1.20 Projected reliability by number of ratings per product (simulation; side note)** *(values unchanged; new ids)*
- **Finding:** With randomly drawn raters, the projected empirical marginal reliability rises at every step in k: 0.508 [0.495, 0.522] at k = 1, 0.688 [0.676, 0.698] at k = 2, and 0.925 [0.922, 0.929] at k = 10.
- **Linked objects:**
  - `tbl-grm-reliability-projection` (N2, `6ed27c6c`) and `fig-grm-reliability-projection` (`21696dce`).
  - Settings: unlabelled stdout `86e9fe64`. Method note: `5a5cda42`.
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

- **Settings (verbatim):** "50 replications of 2000 simulated products per k; seed 20260713."
- **Method note (verbatim, `5a5cda42`):** "**Side note: projected reliability with more ratings.** A simple gauge of the value of adding ratings, supplementary to the observed values above. Products with θ ~ N(0, 1) are simulated; each gets k ratings from k raters of the actual panel, drawn at random, with ratings generated from the fitted GRM and scored with its parameters (treated as known). The table gives the empirical marginal reliability (mean and 95% range over replications) and the mean product-level reliability rel_post."
- **Captions:**
  - Table: "Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²)."
  - Figure: "Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications."
- **Direction (read off the printed values):**
  - The values rise from k = 1 to 10, with shrinking increments: +0.180 from k = 1→2 and +0.007 from k = 9→10. I computed these increments from the printed values; the notebook does not print them.
  - Empirical reliability and Mean rel_post differ by at most 0.002 in any row.
  - No value reaches 0.960. The maximum is 0.925 / 0.926 at k = 10.
- **Caveats:**
  - The 95% range is over 50 replications. It excludes parameter uncertainty, because the parameters are "treated as known".
  - The values are simulated, not observed.
  - Only k = 1–10 is covered.
  - "Side note" and "simple gauge" are the notebook's own framing.

## (e) Rater parameters, information and uncertainty

**F2.1 GRM discrimination a with SE** *(values unchanged; new id; "Ratings by rater")*
- **Finding:** GRM discriminations range from 0.63 (R18) to 3.71 (R19). The SEs are largest for raters with few ratings.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `82eaadcc`). Headers: Rater | Ratings by rater | a | b1 | b2 | b3 | b4 | b5 | b6.
- **Numbers (a (SE)):** R01 1,174 1.96 (0.16); R02 873 2.50 (0.33); R03 720 1.94 (0.20); R04 620 2.04 (0.24); R05 633 2.21 (0.23); R06 520 2.81 (0.42); R07 547 1.99 (0.20); R08 522 2.17 (0.28); R09 400 0.86 (0.15); R10 383 2.24 (0.34); R11 369 1.82 (0.21); R12 264 2.90 (0.57); R13 254 1.50 (0.22); R14 259 2.75 (0.66); R15 73 2.50 (0.52); R16 52 3.70 (1.36); R17 52 1.45 (0.46); R18 55 0.63 (0.26); R19 50 3.71 (2.22).
- **Caption:** "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used."
- **Caveats:**
  - R19 and R16 (50 and 52 ratings) have the two highest a values and the two largest SEs (2.22, 1.36).
  - Notebook (`6791334a`): "a is the rater's discrimination: how sharply the ratings separate products of different creativity."

**F2.2 GRM thresholds b_k with SE (severity)** *(values unchanged; new id)*
- **Finding:** b1 ranges from -6.56 (R18) to 0.29 (R06). R06 is the only rater with a positive b1.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `82eaadcc`).
- **Numbers:**

  | Rater | Ratings by rater | b1 | b2 | b3 | b4 | b5 | b6 |
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

- **Caveats:**
  - Notebook (`6791334a`, verbatim): "b_k is the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater. No rater has an internal category gap, so b_k always separates categories k and k + 1; raters who never used the top categories have no estimate for the highest thresholds."
  - R18 has the largest threshold SEs (b1 SE 3.05).

**F2.3 Rater information summary and shares** *(values unchanged; new id; "Ratings by rater"; caption changed)*
- **Finding:**
  - Information per rating ranges from 0.123 (R18) to 3.539 (R19).
  - Share of panel information ranges from 0.005 (R18) to 0.135 (R19).
- **Linked objects:** `tbl-grm-information-summary` (N2, `54f2a9ef`), `fig-grm-rater-information` (`0974fb2e`) and `fig-grm-information-shares` (`c6c942e1`).
- **Headers:** Rater | Ratings by rater | Information per rating | θ at maximum | Maximum information | Share of panel information | Share at θ = −2 | Share at θ = −1 | Share at θ = 0 | Share at θ = 1 | Share at θ = 2.
- **Numbers (Information per rating / θ at maximum / Maximum information / Share / shares at θ = −2, −1, 0, 1, 2):**
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
- **Caption (current, verbatim):** "Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ)."
- **Notebook statements:**
  - `d3ec4aff`: "Information from different raters adds up under local independence."
  - `bd9d7da1`: "For each rater: information averaged over the N(0, 1) distribution of θ, where it peaks, and the rater's share of the full-panel information."

**F2.4 Intervals for rater information and share** *(values unchanged; new id; "Ratings by rater"; caption changed)*
- **Finding:** The intervals are widest for raters with few ratings:
  - R19: information 3.54 [0.41, 11.02], share 0.135 [0.017, 0.331];
  - R16: information 3.30 [0.73, 6.49], share 0.126 [0.026, 0.223].
- **Linked object:** `tbl-grm-rater-information-ci` (N2, `c43a5551`).
- **Numbers:**

  | Rater | Ratings by rater | Information per rating [95% interval] | Share of panel information [95% interval] |
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

- **Caption (current, verbatim):** "Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws."
- **Caveats:**
  - Notebook (`20da2179`): "95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings."
  - These are the same draws as in F1.12 (200 accepted, 87 rejected).
  - Information prints with 2 decimals here and 3 in F2.3 (for example R02 1.705 vs 1.70, R13 0.655 vs 0.65).
  - The lower bound of R18's share prints 0.000.

**F2.5 Category response functions** *(unchanged; new id)*
- **Linked object:** `fig-grm-category-response-functions` (N2, `81cf428c`). This is a figure only.

## (f) Model dependence of scores and rankings

**F2.6 Correlations of EAP scores between models** *(values unchanged; new id; new model labels)*
- **Finding:** All correlations between models are 0.975 or higher. GRM–M3 is 0.996 on both coefficients. GRM–M1 is lowest (Pearson 0.975, Spearman 0.978).
- **Linked object:** `tbl-theta-correlations` (N2, `9f614151`). Headers: Method | Model | M1 (rating-scale MFRM) | M2 (partial-credit MFRM) | M3 (GPCM) | GRM | M1, sirt default grid.
- **Numbers:**
  - Pearson: M1–M2 0.993; M1–M3 0.980; M1–GRM 0.975; M2–M3 0.989; M2–GRM 0.985; M3–GRM 0.996.
  - Spearman: M1–M2 0.996; M1–M3 0.983; M1–GRM 0.978; M2–M3 0.987; M2–GRM 0.983; M3–GRM 0.996.
  - "M1, sirt default grid" vs M1: 1.000 on both coefficients.
- **Caption:** "Correlations of the EAP estimates between models (Pearson and Spearman). 'M1, sirt default grid' is M1 re-estimated with the default quadrature grid of sirt, as a software check."
- **Notebook framing (`07dac156`):** "High values mean the ranking of products hardly depends on the model."

**F2.7 Ranking change relative to the GRM** *(values unchanged; new id; new model labels)*
- **Finding:** Relative to the GRM, the share of products changing quintile is 0.202 under M1, 0.150 under M2 and 0.075 under M3.
- **Linked object:** `tbl-score-agreement` (N2, `9c290637`).
- **Numbers:**

  | Model | Pearson r | Spearman ρ | Mean percentile shift | 95th percentile of shift | Maximum shift | Share changing quintile | Share changing ≥ 2 quintiles |
  |---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | 0.975 | 0.978 | 0.042 | 0.130 | 0.432 | 0.202 | 0.004 |
  | M2 (partial-credit MFRM) | 0.985 | 0.983 | 0.033 | 0.117 | 0.413 | 0.150 | 0.003 |
  | M3 (GPCM) | 0.996 | 0.996 | 0.017 | 0.044 | 0.234 | 0.075 | 0.001 |

- **Caption:** "Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes."
- **Notebook statement (`f20aeb5b`):** "How far products move in the ranking when another model replaces the GRM: the mean and 95th-percentile shift in percentile rank, and the share of products that change quintile."

## (g) Sensitivity analyses

**F2.8 Sensitivity to the rater exclusion** *(values unchanged; new id)*
- **Finding:** Refitting the GRM with all 22 raters gives these results:
  - the empirical reliability changes from 0.67199 to 0.67186;
  - the model-based reliability changes from 0.95986 to 0.96186;
  - θ̂ from the two fits correlates at 0.99997 (Pearson).
- **Linked object:** `tbl-sensitivity-rater-exclusion` (N2, `e46ff49c`), printed with 5 decimals. Headers: Quantity | Final data | All raters | Note.
- **Numbers (Final data vs All raters):**
  - n raters 19 vs 22; n ratings 7,820 vs 7,844; n products 3,668 vs 3,669; excluded raters "–" vs R20;R21;R22.
  - empirical marginal reliability 0.67199 vs 0.67186 (Note: "Var(theta)/(Var(theta)+mean(PSD^2))").
  - model based marginal reliability 0.95986 vs 0.96186 (Note: "mirt::marginal_rxx (hypothetical full panel)").
  - Rows with the Note "all-raters vs final GRM, 3668 common products":
    - theta pearson common products 0.99997;
    - theta spearman common products 0.99996;
    - theta mean abs diff 0.00171;
    - theta max abs diff 0.16246;
    - share products changing quintile 0.00491.
  - Rows with the Note "all-raters vs final GRM, 19 common raters": a max abs diff common raters 0.19820; a pearson common raters 0.99880.
- **Caveat:** No CIs are given for the differences.

## (h) Raw mean vs model-based scores

**F2.9 Raw mean rating vs GRM score** *(values unchanged; new id; header "Ratings per product")*
- **Finding:** Within the groups of products with 1, 2 and 3+ ratings:
  - Kendall's τ-b between the raw mean and the GRM score is 0.815–0.842.
  - 0.042–0.070 of the pairs with different raw means are ordered the other way round by the GRM.
  - Among products with equal raw means, the mean θ̂ range is 0.619–1.537 and the maximum is 2.196.
- **Linked object:** `tbl-raw-mean-vs-grm` (N2, `eb1111f4`).
- **Numbers:**

  | Ratings per product | Products | Kendall's τ-b | Share of pairs in reversed order | Mean θ̂ range at equal raw mean | Maximum θ̂ range at equal raw mean |
  |---|---|---|---|---|---|
  | 1 | 897 | 0.832 | 0.042 | 1.283 | 1.436 |
  | 2 | 2,080 | 0.815 | 0.067 | 1.537 | 2.196 |
  | 3+ | 691 | 0.842 | 0.070 | 0.619 | 1.396 |

- **Caption:** "Raw mean rating versus GRM score by number of ratings per product: Kendall's tau-b, share of product pairs in reversed order, and range of GRM scores among products with the same raw mean."
- **Notebook explanation (verbatim, `6ae6b373`):** "**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, separately for products with 1, 2 and 3 or more ratings. The raw mean is tied for almost all products (with one rating it takes only 7 values), so agreement is given as Kendall's τ-b and as the share of product pairs with different raw means that the GRM orders the other way round. The last two columns show how far apart the GRM scores of products with the same raw mean lie: products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination."
- **Direction:**
  - τ-b: 3+ (0.842) > 1 (0.832) > 2 (0.815).
  - Reversed share: 1 (0.042) < 2 (0.067) < 3+ (0.070).
  - Mean θ̂ range: 2 (1.537) > 1 (1.283) > 3+ (0.619).
  - Maximum θ̂ range: 2 (2.196) > 1 (1.436) > 3+ (1.396).
  - The Products column sums to 3668. I computed this sum; the table has no pooled row.
- **Caveats:**
  - The share of tied products, the size of the equal-raw-mean groups and the number of pairs are not printed.
  - No CIs are given.
  - The mechanism clause is not a tested result. Mark it for author confirmation if used.

**F2.10 Figure: GRM score against raw mean** *(unchanged; new ids)*
- **Linked object:** `fig-raw-mean-vs-theta` (N2, `813b9af4`). This is a figure only.
- **Caption:** "GRM score (EAP) against the raw mean rating of each product, by number of ratings per product. Points are jittered horizontally."
- **Notebook statement (`1213e88c`):** "The same comparison as a figure. Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal."

---

## Not found

These are absent from the notebooks. Do not invent them downstream.
- **CIs:**
  - for rel_post by number of ratings (F1.14);
  - for the sensitivity differences (F2.8);
  - for the raw-mean vs GRM measures (F2.9);
  - CIs or SEs for the M1/M2 parameters and for the M1–M3 marginal and empirical reliabilities.
- **Global fit:** any index other than the non-computable C2 (no RMSEA, SRMSR or M2).
- **Q3:**
  - the number of rater pairs that are not computable. The notebook prints only "137 computable" and "171" total pairs, and does not split the remainder into pairs with no overlap, 1–2 shared products, or zero residual variance;
  - what "Overlap" in `tbl-grm-q3-flagged` means;
  - the full list of the 20 flagged pairs.
- **LR df:** the count of unused end categories as a single printed figure. AUDIT.md's "6" is NOT IN NOTEBOOK — not quotable.
- **Figures:** numeric values behind the figures (full-panel information curve, rel_post by θ̂, category response functions, raw-mean-vs-θ̂ scatter).
- **Rater and product summaries:**
  - the latent θ̂ distribution (mean, SD);
  - a single severity summary per rater;
  - per-rater uncertainty for the descriptive response-style indices (F0.8).
- **Precision:** GRM parameters and rater-information CI bounds at 3 decimals.
- **Fit cut-offs:** infit/outfit misfit thresholds (none are applied; REPORT.md's 0.7–1.3 is NOT IN NOTEBOOK).
- **Tests:**
  - trend tests across n, or across the raw-mean groups;
  - any ICC;
  - an M0 vs M1 severity test;
  - a within-package M1 vs M2 LR test;
  - a held-out predictive check;
  - diagnostics of the rejected parameter draws.
- **F2.9 (raw mean vs GRM):**
  - a pooled row;
  - correlations, percentile shifts and quintile measures;
  - the tied share and group sizes.
- **F1.20 (projection):**
  - selected rater sets (most/least informative);
  - `true_r2`;
  - quantiles of Mean rel_post;
  - k > 10;
  - parameter uncertainty;
  - the number of ratings needed for a target reliability (do not derive one).
- **Study context:** the timespan of data collection, rater demographics and rater expertise.

**Possible extensions (context file only, NOT IN NOTEBOOK, not a result).** None of the three notebooks mentions extensions. ANALYSIS_TODO.md ("Possible extensions (deliberately NOT in the paper, decision 2026-10-27)") lists:
- projection with selected or workload-weighted rater sets;
- ratings needed for a target reliability (.70/.80/.90);
- an M0 vs M1 severity test;
- a within-package M1 vs M2 LR test;
- a held-out predictive check;
- rejected-draw diagnostics.

Any future-work wording is the author's to confirm.

**Resolved since the previous version:**
- The Q3 "computable" definition is now in the notebook (`ef6ed18f`). Former Flag 5 and the related Not-found item are removed.
- F0.8 now has an embeddable labelled table.
- The ambiguous "Ratings (n)" header is replaced by "Ratings by rater", "Ratings per product" and "Ratings (total)".

## Flags

1. **Pre-exclusion residue (unchanged).**
   - N0 is pre-exclusion. `tbl-cleaning-log` stops at 7844.
   - N1 is fully post-exclusion.
   - In N2, pre-exclusion values appear only where labelled as such: the "All raters" column of `tbl-sensitivity-rater-exclusion`, `tbl-excluded-raters`, and the exclusion/duplicate rows of `tbl-design-summary`.
2. **`02_artifacts.md` is stale.**
   - It lists the previous N2 cell ids. For example, `tbl-design-summary` 475838c2 is now `28af567a`, and `tbl-grm-reliability-projection` 5fa6455c is now `6ed27c6c`.
   - It reports 42 labels and lacks `tbl-overview-rater-response-styles` (N1 `ovtbl02`). The current total is 43.
   - It still names the old "Ratings (n)" header and the old model labels.
   - Re-run the results-embedder if it has not already been re-run in parallel.
3. **Privacy (unchanged).**
   - N0 `520638b8` contains the full Google Sheets URL ("anyone with the link").
   - N0/N1 stdout prints absolute local paths and action UUIDs.
   - No original rater IDs are printed.
4. **LR df vs AUDIT.** The mechanism is explained (`2bf87a03`), but the count is not printed. Do not quote "6".
5. **R09 mean prints in two forms.**
   - `tbl-overview-rater-response-styles`: 3.643.
   - Unlabelled `fb6df84b`: 3.642.
   - Same stored value, different display rounding. Quote 3.643 with the embedded table.
6. **Parameter draws.** These are explained in `09f9927b`. `tbl-grm-rater-information-ci` has no Draws column; its caption says "200 accepted parameter draws".
7. **Display inconsistencies (to quote as printed):**
   - **Separators:** N2 numeric cells have them (7,820). N0, N1, N2 text notes and N2 stdout do not (7820, 1000, 3668, 2000).
   - **Model labels** differ by place:
     - cells print "M1 (rating-scale MFRM)" and "M2 (partial-credit MFRM)";
     - the `tbl-reliability-overview` rows print "M1 (RSM)" and "M2 (PCM)";
     - the `tbl-threshold-order` caption prints "M2 (PCM) and M3 (GPCM)";
     - the `tbl-model-fit` and `tbl-rater-fit-m1` captions print "rating scale model / MFRM".
   - **Integer display:** in `tbl-theta-correlations` the diagonal prints "1" next to "1.000". In `tbl-overview-rater-response-styles`, R08's Mean is "3" and five Share highest (7) cells are "0".
   - **Code-name labels** remain: "min_ratings_per_rater (exclusion cut-off)", "empirical_marginal_reliability (primary; actual scores)", "model_based_marginal_reliability_mirt (hypothetical full panel)", "marginal_rxx (mirt)".
   - **Q3:** the stdout still says "flag_q3", and "Overlap" is "–" in every row.
   - **Precision is mixed:**
     - 2 decimals: GRM parameters and information CIs;
     - 3 decimals: most tables;
     - 5 decimals: the sensitivity table;
     - 6 decimals: N1 `31873726` shares.
8. **Markdown order mismatches in N2 persist.**
   - `5afe758e` ("Full panel") is separated from `fig-grm-panel-information` (`006409e7`) by the information-CI block (`20da2179`, `c43a5551`).
   - `a326c3f5` ("Reliability by number of ratings") precedes `09f9927b` / `tbl-grm-reliability-ci` rather than `tbl-grm-reliability-by-n` (`4c835603`).
   - `8307cc03` (M3 discriminations) is separated from `tbl-discrimination-m3` (`293a100e`) by tbl-score-agreement, tbl-raw-mean-vs-grm, fig-raw-mean-vs-theta and tbl-sensitivity-rater-exclusion.
9. **Unlabelled but cited sources.** These are quotable but cannot be embedded:
   - N1 `3b12b8bf` and `aa371443` (F0.4, F0.5);
   - N2 `3907a470` (mean Q3);
   - N2 `86e9fe64` (projection settings).

   F0.8 is now embeddable through `ovtbl02`.
10. **Terminology.**
    - N1 and N2 say "products". The label `tbl-overview-ratings-per-action` still says "action".
    - N0 uses "actions".
    - The N2 intro (`bc5ee2d0`) says "The rated products are the football actions".
11. **Stale reference.** The N0 intro markdown (`64b27fc9`, `73ef4dcd`) still refers to deleted notebooks (`02a`–`02d`, `03`, `02_creativity_ratings_R.qmd`).
12. **Coinciding printed values.** "empirical_marginal_reliability (primary; actual scores)", "var theta eap" and "rel post mean" all print 0.672. This is reported as observed.
13. **Removed or no-longer-printed content.** The full list is in Changes item 8. Drafts may still contain:
    - "Ratings (n)", "M1 (RSM/MFRM)" or "M2 (PCM)" as table labels;
    - the caption sentence "Ratings (n) is the number of ratings the rater gave.";
    - Tolerance "0.0001";
    - "0.000545256".

    Replace them with the current printed forms.
14. **Mechanism sentences in N2 markdown.** These are the notebook's framing, not results. Mark them for author confirmation if used:
    - `6ae6b373` ("products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination");
    - `8307cc03` ("Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data");
    - `07dac156` ("High values mean the ranking of products hardly depends on the model");
    - `5a5cda42` ("A simple gauge of the value of adding ratings");
    - N1 `f3482d97` ("anticipate what the models estimate formally").
15. **Projection vs observed reliability (F1.20 vs F1.14).**
    - The projection simulates θ ~ N(0, 1) with random raters ("each equally likely") and known parameters. The observed table uses the actual products and raters.
    - The notebook makes no numeric comparison between them. Any side-by-side statement (for example projected k = 2 Mean rel_post 0.690 vs observed 0.698) would be the writer's own juxtaposition.

---

Files read:
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb` (all Markdown outputs, markdown cells and cell ids checked in the raw JSON)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb` (including the raw Markdown output of `ovtbl02`)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/03_findings.md` (previous version)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/02_artifacts.md` (staleness check only)