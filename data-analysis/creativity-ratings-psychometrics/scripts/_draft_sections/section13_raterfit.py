# ====================================================================
# 12. RATER-FIT UND RATER-EFFEKT-DIAGNOSTIK (Abschnitt 13 des Auftrags)
# ====================================================================
md(r"""
## 11. Rater-Fit-Diagnostik

### 11.1 Leave-one-rater-out-Konsistenz

Für jede Aktion mit $n_i \ge 2$ Ratings berechnen wir den
**Konsensus ohne Rater $j$** (Mittelwert der übrigen Ratings) und
vergleichen Rater $j$s eigenes Rating damit. Das vermeidet die
Zirkularität, einen Rater mit einem Konsens zu vergleichen, der sein
eigenes Rating bereits enthält.
""")

code(r"""
ratings_indexed = ratings_clean.set_index(["action_id", "rater_id"])["rating_numeric"]
action_sum = ratings_clean.groupby("action_id")["rating_numeric"].sum()
action_n = ratings_clean.groupby("action_id")["rating_numeric"].size()

tmp = ratings_clean.copy()
tmp["_action_sum"] = tmp["action_id"].map(action_sum)
tmp["_action_n"] = tmp["action_id"].map(action_n)
tmp["loo_consensus"] = np.where(
    tmp["_action_n"] >= 2,
    (tmp["_action_sum"] - tmp["rating_numeric"]) / (tmp["_action_n"] - 1),
    np.nan,
)

def loo_stats(g):
    valid = g.dropna(subset=["loo_consensus"])
    if len(valid) < 5:
        return pd.Series({"leave_one_out_spearman": np.nan, "leave_one_out_mae": np.nan,
                            "leave_one_out_mean_diff": np.nan, "leave_one_out_weighted_kappa": np.nan,
                            "n_loo": len(valid)})
    spearman_r = sps.spearmanr(valid["rating_numeric"], valid["loo_consensus"]).correlation
    mae = np.abs(valid["rating_numeric"] - valid["loo_consensus"]).mean()
    mean_diff = (valid["rating_numeric"] - valid["loo_consensus"]).mean()
    loo_rounded = valid["loo_consensus"].round().clip(1, 7).astype(int)
    w_kappa = cohen_kappa_score(valid["rating_numeric"], loo_rounded, weights="quadratic")
    return pd.Series({"leave_one_out_spearman": spearman_r, "leave_one_out_mae": mae,
                        "leave_one_out_mean_diff": mean_diff,
                        "leave_one_out_weighted_kappa": w_kappa, "n_loo": len(valid)})

loo_df = tmp.groupby("rater_id").apply(loo_stats, include_groups=False).reset_index()
save_table(loo_df, "leave_one_out_consistency")
print(f"Leave-one-out-Konsistenz berechnet fuer {loo_df['leave_one_out_spearman'].notna().sum()} "
      f"von {len(loo_df)} Ratern (Rest: zu wenige Aktionen mit >=2 Ratings).")
loo_df.sort_values("leave_one_out_spearman").head(10)
""")

md(r"""
### 11.2 Zusammenfassende Rater-Diagnostiktabelle und explorative Flags

**Wichtig:** Flags markieren Rater nur explorativ, **nicht** als
"schlecht". Kriterien (jedes für sich schwach, gemeinsam zu
interpretieren): sehr geringe Kategorienvariation ($\le 2$ genutzte
Kategorien), extrem geringe Konnektivität (mittlere Paarüberlappung
$<5$), auffällig niedrige JRT-Diskrimination ($<0.4$), starke Drift
($|\text{Slope}| > 2\cdot SE$), negative oder sehr geringe
Leave-one-out-Konsistenz (Spearman $<0.1$).
""")

code(r"""
rater_diagnostics = rater_desc.merge(severity_df.drop(columns=["n_ratings", "raw_mean"], errors="ignore"),
                                        on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(
    ordinal_severity if "ordinal_severity" in dir() else pd.DataFrame({"rater_id": []}),
    on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(
    jrt_rater_table if "jrt_rater_table" in dir() else pd.DataFrame({"rater_id": []}),
    on="rater_id", how="left")
rater_diagnostics = rater_diagnostics.merge(loo_df, on="rater_id", how="left")

rater_diagnostics["network_component"] = rater_diagnostics["rater_id"].apply(
    lambda r: 0 if r in largest_component_raters else -1)
rater_diagnostics["network_degree"] = rater_diagnostics["rater_id"].map(rater_degree)
rater_diagnostics["mean_pair_overlap"] = rater_diagnostics["rater_id"].map(mean_pair_overlap)

def build_flags(row):
    flags = []
    if row.get("n_categories_used", 7) <= 2:
        flags.append("geringe_kategorienvariation")
    if pd.notna(row.get("mean_pair_overlap")) and row["mean_pair_overlap"] < 5:
        flags.append("geringe_konnektivitaet")
    if pd.notna(row.get("jrt_discrimination")) and row["jrt_discrimination"] < 0.4:
        flags.append("niedrige_diskrimination")
    if pd.notna(row.get("drift_estimate")) and pd.notna(row.get("drift_se")) and row["drift_se"] > 0:
        if abs(row["drift_estimate"]) > 2 * row["drift_se"]:
            flags.append("moegliche_drift")
    if pd.notna(row.get("leave_one_out_spearman")) and row["leave_one_out_spearman"] < 0.1:
        flags.append("geringe_loo_konsistenz")
    if row.get("network_component", 0) != 0:
        flags.append("ausserhalb_groesster_komponente")
    return ";".join(flags) if flags else "keine_auffaelligkeit"

rater_diagnostics["diagnostic_flag"] = rater_diagnostics.apply(build_flags, axis=1)
n_flagged = (rater_diagnostics["diagnostic_flag"] != "keine_auffaelligkeit").sum()
print(f"Rater mit mindestens einer explorativen Auffaelligkeit: {n_flagged} von {len(rater_diagnostics)}")
print(rater_diagnostics["diagnostic_flag"].value_counts())
""")

