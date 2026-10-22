# Running the JRT notebook on a server

`02d_judge_response_theory.ipynb` fits two Bayesian JRT models (4 chains x 2000
draws + 2000 tuning each). This is too much memory for the laptop, so it runs on a
server. The notebook is self-contained: it needs only the cleaned ratings.

## What goes to the server

| File | Why |
|---|---|
| `notebooks/02d_judge_response_theory.ipynb` | the analysis |
| `data/processed/ratings_long_clean.csv` | cleaned ratings from `00` (rater IDs are pseudonymised, `R01`…) |
| `server/requirements-jrt.txt` | pinned Python packages |
| `server/run_jrt_server.sh` | sets up the environment, runs, summarises, packs results |

Do **not** copy `data/raw/` (it holds the pseudonym key and the raw sheet export).

## Steps

**1. Locally — pack the bundle** (from `data-analysis/creativity-ratings-psychometrics/`):

```bash
bash server/pack_for_server.sh          # -> jrt_server_bundle.tar.gz
scp jrt_server_bundle.tar.gz user@server:~/
```

**2. On the server — unpack and smoke-test** (needs Python 3.12; set `PYTHON=/path/to/python3.12`
if it is not on the PATH as `python3.12`):

```bash
mkdir -p ~/jrt && cd ~/jrt
tar -xzf ~/jrt_server_bundle.tar.gz
bash server/run_jrt_server.sh --smoke   # ~5 min + first-time pip install; outputs are throwaway
```

**3. On the server — full run**, inside `tmux`/`screen` (or `nohup`) so it survives a logout:

```bash
tmux new -s jrt
bash server/run_jrt_server.sh           # ~40-90 min, depending on the CPU
# detach: Ctrl-b d   reattach: tmux attach -t jrt
```

Resources: 4 CPU cores (one per chain) and **at least 8 GB free RAM**; 16 GB is
comfortable. The log `results/logs/02d_server_run_<timestamp>.log` records peak
memory and wall time. At the end, the script prints the convergence table, the
LOO comparison and the warnings.

**4. Copy the results back and unpack them in the analysis folder:**

```bash
scp user@server:~/jrt/jrt_results.tar.gz .
tar -xzf jrt_results.tar.gz             # overwrites the notebook + jrt tables/figures/logs
```

`jrt_results.tar.gz` contains the executed notebook (with outputs), all
`results/tables/*jrt*.csv`, `results/figures/fig_jrt_*` and the run log. The fitted
models (`results/models/jrt_*.nc`, ~1-2 GB) are left on the server. Copy them only if
you want to re-inspect the posteriors; `results/models/` is gitignored.

## What to check before the paper is drafted

- `jrt_convergence_by_group.csv`: every group has `max_r_hat` < 1.01 and
  `min_ess_bulk`/`min_ess_tail` > 400. `model_diagnostics_jrt.csv` has 0 divergences.
- `jrt_equal_discrimination_convergence.csv`: the same for the nested model.
- `jrt_loo_comparison.csv`: `share_pareto_k_gt_0.7`. If it is above 0.05, PSIS-LOO
  is unreliable for those ratings; see the note in the main conversation.
- `warnings_log_jrt.csv` should be empty, or contain only warnings you accept.

If convergence fails, raise `JRT_TUNE` (e.g. `JRT_TUNE=4000 bash server/run_jrt_server.sh`).
The defaults in the notebook stay what the paper reports.
