#!/usr/bin/env bash
# Runs the JRT pipeline (R/01 ... R/03, ~25 min) and re-executes the two display
# notebooks. Run from the analysis folder:  bash run_pipeline.sh
# JRT_QUICK=1 bash run_pipeline.sh  gives a quick check (outputs not for the paper).
# Notebooks 00 and 01 are run separately (see README.md).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
mkdir -p results/logs
LOG="results/logs/run_$(date +%Y%m%d_%H%M%S).log"
echo ">> log: $LOG"
for s in 01_grm 02_comparison 03_simulations; do
  echo ">> R/$s.R  ($(date +%H:%M:%S))" | tee -a "$LOG"
  Rscript "R/$s.R" >> "$LOG" 2>&1 || { echo "!! $s failed - see $LOG"; tail -30 "$LOG"; exit 1; }
done
echo ">> notebooks  ($(date +%H:%M:%S))" | tee -a "$LOG"
../../.venv/bin/jupyter nbconvert --to notebook --execute --inplace \
  notebooks/02_jrt_results.ipynb notebooks/03_jrt_supplement.ipynb >> "$LOG" 2>&1
echo ">> done  ($(date +%H:%M:%S))" | tee -a "$LOG"
