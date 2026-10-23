# Audit of the JRT/MFRM analysis against `ANLEITUNG_JRT_Audit.md`

Branch `audit/jrt-spec`. Started 2026-10-22. The spec is `../../ANLEITUNG_JRT_Audit.md`
(German); this audit and all new code are in English.

## 0. Summary

- **The existing paper model does not meet the spec.** The paper reports a Bayesian JRT in
  `02d`, fitted in Python/PyMC. It is not a GRM with rater-specific thresholds b_jk fitted by
  MML. It uses one set of thresholds shared by all raters, plus a leniency λ_j per rater.
  Its marginal reliability uses 1/(1 + ∫φ/I) for k "average" raters rather than the
  posterior-based I/(I+1) convention.
- **None of the spec's MML models existed in working form.** `mirt`/`sirt` code existed only
  in `notebooks/02_creativity_ratings_R.qmd`, and that file does not run: `save_table`,
  `has_pkg` and `log_warning` are undefined, `df_wide` is used before it is defined, and the
  `jrt` calls are placeholders.
- **Correction:** a new R pipeline implements spec §§2–7 one-to-one:
  - `R/jrt_functions.R`
  - `R/01_data_design.R` … `R/06_summary.R`
  - `server/run_jrt_audit_server.sh`

  The pipeline was first checked end-to-end on a small simulated dataset. The full run on
  the real data was done **locally on 2026-10-22** (R is not installed on the server; about
  14½ minutes, 12¾ of them for the Krippendorff bootstrap). Log:
  `results/logs/jrt_audit_server_run_20261022_115204.log`.
- **Results of the run** (details in §2):
  - All models converged with positive definite information matrices.
  - The final run (2026-10-22, 16:43) excludes raters with fewer than 15 ratings (R20, R21, R22). It has 7,820 ratings, 3,668 products and 19 raters. All numbers below are from this run.
  - The GRM has the lowest AIC, BIC and SABIC (BIC 24,508.8, against 24,529.6 for the PCM).
  - Both LR tests reject the restricted model.
  - θ̂ correlates at 0.975 to 0.996 across all models.
  - Empirical marginal reliability of the actual GRM scores is **0.67**, against 0.96 for
    the hypothetical full panel.
  - **Sensitivity:** in the first run, with all 22 raters, R21 and R22 were not identified
    (negative slopes with huge SEs). Excluding them changes the product scores only
    trivially: θ̂ correlates at r = 0.99997 with the all-raters run (max |Δθ̂| = 0.16). The
    all-raters results are in commit `5a0cf88`.
- **The author's decisions are applied** (see the table below and §5).
  - M1 is fitted with `rm.facets`.
  - R20 and R22 were flagged and then, together with R21, excluded (fewer than 15 ratings).
  - Everything on the deletion list was removed (§4).
  - The paper now draws on `notebooks/02_jrt_results.ipynb`, a display notebook for the R
    outputs (`paper.config.yml`, `manuscript/_status.md`).

### Decisions taken before the audit (author, 2026-10-22)

| Question | Decision |
|---|---|
| Several rating dimensions per row (creativity, technical correctness, aesthetic appeal) | Model **creativity only**. The other two stay in the data but go into no model. |
| Category gaps (8 of 22 raters do not use every category) | **Keep all 7 categories**; document the gaps, do not fix them |
| Form of the new pipeline | R scripts plus a server runner, not notebooks |
| Uncommitted work at the start | Baseline commit `79ae482` on the audit branch |
| M1 cannot be estimated in mirt with 7 categories | **Use `sirt::rm.facets` as M1.** Keep raters with fewer than 15 ratings for now |
| Internal category gaps (R20, R22) | **Flag them, do not exclude** (they may be excluded later). Superseded by the 15-ratings minimum below, which removes both |
| Minimum ratings per rater (after the first full run) | **Exclude raters with fewer than 15 ratings** from the whole pipeline (R20, R21, R22; 24 ratings, 1 product drops out). Reason: parameters not identified. The all-raters run is kept in git (commit `5a0cf88`) as a sensitivity comparison |
| Deletion list (§4) | **Approved in full.** The paper switches to the GRM outputs, so `02d` is removed too |

## 1. Inventory

Status key:
- ✅ meets the spec
- ⚠️ present, but deviates (the deviation is named)
- ❌ missing
- 🗑️ not in the spec, so a candidate for removal

### 1.1 Existing code

| # | File · cell/chunk | Content (one sentence) | Spec step | Status |
|---|---|---|---|---|
| A1 | `00_data_loading_preprocessing.ipynb` §§1–3 | Downloads the Google Sheet and optionally joins StatsBomb event details. | §2 (import) | ✅ data import; never deleted |
| A2 | `00` §4 | Maps columns to the schema and pseudonymises rater IDs (`R01`…). | §2 | ✅ |
| A3 | `00` §5 | Drops ratings flagged "action not recognised" (1,290 rows), logged. | §2 | ✅ (documented exclusion) |
| A4 | `00` §6 | Checks types and ranges; one out-of-range value removed. | §2 | ✅ |
| A5 | `00` §7 | Lists duplicate product–rater pairs and keeps the last entry. | §2 duplicates | ⚠️ Listed and not averaged, which is right. But the 12 pairs and the 1 conflicting pair (R14) were only reported as a row count. → Now in `results/data/duplicate_ratings_report.csv` |
| A6 | `00` §§8–9 | Derives rating order and saves `ratings_long_clean.csv` plus the cleaning log. | §2 | ✅ (input of the new pipeline) |
| B1 | `01_data_overview.ipynb` §§2–3 | Counts ratings, products and raters, and ratings per action. | §2 descriptives | ⚠️ No per-rater mean/SD table in the spec format. → `results/data/design_summary*.csv` |
| B2 | `01` §4 | Overall Krippendorff's α, **interval** level, without a CI. | §6 | ⚠️ Spec requires ordinal α with a bootstrap CI over products. → `R/05_naive_indices.R` |
| B3 | `01` §5 | Bipartite graph components and rater-overlap heatmap (Python). | §2 connectivity/overlap | ⚠️ The overlap matrix was not saved as a CSV, and connectivity was not a hard stop. → `R/01_data_design.R` |
| B4 | `01` §6 | Recommendations for future rater assignment. | — | 🗑️ |
| B5 | `01` §7.1 | Distribution of all ratings and category frequencies. | §2 categories | ⚠️ Overall only; no rater × category table. → `results/data/category_usage.csv` |
| B6 | `01` §7.2 | Rater response styles (mean, SD, central/extreme rate). | §2 descriptives | ⚠️ Partly covered; replaced by `design_summary_raters.csv` |
| B7 | `01` §7.3 | Descriptive drift: Spearman correlation of rating with order. | — | 🗑️ |
| B8 | `01` §7.4 | Degree distributions and component summary. | §2 | ⚠️ Superseded by `R/01` |
| B9 | `01` §7.5 | Rater × action-type contingency. | — | 🗑️ |
| B10 | `01` "Demonstrate rater tendencies" / "secondary dimensions" | Ad-hoc seaborn plots, including secondary dimensions. | — | 🗑️ |
| C1 | `02a_classical_consensus.ipynb` §2 | Raw and rater-centred mean scores. | — | 🗑️ |
| C2 | `02a` §3 | Pairwise agreement, Bland–Altman plots, heatmaps. | — | 🗑️ |
| C3 | `02a` §4 | Krippendorff's α, interval and ordinal, with a cluster bootstrap and subgroups. | §6 | ⚠️ Python, stale (old rater IDs); subgroup analyses are not in the spec. → `R/05` |
| C4 | `02a` §4.3 | Spearman–Brown projection. | — | 🗑️ |
| C5 | `02a` §5 | Leave-one-rater-out consistency. | — | 🗑️ |
| C6 | `02a` — | Cronbach's α. | §6 | ❌ Missing everywhere. → `R/05` |
| D1 | `02b_linear_mixed_model.ipynb` (all) | Bayesian crossed LMM, G-theory, D-study, drift, match facet, CV. | — | 🗑️ |
| E1 | `02c_ordinal_facet_model.ipynb` (all) | Bayesian **cumulative**-logit MFRM (PyMC), infit/outfit, separation reliability. | §5 (MFRM) | ⚠️ Wrong family (cumulative, not adjacent-category), Bayesian not MML, not nested in the `mirt` ladder, stale. → `R/04` |
| F1 | `02d_judge_response_theory.ipynb` §§1–2 | Bayesian JRT: a_j·θ + λ_j with **shared** thresholds τ_k, θ ~ N(0,1), largest component. | §3 | ⚠️ Not a GRM with b_jk and not MML. → `R/02_grm.R` |
| F2 | `02d` §3 | R-hat/ESS, rater table, discrimination vs. response style, trace plots. | §3 convergence/parameters | ⚠️ MCMC diagnostics instead of MML convergence; no IRT-metric b_jk |
| F3 | `02d` §3.1 | Posterior predictive check. | — | 🗑️ (no PPC in the spec; MML fit is checked by itemfit, Q3 and C2) |
| F4 | `02d` §4 | Equal-discrimination model compared by PSIS-LOO. | §5 | ⚠️ Replaced by the M2-vs-M3 LR test (MML) |
| F5 | `02d` §5 | Category curves and information for 3 raters. | §3 CRFs, §4a | ⚠️ Only 3 raters; shared-threshold model; no grid CSV and no shares |
| F6 | `02d` §6 | D-study of marginal reliability, 1/(1+∫φ/(k·Ī)); empirical reliability; precision by n. | §4b/§4c | ⚠️ Convention differs from I/(I+1); no product-level `rel_post`/`rel_info`; no product table with rater sets |
| F7 | `02d` §7 | Exports `scores_jrt.csv` and `raters_jrt.csv`. | §4c | ⚠️ Superseded by `results/grm/product_scores.csv` |
| G1 | `03_approach_comparison.ipynb` (all) | Compares A–D, rater flags, final `action_scores.csv`, automated text, QC. | §7 (partly) | 🗑️ / ⚠️ Stale; its role passes to `R/06_summary.R` |
| H1 | `02_creativity_ratings_R.qmd` §3 | lme4 LMM, `sirt::rm.facets`, `mirt` graded, `jrt` without NA handling. | §3/§5 | ⚠️ Does not run (undefined helpers, `df_wide` used before it exists). The `rm.facets` call is kept and documented in `R/04` |
| H2 | R qmd §§4–18 | Connectivity, pairwise agreement, α, lme4, brms ordinal, jrt placeholder, drift, CV, match facet, QC. | mixed | 🗑️ / ⚠️ Does not run; the spec parts are re-implemented in `R/01`–`R/06` |
| S1 | `server/run_jrt_server.sh`, `pack_for_server.sh`, `requirements-jrt.txt`, `README.md` | Server run of the Bayesian `02d`. | — | 🗑️ deleted with `02d`; `server/README.md` rewritten for the R pipeline |
| T1 | `results/tables/*`, `results/figures/*`, `results/models/*.nc`, `results/logs/*` from `02a`–`03` | Outputs of the notebooks above. | — | 🗑️ together with their notebooks |

### 1.2 New code (this audit)

| File | Spec | Runs where |
|---|---|---|
| `R/jrt_functions.R` | shared paths, seed `20260713`, MML settings, I/(I+1) helpers, data fingerprint and same-data assertions | — |
| `R/01_data_design.R` | §2 | local (seconds) — **run on the real data** |
| `R/02_grm.R` | §3 | server |
| `R/03_grm_information.R` | §4 | server (light, reloads model) |
| `R/04_model_comparison.R` | §5 | server |
| `R/05_naive_indices.R` | §6 | server (1000 bootstraps) |
| `R/06_summary.R` | §7 | server/local |
| `server/run_jrt_audit_server.sh`, `server/pack_jrt_audit_for_server.sh` | runner (`--smoke` for a quick run) | — |

## 2. Spec checklist

Status as of this commit:
- **[x]** done and verified on the real data
  (full run on the real data, 2026-10-22)
- **[!]** deviation or open point

### §2 Data and design (`R/01_data_design.R`, run on the real data)
- [x] Long format `results/data/ratings_long.csv` and wide matrix `ratings_wide.csv` (3,669 products × 22 raters, 7,844 ratings, 9.7% filled). Both are gitignored like `data/`. A fingerprint in `data_fingerprint.txt` is asserted by every later script. `rm.facets` gets the same long data.
- [x] **More than one facet?** Each row also carries `technical_correctness` and `aesthetic_appeal`. The author decided to model creativity only.
- [x] **Duplicates:** none left after `00`. Upstream there were 12 pairs (13 rows removed by "keep last"); one pair (R14) had conflicting values. See `duplicate_ratings_report.csv`. Nothing is averaged.
- [x] **Categories:** the 1–7 scale is coded 0–6 internally (rating − 1).
- [!] **Category use per rater** (`category_usage.csv`): 8 of 22 raters have gaps.
  - End gaps: R01, R03, R06 and R18 never use 7; R17 and R21 never use 6–7.
  - **Internal gaps:** R20 never uses 2 (13 ratings); R22 has 2 ratings, in categories 2 and 4.
  - With R20, R21 and R22 excluded (15-ratings minimum), **no internal gaps remain**. 5 of 19 raters have end gaps (R01, R03, R06, R17, R18).
  - mirt recodes each rater's categories, so:
    - for raters with internal gaps, the GRM/PCM/GPCM thresholds above the gap are shifted;
    - the RSM (M1) cannot be estimated in mirt at all ("items must have the same number of categories", confirmed on test data).
  - The author decided to keep all 7 categories. The consequences are documented in `rater_parameters.csv`, where the `category_boundaries` column says which categories each b_k separates.
  - **Proposed fixes (not applied):** see §5.
- [x] **Connectivity:** one component, asserted as a hard stop. The overlap matrix is in `rater_overlap.csv`: With 22 raters, 37 of 231 rater pairs shared no product (median overlap 7). After the exclusions, 17 of 171 pairs share no product (median overlap 13).
- [x] **Descriptives:** `design_summary.csv`, `design_summary_raters.csv` (n, mean, SD) and `design_summary_ratings_per_product.csv`.

### §3 GRM (`R/02_grm.R`)
- [x] MML via EM with 61 fixed quadrature points. TOL is 1e-4 (the mirt default) and at most 2,000 cycles; all settings are written out in `jrt_functions.R`.
- [x] Identification: θ ~ N(0,1), all a_j and b_jk free, no constraints (asserted).
- [x] Convergence: `converged`, EM cycles and condition number go to `convergence.csv`. All warnings are captured to `results/logs/warnings_jrt_audit_02_grm.csv`.
  - **Result:** converged after 165 EM cycles; log-likelihood −11,733.23 with 127 parameters; condition number 7.8 × 10³.
- [x] SEs: `SE.type = "Oakes"`, with the positive-definite check from `extract.mirt(mod, "secondordertest")`.
  - **Result:** the information matrix is positive definite.
- [x] Parameters in IRT metric with SEs. Flags for a > 4 and |b| > 5 are joined with n and category use.
  - **Result:** no a > 4. The 19 raters have a between 0.63 and 3.71; for R16 (a = 3.70, SE 1.36) and R19 (a = 3.71, SE 2.22) the SEs are large. All thresholds are ordered.
  - **[!] |b| > 5:** R18 only (max |b| = 6.6, low a = 0.63, 55 ratings).
  - In the all-raters run, R21 (a = −0.09, SE 1.01, max |b| = 24.5) and R22 (a = −3.86, SE 7.83) were not identified. This led to the 15-ratings minimum (§5).
- [!] **Rater fit:** mirt 1.46 has no `impute` argument any more; it is hard-coded off in `itemfit()` and `M2()`. Instead:
  - infit/outfit are computed directly on the observed ratings, which mirt supports with missing data;
  - S-X² uses an **explicit multiple imputation**: plausible values, then `imputeMissing`, then a refit with all parameters fixed, then S-X²; S-X² and df are averaged over 20 imputations with seed 20260713.

  With about 90% of cells imputed, S-X² leans strongly towards good fit. It is reported, but not as primary evidence.

  **Result:**
  - S-X²: no rater misfits (all p ≥ .29, the lowest for R12; RMSEA ≈ 0). mirt warns 20 times that "imputing too much data can lead to very conservative results", which is the low power described above.
  - **[!] infit/outfit:** 14 of 19 raters are flagged, with mean squares mostly 0.4–0.7, i.e. *overfit*. This is most likely an artefact of the sparse design: with about 2 ratings per product, the EAP estimate is drawn towards exactly those ratings, so the residuals are small. The flags are reported but not used to judge raters.
  - z-outfit for R18 is `NA`; this is the "NaNs produced" warning.
- [x] Q3 is computed pairwise over shared products, with `n_common` beside each pair. Pairs with fewer than 3 shared products are not computed; pairs with fewer than 30 are flagged as unstable. On test data it matches `mirt::residuals(type = "Q3")` to 3e-17.
  - **Result:** on the real data it matches mirt to 2e-16. All 171 pairs are listed. The mean Q3 is −0.24, the known downward bias of Q3 when a product has only a few ratings.
    - 20 pairs with at least 30 shared products deviate from that mean by more than 0.2. 17 of them are negative, down to −0.76 (R08–R19). The other 3 have a raw Q3 between 0.04 and 0.11 (R01–R09, R10–R11, R11–R18).
    - Larger positive values (up to 0.94, R01–R14) occur only in pairs with 10 or fewer shared products, which are flagged as unstable.
    - There is no sign of local dependence.
- [!] **Absolute fit:** `M2(type = "C2")`. mirt 1.46 has no imputation here, so the moments come from the available pairs.
  - **Result: not computable** on the real data. mirt stops with "missing value where TRUE/FALSE needed", most likely because 17 of the 171 rater pairs share no product. This is recorded in `global_fit.csv`. Absolute GRM fit therefore rests on S-X², Q3 and the model comparison.
- [x] Category response functions for every rater: `figures/grm_category_response_functions.*`.
- [x] EAP scores with PSD (`fscores(..., full.scores.SE = TRUE)`). The shrinkage note is in the script header and in §4.

### §4 Information and reliability (`R/03_grm_information.R`)
- [x] Rater information on the grid −4…4 in steps of 0.05. The per-rater summary gives the N(0,1)-weighted area, the θ of the maximum, the maximum, and the rater's share at θ = −2…2 and weighted. Plots show the curves and the stacked shares.
- [x] Full panel: `panel_information_grid.csv` (θ, info, se, rel = I/(I+1)), plus `marginal_rxx` and a grid recomputation as a check.
- [x] Product level: information only from each product's own raters, with an assertion that this is below the full-panel information. Columns: `theta_eap`, `psd`, `rel_post = 1 − psd²`, `info_at_eap`, `rel_info`, `n_ratings`, `raters`.
- [x] Consistency of `rel_post` and `rel_info` (correlation, mean difference, the 25 largest differences). Empirical reliability from `empirical_rxx`, asserted equal to the manual formula.
- [x] Histogram of `rel_post`, `rel_post` by n and by θ̂. No products are filtered.
- **Results:**
  - Full panel: model-based marginal reliability 0.960; the grid recomputation gives 0.960 as well.
  - Actual scores: empirical marginal reliability 0.672 (Var θ̂ = 0.672, mean PSD² = 0.328).
  - `rel_post`: median 0.698 (Q1 0.596, Q3 0.769).
  - `rel_post` and `rel_info` correlate at 0.935, with a mean difference of 0.016. 320 products differ by more than 0.1.
- [x] **Reliability convention** (`grep`): every new script uses I/(I+1) (`rel_from_info`). The old 1/(1+∫φ/I) was used only in `02d`, which has been deleted.

### §5 Comparison (`R/04_model_comparison.R`)
- [x] M1 `rsm`, M2 `Rasch`, M3 `gpcm` and the GRM all use the same matrix, asserted by row count, rating count and NA pattern.
- [x] `rm.facets` parametrisation documented from `?rm.facets`. It is the RSM with a rater shift, MML via EM on a 30-point grid over [−9, 9], σ estimated, Σb_r = 0. See `mfrm_equivalence.md`.
- [x] **M1 is `sirt::rm.facets`** (author decision 2026-10-22). mirt's `rsm` is still attempted, and its error is recorded in `model_fit.csv`.
  - M1 uses a fine grid of 321 points on [−8, 8].
  - On simulated data without category gaps, `rm.facets` and mirt's `rsm` agree:
    - log-likelihood difference 0.04;
    - rater locations correlate at r = −1.000 (opposite sign conventions);
    - both latent variances are about 0.54.

    `software_crosscheck.csv` recomputes this on every run, which is what justifies the cross-software M1-vs-M2 LR test.
  - The original call (sirt's default 30-point grid on [−9, 9]) is fitted as well and compared with M1 in `mfrm_equivalence.md`.
  - df for M1 vs M2: J + K − 1 free RSM parameters, against mirt's PCM count. They differ from (J−1)(K−2) wherever raters leave end categories unused; that difference is reported.
  - For a rater with an internal gap, the nesting would only be approximate, because mirt rescores categories above the gap. After the exclusions no such rater remains, so M1 is nested in M2.
  - **Result:**
    - The cross-check on the real-data run gives a log-likelihood difference of 0.037, rater locations correlated at r = −1.000, and latent variances of 0.544 and 0.537.
    - M1 log-likelihood is −12,186.22 with 25 parameters. mirt `rsm` failed, as expected.
    - M1 vs M2: χ²(84) = 737.5, p < 10⁻¹⁰⁰. The df are 84, against 90 from (J−1)(K−2), because of the end gaps.
    - The default-grid `rm.facets` gives the same θ̂ as M1 (r = 0.999999).
- [x] M1 rater infit/outfit is computed from the M1 parameters at the EAP estimate. The category probabilities are checked against the `rm.facets` output.
- [x] M2 vs M3 LR test, with the df checked against J − 1. AIC, BIC and SABIC for M1–M3 and the GRM.
- [x] θ̂ correlations (Pearson and Spearman) for M2, M3, GRM and `rm.facets`. Also the spread of a_j in M3, threshold order in M2/M3, and M1 infit/outfit (if M1 runs).
- [x] Marginal reliability only, for comparison. It is computed on each model's own latent variance: `mirt::marginal_rxx` assumes N(0,1) and is not valid for Rasch models with a free variance.
- **Results:**
  - **M2 vs M3:** χ²(18) = 122.0, p = 1.8 × 10⁻¹⁷. The df match J − 1.
  - **Information criteria:**

    | Model | AIC | BIC | SABIC |
    |---|---|---|---|
    | M1 | 24,422.4 | 24,577.6 | 24,498.2 |
    | M2 | 23,853.0 | 24,529.6 | 24,183.2 |
    | M3 | 23,767.0 | 24,555.4 | 24,151.8 |
    | GRM | **23,720.5** | **24,508.8** | **24,105.3** |

    The GRM and M3 have the same number of parameters (127), and the GRM's log-likelihood is higher by 23.3.
  - **θ̂ correlations:** Pearson 0.975–0.996 and Spearman 0.978–0.996 across M1, M2, M3 and the GRM.
  - **M3 slopes:** a ranges from 0.28 (R09) to 2.61 (R16). All are positive.
  - **Thresholds:** unordered thresholds occur in M2/M3 for several raters (`threshold_order.csv`); in the GRM they are ordered by construction.
  - **Marginal reliability:** 0.943 (M1), 0.944 (M2), 0.955 (M3) and 0.960 (GRM). The empirical reliability is 0.626, 0.637, 0.657 and 0.672 in the same order.

### §6 Naive indices (`R/05_naive_indices.R`)
- [x] Cronbach's α from `psych::alpha` on the pairwise covariance matrix. A pair needs at least 3 shared products. Raters whose covariances cannot be computed are dropped one at a time and listed.
- [x] No product is rated by all raters. α is therefore also reported for the largest fully crossed block of raters, searching blocks of each size.
- [x] Krippendorff's α (ordinal) with `irr::kripp.alpha(t(wide))`. The orientation (raters × units) and the NA count are asserted. The bootstrap over products uses 1,000 replications and seed 20260713.
- **Results:**
  - **Krippendorff's α (ordinal):** 0.392, 95% CI [0.362, 0.417].
  - **[!] Cronbach's α (pairwise):** 0.928 over 14 raters. 5 raters (R19, R14, R02, R16, R12) were dropped for incomplete covariances. `psych` warned that the matrix was not positive definite and smoothed it.
  - **Cronbach's α (largest crossed block):** 0.658, from 3 raters (R07, R09, R11) on 139 products.
  - Neither α refers to the scores actually produced.

### §7 Summary (`R/06_summary.R`)
- [x] `results/summary/reliability_overview.csv` and `REPORT.md` are generated from the CSVs only.

### Additions for the manuscript (2026-10-23, author decisions D7–D9)
Run log: `results/logs/jrt_audit_server_run_20261023_103224.log`. Model results are unchanged from the run of 2026-10-22.
- **Effect sizes for model choice:** `model_fit.csv` now has ΔAIC, ΔBIC and ΔSABIC relative to the best model. The GRM is best on all three.

  | Model | ΔAIC | ΔBIC | ΔSABIC |
  |---|---|---|---|
  | M3 | 46.6 | 46.6 | 46.6 |
  | M2 | 132.5 | 20.8 | 78.0 |
  | M1 | 702.0 | 68.8 | 392.9 |
- **Change of the product ranking against the GRM** (`score_agreement.csv`): the mean shift in percentile rank is 0.017 (M3), 0.033 (M2) and 0.042 (M1). 7.5% (M3), 15.0% (M2) and 20.2% (M1) of products change quintile, and at most 0.4% move by two quintiles or more.
- **Intervals from 200 parameter draws** (`reliability_ci.csv`, `rater_information_ci.csv`). The draws use the asymptotic normal distribution with the Oakes covariance. 87 draws with a ≤ 0 or unordered intercepts were rejected; `mirt::draw_parameters()` fails on this model in mirt 1.46.1.
  - Empirical marginal reliability: 0.672 [0.649, 0.687]. This interval also resamples products.
  - Model-based marginal reliability: 0.960 [0.953, 0.968].
  - Rater information intervals are wide for the raters with about 50 ratings, for example R19: 3.54 [0.41, 11.0] and R16: 3.30 [0.73, 6.49].
- **Cronbach's α bootstrap over products** (1,000 replications):
  - Pairwise: 0.928 [0.891, 0.943]. **[!]** 361 replications failed, because a rater pair lost all shared products. The interval is conditional on the successful replications and only approximate.
  - Crossed block: 0.658 [0.526, 0.756], with no failures.
- **Sensitivity to the rater exclusion** (`sensitivity_rater_exclusion.csv`). The GRM was refitted on all 22 raters without SEs.
  - θ̂ of the 3,668 common products: r = 0.99997, mean |Δ| = 0.0017, max |Δ| = 0.16, and 0.5% of products change quintile.
  - Empirical reliability: 0.672 with all raters, against 0.672 in the final data. Model-based reliability: 0.962 against 0.960.
  - Discriminations of the 19 common raters: r = 0.9988, max |Δa| = 0.20.
- **Display notebook:**
  - Threshold SEs are now shown, and p-values are exact.
  - Integers have no decimals, and missing values show as "–".
  - R figures no longer have built-in titles, and they are embedded without resampling.
  - The notebook is generated by `notebooks/build_02_jrt_results.py`.
- **Notebook 01** applies the same rater exclusion (19 raters, 7,820 ratings).
- **Original-ID lookups** were moved to `notebooks/local_rater_lookup.ipynb`, which is gitignored. No published notebook shows original IDs.

## 3. Deviations found and corrections

| # | Deviation in the existing analysis | Cause | Correction |
|---|---|---|---|
| D1 | The central model is Bayesian, with shared thresholds and rater leniency, instead of a GRM with b_jk by MML. | Design choice in `02d`: thought too sparse for b_jk. | `R/02_grm.R` fits the spec's GRM. Whether b_jk can be estimated is now checked empirically (SEs, PD information matrix, \|b\| flags). |
| D2 | Reliability convention 1/(1+∫φ/(k·Ī)) and an IRT D-study over k average raters. | Green et al. (1984) marginal formula. | I/(I+1) used throughout; the D-study is not in the spec. |
| D3 | No product-level reliability from each product's own rater set. | Not implemented. | `product_scores.csv` with `info_at_eap` over R_n, `rel_post` and `rel_info`. |
| D4 | The MFRM was cumulative-logit Bayesian (`02c`), and `rm.facets` existed only in a broken qmd. | — | Adjacent-category MML ladder in mirt, plus the documented `rm.facets`. |
| D5 | No RSM/PCM/GPCM ladder and no LR tests. | — | `R/04`. |
| D6 | Krippendorff's α at interval level in the paper's `01`; no Cronbach's α. | — | Ordinal α with a bootstrap CI; Cronbach's α computed pairwise and on a crossed block. |
| D7 | No category-use table per rater; mirt recoding not checked. | — | `category_usage.csv`; consequences documented (§2, §5). |
| D8 | The overlap matrix was not saved, and connectivity was not a hard stop. | — | `rater_overlap.csv`, plus a `stop()` if the graph has more than one component. |
| D9 | The R qmd does not run. | Helpers removed, chunks out of order. | Replaced by `R/` scripts; the qmd is a deletion candidate. |
| D10 | No package versions or session info for the R parts. | — | `results/logs/session_info_jrt_audit_*.txt` written by every script. |

## 4. Deletion candidates (🗑️) — **approved 2026-10-22 and deleted**

Everything below was removed, including `02d` and its server files after the paper was switched to the GRM.
The gitignored model traces (`results/models/*.nc`) and `data/processed/action_scores.csv` / `rater_diagnostics.csv` were removed as well.

| Candidate | Used by spec analyses? | Note |
|---|---|---|
| `notebooks/02a_classical_consensus.ipynb` and its tables/figures (`*classical*`, `krippendorff_alpha_*`, `pairwise_rater_agreement`, `leave_one_out_consistency`) | no | Stale (old rater IDs). §6 is redone in `R/05`. |
| `notebooks/02b_linear_mixed_model.ipynb` and outputs (`*lmm*`, `extended_model_*`, `cross_validation_*`, `fig_appendix_lmm_*`, `results/models/gaussian_*.nc`, `extended_match_model.nc`) | no | Not in the spec. |
| `notebooks/02c_ordinal_facet_model.ipynb` and outputs (`*mfrm*`, `ordinal_*`, `fig_mfrm_*`, `results/models/ordinal_crossed_model.nc`) | no | Replaced by the §5 ladder. |
| `notebooks/03_approach_comparison.ipynb` and outputs (`comparison_*`, `sample_description_summary`, `qc_checklist`, `warnings_log*.csv`, `automated_interpretation.txt`, `fig_comparison_*`, `data/processed/action_scores.csv`, `rater_diagnostics.csv`) | no | Replaced by `R/06`. |
| `notebooks/02_creativity_ratings_R.qmd` | no | Does not run. Its `rm.facets` call is carried over and documented in `R/04`. |
| `01_data_overview.ipynb` §4 (interval α), §6 (recommendations), §7.3 (drift), §7.5 (rater × action type), the two demo sections | **yes, the manuscript cites `01`** (`fig-overview-*`, `tbl-overview-ratings-per-action`) | Cells removed; the notebook was re-run. The remaining sections were renumbered (§4 connectivity, §5 design diagnostics), and the manuscript labels are unchanged. |
| `notebooks/02d_judge_response_theory.ipynb`, `server/run_jrt_server.sh`, `pack_for_server.sh`, `requirements-jrt.txt`, `server/README.md`, `*jrt*.csv`, `fig_jrt_*`, `results/models/jrt_*.nc`, `results/logs/02d_*` | was a dependency of the manuscript | Deleted after the author switched the paper to the GRM outputs (`notebooks/02_jrt_results.ipynb`); `server/README.md` was rewritten, not deleted. |
| `APPROACHES.md`, `ANALYSIS_TODO.md`, `README.md` | described A–D | Rewritten for the GRM pipeline. |
| `requirements.txt` entries for statsmodels, scikit-learn, PyMC, arviz, krippendorff and seaborn; R packages lme4, brms, jrt and others in `install_r_packages.R` | needed only by removed notebooks | Pruned. |

Never deleted: `00_data_loading_preprocessing.ipynb`, `data/raw/*` and `data/processed/ratings_long_clean.csv`.

## 5. Decisions (2026-10-22) and remaining open points

1. **M1:** fitted with `sirt::rm.facets` (see §2/§5).
2. **Minimum of 15 ratings per rater** (decided after the first full run): R20, R21 and R22 are excluded in `R/01_data_design.R` (`MIN_RATINGS_PER_RATER`; `results/data/excluded_raters.csv`). This also removes both raters with internal gaps.
   - The author reported that R22's ratings had been deleted. However, after `00` was re-run on 2026-10-22, the cleaned data still contain R22 (2 ratings). The sheet update removed only the former R23, who had only "not recognised" ratings and therefore never reached the models.
   - The pseudonyms of all other raters are unchanged. **To be confirmed by the author.**
3. **Manuscript:** switched to the GRM outputs via `notebooks/02_jrt_results.ipynb`; `paper.config.yml` is updated.
   - The manuscript artifacts (`02_artifacts.md` … `manuscript.qmd`) are obsolete. The paper pipeline is re-run from phase 3 after the server run (`manuscript/_status.md`).
4. **Deletion list:** done (§4).
5. **Open after the full run (author to decide):**
   - ~~R21 and R22 not identified~~: resolved by the 15-ratings minimum.
   - **R18:** low discrimination (a = 0.63) and an extreme threshold (|b| = 6.6) on 55 ratings. Worth checking in the raw data.
   - **C2** is not computable (see §3). Absolute fit is argued from S-X², Q3 and the model comparison.
   - **infit/outfit flags** are probably artefacts of the sparse design (see §3). Report the values without using the flags to judge raters.
   - To look up raters in the raw data, map pseudonyms with `switch_rater_ids()` in `R/jrt_functions.R`, which uses the gitignored key `data/raw/rater_pseudonym_key.csv`. Original IDs never go into `results/`.

## 6. Running the pipeline

```bash
# locally, in full (as done on 2026-10-22; analysis folder)
nohup bash server/run_jrt_audit_server.sh > jrt_audit_run.out 2>&1 &

# or on a server with R
bash server/pack_jrt_audit_for_server.sh
scp jrt_audit_server_bundle.tar.gz user@server:~/
# on the server
mkdir -p ~/jrt_audit && cd ~/jrt_audit && tar -xzf ~/jrt_audit_server_bundle.tar.gz
Rscript install_r_packages.R              # first time only
bash server/run_jrt_audit_server.sh --smoke
tmux new -s jrt_audit; bash server/run_jrt_audit_server.sh
# back locally
scp user@server:~/jrt_audit/jrt_audit_results.tar.gz . && tar -xzf jrt_audit_results.tar.gz
```

Run time on a laptop (2026-10-22): 14½ minutes in total. `05` takes 12¾ of them (the
Krippendorff bootstrap), `02` 50 s, `04` 42 s, and the other steps a few seconds each.

### Additions 2026-10-23 (second round, for the manuscript)

- **Raw mean vs GRM score** (`R/03_grm_information.R` → `results/grm/raw_mean_vs_grm.csv`,
  `figures/grm_raw_mean_vs_theta.*`; notebook `tbl-raw-mean-vs-grm`, `fig-raw-mean-vs-theta`):
  agreement of the unweighted rater mean with the GRM EAP score, overall and for products
  with 1, 2 and 3+ ratings, plus the range of GRM scores among products with equal raw mean.
  `rank_change()` moved to `jrt_functions.R` (shared with `04`, outputs unchanged).
- **C2:** cause identified. `M2(type = "C2")` returns NaN because 17 of 171 rater pairs share no
  products (undefined bivariate moments); the earlier error came from the null-model comparison
  on that NaN. Now `c2_global_fit()` in `jrt_functions.R`; `global_fit.csv` regenerated from the
  saved model with this function (no refit).
- **Notebook explanations:** accepted vs rejected parameter draws, LR df 84 vs 90
  (6 unused end categories: R01, R03, R06, R18 never use 7; R17 never uses 6 or 7), mean Q3 and
  the flag_q3 criterion, n_boot / n_boot_failed in the naive-indices table, no misfit cut-offs.
- Information figures: two-column legend. Notebook 01: "products" wording, integer formatting,
  response styles shown with 3 decimals.
- `03` re-run with the fixed seed reproduced all earlier outputs byte for byte.
