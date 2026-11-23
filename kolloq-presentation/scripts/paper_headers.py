"""Header screenshots of the two Barbot et al. (2019) PACA papers for slide 5.

Renders page 1 of each PDF at 150 dpi with pdftoppm and crops the journal
banner, title and author block. Writes img/barbot2019_header.png and
img/barbot2019b_header.png.

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/paper_headers.py
"""

import subprocess
import tempfile
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
LIT = Path("/home/max/drive/KNOWLEDGE/phd_lit")

# pdf stem -> (output name, crop box in px at 150 dpi on a 1238 x 1650 page)
PAPERS = {
    "barbot2019": ("barbot2019_header.png", (80, 50, 1160, 455)),
    "barbot2019b": ("barbot2019b_header.png", (80, 50, 1160, 455)),
}


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for stem, (out, box) in PAPERS.items():
            prefix = Path(tmp) / stem
            subprocess.run(
                ["pdftoppm", "-r", "150", "-f", "1", "-l", "1", "-png", str(LIT / f"{stem}.pdf"), str(prefix)],
                check=True,
            )
            page = next(Path(tmp).glob(f"{stem}-*.png"))
            im = Image.open(page).convert("RGB").crop(box)
            im.save(IMG / out)
            print("wrote", out, im.size)


if __name__ == "__main__":
    main()
