#!/usr/bin/env bash
# Run ON THE SERVER from the unpacked bundle folder:
#   bash server/run_jrt_server.sh            # full run (4 chains x 2000 draws, both models)
#   bash server/run_jrt_server.sh --smoke    # quick check (4 chains x 60 draws), ~5 min
#
# Creates a venv (first run only), executes 02d_judge_response_theory.ipynb in place,
# prints the convergence summary and packs the outputs into jrt_results.tar.gz.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

SMOKE=0
[[ "${1:-}" == "--smoke" ]] && SMOKE=1

PYTHON="${PYTHON:-python3.12}"
VENV="$ROOT/.venv-jrt"

# --- environment -------------------------------------------------------------
if [[ ! -x "$VENV/bin/python" ]]; then
  echo ">> Creating venv with $PYTHON"
  "$PYTHON" -m venv "$VENV"
  "$VENV/bin/pip" install --upgrade pip
  "$VENV/bin/pip" install -r server/requirements-jrt.txt
  "$VENV/bin/python" -m ipykernel install --prefix "$VENV" --name python3
fi
export PATH="$VENV/bin:$PATH"
export JUPYTER_PATH="$VENV/share/jupyter"

# One BLAS thread per chain: PyMC runs 4 chains in parallel processes.
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
# Separate PyTensor compile cache, so it does not clash with other users/projects.
export PYTENSOR_FLAGS="compiledir=$ROOT/.pytensor_cache"

mkdir -p results/tables results/figures results/models results/logs

STAMP="$(date +%Y%m%d_%H%M%S)"
LOG="results/logs/02d_server_run_${STAMP}.log"
NB="notebooks/02d_judge_response_theory.ipynb"

if [[ $SMOKE -eq 1 ]]; then
  export JRT_DRAWS=60 JRT_TUNE=60
  RUN_NB="notebooks/_smoke_02d.ipynb"
  cp "$NB" "$RUN_NB"
  echo ">> SMOKE TEST (60 draws) - outputs are NOT for the paper"
else
  unset JRT_DRAWS JRT_TUNE
  RUN_NB="$NB"
  echo ">> FULL RUN (4 chains x 2000 draws + 2000 tuning, two models)"
fi

# --- run -----------------------------------------------------------------------
TIME_CMD=""
[[ -x /usr/bin/time ]] && TIME_CMD="/usr/bin/time -v"   # peak memory in the log, if available

echo ">> Started $(date), log: $LOG"
( cd notebooks && $TIME_CMD jupyter nbconvert --to notebook --execute --inplace \
    --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.kernel_name=python3 \
    "$(basename "$RUN_NB")" ) > "$LOG" 2>&1 || { echo "!! Notebook failed - see $LOG"; tail -40 "$LOG"; exit 1; }
echo ">> Finished $(date)"
grep -E "Maximum resident set size|Elapsed \(wall clock\)" "$LOG" || true

# --- summary ---------------------------------------------------------------------
echo; echo "== Convergence by parameter group (JRT) =="
cat results/tables/jrt_convergence_by_group.csv
echo; echo "== Equal-discrimination model =="
cat results/tables/jrt_equal_discrimination_convergence.csv
echo; echo "== LOO comparison =="
cat results/tables/jrt_loo_comparison.csv
echo; echo "== Warnings =="
cat results/tables/warnings_log_jrt.csv

if [[ $SMOKE -eq 1 ]]; then
  rm -f "$RUN_NB"
  echo; echo ">> Smoke test OK. Start the full run with: bash server/run_jrt_server.sh"
  exit 0
fi

# --- pack results ------------------------------------------------------------------
tar -czf jrt_results.tar.gz \
  "$NB" \
  results/tables/*jrt*.csv \
  results/figures/fig_jrt_* \
  results/logs/session_info_jrt.json \
  "$LOG"
echo; echo ">> Results packed: $ROOT/jrt_results.tar.gz"
echo "   Fitted models (large, optional): $ROOT/results/models/jrt_*.nc"
