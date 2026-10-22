# 03_findings.md: Results findings (Phase 4, results-interpreter)

Regenerated from scratch on 2026-10-21. No value has been carried over from the previous version of this file.

**In-scope sources only:** `00_data_loading_preprocessing.ipynb`, `01_data_overview.ipynb` and `02d_judge_response_theory.ipynb`, plus the CSVs and logs those three notebooks write. Excluded: 02a/02b/02c/03, `02_creativity_ratings_R.qmd`, and all `classical_*`, `lmm_*`, `mfrm_*`, `comparison_*` and `sample_description_summary*` outputs.

Paths:
- NB = `data-analysis/creativity-ratings-psychometrics/notebooks/`
- TAB = `data-analysis/creativity-ratings-psychometrics/results/tables/`
- LOG = `data-analysis/creativity-ratings-psychometrics/results/logs/`

**Rules applied:**
- Values are copied exactly as they appear in the CSV or the printed cell output. Where a notebook prints a rounded version of a CSV value, both are given.
- Nothing is recomputed. Where I compared values against each other (for the consistency flags), I only checked existing numbers; no new number is introduced.
- Descriptive only.

**Labels:** the `#| label:` options now present in the notebooks are used. They differ in part from the proposals in `02_artifacts.md` (see X1).

---

## A. Design and sample (00, 01)

### F0.1 Raw export
- **Finding:** The raw Google-Sheets export contained 9150 rows. 23 distinct rater IDs were pseudonymised.
- **Linked object:** none
- **Numbers:**
  - "Downloaded 9150 rows." (00, cell `520638b8`)
  - "Raters pseudonymised: 23 (key saved to data/raw/rater_pseudonym_key.csv)" (00, cell `fdbdb3b4`)
  - "Event details saved: … action_events_raw.csv (4104 actions)" (00, cell `722729d7`; StatsBomb lookup on the raw action IDs)
- **Direction/comparison:** —
- **Caveats in data:** The raw export has 23 raters; the cleaned data has 22 (F0.2). The outputs don't say which step removed the 23rd rater (see X3).

### F0.2 Cleaning log
- **Finding:** Five cleaning steps reduced 9150 rows to 7844 rows.
- **Linked object:** `tbl-cleaning-log` (00, cell `bbcbf730`; CSV written in cell `dd37b3ec`)
- **Numbers** (TAB `cleaning_log.csv`; identical to the printout in `dd37b3ec`):

  | step | n_rows_before | n_rows_after | n_rows_affected |
  |---|---|---|---|
  | drop_action_not_recognized | 9150 | 7858 | 1292 |
  | drop_missing_id | 7858 | 7858 | 0 |
  | drop_out_of_range | 7858 | 7857 | 1 |
  | drop_missing_rating | 7857 | 7857 | 0 |
  | resolve_duplicates | 7857 | 7844 | 13 |

- **Supporting printouts:**
  - Cell `fb9eaf36`: "Rows flagged as action_not_recognized: 1292"
  - Cell `36dd5cb3`: "Missing action_id: 0", "Missing rater_id:  0", "Non-convertible, non-missing raw rating values: 0"
  - Cell `793192b4`: "Values outside {1,...,7} or non-integer: 1". This is a single row: rater R04, rating 0.0.
  - Cell `72468670`: "Rows with a duplicate (action_id, rater_id) combination: 25". The rule is to keep the last entry. The 25 rows form 11 pairs and 1 triple (R22), so 13 rows were removed. In one pair the ratings differ: R14 on action `36a6bfe9-…`, 2.0 (row 3847) vs 1.0 (row 7606).
  - Cell `dd37b3ec`: "Raters: 22", "Actions: 3669", "Warnings collected: 3"
- **Direction/comparison:** The largest exclusion is "action not recognized" (1292 rows).
- **Caveats in data:**
  - The cleaning log now has 5 rows with no duplicated step. Problem P10 in `02_artifacts.md` no longer applies.
  - Cell `72468670` prints "Cleaning complete: 7858 -> 7844 rows." The 7858 is the count after the first exclusion, because the variable `n0` is reset in cell `36dd5cb3`. It is not the raw count of 9150.
  - The 3 warnings collected in 00 are only printed; no CSV of them is written.

### F0.3 Cleaned sample size and connectivity
- **Finding:** The cleaned data has 7844 ratings of 3669 actions by 22 raters. The rater–action graph is one connected component containing all actions and raters.
- **Linked object:** `tbl-overview-ratings-per-action` (01, cell `9307f652`). No label on the component table.
- **Numbers:**
  - TAB `sample_ratings_per_action.csv`: n_ratings 7844.0, n_actions 3669.0, n_raters 22.0
  - 01, cell `981d6824`: "Total ratings:   7844", "Distinct actions: 3669", "Distinct raters:  22", "Average ratings per action: 2.14", "Average ratings per rater:  356.5"
  - TAB `connectivity_component_summary.csv`: component 0, n_actions 3669, n_raters 22, raters R01–R22
  - 01, cell `bacf60d8`: "Number of connected components: 1"
  - 02d, cell `aabc161c`: "Loaded 7844 ratings (3669 actions, 22 raters)."
  - 02d, cell `c3b5a10e`: "Connected components: 1; largest: 3669 actions, 22 raters."
  - 02d, cell `cd9b2c8a`: "Ordinal model: 7844 ratings, 3669 actions, 22 raters."
  - TAB `model_diagnostics_jrt.csv`: n_components 1.0
- **Direction/comparison:** —
- **Caveats in data:** The JRT model uses the full cleaned data set; no actions or raters were excluded for connectivity.

### F0.4 Ratings per action
- **Finding:** 898 actions have 1 rating, 2080 have 2 and 691 have 3 or more. The maximum is 12.
- **Linked object:** `tbl-overview-ratings-per-action` (01, cell `9307f652`); `fig-overview-degree-distributions` (01, cell `9f03e286`, panel A)
- **Numbers** (TAB `sample_ratings_per_action.csv`):
  - n_actions_1_rating 898.0; n_actions_2_ratings 2080.0; n_actions_3plus_ratings 691.0
  - share_actions_1_rating 0.2447533387844099; share_actions_2_ratings 0.5669119651131098; share_actions_3plus_ratings 0.18833469610248024
  - max_ratings_per_action 12.0; mean_ratings_per_action 2.137912237666939; harmonic_mean_ratings_per_action 1.726320341325184
- **Full distribution** (01, cell `3b12b8bf`): 1: 898; 2: 2080; 3: 357; 4: 123; 5: 118; 6: 50; 7: 25; 8: 9; 9: 6; 10: 2; 12: 1.
- **Cumulative** (same cell): ≥1 3669; ≥2 2771; ≥3 691; ≥4 334; ≥5 211; ≥6 93; ≥7 43; ≥8 18; ≥9 9; ≥10 3; ≥12 1.
- **Direction/comparison:** 2 ratings is the most common count (0.5669119651131098 of actions).
- **Caveats in data:**
  - 01 cell `8081f873` prints "24% of actions currently have only one rating…" (rounded display of 0.2447533387844099).
  - The ratings-per-action bar chart in `3b12b8bf` is not saved to `results/` and has no label.

### F0.5 Ratings per rater
- **Finding:** The number of ratings per rater ranges from 2 to 1174, with a median of 316.5.
- **Linked object:** `fig-overview-degree-distributions` (panel B); `rater_descriptive_statistics.csv` (01, cell `fb6df84b`; this cell has no label)
- **Numbers:**
  - TAB `sample_ratings_per_action.csv`: median_ratings_per_rater 316.5; min_ratings_per_rater 2.0; max_ratings_per_rater 1174.0
  - Per rater (01, cell `3b12b8bf`): R22 2, R21 9, R20 13, R19 50, R16 52, R17 52, R18 55, R15 73, R13 254, R14 259, R12 264, R11 369, R10 383, R09 400, R06 520, R08 522, R07 547, R04 620, R05 633, R03 720, R02 873, R01 1174
  - 01, cell `9f03e286`: "Raters with <= 2 rated actions: 1"
  - 01, cell `8081f873`: "8 raters have rated notably fewer actions than the median rater (316): R15, R16, R17, R18, R19, R20, R21, R22." The rule is fewer than half the median. The printed "316" is a rounded display of 316.5.
- **Best-partner overlap** (number of actions shared with the rater's best-connected partner; 01, cell `aa371443`): R22 1, R21 8, R20 10, R17 44, R18 46, R19 46, R16 52, R15 61, R14 108, R12 145, R09 147, R13 154, R10 157, R05 190, R08 191, R06 240, R04 257, R02 257, R03 329, R01 329, R11 357, R07 357.
  - Cell `8081f873`: "3 of 22 raters have fewer than 15 shared actions with their best-connected partner: R22, R21, R20."
  - Linked figure: `fig-overview-rater-overlap` (heatmap; saved as png/svg with no caption file).
- **Direction/comparison:** Rater IDs are ordered by raw row count, so R01 has the most ratings and R22 the fewest.
- **Caveats in data:** R22 (2 ratings), R21 (9) and R20 (13) have very few ratings.

### F0.6 Category frequencies
- **Finding:** Categories 1 and 2 together account for 0.5290668026517084 of all ratings. Categories 6 and 7 account for 0.05736868944416114.
- **Linked object:** `fig-overview-rating-distribution` (01, cell `31873726`)
- **Numbers** (TAB `overview_category_frequencies.csv`; same as the printout in `31873726`):

  | category | n | share |
  |---|---|---|
  | 1 | 2034 | 0.2593064762876084 |
  | 2 | 2116 | 0.26976032636409997 |
  | 3 | 1471 | 0.18753187149413564 |
  | 4 | 1045 | 0.13322284548699642 |
  | 5 | 728 | 0.09280979092299847 |
  | 6 | 341 | 0.043472718001019886 |
  | 7 | 109 | 0.013895971443141255 |

  - The combined shares come from TAB `jrt_derived_counts.csv` (share_ratings_categories_1_2, share_ratings_categories_6_7).
  - 02d cell `cd9b2c8a` prints the same counts: "[2034 2116 1471 1045  728  341  109]".
- **Direction/comparison:** Frequency is highest for category 2 (2116) and lowest for category 7 (109). From category 2 upward, frequency falls with each higher category.
- **Caveats in data:** Category 7 is sparse (109 ratings).

### F0.7 Krippendorff's α
- **Finding:** Krippendorff's α (interval level), computed on the full incomplete rater × action matrix, is 0.41813163607566517.
- **Linked object:** none. Cell `2d38a684` has no label.
- **Numbers** (TAB `overview_krippendorff_alpha.csv`): krippendorff_alpha_interval 0.41813163607566517; n_actions_pairable 2771.0; share_actions_pairable 0.75524666121559.
  - 01 cell `2d38a684` prints: "Krippendorff's alpha (interval, rough overall estimate): 0.418" and "Actions with >=2 ratings (contributing to this estimate): 2771 of 3669 (75.5%)".
- **Direction/comparison:** —
- **Caveats in data:**
  - The coefficient treats raters as interchangeable, as the notebook itself states (01 markdown `fa198c36`: "a crude, one-number descriptive of raw agreement that treats raters as interchangeable").
  - No CI or bootstrap is reported.
  - The package version of `krippendorff` is not printed.

### F0.8 Rater response styles (descriptive)
- **Finding:** Rater mean ratings range from 1.7596153846153846 (R06) to 3.8363636363636364 (R18).
- **Linked object:** `fig-overview-rater-response-styles` (01, cell `374f3c3d`). The table cell `fb6df84b` has no label.
- **Numbers** (TAB `rater_descriptive_statistics.csv`, sorted by mean):

  | rater | n_ratings | mean | sd | n_categories_used | floor_rate | ceiling_rate |
  |---|---|---|---|---|---|---|
  | R06 | 520 | 1.7596153846153846 | 1.1112942020979062 | 6 | 0.5788461538461539 | 0.0 |
  | R17 | 52 | 2.076923076923077 | 1.2962412303657644 | 5 | 0.4807692307692308 | 0.0 |
  | R01 | 1174 | 2.163543441226576 | 1.0217580336635101 | 6 | 0.2870528109028961 | 0.0 |
  | R14 | 259 | 2.22007722007722 | 1.3589433857953366 | 7 | 0.40540540540540543 | 0.007722007722007722 |
  | R11 | 369 | 2.3333333333333335 | 1.396813143022981 | 7 | 0.34417344173441733 | 0.0027100271002710027 |
  | R07 | 547 | 2.4040219378427787 | 1.4062336050240025 | 7 | 0.33455210237659966 | 0.003656307129798903 |
  | R05 | 633 | 2.7156398104265405 | 1.554299450379687 | 7 | 0.25118483412322273 | 0.018957345971563982 |
  | R03 | 720 | 2.75 | 1.4018664292279717 | 6 | 0.22361111111111112 | 0.0 |
  | R04 | 620 | 2.8209677419354837 | 1.6282677690955334 | 7 | 0.2645161290322581 | 0.008064516129032258 |
  | R10 | 383 | 2.9973890339425586 | 1.3114451772637832 | 7 | 0.06527415143603134 | 0.005221932114882507 |
  | R22 | 2 | 3.0 | 1.4142135623730951 | 2 | 0.0 | 0.0 |
  | R08 | 522 | 3.0 | 1.545223586055465 | 7 | 0.19348659003831417 | 0.013409961685823755 |
  | R02 | 873 | 3.0320733104238258 | 1.8408906485558885 | 7 | 0.27605956471935855 | 0.05154639175257732 |
  | R21 | 9 | 3.111111111111111 | 1.3642254619787417 | 5 | 0.1111111111111111 | 0.0 |
  | R12 | 264 | 3.359848484848485 | 1.1516468517963518 | 7 | 0.041666666666666664 | 0.003787878787878788 |
  | R16 | 52 | 3.4423076923076925 | 1.589345179483523 | 7 | 0.07692307692307693 | 0.057692307692307696 |
  | R20 | 13 | 3.4615384615384617 | 1.8980421761815784 | 5 | 0.3076923076923077 | 0.0 |
  | R15 | 73 | 3.4657534246575343 | 1.7003446691514401 | 7 | 0.0958904109589041 | 0.0273972602739726 |
  | R09 | 400 | 3.6425 | 1.8187808166867907 | 7 | 0.1575 | 0.055 |
  | R19 | 50 | 3.68 | 1.9529151417868644 | 7 | 0.2 | 0.08 |
  | R13 | 254 | 3.6811023622047245 | 1.1161220472077293 | 7 | 0.015748031496062992 | 0.003937007874015748 |
  | R18 | 55 | 3.8363636363636364 | 1.2585064099313852 | 6 | 0.01818181818181818 | 0.0 |

  The CSV also has median, iqr, entropy, extreme_category_rate and central_category_rate.
- **Direction/comparison:** R06 has the highest floor rate (0.5788461538461539). Five raters have a ceiling rate of 0.0.
- **Caveats in data:** R22 (n = 2), R21 (n = 9) and R20 (n = 13) are based on very few ratings.

### F0.9 Temporal drift (descriptive)
- **Finding:** Among the 20 raters with at least 10 ratings, 3 have an absolute Spearman correlation between rating and rating order greater than .2.
- **Linked object:** none. Cell `4e8b9214` has no label.
- **Numbers:**
  - TAB `overview_drift_correlation_by_rater.csv`: R01 -0.3001559154879249; R09 -0.3677232235594994; R12 0.20248946268481147 (the three with |ρ| > .2). R21 and R22 are empty (fewer than 10 ratings).
  - 01 `4e8b9214`: count 20, mean 0.004941, std 0.144250, min -0.367723, 25% -0.041215, 50% 0.017249, 75% 0.114406, max 0.202489.
- **Direction/comparison:** R01 and R09 are negative; R12 is positive.
- **Caveats in data:** No p-values or CIs are reported.

### F0.10 Rater assignment vs. action type
- **Finding:** A chi-square test of the rater × StatsBomb action type table gives chi2 = 1260.2, df = 210, p = 3.618e-149 and Cramer's V = 0.127. 49% of cells have an expected count below 5.
- **Linked object:** none. Cell `976a6f9b` has no label. TAB `rater_by_action_type_contingency.csv` holds counts; the notebook displays row percentages.
- **Numbers:** as printed in 01, cell `976a6f9b`, which notes that the chi-square approximation "is rough when this share is large".
- **Direction/comparison:** Row percentages differ between raters. Examples: Pass ranges from 46.5 (R13) to 77.8 (R21). Clearance, Dispossessed, Interception and Error are 0.0 for many raters.
- **Caveats in data:** 49% of cells have expected counts below 5.

---

## B. Model specification and estimation (02d)

### F1.0a Model and priors (as specified in the code and markdown)
- **Linear predictor:** η_ij = a_j·θ_i + λ_j; Pr(Y_ij ≤ k) = logit⁻¹(τ_k − η_ij), using OrderedLogistic with 6 shared cutpoints (cell `cd9b2c8a`, markdown `949e9c7b`).
- **θ:** θ_i ~ N(0, 1); the scale is fixed.
- **Leniency:** λ_j ~ ZeroSumNormal(σ_λ), so it is relative to the average rater, and a higher value means more lenient. Prior σ_λ ~ Exp(1).
- **Discrimination:** log a_j = mu_log_a + log_a_raw·sigma_log_a, with log_a_raw ~ N(0, 1) (non-centred). Priors: mu_log_a ~ N(0, 1); sigma_log_a ~ Exp(2).
- **Cutpoints:** τ ~ N(linspace(−2.5, 2.5, 6), 1.5) with an ordered transform.
- **Equal-discrimination model:** built by the same function with `equal_discrimination=True`, so log a_j = mu_log_a for every rater and sigma_log_a is absent. Everything else is identical.
- **Thresholds:** shared across raters. The notebook states that rater-specific thresholds b_jk were not estimated, so a common category structure is assumed and not tested (markdown `82dc7ee7`, `949e9c7b`).

### F1.0b Sampler settings and software
- **Sampler:**
  - Cell `d37d444b`: "Sampler: 4 chains x 2000 draws after 2000 tuning steps, target_accept = 0.95"
  - PyMC log: "Sampling 4 chains for 2_000 tune and 2_000 draw iterations (8_000 + 8_000 draws total) took 511 seconds."
  - "Initializing NUTS using jitter+adapt_diag…"
  - NUTS sampled: [theta, sigma_lambda, leniency, mu_log_a, sigma_log_a, log_a_raw, cutpoints]
  - Equal-discrimination model (cell `e6164b08`): same settings, "took 283 seconds"; NUTS sampled [theta, sigma_lambda, leniency, mu_log_a, cutpoints]
  - TAB `model_diagnostics_jrt.csv`: n_draws_per_chain 2000.0, n_tune 2000.0, n_chains 4.0
- **Software and run details:**
  - Seed: 20260713 (cell `46f1cec5`; LOG `session_info_jrt.json`)
  - Package versions (cell `5c952e6d` / LOG `session_info_jrt.json`): numpy 2.4.6, pandas 3.0.3, scipy 1.18.0, matplotlib 3.11.0, networkx 3.6.1, pymc 6.1.0, arviz 1.2.0
  - Python "3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]"; platform "Linux-6.8.0-134-generic-x86_64-with-glibc2.39"; git_commit "not available"
  - Run log LOG `02d_server_run_20261021_070336.log`: wall clock 17:49.66, exit status 0
- **Caveats:**
  - 02d ran on a different machine (project root printed as `/home/mklemp/jrt`).
  - 00 and 01 use a kernel with Python 3.12.9 (notebook metadata); their package versions are not printed.
  - The pytensor version is not printed.

### F1.1 Convergence of the JRT model (by parameter group)
- **Finding:** There were 0 divergences. The largest split R-hat across all groups is 1.004775. The smallest bulk ESS is 2014.040992 and the smallest tail ESS is 3033.626914 (both for the hyperparameters).
- **Linked object:** `tbl-jrt-convergence` (cell `c82c7804`); `fig-jrt-traceplots` (cell `jrttrc01`)
- **Numbers** (TAB `jrt_convergence_by_group.csv`):

  | parameter_group | n_parameters | max_r_hat | min_ess_bulk | min_ess_tail |
  |---|---|---|---|---|
  | action creativity (theta) | 3669 | 1.004775 | 14092.959882 | 4132.096533 |
  | rater leniency (lambda_j) | 22 | 1.000823 | 4171.44245 | 5636.115711 |
  | rater discrimination (a_j) | 22 | 1.002028 | 2940.414765 | 4457.720773 |
  | thresholds (tau_k) | 6 | 1.001618 | 3445.797577 | 4534.336847 |
  | hyperparameters | 3 | 1.001461 | 2014.040992 | 3033.626914 |

  - Cell `c82c7804` prints: "Divergences: 0, max R-hat: 1.0048, min bulk ESS: 2014, min tail ESS: 3034"
  - TAB `model_diagnostics_jrt.csv`: max_rhat 1.004775, n_divergences 0.0, min_ess_bulk 2014.040992, min_ess_tail 3033.626914
- **Direction/comparison:** All groups meet the notebook's stated criteria (R-hat < 1.01, bulk and tail ESS > 400, no divergences). No convergence warning was logged: `warnings_log_jrt.csv` has 0 rows, and cell `13be8b84` prints "0 warnings collected in this notebook."
- **Caveats in data:** The trace plots are visual only and NOT QUOTABLE.

### F1.2 Convergence of the equal-discrimination model
- **Finding:** There were 0 divergences, the largest R-hat is 1.003762, and the smallest ESS is 1552.024542.
- **Linked object:** none. The CSV is written in cell `e6164b08`.
- **Numbers** (TAB `jrt_equal_discrimination_convergence.csv`):

  | group | n | max_r_hat | min_ess_bulk | min_ess_tail |
  |---|---|---|---|---|
  | theta | 3669 | 1.003762 | 8146.007755 | 4222.082082 |
  | lambda_j | 22 | 1.001716 | 2894.219418 | 4722.70033 |
  | a_j | 22 | 1.002012 | 1552.024542 | 2584.005322 |
  | tau_k | 6 | 1.001538 | 1951.303349 | 3199.177386 |
  | hyperparameters | 2 | 1.002012 | 1552.024542 | 2584.005322 |

  - Cell `e6164b08` prints: "Equal-discrimination model: divergences 0, max R-hat 1.0038, min ESS 1552"
  - TAB `model_diagnostics_jrt.csv`: max_rhat_equal_discrimination 1.003762, n_divergences_equal_discrimination 0.0
- **Direction/comparison:** —
- **Caveats in data:** The a_j group lists 22 parameters, but they are all the same value, exp(mu_log_a). That is why its ESS equals the hyperparameter group's (sigma_lambda, mu_log_a).

### F1.3 Thresholds and hyperparameters
- **Finding:** The posterior means of the six shared cutpoints rise from -2.25336 to 6.441121. Posterior means: sigma_lambda = 1.232476, mu_log_a = 0.622311, sigma_log_a = 0.388639.
- **Linked object:** `tbl-jrt-model-summary` (cell `jrtsum01`)
- **Numbers** (TAB `jrt_model_summary.csv`; **89% equal-tailed intervals**):

  | parameter | mean | sd | eti89_lb | eti89_ub | ess_bulk | ess_tail | r_hat |
  |---|---|---|---|---|---|---|---|
  | cutpoints[0] | -2.25336 | 0.087836 | -2.393261 | -2.114741 | 3445.797577 | 4534.336847 | 1.001618 |
  | cutpoints[1] | -0.200214 | 0.082279 | -0.33365 | -0.069299 | 3532.699459 | 4958.535732 | 1.001511 |
  | cutpoints[2] | 1.2307 | 0.083471 | 1.09796 | 1.364848 | 3919.306183 | 5365.775528 | 1.001455 |
  | cutpoints[3] | 2.579319 | 0.089684 | 2.437743 | 2.722816 | 4188.749061 | 5457.528095 | 1.00121 |
  | cutpoints[4] | 4.253115 | 0.108634 | 4.081734 | 4.427186 | 4901.381096 | 5413.471024 | 1.001409 |
  | cutpoints[5] | 6.441121 | 0.166129 | 6.177749 | 6.712673 | 6407.521589 | 5666.343358 | 1.000734 |
  | sigma_lambda | 1.232476 | 0.198034 | 0.956799 | 1.583755 | 13678.210075 | 5966.578547 | 0.999898 |
  | mu_log_a | 0.622311 | 0.09191 | 0.473327 | 0.765465 | 2014.040992 | 3033.626914 | 1.001461 |
  | sigma_log_a | 0.388639 | 0.077641 | 0.281909 | 0.521657 | 3070.046766 | 4007.828014 | 1.000855 |

  The CSV also has mcse_mean and mcse_sd.
- **Threshold gaps** (differences between consecutive posterior-mean cutpoints; TAB `jrt_derived_counts.csv`): threshold_gap_1_2 2.0531452144114093; threshold_gap_2_3 1.4309147172774972; threshold_gap_3_4 1.3486183730574282; threshold_gap_4_5 1.6737964330037762; threshold_gap_5_6 2.188005717864627.
  - The cell `jrtder01` display rounds these to 6 decimals (e.g. 2.053145).
- **Direction/comparison:**
  - The 89% interval for sigma_log_a (0.281909 to 0.521657) does not include 0.
  - The smallest gap is between cutpoints 3 and 4; the largest is between cutpoints 5 and 6.
- **Caveats in data:**
  - This table uses 89% intervals, while the rater table (F2.1) uses 95% intervals.
  - The gap labels "k_(k+1)" index cutpoints, not rating categories.

### F1.4 Posterior predictive check
- **Finding:** All 7 observed category shares and all 22 observed rater means fall inside the 95% posterior predictive intervals.
- **Linked object:** `fig-jrt-ppc` (cell `jrtppc01`)
- **Numbers:**
  - Cell `jrtppc01` prints: "Categories with observed share inside the 95% PI: 7 of 7" and "Raters with observed mean inside the 95% PI: 22 of 22"
  - TAB `jrt_ppc_category_shares.csv`:

    | category | observed_share | predicted_share_mean | lower | upper |
    |---|---|---|---|---|
    | 1 | 0.2593064762876084 | 0.25912624298827164 | 0.2491012238653748 | 0.2707865884752677 |
    | 2 | 0.26976032636409997 | 0.2679877932177459 | 0.25470741968383476 | 0.28136155022947473 |
    | 3 | 0.18753187149413564 | 0.1875616713411526 | 0.1755481896991331 | 0.19926695563488017 |
    | 4 | 0.13322284548699642 | 0.1331906552779195 | 0.1236613972463029 | 0.14253250892401834 |
    | 5 | 0.09280979092299847 | 0.09327447730749623 | 0.08477498725140234 | 0.10173699643039266 |
    | 6 | 0.043472718001019886 | 0.04471411269760331 | 0.03926568077511474 | 0.051252549719530846 |
    | 7 | 0.013895971443141255 | 0.014145047169811322 | 0.011218765935747067 | 0.01721060683324834 |

  - TAB `jrt_ppc_rater_means.csv`: observed_within_95pi is True for all 22 raters. The widest intervals are for R22 (observed 3.0; predicted median 3.5; PI 1.5 to 5.5) and R21 (observed 3.111111111111111; PI 2.2222222222222223 to 4.111111111111111).
- **Direction/comparison:** —
- **Caveats in data:**
  - Replicates are drawn from every 10th posterior draw; the number of replicated datasets is not printed.
  - The check covers only category shares (pooled) and rater means. No per-rater category distributions or action-level checks are reported.

---

## C. RQ1: Rater leniency and discrimination (02d)

### F2.1 Per-rater posterior summaries
- **Finding:** Posterior mean discrimination ranges from 0.9569497104368692 (R18) to 3.2408227509685186 (R02), with a median of 2.0844708365638205. Posterior mean leniency ranges from -2.9279955470625105 (R06) to 1.6348645170687754 (R18).
- **Linked object:** `tbl-jrt-rater-parameters` (cell `jrtrat01`); `fig-jrt-rater-parameters` (cell `jrtfig01`)
- **Numbers** (TAB `jrt_rater_table.csv`; 95% intervals from the 2.5th and 97.5th posterior percentiles; columns ending "_se" are posterior SDs):

  | rater | n | a_j | a_lower | a_upper | a_sd | λ_j | λ_lower | λ_upper | λ_sd | (log a_j − mu_log_a) lower | upper |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | R01 | 1174 | 1.269696468625329 | 1.1258365005238367 | 1.419511835926998 | 0.07514216475370604 | -1.1344086055290186 | -1.3188046659895265 | -0.94993881069088 | 0.09484790584876884 | -0.5887920619179854 | -0.17598259660607984 |
  | R02 | 873 | 3.2408227509685186 | 2.9638001626558363 | 3.537435137027491 | 0.1464688918490874 | -0.0888796677391232 | -0.33343989056280554 | 0.15921598094536116 | 0.1269154614532911 | 0.36345963890894595 | 0.7529634404869995 |
  | R03 | 720 | 1.9070836978009615 | 1.6896776583343285 | 2.128183636707161 | 0.11103494598437515 | -0.05112535720348414 | -0.263854492399532 | 0.16229839067979326 | 0.1076034226496092 | -0.18028962743952065 | 0.23190317276261352 |
  | R04 | 620 | 2.4217697430340066 | 2.1725044790627894 | 2.6798508621906234 | 0.130287145138922 | -0.43057993310279624 | -0.6762559946973482 | -0.18923251188427218 | 0.12470811202524328 | 0.06525152766236769 | 0.4716620347241151 |
  | R05 | 633 | 2.3233000491144504 | 2.0837820352316747 | 2.5790758139927146 | 0.125539520176109 | -0.38293935411639896 | -0.6097297897264637 | -0.1533526373785844 | 0.11781322373089288 | 0.024580933083274623 | 0.41892987137553955 |
  | R06 | 520 | 2.570026657117077 | 2.202244881553404 | 2.961305550607863 | 0.19206320389056183 | -2.9279955470625105 | -3.2808028219761503 | -2.600388639296773 | 0.17316116480680355 | 0.09500765712286645 | 0.5469796415772266 |
  | R07 | 547 | 2.133683556029969 | 1.8803276793385129 | 2.40659129335491 | 0.13252888913380548 | -0.9563061373553541 | -1.1908430527258098 | -0.733514983981121 | 0.11769923871455354 | -0.06887666961876424 | 0.3446341607911947 |
  | R08 | 522 | 2.118730061238317 | 1.8733886253039729 | 2.3723434496404323 | 0.12704518302358744 | 0.3058300750049105 | 0.06149352796513383 | 0.5421823032347299 | 0.12197106992326814 | -0.07216987175511033 | 0.33636601548360956 |
  | R09 | 400 | 2.333783886519116 | 2.0104944698446565 | 2.6685362414428666 | 0.16877460237091968 | 1.3233749706607214 | 1.0524444128622377 | 1.596528575514195 | 0.13873209721408863 | 0.0011793909140565882 | 0.4380141313342333 |
  | R10 | 383 | 1.4303046882203136 | 1.1911925594701722 | 1.6725780246258664 | 0.12241806434254335 | 0.4766318227469328 | 0.2318822181440953 | 0.724723534189398 | 0.12657585480024436 | -0.5058292505041089 | -0.042746970296267624 |
  | R11 | 369 | 2.0170635705788564 | 1.730386169342869 | 2.3256353491435338 | 0.15302340004228634 | -1.053158559469446 | -1.3165837667347446 | -0.7947446750252091 | 0.13303177912518724 | -0.1377815811236344 | 0.3047224158313658 |
  | R12 | 264 | 1.118046344894942 | 0.8673942376207372 | 1.3729601632050448 | 0.1297225180917946 | 0.9677773067425324 | 0.7081136906707358 | 1.2271492003439508 | 0.13369553723802605 | -0.7900443670352918 | -0.25452544787869574 |
  | R13 | 254 | 0.9635205216640959 | 0.7145273922210039 | 1.2167762409217735 | 0.1274875876542293 | 1.4307624155883651 | 1.1657684779085955 | 1.6870648697265154 | 0.13174940258893197 | -0.9898261266669703 | -0.3915290360264783 |
  | R14 | 259 | 2.300289520701491 | 1.8912868847540307 | 2.7526393009513312 | 0.2172304102047308 | -1.6316493992198928 | -1.9914560577598677 | -1.2915589066178308 | 0.17833678427130462 | -0.04092208859932166 | 0.4588970245918969 |
  | R15 | 73 | 2.1919060283580563 | 1.7150013841004481 | 2.7326637875224504 | 0.2583647600295441 | 0.9274493421644872 | 0.4656027399449838 | 1.3862289889717387 | 0.23296680093496377 | -0.11947714989778198 | 0.4398878591095988 |
  | R16 | 52 | 2.1039464670850787 | 1.5396934761406924 | 2.735323399277244 | 0.3024742831102001 | 0.5567676733512825 | -0.010569420078448084 | 1.1167554940249205 | 0.2847492502831985 | -0.21470786616944162 | 0.4320281309989416 |
  | R17 | 52 | 2.0244749103816244 | 1.3121460349324479 | 2.84837285253876 | 0.38957466393177187 | -1.3037849231909602 | -1.910712776959916 | -0.7054323785922881 | 0.30546520639608277 | -0.3542300062001244 | 0.4540952705887118 |
  | R18 | 55 | 0.9569497104368692 | 0.5800183119166565 | 1.3749172709075008 | 0.20446437551491795 | 1.6348645170687754 | 1.1560423025440825 | 2.10929354305191 | 0.2441723749490766 | -1.1653708368888764 | -0.300932486542151 |
  | R19 | 50 | 3.089340688049874 | 2.2613298636072496 | 4.117683950529345 | 0.46820248032148754 | 1.2823409043854967 | 0.5169191794343682 | 2.020568919254121 | 0.379494003040306 | 0.17071087193175055 | 0.8307246207113586 |
  | R20 | 13 | 2.064995206042562 | 1.0943348015222152 | 3.365693695674406 | 0.5798476500178956 | 0.7823928916828852 | -0.31490491361654854 | 1.8397166061934584 | 0.555397326836808 | -0.5330603399200403 | 0.5960595718462975 |
  | R21 | 9 | 1.5070949565380631 | 0.6855452653201803 | 2.6185005395150944 | 0.49999548951006645 | 0.5126750314037867 | -0.6335506677015598 | 1.6547087242690253 | 0.5827299092262829 | -0.9852921535163875 | 0.3341029479655384 |
  | R22 | 2 | 1.7668595253527435 | 0.7445925072535199 | 3.3512128198377367 | 0.6786987089652162 | -0.2400394668111801 | -2.051858396403093 | 1.5922548547304833 | 0.9263163414831131 | -0.884070845315405 | 0.5796922413463762 |

  - Cell `jrtrat01` prints: "Discrimination: median=2.08, range=[0.96, 3.24], pool exp(mu_log_a) = 1.87"; "Raters with noticeably low discrimination (< 0.5): 0"; "Leniency: range=[-2.93, 1.63]"
  - TAB `model_diagnostics_jrt.csv`: median_discrimination 2.0844708365638205; min_discrimination 0.9569497104368692; max_discrimination 3.2408227509685186; n_raters_discrimination_lt_0.5 0.0
  - TAB `jrt_derived_counts.csv`: ratio_max_min_discrimination 3.3866176201558282
  - `raters_jrt.csv` is a copy of `jrt_rater_table.csv` (cell `0bd4a3e7`: `raters_jrt = jrt_rater_table.copy()`).
- **Direction/comparison:** R06 has the lowest leniency and R18 the highest. R02 has the highest discrimination and R18 the lowest.
- **Caveats in data:**
  - Posterior SDs of a_j are largest for the raters with few ratings: R22 0.6786987089652162 (n = 2), R20 0.5798476500178956 (n = 13), R21 0.49999548951006645 (n = 9).
  - The leniency intervals for R20, R21 and R22 span 0.

### F2.2 Pool discrimination and CI-exclusion counts
- **Finding:** The pool discrimination exp(mu_log_a) (posterior median) is 1.8680804941316524. For 11 of 22 raters, the 95% interval of log a_j − mu_log_a excludes 0: 6 above and 5 below.
- **Linked object:** `tbl-jrt-derived-counts` (cell `jrtder01`); `fig-jrt-rater-parameters`
- **Numbers** (TAB `jrt_derived_counts.csv`): n_raters 22.0; pool_discrimination_exp_mu_log_a 1.8680804941316524; n_raters_discrimination_ci_excludes_pool 11.0; n_raters_discrimination_ci_above_pool 6.0; n_raters_discrimination_ci_below_pool 5.0; n_raters_discrimination_lt_0.5 0.0.
  - From the F2.1 columns: above pool are R02, R04, R05, R06, R09 and R19; below pool are R01, R10, R12, R13 and R18.
- **Direction/comparison:** —
- **Caveats in data:**
  - See X4. The count is based on the joint-posterior difference log a_j − mu_log_a, not on the marginal a_j interval compared with the point value 1.868….
  - R09's lower bound is 0.0011793909140565882, very close to 0.

### F2.3 Leniency CI-exclusion counts
- **Finding:** For 16 of 22 raters the 95% leniency interval excludes 0: 8 above (more lenient than the average rater) and 8 below.
- **Linked object:** `tbl-jrt-derived-counts`; `fig-jrt-rater-parameters` (panel B)
- **Numbers** (TAB `jrt_derived_counts.csv`): n_raters_leniency_ci_excludes_0 16.0; n_raters_leniency_ci_above_0 8.0; n_raters_leniency_ci_below_0 8.0. The hyperparameter σ_λ is 1.232476 (89% ETI 0.956799 to 1.583755; F1.3).
  - From F2.1: above 0 are R08, R09, R10, R12, R13, R15, R18 and R19; below 0 are R01, R04, R05, R06, R07, R11, R14 and R17.
  - Intervals that include 0: R02, R03, R16, R20, R21, R22. R16's lower bound is -0.010569420078448084.
- **Direction/comparison:** —
- **Caveats in data:** λ_j is relative to the average rater (sum-to-zero), not to an absolute zero.

### F2.4 mu_log_a and sigma_log_a
- **Finding:** mu_log_a = 0.622311 (SD 0.09191; 89% ETI 0.473327 to 0.765465). sigma_log_a = 0.388639 (SD 0.077641; 89% ETI 0.281909 to 0.521657).
- **Linked object:** `tbl-jrt-model-summary`
- **Numbers:** see F1.3 (TAB `jrt_model_summary.csv`).
- **Caveats in data:** No 95% interval is reported for these hyperparameters.

### F2.5 Information by rater
- **Finding:** Peak Fisher information per rater ranges from 0.28630034428415285 (R18) to 3.2836317353059203 (R02). The mean information per rating across the pool peaks at 1.3335752264232335, at θ = 0.7400000000000002.
- **Linked object:** `fig-jrt-category-curves-information` (cell `015e75b6`; shows the lowest-, median- and highest-discrimination raters); `fig-jrt-information-reliability` panel A (cell `e72f0b74`)
- **Numbers** (TAB `jrt_information_by_rater.csv`):

  | rater | peak_information | theta_at_peak | information_at_theta_0 |
  |---|---|---|---|
  | R01 | 0.5040152755083486 | 2.1000000000000005 | 0.4687586696606736 |
  | R02 | 3.2836317353059203 | 0.5 | 3.198120526838502 |
  | R03 | 1.137057547969611 | 0.8200000000000003 | 1.1090225374187277 |
  | R04 | 1.833613399563553 | 0.7999999999999998 | 1.7594600265577751 |
  | R05 | 1.6875411320720524 | 0.8200000000000003 | 1.622944795018714 |
  | R06 | 2.064991445924355 | 1.7400000000000002 | 1.514807947705219 |
  | R07 | 1.4233233347684902 | 1.1600000000000001 | 1.3326675415245148 |
  | R08 | 1.4034438105308455 | 0.5800000000000001 | 1.3838626883372405 |
  | R09 | 1.7028008611643537 | 0.08000000000000007 | 1.7021501779551456 |
  | R10 | 0.6395888420293675 | 0.7400000000000002 | 0.6330680286829592 |
  | R11 | 1.2719882325386491 | 1.2800000000000002 | 1.1864653436801305 |
  | R12 | 0.3908080697255438 | 0.5 | 0.38967461200325915 |
  | R13 | 0.2902457386896657 | 0.09999999999999964 | 0.2902205261235731 |
  | R14 | 1.6542766138955347 | 1.38 | 1.5145655259210038 |
  | R15 | 1.5020595664634513 | 0.28000000000000025 | 1.4970583691912196 |
  | R16 | 1.383927158796656 | 0.45999999999999996 | 1.3719158148408355 |
  | R17 | 1.2813527479970623 | 1.4000000000000004 | 1.1852763253677954 |
  | R18 | 0.28630034428415285 | -0.1200000000000001 | 0.28627152377859316 |
  | R19 | 2.9838399679662384 | 0.08000000000000007 | 2.9821813507814103 |
  | R20 | 1.3331591214207559 | 0.3600000000000003 | 1.326333108908393 |
  | R21 | 0.7101087085473853 | 0.6799999999999997 | 0.7033661858654757 |
  | R22 | 0.975995814244952 | 1.0 | 0.9447240797016305 |

  - TAB `jrt_derived_counts.csv`: theta_pool_mean_information_peak 0.7400000000000002; pool_mean_information_peak 1.3335752264232335
- **Direction/comparison:** Raters with lower leniency tend to have their information peak at higher θ (e.g. R06, λ = -2.928…, peaks at θ = 1.74…; R01 at 2.10…). This is a purely descriptive pairing of the table columns.
- **Caveats in data:**
  - Information is computed by plugging in the posterior means of a_j, λ_j and τ_k. It is not averaged over the posterior, and no uncertainty is given.
  - The θ grid is linspace(−4, 4, 401), a step of 0.02, so theta_at_peak is grid-resolved.
  - The pool-sum information curve in fig-jrt-information-reliability (A) is plot-only and NOT QUOTABLE.

### F2.6 PSIS-LOO: rater-specific vs. equal discrimination
- **Finding:** The JRT model with rater-specific discrimination has higher elpd_loo than the equal-discrimination model, by elpd_diff = 163.25478584290235 (SE 19.684919284549657).
- **Linked object:** `tbl-jrt-equal-discrimination-loo` (cell `e6164b08`)
- **Numbers** (TAB `jrt_loo_comparison.csv`):

  | model | elpd_loo | se | p_loo | elpd_diff_vs_equal | se_diff_vs_equal | share_pareto_k_gt_0.7 |
  |---|---|---|---|---|---|---|
  | JRT, equal discrimination (a_j = a) | -11701.18535331233 | 62.843364716277925 | 2375.8767147154235 | 0.0 | 0.0 | 0.0014023457419683834 |
  | JRT, rater-specific discrimination (a_j) | -11537.930567469428 | 65.51659122461588 | 2573.6857918258565 | 163.25478584290235 | 19.684919284549657 | 0.02804691483936767 |

  - Cell `e6164b08` prints: "elpd_diff (rater-specific - equal discrimination) = 163.3, SE = 19.7, ratio = 8.3"
  - TAB `model_diagnostics_jrt.csv`: elpd_diff_rater_specific_minus_equal 163.25478584290235; elpd_diff_se 19.684919284549657
  - SE of the difference = sqrt(N·var(pointwise diff)) (code in `e6164b08`).
- **Direction/comparison:** elpd_diff is positive, in favour of rater-specific discrimination. The ratio of difference to SE is printed as 8.3.
- **Caveats in data:**
  - ArviZ printed "UserWarning: Estimated shape parameter of Pareto distribution is greater than 0.70 for one or more samples…" twice, once for each model's `az.loo`.
  - The share of observations with k > 0.7 is 0.02804691483936767 for the rater-specific model and 0.0014023457419683834 for the equal model. Both are below the notebook's 5% logging threshold, so no entry was made in `warnings_log_jrt.csv` (see X5).
  - p_loo is 2573.6857918258565 and 2375.8767147154235 (as printed).
  - Not present in notebook: the count of observations with k > 0.7, the maximum k, the share with k > 1, and any moment-matching or k-fold re-check.

---

## D. RQ2: Reliability and precision of JRT scores (02d)

### F3.1 Empirical and marginal reliability at the realised panel size
- **Finding:** Empirical reliability of the JRT scores is 0.6603541094329908. Marginal reliability at the realised harmonic-mean panel size (k = 1.726320341325184) is 0.6462162523422212.
- **Linked object:** `fig-jrt-information-reliability` (cell `e72f0b74`); `tbl-jrt-d-study` (cell `jrtdst01`)
- **Numbers:**
  - TAB `model_diagnostics_jrt.csv`: empirical_reliability 0.6603541094329908; k_harmonic 1.726320341325184; marginal_reliability_k_harmonic 0.6462162523422212; marginal_reliability_k1 0.514110299035415
  - Cell `e72f0b74` prints: "Empirical reliability of the JRT scores: 0.660" and "Marginal reliability at the harmonic-mean k = 1.73: 0.646"
- **Definitions** (markdown `0c06a846` / code):
  - Empirical reliability = Var(θ̂) / [Var(θ̂) + mean(PSD²)], where θ̂ is the posterior mean and PSD the posterior SD.
  - Marginal reliability = 1 / (1 + ∫φ(θ)·[k·Ī(θ)]⁻¹ dθ), where Ī is the mean plug-in information across the 22 raters.
- **Direction/comparison:** Empirical reliability (0.6603541094329908) is slightly higher than marginal reliability at the harmonic-mean k (0.6462162523422212). They are different quantities.
- **Caveats in data:**
  - No interval or uncertainty is reported for either reliability.
  - The marginal-reliability calculation assumes the k judges are drawn at random from the pool (equal weights on the 22 raters' information). It does not weight raters by their actual rating volume.

### F3.2 Score distribution
- **Finding:** Across the 3669 actions, the posterior-mean scores have SD 0.813 and range from -2.08 to 3.08 (as printed).
- **Linked object:** none (printed in cell `jrtprc01`)
- **Numbers:** "Score posterior mean: SD across actions = 0.813, range = [-2.08, 3.08]" (cell `jrtprc01`). The unrounded per-action values are in TAB `scores_jrt.csv` (3669 rows; columns score, score_se, score_lower, score_upper). No summary row of unrounded values is exported.
- **Caveats in data:** Only rounded summary values are printed. `scores_jrt.csv` has no missing scores (all actions are in component 0).

### F3.3 Score precision by number of ratings
- **Finding:** The mean posterior SD of θ falls from 0.6506952848078058 (1 rating) to 0.39954470672839787 (5 or more ratings).
- **Linked object:** `tbl-jrt-score-precision` (cell `jrtprc01`)
- **Numbers** (TAB `jrt_score_precision_by_n.csv`):

  | n_ratings_group | n_actions | mean_posterior_sd | min_posterior_sd | max_posterior_sd | mean_ci_width (95%) |
  |---|---|---|---|---|---|
  | 1 | 898 | 0.6506952848078058 | 0.45614653160094437 | 0.9481187665287324 | 2.575876218002324 |
  | 2 | 2080 | 0.5723633427808366 | 0.37075073911556555 | 0.8626656522178957 | 2.256522675935757 |
  | 3 | 357 | 0.5034461065328978 | 0.3534250425802517 | 0.7165808489912396 | 1.982428654699967 |
  | 4 | 123 | 0.44428518728731153 | 0.3324244072869472 | 0.6971813824216273 | 1.747768127410395 |
  | 5+ | 211 | 0.39954470672839787 | 0.2583077103873673 | 0.5839340307616312 | 1.5694773558748427 |

- **Direction/comparison:** Mean posterior SD and mean interval width both decrease monotonically as the number of ratings increases.
- **Caveats in data:**
  - The min–max ranges overlap heavily between groups. For example, the maximum SD for 2 ratings (0.8626656522178957) is above the minimum SD for 1 rating (0.45614653160094437).
  - The group counts add up to 3669 and match F0.4.

### F3.4 D-study: marginal reliability by number of judges
- **Finding:** Marginal reliability rises from 0.514110299035415 at k = 1 to 0.91365019867287 at k = 10.
- **Linked object:** `tbl-jrt-d-study` (cell `jrtdst01`); `fig-jrt-information-reliability` panel B
- **Numbers** (TAB `jrt_marginal_reliability.csv`):

  | k | marginal_reliability |
  |---|---|
  | 1 | 0.514110299035415 |
  | 2 | 0.6790922687243275 |
  | 3 | 0.7604354765814204 |
  | 4 | 0.8088802281726432 |
  | 5 | 0.8410276299187582 |
  | 6 | 0.8639174643970545 |
  | 7 | 0.8810453042518633 |
  | 8 | 0.8943436006150454 |
  | 9 | 0.9049675576934999 |
  | 10 | 0.91365019867287 |
  | 1.726320341325184 (harmonic mean, realised) | 0.6462162523422212 |

  The cell `jrtdst01` display is rounded to 3 decimals (0.514, 0.679, 0.760, 0.809, 0.841, 0.864, 0.881, 0.894, 0.905, 0.914, 0.646).
- **Direction/comparison:**
  - The increase from k = 1 to k = 2 is the largest of any one-step increase.
  - Values at or above .80 start at k = 4 (0.8088802281726432). Values at or above .90 start at k = 9 (0.9049675576934999).
- **Caveats in data:** These are model-based projections (same assumptions as F3.1), with no uncertainty bands.

---

## E. Internal inconsistencies and flags

- **X1. `02_artifacts.md` is out of date with the re-run notebooks.**
  - It says "no cell in any of the three notebooks is labelled yet". The notebooks now carry labels:
    - 00: `tbl-cleaning-log`
    - 01: `tbl-overview-ratings-per-action`, `fig-overview-rater-overlap`, `fig-overview-rating-distribution`, `fig-overview-rater-response-styles`, `fig-overview-degree-distributions`
    - 02d: `tbl-jrt-convergence`, `tbl-jrt-model-summary`, `tbl-jrt-rater-parameters`, `fig-jrt-rater-parameters`, `fig-jrt-traceplots`, `fig-jrt-ppc`, `tbl-jrt-equal-discrimination-loo`, `fig-jrt-category-curves-information`, `fig-jrt-information-reliability`, `tbl-jrt-d-study`, `tbl-jrt-score-precision`, `tbl-jrt-derived-counts`
  - Several of these differ from the labels proposed in 02_artifacts (e.g. `fig-rating-distribution` → `fig-overview-rating-distribution`; `fig-jrt-category-information` → `fig-jrt-category-curves-information`; `tbl-jrt-marginal-reliability` → `tbl-jrt-d-study`).
  - 02_artifacts P3 (LOO depends on 02c) and P10 (duplicated cleaning-log row) no longer apply. The equal-discrimination model is now fitted inside 02d, and the cleaning log has 5 unique rows.
  - 02_artifacts still uses "severity". The CSVs and labels now use "leniency".
  - P12 ("no JRT discrimination figure") is also obsolete: `fig-jrt-rater-parameters` now exists.
  - The results-embedder should be re-run.
- **X2. Pseudonymisation leak in notebook output.** 00, cell `520638b8` displays `ratings_raw.head()` before pseudonymisation. Original user IDs are visible in the stored output (`urst3254`, `anma2416`, `azne2115`). Do not embed or publish this cell output as it stands.
- **X3. 23 raters before cleaning vs. 22 after.** 00 cell `fdbdb3b4` reports 23 pseudonymised raters; the cleaned data has 22. No output identifies which rater was removed or at which step.
- **X4. Two readings of "above/below the pool discrimination".**
  - The counts in F2.2 (11 = 6 + 5) use the 95% interval of log a_j − mu_log_a.
  - `fig-jrt-rater-parameters` instead shows the marginal 95% intervals of a_j against a dashed line at the point value 1.8680804941316524.
  - For R07 (a_lower 1.8803276793385129), R08 (1.8733886253039729) and R14 (1.8912868847540307), the marginal lower bound is above 1.868…, but their log-deviation intervals include 0. These three are not counted as "above pool". A reader of the figure could therefore reach a different count from the text.
- **X5. Pareto-k warnings not logged.** ArviZ emitted the k > 0.7 UserWarning for both models (cell `e6164b08` stderr). `warnings_log_jrt.csv` is empty because the notebook only logs when the share exceeds 5%.
- **X6. Stale outputs in 01.** Cells `c64ee46d` and `7bad1e05` have `execution_count: null` and empty source, but carry outputs from an earlier session (execution_count 17/18). Their values (cumulative ratings per action) coincide with cell `3b12b8bf`. Do not cite them.
- **X7. Stale aggregate warnings file.** TAB `warnings_log.csv` (not written by 00, 01 or 02d in this run) is dated 2026-10-15. It contains a JRT entry "Max R-hat = 1.0166 >= 1.01 for the JRT model." from an earlier run, which contradicts the current max R-hat of 1.004775. Do not use it.
- **X8. Rounded displays vs. CSV values.**
  - "Cleaning complete: 7858 -> 7844 rows." uses the post-exclusion base, not 9150 (F0.2).
  - "median rater (316)" vs. median_ratings_per_rater 316.5 (F0.5).
  - Rounded printouts (e.g. 0.660, 0.646, 163.3, 19.7) should be replaced by the CSV values when quoting.
- **X9. Interval widths differ between tables.** `jrt_model_summary.csv` uses 89% ETI; `jrt_rater_table.csv`, PPC, scores and score precision use 95%.
- **X10. Provenance.** 02d ran on another host (`/home/mklemp/jrt`) with git_commit "not available". 00 and 01 ran locally (Python 3.12.9 kernel) on 2026-10-20 and print no package versions.
- **X11. Out-of-scope references in in-scope notebooks.** The 00 markdown mentions 02a–02c, 03 and `02_creativity_ratings_R.qmd`. The 01 markdown (§7.3) points to `02b_linear_mixed_model.ipynb` for drift slopes. The 01 §7.2 markdown still uses "severity".

---

## Not found

These are absent from the in-scope notebook outputs. Do not invent them downstream.

- **Agreement and reliability uncertainty:** CI or bootstrap for Krippendorff's α; any rater-pair or subset α.
- **Reliability uncertainty:** posterior or bootstrap intervals for empirical reliability, marginal reliability or D-study values.
- **Classical comparisons in scope:** any ICC, G-coefficient, Spearman–Brown or MFRM separation/reliability index. These exist only in excluded outputs.
- **PSIS-LOO details:** count of observations with Pareto k > 0.7; maximum k; share with k > 1; any LOO re-check (moment matching, k-fold); LOO standard errors other than those listed in F2.6.
- **Prior checks:** prior predictive checks and prior-sensitivity analyses.
- **Model variants:** rater-specific thresholds (b_jk) or any test of the shared-threshold assumption; any rater-fit or infit/outfit statistic.
- **Other posterior summaries:** 95% intervals for the hyperparameters and thresholds (only 89% ETI is reported); E-BFMI, tree depth or step-size diagnostics; acceptance rates.
- **PPC details:** the number of posterior predictive replicates; per-rater category-share PPC; action-level PPC.
- **Information uncertainty:** uncertainty in the information functions (plug-in only); numeric values of the pool-sum information curve (plot only, NOT QUOTABLE).
- **Unrounded score summaries:** SD and range of the JRT scores across actions as unrounded exported values (printed as 0.813 and [-2.08, 3.08] only).
- **Provenance:** package versions for 00/01 (including `krippendorff`, `duckdb`, `seaborn`); the pytensor version; a git commit for the 02d run.
- **Cleaning detail:** which rater (of 23) was removed in cleaning, and in which step.
- **Sample description:** demographics or expertise of raters; how actions were assigned to raters (only the descriptive χ² in F0.10 is present).
- **Secondary dimensions:** `technical_correctness` and `aesthetic_appeal` are only shown in an unlabelled exploratory PairGrid (01, cell `a3a60c1e`). No correlation values are printed, so they are NOT QUOTABLE.
