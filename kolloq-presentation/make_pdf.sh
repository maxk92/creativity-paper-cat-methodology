#!/usr/bin/env bash
# Rebuilds the slide PDF from kolloq-slides.qmd via quarto render + decktape.
#
#   ./make_pdf.sh              -> kolloq-slides.pdf            (one page per slide)
#   ./make_pdf.sh --fragments  -> kolloq-slides-fragments.pdf  (one page per reveal step)
#
# decktape hangs on the self-contained HTML (the embedded video clips), so the
# PDF is built from a copy of the deck rendered with embed-resources: false.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

QMD="kolloq-slides-pdf.qmd"
HTML="kolloq-slides-pdf.html"
PORT=8744

FRAGMENTS=0
for arg in "$@"; do
  case "$arg" in
    --fragments) FRAGMENTS=1 ;;
    *) echo "unknown option: $arg" >&2; exit 2 ;;
  esac
done

if [[ "$FRAGMENTS" -eq 1 ]]; then
  PDF="kolloq-slides-fragments.pdf"
  DECKTAPE_EXTRA=(--fragments)
else
  PDF="kolloq-slides.pdf"
  DECKTAPE_EXTRA=()
fi

sed 's/^embed-resources: true/embed-resources: false/; s/^    embed-resources: true/    embed-resources: false/' kolloq-slides.qmd > "$QMD"
quarto render "$QMD" --to revealjs

python3 -m http.server "$PORT" >/tmp/kolloq-slides-httpserver.log 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT

for _ in $(seq 1 20); do
  curl -sf "http://localhost:$PORT/$HTML" >/dev/null && break
  sleep 0.5
done

timeout 600 decktape reveal --size 1280x720 "${DECKTAPE_EXTRA[@]}" \
  --pdf-title "How many ratings, and from whom? (colloquium)" \
  --pdf-author "Maximilian Klemp-Weins" \
  "http://localhost:$PORT/$HTML" "$PDF"

rm -rf "$QMD" "$HTML" "${HTML%.html}_files"
echo "Wrote $PDF"
