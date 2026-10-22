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

  The heavy steps run on the server. Only `R/01_data_design.R` has been run on the real
  data so far. The other scripts were checked end-to-end on a small simulated dataset.
- **Open decisions for the author** are listed in §5 below: M1 cannot be estimated in `mirt`
  while all 7 categories are kept; two raters have a category gap in the middle of the
  scale; and the manuscript depends on `02d`.

### Decisions taken before the audit (author, 2026-10-22)

| Question | Decision |
|---|---|
| Several rating dimensions per row (creativity, technical correctness, aesthetic appeal) | Model **creativity only**. The other two stay in the data but go into no model. |
| Category gaps (8 of 22 raters do not use every category) | **Keep all 7 categories**; document the gaps, do not fix them |
| Form of the new pipeline | R scripts plus a server runner, not notebooks |
| Uncommitted work at the start | Baseline commit `79ae482` on the audit branch |

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
| A3 | `00` §5 | Drops ratings flagged "action not recognised" (1,292 rows), logged. | §2 | ✅ (documented exclusion) |
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
| S1 | `server/run_jrt_server.sh`, `pack_for_server.sh`, `requirements-jrt.txt`, `README.md` | Server run of the Bayesian `02d`. | — | 🗑️ only if `02d` is removed (see §5) |
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
- **[c]** coded and tested on simulated data only; it is checked off after the server run
- **[!]** deviation or open point

### §2 Data and design (`R/01_data_design.R`, run on the real data)
- [x] Long format `results/data/ratings_long.csv` and wide matrix `ratings_wide.csv` (3,669 products × 22 raters, 7,844 ratings, 9.7% filled). Both are gitignored like `data/`. A fingerprint in `data_fingerprint.txt` is asserted by every later script. `rm.facets` gets the same long data.
- [x] **More than one facet?** Each row also carries `technical_correctness` and `aesthetic_appeal`. The author decided to model creativity only.
- [x] **Duplicates:** none left after `00`. Upstream there were 12 pairs (13 rows removed by "keep last"); one pair (R14) had conflicting values. See `duplicate_ratings_report.csv`. Nothing is averaged.
- [x] **Categories:** the 1–7 scale is coded 0–6 internally (rating − 1).
- [!] **Category use per rater** (`category_usage.csv`): 8 of 22 raters have gaps.
  - End gaps: R01, R03, R06 and R18 never use 7; R17 and R21 never use 6–7.
  - **Internal gaps:** R20 never uses 2 (13 ratings); R22 has 2 ratings, in categories 2 and 4.
  - mirt recodes each rater's categories, so:
    - for raters with internal gaps, the GRM/PCM/GPCM thresholds above the gap are shifted;
    - the RSM (M1) cannot be estimated in mirt at all ("items must have the same number of categories", confirmed on test data).
  - The author decided to keep all 7 categories. The consequences are documented in `rater_parameters.csv`, where the `category_boundaries` column says which categories each b_k separates.
  - **Proposed fixes (not applied):** see §5.
- [x] **Connectivity:** one component, asserted as a hard stop. The overlap matrix is in `rater_overlap.csv`: 37 of 231 rater pairs share no product, and the median overlap is 7.
- [x] **Descriptives:** `design_summary.csv`, `design_summary_raters.csv` (n, mean, SD) and `design_summary_ratings_per_product.csv`.

### §3 GRM (`R/02_grm.R`)
- [c] MML via EM with 61 fixed quadrature points. TOL is 1e-4 (the mirt default) and at most 2,000 cycles; all settings are written out in `jrt_functions.R`.
- [c] Identification: θ ~ N(0,1), all a_j and b_jk free, no constraints (asserted).
- [c] Convergence: `converged`, EM cycles and condition number go to `convergence.csv`. All warnings are captured to `results/logs/warnings_jrt_audit_02_grm.csv`.
- [c] SEs: `SE.type = "Oakes"`, with the positive-definite check from `extract.mirt(mod, "secondordertest")`.
- [c] Parameters in IRT metric with SEs. Flags for a > 4 and |b| > 5 are joined with n and category use.
- [!] **Rater fit:** mirt 1.46 has no `impute` argument any more; it is hard-coded off in `itemfit()` and `M2()`. Instead:
  - infit/outfit are computed directly on the observed ratings, which mirt supports with missing data;
  - S-X² uses an **explicit multiple imputation**: plausible values, then `imputeMissing`, then a refit with all parameters fixed, then S-X²; S-X² and df are averaged over 20 imputations with seed 20260713.

  With about 90% of cells imputed, S-X² leans strongly towards good fit. It is reported, but not as primary evidence.
- [c] Q3 is computed pairwise over shared products, with `n_common` beside each pair. Pairs with fewer than 3 shared products are not computed; pairs with fewer than 30 are flagged as unstable. On test data it matches `mirt::residuals(type = "Q3")` to 3e-17.
- [!] **Absolute fit:** `M2(type = "C2")`. mirt 1.46 has no imputation here, so the moments come from the available pairs. If the run fails, the reason is written to `global_fit.csv`.
- [c] Category response functions for every rater: `figures/grm_category_response_functions.*`.
- [c] EAP scores with PSD (`fscores(..., full.scores.SE = TRUE)`). The shrinkage note is in the script header and in §4.

### §4 Information and reliability (`R/03_grm_information.R`)
- [c] Rater information on the grid −4…4 in steps of 0.05. The per-rater summary gives the N(0,1)-weighted area, the θ of the maximum, the maximum, and the rater's share at θ = −2…2 and weighted. Plots show the curves and the stacked shares.
- [c] Full panel: `panel_information_grid.csv` (θ, info, se, rel = I/(I+1)), plus `marginal_rxx` and a grid recomputation as a check.
- [c] Product level: information only from each product's own raters, with an assertion that this is below the full-panel information. Columns: `theta_eap`, `psd`, `rel_post = 1 − psd²`, `info_at_eap`, `rel_info`, `n_ratings`, `raters`.
- [c] Consistency of `rel_post` and `rel_info` (correlation, mean difference, the 25 largest differences). Empirical reliability from `empirical_rxx`, asserted equal to the manual formula.
- [c] Histogram of `rel_post`, `rel_post` by n and by θ̂. No products are filtered.
- [x] **Reliability convention** (`grep`): every new script uses I/(I+1) (`rel_from_info`). The old 1/(1+∫φ/I) appears only in `02d`.

### §5 Comparison (`R/04_model_comparison.R`)
- [c] M1 `rsm`, M2 `Rasch`, M3 `gpcm` and the GRM all use the same matrix, asserted by row count, rating count and NA pattern.
- [c] `rm.facets` parametrisation documented from `?rm.facets`. It is the RSM with a rater shift, MML via EM on a 30-point grid over [−9, 9], σ estimated, Σb_r = 0. See `mfrm_equivalence.md`.
- [!] **Equivalence of `rm.facets` with M1 and the M1-vs-M2 LR test:** both are blocked while M1 cannot be estimated in mirt (§2 category gaps). The script records this and runs everything else. `rm.facets` itself works, because it keeps the full 0–6 category set for every rater.
- [c] M2 vs M3 LR test, with the df checked against J − 1. AIC, BIC and SABIC for M1–M3 and the GRM.
- [c] θ̂ correlations (Pearson and Spearman) for M2, M3, GRM and `rm.facets`. Also the spread of a_j in M3, threshold order in M2/M3, and M1 infit/outfit (if M1 runs).
- [c] Marginal reliability only, for comparison. It is computed on each model's own latent variance: `mirt::marginal_rxx` assumes N(0,1) and is not valid for Rasch models with a free variance.

### §6 Naive indices (`R/05_naive_indices.R`)
- [c] Cronbach's α from `psych::alpha` on the pairwise covariance matrix. A pair needs at least 3 shared products. Raters whose covariances cannot be computed are dropped one at a time and listed.
- [c] No product is rated by all raters. α is therefore also reported for the largest fully crossed block of raters, searching blocks of each size.
- [c] Krippendorff's α (ordinal) with `irr::kripp.alpha(t(wide))`. The orientation (raters × units) and the NA count are asserted. The bootstrap over products uses 1,000 replications and seed 20260713.

### §7 Summary (`R/06_summary.R`)
- [c] `results/summary/reliability_overview.csv` and `REPORT.md` are generated from the CSVs only.

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

## 4. Deletion candidates (🗑️) — **waiting for approval, nothing deleted yet**

| Candidate | Used by spec analyses? | Note |
|---|---|---|
| `notebooks/02a_classical_consensus.ipynb` and its tables/figures (`*classical*`, `krippendorff_alpha_*`, `pairwise_rater_agreement`, `leave_one_out_consistency`) | no | Stale (old rater IDs). §6 is redone in `R/05`. |
| `notebooks/02b_linear_mixed_model.ipynb` and outputs (`*lmm*`, `extended_model_*`, `cross_validation_*`, `fig_appendix_lmm_*`, `results/models/gaussian_*.nc`, `extended_match_model.nc`) | no | Not in the spec. |
| `notebooks/02c_ordinal_facet_model.ipynb` and outputs (`*mfrm*`, `ordinal_*`, `fig_mfrm_*`, `results/models/ordinal_crossed_model.nc`) | no | Replaced by the §5 ladder. |
| `notebooks/03_approach_comparison.ipynb` and outputs (`comparison_*`, `sample_description_summary`, `qc_checklist`, `warnings_log*.csv`, `automated_interpretation.txt`, `fig_comparison_*`, `data/processed/action_scores.csv`, `rater_diagnostics.csv`) | no | Replaced by `R/06`. |
| `notebooks/02_creativity_ratings_R.qmd` | no | Does not run. Its `rm.facets` call is carried over and documented in `R/04`. |
| `01_data_overview.ipynb` §4 (interval α), §6 (recommendations), §7.3 (drift), §7.5 (rater × action type), the two demo sections | **yes, the manuscript cites `01`** (`fig-overview-*`, `tbl-overview-ratings-per-action`) | Remove only the cells, not the notebook. §§2–3, 5 and 7.1–7.4 stay as manuscript figures until the paper is switched to `results/data/*`. |
| `notebooks/02d_judge_response_theory.ipynb`, `server/run_jrt_server.sh`, `pack_for_server.sh`, `requirements-jrt.txt`, `server/README.md`, `*jrt*.csv`, `fig_jrt_*`, `results/models/jrt_*.nc`, `results/logs/02d_*` | **yes:** `manuscript/03_findings.md`, `04_outline.md` and `manuscript.qmd` cite its numbers and labels | **Flagged as a dependency, not deleted.** Remove it only once the manuscript has been switched to the GRM outputs (author decision). |
| `APPROACHES.md`, `ANALYSIS_TODO.md` | describe A–D | Update after approval, rather than delete. |
| `requirements.txt` entries for statsmodels, scikit-learn, PyMC and arviz | needed by `02b`–`02d` | Update after approval. |

Never deleted: `00_data_loading_preprocessing.ipynb`, `data/raw/*` and `data/processed/ratings_long_clean.csv`.

## 5. Open decisions for the author

1. **M1 (RSM) is not estimable in mirt while 7 categories are kept.** The M1-vs-M2 LR test and the `rm.facets` ≡ M1 check depend on it. Options:
   - (a) Collapse the sparse top categories for **all** models (e.g. 5–7 → 5 gives K = 5) and drop R20–R22, which have fewer than 15 ratings. All 19 remaining raters then use every category.
   - (b) Use `rm.facets` (which keeps empty categories) as M1 and accept that M1 vs M2 is compared across software.
   - (c) Drop M1 from the ladder and report M2 vs M3 plus `rm.facets` descriptively.
2. **Internal gaps in R20 and R22** (13 and 2 ratings). Their thresholds are not comparable with those of other raters. Options: exclude them from all models, or keep them and flag them (current setting).
3. **The manuscript depends on `02d`.** Should the paper switch to the GRM outputs? Until it does, `02d` stays.
4. **Approve the deletion list in §4** (completely or item by item).

## 6. Running the pipeline

```bash
# locally (analysis folder)
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

Expected run time is minutes: the mirt fits are fast. The slow parts are the 20 S-X²
imputations, C2, the four SE computations and the 1,000 Krippendorff bootstraps.
