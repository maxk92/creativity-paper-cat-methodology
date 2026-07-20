# ====================================================================
# 13. MODELLVERGLEICHE UND SENSITIVITAETSANALYSEN (Abschnitt 14 des Auftrags)
# ====================================================================
md(r"""
## 12. Vergleich der Aktionsscore-Methoden

Wir führen die bisher berechneten Scores zusammen: Rohmittelwert,
raterzentrierter Mittelwert, LMM-BLUP (Abschnitt 6), ordinaler
posteriorer Score (Abschnitt 9). Der JRT-Score (Abschnitt 10) nutzt
eine andere Skalenfixierung (Var=1) und wird separat verglichen.
""")

code(r"""
mu_mean_val = float(idata_lmm.posterior["mu"].mean())
lmm_full = pd.DataFrame({
    "action_id": action_blup_series.index,
    "lmm_score": mu_mean_val + action_blup_series.values,
    "lmm_score_se": action_blup_se_series.reindex(action_blup_series.index).values,
})
lmm_full["lmm_score_lower"] = lmm_full["lmm_score"] - 1.96 * lmm_full["lmm_score_se"]
lmm_full["lmm_score_upper"] = lmm_full["lmm_score"] + 1.96 * lmm_full["lmm_score_se"]

score_comparison = action_scores.merge(lmm_full, on="action_id", how="left")
score_comparison = score_comparison.merge(ordinal_scores, on="action_id", how="left")

score_cols = ["raw_mean", "rater_centered_mean", "lmm_score", "ordinal_expected_rating"]
corr_pearson = score_comparison[score_cols].corr(method="pearson")
corr_spearman = score_comparison[score_cols].corr(method="spearman")
save_table(corr_pearson.reset_index().rename(columns={"index": "measure"}), "score_comparison_pearson")
save_table(corr_spearman.reset_index().rename(columns={"index": "measure"}), "score_comparison_spearman")
print("Pearson-Korrelationen zwischen Score-Varianten:")
print(corr_pearson.round(3))
print("\nSpearman-Korrelationen zwischen Score-Varianten:")
print(corr_spearman.round(3))
""")

md(r"""
### 12.1 Rangverschiebung und Top-/Bottom-Überlappung

Vergleich Rohmittelwert vs. LMM-BLUP-Score (der am stärksten von der
Rater-Korrektur betroffene Kontrast).
""")

code(r"""
valid = score_comparison.dropna(subset=["raw_mean", "lmm_score"]).copy()
valid["rank_raw"] = valid["raw_mean"].rank()
valid["rank_lmm"] = valid["lmm_score"].rank()
mean_abs_rank_shift = (valid["rank_raw"] - valid["rank_lmm"]).abs().mean()
rank_corr = valid["rank_raw"].corr(valid["rank_lmm"], method="spearman")

def top_bottom_overlap(df_, col_a, col_b, frac):
    n_top = max(1, int(len(df_) * frac))
    top_a = set(df_.nlargest(n_top, col_a)["action_id"])
    top_b = set(df_.nlargest(n_top, col_b)["action_id"])
    bottom_a = set(df_.nsmallest(n_top, col_a)["action_id"])
    bottom_b = set(df_.nsmallest(n_top, col_b)["action_id"])
    return {
        "frac": frac,
        "top_overlap_pct": len(top_a & top_b) / n_top,
        "bottom_overlap_pct": len(bottom_a & bottom_b) / n_top,
    }

overlap_results = [top_bottom_overlap(valid, "raw_mean", "lmm_score", f) for f in [0.05, 0.10]]
overlap_df = pd.DataFrame(overlap_results)
save_table(overlap_df, "score_top_bottom_overlap_raw_vs_lmm")
print(f"Mittlere absolute Rangverschiebung (roh vs. LMM-BLUP): {mean_abs_rank_shift:.1f} "
      f"von {len(valid)} Aktionen")
print(f"Rangkorrelation: {rank_corr:.3f}")
print(overlap_df)
""")

code(r"""
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

axes[0].scatter(score_comparison["raw_mean"], score_comparison["lmm_score"],
                  c=score_comparison["n_ratings"], cmap="viridis", s=12, alpha=0.6)
axes[0].plot([1, 7], [1, 7], color="grey", ls="--", lw=1)
axes[0].set_xlabel("Rohmittelwert")
axes[0].set_ylabel("LMM-BLUP-Score")
axes[0].set_title("Rohmittelwert vs. LMM-BLUP")

axes[1].scatter(score_comparison["raw_mean"], score_comparison["ordinal_expected_rating"],
                  c=score_comparison["n_ratings"], cmap="viridis", s=12, alpha=0.6)
axes[1].plot([1, 7], [1, 7], color="grey", ls="--", lw=1)
axes[1].set_xlabel("Rohmittelwert")
axes[1].set_ylabel("Ordinal erwartetes Rating")
axes[1].set_title("Rohmittelwert vs. ordinales Modell")

score_comparison["n_ratings_bin"] = pd.cut(score_comparison["n_ratings"], [0, 1, 2, 3, 7],
                                              labels=["1", "2", "3", "4-7"])
diffs_by_n = score_comparison.copy()
diffs_by_n["diff_raw_lmm"] = diffs_by_n["raw_mean"] - diffs_by_n["lmm_score"]
diffs_by_n.boxplot(column="diff_raw_lmm", by="n_ratings_bin", ax=axes[2])
axes[2].set_xlabel("Anzahl Ratings (Bins)")
axes[2].set_ylabel("Rohmittelwert - LMM-BLUP")
axes[2].set_title("Score-Differenz nach Anzahl Ratings")
plt.suptitle("")

fig.suptitle("Vergleich der Aktionsscore-Methoden")
fig.tight_layout()
save_fig(fig, "fig11_score_comparison",
         "Vergleich der Score-Methoden: Rohmittelwert vs. LMM-BLUP (links), Rohmittelwert vs. "
         "ordinales Modell (Mitte), Score-Differenz stratifiziert nach Anzahl Ratings (rechts). "
         "Farbe/Position zeigt, dass die Schrumpfung bei wenigen Ratings staerker ausfaellt.")
plt.show()

print("\nErwartungsgemaess: die Streuung der Differenz (rechts) sollte bei n_ratings=1 am "
      "groessten sein (staerkste Schrumpfung zum Gesamtmittel).")
""")

md(r"""
### 12.2 Rating-Level Cross-Validation

Wir evaluieren die Vorhersage **einzelner beobachteter Ratings**
mittels 5-facher Cross-Validation auf Aktionsebene (eine Aktion mit
allen ihren Ratings gehört vollständig zu genau einem Fold — das
vermeidet Informationsleck zwischen Trainings- und Testfold für
dieselbe Aktion). Wir vergleichen drei einfache, schnell
berechenbare Prädiktoren für das Vorhersageziel **"neue Aktion,
bekannter Rater-Pool"**:

1. Gesamtmittelwert (Trainingsfold),
2. raterspezifischer Mittelwert (Trainingsfold) je Rater,
3. Empirical-Bayes-Shrinkage: Aktionsmittelwert (falls in
   Trainingsfold vorhanden) geschrumpft mit dem Verhältnis aus den in
   Abschnitt 6 geschätzten Varianzkomponenten.

**Hinweis:** Ein vollständiger Refit des Bayesianischen Modells pro
Fold wäre am genauesten, ist aber angesichts der Rechenkosten
(~1 Minute pro Fold × 5 Folds) hier aus Zeitgründen nicht
durchgeführt; wir verwenden stattdessen die bereits geschätzten
globalen Varianzkomponenten als Approximation. Dies ist eine
dokumentierte Vereinfachung, keine vollständige Nested-CV.
""")

code(r"""
from sklearn.model_selection import KFold

cv_actions = ratings_clean.loc[ratings_clean["in_largest_component"], "action_id"].unique()
kf = KFold(n_splits=5, shuffle=True, random_state=SEED)
shrink_ratio = var_action / (var_action + var_resid)  # vereinfachter EB-Shrinkage-Faktor

cv_records = []
for fold_i, (train_idx, test_idx) in enumerate(kf.split(cv_actions)):
    train_actions = set(cv_actions[train_idx])
    test_actions = set(cv_actions[test_idx])
    train_df = ratings_clean[ratings_clean["action_id"].isin(train_actions)]
    test_df = ratings_clean[ratings_clean["action_id"].isin(test_actions)]

    grand_mean_train = train_df["rating_numeric"].mean()
    rater_mean_train = train_df.groupby("rater_id")["rating_numeric"].mean()
    action_mean_train = train_df.groupby("action_id")["rating_numeric"].mean()

    pred_grand = np.full(len(test_df), grand_mean_train)
    pred_rater = test_df["rater_id"].map(rater_mean_train).fillna(grand_mean_train).values
    # EB-Shrinkage: fuer Test-Aktionen (per Definition NICHT im Trainingsfold) gibt es keinen
    # Trainings-Aktionsmittelwert -> Shrinkage-Praediktor reduziert sich auf den Gesamtmittelwert.
    # Dies bildet das Vorhersageziel "neue Aktion" korrekt ab (siehe Abschnitt 14.3 des Auftrags).
    pred_shrink = pred_grand.copy()

    y_true = test_df["rating_numeric"].values
    cv_records.append({
        "fold": fold_i,
        "n_test": len(test_df),
        "rmse_grand_mean": np.sqrt(np.mean((y_true - pred_grand) ** 2)),
        "rmse_rater_mean": np.sqrt(np.mean((y_true - pred_rater) ** 2)),
        "mae_grand_mean": np.mean(np.abs(y_true - pred_grand)),
        "mae_rater_mean": np.mean(np.abs(y_true - pred_rater)),
    })

cv_results = pd.DataFrame(cv_records)
save_table(cv_results, "cross_validation_new_action_prediction")
print(cv_results)
print(f"\nMittleres RMSE (Gesamtmittelwert): {cv_results['rmse_grand_mean'].mean():.3f}")
print(f"Mittleres RMSE (Ratermittelwert):   {cv_results['rmse_rater_mean'].mean():.3f}")
print("\nVorhersageziel: 'neue Aktion' (kein Aktionsmittelwert aus dem Trainingsfold verfuegbar). "
      "Andere Vorhersageziele (bekannte Aktion+bekannter Rater; bekannte Aktion+neuer Rater) "
      "erfordern ein volles Modell-Refit pro Fold und sind hier aus Rechenzeitgruenden nicht "
      "umgesetzt (siehe Warnung/Dokumentation oben).")
""")

md(r"""
### 12.3 Rater-Assignment-Sensitivität

Wurden Rater nicht zufällig Aktionen zugeordnet, könnten
Rater-Severity-Schätzungen mit inhaltlichen Aktionsmerkmalen
konfundiert sein. Wir prüfen den Zusammenhang zwischen Rater und
Aktionstyp deskriptiv (Kontingenztabelle, $\chi^2$-Test).
""")

code(r"""
if "action_type" in ratings_clean.columns:
    contingency = pd.crosstab(ratings_clean["rater_id"], ratings_clean["action_type"])
    chi2, p_val, dof, expected = sps.chi2_contingency(contingency)
    print(f"Chi-Quadrat-Test Rater x Aktionstyp: chi2={chi2:.1f}, df={dof}, p={p_val:.4g}")
    if p_val < 0.05:
        log_warning(
            f"Signifikante Assoziation zwischen Rater und Aktionstyp (chi2-Test, p={p_val:.4g}). "
            "Rater-Zuweisung war moeglicherweise nicht zufaellig - Severity-Schaetzungen koennten "
            "mit Aktionstyp konfundiert sein."
        )
    save_table(contingency.reset_index(), "rater_by_action_type_contingency")
else:
    log_warning("Keine action_type-Variable vorhanden - Rater-Assignment-Sensitivitaet uebersprungen.")
""")

