# Analysis to-do list (JRT paper)

Status as of 2026-10-21. The paper uses `00`, `01` and `02d`. Items are grouped by priority.
**Server** = needs new MCMC sampling (run via `server/run_jrt_server.sh`); **local** = runs on the laptop
from the saved fits (`JRT_USE_SAVED_FITS=1`) or the CSVs.

## Done
- [x] JRT converged (4 x 2000 draws; R-hat < 1.005, ESS > 1,500, 0 divergences), PPC, trace plots
- [x] Equal-discrimination model fitted in `02d`; PSIS-LOO comparison (Pareto-k > 0.7: 2.8% / 0.1%)
- [x] Marginal reliability / D-study with 95% posterior intervals, equal and rating-weighted rater pool
- [x] Discrimination vs. descriptive response style (Spearman correlations with central/extreme rate, SD)
- [x] Labelled, display-only notebook cells for embedding; pseudonymised rater IDs

## Recommended (directly answer review points)
- [ ] **Grouped K-fold cross-validation** (server). PSIS-LOO leaves out single ratings, and the
  Pareto-k share differs between models (2.8% vs. 0.1%). 10-fold CV with folds grouped by action
  (the whole action left out, its θ predicted from the prior) tests whether rater-specific
  discrimination improves prediction for *new actions*. Cost: 2 models x 10 refits.
- [ ] **Rater-specific thresholds** (server). Shared thresholds let differences in scale use
  (central tendency) be absorbed by a_j (see the response-style correlation table). Options:
  (a) full JRT-GRM with b_jk per rater, with hierarchical shrinkage towards the shared thresholds;
  (b) a lighter "scale-stretch" variant (rater-specific threshold spread s_j: τ_jk = s_j·τ_k).
  Compare with the current model by K-fold/LOO and check whether the a_j ranking survives.
- [ ] **Prior sensitivity** (server, cheap per fit). Refit with wider/narrower priors on
  σ_log a (Exp(1), Exp(4)) and σ_λ; report the change in a_j, λ_j, elpd and reliability.
  Alternatively power-scaling sensitivity (priorsense-style) from the existing fits.
- [ ] **Per-rater "action not recognised" rates** (local, from `00`/raw). Missingness is
  rater-dependent and is excluded before modelling; describe it per rater and check whether it
  correlates with leniency or discrimination.

## Optional — robustness and extensions
- [ ] **Compare other measurement models** (server). Within the same Bayesian framework:
  - generalized partial credit model (GPCM) form of JRT instead of the graded response form;
  - many-facet Rasch / rating-scale model with a_j ≡ 1 and freely estimated σ_θ (the classical
    MFRM), to state precisely how the equal-discrimination model relates to MFRM;
  - partial credit / rater-specific threshold models (see above).
  Compare by grouped K-fold CV; report rank agreement of the fair scores across models.
- [ ] **Score comparison with simple means** (local). Only if the paper should make claims about
  mean scores: correlation and rank shifts between raw means and JRT θ, and how many actions
  change ranks (deciles). Currently out of scope — the draft must not claim this without it.
- [ ] **Clustering of actions** (server). Actions are nested in matches/players; add match (or
  player) random effects to θ, or at least report the intraclass share of θ by match.
- [ ] **Non-normal latent distribution** (server). Ratings are right-skewed (categories 1-2
  dominate); try a skew-normal or mixture prior for θ and compare the fit and the information
  pattern at the low end.
- [ ] **Shrinkage of single-rated actions** (local). Describe how strongly θ of actions with one
  rating is pulled to 0 (posterior SD vs. n_ratings is in `jrt_score_precision_by_n.csv`); add
  a recommendation for the minimum number of ratings per action for downstream use.
- [ ] **Rater drift** (local/server). Rating order is available; a descriptive Spearman check is
  in `01`. A model with time-varying leniency (λ_j + slope_j·order) would test drift formally.
- [ ] **Simulation-based D-study** (server). Simulate new designs (k judges per action drawn from
  the pool, with realistic connectivity) from the posterior, refit, and compare the realised score
  reliability with the analytic marginal reliability.
- [ ] **Secondary dimensions** (local). Technical correctness and aesthetic appeal are collected;
  correlate them with θ (convergent/discriminant evidence) — possibly a separate paper.
- [ ] **Validity evidence** (local, needs event data). Relate θ to action type or outcome
  (e.g. proximity to goals, as in Kempe & Memmert, 2018) for criterion validity.

## Housekeeping
- [ ] Re-run or delete the stale outputs of `02a`–`02c`, `03` and the R qmd (still carry old rater IDs).
- [ ] Record package versions for `00`/`01` (session info) for the reproducibility statement.
- [ ] Archive code and data (OSF/Zenodo DOI) for the data-availability statement.
