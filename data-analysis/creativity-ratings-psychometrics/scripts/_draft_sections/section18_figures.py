# ====================================================================
# 17. VERBLEIBENDE KERNABBILDUNGEN (Abschnitt 18 des Auftrags)
# ====================================================================
md(r"""
## 16. Judge Category Curves, Informationsfunktionen, Score-Unsicherheit

### 16.1 Judge Category Curves und Informationsfunktion (aus dem JRT-Modell)

Für eine Auswahl von Ratern mit niedriger, mittlerer und hoher
geschätzter Diskrimination zeigen wir die modellimplizierten
Kategorienwahrscheinlichkeiten $P(Y=k\mid\theta)$ über das latente
Kreativitätskontinuum sowie die zugehörige Fisher-Informationsfunktion
$I_j(\theta) = a_j^2 \sum_k P_{jk}(\theta)\,[1-P_{jk}(\theta)]$
(Näherung über die kumulativen Wahrscheinlichkeiten).
""")

code(r"""
def category_probs(theta_grid, a, lam, cuts):
    eta = a * theta_grid + lam
    cum = 1 / (1 + np.exp(-(cuts[None, :] - eta[:, None])))
    cum = np.concatenate([np.zeros((len(theta_grid), 1)), cum, np.ones((len(theta_grid), 1))], axis=1)
    return np.diff(cum, axis=1)  # (n_theta, 7)

theta_grid = np.linspace(-3, 3, 200)
cut_mean_jrt = idata_jrt.posterior["cutpoints"].mean(dim=("chain", "draw")).values

example_raters_idx = [int(np.argmin(disc)), int(np.argsort(disc)[len(disc) // 2]), int(np.argmax(disc))]
example_labels = ["niedrigste Diskrimination", "mediane Diskrimination", "hoechste Diskrimination"]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for col, (ridx, label) in enumerate(zip(example_raters_idx, example_labels)):
    a_r = disc[ridx]
    lam_r = jrt_rater_table.loc[ridx, "jrt_severity"]
    probs = category_probs(theta_grid, a_r, lam_r, cut_mean_jrt)
    for k in range(7):
        axes[0, col].plot(theta_grid, probs[:, k], label=f"Y={k+1}")
    axes[0, col].set_title(f"{rater_levels_o[ridx]}: {label}\n(a={a_r:.2f})")
    axes[0, col].set_xlabel(r"$\theta$ (latente Aktionskreativitaet)")
    if col == 0:
        axes[0, col].set_ylabel("P(Y=k)")
        axes[0, col].legend(fontsize=7, ncol=2)

    info = (a_r ** 2) * np.sum(probs * (1 - probs), axis=1)
    axes[1, col].plot(theta_grid, info, color="#C44E52")
    axes[1, col].set_xlabel(r"$\theta$")
    if col == 0:
        axes[1, col].set_ylabel("Informationsfunktion (Naeherung)")

fig.suptitle("Judge Category Curves (oben) und Informationsfunktionen (unten) "
              "fuer Rater mit niedriger/medianer/hoher Diskrimination")
fig.tight_layout()
save_fig(fig, "fig14_judge_category_curves_information",
         "Kategorienwahrscheinlichkeiten (oben) und Fisher-Informationsnaeherung (unten) fuer "
         "drei exemplarische Rater mit niedriger, medianer und hoher JRT-Diskrimination.")
plt.show()
""")

md(r"""
### 16.2 Unsicherheitsintervalle ausgewählter Aktionsscores

Wir zeigen für eine Zufallsstichprobe von 40 Aktionen (stratifiziert
über die Anzahl Ratings) die 95%-Unsicherheitsintervalle des
LMM-BLUP- und des ordinalen Scores nebeneinander.
""")

code(r"""
sample_for_plot = (
    final_action_scores.dropna(subset=["lmm_score", "ordinal_latent_score"])
    .groupby(final_action_scores["n_ratings"].clip(upper=4))
    .apply(lambda g: g.sample(min(10, len(g)), random_state=SEED), include_groups=False)
    .reset_index(drop=True)
    .sort_values("lmm_score")
)

fig, ax = plt.subplots(figsize=(8, 10))
y_pos = np.arange(len(sample_for_plot))
ax.errorbar(sample_for_plot["lmm_score"], y_pos - 0.15,
             xerr=[sample_for_plot["lmm_score"] - sample_for_plot["lmm_score_lower"],
                   sample_for_plot["lmm_score_upper"] - sample_for_plot["lmm_score"]],
             fmt="o", ms=4, color="#4C72B0", label="LMM-BLUP", capsize=2)
ax_ord = ax.twiny()
ax_ord.errorbar(sample_for_plot["ordinal_latent_score"], y_pos + 0.15,
                  xerr=[sample_for_plot["ordinal_latent_score"] - sample_for_plot["ordinal_latent_lower"],
                        sample_for_plot["ordinal_latent_upper"] - sample_for_plot["ordinal_latent_score"]],
                  fmt="s", ms=4, color="#DD8452", label="ordinal", capsize=2)
ax.set_yticks(y_pos)
ax.set_yticklabels(sample_for_plot["action_id"] + " (n=" + sample_for_plot["n_ratings"].astype(str) + ")",
                     fontsize=7)
ax.set_xlabel("LMM-BLUP-Score", color="#4C72B0")
ax_ord.set_xlabel("Ordinaler latenter Score", color="#DD8452")
ax.set_title("95%-Unsicherheitsintervalle: Stichprobe von Aktionsscores\n"
              "(stratifiziert nach Anzahl Ratings)")
fig.tight_layout()
save_fig(fig, "fig15_score_uncertainty_sample",
         "95%-Unsicherheitsintervalle fuer eine nach Anzahl Ratings stratifizierte Stichprobe "
         "von Aktionen: LMM-BLUP-Score (blau, unten) vs. ordinaler latenter Score (orange, oben).")
plt.show()
""")

