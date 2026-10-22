# Running the JRT pipeline on a server

The R pipeline in `R/` (`01_data_design.R` … `06_summary.R`) fits the GRM, the
model ladder (RSM via `sirt::rm.facets`, PCM, GPCM) and the naive indices. The
model fits, the S-X² multiple imputation, C2 and the Krippendorff bootstrap are
run on a server; only `R/01_data_design.R` is light enough for the laptop.

## What goes to the server

`server/pack_jrt_audit_for_server.sh` bundles the R scripts, the cleaned ratings
(`data/processed/ratings_long_clean.csv`, pseudonymised rater IDs), the duplicate
report from `00`, `install_r_packages.R` and the runner. Do **not** copy
`data/raw/` (it holds the pseudonym key).

## Steps

```bash
# 1. locally, in data-analysis/creativity-ratings-psychometrics/
bash server/pack_jrt_audit_for_server.sh
scp jrt_audit_server_bundle.tar.gz user@server:~/

# 2. on the server
mkdir -p ~/jrt_audit && cd ~/jrt_audit && tar -xzf ~/jrt_audit_server_bundle.tar.gz
Rscript install_r_packages.R                 # first time only
bash server/run_jrt_audit_server.sh --smoke  # 2 imputations, 20 bootstraps; not for the paper

# 3. full run, inside tmux so it survives a logout
tmux new -s jrt_audit
bash server/run_jrt_audit_server.sh

# 4. locally: copy back and unpack in the analysis folder
scp user@server:~/jrt_audit/jrt_audit_results.tar.gz .
tar -xzf jrt_audit_results.tar.gz
```

Needs R ≥ 4.3. A single core is enough; the log
`results/logs/jrt_audit_server_run_<timestamp>.log` records wall time and peak memory.

## What to check

- `results/grm/convergence.csv`: `converged = TRUE`, `information_matrix_pd = TRUE`.
- `results/comparison/model_fit.csv`: all models estimated and converged.
- `results/comparison/software_crosscheck.csv`: `abs_difference` close to 0.
- `results/logs/warnings_jrt_audit_*.csv`: every warning is understood.
