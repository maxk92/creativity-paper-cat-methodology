# ====================================================================
# 16. EXPORT DER ERGEBNISDATEIEN (Abschnitt 17 des Auftrags)
# ====================================================================
md(r"""
## 15. Finale Ergebnisdateien: `action_scores.csv` und `rater_diagnostics.csv`

Wir führen alle bisher berechneten Score- und Diagnostikkomponenten in
den beiden zentralen Ergebnisdateien zusammen. **Nicht verfügbare
Modellwerte werden als fehlend (`NaN`), nicht als Null gespeichert**
(z. B. für Aktionen außerhalb der größten Komponente, für die keine
LMM-/Ordinal-Scores vorliegen).
""")

code(r"""
final_action_scores = action_scores.merge(lmm_full, on="action_id", how="left")
final_action_scores = final_action_scores.merge(ordinal_scores, on="action_id", how="left")

if "theta_jrt" not in dir():
    theta_jrt_mean = idata_jrt.posterior["theta"].mean(dim=("chain", "draw")).values
    theta_jrt_sd = idata_jrt.posterior["theta"].std(dim=("chain", "draw")).values
    jrt_action_scores = pd.DataFrame({
        "action_id": action_levels_o, "jrt_score": theta_jrt_mean, "jrt_score_se": theta_jrt_sd,
    })
final_action_scores = final_action_scores.merge(jrt_action_scores, on="action_id", how="left")

def score_flag(row):
    flags = []
    if row["n_ratings"] == 1:
        flags.append("einzelrating")
    if row.get("connected_component", 0) != 0:
        flags.append("kleine_komponente")
    return ";".join(flags) if flags else "ok"

final_action_scores["score_flag"] = final_action_scores.apply(score_flag, axis=1)

action_scores_out_cols = [
    "action_id", "n_ratings", "connected_component", "raw_mean", "raw_median",
    "rater_centered_mean", "lmm_score", "lmm_score_se", "lmm_score_lower", "lmm_score_upper",
    "ordinal_latent_score", "ordinal_latent_lower", "ordinal_latent_upper", "ordinal_expected_rating",
    "jrt_score", "jrt_score_se", "score_flag",
]
final_action_scores_out = final_action_scores[action_scores_out_cols].copy()
final_action_scores_out.to_csv(DATA_PROCESSED / "action_scores.csv", index=False)
print(f"action_scores.csv gespeichert: {len(final_action_scores_out)} Aktionen, "
      f"{final_action_scores_out.shape[1]} Spalten.")
final_action_scores_out.head()
""")

code(r"""
rater_diagnostics_out_cols = [
    "rater_id", "n_ratings", "n_actions", "n_categories_used", "raw_mean", "sd",
    "extreme_category_rate", "central_category_rate", "network_component", "network_degree",
    "mean_pair_overlap", "lmm_severity", "lmm_severity_se", "ordinal_severity",
    "ordinal_severity_lower", "ordinal_severity_upper", "jrt_discrimination", "jrt_severity",
    "leave_one_out_spearman", "leave_one_out_mae", "drift_estimate", "diagnostic_flag",
]
rater_diagnostics_out_cols = [c for c in rater_diagnostics_out_cols if c in rater_diagnostics.columns]
rater_diagnostics_out = rater_diagnostics[rater_diagnostics_out_cols].copy()
rater_diagnostics_out = rater_diagnostics_out.rename(columns={"sd": "raw_sd"})
rater_diagnostics_out.to_csv(DATA_PROCESSED / "rater_diagnostics.csv", index=False)
print(f"rater_diagnostics.csv gespeichert: {len(rater_diagnostics_out)} Rater, "
      f"{rater_diagnostics_out.shape[1]} Spalten.")
rater_diagnostics_out.head()
""")

md(r"""
### 15.1 Publication-Ready Tabellen
""")

code(r"""
sample_description = pd.DataFrame([
    {"quantity": "Anzahl Ratings gesamt", "value": len(ratings_clean)},
    {"quantity": "Anzahl Aktionen", "value": ratings_clean["action_id"].nunique()},
    {"quantity": "Anzahl Rater", "value": ratings_clean["rater_id"].nunique()},
    {"quantity": "Aktionen mit 1 Rating", "value": int((ratings_per_action == 1).sum())},
    {"quantity": "Aktionen mit 2 Ratings", "value": int((ratings_per_action == 2).sum())},
    {"quantity": "Aktionen mit >=3 Ratings", "value": int((ratings_per_action >= 3).sum())},
    {"quantity": "Anzahl Zusammenhangskomponenten", "value": n_components},
    {"quantity": "Aktionen in groesster Komponente", "value": len(largest_component_actions)},
    {"quantity": "Krippendorffs Alpha (ordinal)", "value": round(alpha_ordinal, 3)},
    {"quantity": "sigma^2_action (linear)", "value": round(var_action, 3)},
    {"quantity": "sigma^2_rater (linear)", "value": round(var_rater, 3)},
    {"quantity": "sigma^2_residual (linear)", "value": round(var_resid, 3)},
    {"quantity": "Absolute Reliabilitaet (k=1)", "value": round(float(d_study.loc[0, "rho_abs"]), 3)},
    {"quantity": "Relative Reliabilitaet (k=1)", "value": round(float(d_study.loc[0, "rho_rel"]), 3)},
    {"quantity": "Absolute Reliabilitaet (k=2)", "value": round(float(d_study.loc[1, "rho_abs"]), 3)},
    {"quantity": "Relative Reliabilitaet (k=2)", "value": round(float(d_study.loc[1, "rho_rel"]), 3)},
])
save_table(sample_description, "sample_description_summary")
sample_description
""")

