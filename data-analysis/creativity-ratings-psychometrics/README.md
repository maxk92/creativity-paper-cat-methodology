# Psychometric analysis of incompletely crossed creativity ratings

Creativity ratings (CAT-style, unipolar 7-point scale) of football actions. Raters
were assigned to actions in an unbalanced, incompletely crossed design, so each
action has a different number of ratings from a different subset of raters.

The central model is **judge response theory (JRT) as a graded response model
(GRM)**: raters are the items, actions (products) are the persons, and the model is
fitted by marginal maximum likelihood in `mirt`. Its scores, information and
reliability are what the paper uses. An adjacent-category ladder (rating scale
model / MFRM → partial credit model → generalized partial credit model) and two
naive indices (Cronbach's α, Krippendorff's α) are computed for comparison only.
`../../reference/jrt_reference.json` states what a JRT analysis should report and
how to word it; [`AUDIT.md`](AUDIT.md) is the history of the October 2026 audit
from which this pipeline was condensed (2026-11-10).

## Pipeline

| Step | File | Runs | What it does |
|---|---|---|---|
| 0 | `notebooks/00_data_loading_preprocessing.ipynb` | local | Downloads the ratings (Google Sheet), joins StatsBomb event details, pseudonymises raters (`R01`…), drops "action not recognised" ratings, resolves duplicates (latest timestamp kept). Writes `data/processed/ratings_long_clean.csv` and `results/tables/` |
| 1 | `R/01_grm.R` | local, ~3 min | Data basis (rater exclusion, wide matrix, category use, connectivity, descriptives), GRM fit, rater parameters with SEs, EAP scores with posterior SDs, rater and panel information, reliability (empirical, model-based, per product), raw mean vs GRM score, figures; then the supplementary diagnostics: 95% intervals from parameter draws, infit/outfit and S-X², Q3, C2 |
| 2 | `notebooks/01_data_overview.ipynb` | local | Descriptive design overview for the manuscript (degree distributions, response styles, rating distribution). Reads `results/data/excluded_raters.csv`, so it needs step 1 |
| 3 | `R/02_comparison.R` | local, ~20 min | M1 RSM/MFRM (`sirt::rm.facets`), M2 PCM and M3 GPCM (`mirt`), information criteria, LR tests, score agreement, rater parameters by model, M1 rater fit, per-model marginal reliability; GRM refitted on all raters (sensitivity); Cronbach's α and Krippendorff's α with bootstrap CIs (the slow part); the reliability overview table |
| 4 | `R/03_simulations.R` | local, ~3 min | Reliability by number of ratings, simulated from the fitted GRM: k = 1…10 random raters per product, and the actual design topped up to at least 4 ratings per product |
| 5 | `notebooks/02_jrt_results.ipynb` | local, seconds | Display notebook with the **main-paper** tables and figures (14 labelled objects) |
| 6 | `notebooks/03_jrt_supplement.ipynb` | local, seconds | Display notebook with the **supplementary** tables and figures (32 labelled objects) |

`R/jrt_functions.R` holds the shared settings (paths, seed `20260713`, mirt
settings, the I/(I+1) reliability helpers). `notebooks/jrt_display.py` holds the
table and figure formatting used by notebooks 02 and 03. The R scripts write CSVs
and figures; the notebooks only display them (a few figures are drawn in the
notebook from the CSVs). `mirt` is used directly rather than through the `jrt`
package, because the pipeline needs the mirt object itself (information,
simulation, parameter draws, fixed-parameter refits).

## Running

```bash
cd notebooks && ../../../.venv/bin/jupyter nbconvert --to notebook --execute --inplace 00_data_loading_preprocessing.ipynb && cd ..
bash run_pipeline.sh            # R/01 ... R/03, then notebooks 02 and 03 (~25 min, log in results/logs/)
cd notebooks && ../../../.venv/bin/jupyter nbconvert --to notebook --execute --inplace 01_data_overview.ipynb
```

- `JRT_QUICK=1 bash run_pipeline.sh` lowers the draws, imputations, bootstraps and
  replications for a quick check; those outputs are not for the paper.
- `JRT_INPUT=<csv>` makes the R scripts read another cleaned file, e.g. an archived
  data freeze (the input is printed at the start of `R/01_grm.R`); `JRT_DUPLICATES=<csv>`
  does the same for the duplicate log of notebook 00, which only feeds two counts in the
  design summary.
- R packages: `Rscript install_r_packages.R`. Python (notebooks): `pip install -r requirements.txt`
  in the repo venv.

## Data behind the committed results

The committed `results/` were computed from the data freeze of 2026-11-04
(9,077 cleaned ratings, 28 raters; 9,046 ratings of 3,669 products by 24 raters
after excluding raters with fewer than 15 ratings), which is also the data behind
the manuscript. Verification copies of that file and of the matching duplicate log are kept locally as
`data/processed/ratings_long_clean_freeze_2026-11-04.csv` and
`data/processed/flagged_duplicate_rater_action_pairs_freeze_2026-11-04.csv` (gitignored);
the committed results reproduce the pre-2026-11-10 results exactly with
`JRT_INPUT=... JRT_DUPLICATES=... bash run_pipeline.sh`.
`data/processed/ratings_long_clean.csv` as regenerated by notebook 00 on 2026-11-10
already contains additional offline ratings (9,471 ratings, 3,840 products, a new
rater R29 with one rating); rerunning `run_pipeline.sh` uses that file and changes
every number in the notebooks, so the manuscript would need the results pipeline
again.

## Manuscript embeds

The manuscript embeds objects by label (`{{< embed <notebook>#<label> >}}`); labels
are unique across the two notebooks and stable.

- `02_jrt_results.ipynb` (main text): `tbl-design-summary`, `fig-category-usage-shares`,
  `tbl-model-fit`, `tbl-grm-reliability-by-n`, `fig-grm-reliability-observed-vs-simulated`,
  `fig-m1-rater-severity`, `tbl-grm-rater-parameters`, `fig-grm-rater-discrimination-ci`,
  `fig-grm-category-response-functions`, `fig-grm-rater-information-ci`, `fig-grm-rater-information`,
  `tbl-raw-mean-vs-grm`, `fig-raw-mean-vs-theta`, `tbl-score-agreement`.
- `03_jrt_supplement.ipynb` (Supplementary Material, plus three tables that the main text
  embeds from there: `tbl-reliability-overview`, `tbl-grm-reliability-min-ratings`,
  `tbl-rater-overview`): all other labels; see the notebook.

## Folder layout

```text
.
├── README.md, AUDIT.md, ANALYSIS_TODO.md
├── requirements.txt          Python (notebooks)
├── install_r_packages.R      R (pipeline in R/)
├── run_pipeline.sh           R/01 ... R/03 + notebooks 02, 03
├── R/                        jrt_functions.R, 01_grm.R, 02_comparison.R, 03_simulations.R
├── notebooks/                00, 01, 02, 03, jrt_display.py
├── data/                     gitignored, regenerated by 00
└── results/
    ├── tables/, figures/     outputs of 00 and 01
    ├── data/                 excluded_raters.csv (read by 01), ratings_wide.csv (gitignored)
    ├── main/                 CSVs and figures/ behind the main-paper objects
    ├── supplement/           CSVs and figures/ behind the supplementary objects
    ├── models/               fitted models (.rds, gitignored)
    └── logs/                 run logs, session_info.txt
```

A CSV goes to `results/main/` if a main-paper object is built from it, otherwise
to `results/supplement/`; `read_res()` in `jrt_display.py` searches both, so the
split is a reporting classification, not a code dependency.

## Models in brief

- **GRM (retained scoring model).** P(X_nj ≥ k | θ_n) = 1 / (1 + exp(−a_j (θ_n − b_jk))),
  θ ~ N(0, 1), rater-specific discrimination a_j and ordered thresholds b_jk.
  Product scores are EAP estimates with posterior SD; conditional reliability
  rel(θ) = I(θ)/(I(θ) + 1) with SE(θ) = 1/√(I(θ) + 1). The **empirical marginal
  reliability** Var(θ̂)/(Var(θ̂) + mean PSD²) of the actual scores is the primary
  reliability figure; the model-based marginal reliability refers to a hypothetical
  product rated by all raters.
- **Ladder.** M1 RSM (shared thresholds shifted by rater severity, equal slopes;
  `sirt::rm.facets`, the many-facet Rasch model), M2 PCM (rater-specific thresholds),
  M3 GPCM (rater-specific thresholds and slopes). LR tests M1 vs M2 (thresholds) and
  M2 vs M3 (discriminations); the GRM is compared by information criteria only.
  M1 uses `sirt` because `mirt` recodes each rater's observed categories and its RSM
  refuses raters with different numbers of categories.
- **Naive indices.** Cronbach's α (consistency of the unweighted rater mean,
  pairwise covariances and the largest fully crossed block) and ordinal
  Krippendorff's α (agreement of single ratings).

## Notes

- Rater IDs are pseudonymised in `00`; the key in `data/raw/` never leaves the machine.
  IDs are permanent: raters in the key keep their pseudonym and new raters get the
  next free number. The key is gitignored and is the only record of the assignment.
- To look up a rater in the raw data: `source("R/jrt_functions.R"); switch_rater_ids(c("R18", "R21"))`
  (and `switch_rater_ids(ids, "pseudonym")` back). Never write its output to `results/`.
  `notebooks/local_rater_lookup.ipynb` (gitignored) shows the original IDs next to the rater tables.
- Only the creativity rating is modelled. `technical_correctness` and `aesthetic_appeal`
  stay in the data but go into no model.
- Raters with fewer than 15 ratings (`MIN_RATINGS_PER_RATER` in `R/jrt_functions.R`) are
  excluded from the whole pipeline (`results/data/excluded_raters.csv`). All 7 categories
  are kept; raters with unused categories are flagged in `results/supplement/category_usage.csv`.
- `reports/jrt_results_summary.qmd` is an older discussion report that reads the
  pre-2026-11-10 result paths; its rendered html/pdf are kept as they are.
