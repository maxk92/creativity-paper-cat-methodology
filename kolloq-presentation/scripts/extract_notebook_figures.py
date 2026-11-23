"""Export labelled figure outputs of the results notebooks as PNG files.

The figures listed in FIGS exist only as outputs inside the executed notebooks
(no file on disk). This writes them to img/nb/<label>.png so the slides can
size them freely without the embed shortcode.

Run from kolloq-presentation/:
  python3 -I scripts/extract_notebook_figures.py
"""

import base64
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NB_DIR = HERE.parent.parent / "data-analysis" / "creativity-ratings-psychometrics" / "notebooks"
OUT = HERE.parent / "img" / "nb"

FIGS = {
    "02_jrt_results.ipynb": [
        "fig-category-usage-shares",
        "fig-grm-reliability-observed-vs-simulated",
        "fig-m1-rater-severity",
        "fig-grm-rater-discrimination-ci",
        "fig-grm-rater-information-ci",
    ],
    "03_jrt_supplement.ipynb": [
        "fig-design-ratings-per-product",
    ],
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for nb_name, labels in FIGS.items():
        nb = json.loads((NB_DIR / nb_name).read_text())
        for label in labels:
            cell = next(
                c for c in nb["cells"]
                if c["cell_type"] == "code" and f"#| label: {label}" in "".join(c["source"])
            )
            png = next(o["data"]["image/png"] for o in cell["outputs"] if "image/png" in o.get("data", {}))
            (OUT / f"{label}.png").write_bytes(base64.b64decode(png))
            print("wrote", OUT / f"{label}.png")


if __name__ == "__main__":
    main()
