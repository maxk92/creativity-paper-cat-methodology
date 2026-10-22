#!/usr/bin/env bash
# Run LOCALLY. Packs everything the server needs for the JRT audit pipeline
# into jrt_audit_server_bundle.tar.gz (in the analysis folder), keeping the layout.
set -euo pipefail

ANALYSIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ANALYSIS_DIR"

FILES=(
  R/jrt_functions.R
  R/01_data_design.R
  R/02_grm.R
  R/03_grm_information.R
  R/04_model_comparison.R
  R/05_naive_indices.R
  R/06_summary.R
  data/processed/ratings_long_clean.csv
  results/tables/flagged_duplicate_rater_action_pairs.csv
  install_r_packages.R
  server/run_jrt_audit_server.sh
)
for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || { echo "Missing: $f (run 00_data_loading_preprocessing.ipynb first?)" >&2; exit 1; }
done

tar -czf jrt_audit_server_bundle.tar.gz "${FILES[@]}"
echo "Created $ANALYSIS_DIR/jrt_audit_server_bundle.tar.gz"
tar -tzf jrt_audit_server_bundle.tar.gz
