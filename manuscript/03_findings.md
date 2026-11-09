# 03_findings.md: Results findings (results-interpreter, Phase 4 revision run 2026-11-09, frozen data 9,046 ratings)

## Changes vs previous findings

1. **Every value in the previous findings file is stale.** The pipeline was re-run on the frozen data set (N2 `tbl-design-summary`: 9,046 ratings / 3,669 products / 24 raters; N0: 10447 raw rows, 9077 after cleaning, 28 raters). No value below is carried over from the previous file; every number was re-read from the stored notebook outputs.
2. **Nine new labelled cells in N2**, each with its own finding: `fig-design-ratings-per-product` (F0.4), `fig-category-usage-shares` (F0.8), `fig-grm-rater-discrimination-ci` (F2.3), `fig-grm-rater-information-ci` (F2.6), `tbl-grm-reliability-min-ratings` (F1.21), `tbl-grm-reliability-observed-vs-simulated` (F1.22), `fig-grm-reliability-observed-vs-simulated` (F1.23), `fig-m1-rater-severity` (F2.8), `tbl-rater-overview` (F2.9). Total labels: 52 (N0 1, N1 6, N2 45).
3. **Structural changes in existing cells.**
   - `tbl-grm-q3-flagged` no longer has the "Overlap" column (now: Rater 1 | Rater 2 | Shared products | Q3 | Q3 minus mean Q3 | Flagged).
   - `tbl-reliability-overview` has a new row "GRM: empirical marginal reliability, at least 4 ratings per product (simulated)" inserted after the empirical-reliability row (added by `_with_min4_row`, display only).
   - `tbl-reliability-overview` row labels now read "M1 (rating-scale MFRM): marginal reliability" and "M2 (partial-credit MFRM): marginal reliability" (the old "M1 (RSM)"/"M2 (PCM)" forms are gone).
   - `tbl-lr-tests` p values print as "< .001" (no more scientific notation).
   - `tbl-model-fit` Δ cells print with three decimals ("0.000"); `tbl-theta-correlations` diagonal prints "1.000"; `tbl-marginal-reliability-models` Latent variance prints "1.000".
   - `tbl-sensitivity-rater-exclusion` Note cells now contain a thousands separator ("3,669 common products") and "mirt::marginal rxx" (underscore turned into a space by `readable_text`).
   - N1 `tbl-overview-rater-response-styles` now prints decimals in every column that holds a non-integer value: R08 and R26 Mean "3.000" (not "3"), Share highest (7) "0.000" (not "0"). Median, IQR and Categories used still print as integers.
   - N1 `tbl-overview-ratings-per-action`: median_ratings_per_rater prints "318.500".
   - The caption of `tbl-model-fit` now says "M1 rating-scale MFRM, M2 partial-credit MFRM"; `tbl-threshold-order` caption "M2 (partial-credit MFRM) and M3 (GPCM)"; `tbl-rater-fit-m1` caption "M1 (rating-scale MFRM)".
   - The projection note (`77937868`) no longer says "Side note" / "simple gauge"; it now says "A model-based gauge of the value of adding ratings, complementing the observed values above."
4. **Substantive differences visible in the new outputs (reported, not interpreted):** BIC now favours M1 (ΔBIC M1 0.000, GRM 4.161) while AIC and SABIC favour the GRM; previously the GRM was best on all three. The number of unused-category raters is 8 (previously 5) and one rater (R27) has an internal gap (previously 0). The projection and min-4 simulation and the observed-vs-simulated comparison are new.
5. **All N2 cell ids changed again.** Ids below are the current ones (they match `02_artifacts.md`). N0 and N1 ids are unchanged.

## Rater IDs and final counts

- **Retained raters (24):** R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R23, R24, R25, R26, R27 (every rater table in N1 and N2 lists exactly these 24). This matches the expectation R01–R19 and R23–R27. **No deviation.**
- **Excluded raters (4):** R20 (13 ratings), R21 (9), R22 (2), R28 (7) — `tbl-excluded-raters`; together 31 ratings (`tbl-design-summary` "ratings excluded 31"). Matches the expectation.
- **IDs are permanent and do not follow workload order.** N0 `fdbdb3b4` code comment: "IDs are permanent: raters already in the key keep their pseudonym, and new raters get the next free numbers (most raw rows first). The numbers therefore do not reflect workload order, and results stay comparable across data updates." N0 stdout: "Raters in the key: 28; new in this download: 0".
- **Final counts, consistent across notebooks:**
  - N1 `f6039400` stdout: "Loaded 9077 ratings; excluded 31 ratings from 4 raters with fewer than 15 ratings (R20, R21, R22, R28); 9046 ratings remain."
  - N1 `981d6824`: Total ratings 9046; Distinct products 3669; Distinct raters 24; "Average ratings per product: 2.47"; "Average ratings per rater: 376.9".
  - N2 `tbl-design-summary` (c37b4a38): n ratings 9,046; n products 3,669; n raters 24.
  - N2 `tbl-grm-convergence` (d2a66a75): Products 3,669; Ratings (total) 9,046.
  - N0 is pre-exclusion: 9077 rows, 28 raters, 3670 actions.
- **Data fingerprint:** the md5 68037eafc9939992751c2bf646c48a9e is **not printed in any notebook** (the `tbl-design-summary` code explicitly drops the `data_fingerprint` row: `d[d["quantity"] != "data_fingerprint"]`). NOT IN NOTEBOOK — not quotable from the notebooks.

---

Notebooks (the only quotable sources):
- **N0** = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- **N1** = `.../notebooks/01_data_overview.ipynb`
- **N2** = `.../notebooks/02_jrt_results.ipynb` (main; 45 labels)

How to read this file:
- **Values** are copied exactly as printed (decimals, separators, dashes).
- **N2 formatting** (`tidy()`/`fmt_cell` in the build script): numbers with thousands separators; columns with any non-integer value print every value with 3 decimals; whole-number columns print without decimals; p values "< .001" or 3 decimals; missing as "–". `est_se()` gives "estimate (SE)" with 2 decimals (`tbl-grm-rater-parameters`). `est_ci()` gives "estimate [low, high]": 2 decimals for information, 3 for shares and the projection/min-4 tables. `tbl-sensitivity-rater-exclusion` prints 5 decimals. `tbl-rater-overview` is hand-formatted: 2 decimals, "Ratings" without separator, share as "x.x% [low, high]" with the % sign only on the estimate.
- **N1 formatting** (`show_table`/`fmt_cell`): no thousands separators; columns with any non-integer print 3 decimals; `fb6df84b` uses `round(3)` (floats like "520.0").
- **N0 formatting:** `tbl-cleaning-log` is `to_markdown` of a raw frame (no separators, snake_case).
- Direction statements marked "read off the printed values" are my comparisons of printed numbers; the notebook does not print them.

---

## (a) Data, cleaning and design

**F0.1 Raw data and cleaning (pre-exclusion, N0)**
- **Finding:** The sheet export had 10447 rows; cleaning removed 1347 not-recognised rows, 1 out-of-range value and 22 duplicate rows, leaving 9077 rows from 28 raters and 3670 actions.
- **Linked object:** `tbl-cleaning-log` (N0, `bbcbf730`). Supporting stdout in `520638b8`, `fdbdb3b4`, `fb9eaf36`, `36dd5cb3`, `793192b4`, `72468670`, `dd37b3ec`.
- **Numbers (table as printed):**

  | step | n_rows_before | n_rows_after | n_rows_affected | description |
  |---|---|---|---|---|
  | drop_action_not_recognized | 10447 | 9100 | 1347 | Rows where the rater flagged the action as not recognized were excluded |
  | drop_missing_id | 9100 | 9100 | 0 | Rows with missing action_id/rater_id removed |
  | drop_out_of_range | 9100 | 9099 | 1 | Rating values outside {1,...,7} or non-integer removed |
  | drop_missing_rating | 9099 | 9099 | 0 | Rows with missing or non-convertible rating removed |
  | resolve_duplicates | 9099 | 9077 | 22 | Duplicates resolved: latest entry per (action_id, rater_id) kept |

  - Stdout: "Downloaded 10447 rows."; "Rows flagged as action_not_recognized: 1347"; "Missing action_id: 0"; "Missing rater_id:  0"; "Non-convertible, non-missing raw rating values: 0"; "Values outside {1,...,7} or non-integer: 1" (the row: rater R04, rating 0.0); "Missing/non-convertible rating values: 0".
  - Duplicates: "Rows with a duplicate (action_id, rater_id) combination: 43". The printed list shows 21 distinct (action_id, rater_id) pairs: 20 pairs with two rows and one with three rows (R22, three rows all rated 4.0). One pair conflicts: R14 on action 36a6bfe9-… rated 1.0 and 2.0; all other duplicates carry identical ratings. (The counts 21 and 1 are my reading of the printed list; N2 `tbl-design-summary` prints "duplicate pairs resolved in 00 21" and "duplicate pairs conflicting 1".)
  - **Rule (N0 markdown `6ad60c29`, verbatim):** "*the entry with the latest timestamp is kept* (a later entry typically reflects a correction). Sheet order is not used, because the export is not in chronological order. This assumption should be revisited if the actual cause of duplicates in the sheet becomes known."
  - "Cleaning complete: 9100 -> 9077 rows."; "Raters: 28"; "Actions: 3670"; "Warnings collected: 3".
  - Event details: "Event details saved: … (4104 actions)" (optional StatsBomb lookup, not merged).
- **Caveats:** Pre-exclusion. The cleaning log has no rater-exclusion row. Headers are snake_case code names.

**F0.2 Rater exclusion**
- **Finding:** Four raters with fewer than 15 ratings were excluded; together they gave 31 ratings and their exclusion dropped 1 product.
- **Linked objects:** `tbl-excluded-raters` (N2, `43fb15c3`; headers Rater | Ratings by rater | Reason); `tbl-design-summary` (N2, `c37b4a38`).
- **Numbers:** R20 13; R21 9; R22 2; R28 7; Reason "fewer than 15 ratings" in each row. Design summary: min ratings per rater (exclusion cut-off) 15; raters excluded R20;R21;R22;R28; ratings excluded 31; products dropped 1.
- **Notebook statement (N2 intro `92527bc1`):** "Raters with fewer than 15 ratings are excluded from the whole pipeline (decision 2026-10-22; see `results/data/excluded_raters.csv`)."

**F0.3 Final design**
- **Finding:** The final design has 9,046 ratings of 3,669 products by 24 raters; 10.3% of the product × rater matrix is filled, the design is one connected component, and 30 of 276 rater pairs share no product.
- **Linked objects:** `tbl-design-summary` (N2, `c37b4a38`; headers Quantity | Value); `tbl-overview-ratings-per-action` (N1, `ovtbl01`; headers quantity | value); N1 stdout `981d6824`, `bacf60d8`.
- **Numbers (N2, every row as printed):** n ratings 9,046; n products 3,669; n raters 24; min ratings per rater (exclusion cut-off) 15; raters excluded R20;R21;R22;R28; ratings excluded 31; products dropped 1; n categories 7; scale 1-7; internal coding rating - 1 (0-6); ratings per product mean 2.466; ratings per product median 2; ratings per product min 1; ratings per product max 13; ratings per product harmonic mean 1.806; products with 1 rating 832; ratings per rater min 46; ratings per rater max 1,174; matrix fill 0.103; n components 1; rater pairs total 276; rater pairs without overlap 30; rater pairs overlap median 19; raters with category gaps 8; raters with internal gap 1; duplicate pairs resolved in 00 21; duplicate pairs conflicting 1.
- **Numbers (N1 `ovtbl01`, every row):** n_ratings 9046; n_products 3669; n_raters 24; n_products_1_rating 832; n_products_2_ratings 2107; n_products_3plus_ratings 730; share_products_1_rating 0.227; share_products_2_ratings 0.574; share_products_3plus_ratings 0.199; max_ratings_per_product 13; mean_ratings_per_product 2.466; harmonic_mean_ratings_per_product 1.806; median_ratings_per_rater 318.500; min_ratings_per_rater 46; max_ratings_per_rater 1174.
- **N1 stdout:** `981d6824` "Average ratings per product: 2.47", "Average ratings per rater: 376.9"; `bacf60d8` "Number of connected components: 1", component 0 with n_products 3669, n_raters 24; `9f03e286` "Raters with <= 2 rated products: 0".
- **Notebook statement (N2 `fd5772fd`, verbatim):** "**Design.** Size and coverage of the products × raters matrix that every model uses. The design is incomplete: each product is rated by a few raters only, and missing ratings are left out of the likelihood, not imputed. A connected design (one component) is required so that all raters and products lie on one scale (Eckes, 2015)."
- **Caveats:** 832 products (0.227) have a single rating. 30 of 276 pairs have no shared product. "matrix fill" 0.103 is printed as a proportion.

**F0.4 Distribution of ratings per product** *(includes NEW `fig-design-ratings-per-product`)*
- **Finding:** Most products have 2 ratings (2107); the counts fall to 68 at 3 ratings, rise again to 198 at 5 ratings, and then decline to 1 product with 13 ratings.
- **Linked objects:** **`fig-design-ratings-per-product` (N2, `e14aa571`, NEW)**; `fig-overview-degree-distributions` (N1, `ovfig04`, panel A). The numbers come from N1 `3b12b8bf` stdout; the N2 figure annotates each bar with its count (same source CSV `design_summary_ratings_per_product.csv`), but the in-image numbers are not quotable as text — quote the N1 stdout.
- **What the new figure shows (caption verbatim):** "Number of products by number of ratings received." Bar chart, x = ratings per product (ticks at every observed value), y = Products, each bar labelled with its count. Note `2854cd3e`: "**Ratings per product.** Number of products by the number of ratings they received."
- **Numbers (N1 `3b12b8bf`):**

  | ratings per product | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | products | 832 | 2107 | 68 | 153 | 198 | 137 | 95 | 36 | 22 | 14 | 4 | 2 | 1 |

  Cumulative ("x or more ratings"): 1 → 3669; 2 → 2837; 3 → 730; 4 → 662; 5 → 509; 6 → 311; 7 → 174; 8 → 79; 9 → 43; 10 → 21; 11 → 7; 12 → 3; 13 → 1.
- **Caveats in data:** The distribution is not monotone (68 products with 3 ratings vs 153 with 4 and 198 with 5). Counts at 11–13 ratings are 4, 2 and 1.

**F0.5 Ratings per rater and pairwise overlap**
- **Finding:** Raters gave between 46 (R26) and 1174 (R01) ratings; the best-partner overlap ranges from 19 (R26) to 371 (R07, R23).
- **Linked object:** `fig-overview-rater-overlap` (N1, `ovfig01`). Numbers from N1 `3b12b8bf` and `aa371443` stdout.
- **Ratings per rater (ascending, as printed):** R26 46, R27 47, R19 50, R17 52, R18 55, R15 73, R25 138, R24 190, R13 254, R14 259, R12 264, R16 268, R11 369, R10 383, R09 400, R06 520, R08 522, R07 547, R23 589, R04 620, R05 633, R03 720, R02 873, R01 1174.
- **Best-connected-partner overlap (ascending, as printed):** R26 19, R27 42, R17 44, R19 46, R18 50, R15 64, R14 108, R25 125, R12 145, R09 147, R13 154, R10 157, R24 167, R05 190, R08 191, R16 227, R06 240, R02 257, R04 257, R01 329, R03 329, R11 357, R07 371, R23 371.
- **Caveats:** Six raters (R26, R27, R19, R17, R18, R15) have 73 or fewer ratings.

**F0.6 Category frequencies across all ratings**
- **Finding:** Category 2 is the most frequent (2355) and category 7 the rarest (128).
- **Linked object:** `fig-overview-rating-distribution` (N1, `ovfig02`). Numbers from N1 `31873726` stdout.
- **Numbers:** category 1: n 2179, share 0.240880; 2: 2355, 0.260336; 3: 1777, 0.196440; 4: 1282, 0.141720; 5: 909, 0.100486; 6: 416, 0.045987; 7: 128, 0.014150.

**F0.7 Category use per rater**
- **Finding:** Eight raters left at least one category unused; in seven of them only top categories are unused, and R27 additionally never used category 5 (internal gap True).
- **Linked object:** `tbl-category-usage` (N2, `49d9be87`).
- **Numbers (headers verbatim):**

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
  | R16 | 29 | 65 | 81 | 55 | 26 | 9 | 3 | 268 | – | False |
  | R17 | 25 | 10 | 9 | 4 | 4 | 0 | 0 | 52 | 6;7 | False |
  | R18 | 1 | 8 | 14 | 12 | 16 | 4 | 0 | 55 | 7 | False |
  | R19 | 10 | 6 | 8 | 6 | 10 | 6 | 4 | 50 | – | False |
  | R23 | 65 | 99 | 151 | 117 | 100 | 40 | 17 | 589 | – | False |
  | R24 | 16 | 37 | 30 | 34 | 44 | 27 | 2 | 190 | – | False |
  | R25 | 18 | 30 | 39 | 34 | 15 | 2 | 0 | 138 | 7 | False |
  | R26 | 5 | 13 | 12 | 10 | 5 | 1 | 0 | 46 | 7 | False |
  | R27 | 21 | 12 | 6 | 7 | 0 | 1 | 0 | 47 | 5;7 | True |

- **Number of thresholds per rater:** not printed as a column. `tbl-grm-rater-parameters` shows the consequence: b6 is "–" for R01, R03, R06, R18, R25, R26; b5 and b6 are "–" for R17 and R27 (see F2.2). `tbl-threshold-order` prints Steps 4 for R17 and R27, 5 for R03, R06, R18.
- **Notebook statements:** `18b6b4b1` "Raters who never use a category get fewer thresholds in mirt, because mirt only models the categories a rater actually used." Caption: "Unused categories at the ends of the scale reduce the number of thresholds of a rater; an unused category inside the observed range (internal gap) makes that rater's thresholds incomparable with those of other raters."
- **Caveats:** Missing categories are semicolon-joined ("6;7"). Design summary: raters with category gaps 8; raters with internal gap 1.

**F0.8 Category use as shares (NEW figure)**
- **Linked object:** **`fig-category-usage-shares` (N2, `c39bf61e`, NEW)**. Figure only; no values are printed as text.
- **Caption (verbatim):** "Share of each rater's ratings in each of the 7 categories, sorted by the rater's mean rating; n = number of ratings; ✕ = category never used."
- **Note (`b33ccad2`, verbatim):** "The same category use as shares of each rater's ratings. Raters sorted by mean rating; ✕ marks categories a rater never used."
- **What is plotted (from code):** one horizontal stacked bar per rater (24), segments = share of the rater's ratings in categories 1–7 (viridis_r colours), raters sorted by mean rating (descending in the data frame, so the highest mean is at the bottom row), right-margin text "n=<ratings>" plus "✕ <unused categories>" where applicable; x axis 0–100%; legend "Category" below the axes. Source CSVs: `category_usage.csv` and `design_summary_raters.csv`.
- **Quotable numbers:** the underlying counts are those of F0.7; the shares themselves are not printed anywhere (values read off the plot are not quotable).

**F0.9 Rater response styles (descriptive)**
- **Finding:** Rater means range from 1.760 (R06) to 3.836 (R18); SDs from 1.022 (R01) to 1.953 (R19).
- **Linked objects:** `tbl-overview-rater-response-styles` (N1, `ovtbl02`); `fig-overview-rater-response-styles` (N1, `ovfig03`). Source frame N1 `fb6df84b` (`round(3)`, includes n_products = n_ratings for every rater).
- **Numbers (exactly as printed in `ovtbl02`):**

  | Rater | Ratings by rater | Mean | Median | SD | IQR | Categories used | Entropy | Share lowest (1) | Share highest (7) | Share extreme (1, 7) | Share middle (3-5) |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | R06 | 520 | 1.760 | 1 | 1.111 | 1 | 6 | 1.191 | 0.579 | 0.000 | 0.579 | 0.192 |
  | R27 | 47 | 2.064 | 2 | 1.241 | 2 | 5 | 1.337 | 0.447 | 0.000 | 0.447 | 0.277 |
  | R17 | 52 | 2.077 | 2 | 1.296 | 2 | 5 | 1.367 | 0.481 | 0.000 | 0.481 | 0.327 |
  | R01 | 1174 | 2.164 | 2 | 1.022 | 2 | 6 | 1.358 | 0.287 | 0.000 | 0.287 | 0.315 |
  | R14 | 259 | 2.220 | 2 | 1.359 | 2 | 7 | 1.496 | 0.405 | 0.008 | 0.413 | 0.313 |
  | R11 | 369 | 2.333 | 2 | 1.397 | 2 | 7 | 1.532 | 0.344 | 0.003 | 0.347 | 0.309 |
  | R07 | 547 | 2.404 | 2 | 1.406 | 2 | 7 | 1.580 | 0.335 | 0.004 | 0.338 | 0.353 |
  | R05 | 633 | 2.716 | 2 | 1.554 | 3 | 7 | 1.700 | 0.251 | 0.019 | 0.270 | 0.382 |
  | R03 | 720 | 2.750 | 3 | 1.402 | 2 | 6 | 1.643 | 0.224 | 0.000 | 0.224 | 0.493 |
  | R04 | 620 | 2.821 | 2 | 1.628 | 3 | 7 | 1.715 | 0.265 | 0.008 | 0.273 | 0.405 |
  | R10 | 383 | 2.997 | 3 | 1.311 | 2 | 7 | 1.564 | 0.065 | 0.005 | 0.070 | 0.488 |
  | R08 | 522 | 3.000 | 3 | 1.545 | 2 | 7 | 1.761 | 0.193 | 0.013 | 0.207 | 0.492 |
  | R26 | 46 | 3.000 | 3 | 1.265 | 2 | 6 | 1.605 | 0.109 | 0.000 | 0.109 | 0.587 |
  | R25 | 138 | 3.029 | 3 | 1.249 | 2 | 6 | 1.602 | 0.130 | 0.000 | 0.130 | 0.638 |
  | R02 | 873 | 3.032 | 3 | 1.841 | 3 | 7 | 1.822 | 0.276 | 0.052 | 0.328 | 0.391 |
  | R16 | 268 | 3.086 | 3 | 1.323 | 2 | 7 | 1.661 | 0.108 | 0.011 | 0.119 | 0.604 |
  | R12 | 264 | 3.360 | 3 | 1.152 | 1 | 7 | 1.547 | 0.042 | 0.004 | 0.045 | 0.735 |
  | R15 | 73 | 3.466 | 3 | 1.700 | 3 | 7 | 1.793 | 0.096 | 0.027 | 0.123 | 0.452 |
  | R23 | 589 | 3.469 | 3 | 1.531 | 3 | 7 | 1.799 | 0.110 | 0.029 | 0.139 | 0.625 |
  | R09 | 400 | 3.643 | 4 | 1.819 | 3 | 7 | 1.903 | 0.158 | 0.055 | 0.212 | 0.495 |
  | R19 | 50 | 3.680 | 4 | 1.953 | 3 | 7 | 1.902 | 0.200 | 0.080 | 0.280 | 0.480 |
  | R13 | 254 | 3.681 | 4 | 1.116 | 1 | 7 | 1.520 | 0.016 | 0.004 | 0.020 | 0.799 |
  | R24 | 190 | 3.747 | 4 | 1.593 | 3 | 7 | 1.790 | 0.084 | 0.011 | 0.095 | 0.568 |
  | R18 | 55 | 3.836 | 4 | 1.259 | 2 | 6 | 1.584 | 0.018 | 0.000 | 0.018 | 0.764 |

- **Direction (read off the printed values):** Entropy lowest R06 1.191, highest R09 1.903. Share lowest (1): highest R06 0.579, lowest R13 0.016. Share highest (7): highest R19 0.080; eight raters print 0.000 (R06, R27, R17, R01, R03, R26, R25, R18). Share extreme: highest R06 0.579, lowest R18 0.018. Share middle: highest R13 0.799, lowest R06 0.192.
- **Display difference:** `fb6df84b` prints R09's mean as 3.642; `ovtbl02` prints 3.643 (same stored value, `round(3)` vs `f"{v:.3f}"`). Quote 3.643 with the embedded table. `tbl-rater-overview` prints 3.64.
- **Definitions (N1 `f3482d97`, code):** extreme = categories 1 and 7; middle = 3–5; entropy with natural logarithm. Framing in `f3482d97`: these descriptives "anticipate what the models estimate formally: severity (the mean), scale width/discrimination (SD, entropy), and central or extreme tendency."
- **Caveats:** raw 1–7 values, not adjusted for which products each rater saw. R26, R27, R19, R17, R18 have 46–55 ratings.

## (b) Model comparison and fit

**F1.1 Information criteria**
- **Finding:** The GRM has the lowest AIC and SABIC; M1 has the lowest BIC, with the GRM 4.161 BIC units above it. Within the adjacent-category ladder, M3 has the lowest AIC and SABIC and M1 the lowest BIC.
- **Linked object:** `tbl-model-fit` (N2, `36fafae5`).
- **Numbers:**

  | Model | Software | Family | Log-likelihood | Parameters | AIC | BIC | SABIC | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | sirt::rm.facets | adjacent category | -13,994.486 | 30 | 28,048.971 | 28,235.202 | 28,139.876 | 790.421 | 0.000 | 402.560 |
  | M2 (partial-credit MFRM) | mirt | adjacent category | -13,574.262 | 135 | 27,418.524 | 28,256.560 | 27,827.596 | 159.974 | 21.359 | 90.280 |
  | M3 (GPCM) | mirt | adjacent category | -13,495.966 | 158 | 27,307.931 | 28,288.744 | 27,786.698 | 49.381 | 53.542 | 49.381 |
  | GRM | mirt | cumulative (not in LR ladder) | -13,471.275 | 158 | 27,258.550 | 28,239.363 | 27,737.316 | 0.000 | 4.161 | 0.000 |

- **Best model per criterion (read off):** AIC → GRM; BIC → M1; SABIC → GRM. BIC order: M1 (0.000) < GRM (4.161) < M2 (21.359) < M3 (53.542).
- **Caption:** "Fit of the adjacent-category ladder (M1 rating-scale MFRM, M2 partial-credit MFRM, M3 generalized partial credit model) and the graded response model: log-likelihood, number of parameters, information criteria and their difference (delta) to the best model on each criterion."
- **Notebook statement (`89bc0612`, verbatim):** "**Model comparison.** The adjacent-category models form a ladder: - M1, the rating scale model with a rater shift (Andrich, 1978). This is the many-facet Rasch model (Linacre, 1989; Primi et al., 2019), fitted with `sirt::rm.facets`. - M2, the partial credit model (Masters, 1982): adds rater-specific thresholds. - M3, the generalized partial credit model (Muraki, 1992): adds rater-specific discriminations. The GRM belongs to the cumulative family, so it is compared with the ladder by information criteria only (lower is better)."

**F1.2 Likelihood-ratio tests**
- **Finding:** Both steps up the ladder give p < .001.
- **Linked object:** `tbl-lr-tests` (N2, `ebf910f0`).
- **Numbers:**

  | Comparison | χ² | df | df if all categories used | df equal | p |
  |---|---|---|---|---|---|
  | M1 vs M2: rater-specific thresholds | 840.447 | 105 | 115 | False | < .001 |
  | M2 vs M3: rater-specific discriminations | 156.593 | 23 | 23 | True | < .001 |

- **Notebook explanation (`a5216280`, verbatim):** "**Likelihood-ratio tests.** Each test checks whether the next step up the ladder improves fit: rater-specific thresholds (M1 vs M2), then rater-specific discriminations (M2 vs M3). \"df if all categories used\" is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of unused end categories."
- **Caption:** "Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2."
- **Caveats:** The df difference (115 − 105 = 10) is not printed as a figure. See Flag 4 on how it relates to the category-usage table. M1 fitted in sirt, M2 in mirt. The exact p values are not printed (only "< .001").

**F1.3 GRM estimation**
- **Finding:** The GRM converged after 436 EM iterations with a positive-definite information matrix.
- **Linked object:** `tbl-grm-convergence` (N2, `d2a66a75`).
- **Numbers (single row):** Method EM; Quadrature points 61; SE type Oakes; Tolerance 10⁻⁴; Converged True; Iterations 436; Information matrix positive definite True; Log-likelihood -13,471.275; Parameters 158; AIC 27,258.550; BIC 28,239.363; SABIC 27,737.316; Products 3,669; Ratings (total) 9,046.
- **Notebook statement (`766c1c00`, verbatim):** "**Central model.** Judge response theory treats raters as items and products as persons (Myszkowski & Storme, 2019). It is fitted here as a graded response model (Samejima, 1969) by marginal maximum likelihood in `mirt` (Chalmers, 2012). The table shows whether estimation converged and gives the information criteria."

**F1.4 Discriminations in M3 (GPCM)**
- **Finding:** M3 discriminations range from 0.305 (R18) to 2.221 (R27).
- **Linked object:** `tbl-discrimination-m3` (N2, `a5fa5502`). Headers: Rater | Ratings by rater | Estimate | SE.
- **Numbers (printed order, ascending):** R18 55 0.305 0.141; R09 400 0.306 0.055; R17 52 0.797 0.274; R23 589 0.849 0.082; R03 720 0.861 0.111; R13 254 0.895 0.156; R04 620 0.922 0.147; R11 369 0.926 0.128; R07 547 1.092 0.126; R08 522 1.103 0.176; R05 633 1.193 0.156; R01 1,174 1.219 0.110; R14 259 1.261 0.336; R02 873 1.373 0.285; R19 50 1.395 0.812; R10 383 1.426 0.294; R16 268 1.560 0.222; R15 73 1.621 0.436; R24 190 1.772 0.320; R25 138 2.008 0.419; R26 46 2.042 1.217; R06 520 2.134 0.399; R12 264 2.169 0.516; R27 47 2.221 0.873.
- **Caveats:** Largest SEs: R26 1.217, R27 0.873, R19 0.812 (46–50 ratings each). Notebook framing (`9e0c8a51`): "Rater discriminations in M3. Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data."

**F1.5 Unordered step parameters in M2/M3**
- **Finding:** Nine raters have unordered steps in M2 and eight in M3.
- **Linked object:** `tbl-threshold-order` (N2, `276c901a`). Headers: Model | Rater | Steps | Ordered | Reversals | Step parameters. Ordered is False in every row.
- **Numbers (Rater, Steps, Reversals, Step parameters):**
  - M2 (partial-credit MFRM): R03 5, 1, -0.89;-0.23;1.09;0.68;2.65 — R04 6, 1, -0.56;0.58;0.69;0.55;2.24;3.85 — R05 6, 1, -0.77;0.59;0.57;1.45;1.80;2.71 — R06 5, 1, 0.89;1.24;1.59;2.86;2.39 — R11 6, 1, -0.34;1.01;1.13;1.02;2.77;4.26 — R15 6, 1, -2.27;0.36;0.40;0.20;1.35;3.20 — R17 4, 2, 0.47;0.18;1.32;1.05 — R19 6, 2, -0.49;-0.88;0.08;-0.28;1.25;1.81 — R27 4, 1, 0.18;0.85;0.48;3.04.
  - M3 (GPCM): R03 5, 1, -0.81;-0.21;1.19;0.59;2.73 — R04 6, 1, -0.52;0.62;0.67;0.45;2.19;3.82 — R09 6, 2, -0.43;-0.73;0.60;-0.06;1.09;3.73 — R11 6, 1, -0.26;1.10;1.17;0.98;2.78;4.27 — R15 6, 1, -1.85;0.18;0.37;0.35;1.18;2.69 — R17 4, 2, 0.77;0.21;1.49;0.92 — R18 5, 1, -7.37;-2.14;0.46;-0.70;5.11 — R19 6, 2, -0.57;-0.76;0.01;-0.14;1.09;1.69.
- **Notebook statement (`838c800e`, verbatim):** "Raters whose adjacent-category step parameters are out of order. In adjacent-category models this means that some category is never the most likely response (Andrich, 1978). In the GRM, thresholds are ordered by construction."

**F1.6 Marginal and empirical reliability by model**
- **Linked object:** `tbl-marginal-reliability-models` (N2, `79072096`).
- **Numbers:**

  | Model | Latent variance | Marginal reliability | marginal_rxx (mirt) | Empirical reliability |
  |---|---|---|---|---|
  | M1 (rating-scale MFRM) | 1.053 | 0.957 | – | 0.653 |
  | M2 (partial-credit MFRM) | 1.140 | 0.957 | – | 0.660 |
  | M3 (GPCM) | 1.000 | 0.965 | 0.965 | 0.675 |
  | GRM | 1.000 | 0.969 | 0.969 | 0.689 |

- **Direction (read off):** Empirical reliability rises M1 < M2 < M3 < GRM; marginal reliability M1 = M2 (0.957) < M3 < GRM.
- **Notebook statement (`cab6dfb5`):** "Marginal reliability (hypothetical full panel) and empirical reliability (actual scores) for each model."

**F1.7 GRM rater infit/outfit**
- **Finding:** Under the GRM every rater's infit and outfit is below 1; infit ranges from 0.429 (R02) to 0.980 (R18), outfit from 0.402 (R02) to 0.971 (R18).
- **Linked object:** `tbl-grm-rater-fit` (N2, `f2cf3d5c`). Headers: Rater | Ratings by rater | Infit | Outfit | S-X² | df | p | Imputations.
- **Numbers (Infit / Outfit):** R01 0.718/0.688; R02 0.429/0.402; R03 0.753/0.758; R04 0.626/0.592; R05 0.618/0.618; R06 0.588/0.445; R07 0.782/0.686; R08 0.590/0.580; R09 0.870/0.867; R10 0.620/0.596; R11 0.874/0.849; R12 0.545/0.543; R13 0.841/0.844; R14 0.541/0.461; R15 0.769/0.678; R16 0.800/0.792; R17 0.924/0.900; R18 0.980/0.971; R19 0.529/0.505; R23 0.857/0.846; R24 0.672/0.688; R25 0.717/0.709; R26 0.445/0.450; R27 0.640/0.654.
- **Notebook note (`f526bd7f`, verbatim):** "**Rater fit.** Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982). With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked. S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative. No misfit cut-offs for infit and outfit are applied in this notebook."
- **Caveat:** This table has no flag column; the ⚑ flags appear only in `tbl-rater-overview` (F2.9, Flag 3).

**F1.8 S-X² (multiple imputation)**
- **Finding:** All S-X² p values lie between 0.328 (R11) and 0.665 (R16).
- **Linked object:** `tbl-grm-rater-fit` (N2, `f2cf3d5c`).
- **Numbers (S-X² / df / p; Imputations 20 for every rater):** R01 258.966/259.050/0.490; R02 345.634/345.950/0.495; R03 343.952/345.900/0.519; R04 355.591/361.700/0.581; R05 347.448/341.000/0.393; R06 205.597/211.800/0.607; R07 334.015/334.400/0.496; R08 344.718/339.700/0.414; R09 532.278/528.000/0.440; R10 288.272/291.300/0.539; R11 346.711/335.750/0.328; R12 233.549/239.600/0.598; R13 321.109/316.650/0.420; R14 286.810/284.150/0.445; R15 296.561/297.850/0.510; R16 261.093/271.550/0.665; R17 312.436/311.750/0.478; R18 403.956/407.750/0.544; R19 341.092/338.050/0.443; R23 391.725/391.300/0.484; R24 274.123/276.350/0.527; R25 233.083/235.900/0.540; R26 212.506/215.800/0.551; R27 214.002/214.500/0.497.
- **Caveat:** see the note in F1.7 ("About 90% of the cells are imputed, which makes the test conservative").

**F1.9 Local dependence (Q3)**
- **Finding:** The mean Q3 over 222 computable rater pairs is -0.202, and 28 pairs are flagged; the table shows the ten largest deviations, eight negative and two positive (R09–R23, R10–R11).
- **Linked object:** `tbl-grm-q3-flagged` (N2, `e1768cfb`). Summary line in unlabelled N2 `ccbeaf11` (stdout).
- **Numbers:**
  - Stdout verbatim: "Mean Q3 over 222 computable rater pairs: -0.202; pairs flagged (flag_q3): 28"

    | Rater 1 | Rater 2 | Shared products | Q3 | Q3 minus mean Q3 | Flagged |
    |---|---|---|---|---|---|
    | R08 | R12 | 51 | -0.626 | -0.423 | True |
    | R08 | R19 | 46 | -0.616 | -0.413 | True |
    | R02 | R08 | 72 | -0.613 | -0.411 | True |
    | R02 | R04 | 257 | -0.612 | -0.410 | True |
    | R09 | R23 | 130 | 0.199 | 0.402 | True |
    | R02 | R14 | 108 | -0.594 | -0.392 | True |
    | R10 | R11 | 32 | 0.185 | 0.387 | True |
    | R02 | R05 | 57 | -0.566 | -0.364 | True |
    | R05 | R10 | 152 | -0.542 | -0.339 | True |
    | R01 | R10 | 157 | -0.521 | -0.319 | True |

- **Notebook note (`95a352e9`, verbatim):** "**Local dependence.** Yen's (1984) Q3 is the correlation between two raters' residuals over the products both rated. It is computed for rater pairs with at least 3 jointly rated products (and residual variance in both raters); other pairs are not computable. With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so the table ranks pairs by their deviation from the mean Q3 over all computable pairs (printed below the table). Flagged marks pairs with at least 30 jointly rated products whose Q3 deviates from the mean Q3 by more than 0.2."
- **Caption:** "Rater pairs with the largest local dependence (Q3 minus mean Q3) among pairs with at least 30 jointly rated products."
- **Caveats:** Only 10 of the 28 flagged pairs are shown. R02 appears in four of the ten rows, R08 and R10 in three each (my count). The number of non-computable pairs (276 − 222 = 54, my subtraction) is not printed. Stdout uses the code name "flag_q3".

**F1.10 Global fit (C2)**
- **Finding:** C2 was not computable because 30 of 276 rater pairs share no products.
- **Linked object:** `tbl-grm-global-fit` (N2, `895cb79a`).
- **Numbers:** Statistic C2; Computable False; Rater pairs 276; Rater pairs without shared products 30; Note "Not computable: 30 of 276 rater pairs share no products, so their bivariate moments and hence C2 are undefined."
- **Notebook statement (`8ca12a65`, verbatim):** "**Global fit.** C2 is a limited-information test of overall model fit (Cai & Monroe, 2014). The table reports either the statistic or the reason it could not be computed: C2 needs the joint distribution of every pair of raters, which is undefined for rater pairs that share no products."
- **Caveat:** No other global fit index is reported.

**F1.11 M1 (rating-scale MFRM) rater fit**
- **Finding:** Under M1, three raters have infit and outfit above 1: R09 (1.083/1.060), R17 (1.323/1.167) and R18 (1.170/1.231); R12 is lowest (0.260/0.278).
- **Linked object:** `tbl-rater-fit-m1` (N2, `fcb695cf`). Headers: Rater | Ratings by rater | Infit | Outfit.
- **Numbers (Infit / Outfit):** R01 0.494/0.508; R02 0.823/0.816; R03 0.663/0.664; R04 0.723/0.692; R05 0.738/0.713; R06 0.898/0.703; R07 0.884/0.792; R08 0.573/0.581; R09 1.083/1.060; R10 0.438/0.418; R11 0.994/0.947; R12 0.260/0.278; R13 0.446/0.450; R14 0.769/0.725; R15 0.791/0.736; R16 0.525/0.542; R17 1.323/1.167; R18 1.170/1.231; R19 0.738/0.773; R23 0.762/0.754; R24 0.619/0.625; R25 0.454/0.487; R26 0.326/0.352; R27 0.706/0.709.
- **Notebook statement (`cff2945e`):** "Infit and outfit under M1, the fit statistics usually reported for many-facet Rasch models (Eckes, 2015)."
- **Caveat:** "No misfit cut-offs for infit and outfit are applied in this notebook" (`f526bd7f`).

## (c) Reliability

**F1.12 Marginal reliabilities with 95% intervals**
- **Finding:** The empirical marginal reliability of the actual GRM scores is 0.689 [0.669, 0.703]; the model-based marginal reliability of the hypothetical full panel is 0.969 [0.965, 0.974].
- **Linked object:** `tbl-grm-reliability-ci` (N2, `9cd2a054`). Same values in `tbl-grm-reliability-summary` (`59a029f6`) and `tbl-reliability-overview` (`eee39e77`).
- **Numbers:**

  | Quantity | Estimate | 95% CI lower | 95% CI upper | Draws | Draws rejected |
  |---|---|---|---|---|---|
  | empirical marginal reliability | 0.689 | 0.669 | 0.703 | 200 | 43 |
  | model based marginal reliability | 0.969 | 0.965 | 0.974 | 200 | 43 |

  - Summary rows: "empirical marginal reliability (primary; actual scores)" 0.689; "model based marginal reliability mirt (hypothetical full panel)" 0.969; "model based marginal reliability grid (check)" 0.969; "var theta eap" 0.689; "mean psd squared" 0.311.
  - Overview "CI or note" verbatim: "95% CI [0.669, 0.703] (200 parameter draws); Var(theta)/(Var(theta)+mean(PSD^2))" and "95% CI [0.965, 0.974] (200 parameter draws); mirt::marginal rxx, all raters".
- **Notebook explanation (`8ccf3d9c`, verbatim):** "**Uncertainty of the marginal reliabilities.** 95% intervals from 200 draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. Draws counts the accepted draws. A draw is rejected and replaced when it is not a valid GRM, that is when some discrimination a ≤ 0 or some rater's thresholds are out of order; Draws rejected counts these."
- **Notebook explanation (`5b630dd6`, verbatim):** "**Reliability of the actual scores.** The empirical marginal reliability Var(θ̂)/(Var(θ̂) + mean PSD²) refers to the EAP scores actually obtained (Chalmers, 2012) and is the primary figure. The model-based marginal reliability (Green et al., 1984) refers to the hypothetical full panel. rel_post = 1 − PSD² gives each product's reliability from its own raters."
- **Caption:** "Empirical and model-based marginal reliability of the GRM with 95% intervals from accepted parameter draws; draws that did not give a valid GRM were rejected and replaced."

**F1.13 Distribution of product-level reliability rel_post**
- **Finding:** rel_post = 1 − PSD² has a median of 0.712 (Q1 0.599, Q3 0.789, IQR 0.191) and ranges from 0.068 to 0.954.
- **Linked objects:** `tbl-grm-reliability-summary` (N2, `59a029f6`); `fig-grm-rel-post-histogram` (`25a35b26`; note `82d77d33` "Distribution of product-level reliability across products.").
- **Numbers:** rel post min 0.068; rel post p10 0.508; rel post q1 0.599; rel post median 0.712; rel post q3 0.789; rel post p90 0.866; rel post max 0.954; rel post mean 0.689; rel post iqr 0.191.
- **Overview row:** "GRM: median rel post" 0.712, note "first quartile 0.599, third quartile 0.789"; "GRM: IQR rel post" 0.191.

**F1.14 Reliability by number of ratings per product (observed)**
- **Finding:** Mean rel_post rises from 0.522 (1 rating) to 0.915 (9 ratings), drops to 0.897 at 10 ratings, and reaches 0.948 at 12 and 0.947 at 13 ratings; mean PSD falls from 0.684 to 0.228–0.230.
- **Linked objects:** `tbl-grm-reliability-by-n` (N2, `657292d8`); `fig-grm-rel-post-by-n` (`cf6ef810`; note `29d8973a` "Product-level reliability by number of ratings (the same information as the table above, as a figure).").
- **Numbers (every row):**

  | Ratings per product | Products | Mean rel_post | Median rel_post | Mean rel_info | Mean PSD |
  |---|---|---|---|---|---|
  | 1 | 832 | 0.522 | 0.528 | 0.544 | 0.684 |
  | 2 | 2,107 | 0.699 | 0.716 | 0.714 | 0.544 |
  | 3 | 68 | 0.756 | 0.769 | 0.775 | 0.489 |
  | 4 | 153 | 0.814 | 0.831 | 0.818 | 0.426 |
  | 5 | 198 | 0.851 | 0.863 | 0.857 | 0.382 |
  | 6 | 137 | 0.875 | 0.885 | 0.880 | 0.350 |
  | 7 | 95 | 0.890 | 0.895 | 0.893 | 0.330 |
  | 8 | 36 | 0.908 | 0.910 | 0.911 | 0.301 |
  | 9 | 22 | 0.915 | 0.915 | 0.915 | 0.290 |
  | 10 | 14 | 0.897 | 0.919 | 0.902 | 0.314 |
  | 11 | 4 | 0.922 | 0.915 | 0.926 | 0.277 |
  | 12 | 2 | 0.948 | 0.948 | 0.946 | 0.228 |
  | 13 | 1 | 0.947 | 0.947 | 0.947 | 0.230 |

- **Non-monotonic rows (read off):** Mean rel_post at 10 ratings (0.897) is below 9 ratings (0.915); at 13 (0.947) below 12 (0.948). Median rel_post at 11 (0.915) is below 10 (0.919). Mean rel_info at 10 (0.902) below 9 (0.915). Mean PSD at 10 (0.314) above 9 (0.290); at 13 (0.230) above 12 (0.228).
- **Notebook statement (`a30edc1b`):** "**Reliability by number of ratings.** How product-level precision grows with the number of ratings a product received."
- **Caveats:** Rows 10–13 rest on 14, 4, 2 and 1 products. No CIs. No row reaches 0.969.

**F1.15 Full-panel (hypothetical) information and reliability**
- **Linked object:** `fig-grm-panel-information` (N2, `715f5154`). Figure only; the only printed full-panel value is the model-based 0.969 (F1.12).
- **Notebook statement (`c8ad3efc`, verbatim):** "**Full panel.** Information and conditional reliability I/(I+1) if every rater rated a product. This is a hypothetical upper bound, not the precision of the actual scores."
- **Caption:** "Information and conditional reliability I/(I+1) of the full panel. The curve is hypothetical: it applies to a product rated by all raters."

**F1.16 Consistency of rel_post and rel_info**
- **Finding:** The two product-level indices correlate at 0.947; the mean of rel_info − rel_post is 0.015, the maximum absolute difference 0.358, and 229 products differ by more than 0.1.
- **Linked objects:** `tbl-grm-reliability-summary` (`59a029f6`); `fig-grm-rel-consistency` (`40422b1f`).
- **Numbers:** consistency cor rel post rel info 0.947; consistency mean diff rel info minus rel post 0.015; consistency max abs diff 0.358; products abs diff gt 0.1 229.
- **Notebook statement (`f203ce16`, verbatim):** "**Check.** Two routes to the same product-level reliability: from the posterior (rel_post) and from the information of the product's own raters (rel_info). Points near the diagonal mean the two routes agree."

**F1.17 rel_post by θ̂**
- **Linked object:** `fig-grm-rel-post-by-theta` (N2, `1fceb3c7`). Figure only; no numbers printed.
- **Notebook statement (`83614bc3`):** "Product-level reliability by estimated creativity. Precision depends on where a product lies relative to its raters' thresholds."

**F1.18 Naive indices with bootstrap CIs**
- **Finding:** Pairwise-covariance Cronbach's α is 0.949 (18 raters, 1,946 products; 353 of 1,000 bootstrap replications failed), the fully crossed block gives 0.750 (3 raters, 261 products), and Krippendorff's ordinal α is 0.391 (24 raters, 2,837 products).
- **Linked objects:** `tbl-naive-indices` (N2, `301d57ec`); `tbl-reliability-overview` (`eee39e77`).
- **Numbers:**

  | Index | Value | 95% CI lower | 95% CI upper | Raters | Products | Bootstrap replications | Failed replications |
  |---|---|---|---|---|---|---|---|
  | Cronbach's alpha: pairwise covariances, all usable raters | 0.949 | 0.926 | 0.958 | 18 | 1,946 | 1,000 | 353 |
  | Cronbach's alpha: fully crossed block (listwise complete) | 0.750 | 0.684 | 0.800 | 3 | 261 | 1,000 | 0 |
  | Krippendorff's alpha (ordinal) | 0.391 | 0.363 | 0.417 | 24 | 2,837 | 1,000 | 0 |

  Overview "CI or note" entries verbatim: "95% bootstrap CI [0.363, 0.417], 1,000 replications"; "95% CI [0.926, 0.958] (bootstrap, 647 of 1,000 replications computable, approximate); 18 raters; removed: R26;R19;R14;R02;R12;R27"; "95% CI [0.684, 0.800] (bootstrap, 1,000 replications); 3 raters, 261 products".
- **Notebook note (`3262dbf6`, verbatim):** "**Naive indices** are reference values for common practice. They are not used downstream. - **Cronbach's α** (Cronbach, 1951) measures the consistency of the unweighted rater mean. It assumes τ-equivalent raters and complete data, so here it is computed from pairwise covariances and on the largest fully crossed block. - **Krippendorff's α** (ordinal; Hayes & Krippendorff, 2007) measures the agreement of single ratings, treating raters as interchangeable. Confidence intervals for both come from a bootstrap over products. For the pairwise Cronbach's α, replications in which some rater pair loses all shared products cannot be computed; the interval uses the remaining replications and is approximate (Failed replications in the table)."
- **Caveats:** Six raters were removed for the pairwise α (R26, R19, R14, R02, R12, R27); the removal rule is not stated in the notebook. The three raters of the crossed block are not named.

**F1.19 Overview of indices**
- **Linked object:** `tbl-reliability-overview` (N2, `eee39e77`). Headers: Index | Refers to | Value | CI or note.
- **Rows (Index — Refers to — Value):** Krippendorff's alpha (ordinal) — consensus of single ratings — 0.391; Cronbach's alpha (pairwise covariances) — consistency of the unweighted rater mean — 0.949; Cronbach's alpha (fully crossed block) — consistency of the unweighted rater mean (crossed subset) — 0.750; GRM: empirical marginal reliability — actual theta hat (primary) — 0.689; **GRM: empirical marginal reliability, at least 4 ratings per product (simulated) — actual design topped up to at least 4 ratings per product — 0.835** (note: "95% range [0.829, 0.840], 50 replications; 6,778 ratings added to 3,007 products"); GRM: model-based marginal reliability — hypothetical full panel — 0.969; GRM: median rel post — precision per product — 0.712; GRM: IQR rel post — precision per product — 0.191; M1 (rating-scale MFRM): marginal reliability — comparison — 0.957; M2 (partial-credit MFRM): marginal reliability — comparison — 0.957; M3 (GPCM): marginal reliability — comparison — 0.965.
- **Notebook statement (`3616abab`, verbatim):** "**Overview.** All indices side by side, with what each refers to. They answer different questions: the reliability of the actual scores, of a hypothetical full panel, or of single ratings. They are not interchangeable."

**F1.20 Projected reliability by number of ratings per product (simulation)**
- **Finding:** With k raters drawn at random per simulated product, the projected empirical marginal reliability rises at every step from 0.530 [0.513, 0.544] at k = 1 to 0.928 [0.925, 0.931] at k = 10.
- **Linked objects:** `tbl-grm-reliability-projection` (N2, `b7cae78d`); `fig-grm-reliability-projection` (`4f64ac77`). Settings in unlabelled N2 `64142953` (stdout).
- **Numbers (every k):**

  | Ratings per product (k) | Empirical reliability [95% range] | Mean rel_post |
  |---|---|---|
  | 1 | 0.530 [0.513, 0.544] | 0.530 |
  | 2 | 0.705 [0.696, 0.713] | 0.706 |
  | 3 | 0.787 [0.778, 0.797] | 0.787 |
  | 4 | 0.834 [0.827, 0.841] | 0.834 |
  | 5 | 0.864 [0.857, 0.872] | 0.864 |
  | 6 | 0.884 [0.879, 0.888] | 0.885 |
  | 7 | 0.900 [0.896, 0.903] | 0.900 |
  | 8 | 0.911 [0.907, 0.915] | 0.911 |
  | 9 | 0.921 [0.917, 0.925] | 0.921 |
  | 10 | 0.928 [0.925, 0.931] | 0.928 |

- **Settings (stdout `64142953`, verbatim):** "50 replications of 2000 simulated products per k; seed 20260713."
- **Procedure and assumptions (note `77937868`, verbatim):** "**Projected reliability with more ratings.** A model-based gauge of the value of adding ratings, complementing the observed values above. Products with θ ~ N(0, 1) are simulated; each gets k ratings from k raters of the actual panel, drawn at random, with ratings generated from the fitted GRM and scored with its parameters (treated as known). The table gives the empirical marginal reliability (mean and 95% range over replications) and the mean product-level reliability rel_post."
- **Captions (verbatim):** Table: "Projected reliability of GRM scores by number of ratings per product (k), simulated from the fitted model with raters of the panel drawn at random (each equally likely): empirical marginal reliability with its 95% range over 50 replications of 2,000 products, and mean product-level reliability (1 − PSD²)." Figure: "Projected empirical marginal reliability by number of ratings per product, simulated from the fitted GRM with randomly drawn raters. Band: 95% range over replications."
- **What the notebook says about rater drawing:** "drawn at random", "each equally likely". It does **not** state explicitly that rater workload is ignored, nor whether draws are with or without replacement within a product; it does not name the true-score definition. Parameters "treated as known" (no parameter uncertainty in the band). Replications 50; products per replication 2000; seed 20260713.
- **Direction (read off):** Empirical reliability and Mean rel_post differ by at most 0.001 in any row. First k with empirical ≥ 0.80 is k = 4 (0.834); ≥ 0.90 is k = 7 (0.900). The notebook does not print these thresholds. No k reaches 0.969; maximum 0.928 at k = 10. Only k = 1–10 is covered.

**F1.21 Simulated reliability of the actual design topped up to at least 4 ratings (NEW)**
- **Finding:** Topping up the actual design so that every product has at least 4 ratings (3,007 products topped up, 6,778 ratings added, 15,824 ratings in total) gives a simulated empirical reliability of 0.835 [0.829, 0.840]; the same simulation on the unchanged design gives 0.686 [0.675, 0.695].
- **Linked object:** **`tbl-grm-reliability-min-ratings` (N2, `26c01033`, NEW)**. The min-4 value also appears in `tbl-reliability-overview` and as an in-figure label in `fig-grm-reliability-observed-vs-simulated`.
- **Numbers (both rows, every column):**

  | Design | Products topped up | Ratings added | Ratings (total) | Empirical reliability [95% range] | Mean rel_post | Replications |
  |---|---|---|---|---|---|---|
  | Actual design | 0 | 0 | 9,046 | 0.686 [0.675, 0.695] | 0.687 | 50 |
  | At least 4 ratings per product | 3,007 | 6,778 | 15,824 | 0.835 [0.829, 0.840] | 0.835 | 50 |

- **Procedure and assumptions (note `c7486592`, verbatim):** "**Minimum number of ratings per product.** The actual design with every product topped up to at least 4 ratings: for each product with fewer than 4 ratings, the missing ratings are generated from the fitted GRM by raters of the panel drawn at random (equal probability), the real ratings are kept, and all products are rescored with the GRM (parameters treated as known). The row for the actual design repeats the simulation on the unchanged design, as a check against the observed empirical reliability."
- **Caption (verbatim):** "Simulated reliability of the actual design (check) and of the actual design topped up so that every product has at least 4 ratings: empirical marginal reliability with its 95% range over 50 replications, mean product-level reliability (1 − PSD²), and the number of products topped up and ratings added."
- **What the notebook does and does not state:** raters "drawn at random (equal probability)"; real ratings kept; all products rescored with the GRM; parameters treated as known; 50 replications. Not stated: whether a topped-up product can receive a second rating from a rater who already rated it, whether workload is respected (it says equal probability), the seed for this simulation, and how θ for the actual products enters the generation of the added ratings (the note says the missing ratings are "generated from the fitted GRM"; nothing more). Treat these as NOT IN NOTEBOOK.
- **Check row vs observed (read off):** the simulated "Actual design" value 0.686 vs the observed empirical reliability 0.689 (F1.12); the notebook calls the row "a check against the observed empirical reliability" but does not print the difference.
- **Arithmetic check (mine):** 9,046 + 6,778 = 15,824, consistent. 3,007 = 832 + 2,107 + 68 (products with 1, 2, 3 ratings in F1.14), consistent.

**F1.22 Observed vs simulated reliability by number of ratings (NEW table)**
- **Finding:** For every k from 1 to 10 the observed mean rel_post is below the simulated empirical reliability; the simulated column is "–" for k = 11–13.
- **Linked object:** **`tbl-grm-reliability-observed-vs-simulated` (N2, `00aeab14`, NEW)**.
- **Numbers (every row):**

  | Ratings per product (k) | Products | Observed mean rel_post | Simulated empirical reliability [95% range] |
  |---|---|---|---|
  | 1 | 832 | 0.522 | 0.530 [0.513, 0.544] |
  | 2 | 2,107 | 0.699 | 0.705 [0.696, 0.713] |
  | 3 | 68 | 0.756 | 0.787 [0.778, 0.797] |
  | 4 | 153 | 0.814 | 0.834 [0.827, 0.841] |
  | 5 | 198 | 0.851 | 0.864 [0.857, 0.872] |
  | 6 | 137 | 0.875 | 0.884 [0.879, 0.888] |
  | 7 | 95 | 0.890 | 0.900 [0.896, 0.903] |
  | 8 | 36 | 0.908 | 0.911 [0.907, 0.915] |
  | 9 | 22 | 0.915 | 0.921 [0.917, 0.925] |
  | 10 | 14 | 0.897 | 0.928 [0.925, 0.931] |
  | 11 | 4 | 0.922 | – |
  | 12 | 2 | 0.948 | – |
  | 13 | 1 | 0.947 | – |

- **Note (`7561808c`, verbatim):** "Observed and simulated reliability by number of ratings side by side. Observed: mean rel_post of the actual products with that many ratings. Simulated: the projection above (k raters drawn at random per simulated product)."
- **Caption (verbatim):** "Reliability by number of ratings per product: observed mean product-level reliability (1 − PSD²) of the actual products, and simulated empirical marginal reliability with its 95% range over 50 replications (projection with randomly drawn raters)."
- **Direction (read off):** Observed lies inside the simulated 95% range at k = 1 (0.522 in [0.513, 0.544]), k = 2 (0.699 in [0.696, 0.713]) and k = 8 (0.908 in [0.907, 0.915]); it lies below the lower bound at k = 3, 4, 5, 6, 7, 9 and 10. Largest gap at k = 10 (0.897 vs 0.928; 14 products). The notebook prints no differences or tests.
- **Caveats:** The two columns are different quantities (observed mean rel_post of actual products vs simulated empirical marginal reliability; see the note). This table is a display-only merge of `tbl-grm-reliability-by-n` and `tbl-grm-reliability-projection`.

**F1.23 Observed vs simulated reliability (NEW figure)**
- **Linked object:** **`fig-grm-reliability-observed-vs-simulated` (N2, `7297874b`, NEW)**. One `display_data` output ("<Figure size 700x400 with 1 Axes>"); no text output.
- **Caption (verbatim, from the cell source via the build script line 373):** "Reliability by number of ratings per product. Dots: observed mean product-level reliability (1 − PSD²) of the actual products with that many ratings (dot size = number of products; faded = fewer than 10 products). Line and band: simulated empirical marginal reliability (mean and 95% range over 50 replications) for products that each receive exactly k ratings from k raters drawn at random from the panel with equal probability, with ratings generated and scored by the fitted GRM. Dashed lines: simulated reliability of the actual design topped up to at least 4 ratings per product, and model-based reliability of the hypothetical full panel."
- **What is plotted (from code):** x = Ratings per product (1 to 13), y = Reliability (axis 0.45–1.0); blue dots = observed mean rel_post per k from `reliability_by_n_ratings.csv` (size ∝ √products; alpha .25 if fewer than 10 products, i.e. k = 11, 12, 13); orange line with squares and band = `reliability_projection.csv` empirical and [q025, q975] for k = 1–10; dotted grey lines at .70 and .80 labelled ".70"/".80"; purple dashed line at the min-4 empirical value labelled "actual design, at least 4 ratings per product: <value>"; green dashed line at the full-panel value labelled "full panel of <n raters> raters: <value>"; legend "Simulated (k random raters)" / "Observed (actual products)".
- **In-image numbers:** the two dashed-line labels are rendered from the CSVs with `r3()` (no leading zero), so they read ".835" and ".969" and "24 raters" by construction. Values read off the image are not quotable; the quotable sources are `tbl-grm-reliability-min-ratings` (0.835) and `tbl-reliability-overview` / `tbl-grm-reliability-ci` (0.969), `tbl-design-summary` (24).

## (d) Rater parameters, information and uncertainty

**F2.1 GRM discrimination a with SE**
- **Finding:** GRM discriminations range from 0.66 (R18) to 3.19 (R26).
- **Linked object:** `tbl-grm-rater-parameters` (N2, `2dd874d8`). Headers: Rater | Ratings by rater | a | b1 | b2 | b3 | b4 | b5 | b6.
- **Numbers (a (SE)):** R01 1,174 1.82 (0.13); R02 873 2.71 (0.35); R03 720 1.83 (0.17); R04 620 1.93 (0.21); R05 633 2.36 (0.23); R06 520 3.10 (0.45); R07 547 2.01 (0.17); R08 522 2.13 (0.25); R09 400 0.93 (0.15); R10 383 2.37 (0.34); R11 369 1.86 (0.19); R12 264 2.72 (0.46); R13 254 1.54 (0.22); R14 259 2.54 (0.53); R15 73 2.76 (0.54); R16 268 2.47 (0.26); R17 52 1.81 (0.53); R18 55 0.66 (0.27); R19 50 2.70 (1.01); R23 589 1.75 (0.13); R24 190 2.89 (0.37); R25 138 3.01 (0.47); R26 46 3.19 (1.72); R27 47 3.04 (0.91).
- **Direction (read off):** Highest a: R26 3.19 (46 ratings, SE 1.72); lowest: R18 0.66 (55 ratings, SE 0.27). Largest SEs: R26 1.72, R19 1.01, R27 0.91. Smallest SEs: R01 0.13, R23 0.13.
- **Caption:** "Rater parameters of the graded response model in IRT metric: discrimination a and thresholds b1 to b6 (bk separates rating categories k and k + 1), each as estimate (standard error). A dash marks a threshold above the highest category a rater used."

**F2.2 GRM thresholds b_k with SE**
- **Finding:** b1 ranges from -6.25 (R18) to 0.25 (R06); R06 is the only rater with a positive b1.
- **Linked object:** `tbl-grm-rater-parameters` (N2, `2dd874d8`).
- **Numbers:**

  | Rater | Ratings by rater | b1 | b2 | b3 | b4 | b5 | b6 |
  |---|---|---|---|---|---|---|---|
  | R01 | 1,174 | -0.81 (0.06) | 0.59 (0.05) | 1.79 (0.10) | 2.84 (0.16) | 3.92 (0.29) | – |
  | R02 | 873 | -0.67 (0.06) | -0.02 (0.05) | 0.41 (0.05) | 0.90 (0.06) | 1.38 (0.08) | 1.99 (0.12) |
  | R03 | 720 | -1.11 (0.08) | -0.16 (0.06) | 0.77 (0.07) | 1.30 (0.10) | 2.51 (0.20) | – |
  | R04 | 620 | -0.79 (0.08) | 0.17 (0.06) | 0.68 (0.07) | 1.13 (0.09) | 2.10 (0.15) | 3.51 (0.33) |
  | R05 | 633 | -0.83 (0.07) | 0.13 (0.05) | 0.66 (0.06) | 1.28 (0.08) | 1.86 (0.12) | 2.70 (0.19) |
  | R06 | 520 | 0.25 (0.05) | 0.98 (0.07) | 1.53 (0.10) | 2.19 (0.16) | 2.62 (0.22) | – |
  | R07 | 547 | -0.52 (0.07) | 0.44 (0.06) | 1.11 (0.08) | 1.75 (0.12) | 2.51 (0.18) | 3.90 (0.42) |
  | R08 | 522 | -1.17 (0.10) | -0.29 (0.06) | 0.39 (0.07) | 1.10 (0.09) | 1.90 (0.14) | 3.01 (0.26) |
  | R09 | 400 | -2.05 (0.31) | -1.00 (0.18) | -0.06 (0.12) | 0.72 (0.15) | 1.79 (0.26) | 3.49 (0.50) |
  | R10 | 383 | -1.99 (0.16) | -0.19 (0.07) | 0.44 (0.08) | 1.09 (0.11) | 2.04 (0.19) | 3.22 (0.41) |
  | R11 | 369 | -0.49 (0.09) | 0.62 (0.08) | 1.20 (0.11) | 1.71 (0.14) | 2.75 (0.25) | 4.13 (0.62) |
  | R12 | 264 | -2.05 (0.21) | -0.90 (0.10) | 0.20 (0.08) | 1.34 (0.12) | 2.23 (0.20) | 3.60 (0.49) |
  | R13 | 254 | -3.36 (0.47) | -1.52 (0.19) | -0.30 (0.11) | 1.13 (0.15) | 2.54 (0.32) | 4.31 (0.80) |
  | R14 | 259 | -0.17 (0.09) | 0.58 (0.09) | 1.13 (0.13) | 1.89 (0.20) | 2.45 (0.28) | 3.19 (0.43) |
  | R15 | 73 | -1.67 (0.24) | -0.21 (0.14) | 0.27 (0.13) | 0.66 (0.14) | 1.30 (0.19) | 2.60 (0.41) |
  | R16 | 268 | -1.53 (0.13) | -0.52 (0.08) | 0.43 (0.08) | 1.36 (0.12) | 2.31 (0.19) | 3.18 (0.31) |
  | R17 | 52 | -0.18 (0.20) | 0.47 (0.22) | 1.14 (0.34) | 1.70 (0.47) | – | – |
  | R18 | 55 | -6.25 (2.86) | -2.59 (1.13) | -0.51 (0.47) | 0.96 (0.56) | 4.28 (1.69) | – |
  | R19 | 50 | -1.03 (0.24) | -0.63 (0.20) | -0.14 (0.18) | 0.23 (0.19) | 1.03 (0.25) | 1.87 (0.37) |
  | R23 | 589 | -1.75 (0.12) | -0.92 (0.08) | 0.02 (0.06) | 0.81 (0.08) | 1.83 (0.12) | 2.83 (0.20) |
  | R24 | 190 | -1.66 (0.15) | -0.79 (0.09) | -0.29 (0.08) | 0.26 (0.08) | 1.09 (0.12) | 2.56 (0.35) |
  | R25 | 138 | -1.25 (0.14) | -0.45 (0.10) | 0.35 (0.10) | 1.27 (0.14) | 2.39 (0.35) | – |
  | R26 | 46 | -1.15 (0.33) | -0.18 (0.18) | 0.58 (0.20) | 1.55 (0.31) | 2.69 (0.61) | – |
  | R27 | 47 | -0.30 (0.15) | 0.46 (0.17) | 0.92 (0.21) | 2.16 (0.49) | – | – |

- **Notebook note (`2896214b`, verbatim):** "**Rater parameters.** a is the rater's discrimination: how sharply the ratings separate products of different creativity. b_k is the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater. For a rater without an internal category gap, b_k separates categories k and k + 1; raters who never used the top categories have no estimate for the highest thresholds. For a rater with an internal gap (an unused category inside the observed range, see the category-use table), the thresholds separate other category boundaries and are not directly comparable with those of the other raters."
- **Caveats:** R27 has an internal gap (category 5 unused), so by the note its four thresholds are "not directly comparable with those of the other raters"; the table does not mark this. R18 has the largest threshold SEs (b1 SE 2.86, b5 SE 1.69). Dashes: b6 for R01, R03, R06, R18, R25, R26; b5–b6 for R17, R27.

**F2.3 Discrimination with 95% intervals (NEW figure)**
- **Linked object:** **`fig-grm-rater-discrimination-ci` (N2, `053aebab`, NEW)**. Figure only; no printed values.
- **Caption (verbatim):** "Discrimination a per rater in the graded response model with 95% intervals (estimate ± 1.96 SE), sorted by a. Dashed line: median. Under the Rasch-family models M1 and M2 all raters share one value."
- **Note (`8212b3db`, verbatim):** "Discrimination per rater as a figure, with 95% intervals (estimate ± 1.96 SE). Under M1 and M2 all raters would share one value."
- **What is plotted (from code):** one row per rater sorted by a (ascending from the bottom), point = a, horizontal bar = ±1.96 × a_se from `rater_parameters.csv`, vertical dashed line at the median a, x label "Discrimination a". The underlying values are those of F2.1 (2 decimals). The median a and the interval bounds are not printed anywhere (not quotable).

**F2.4 Rater information summary and shares**
- **Finding:** Information per rating ranges from 0.135 (R18) to 2.517 (R26); the share of panel information from 0.004 (R18) to 0.074 (R26).
- **Linked objects:** `tbl-grm-information-summary` (N2, `31b650f2`); `fig-grm-rater-information` (`bff96842`); `fig-grm-information-shares` (`347ba06c`).
- **Headers:** Rater | Ratings by rater | Information per rating | θ at maximum | Maximum information | Share of panel information | Share at θ = −2 | Share at θ = −1 | Share at θ = 0 | Share at θ = 1 | Share at θ = 2.
- **Numbers (Information per rating / θ at maximum / Maximum information / Share / shares at θ = −2, −1, 0, 1, 2):**
  - R01 0.860 / 2.800 / 0.980 / 0.025 / 0.022, 0.029, 0.023, 0.025, 0.028
  - R02 1.965 / 0.400 / 2.320 / 0.058 / 0.013, 0.054, 0.060, 0.060, 0.058
  - R03 0.971 / 0.900 / 1.047 / 0.029 / 0.033, 0.034, 0.027, 0.027, 0.027
  - R04 1.040 / 0.650 / 1.181 / 0.031 / 0.021, 0.033, 0.030, 0.031, 0.031
  - R05 1.523 / 0.650 / 1.742 / 0.045 / 0.022, 0.049, 0.043, 0.045, 0.048
  - R06 1.702 / 2.300 / 2.932 / 0.050 / 0.001, 0.007, 0.056, 0.075, 0.082
  - R07 1.067 / 1.300 / 1.269 / 0.031 / 0.013, 0.029, 0.031, 0.033, 0.036
  - R08 1.322 / 0.300 / 1.414 / 0.039 / 0.040, 0.046, 0.037, 0.037, 0.038
  - R09 0.276 / 0.100 / 0.281 / 0.008 / 0.018, 0.010, 0.007, 0.007, 0.008
  - R10 1.486 / 0.500 / 1.734 / 0.044 / 0.101, 0.034, 0.044, 0.044, 0.046
  - R11 0.912 / 1.200 / 1.104 / 0.027 / 0.013, 0.025, 0.026, 0.029, 0.030
  - R12 1.890 / 1.450 / 2.058 / 0.056 / 0.137, 0.070, 0.051, 0.048, 0.059
  - R13 0.683 / -0.600 / 0.698 / 0.020 / 0.045, 0.025, 0.018, 0.018, 0.019
  - R14 1.490 / 2.200 / 1.986 / 0.044 / 0.004, 0.022, 0.049, 0.052, 0.057
  - R15 2.009 / 0.350 / 2.397 / 0.059 / 0.110, 0.050, 0.061, 0.060, 0.046
  - R16 1.680 / 2.400 / 1.763 / 0.049 / 0.079, 0.058, 0.045, 0.045, 0.049
  - R17 0.814 / 0.800 / 1.041 / 0.024 / 0.008, 0.018, 0.026, 0.027, 0.023
  - R18 0.135 / -0.400 / 0.137 / 0.004 / 0.009, 0.005, 0.004, 0.003, 0.004
  - R19 2.029 / -0.250 / 2.300 / 0.060 / 0.033, 0.074, 0.060, 0.055, 0.053
  - R23 0.933 / 0.300 / 0.956 / 0.027 / 0.055, 0.033, 0.025, 0.025, 0.027
  - R24 2.313 / -0.350 / 2.578 / 0.068 / 0.120, 0.083, 0.067, 0.060, 0.043
  - R25 2.361 / -0.450 / 2.583 / 0.069 / 0.055, 0.088, 0.066, 0.063, 0.060
  - R26 2.517 / 0.500 / 2.832 / 0.074 / 0.042, 0.093, 0.074, 0.064, 0.062
  - R27 2.013 / 0.650 / 2.794 / 0.059 / 0.004, 0.031, 0.068, 0.067, 0.066
- **Direction (read off):** θ at maximum ranges from -0.600 (R13) to 2.800 (R01). Maximum information ranges from 0.137 (R18) to 2.932 (R06). At θ = −2 the largest shares are R12 0.137, R24 0.120, R15 0.110, R10 0.101; at θ = 2 the largest are R06 0.082, R27 0.066, R24 is 0.043.
- **Caption:** "Rater information summary: information integrated over N(0, 1), location and height of the maximum, and share of the full-panel information (weighted over N(0, 1) and at selected values of θ)."
- **Notebook statements:** `1a2b3c14` "**Rater information.** I_j(θ) shows how much a rater's rating tells about θ at each level of creativity. Information from different raters adds up under local independence."; `b69896ff` "**Information shares.** Each rater's share of the total information of all raters, along θ."; `3e064209` "**Information summary.** For each rater: information averaged over the N(0, 1) distribution of θ, where it peaks, and the rater's share of the full-panel information."

**F2.5 Intervals for rater information and share**
- **Finding:** The intervals are widest for R26 (information 2.52 [0.11, 6.75]; share 0.074 [0.003, 0.178]) and R19 (2.03 [0.27, 5.31]; 0.060 [0.008, 0.141]).
- **Linked object:** `tbl-grm-rater-information-ci` (N2, `bedab482`).
- **Numbers:**

  | Rater | Ratings by rater | Information per rating [95% interval] | Share of panel information [95% interval] |
  |---|---|---|---|
  | R01 | 1,174 | 0.86 [0.66, 1.05] | 0.025 [0.019, 0.031] |
  | R02 | 873 | 1.96 [1.11, 2.97] | 0.058 [0.031, 0.088] |
  | R03 | 720 | 0.97 [0.65, 1.33] | 0.029 [0.018, 0.039] |
  | R04 | 620 | 1.04 [0.67, 1.44] | 0.031 [0.019, 0.044] |
  | R05 | 633 | 1.52 [1.04, 2.11] | 0.045 [0.029, 0.059] |
  | R06 | 520 | 1.70 [0.96, 2.50] | 0.050 [0.027, 0.072] |
  | R07 | 547 | 1.07 [0.80, 1.41] | 0.031 [0.022, 0.042] |
  | R08 | 522 | 1.32 [0.87, 1.92] | 0.039 [0.023, 0.057] |
  | R09 | 400 | 0.28 [0.13, 0.48] | 0.008 [0.004, 0.015] |
  | R10 | 383 | 1.49 [0.83, 2.19] | 0.044 [0.026, 0.066] |
  | R11 | 369 | 0.91 [0.60, 1.22] | 0.027 [0.017, 0.038] |
  | R12 | 264 | 1.89 [0.93, 2.99] | 0.056 [0.028, 0.088] |
  | R13 | 254 | 0.68 [0.38, 1.08] | 0.020 [0.011, 0.033] |
  | R14 | 259 | 1.49 [0.53, 2.62] | 0.044 [0.016, 0.077] |
  | R15 | 73 | 2.01 [0.82, 3.54] | 0.059 [0.024, 0.105] |
  | R16 | 268 | 1.68 [1.11, 2.32] | 0.049 [0.033, 0.071] |
  | R17 | 52 | 0.81 [0.23, 1.80] | 0.024 [0.006, 0.052] |
  | R18 | 55 | 0.13 [0.02, 0.39] | 0.004 [0.000, 0.011] |
  | R19 | 50 | 2.03 [0.27, 5.31] | 0.060 [0.008, 0.141] |
  | R23 | 589 | 0.93 [0.69, 1.16] | 0.027 [0.018, 0.036] |
  | R24 | 190 | 2.31 [1.34, 3.53] | 0.068 [0.040, 0.097] |
  | R25 | 138 | 2.36 [1.20, 3.40] | 0.069 [0.036, 0.101] |
  | R26 | 46 | 2.52 [0.11, 6.75] | 0.074 [0.003, 0.178] |
  | R27 | 47 | 2.01 [0.50, 4.12] | 0.059 [0.014, 0.115] |

- **Caption:** "Average information per rating (information integrated over θ ~ N(0, 1)) and share of the full-panel information for each rater, with 95% intervals from 200 accepted parameter draws."
- **Notebook note (`eab45d1d`, verbatim):** "**Uncertainty of rater information.** 95% intervals for each rater's average information and share, from the same parameter draws. Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings."
- **Caveats:** Same draws as F1.12 (200 accepted, 43 rejected). Information prints with 2 decimals here, 3 in F2.4 (e.g. R26 2.517 vs 2.52). R18's lower share bound prints 0.000.

**F2.6 Information per rating with intervals (NEW figure)**
- **Linked object:** **`fig-grm-rater-information-ci` (N2, `f2df62dc`, NEW)**. Figure only.
- **Caption (verbatim):** "Average information per rating (information integrated over θ ~ N(0, 1)) for each rater with 95% intervals from 200 accepted parameter draws, sorted by information. Point size is proportional to the square root of the rater's number of ratings."
- **Note (`34c34fb4`):** "Average information per rating as a figure, with the same 95% intervals."
- **What is plotted (from code):** one row per rater sorted by `info_weighted_area`, grey horizontal line from `info_ci_low` to `info_ci_high`, green point at the estimate sized 10 + 120·√(n_ratings/max n_ratings), x label "Information per rating". The values are those of F2.5.

**F2.7 Category response functions**
- **Linked object:** `fig-grm-category-response-functions` (N2, `6ad574ba`; "<Figure size 3300x2700 with 1 Axes>"). Figure only. Note `2cd95b60`: "**Category response functions.** The probability of each rating category as a function of θ, one panel per rater."

**F2.8 M1 rater severity (NEW figure)**
- **Finding:** M1 severities (as printed in `tbl-rater-overview`, 2 decimals) range from -0.88 (R24) to 1.37 (R06); 13 raters have negative and 11 positive severity.
- **Linked object:** **`fig-m1-rater-severity` (N2, `b55889a1`, NEW)**. Figure only; the severity values are printed only in `tbl-rater-overview` (F2.9). Severity SEs are not printed anywhere (only drawn as bars).
- **Caption (verbatim):** "Left: rater severity in M1 (rating-scale MFRM) with 95% intervals (estimate ± 1.96 SE); 0 = average rater, higher = stricter. Right: the rater's raw mean rating (1–7). Raters sorted by severity."
- **Note (`51af707f`, verbatim):** "**Rater severity under M1.** The rating-scale MFRM summarises each rater in one severity parameter (0 = average rater; higher = stricter), shown with 95% intervals next to the rater's raw mean rating."
- **What is plotted (from code):** two panels with shared y (raters sorted by severity estimate, `rater_parameters_by_model.csv`, model M1_RSM, parameter b_rater). Left: point at the estimate, grey bar ±1.96·SE, vertical line at 0, x label "Severity (logits): lenient ← 0 → strict"; points coloured red if estimate > 0, blue otherwise. Right: horizontal bars of the raw mean rating (`design_summary_raters.csv`), x axis 1–7, same colours. The caption does not mention the colours.
- **Severity values (every rater, from `tbl-rater-overview`, ascending):** R24 -0.88; R18 -0.79; R19 -0.76; R13 -0.68; R09 -0.58; R23 -0.57; R15 -0.46; R12 -0.40; R10 -0.22; R16 -0.20; R25 -0.19; R08 -0.14; R02 -0.07; R03 0.01; R26 0.13; R04 0.15; R05 0.17; R07 0.52; R11 0.57; R17 0.68; R27 0.75; R01 0.75; R14 0.84; R06 1.37.
- **Caveats:** The severity range (1.37 − (−0.88) = 2.25) is my subtraction; the notebook does not print it. Severity is printed at 2 decimals only.

**F2.9 Rater overview (NEW table)**
- **Linked object:** **`tbl-rater-overview` (N2, `55fbc1ec`, NEW)**. Headers: Rater | Ratings | Mean rating | Severity (M1) | a (GRM) | Share of panel information [95% interval] | Infit / outfit (GRM) | Unused categories.
- **Caption (verbatim):** "Rater overview sorted by severity: number of ratings, raw mean rating, severity in M1 (rating-scale MFRM), discrimination a in the GRM, share of the full-panel information with 95% interval, GRM infit and outfit mean squares (⚑ = flagged), and categories never used."
- **Note (`ea0a0f8c`, verbatim):** "**Rater overview.** One row per rater: number of ratings, raw mean, M1 severity, GRM discrimination, share of the full-panel information with 95% interval, GRM infit and outfit (⚑ = flagged in the rater-fit output), and categories never used. Sorted by M1 severity."
- **Numbers (every row, exactly as printed):**

  | Rater | Ratings | Mean rating | Severity (M1) | a (GRM) | Share of panel information [95% interval] | Infit / outfit (GRM) | Unused categories |
  |---|---|---|---|---|---|---|---|
  | R24 | 190 | 3.75 | -0.88 | 2.89 | 6.8% [4.0, 9.7] | 0.67 / 0.69 ⚑ | – |
  | R18 | 55 | 3.84 | -0.79 | 0.66 | 0.4% [0.0, 1.1] | 0.98 / 0.97 | 7 |
  | R19 | 50 | 3.68 | -0.76 | 2.70 | 6.0% [0.8, 14.1] | 0.53 / 0.51 ⚑ | – |
  | R13 | 254 | 3.68 | -0.68 | 1.54 | 2.0% [1.1, 3.3] | 0.84 / 0.84 | – |
  | R09 | 400 | 3.64 | -0.58 | 0.93 | 0.8% [0.4, 1.5] | 0.87 / 0.87 | – |
  | R23 | 589 | 3.47 | -0.57 | 1.75 | 2.7% [1.8, 3.6] | 0.86 / 0.85 | – |
  | R15 | 73 | 3.47 | -0.46 | 2.76 | 5.9% [2.4, 10.5] | 0.77 / 0.68 ⚑ | – |
  | R12 | 264 | 3.36 | -0.40 | 2.72 | 5.6% [2.8, 8.8] | 0.55 / 0.54 ⚑ | – |
  | R10 | 383 | 3.00 | -0.22 | 2.37 | 4.4% [2.6, 6.6] | 0.62 / 0.60 ⚑ | – |
  | R16 | 268 | 3.09 | -0.20 | 2.47 | 4.9% [3.3, 7.1] | 0.80 / 0.79 | – |
  | R25 | 138 | 3.03 | -0.19 | 3.01 | 6.9% [3.6, 10.1] | 0.72 / 0.71 | 7 |
  | R08 | 522 | 3.00 | -0.14 | 2.13 | 3.9% [2.3, 5.7] | 0.59 / 0.58 ⚑ | – |
  | R02 | 873 | 3.03 | -0.07 | 2.71 | 5.8% [3.1, 8.8] | 0.43 / 0.40 ⚑ | – |
  | R03 | 720 | 2.75 | 0.01 | 1.83 | 2.9% [1.8, 3.9] | 0.75 / 0.76 | 7 |
  | R26 | 46 | 3.00 | 0.13 | 3.19 | 7.4% [0.3, 17.8] | 0.45 / 0.45 ⚑ | 7 |
  | R04 | 620 | 2.82 | 0.15 | 1.93 | 3.1% [1.9, 4.4] | 0.63 / 0.59 ⚑ | – |
  | R05 | 633 | 2.72 | 0.17 | 2.36 | 4.5% [2.9, 5.9] | 0.62 / 0.62 ⚑ | – |
  | R07 | 547 | 2.40 | 0.52 | 2.01 | 3.1% [2.2, 4.2] | 0.78 / 0.69 ⚑ | – |
  | R11 | 369 | 2.33 | 0.57 | 1.86 | 2.7% [1.7, 3.8] | 0.87 / 0.85 | – |
  | R17 | 52 | 2.08 | 0.68 | 1.81 | 2.4% [0.6, 5.2] | 0.92 / 0.90 | 6,7 |
  | R27 | 47 | 2.06 | 0.75 | 3.04 | 5.9% [1.4, 11.5] | 0.64 / 0.65 ⚑ | 5,7 |
  | R01 | 1174 | 2.16 | 0.75 | 1.82 | 2.5% [1.9, 3.1] | 0.72 / 0.69 ⚑ | 7 |
  | R14 | 259 | 2.22 | 0.84 | 2.54 | 4.4% [1.6, 7.7] | 0.54 / 0.46 ⚑ | – |
  | R06 | 520 | 1.76 | 1.37 | 3.10 | 5.0% [2.7, 7.2] | 0.59 / 0.44 ⚑ | – |

- **Direction (read off):** 15 raters carry ⚑ (R24, R19, R15, R12, R10, R08, R02, R26, R04, R05, R07, R27, R01, R14, R06); 9 do not (R18, R13, R09, R23, R16, R25, R03, R11, R17). Severity order does not follow the mean-rating order exactly (e.g. R18 has the highest mean 3.84 but the second-lowest severity -0.79; R24 has mean 3.75 and the lowest severity -0.88; R01 and R27 both print 0.75).
- **Caveats:** The flag rule is not stated in the notebook ("flagged in the rater-fit output"); `tbl-grm-rater-fit` shows no flag column and the rater-fit note says "No misfit cut-offs for infit and outfit are applied in this notebook" (see Flag 3). Unused categories are comma-joined ("6,7") here and semicolon-joined in `tbl-category-usage`. "Ratings" has no thousands separator (1174). Share interval bounds carry no % sign.

## (e) Model dependence of scores

**F2.10 Correlations of EAP scores between models**
- **Finding:** All between-model correlations are 0.977 or higher; GRM–M3 is 0.996 on both coefficients, GRM–M1 is lowest (Pearson 0.977, Spearman 0.979).
- **Linked object:** `tbl-theta-correlations` (N2, `06919dea`). Headers: Method | Model | M1 (rating-scale MFRM) | M2 (partial-credit MFRM) | M3 (GPCM) | GRM | M1, sirt default grid.
- **Numbers:** Pearson: M1–M2 0.993; M1–M3 0.981; M1–GRM 0.977; M2–M3 0.989; M2–GRM 0.985; M3–GRM 0.996. Spearman: M1–M2 0.996; M1–M3 0.984; M1–GRM 0.979; M2–M3 0.988; M2–GRM 0.984; M3–GRM 0.996. "M1, sirt default grid" vs M1: 1.000 (both). Diagonal 1.000.
- **Notebook statement (`6f8cf70e`):** "**Agreement of scores.** Correlations of the product scores between models. High values mean the ranking of products hardly depends on the model."

**F2.11 Ranking change relative to the GRM**
- **Finding:** Relative to the GRM, 0.206 of products change quintile under M1, 0.155 under M2 and 0.081 under M3.
- **Linked object:** `tbl-score-agreement` (N2, `2071b243`).
- **Numbers:**

  | Model | Pearson r | Spearman ρ | Mean percentile shift | 95th percentile of shift | Maximum shift | Share changing quintile | Share changing ≥ 2 quintiles |
  |---|---|---|---|---|---|---|---|
  | M1 (rating-scale MFRM) | 0.977 | 0.979 | 0.042 | 0.126 | 0.433 | 0.206 | 0.003 |
  | M2 (partial-credit MFRM) | 0.985 | 0.984 | 0.032 | 0.112 | 0.411 | 0.155 | 0.002 |
  | M3 (GPCM) | 0.996 | 0.996 | 0.016 | 0.046 | 0.232 | 0.081 | 0.000 |

- **Caption:** "Change of the product ranking relative to the GRM: correlations, absolute shift in percentile rank (0-1 scale) and share of products whose quintile changes."
- **Notebook statement (`cfacd46d`, verbatim):** "**Change in product ranking.** How far products move in the ranking when another model replaces the GRM: the mean and 95th-percentile shift in percentile rank, and the share of products that change quintile."
- **Caveat:** M3's "Share changing ≥ 2 quintiles" prints 0.000 (3-decimal display).

## (f) Sensitivity

**F2.12 Sensitivity to the rater exclusion**
- **Finding:** Refitting the GRM with all 28 raters changes the empirical reliability from 0.68896 to 0.68837 and the model-based reliability from 0.96893 to 0.97142; θ̂ from the two fits correlates at 0.99994 (Pearson and Spearman).
- **Linked object:** `tbl-sensitivity-rater-exclusion` (N2, `d89f7935`), 5 decimals. Headers: Quantity | Final data | All raters | Note.
- **Numbers (every row):** n raters 24 vs 28; n ratings 9,046 vs 9,077; n products 3,669 vs 3,670; excluded raters – vs R20;R21;R22;R28; empirical marginal reliability 0.68896 vs 0.68837 (Note "Var(theta)/(Var(theta)+mean(PSD^2))"); model based marginal reliability 0.96893 vs 0.97142 (Note "mirt::marginal rxx (hypothetical full panel)"); theta pearson common products 0.99994; theta spearman common products 0.99994; theta mean abs diff 0.00204; theta max abs diff 0.35026; share products changing quintile 0.00273 (these five with Note "all-raters vs final GRM, 3,669 common products"); a max abs diff common raters 0.19349; a pearson common raters 0.99802 (Note "all-raters vs final GRM, 24 common raters").
- **Notebook note (`be69f6b6`, verbatim):** "**Sensitivity to the rater exclusion.** The GRM refitted on all raters, including the three with fewer than 15 ratings, compared with the final GRM: reliability, agreement of the product scores, and the discriminations of the common raters." — **stale: four raters are excluded (see Flag 2).**
- **Caveats:** No CIs for the differences. "marginal rxx" is a display artefact of `readable_text` (underscore → space).

## (g) Raw mean vs model-based scores

**F2.13 Raw mean rating vs GRM score**
- **Finding:** Within the groups of products with 1, 2 and 3+ ratings, Kendall's τ-b between raw mean and GRM score is 0.833, 0.818 and 0.849; 0.041, 0.066 and 0.071 of pairs with different raw means are ordered the other way by the GRM; the maximum θ̂ range among products with equal raw means is 2.170 (2-rating group).
- **Linked object:** `tbl-raw-mean-vs-grm` (N2, `81a153de`).
- **Numbers:**

  | Ratings per product | Products | Kendall's τ-b | Share of pairs in reversed order | Mean θ̂ range at equal raw mean | Maximum θ̂ range at equal raw mean |
  |---|---|---|---|---|---|
  | 1 | 832 | 0.833 | 0.041 | 1.229 | 1.430 |
  | 2 | 2,107 | 0.818 | 0.066 | 1.531 | 2.170 |
  | 3+ | 730 | 0.849 | 0.071 | 0.537 | 1.317 |

- **Notebook explanation (`082bc140`, verbatim):** "**Raw mean versus GRM score.** Common practice scores a product by the unweighted mean of its ratings, which treats all raters as interchangeable. The table compares this raw mean with the GRM score, separately for products with 1, 2 and 3 or more ratings. The raw mean is tied for almost all products (with one rating it takes only 7 values), so agreement is given as Kendall's τ-b and as the share of product pairs with different raw means that the GRM orders the other way round. The last two columns show how far apart the GRM scores of products with the same raw mean lie: products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination."
- **Direction (read off):** τ-b: 3+ (0.849) > 1 (0.833) > 2 (0.818). Reversed share: 1 (0.041) < 2 (0.066) < 3+ (0.071). Mean θ̂ range: 2 (1.531) > 1 (1.229) > 3+ (0.537). Max θ̂ range: 2 (2.170) > 1 (1.430) > 3+ (1.317). Products sum to 3669 (my sum; no pooled row).
- **Caveats:** No CIs; the tied share and group sizes are not printed. The mechanism clause ("when they were rated by raters of different severity or discrimination") is the notebook's framing, not a tested result.

**F2.14 Figure: GRM score against raw mean**
- **Linked object:** `fig-raw-mean-vs-theta` (N2, `a45de2f9`). Figure only. Note `be95800a`: "The same comparison as a figure. Each point is a product; the vertical spread at a given raw mean shows the products whose GRM scores differ although their raw means are equal."

---

## Not found

Absent from the notebooks; do not invent downstream.
- **Data fingerprint** md5 68037eafc9939992751c2bf646c48a9e (explicitly dropped from `tbl-design-summary`).
- **CIs/SEs:** for rel_post by number of ratings; for the sensitivity differences; for the raw-mean vs GRM measures; for M1 severity (only drawn in `fig-m1-rater-severity`, never printed); for M1/M2 thresholds; for the M1–M3 marginal/empirical reliabilities.
- **Severity summary:** the severity range, the SEs, and any test of rater severity differences; severity at more than 2 decimals.
- **Discrimination summary:** ratio of max to min discrimination (the report's `discrimination_summary.csv` is not displayed in any notebook); the median a drawn in `fig-grm-rater-discrimination-ci`.
- **Fit flags:** the rule behind ⚑ in `tbl-rater-overview` (no cut-off is stated; `tbl-grm-rater-fit` has no flag column).
- **Global fit:** anything other than the non-computable C2.
- **Q3:** the number of non-computable pairs; the full list of the 28 flagged pairs.
- **LR df:** the count of unused end categories as a printed figure (see Flag 4).
- **Exact p values** for the LR tests (printed only as "< .001").
- **Thresholds for the projection:** the first k reaching .70/.80/.90 (derivable from the table but not printed); k > 10; parameter uncertainty in the projection band; most/least-informative or workload-weighted rater sets; true-score correlation (`true_r2`).
- **Min-4 simulation:** seed; whether a rater may rate the same product twice; how the added ratings' θ is generated; per-k breakdown; any design other than "at least 4".
- **Observed vs simulated:** differences, tests or a statement on which quantity is larger.
- **Figures:** numeric values behind `fig-grm-panel-information`, `fig-grm-rel-post-by-theta`, `fig-grm-category-response-functions`, `fig-raw-mean-vs-theta`, `fig-category-usage-shares` (shares), `fig-grm-rater-discrimination-ci` (median), `fig-m1-rater-severity` (SEs).
- **Crossed-block raters:** which 3 raters form the fully crossed block; the removal rule for the 6 raters dropped from the pairwise α.
- **Study context:** data-collection timespan (timestamps in N0 head show 2026-10-23 for a few rows only), rater demographics and expertise.
- **Tests:** trend tests across n; ICCs; an M0 vs M1 severity test; a within-package M1 vs M2 test; held-out checks; rejected-draw diagnostics.

## NOT IN NOTEBOOK — not quotable

- md5 68037eafc9939992751c2bf646c48a9e (orchestrator context only).
- "Infit or outfit outside 0.7–1.3" as the fit-flag rule (report qmd caption of `tbl-raters`; AUDIT/REPORT files).
- "x-fold" discrimination ratio (`disc['ratio_max_min']` in the report qmd).
- "passes .80 at 4 ratings" (report qmd `k80`; derived, not printed).
- Severity range "2.25 logits" (my subtraction; report qmd `sev_range`).
- Report qmd statements such as "regardless of how many ratings each rater gave in reality" and "The simulated curve therefore does not use our distribution of ratings per action" — the notebook says only "drawn at random (each equally likely / equal probability)".
- Model labels "M1 (RS-MFRM)", "M2 (PC-MFRM)" (report qmd); the notebooks print "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)".
- Report-qmd roundings: ΔBIC "4.2", χ² "840.45"/"156.59", θ correlation "0.9999", reliabilities ".688"/".689" at 3 decimals from the 5-decimal sensitivity table, percentages "10%" (matrix fill), "15.5%"/"20.6%" (quintile shares), "6.8%" (shares are printed as 0.068 in `tbl-grm-information-summary`; the % form exists only in `tbl-rater-overview`).
- Any value from `01_data_overview_new_ratings.ipynb`, `data/archive_pre_rerun_20261103/`, R scripts, AUDIT.md, REPORT.md.
- Previous findings values (7,820 / 3,668 / 19 raters; 0.672; 0.960; etc.).

## Flags

1. **BIC verdict changed.** `tbl-model-fit` now shows M1 best on BIC (ΔBIC 0.000) with the GRM at 4.161; the GRM remains best on AIC and SABIC. Any draft text saying the GRM is best on all three criteria is stale.
2. **Stale note in N2 `be69f6b6`:** "including the three with fewer than 15 ratings" — four raters (R20, R21, R22, R28) are excluded in this run (`tbl-excluded-raters`, `tbl-design-summary`, `tbl-sensitivity-rater-exclusion`). Quote the tables, not the note's "three".
3. **Fit flags vs "no cut-offs".** `tbl-rater-overview` marks 15 raters with ⚑ ("flagged in the rater-fit output"), while the rater-fit note `f526bd7f` says "No misfit cut-offs for infit and outfit are applied in this notebook" and `tbl-grm-rater-fit` prints no flag column. The flag rule is not stated anywhere in the notebooks; do not quote 0.7–1.3.
4. **LR df vs category-usage table.** 115 − 105 = 10 (my subtraction). The note `a5216280` attributes the reduction to "the number of unused end categories". Counting from `tbl-category-usage`, unused end categories number 9 (R01, R03, R06, R18, R25, R26, R27: category 7 each; R17: 6 and 7) and R27's internal gap (category 5) adds one more unused category, giving 10 unused categories in total. `tbl-threshold-order` prints Steps 4 for R27 (two fewer than 6). The note's wording ("end category") does not cover R27's internal gap; the writer should not state "10 unused end categories".
5. **R27 internal gap.** `tbl-category-usage` Internal gap True for R27 (category 5 unused, 6 used once). The rater-parameters note says such a rater's thresholds "are not directly comparable with those of the other raters", but `tbl-grm-rater-parameters` and `tbl-rater-overview` do not mark R27. The design summary says "raters with internal gap 1".
6. **Non-monotonic reliability rows.** `tbl-grm-reliability-by-n`: k = 10 (14 products) has mean rel_post 0.897 < 0.915 at k = 9, and k = 13 (1 product) 0.947 < 0.948 at k = 12. These rows also appear in `tbl-grm-reliability-observed-vs-simulated` and as faded/small dots in the new figure.
7. **Observed vs simulated are different quantities.** The note `7561808c` defines observed as mean rel_post and simulated as empirical marginal reliability; the table and figure juxtapose them. Any statement that observed values "fall below" the simulation (true for k = 3–7, 9, 10 by the printed numbers) is a reader's comparison; the notebook makes none.
8. **Min-4 check row vs observed.** Simulated "Actual design" 0.686 [0.675, 0.695] vs observed empirical 0.689 [0.669, 0.703]; the notebook calls the row "a check" but prints no comparison.
9. **Simulation assumptions stated vs unstated.** Stated: raters drawn at random, each equally likely / equal probability; ratings generated from the fitted GRM and scored with its parameters treated as known; θ ~ N(0, 1) (projection only); 50 replications; 2000 products per k (projection); seed 20260713 (projection only). Not stated: workload weighting (only implied by "equally likely"), sampling with/without replacement, min-4 seed, how θ enters the min-4 top-up. The writer must not state the unstated assumptions as notebook facts.
10. **In-figure numbers in `fig-grm-reliability-observed-vs-simulated`:** ".835" and ".969" and "24 raters" are baked into the image as text (via `r3()`, no leading zero). Quote them from `tbl-grm-reliability-min-ratings`, `tbl-grm-reliability-ci`/`tbl-reliability-overview` and `tbl-design-summary` in the tables' "0.835"/"0.969" form.
11. **Display inconsistencies (quote as printed):** separators in N2 numeric cells (9,046) but not in N0/N1, N2 stdout, or `tbl-rater-overview` "Ratings" (1174); `tbl-rater-overview` 2 decimals vs 3 elsewhere (R09 mean 3.64 vs 3.643; share 6.8% vs 0.068; a 2.89 both); information 2 decimals in `tbl-grm-rater-information-ci` vs 3 in `tbl-grm-information-summary`; list separators "6,7" (overview) vs "6;7" (category usage); "mirt::marginal rxx" (sensitivity, overview) vs "marginal_rxx (mirt)" header (marginal-reliability table); N1 `ovtbl02` prints "3.000"/"0.000" where `fb6df84b` prints "3.000"/"0.000" too but R09 3.642 vs 3.643; `ovtbl01` "318.500".
12. **Markdown order mismatches in N2:** `c8ad3efc` ("Full panel") precedes the information-CI block and `fig-grm-panel-information` (`715f5154`) follows `fig-grm-rater-information-ci`; `a30edc1b` ("Reliability by number of ratings") precedes the reliability-CI note and table rather than `tbl-grm-reliability-by-n`; `9e0c8a51` (M3 discriminations) sits before `tbl-score-agreement`, far from `tbl-discrimination-m3` (`a5fa5502`).
13. **Stale references in N0 intro** (`64b27fc9`, `73ef4dcd`): deleted notebooks `02a`–`02d`, `03`, `02_creativity_ratings_R.qmd`. N1 intro mentions `../AUDIT.md` and `../R/01_data_design.R` (context, not results).
14. **Privacy:** N0 `520638b8` prints the full Google Sheets URL; N0/N1 print absolute local paths and action UUIDs; no original rater IDs are printed.
15. **Terminology:** N0 says "actions"; N1 label `tbl-overview-ratings-per-action` keeps "action" while its rows say "n_products"; N2 intro: "The rated products are the football actions".
16. **Unlabelled but cited sources** (quotable, not embeddable): N1 `3b12b8bf`, `aa371443`, `31873726`, `981d6824`, `bacf60d8`, `f6039400`; N2 `ccbeaf11` (mean Q3), `64142953` (projection settings); N0 stdout cells.
17. **Coinciding printed values:** "empirical marginal reliability (primary; actual scores)", "var theta eap" and "rel post mean" all print 0.689; M1 and M2 marginal reliability both print 0.957; M3 ΔAIC = ΔSABIC = 49.381 (M3 and GRM have the same parameter count, 158).
18. **Mechanism/framing sentences in N2 markdown** (mark for author confirmation if used): `082bc140` (same raw mean, different GRM scores "when they were rated by raters of different severity or discrimination"); `9e0c8a51` ("how far the equal-discrimination assumption of M1 and M2 is from the data"); `6f8cf70e` ("the ranking of products hardly depends on the model"); `77937868` ("A model-based gauge of the value of adding ratings"); `83614bc3` ("Precision depends on where a product lies relative to its raters' thresholds"); N1 `f3482d97` ("anticipate what the models estimate formally").
19. **`02_artifacts.md` is current** (same ids, 52 labels); nothing to resolve there.

## Coverage check: reports/jrt_results_summary.qmd

Read only as a checklist (the report is not a quotable source). For each result it shows: the notebook cell/label that provides it, or NOT AVAILABLE.

| Report item | Notebook source |
|---|---|
| Data version fingerprint | NOT AVAILABLE (dropped from `tbl-design-summary`) |
| "by BIC the simplest model wins narrowly over the GRM" (best_bic = M1) | `tbl-model-fit` (M1 ΔBIC 0.000; GRM 4.161) |
| Krippendorff's α .391 | `tbl-naive-indices`, `tbl-reliability-overview` |
| GRM empirical reliability .689 | `tbl-grm-reliability-ci`, `tbl-grm-reliability-summary`, `tbl-reliability-overview` |
| Projection k = 1 .530, k = 2 .705 | `tbl-grm-reliability-projection` |
| "passes .80 at 4 ratings" (k80) | derivable from `tbl-grm-reliability-projection` (k = 4: 0.834) but NOT printed; do not state as a notebook result |
| Min-4 .835 | `tbl-grm-reliability-min-ratings`, `tbl-reliability-overview` |
| r = .977 to .996 with the GRM (M1, GPCM) | `tbl-score-agreement` / `tbl-theta-correlations` |
| Design snapshot (ratings, actions, raters, excluded, ratings per rater 46–1,174, mean/median/range 2.47/2/1–13, 832 single-rated, 30 of 276 pairs, scale 1-7, 7 categories) | `tbl-design-summary` (mean prints 2.466), `tbl-excluded-raters` |
| "10% of the matrix is filled" | `tbl-design-summary` matrix fill 0.103 (percent form not printed) |
| fig-design (actions by ratings received) | `fig-design-ratings-per-product`; counts in N1 `3b12b8bf` |
| tbl-fit (Δ at 1 decimal; "Assumes" text) | `tbl-model-fit` (3 decimals); the "Assumes" descriptions are NOT in the notebook (model descriptions in `89bc0612` are the closest) |
| tbl-lr (χ² at 2 decimals, df, p) | `tbl-lr-tests` (χ² 840.447 / 156.593; df 105 / 23; p < .001) |
| ΔBIC for the GRM = 4.2 | `tbl-model-fit` 4.161 |
| "most discriminating rater's value is x times the least" (ratio_max_min) | NOT AVAILABLE (no notebook cell shows `discrimination_summary.csv`; `tbl-discrimination-m3` gives 2.221 and 0.305 but no ratio) |
| fig-disc | `fig-grm-rater-discrimination-ci` |
| tbl-agree (r, ρ, shift in pct points, quintile %) | `tbl-score-agreement` (proportions, 3 decimals) |
| Kendall τ-b per group (.833, .818, .849) | `tbl-raw-mean-vs-grm` |
| "same raw mean can differ by up to 2.17 SD" | `tbl-raw-mean-vs-grm` maximum θ̂ range 2.170 (2-rating row) |
| GRM converged, 436 iterations | `tbl-grm-convergence` |
| C2 not computable, 30 of 276 | `tbl-grm-global-fit` |
| Sensitivity: θ correlation 0.9999; reliability .688 vs .689 | `tbl-sensitivity-rater-exclusion` (0.99994; 0.68837 vs 0.68896, 5 decimals) |
| "4 excluded low-volume raters" | `tbl-excluded-raters` |
| tbl-rel (Krippendorff, Cronbach crossed block .750, GRM actual .689, min-4 .835 with range and counts, full panel .969, median rel_post .712) | `tbl-reliability-overview` (all rows incl. the min-4 row); `tbl-naive-indices` |
| "Answers" column text | NOT in notebook (the "Refers to" column of `tbl-reliability-overview` is the closest) |
| "The same simulation run on the actual design gives .686, close to the observed .689" | `tbl-grm-reliability-min-ratings` (0.686) and `tbl-grm-reliability-ci` (0.689); the word "close" is the report's |
| fig-reln (dots, line/band, .70/.80 guides, min-4 and full-panel dashed lines) | `fig-grm-reliability-observed-vs-simulated` |
| fig-reln caption assumptions ("regardless of how many ratings each rater gave in reality"; "does not use our distribution of ratings per action") | NOT verbatim in the notebook; notebook says "drawn at random from the panel with equal probability" (`fig-grm-reliability-observed-vs-simulated` caption, `tbl-grm-reliability-projection` caption, notes `77937868`, `c7486592`) |
| tbl-reln (observed vs simulated per k) | `tbl-grm-reliability-observed-vs-simulated` |
| fig-sev (severity with 95% intervals, raw mean) | `fig-m1-rater-severity` |
| Severity range "2.25 logits"; most lenient R24 (mean 3.75) to strictest R06 (mean 1.76) | severities and means in `tbl-rater-overview` (R24 -0.88, 3.75; R06 1.37, 1.76); the range is NOT printed |
| fig-scale (share of scale points per rater) | `fig-category-usage-shares` |
| "8 of 24 raters never used at least one scale point; in every case this included the top category (7)" | `tbl-design-summary` (raters with category gaps 8); `tbl-category-usage` (all 8 Missing-categories entries include 7); the sentence itself is NOT printed |
| Floor use: R06 gave a "1" in 58% of ratings | `tbl-overview-rater-response-styles` Share lowest (1) 0.579 |
| fig-info | `fig-grm-rater-information-ci` |
| Information per rating from 0.13 (R18) to 2.52 (R26) | `tbl-grm-rater-information-ci` (2 decimals) / `tbl-grm-information-summary` (0.135, 2.517) |
| "one rating by the top rater carries as much as several ratings by the least informative one" | NOT printed (interpretive) |
| tbl-raters (rater summary with "Fit flag: GRM infit or outfit outside 0.7–1.3") | `tbl-rater-overview` provides the table; the 0.7–1.3 rule is NOT in the notebook |
| "Infit/outfit values below 1 mostly reflect the design" | note `f526bd7f` ("values below 1 are expected, because the score is estimated from the very ratings being checked") |
| RQ1: .522 with 1 rating, .699 with 2; passes .80 from about 4 | `tbl-grm-reliability-by-n` (0.522, 0.699); "4" derived from the projection, NOT printed |
| RQ2: strictness range, 8 unused, "x-fold" discrimination | severities `tbl-rater-overview`; gaps `tbl-design-summary`; ratio NOT AVAILABLE |
| RQ3a: χ²(105) = 840.45, χ²(23) = 156.59, p < .001; BIC prefers M1 | `tbl-lr-tests` (840.447, 156.593), `tbl-model-fit` |
| RQ3b: 15.5%–20.6% change quintile (M2, max = M1); τ-b .818–.849 | `tbl-score-agreement` (0.155, 0.206); `tbl-raw-mean-vs-grm` |
| Model labels "M1 (RS-MFRM)" / "M2 (PC-MFRM)" | NOT in notebook; use "M1 (rating-scale MFRM)" / "M2 (partial-credit MFRM)" |

---

Files read:
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/02_jrt_results.ipynb` (all 29 stored Markdown table outputs, all markdown cells, the two stdout cells; long notes verified sentence-by-sentence against the generator)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/build_02_jrt_results.py` (generator of N2; used only to recover the full text of markdown cells and the caption of `fig-grm-reliability-observed-vs-simulated` that the grep tool truncated; every quoted sentence was confirmed present in the notebook JSON)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb` (cells, stdout, raw Markdown of `ovtbl01` and `ovtbl02`)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb` (cells, stdout, raw Markdown of `tbl-cleaning-log`)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/02_artifacts.md` (labels and cell ids)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/manuscript/03_findings.md` (previous version, format reference only)
- `/home/max/drive/projects/3_Creativity/11-paper-CAT-methodology/data-analysis/creativity-ratings-psychometrics/reports/jrt_results_summary.qmd` (coverage checklist only)


---

## Delta 2026-11-09 (commit 164c146): new label and newly printed values

N2 was regenerated after this findings file was written. All N2 cell ids changed again (see item 6). Everything below was read from the stored notebook outputs; nothing else in this file changes except the supersessions listed in item 5.

### 1. F1.4a `tbl-discrimination-summary` (NEW table) — spread of the M3 discriminations
- **Finding:** The 24 M3 (GPCM) discriminations have a minimum of 0.305, a median of 1.240, a maximum of 2.221, a max/min ratio of 7.277 and an SD of 0.550.
- **Linked object:** **`tbl-discrimination-summary` (N2, `5ef7276b`, NEW; execution_count 43)**. It directly follows `tbl-discrimination-m3` (`67fca3da`); there is no markdown note cell between the two tables and no dedicated note for the new table. The only M3-discrimination note remains `82319128` (old `9e0c8a51`): "Rater discriminations in M3. Their spread shows how far the equal-discrimination assumption of M1 and M2 is from the data." (still placed before `tbl-score-agreement`, see Flag 12).
- **Caption (verbatim):** "Spread of the rater discriminations in M3 (GPCM): minimum, quartiles, median, maximum, ratio of the largest to the smallest discrimination, and standard deviation across raters."
- **Headers:** Statistic | Value. Source: `show_table("comparison/discrimination_summary.csv")` (no column selection; the whole CSV is displayed).
- **Numbers (every row, exactly as printed; 3 decimals):**

  | Statistic | Value |
  |---|---|
  | min | 0.305 |
  | q1 | 0.915 |
  | median | 1.240 |
  | q3 | 1.659 |
  | max | 2.221 |
  | ratio max min | 7.277 |
  | sd | 0.550 |

- **Consistency (read off):** min 0.305 = R18 and max 2.221 = R27 in `tbl-discrimination-m3` (F1.4). The rater ids are not printed in the summary table; the median/quartile values are not attributable to a rater (24 values, so the median is not a single rater's estimate). No SEs, no CI, no N column.
- **Caveats:** Row labels are code-style lower-case ("q1", "q3", "ratio max min", "sd"; underscore of `ratio_max_min` turned into spaces by `readable_text`). "ratio max min" = 7.277 is the printed figure; do not round to "7-fold"/"7.3-fold" unless marked as a rounding.

### 2. F1.20a Smallest k with simulated empirical reliability ≥ .80 (NEW printed line)
- **Finding:** The notebook now prints that the smallest k at which the projected empirical reliability reaches at least .80 is k = 4.
- **Source:** unlabelled stdout cell N2 `c7a7fe2a` (old `64142953`; execution_count 29), the projection-settings cell. Not embeddable; quotable as stdout.
- **Printed lines (verbatim, both lines of the cell):**
  - "50 replications of 2000 simulated products per k; seed 20260713."
  - "Smallest k with simulated empirical reliability of at least .80: 4."
- **Numbers:** k = 4. The reliability value at k = 4 is not repeated in this line; it is 0.834 [0.827, 0.841] in `tbl-grm-reliability-projection` (`4021099f`, F1.20).
- **Caveats:** The line refers to the projection (random raters, θ ~ N(0, 1)), not to the observed `tbl-grm-reliability-by-n` (where k = 4 prints 0.814) and not to the min-4 top-up (0.835). Thresholds .70 and .90 are still not printed (first k ≥ .70 = 2 and ≥ .90 = 7 remain my readings of the table). The code (build script line 359) would print "none up to k = 10" if no k qualified; the printed result is "4".

### 3. F2.8a M1 severity range (NEW printed line)
- **Finding:** Under M1 the most lenient rater is R24 with severity -0.878 (SE 0.066) and the strictest is R06 with 1.369 (SE 0.057), a span of 2.247 logits.
- **Source:** unlabelled stdout cell N2 `411ec44f` (NEW; execution_count 47), directly after `fig-m1-rater-severity` (`470979b6`). Not embeddable; quotable as stdout.
- **Printed line (verbatim):** "M1 severity ranges from -0.878 (SE 0.066, R24) to 1.369 (SE 0.057, R06): a span of 2.247 logits."
- **Numbers:** R24 -0.878 (SE 0.066); R06 1.369 (SE 0.057); span 2.247 logits. 3 decimals.
- **Consistency (read off):** `tbl-rater-overview` prints the same two raters at 2 decimals (-0.88, 1.37). The span 2.247 is printed by the notebook (computed in the cell as max − min); the earlier "2.25 (my subtraction)" in F2.8 is superseded by the printed 2.247.
- **Caveats:** Only the two extreme raters' SEs are printed; the SEs of the other 22 raters remain unprinted (drawn as bars in `fig-m1-rater-severity` only). No test of severity differences. Severities of the other raters are still only available at 2 decimals (`tbl-rater-overview`).

### 4. Note fixes (verbatim text of the changed notebook notes and captions)

**4a. Sensitivity note — `91ed9596`→ correct id `91ed9594` (old `be69f6b6`), verbatim:**
"**Sensitivity to the rater exclusion.** The GRM refitted on all raters, including those with fewer than 15 ratings, compared with the final GRM: reliability, agreement of the product scores, and the discriminations of the common raters."
- The stale "three" is gone. The note now says "those", not "four"; the number four is printed only in the tables (`tbl-excluded-raters` `f04b368b`: R20, R21, R22, R28; `tbl-sensitivity-rater-exclusion` `adbcdb13`: n raters 24 vs 28). Caption of `tbl-sensitivity-rater-exclusion` unchanged: "Sensitivity of the GRM results to excluding raters with fewer than 15 ratings: final data versus all raters."

**4b. LR-test note — `f43c6651` (old `a5216280`), verbatim (three sentences, contiguity verified):**
"**Likelihood-ratio tests.** Each test checks whether the next step up the ladder improves fit: rater-specific thresholds (M1 vs M2), then rater-specific discriminations (M2 vs M3). \"df if all categories used\" is the df if every rater used all 7 categories: (J − 1)(K − 2) for M1 vs M2 and J − 1 for M2 vs M3, with J raters and K categories. A rater who never uses an end category of the scale has one step parameter less in M2 (see the category-use table), so the observed df of M1 vs M2 is smaller by the number of categories raters never used (unused end categories and any internal gap)."
- Changed part: "...smaller by the number of categories raters never used (unused end categories and any internal gap)." (previously "...by the number of unused end categories."). The note does not name R27 and does not print the count (10 = 115 − 105 remains my subtraction; 9 unused end categories + R27's internal gap = 10 remains my count from `tbl-category-usage`).
- **Caption of `tbl-lr-tests` (`fcbab35d`) is UNCHANGED and still says only "end":** "Likelihood-ratio tests within the adjacent-category ladder. 'df if all categories used' gives the df if every rater had used all 7 categories; unused end categories reduce the df of M1 vs M2." Quote the note, not the caption, for the gap rule.

**4c. Rater-fit note — `38b48261` (old `f526bd7f`), verbatim (contiguity of all sentence junctions verified):**
"**Rater fit.** Infit and outfit are mean squares of the standardised residuals, with an expected value of 1 (Wright & Masters, 1982). With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked. S-X² (Orlando & Thissen, 2000; Kang & Chen, 2008) needs complete data, so the missing ratings are imputed 20 times from the fitted model and S-X² is averaged. About 90% of the cells are imputed, which makes the test conservative. The flags in the rater-fit output (flag_infit, flag_outfit; R/02_grm.R) mark values outside 0.7–1.3; with this design they mostly mark values below 0.7, which is expected rather than misfit. No further cut-offs are applied in this notebook."
- Changed part: the last two sentences (previously "No misfit cut-offs for infit and outfit are applied in this notebook."). The phrase "which is expected rather than misfit" is the notebook's framing (mark for author confirmation if used interpretively). `tbl-grm-rater-fit` (`23a684b4`) still prints no flag column; its caption is unchanged ("Rater fit in the graded response model: infit and outfit mean squares (observed ratings) and S-X² pooled over multiple imputations of the missing ratings.").

**4d. `tbl-rater-overview` note and caption now state the ⚑ rule.**
- Note `d321faa3` (old `ea0a0f8c`), verbatim: "**Rater overview.** One row per rater: number of ratings, raw mean, M1 severity, GRM discrimination, share of the full-panel information with 95% interval, GRM infit and outfit (⚑ = infit or outfit outside 0.7–1.3, the flag rule of the rater-fit output), and categories never used. Sorted by M1 severity."
- Caption of `tbl-rater-overview` (`bd1ee008`), verbatim: "Rater overview sorted by severity: number of ratings, raw mean rating, severity in M1 (rating-scale MFRM), discrimination a in the GRM, share of the full-panel information with 95% interval, GRM infit and outfit mean squares (⚑ = infit or outfit outside 0.7–1.3), and categories never used."
- Consistency with the printed values (read off): all 15 ⚑ raters have infit or outfit < 0.7 (none > 1.3); the 9 unflagged raters have both values in 0.7–1.3 (lowest unflagged: R25 0.72 / 0.71; R03 0.75 / 0.76). R24 (0.67 / 0.69) and R15 (0.77 / 0.68) are flagged on one value each. The flag is taken from `flag_infit`/`flag_outfit` in `grm/rater_fit.csv` (code), not recomputed in the notebook.

### 5. Supersessions (what in this file is now resolved; everything else stands)

**"Not found" list — now RESOLVED (delete or amend):**
- "Severity summary: the severity range, the SEs" → range 2.247 logits and the SEs of R24 (0.066) and R06 (0.057) are printed (`411ec44f`, item 3). Still not found: SEs of the other 22 raters; any test of severity differences; severities of other raters at more than 2 decimals.
- "Discrimination summary: ratio of max to min discrimination (the report's `discrimination_summary.csv` is not displayed in any notebook)" → displayed as `tbl-discrimination-summary` (`5ef7276b`), ratio 7.277 (item 1). Still not found: the median a of the GRM drawn in `fig-grm-rater-discrimination-ci` (the new table is M3/GPCM, not GRM).
- "Fit flags: the rule behind ⚑ in `tbl-rater-overview` (no cut-off is stated)" → rule stated in note `d321faa3`, caption of `tbl-rater-overview`, and note `38b48261`: infit or outfit outside 0.7–1.3 (item 4c/4d).
- "Thresholds for the projection: the first k reaching .70/.80/.90" → .80 is printed (k = 4, `c7a7fe2a`, item 2). Still not found: .70 and .90; k > 10; parameter uncertainty in the band; workload-weighted rater sets; `true_r2`.
- "LR df: the count of unused end categories as a printed figure" → still NOT printed; but the attribution now covers internal gaps (item 4b). Keep the entry, amend wording: the note's rule now reads "categories raters never used (unused end categories and any internal gap)".

**"NOT IN NOTEBOOK — not quotable" list — now RESOLVED:**
- "'Infit or outfit outside 0.7–1.3' as the fit-flag rule" → now IN the notebook (`38b48261`, `d321faa3`, `tbl-rater-overview` caption). Quotable.
- "'x-fold' discrimination ratio (`disc['ratio_max_min']`)" → the ratio 7.277 is now printed (`tbl-discrimination-summary`). Quotable as "7.277"; an "x-fold" rounding (e.g. "7-fold") is still a rounding and must be marked as such.
- "'passes .80 at 4 ratings' (report qmd `k80`; derived, not printed)" → now printed: "Smallest k with simulated empirical reliability of at least .80: 4." (`c7a7fe2a`). Quotable for the projection.
- "Severity range '2.25 logits' (my subtraction)" → the notebook prints 2.247 logits (`411ec44f`). "2.25" remains a rounding; quote 2.247.
- All other entries in that list stand (md5; report-qmd wording on rater drawing; "M1 (RS-MFRM)" labels; the report roundings; `01_data_overview_new_ratings.ipynb`; previous values).

**"Flags" list — RESOLVED or amended:**
- Flag 2 (stale "three" in the sensitivity note) → RESOLVED: the note now says "those with fewer than 15 ratings" (`91ed9594`). Note: it does not say "four"; the count four comes from the tables.
- Flag 3 (fit flags vs "no cut-offs") → RESOLVED: the rule 0.7–1.3 is stated in three places; the rater-fit note now says "No further cut-offs are applied". `tbl-grm-rater-fit` still has no flag column (that part stands as a display note, not a contradiction).
- Flag 4 (LR df vs category-usage) → PARTLY RESOLVED: the note now attributes the reduction to "unused end categories and any internal gap", which covers R27's gap. The count (10) is still my subtraction; the caption of `tbl-lr-tests` still says only "unused end categories". The writer may now say the reduction counts all never-used categories including R27's internal gap (quoting the note), still without quoting "10" as a notebook figure.
- Flag 12 (markdown order) → stands; `82319128` (M3 discriminations note) still sits before `tbl-score-agreement`, and the new `tbl-discrimination-summary` has no note of its own.
- Flag 19 ("`02_artifacts.md` is current") → NO LONGER TRUE: `02_artifacts.md` still lists the old ids (e.g. `tbl-discrimination-m3` a5fa5502, `tbl-rater-overview` 55fbc1ec), the old `tbl-rater-overview` caption "(⚑ = flagged)", and does not contain `tbl-discrimination-summary`. The results-embedder needs a delta run (46 N2 labels; total 53 with N0 1 + N1 6).
- All other flags (1, 5–11, 13–18) stand unchanged.
- F2.8 caveat "The severity range (1.37 − (−0.88) = 2.25) is my subtraction; the notebook does not print it" → superseded by item 3 (printed 2.247 from 3-decimal estimates).
- F1.20 Direction "First k with empirical ≥ 0.80 is k = 4 (0.834) ... The notebook does not print these thresholds" → amend: the .80 threshold is now printed; .70/.90 are not.
- F1.2 caveat "See Flag 4" → read with the amended Flag 4.
- F1.7 caveat "This table has no flag column; the ⚑ flags appear only in `tbl-rater-overview`" → stands, but the rule is now stated (item 4c).
- F2.9 caveat "The flag rule is not stated in the notebook" → superseded (item 4d).
- F2.12 "stale: four raters are excluded (see Flag 2)" → superseded; note text now in item 4a.
- Coverage-check rows "ratio_max_min NOT AVAILABLE", "k80 NOT printed", "Severity range NOT printed", "0.7–1.3 rule NOT in the notebook", "RQ1 ... '4' derived ... NOT printed", "RQ2 ... ratio NOT AVAILABLE" → all now AVAILABLE as listed above (7.277; k = 4 for the projection; 2.247 logits; rule stated).

**Spot-check of unchanged tables (values compared cell by cell with the findings file):**
- `tbl-model-fit` (`6b99df62`): identical (all 4 rows, 11 columns; e.g. GRM ΔBIC 4.161, M1 ΔBIC 0.000). No difference.
- `tbl-grm-reliability-ci` (`a230cacd`): identical (0.689 / 0.669 / 0.703 / 200 / 43; 0.969 / 0.965 / 0.974 / 200 / 43). No difference.
- `tbl-grm-reliability-by-n` (`2c343131`): identical, all 13 rows and 6 columns. No difference.
- `tbl-grm-reliability-projection` (`4021099f`): identical, all 10 rows (0.530 [0.513, 0.544] … 0.928 [0.925, 0.931]; Mean rel_post 0.530 … 0.928). Caption unchanged. No difference.
- `tbl-rater-overview` (`bd1ee008`): all 24 rows identical in every column, including the 15 ⚑ marks and the "6,7"/"5,7" lists. Only the caption changed ("⚑ = flagged" → "⚑ = infit or outfit outside 0.7–1.3"). No value difference.

### 6. N2 cell ids changed (old → new). N0 and N1 ids unchanged.

Labelled cells (46):

| Label | old id | new id |
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
| **tbl-discrimination-summary (NEW)** | — | 5ef7276b |
| tbl-threshold-order | 276c901a | 912f094e |
| tbl-rater-fit-m1 | fcb695cf | b315c83a |
| fig-m1-rater-severity | b55889a1 | 470979b6 |
| tbl-marginal-reliability-models | 79072096 | 5eb903e3 |
| tbl-naive-indices | 301d57ec | 68159a62 |
| tbl-reliability-overview | eee39e77 | e5c791df |
| tbl-rater-overview | 55fbc1ec | bd1ee008 |

Unlabelled cells cited in this file (old → new, matched by content):

| Content | old id | new id |
|---|---|---|
| Intro markdown ("Raters with fewer than 15 ratings are excluded…") | 92527bc1 | f2bfa0b0 |
| Design note | fd5772fd | 984c7665 |
| Ratings-per-product note | 2854cd3e | d295f53b |
| Category-use note | 18b6b4b1 | 168c8599 |
| Category-shares note | b33ccad2 | 0df31f46 |
| Central-model note | 766c1c00 | fb3a9f4b |
| Rater-parameters note | 2896214b | 9621d2dd |
| Discrimination-figure note | 8212b3db | 5bfaafc1 |
| CRF note | 2cd95b60 | f00021a9 |
| Rater-fit note (CHANGED) | f526bd7f | 38b48261 |
| Local-dependence note | 95a352e9 | ae69c561 |
| Mean-Q3 stdout | ccbeaf11 | 30b8685b |
| Global-fit note | 8ca12a65 | 8d4cac3b |
| Rater-information note | 1a2b3c14 | 13764ecb |
| Information-shares note | b69896ff | 62f872c1 |
| Information-summary note | 3e064209 | fce04648 |
| Full-panel note | c8ad3efc | c32b3d9e |
| Uncertainty-of-rater-information note | eab45d1d | 4ba77622 |
| Information-figure note | 34c34fb4 | 61896612 |
| Reliability-of-actual-scores note | 5b630dd6 | 757bdcbe |
| Reliability-by-number-of-ratings note | a30edc1b | 0e29eaac |
| Uncertainty-of-marginal-reliabilities note | 8ccf3d9c | bb9727bf |
| Histogram note | 82d77d33 | 2462a510 |
| rel_post-by-n figure note | 29d8973a | 957e3b46 |
| Projected-reliability note | 77937868 | 2dec374d |
| Projection-settings stdout (now also prints the k ≥ .80 line) | 64142953 | c7a7fe2a |
| Min-4 note | c7486592 | 8324c569 |
| Observed-vs-simulated note | 7561808c | f8cc0651 |
| rel_post-by-θ note | 83614bc3 | 6ee99d94 |
| Check (consistency) note | f203ce16 | 724a77e0 |
| Model-comparison note | 89bc0612 | a2d4633b |
| LR-tests note (CHANGED) | a5216280 | f43c6651 |
| Agreement-of-scores note | 6f8cf70e | 8cc9615e |
| M3-discriminations note | 9e0c8a51 | 82319128 |
| Change-in-product-ranking note | cfacd46d | cf79f2c0 |
| Raw-mean-vs-GRM note | 082bc140 | cfd13681 |
| Raw-mean figure note | be95800a | 2d9a4061 |
| Sensitivity note (CHANGED) | be69f6b6 | 91ed9594 |
| Threshold-order note | 838c800e | 7b4d9e8c |
| M1 infit/outfit note | cff2945e | 7a756200 |
| Rater-severity-under-M1 note | 51af707f | 616ffe85 |
| M1 severity range stdout (NEW) | — | 411ec44f |
| Marginal-reliability-by-model note | cab6dfb5 | 60050d5a |
| Naive-indices note | 3262dbf6 | 05ea5bc5 |
| Overview note | 3616abab | 425ba193 |
| Rater-overview note (CHANGED) | ea0a0f8c | d321faa3 |

Header line of this file to update: N2 now has 46 labels (total 53).


## Delta 2026-11-09b (coordinator; notebook 02 note corrected after reading R/08_reliability_min_ratings.R)

The note above `tbl-grm-reliability-min-ratings` previously said that the real ratings are kept in the top-up simulation. That was wrong and has been replaced. The notebook note now reads, verbatim and quotable as the procedure of the top-up simulation:

> Minimum number of ratings per product. A projection built on the actual design (R/08_reliability_min_ratings.R). Two designs are simulated with the same machinery. In the design labelled actual, each product keeps exactly the raters who rated it. In the design labelled at least 4 ratings per product, each product keeps its raters, and every product with fewer than 4 ratings is assigned additional raters, drawn at random with equal probability and without replacement from the panel raters who had not rated it, until it has 4; products with 4 or more ratings are unchanged. In each of the 50 replications, every real product receives a creativity value θ drawn from N(0, 1), all ratings in the design (kept and added rater–product pairs alike) are generated from the fitted GRM, and the products are scored by EAP with the fitted parameters treated as known. The real ratings themselves are not reused; the actual-design row is a validation that should reproduce the observed empirical reliability of the real scores. Summaries as for the projection above.

Consequences for the writer: describe the top-up simulation as keeping the actual rater–product assignment (not the ratings), adding raters without replacement from those who had not rated the product, and generating all ratings from the fitted GRM with θ ~ N(0, 1) per real product and EAP scoring with known parameters; the actual-design row (0.686 [0.675, 0.695]) is a validation against the observed 0.689. The same wording applies to the supplement note. Values in tbl-grm-reliability-min-ratings are unchanged. Display change in the same rebuild: the flag glyph ⚑ in tbl-rater-overview and its caption/note is now † (dagger), and fig-category-usage-shares labels read "unused: 5,7" instead of "✕ 5,7" (the pdf font lacks the glyphs).
