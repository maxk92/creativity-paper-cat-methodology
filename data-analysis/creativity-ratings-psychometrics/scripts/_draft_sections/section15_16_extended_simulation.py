# ====================================================================
# 14. ERWEITERTE ABHAENGIGKEITEN (Abschnitt 15 des Auftrags)
# ====================================================================
md(r"""
## 13. Erweiterte Abhängigkeiten: Match als zusätzliche Facette

Aktionen sind genau einem Match zugeordnet; ein Match enthält mehrere
Aktionen. Wir erweitern das lineare gekreuzte Modell aus Abschnitt 6
um einen zusätzlichen Random Intercept für `match_id`:

$$
y_{ijm} = \mu + u_i^{(\text{action})} + v_j^{(\text{rater})}
+ w_m^{(\text{match})} + \varepsilon_{ijm}
$$

**Wichtig:** Die Aktion ist nested innerhalb des Matches (jede Aktion
gehört zu genau einem Match), während Rater weiterhin gekreuzt mit
beiden bleiben. Wir vergleichen die Varianzzerlegung und prüfen, ob
sich Aktionsränge wesentlich ändern.
""")

code(r"""
if "match_id" in ratings_clean.columns:
    match_idx, match_levels = pd.factorize(df_lmm["match_id"])
    n_match = len(match_levels)
    print(f"Erweitertes Modell: {n_match} Matches.")

    with pm.Model(coords={"action": action_levels, "rater": rater_levels, "match": match_levels}) as extended_model:
        mu_ext = pm.Normal("mu", 4.0, 2.0)
        sigma_action_ext = pm.Exponential("sigma_action", 1.0)
        sigma_rater_ext = pm.Exponential("sigma_rater", 1.0)
        sigma_match = pm.Exponential("sigma_match", 1.0)
        sigma_resid_ext = pm.Exponential("sigma_resid", 1.0)

        u_ext = pm.Normal("u_raw", 0, 1, dims="action") * sigma_action_ext
        v_ext = pm.Normal("v_raw", 0, 1, dims="rater") * sigma_rater_ext
        w_ext = pm.Normal("w_raw", 0, 1, dims="match") * sigma_match

        eta_ext = mu_ext + u_ext[action_idx] + v_ext[rater_idx] + w_ext[match_idx]
        pm.Normal("y_obs", mu=eta_ext, sigma=sigma_resid_ext, observed=y_lmm)

        idata_ext = pm.sample(draws=800, tune=800, chains=4, cores=4, target_accept=0.9,
                                random_seed=SEED, progressbar=False)

    idata_ext.to_netcdf(str(RESULTS_MODELS / "extended_match_model.nc"))

    va_ext = float((idata_ext.posterior["sigma_action"] ** 2).mean())
    vr_ext = float((idata_ext.posterior["sigma_rater"] ** 2).mean())
    vm_ext = float((idata_ext.posterior["sigma_match"] ** 2).mean())
    ve_ext = float((idata_ext.posterior["sigma_resid"] ** 2).mean())
    total_ext = va_ext + vr_ext + vm_ext + ve_ext

    extended_vc = pd.DataFrame([
        {"component": "action", "variance": va_ext, "pct": va_ext / total_ext},
        {"component": "rater", "variance": vr_ext, "pct": vr_ext / total_ext},
        {"component": "match", "variance": vm_ext, "pct": vm_ext / total_ext},
        {"component": "residual", "variance": ve_ext, "pct": ve_ext / total_ext},
    ])
    save_table(extended_vc, "extended_model_variance_components")
    print(extended_vc)

    u_ext_mean = idata_ext.posterior["u_raw"].mean(dim=("chain", "draw")).values * \
                  float(idata_ext.posterior["sigma_action"].mean())
    ext_action_scores = pd.Series(u_ext_mean, index=action_levels, name="action_score_extended")
    base_action_scores = action_blup_series.reindex(action_levels)
    rank_corr_ext = pd.Series(base_action_scores.values).corr(
        pd.Series(ext_action_scores.values), method="spearman")
    print(f"\nRangkorrelation Aktionsscore (Basis-Modell vs. Match-erweitertes Modell): "
          f"{rank_corr_ext:.3f}")
    if rank_corr_ext < 0.9:
        log_warning(
            f"Rangkorrelation zwischen Basis- und Match-erweitertem Modell nur {rank_corr_ext:.3f} "
            "- Match-Zugehoerigkeit veraendert die Aktionsrangfolge nicht-trivial."
        )
else:
    log_warning("Keine match_id-Variable vorhanden - erweitertes Modell uebersprungen.")
    extended_vc = pd.DataFrame()
""")

# ====================================================================
# 15. SIMULATIONS-/RECOVERY-CHECK (Abschnitt 16 des Auftrags)
# ====================================================================
md(r"""
## 14. Simulations- und Recovery-Check

**Dieser Abschnitt ist nur aussagekräftig, weil dieser Lauf mit
SIMULIERTEN Daten arbeitet** (`DEV_MODE=True`), für die die wahren
Aktions-/Rater-Parameter bekannt sind (siehe
`scripts/simulate_ratings.py` und `data/simulation/`). **Bei echten
Ratings entfällt dieser Vergleich**, da keine wahren Werte existieren
— die hier demonstrierte Infrastruktur ist dann für eine
design-basierte Simulation (identische Rater-Aktions-Inzidenzmatrix,
künstliche bekannte Parameter, siehe Abschnitt 16 des Analyseauftrags)
weiter nutzbar, um zu prüfen, welche Parameter mit dem konkreten
unbalancierten Design überhaupt identifizierbar sind.
""")

code(r"""
gt_action = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_action_params.csv")
gt_rater = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_rater_params.csv")
gt_thresh = pd.read_csv(PROJECT_ROOT / "data" / "simulation" / "ground_truth_thresholds.csv")

recovery_action = ordinal_scores.merge(gt_action, on="action_id", how="inner")
bias_theta = (recovery_action["ordinal_latent_score"] - recovery_action["theta_true"]).mean()
rmse_theta = np.sqrt(((recovery_action["ordinal_latent_score"] - recovery_action["theta_true"]) ** 2).mean())
rank_corr_theta = recovery_action["ordinal_latent_score"].corr(recovery_action["theta_true"], method="spearman")
coverage_theta = ((recovery_action["theta_true"] >= recovery_action["ordinal_latent_lower"]) &
                    (recovery_action["theta_true"] <= recovery_action["ordinal_latent_upper"])).mean()

print("=== Recovery: Aktions-Theta (ordinales Modell) ===")
print(f"Bias:  {bias_theta:+.3f}")
print(f"RMSE:  {rmse_theta:.3f}")
print(f"Rangkorrelation (geschaetzt vs. wahr): {rank_corr_theta:.3f}")
print(f"95%-CI-Coverage: {coverage_theta:.1%} (Sollwert ~95%)")

recovery_rater = severity_df.merge(gt_rater, on="rater_id", how="inner")
# Vorzeichen/Skalenpruefung: lmm_severity und severity_true sollten hoch korrelieren
sev_corr = recovery_rater["lmm_severity"].corr(recovery_rater["severity_true"])
print(f"\n=== Recovery: Rater-Severity (lineares Modell) ===")
print(f"Korrelation geschaetzt vs. wahr: {sev_corr:.3f}")

recovery_summary = pd.DataFrame([
    {"quantity": "action_theta_bias", "value": bias_theta},
    {"quantity": "action_theta_rmse", "value": rmse_theta},
    {"quantity": "action_theta_rank_corr", "value": rank_corr_theta},
    {"quantity": "action_theta_ci_coverage", "value": coverage_theta},
    {"quantity": "rater_severity_recovery_corr", "value": sev_corr},
])
save_table(recovery_summary, "simulation_recovery_summary")

if rank_corr_theta < 0.7:
    log_warning(f"Recovery-Rangkorrelation der Aktions-Theta nur {rank_corr_theta:.3f} - "
                 "schwache Parameter-Identifizierbarkeit im vorliegenden Design moeglich.")
""")

code(r"""
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].scatter(recovery_action["theta_true"], recovery_action["ordinal_latent_score"],
                  s=10, alpha=0.4, c=recovery_action["n_ratings"], cmap="viridis")
lims = [recovery_action["theta_true"].min(), recovery_action["theta_true"].max()]
axes[0].plot(lims, lims, color="grey", ls="--", lw=1)
axes[0].set_xlabel(r"Wahres $\theta_i$ (Simulation)")
axes[0].set_ylabel(r"Geschaetztes $\theta_i$ (ordinales Modell)")
axes[0].set_title(f"Aktions-Recovery (r_rank={rank_corr_theta:.2f})")

axes[1].scatter(recovery_rater["severity_true"], recovery_rater["lmm_severity"], s=25, alpha=0.7,
                  color="#DD8452")
lims2 = [recovery_rater["severity_true"].min(), recovery_rater["severity_true"].max()]
axes[1].plot(lims2, lims2, color="grey", ls="--", lw=1)
axes[1].set_xlabel("Wahre Rater-Severity (Simulation)")
axes[1].set_ylabel("Geschaetzte Rater-Severity (lineares Modell)")
axes[1].set_title(f"Rater-Recovery (r={sev_corr:.2f})")

fig.suptitle("Parameter-Recovery: nur gueltig fuer simulierte Entwicklungsdaten")
fig.tight_layout()
save_fig(fig, "fig13_simulation_recovery",
         "Vergleich geschaetzter vs. wahrer (simulierter) Aktions-Kreativitaet (links) und "
         "Rater-Severity (rechts). Nur aussagekraeftig im DEV_MODE-Lauf mit simulierten Daten.")
plt.show()
""")

