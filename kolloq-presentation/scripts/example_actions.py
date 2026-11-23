"""Example actions for the colloquium slides.

Verifies the two example actions (ratings, raw mean, GRM score) against the
pipeline outputs, computes for each action the rating every rater of the panel
would be expected to give at the action's GRM score (the "panel-expected
rating"), and tabulates the mean GRM score of single-rated actions by rater and
rating value.

Writes:
  scripts/example_actions.csv            one row per example action
  scripts/example_actions_by_rater.csv   expected rating per rater and action
  scripts/single_rating_theta.csv        mean theta of single-rated actions by rater x rating
  img/example_actions_expected.svg       dot plot of the expected ratings

Run from kolloq-presentation/:
  ../.venv/bin/python -I scripts/example_actions.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RES = ROOT / "data-analysis" / "creativity-ratings-psychometrics" / "results"
RAW = ROOT / "data-analysis" / "creativity-ratings-psychometrics" / "data" / "raw"

NAVY = "#002855"
BLUE = "#619CFF"
GREY = "#9aa3ad"

EXAMPLES = {
    "130df886-9dd1-454f-935a-f593d9726789": "Dribble A (Bale, Wales–Denmark)",
    "085bd6cb-2573-46a6-b145-65f870ce7e9f": "Dribble B (Danilo, Brazil–Serbia)",
}
# colours per example: (expected-rating markers, actually given rating)
COLOURS = {
    "130df886-9dd1-454f-935a-f593d9726789": ("#9cc3ff", "#002855"),
    "085bd6cb-2573-46a6-b145-65f870ce7e9f": ("#f5c777", "#d62728"),
}
FALLBACK = {
    "13ebfc18-fc9d-4e92-adb7-d0a2b11dd9b5": "Shot (Giroud, France–Australia)",
    "a70f0ed1-5a67-4f20-a630-da52aaba889f": "Pass (Huth, Germany W–Colombia W)",
}
FOCUS_RATERS = ["R19", "R02", "R01", "R06"]


def load():
    scores = pd.read_csv(RES / "supplement" / "product_scores.csv").set_index("product_id")
    wide = pd.read_csv(RES / "data" / "ratings_wide.csv").set_index("product_id")
    params = pd.read_csv(RES / "main" / "rater_parameters.csv").set_index("rater_id")
    sev = pd.read_csv(RES / "supplement" / "rater_parameters_by_model.csv")
    sev = sev[(sev.model == "M1_RSM") & (sev.parameter == "b_rater")].set_index("rater_id")["estimate"]
    events = pd.read_csv(RAW / "action_events_raw.csv").set_index("id")
    return scores, wide, params, sev, events


def expected_rating(theta, a, b):
    """GRM expected rating on the 1-7 scale: 1 + sum_k P(X >= k+1)."""
    b = np.asarray([x for x in b if pd.notna(x)], dtype=float)
    p_ge = 1.0 / (1.0 + np.exp(-a * (theta - b)))
    return 1.0 + p_ge.sum()


def main():
    scores, wide, params, sev, events = load()
    bcols = [f"b{k}" for k in range(1, 7)]

    rows, by_rater = [], []
    for pid, label in {**EXAMPLES, **FALLBACK}.items():
        s = scores.loc[pid]
        given = wide.loc[pid].dropna()
        given = {r: int(v) + 1 for r, v in given.items()}  # internal 0-6 -> 1-7
        theta = float(s.theta_eap)
        exp_all = {
            r: expected_rating(theta, params.loc[r, "a"], params.loc[r, bcols].values)
            for r in params.index
        }
        ev = events.loc[pid]
        rows.append(
            dict(
                product_id=pid,
                label=label,
                is_main=pid in EXAMPLES,
                player=ev.player,
                team=ev.team,
                match=f"{ev.home_team} – {ev.away_team}",
                minute=int(ev.minute),
                type=ev.type,
                raters=";".join(given),
                ratings=";".join(str(v) for v in given.values()),
                rater_severity_m1=";".join(f"{sev[r]:.2f}" for r in given),
                raw_mean=np.mean(list(given.values())),
                theta_eap=theta,
                psd=float(s.psd),
                rel_post=float(s.rel_post),
                panel_expected_rating=np.mean(list(exp_all.values())),
                expected_rating_own_raters=np.mean([exp_all[r] for r in given]),
            )
        )
        for r, e in exp_all.items():
            by_rater.append(
                dict(product_id=pid, label=label, rater_id=r, severity_m1=sev[r],
                     expected_rating=e, given=given.get(r, np.nan))
            )

    df = pd.DataFrame(rows)
    df.to_csv(HERE / "example_actions.csv", index=False)
    dfr = pd.DataFrame(by_rater)
    dfr.to_csv(HERE / "example_actions_by_rater.csv", index=False)

    # mean theta of single-rated actions by rater and rating value
    single = scores[scores.n_ratings == 1]
    w1 = wide.loc[single.index]
    recs = []
    for r in params.index:
        col = w1[r].dropna()
        for val, grp in col.groupby(col):
            recs.append(dict(rater_id=r, rating=int(val) + 1, n=len(grp),
                             mean_theta=single.loc[grp.index, "theta_eap"].mean()))
    st = pd.DataFrame(recs)
    st.to_csv(HERE / "single_rating_theta.csv", index=False)

    # ---- console report -------------------------------------------------
    pd.set_option("display.width", 200)
    print(df[["label", "raters", "ratings", "rater_severity_m1", "raw_mean", "theta_eap", "psd",
              "panel_expected_rating"]].to_string(index=False))
    print("\nMean theta of single-rated actions (focus raters):")
    print(st[st.rater_id.isin(FOCUS_RATERS)].pivot(index="rating", columns="rater_id",
                                                     values="mean_theta").round(2).to_string())
    print(st[st.rater_id.isin(FOCUS_RATERS)].pivot(index="rating", columns="rater_id",
                                                     values="n").to_string())

    # ---- figure: expected rating per rater for the two main actions -----
    main = dfr[dfr.product_id.isin(EXAMPLES)].copy()
    order = sev.sort_values().index.tolist()  # lenient -> strict
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 5.2))
    offsets = {pid: off for pid, off in zip(EXAMPLES, (-0.18, 0.18))}
    markers = {pid: m for pid, m in zip(EXAMPLES, ("o", "s"))}
    for pid, label in EXAMPLES.items():
        sub = main[main.product_id == pid].set_index("rater_id").loc[order]
        x = np.arange(len(order)) + offsets[pid]
        short = label.split(" (")[0]
        c_exp, c_given = COLOURS[pid]
        ax.scatter(x, sub.expected_rating, s=44, marker=markers[pid], facecolor=c_exp, edgecolor=c_exp,
                   linewidth=1.0, label=f"{short}: expected rating of each rater (model)")
        g = sub[sub.given.notna()]
        xg = np.array([order.index(r) for r in g.index]) + offsets[pid]
        ax.scatter(xg, g.given, s=170, marker=markers[pid], facecolor=c_given, edgecolor=c_given,
                   linewidth=1.5, zorder=5, label=f"{short}: rating actually given")
        pm = df.loc[df.product_id == pid, "panel_expected_rating"].item()
        ax.axhline(pm, color=c_given, linestyle="--" if markers[pid] == "o" else ":", linewidth=1.2,
                   label=f"{short}: rating the full panel would give on average ({pm:.2f})")
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(order, rotation=90, fontsize=10)
    ax.set_xlabel("Rater, sorted from most lenient to most strict (M1 severity)")
    ax.set_ylabel("Rating on the 1–7 scale")
    ax.set_ylim(0.8, 7.2)
    ax.set_yticks(range(1, 8))
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="y", color="#e6ecfa")
    ax.legend(fontsize=9.5, loc="upper center", bbox_to_anchor=(0.5, -0.26), frameon=False, ncol=2)
    fig.tight_layout()
    fig.savefig(HERE.parent / "img" / "example_actions_expected.svg")
    fig.savefig(HERE.parent / "img" / "example_actions_expected.png", dpi=200)
    print("\nwrote figure and CSVs")


if __name__ == "__main__":
    main()
