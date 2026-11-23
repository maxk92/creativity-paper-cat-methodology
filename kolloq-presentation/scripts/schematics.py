"""Synthetic schematic figures (no data) for the slides on rater problems and IRT.

Writes to img/:
  schematic_severity.{svg,png}        two raters with the same slope, shifted (lenient vs strict)
  schematic_category_use.{svg,png}    two raters' rating distributions: full range vs compressed
  schematic_discrimination.{svg,png}  two raters with the same centre, steep vs flat
  irt_icc.{svg,png}                   item characteristic curves of three dichotomous items

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/schematics.py
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "img"
NAVY = "#002855"
BLUE = "#619CFF"
ORANGE = "#E69F00"
GREY = "#9aa3ad"

STYLE = {"font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11}


def expected_rating(theta, a, centre):
    """A smooth 1-7 expected-rating curve centred at `centre` with slope `a`."""
    return 1 + 6 / (1 + np.exp(-a * (theta - centre)))


def strip(ax):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(color="#e6ecfa")


def save(fig, name, dpi=200):
    fig.tight_layout()
    fig.savefig(IMG / f"{name}.svg")
    fig.savefig(IMG / f"{name}.png", dpi=dpi)
    print("wrote", name)


def severity():
    theta = np.linspace(-3, 3, 300)
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    ax.plot(theta, expected_rating(theta, 1.3, -0.9), color=BLUE, lw=2.5, label="lenient rater")
    ax.plot(theta, expected_rating(theta, 1.3, 0.9), color=NAVY, lw=2.5, label="strict rater")
    ax.axvline(0, color=GREY, lw=1, ls=":")
    ax.annotate("", xy=(0, expected_rating(0, 1.3, -0.9)), xytext=(0, expected_rating(0, 1.3, 0.9)),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.8))
    ax.text(0.12, 4.0, "same action,\ndifferent rating", color=ORANGE, fontsize=9, va="center")
    ax.set_xlabel("Creativity of the action")
    ax.set_ylabel("Expected rating")
    ax.set_ylim(1, 7)
    ax.set_yticks(range(1, 8))
    ax.set_xticks([])
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    strip(ax)
    save(fig, "schematic_severity")


def category_use():
    cats = np.arange(1, 8)
    full = np.array([0.08, 0.14, 0.18, 0.20, 0.18, 0.14, 0.08])
    compressed = np.array([0.0, 0.22, 0.36, 0.30, 0.12, 0.0, 0.0])
    fig, axes = plt.subplots(1, 2, figsize=(4.6, 3.0), sharey=True)
    for ax, sh, col, title in zip(axes, (full, compressed), (BLUE, NAVY),
                                  ("uses the whole scale", "compresses: never 1, 6, 7")):
        ax.bar(cats, sh, color=col, edgecolor="white")
        ax.set_xticks(cats)
        ax.set_title(title, fontsize=10, color=col)
        ax.set_xlabel("Rating given")
        ax.set_yticks([])
        strip(ax)
        ax.grid(False)
    axes[0].set_ylabel("Share of the rater's ratings")
    save(fig, "schematic_category_use")


def discrimination():
    theta = np.linspace(-3, 3, 300)
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    ax.plot(theta, expected_rating(theta, 2.5, 0), color=BLUE, lw=2.5, label="separates sharply")
    ax.plot(theta, expected_rating(theta, 0.6, 0), color=NAVY, lw=2.5, label="barely separates")
    for x in (-1.2, 1.2):
        ax.axvline(x, color=GREY, lw=1, ls=":")
    for a, col, xarr, ty in ((2.5, BLUE, 1.55, 2.3), (0.6, NAVY, 2.2, 4.0)):
        lo, hi = expected_rating(-1.2, a, 0), expected_rating(1.2, a, 0)
        ax.plot([-1.2, 1.2], [lo, hi], "o", color=col, ms=6, zorder=5)
        ax.plot([-1.2, xarr], [lo, lo], color=col, lw=0.8, ls=":")
        ax.plot([1.2, xarr], [hi, hi], color=col, lw=0.8, ls=":")
        ax.annotate("", xy=(xarr, hi), xytext=(xarr, lo), arrowprops=dict(arrowstyle="<->", color=col, lw=1.6))
        ax.text(xarr + 0.08, ty, f"Δ = {hi - lo:.1f}", color=col, fontsize=9, va="center")
    ax.text(-2.9, 6.6, "two actions, one clearly\nmore creative (dotted)", fontsize=9, color="#444444", va="top")
    ax.set_xlabel("Creativity of the action")
    ax.set_ylabel("Expected rating")
    ax.set_ylim(1, 7)
    ax.set_yticks(range(1, 8))
    ax.set_xticks([])
    ax.set_xlim(-3, 3)
    ax.legend(loc="lower right", fontsize=9, frameon=False)
    strip(ax)
    save(fig, "schematic_discrimination")


def icc():
    theta = np.linspace(-4, 4, 400)
    items = [("Item A: easy (b = −1)", 1.6, -1.0, BLUE, "-"),
             ("Item B: hard (b = +1)", 1.6, 1.0, NAVY, "-"),
             ("Item C: low discrimination (a small)", 0.6, 0.0, GREY, "--")]
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for label, a, b, col, ls in items:
        ax.plot(theta, 1 / (1 + np.exp(-a * (theta - b))), color=col, lw=2.5, ls=ls, label=label)
    th = 0.0
    ax.axvline(th, color=ORANGE, lw=1.2, ls=":")
    pa = 1 / (1 + np.exp(-1.6 * (th + 1)))
    pb = 1 / (1 + np.exp(-1.6 * (th - 1)))
    ax.plot([th, th], [pa, pb], "o", color=ORANGE, ms=7, zorder=5)
    ax.text(th + 0.12, pa + 0.03, f"P(solve A) = {pa:.2f}", color=ORANGE, fontsize=9)
    ax.text(th + 0.12, pb - 0.08, f"P(solve B) = {pb:.2f}", color=ORANGE, fontsize=9)
    ax.text(th - 0.12, 0.45, "a person\nwith θ = 0", color=ORANGE, fontsize=9, ha="right", va="center")
    ax.axhline(0.5, color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("Latent trait θ (e.g. ability)")
    ax.set_ylabel("P(correct response)")
    ax.set_ylim(0, 1)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    strip(ax)
    save(fig, "irt_icc")


def main():
    plt.rcParams.update(STYLE)
    severity()
    category_use()
    discrimination()
    icc()


if __name__ == "__main__":
    main()
