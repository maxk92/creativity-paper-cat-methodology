#!/usr/bin/env bash
# Run ON THE SERVER from the unpacked bundle folder:
#   bash server/run_jrt_audit_server.sh            # full run (R/01 ... R/06)
#   bash server/run_jrt_audit_server.sh --smoke    # quick check: 2 imputations, 20 bootstraps
#
# Runs the JRT audit pipeline (mirt/sirt, MML) with Rscript, logs everything,
# prints the key tables and packs the outputs into jrt_audit_results.tar.gz.
# Needs R >= 4.3 with the packages in install_r_packages.R (mirt, sirt, irr,
# psych, igraph, tidyverse). Install once with: Rscript install_r_packages.R
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

SMOKE=0
[[ "${1:-}" == "--smoke" ]] && SMOKE=1
if [[ $SMOKE -eq 1 ]]; then
  export JRT_SMOKE=1
  echo ">> SMOKE TEST - outputs are NOT for the paper"
else
  unset JRT_SMOKE
  echo ">> FULL RUN"
fi

mkdir -p results/logs
STAMP="$(date +%Y%m%d_%H%M%S)"
LOG="results/logs/jrt_audit_server_run_${STAMP}.log"
TIME_CMD=""
[[ -x /usr/bin/time ]] && TIME_CMD="/usr/bin/time -v"   # peak memory in the log, if available

Rscript -e 'pk <- c("mirt","sirt","irr","psych","igraph","dplyr","tidyr","readr","ggplot2","svglite");
            miss <- pk[!vapply(pk, requireNamespace, logical(1), quietly = TRUE)];
            if (length(miss)) stop("Missing R packages: ", paste(miss, collapse = ", "))'

echo ">> Started $(date), log: $LOG"
for s in 01_data_design 02_grm 03_grm_information 04_model_comparison 05_naive_indices 06_summary; do
  echo ">> $s  ($(date +%H:%M:%S))" | tee -a "$LOG"
  $TIME_CMD Rscript "R/$s.R" >> "$LOG" 2>&1 || { echo "!! $s failed - see $LOG"; tail -40 "$LOG"; exit 1; }
done
echo ">> Finished $(date)"
grep -E "Maximum resident set size|Elapsed \(wall clock\)" "$LOG" || true

echo; echo "== GRM convergence =="; cat results/grm/convergence.csv
echo; echo "== Model fit ==";        cat results/comparison/model_fit.csv
echo; echo "== LR tests ==";         cat results/comparison/lr_tests.csv
echo; echo "== Reliability overview =="; cat results/summary/reliability_overview.csv
echo; echo "== Warnings =="; cat results/logs/warnings_jrt_audit_*.csv

if [[ $SMOKE -eq 1 ]]; then
  echo; echo ">> Smoke test OK. Start the full run with: bash server/run_jrt_audit_server.sh"
  exit 0
fi

tar -czf jrt_audit_results.tar.gz \
  --exclude='results/data/ratings_long.csv' --exclude='results/data/ratings_wide.csv' \
  results/data results/grm results/comparison results/naive results/summary \
  results/logs/session_info_jrt_audit_*.txt results/logs/warnings_jrt_audit_*.csv "$LOG"
echo; echo ">> Results packed: $ROOT/jrt_audit_results.tar.gz"
echo "   (includes the model .rds files in results/grm and results/comparison)"
