# Analysis to-do list (JRT paper)

Status as of 2026-10-22, after the audit (`AUDIT.md`). The analysis is now the R
pipeline in `R/`. The Bayesian notebooks (`02a`–`02d`, `03`) have been removed.

## Next
- [ ] **Server run** of the R pipeline: smoke test first, then the full run (`server/README.md`).
- [ ] Unpack the results, re-execute `notebooks/02_jrt_results.ipynb`, and check the convergence,
  model-fit, cross-check and warning files (`server/README.md`, "What to check").
- [ ] Finalise `AUDIT.md` (checks marked [c] become [x] or [!]) and review `results/summary/REPORT.md`.
- [ ] Manuscript: re-run the paper pipeline from phase 3 (results-embedder, results-interpreter,
  outline, writer, reviewer) on `00`, `01` and `02_jrt_results` (see `manuscript/_status.md`).

## Open author decisions
- [x] Exclude raters with fewer than 15 ratings: decided 2026-10-22, applied in `R/01_data_design.R`.

## Optional (not in the spec)
- [ ] Per-rater rates of "action not recognised" (from `00`). Check whether they relate to severity
  or discrimination.
- [ ] Clustering of actions in matches or players.
- [ ] Secondary dimensions (technical correctness, aesthetic appeal) as validity evidence.
- [ ] Archive code and data (OSF/Zenodo DOI) for the data-availability statement.

## Possible extensions (deliberately NOT in the paper, decision 2026-10-27)
The paper sticks to the empirical findings of the actual rating study and keeps the analysis
simple. Projections and what-if scenarios that need extra design choices are left out. Ideas
that came up in the manuscript reviews and might be interesting later:
- Projection with selected rater sets (e.g. the k most or least informative raters) or with rater
  draws weighted by each rater's workload. Such sets need to account for the uncertainty of the
  rater parameters (simulate from parameter draws), otherwise they favour raters with few ratings.
- Number of ratings needed for a target reliability (.70, .80, .90) from the projection.
- Severity test: model without any rater effect (M0) vs M1, to test rater severity on its own.
- Likelihood-ratio test M1 vs M2 within one package (currently sirt vs mirt).
- Held-out predictive check of the GRM against the adjacent-category models.
- Diagnostics of the rejected parameter draws (which raters cause them).
