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
- [ ] Exclude raters with fewer than 15 ratings (R20, R21, R22)? Currently they are kept and flagged.
  R20 and R22 have an internal category gap, so their thresholds are not comparable with those of
  other raters.
- [ ] R22 is still in the cleaned data (2 ratings). The sheet update removed only the former R23,
  who had only "not recognised" ratings.

## Optional (not in the spec)
- [ ] Per-rater rates of "action not recognised" (from `00`). Check whether they relate to severity
  or discrimination.
- [ ] Clustering of actions in matches or players.
- [ ] Secondary dimensions (technical correctness, aesthetic appeal) as validity evidence.
- [ ] Archive code and data (OSF/Zenodo DOI) for the data-availability statement.
