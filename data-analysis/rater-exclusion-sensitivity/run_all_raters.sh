#!/usr/bin/env bash
# Re-runs the main JRT pipeline (R/01-03, unchanged code) on ALL raters by lowering
# MIN_RATINGS_PER_RATER from 15 to 2 in a temporary copy of R/ (R29, with one rating
# in one category, is not estimable and stays out). Same input file; no Krippendorff
# bootstrap. Result CSVs go to all_raters_results/ for all_raters_sensitivity.qmd.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
PSY=../creativity-ratings-psychometrics
WORK=$(mktemp -d)
cp -r "$PSY/R" "$WORK/R"
sed -i 's/^MIN_RATINGS_PER_RATER <- 15L/MIN_RATINGS_PER_RATER <- 2L/' "$WORK/R/jrt_functions.R"
grep -q "MIN_RATINGS_PER_RATER <- 2L" "$WORK/R/jrt_functions.R"
export JRT_INPUT="$(realpath $PSY/data/processed/ratings_long_clean.csv)"
export JRT_DUPLICATES="$(realpath $PSY/results/tables/flagged_duplicate_rater_action_pairs.csv)"
export JRT_SKIP_KRIPP_BOOT=1
for s in 01_grm 02_comparison 03_simulations; do
  echo ">> $s ($(date +%H:%M:%S))"; Rscript "$WORK/R/$s.R" > "$WORK/$s.log" 2>&1 || { tail -30 "$WORK/$s.log"; exit 1; }
done
rm -rf all_raters_results && mkdir -p all_raters_results
cp "$WORK"/results/main/*.csv "$WORK"/results/supplement/*.csv all_raters_results/
cp "$WORK"/results/data/excluded_raters.csv all_raters_results/
rm -rf "$WORK"
echo ">> done: all_raters_results/"
