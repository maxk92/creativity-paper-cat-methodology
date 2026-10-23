> **Orchestrator note (2026-10-23):** The interpreter's output follows unchanged. It ran in parallel with phase 3 and read `02_artifacts.md` before that file was regenerated. Its "Labels" remark and Flag 8 ("Stale 02_artifacts.md") are therefore resolved: `02_artifacts.md` now lists the current 39 labels from NB00/NB01/NB02, and its labels match the ones used here. Values marked NOT IN NOTEBOOK must not be quoted in the manuscript. This includes the exclusion-sensitivity r = 0.99997 and max |Δθ̂| = 0.16.

# 03 Findings: results of the GRM/JRT pipeline (regenerated 2026-10-23)

Every number below is copied exactly as it appears in a stored notebook output. Nothing is rounded or recomputed. The display tables in `02_jrt_results.ipynb` use `floatfmt=".3f"`, so most values have 3 decimals. Higher-precision values appear only where a notebook prints them.

Sources:
- NB00 = `data-analysis/creativity-ratings-psychometrics/notebooks/00_data_loading_preprocessing.ipynb`
- NB01 = `.../notebooks/01_data_overview.ipynb`
- NB02 = `.../notebooks/02_jrt_results.ipynb`

**Labels:** `manuscript/02_artifacts.md` is stale. It lists the deleted Bayesian `02d` notebook (`tbl-jrt-*`, `fig-jrt-*`), so its labels were not used. The labels below are read directly from the `#| label:` lines in NB00, NB01 and NB02. Phase 3 (results-embedder) needs to be re-run.

**Pre/post exclusion:** NB00 and NB01 outputs are on the cleaned data before the rater exclusion: 7844 ratings, 3669 products, 22 raters. NB02 outputs are on the final data after excluding R20, R21 and R22: 7820 ratings, 3668 products, 19 raters.

---

## (a) Descriptive findings

### NB00: data loading and cleaning (pre-exclusion; not labelled as such, see Flags)

**F0.1 Raw export size**
- **Finding:** The raw sheet export had 9148 rows. 22 raters were pseudonymised.
- **Source:** NB00 cell 520638b8 ("Downloaded 9148 rows."); cell fdbdb3b4 ("Raters pseudonymised: 22").
- **Caveat:** No notebook output shows 23 raters. The "23 → 22" step appears only in AUDIT.md §5.2 (the former R23 had only "not recognised" ratings and was removed by a sheet update). That is not quotable from a notebook.

**F0.2 Cleaning steps**
- **Finding:** The cleaning steps reduced the rows from 9148 to 7844.
- **Linked object:** `tbl-cleaning-log` (NB00 cell bbcbf730; values printed in cell dd37b3ec).

| step | before | after | removed |
|---|---|---|---|
| drop_action_not_recognized | 9148 | 7858 | 1290 |
| drop_missing_id | 7858 | 7858 | 0 |
| drop_out_of_range | 7858 | 7857 | 1 |
| drop_missing_rating | 7857 | 7857 | 0 |
| resolve_duplicates | 7857 | 7844 | 13 |

- **Final cleaned data (cell dd37b3ec):** "Raters: 22", "Actions: 3669", "Warnings collected: 3".
- **Caveat:** AUDIT.md (A3) gives 1,292 not-recognised rows, but the notebook shows 1290. Use 1290.

**F0.3 Out-of-range rating**
- **Finding:** One rating value was out of range: 0.0, given by R04.
- **Source:** NB00 cell 793192b4.

**F0.4 Duplicate rater-product pairs**
- **Finding:** 25 rows belonged to duplicate (action_id, rater_id) combinations. The rule "keep last" removed 13 rows.
- **Source:** NB00 cell 72468670.
- **Pairs in the printed listing:** 12 pairs.
  - One of them is a triple from R22 (an excluded rater).
  - One pair has conflicting values: R14 rated 2.0 in row 3847 and 1.0 in row 7606.
- **Matches NB02:** `tbl-design-summary` reports duplicate_pairs_resolved_in_00 = 12 and duplicate_pairs_conflicting = 1.

### NB01: data overview (all outputs pre-exclusion: 22 raters, 7844 ratings, 3669 actions)

**F1.1 Sample size**
- **Finding:** The cleaned data before exclusion contain 7844 ratings of 3669 actions by 22 raters. The averages are 2.14 ratings per action and 356.5 per rater.
- **Source:** NB01 cell 981d6824.

**F1.2 Ratings per action and per rater**
- **Linked object:** `tbl-overview-ratings-per-action` (cell ovtbl01; table built in cell 9307f652).

| quantity | value |
|---|---|
| n_ratings | 7844.000 |
| n_actions | 3669.000 |
| n_raters | 22.000 |
| n_actions_1_rating | 898.000 |
| n_actions_2_ratings | 2080.000 |
| n_actions_3plus_ratings | 691.000 |
| share_actions_1_rating | 0.245 |
| share_actions_2_ratings | 0.567 |
| share_actions_3plus_ratings | 0.188 |
| max_ratings_per_action | 12.000 |
| mean_ratings_per_action | 2.138 |
| harmonic_mean_ratings_per_action | 1.726 |
| median_ratings_per_rater | 316.500 |
| min_ratings_per_rater | 2.000 |
| max_ratings_per_rater | 1174.000 |

- **Caveat:** This table is cited in the manuscript but reflects 22 raters (pre-exclusion). It conflicts with the final NB02 counts (F2.1).

**F1.3 Distribution of ratings per action and per rater**
- **Source:** NB01 cell 3b12b8bf (pre-exclusion).
- **Number of actions by number of ratings:**

| ratings | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| actions | 898 | 2080 | 357 | 123 | 118 | 50 | 25 | 9 | 6 | 2 | 1 |

- **Ratings per rater:** R22 2, R21 9, R20 13, R19 50, R16 52, R17 52, R18 55, R15 73, R13 254, R14 259, R12 264, R11 369, R10 383, R09 400, R06 520, R08 522, R07 547, R04 620, R05 633, R03 720, R02 873, R01 1174.
- **Related object:** the embedded figure `fig-overview-degree-distributions` (cell ovfig04; cell 9f03e286 prints "Raters with <= 2 rated actions: 1").

**F1.4 Connectivity and rater overlap**
- **Finding:** The bipartite design forms one connected component containing 3669 actions and 22 raters.
- **Source:** NB01 cell bacf60d8.
- **Best-partner overlap per rater** (cell aa371443; `fig-overview-rater-overlap`, cell ovfig01): R22 1, R21 8, R20 10, R17 44, R18 46, R19 46, R16 52, R15 61, R14 108, R12 145, R09 147, R13 154, R10 157, R05 190, R08 191, R06 240, R04 257, R02 257, R03 329, R01 329, R11 357, R07 357.
- **Caveat:** Both the figure and the list are 22×22 (pre-exclusion).

**F1.5 Overall category frequencies (pre-exclusion, N = 7844)**
- **Source:** NB01 cell 31873726; `fig-overview-rating-distribution` (cell ovfig02).

| category | n | share |
|---|---|---|
| 1 | 2034 | 0.259306 |
| 2 | 2116 | 0.269760 |
| 3 | 1471 | 0.187532 |
| 4 | 1045 | 0.133223 |
| 5 | 728 | 0.092810 |
| 6 | 341 | 0.043473 |
| 7 | 109 | 0.013896 |

- **Caveat:** No post-exclusion overall frequency table is printed in any notebook.

**F1.6 Rater response styles (22 raters, pre-exclusion)**
- **Source:** NB01 cell fb6df84b (unlabelled DataFrame). The figure is `fig-overview-rater-response-styles` (cell ovfig03).
- **Rater means:**
  - All 22: from 1.759615 (R06) to 3.836364 (R18).
  - R22 has mean 3.000000 on n = 2.
- **Ceiling rate (share of 7s), counted row by row from the printed table:**
  - Of 22 raters, 8 have ceiling_rate 0.000000: R06, R17, R01, R03, R22, R21, R20, R18. The other 14 are above 0.
  - Of the 19 retained raters, 5 have 0.000000: R06, R17, R01, R03, R18. The other 14 are above 0.
  - Highest ceiling rates: R19 0.080000, R16 0.057692, R09 0.055000, R02 0.051546.
- **Floor rate (share of 1s):**
  - Highest: R06 0.578846, then R17 0.480769.
  - Only R22 has 0.000000.
- **Number of categories used (counted from the table):**
  - 7 categories: 14 raters.
  - 6 categories: 4 raters (R06, R01, R03, R18).
  - 5 categories: 3 raters (R17, R21, R20).
  - 2 categories: 1 rater (R22).
  - Of the 19 retained raters, 14 use all 7 and 5 do not. This matches design summary raters_with_category_gaps = 5 (F2.1).
- **Central-category rate (3–5):**
  - Highest: R13 0.799213, R18 0.763636, R12 0.734848.
  - Lowest: R06 0.192308.
- **Caveat:** The table includes R20, R21 and R22 and is not labelled as pre-exclusion.

### NB02: data and design (final data)

**F2.1 Final data and design**
- **Linked object:** `tbl-design-summary` (NB02 cell 6139f51b).

| quantity | value |
|---|---|
| n_ratings | 7820 |
| n_products | 3668 |
| n_raters | 19 |
| min_ratings_per_rater (exclusion cut-off) | 15 |
| raters_excluded | R20;R21;R22 |
| ratings_excluded | 24 |
| products_dropped | 1 |
| n_categories | 7 |
| scale | 1-7 |
| internal_coding | rating - 1 (0-6) |
| ratings_per_product_mean | 2.1319520174482 |
| ratings_per_product_median | 2 |
| ratings_per_product_min | 1 |
| ratings_per_product_max | 10 |
| ratings_per_product_harmonic_mean | 1.72615922960609 |
| products_with_1_rating | 897 |
| ratings_per_rater_min | 50 |
| ratings_per_rater_max | 1174 |
| matrix_fill | 0.112208000918326 |
| n_components | 1 |
| rater_pairs_total | 171 |
| rater_pairs_without_overlap | 17 |
| rater_pairs_overlap_median | 13 |
| raters_with_category_gaps | 5 |
| raters_with_internal_gap | 0 |
| duplicate_pairs_resolved_in_00 | 12 |
| duplicate_pairs_conflicting | 1 |

- **Verification:** The author's final counts are confirmed here: 7820 ratings, 3668 products, 19 raters.

**F2.2 Excluded raters**
- **Linked object:** `tbl-excluded-raters` (cell 3ecd1ea9).
- R20 had 13 ratings, R21 had 9 and R22 had 2. All three are marked "fewer than 15 ratings".

**F2.3 Category use per rater (final 19 raters)**
- **Linked object:** `tbl-category-usage` (cell ad41df98).
- **Raters with missing categories:**
  - Category 7 unused: R01, R03, R06, R18.
  - Categories 6 and 7 unused: R17.
- internal_gap is False for all 19 raters.
- **Selected cat_7 counts:**
  - R02 45, R09 22, R05 12, R08 7, R04 5, R19 4, R16 3.
  - R07, R10 and R14 have 2 each. R11, R12 and R13 have 1 each.

---

## (b) Model comparison (NB02, Section 4)

**F2.4 Information criteria**
- **Finding:** The GRM has the lowest AIC, BIC and SABIC of the four models.
- **Linked object:** `tbl-model-fit` (cell 290e7399).

| model | software | family | logLik | npar | AIC | BIC | SABIC |
|---|---|---|---|---|---|---|---|
| M1_RSM | sirt::rm.facets | adjacent category | -12186.218 | 25.000 | 24422.435 | 24577.620 | 24498.183 |
| M2_PCM | mirt | adjacent category | -11817.489 | 109.000 | 23852.978 | 24529.585 | 24183.237 |
| M3_GPCM | mirt | adjacent category | -11756.510 | 127.000 | 23767.020 | 24555.360 | 24151.817 |
| GRM | mirt | cumulative (not in LR ladder) | -11733.227 | 127.000 | 23720.455 | 24508.795 | 24105.251 |

- **Other comparisons:**
  - M3 and the GRM have the same npar (127.000).
  - BIC ranks M2 (24529.585) below M3 (24555.360).
- **Caveat stated in NB02 (cell 619d9bec):** The GRM is in the cumulative family. It is compared with the ladder by information criteria only.

**F2.5 Likelihood-ratio tests**
- **Finding:** Both LR tests in the adjacent-category ladder are significant.
- **Linked object:** `tbl-lr-tests` (cell e783ceee).
  - M1 vs M2 (rater-specific thresholds): X2 = 737.457, df = 84, df_expected_formula = 90, p = 0.000.
  - M2 vs M3 (rater-specific discriminations): X2 = 121.958, df = 18, df_expected_formula = 18, p = 0.000.
- **Caveats:**
  - p prints as 0.000 at 3 decimals. The exact p-values are not in any notebook. REPORT.md gives "<2e-16" and AUDIT.md gives "< 10⁻¹⁰⁰" and "1.8 × 10⁻¹⁷", all NOT IN NOTEBOOK and not quotable. From the notebook alone, the writer can state p < .001.
  - For M1 vs M2, the df (84) differ from the formula (90). The reason, end-category gaps, is given in AUDIT.md only.
  - M1 vs M2 is a cross-software test (sirt vs mirt). The software cross-check (logLik difference 0.037) is NOT IN NOTEBOOK.

**F2.6 Threshold order in M2/M3 vs. GRM**
- **Linked object:** `tbl-threshold-order` (cell fa64bb53).
- **M2_PCM:** 9 raters have unordered step parameters: R03, R04, R05, R06, R11, R15, R16, R17, R19. n_reversals = 2 for R15, R17 and R19; 1 for the others.
- **M3_GPCM:** 9 raters have unordered step parameters: R03, R04, R05, R06, R09, R11, R15, R17, R18. n_reversals = 2 for R09 and R17; 1 for the others.
- **GRM:** `tbl-grm-rater-parameters` shows thresholds_ordered = True for all 19 raters. NB02 cell a218d34d says GRM thresholds are ordered by construction.

**F2.7 M3 discriminations**
- **Linked object:** `tbl-discrimination-m3` (cell 3a2c335e).
- Estimates range from 0.283 (R09, se 0.055) to 2.606 (R16, se 1.419). All are positive.
- **Largest SEs:** R19 (estimate 2.327, se 1.866), R16 (se 1.419), R12 (2.383, se 0.680).

**F2.8 M1 (MFRM) rater infit/outfit**
- **Linked object:** `tbl-rater-fit-m1` (cell 769b0edd).
- Infit ranges from 0.238 (R12) to 1.328 (R17).
- **Values ≥ 1:** R17 (infit 1.328, outfit 1.190) and R18 (1.009, 1.071).
- Lowest outfit: R12 0.255.

---

## (c) Fit evidence and its stated limitations (GRM)

**F2.9 Estimation and convergence**
- **Linked object:** `tbl-grm-convergence` (cell ddcec9c7).
- Settings: method EM, quadpts 61, se_type Oakes.
- Result: converged True after 165 iterations. information_matrix_pd = True.
- Fit statistics: logLik -11733.227, npar 127, AIC 23720.455, BIC 24508.795, SABIC 24105.251.
- Data: n_products 3668, n_ratings 7820.
- **Caveats:**
  - tol prints as "0.000" because of the display format. The actual value (1e-4 per AUDIT.md) is NOT IN NOTEBOOK.
  - The condition number (7.8 × 10³ in AUDIT.md) is NOT IN NOTEBOOK.

**F2.10 Rater infit/outfit (GRM)**
- **Finding:** All 19 GRM infit and outfit mean squares are below 1.
- **Linked object:** `tbl-grm-rater-fit` (cell bcf04132).
- Infit ranges from 0.334 (R19) to 0.971 (R18). Outfit ranges from 0.322 (R19) to 0.961 (R18).
- **Caveat stated in NB02 (cell 98e4a70f):** With about 2 ratings per product, values below 1 are expected, because the score is estimated from the very ratings being checked.
- **Not in NB02:** The 0.7–1.3 flag rule and the statement "14 of 19 raters flagged" are in REPORT.md/AUDIT.md only.

**F2.11 S-X² (multiple imputation)**
- **Finding:** No rater's S-X² is significant.
- **Linked object:** `tbl-grm-rater-fit` (cell bcf04132).
- p_S_X2 ranges from 0.294 (R12; S_X2 207.049, df 196.800) to 0.671 (R02). n_imputations = 20 for all raters.
- **Caveat stated in NB02:** S-X² needs complete data, so missing ratings are imputed 20 times. About 90% of cells are imputed, which makes the test conservative.
- **Discrepancy:** AUDIT.md says "all p > .36". The notebook minimum is 0.294 (R12), so the AUDIT statement is inconsistent with the notebook. RMSEA ≈ 0 is NOT IN NOTEBOOK.

**F2.12 Local dependence (Q3)**
- **Linked object:** `tbl-grm-q3-flagged` (cell 13829fea). It shows the top 10 pairs by |q3_minus_mean| among pairs with n_common ≥ 30.

| pair | n_common | q3 | q3_minus_mean |
|---|---|---|---|
| R08–R19 | 46 | -0.761 | -0.524 |
| R08–R12 | 51 | -0.743 | -0.506 |
| R02–R14 | 108 | -0.621 | -0.383 |
| R03–R10 | 49 | -0.616 | -0.379 |
| R01–R10 | 157 | -0.613 | -0.376 |
| R02–R04 | 257 | -0.611 | -0.373 |
| R02–R08 | 72 | -0.589 | -0.352 |
| R10–R11 | 32 | 0.105 | 0.343 |
| R01–R08 | 191 | -0.565 | -0.327 |
| R04–R14 | 47 | -0.560 | -0.322 |

- All 10 rows have flag_q3 True. overlap_flag is nan.
- **Caveat stated in NB02 (cell b929aee9):** With few raters per product, Q3 is biased negatively (Christensen et al., 2017), so pairs are ranked by deviation from the mean Q3.
- **Not in notebook:** the mean Q3 itself (−0.24 in AUDIT.md), "20 pairs deviate by > 0.2", and "up to 0.94, R01–R14".

**F2.13 Global fit (C2)**
- **Finding:** C2 could not be computed.
- **Linked object:** `tbl-grm-global-fit` (cell 1092b747). statistic = C2, note "Not computable: missing value where TRUE/FALSE needed".
- **Caveat:** The likely cause given in AUDIT.md is "37 rater pairs share no product". That is a pre-exclusion figure; the final design has 17 pairs without overlap (F2.1). The cause is not stated in the notebook.

---

## (d) Reliability: empirical marginal vs. full panel vs. alpha

**F2.14 GRM reliability summary**
- **Linked object:** `tbl-grm-reliability-summary` (cell 1c039bcd).

| quantity | value |
|---|---|
| empirical_marginal_reliability (primary; actual scores) | 0.672 |
| model_based_marginal_reliability_mirt (hypothetical full panel) | 0.960 |
| model_based_marginal_reliability_grid (check) | 0.960 |
| var_theta_eap | 0.672 |
| mean_psd_squared | 0.328 |
| rel_post min | 0.057 |
| rel_post p10 | 0.485 |
| rel_post q1 | 0.596 |
| rel_post median | 0.698 |
| rel_post q3 | 0.769 |
| rel_post p90 | 0.813 |
| rel_post max | 0.929 |
| rel_post mean | 0.672 |
| rel_post iqr | 0.173 |
| consistency_cor_rel_post_rel_info | 0.935 |
| consistency_mean_diff_rel_info_minus_rel_post | 0.016 |
| consistency_max_abs_diff | 0.413 |
| products_abs_diff_gt_0.1 | 320.000 |

- **Caveats stated in NB02 (cells e1d17569 and 11294212):**
  - The empirical marginal reliability refers to the EAP scores actually obtained and is the primary figure.
  - The model-based value refers to a hypothetical full panel and is an upper bound, not the precision of the actual scores.
- **Related figures:**
  - `fig-grm-panel-information` (cell 2415165a)
  - `fig-grm-rel-post-histogram` (609dce88)
  - `fig-grm-rel-post-by-theta` (fa9b0260)
  - `fig-grm-rel-consistency` (52fbd3a5)

  These are stored images; their plotted values are not printed.

**F2.15 Product-level reliability by number of ratings**
- **Linked object:** `tbl-grm-reliability-by-n` (cell f242573e). The figure version is `fig-grm-rel-post-by-n` (cell e64833fa).

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

- **Direction:** Mean rel_post rises and mean PSD falls monotonically with n_ratings.
- **Caveat:** n_products is 3 for n = 9 and for n = 10.

**F2.16 Reliability by model**
- **Linked object:** `tbl-marginal-reliability-models` (cell 672f8fa4).

| model | latent_variance | marginal_reliability | marginal_rxx_mirt | empirical_rxx |
|---|---|---|---|---|
| M1_RSM | 0.962 | 0.943 | nan | 0.626 |
| M2_PCM | 1.087 | 0.944 | nan | 0.637 |
| M3_GPCM | 1.000 | 0.955 | 0.955 | 0.657 |
| GRM | 1.000 | 0.960 | 0.960 | 0.672 |

- **Caveat:** NB02 cell ac2c888f says marginal reliability is for the hypothetical full panel and empirical reliability is for the actual scores.

**F2.17 Naive indices**
- **Linked object:** `tbl-naive-indices` (cell 0cd6dfa8).
  - Cronbach's alpha, pairwise covariances, all usable raters: 0.928 (n_raters 14, n_products 1900).
  - Cronbach's alpha, fully crossed block (listwise complete): 0.658 (n_raters 3, n_products 139).
  - Krippendorff's alpha (ordinal): 0.392, 95% CI [0.362, 0.417] (n_raters 19, n_products 2771).
- **Overview table:** `tbl-reliability-overview` (cell 87f4e2ec) adds the following:
  - The bootstrap has 1000 replications.
  - Raters removed for pairwise alpha: R19, R14, R02, R16, R12.
  - Krippendorff's alpha refers to "consensus of single ratings"; Cronbach's alpha refers to "consistency of the unweighted rater mean".
- **Caveats stated in NB02 (cells 78989be7 and fdc98523):**
  - Cronbach's alpha assumes τ-equivalent raters and complete data.
  - Krippendorff's alpha treats raters as interchangeable.
  - The indices answer different questions and are not interchangeable.
- **Not in notebook:**
  - The identity of the 3 crossed-block raters (R07, R09, R11 in AUDIT.md).
  - The psych warning that the matrix was not positive definite and was smoothed.

---

## (e) Rater parameters and information, including uncertainty

**F2.18 GRM rater parameters**
- **Linked object:** `tbl-grm-rater-parameters` (cell 0864d752). The figure is `fig-grm-category-response-functions` (cell 7f6b17ca).
- **Discrimination a:**
  - a ranges from 0.631 (R18, a_se 0.263) to 3.709 (R19, a_se 2.220).
  - Second highest: R16, a = 3.701, a_se 1.359.
  - Other low values: R09 0.863 (a_se 0.151); R17 1.446 (a_se 0.465); R13 1.504 (a_se 0.223).
- **Thresholds:**
  - Most extreme: R18 has b1 = -6.565 and b5 = 4.440. R13 has b1 = -3.384 and b6 = 4.435.
  - Number of thresholds by rater: 4 for R17 (boundaries 1|2…4|5); 5 for R01, R03, R06, R18; 6 for all others.
  - All thresholds are ordered.
- **Uncertainty:**
  - The largest a_se are for raters with ≤ 73 ratings: R19 2.220 (n 50), R16 1.359 (n 52), R15 0.525 (n 73), R17 0.465 (n 52).
  - Among larger raters: R14 0.661 (n 259), R12 0.565 (n 264).
  - Threshold SEs are not shown in the displayed table, although the caption mentions them (see Flags).

**F2.19 Rater information summary**
- **Linked object:** `tbl-grm-information-summary` (cell 024656ba; 3-decimal display). Unlabelled cell ad422588 shows the same values at 6 decimals.
- **Weighted information area (info_weighted_area):**
  - Ranges from 0.123 (R18) to 3.539 (R19).
  - R16 3.300; R12 2.120; R09 0.238.
- **Weighted share of full-panel information (share_weighted):**
  - Highest: R19 0.135 and R16 0.126 (n = 50 and 52).
  - Lowest: R18 0.005 and R09 0.009 (n = 55 and 400).
  - R01, the rater with the most ratings (1174), has share 0.037.
- **Location of the information peak (theta_at_max):**
  - Highest: R01 2.700, R06 2.400, R16 1.850.
  - Lowest: R13 -0.550, R18 -0.500, R19 -0.100.
- **Shares at selected θ:**
  - At θ = -2: R12 0.221, R15 0.138, R10 0.129.
  - R06 has share 0.001 at θ = -2 and 0.083 at θ = +2.
- **Related figures:** `fig-grm-rater-information` (cell b591d2c9) and `fig-grm-information-shares` (cell f37bccfe).
- **Uncertainty caveat:** Information values are computed at point estimates. No SE or CI for information or shares is present in any notebook. The two highest-share raters (R19, R16) are the ones with the largest a_se (F2.18).

---

## (f) Model-dependence of product scores and rankings

**F2.20 Agreement of EAP scores across models**
- **Linked object:** `tbl-theta-correlations` (cell 2be45de3).

| pair | Pearson | Spearman |
|---|---|---|
| GRM–M3_GPCM | 0.996 | 0.996 |
| GRM–M2_PCM | 0.985 | 0.983 |
| GRM–M1_RSM | 0.975 | 0.978 |
| M1–M2 | 0.993 | 0.996 |
| M1–M3 | 0.980 | 0.983 |
| M2–M3 | 0.989 | 0.987 |
| rm_facets_default_grid–M1_RSM | 1.000 | 1.000 |

- rm_facets_default_grid has the same correlations as M1 with every other model.
- **Not in notebook:**
  - Any rank-change statistics, such as top-k overlap or max |Δθ̂| between models.
  - Product-score tables.
  - AUDIT.md's "r = 0.999999" for default grid vs M1. The notebook shows only 1.000.

---

## (g) Sensitivity analyses

**F2.21 Sensitivity checks that are in the notebooks**
- **Integration grid:** M1 on the fine grid vs sirt's default grid correlate at 1.000 (Pearson and Spearman; `tbl-theta-correlations`).
- **Cronbach's alpha on two data subsets:** 0.928 pairwise vs 0.658 crossed block (`tbl-naive-indices`).
- **Two routes to product-level reliability:** rel_post vs rel_info correlate at 0.935, with mean difference 0.016 and max |diff| 0.413. 320 products differ by more than 0.1 (`tbl-grm-reliability-summary`).

**F2.22 Sensitivity of the rater exclusion (r = 0.99997)**
- **Not present in any notebook.** I searched the analysis folder for "0.9999", "99997" and "sensitiv" in all non-CSV files. The value occurs only in `AUDIT.md` line 36, together with "max |Δθ̂| = 0.16".
- Both values are **NOT IN NOTEBOOK and not quotable**.
- The all-raters run is referenced only as git commit `5a0cf88` (AUDIT.md), not as a notebook output.
- The same applies to the AUDIT.md statement that R21 and R22 were not identified in the 22-rater run (R21 a = −0.09, SE 1.01, max |b| = 24.5; R22 a = −3.86, SE 7.83): NOT IN NOTEBOOK.

---

## Not found (absent from all three notebooks)

- **Exclusion sensitivity:** the correlation r = 0.99997 and max |Δθ̂| = 0.16 (AUDIT.md only).
- **Exact LR p-values:** only 0.000 is displayed.
- **Effect sizes for model comparison** beyond logLik, AIC, BIC and SABIC: none reported (no ΔBIC column, no pseudo-R²).
- **Estimation details:** the GRM tol value (prints as 0.000) and the condition number.
- **Q3:** the mean Q3, the number of pairs with |deviation| > 0.2, and the Q3 values for pairs with n_common < 30.
- **S-X² RMSEA.**
- **Threshold SEs in the GRM table:** they are in the caption but are not among the displayed columns.
- **Uncertainty of rater information and shares.**
- **Product rankings:** rank-change or top-k statistics between models, and any product-level score table.
- **Post-exclusion descriptives:**
  - overall category frequencies (only per-rater counts in `tbl-category-usage`);
  - rater response-style table (mean, SD, floor and ceiling rates);
  - overlap heatmap;
  - degree distributions.
- **Crossed-block raters:** the identity of the 3 raters in the crossed block.
- **The 23 → 22 rater step:** absent from any notebook output (AUDIT.md only).
- **Software cross-check (sirt vs mirt):** logLik difference 0.037; latent variances 0.544 and 0.537.

---

## Flags

1. **Pre-exclusion outputs in NB01, not labelled as such.**
   - Every NB01 output reflects 22 raters, 7844 ratings and 3669 actions: cells 981d6824, 3b12b8bf, 9307f652/ovtbl01, bacf60d8, aa371443/ovfig01, 31873726/ovfig02, fb6df84b/ovfig03, 9f03e286/ovfig04.
   - Neither NB01's markdown nor its captions say these are pre-exclusion.
   - Some of them are labelled objects cited by the manuscript: `tbl-overview-ratings-per-action`, `fig-overview-*`.
   - They conflict with NB02: 898 vs 897 single-rated products; max 12 vs 10 ratings per product; min 2 vs 50 ratings per rater; median rater overlap and number of rater pairs differ.
2. **NB00 is also pre-exclusion** ("Raters: 22", "Actions: 3669"). This is expected for a preprocessing step, but it is not marked.
3. **Pseudonymisation leaks.**
   - **(a) NB01 cell b1510393** prints the full pseudonym → original-ID mapping for all 22 raters.
   - **(b) NB02 cell ad422588** prints `original_rater_id` next to each rater's information summary.
   - **(c) NB00 cell 520638b8** no longer prints a raw preview, so the earlier rater-ID leak there is fixed. However, the cell source still contains the full Google Sheet URL, and the sheet is shared as "anyone with the link". That sheet holds the non-pseudonymised user IDs.
   - **(d)** NB01 cell 0036cba5 and NB02 cell 5479a668 load the gitignored key file.
   - All of these should be removed before the notebooks are published or embedded. AUDIT.md §5 states "Original IDs never go into `results/`", but they do appear in the notebook outputs.
4. **AUDIT.md vs notebook inconsistencies.** None of these AUDIT.md values should be used.
   - S-X²: AUDIT says "all p > .36"; the notebook minimum is p = 0.294 (R12).
   - Not-recognised rows: AUDIT says 1,292; the notebook shows 1290.
   - Rater pairs: AUDIT gives 37 of 231 pairs without overlap and median overlap 7. These are pre-exclusion figures and are used to explain why C2 failed. The notebook (final data) shows 17 of 171 and median 13.
5. **Ceiling-rate count (corrected).**
   - 22 raters: 8 have ceiling_rate 0 and 14 have ceiling_rate > 0.
   - 19 retained raters: 5 have 0 (R01, R03, R06, R17, R18) and 14 have > 0.
   - These counts are taken from NB01 cell fb6df84b and are consistent with `tbl-category-usage` (cat_7 = 0 for the same 5 raters).
6. **Display precision.** NB02 tables use 3 decimals, so tol and the LR p-values show as 0.000. Higher precision exists only in unlabelled cell ad422588 (information summary), which contains the leak in flag 3(b).
7. **Duplicate pairs include an excluded rater.** One of the 12 duplicate pairs counted in `tbl-design-summary` belongs to excluded rater R22. The figure 12 therefore describes the pre-exclusion cleaning.
8. **Stale `manuscript/02_artifacts.md`.** It lists `02d` labels; that notebook has been deleted. It also gives the wrong cell id for `tbl-overview-ratings-per-action` (9307f652; the labelled cell is ovtbl01). Phase 3 needs to be re-run.
9. **Unordered steps in M3 for R18 and R09.** M3 has unordered steps for R18 and R09, which M2 does not. M2 has unordered steps for R16 and R19, which M3 does not. This is reported as printed, without explanation.
