#!/usr/bin/env bash
# Run LOCALLY. Packs everything the server needs to run the JRT notebook into
# jrt_server_bundle.tar.gz (in the analysis folder), keeping the folder layout.
set -euo pipefail

ANALYSIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ANALYSIS_DIR"

FILES=(
  notebooks/02d_judge_response_theory.ipynb
  data/processed/ratings_long_clean.csv
  server/requirements-jrt.txt
  server/run_jrt_server.sh
)
for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || { echo "Missing: $f (run 00_data_loading_preprocessing.ipynb first?)" >&2; exit 1; }
done

tar -czf jrt_server_bundle.tar.gz "${FILES[@]}"
echo "Created $ANALYSIS_DIR/jrt_server_bundle.tar.gz"
tar -tzf jrt_server_bundle.tar.gz
