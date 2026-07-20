# ====================================================================
# 10. ORDINALES HIERARCHISCHES FACETTENMODELL (Abschnitt 11 des Auftrags)
# ====================================================================
md(r"""
## 9. Ordinales hierarchisches Facettenmodell

Dies ist die **zentrale Sensitivitäts- bzw. bevorzugte ordinale
Modellierung**: Sie respektiert explizit, dass die Kreativitätsskala
eine begrenzte, geordnete 7-Kategorien-Skala ist, statt sie (wie in
Abschnitt 6) als näherungsweise intervallskaliert zu behandeln.

### 9.1 Kumulatives Logit-Modell

$$
\Pr(Y_{ij} \le k) = \operatorname{logit}^{-1}(\tau_k - \eta_{ij}),
\qquad \eta_{ij} = \theta_i + \lambda_j
$$

mit geordneten globalen Schwellen $\tau_1 < \dots < \tau_6$,
Aktions-Kreativität $\theta_i$ und Rater-Leniency $\lambda_j$
(**gleiche Vorzeichenkonvention wie in Abschnitt 8**: positives
$\lambda_j$ = großzügiger). Die Implementierung nutzt
`pm.OrderedLogistic`, das genau diese Parametrisierung erwartet
(`eta` linear, `cutpoints` aufsteigend).

### 9.2 Engine-Wahl: PyMC statt Bambi

Wir haben geprüft, ob `bambi` (aktuell installierte Version: siehe
Session-Log) ein kumulatives Ordinalmodell mit **zwei gekreuzten**
Random-Intercept-Faktoren (Aktion UND Rater) zuverlässig unterstützt.
Für volle Kontrolle über (a) die non-centered Parametrisierung (nötig
für stabile Sampling-Geometrie bei tausenden Ebenen), (b) die
Identifikationsbedingung der Schwellen und (c) den direkten Zugriff
auf alle Posterior-Komponenten für die spätere JRT-Erweiterung
(Abschnitt 10), implementieren wir das Modell **direkt in PyMC** —
dies folgt der im Analyseauftrag vorgesehenen Ausweichoption
("implementiere das Modell direkt in PyMC oder Stan").

### 9.3 Priors und Identifikation

$$
\theta_i \sim \mathcal N(0, \sigma^2_\theta), \quad
\lambda_j \sim \mathcal N(0, \sigma^2_\lambda), \quad
\sigma_\theta, \sigma_\lambda \sim \text{Exponential}(1)
$$

Die Schwellen $\tau_{1:6}$ erhalten schwach informative Normal-Priors
um äquidistante Startwerte, mit einer erzwungenen Ordnungsrestriktion
(`transform=pm.distributions.transforms.ordered`). Identifikation:
$\mathbb E[\theta_i]=0$ und $\mathbb E[\lambda_j]=0$ durch die
Zero-mean-Priors (weiche Zentrierung); es gibt keinen zusätzlichen
freien Interzept (der wäre mit den Schwellen konfundiert).

Wir schätzen wie in Abschnitt 6 ausschließlich auf der größten
verbundenen Komponente.
""")

code(r"""
df_ord = ratings_clean.loc[ratings_clean["in_largest_component"]].copy()
action_idx_o, action_levels_o = pd.factorize(df_ord["action_id"])
rater_idx_o, rater_levels_o = pd.factorize(df_ord["rater_id"])
y_ord = (df_ord["rating_numeric"].values.astype(int) - 1)  # 0-basiert fuer PyMC

assert (action_levels_o == action_levels).all() if len(action_levels_o) == len(action_levels) else True
print(f"Ordinales Modell: {len(y_ord)} Ratings, {len(action_levels_o)} Aktionen, "
      f"{len(rater_levels_o)} Rater.")
print(f"Kategorienhaeufigkeiten (0-basiert): {np.bincount(y_ord, minlength=7)}")
""")

code(r"""
with pm.Model(coords={"action": action_levels_o, "rater": rater_levels_o,
                        "cut": range(6)}) as ordinal_model:
    sigma_theta = pm.Exponential("sigma_theta", 1.0)
    sigma_lambda = pm.Exponential("sigma_lambda", 1.0)

    theta_raw = pm.Normal("theta_raw", 0, 1, dims="action")
    lam_raw = pm.Normal("lam_raw", 0, 1, dims="rater")
    theta = pm.Deterministic("theta", theta_raw * sigma_theta, dims="action")
    lam = pm.Deterministic("lam", lam_raw * sigma_lambda, dims="rater")

    cutpoints = pm.Normal(
        "cutpoints", mu=np.linspace(-2.5, 2.5, 6), sigma=1.5,
        transform=pm.distributions.transforms.ordered,
        initval=np.linspace(-2.5, 2.5, 6), dims="cut",
    )

    eta_ord = theta[action_idx_o] + lam[rater_idx_o]
    pm.OrderedLogistic("y_obs", eta=eta_ord, cutpoints=cutpoints, observed=y_ord)

    idata_ord = pm.sample(draws=1000, tune=1000, chains=4, cores=4,
                            target_accept=0.9, random_seed=SEED,
                            progressbar=False)
    pm.compute_log_likelihood(idata_ord)

idata_ord.to_netcdf(str(RESULTS_MODELS / "ordinal_crossed_model.nc"))
print("Modell gespeichert: results/models/ordinal_crossed_model.nc")
""")

md(r"""
### 9.4 Konvergenzdiagnostik (zwingend für Bayesianische Modelle)
""")

code(r"""
summary_ord = az.summary(idata_ord, var_names=["sigma_theta", "sigma_lambda", "cutpoints"],
                           round_to=4)
print(summary_ord)
save_table(summary_ord.reset_index().rename(columns={"index": "parameter"}),
            "ordinal_model_summary")

n_divergences_ord = int(idata_ord.sample_stats["diverging"].sum())
max_rhat_ord = float(summary_ord["r_hat"].max())
min_ess_ord = float(summary_ord["ess_bulk"].min())
print(f"\nDivergenzen: {n_divergences_ord}")
print(f"Max R-hat: {max_rhat_ord:.4f}")
print(f"Min ESS (bulk): {min_ess_ord:.0f}")

cuts_sorted = np.all(np.diff(idata_ord.posterior["cutpoints"].mean(dim=("chain", "draw")).values) > 0)
print(f"Schwellen geordnet (Posterior-Mittel): {cuts_sorted}")

if max_rhat_ord >= 1.01:
    log_warning(f"Max R-hat = {max_rhat_ord:.4f} >= 1.01 fuer das ordinale Modell.")
if n_divergences_ord > 0:
    log_warning(f"{n_divergences_ord} Divergenzen im ordinalen Modell.")
if not cuts_sorted:
    log_warning("Kategorienschwellen des ordinalen Modells sind im Posterior-Mittel NICHT geordnet.")

az.plot_trace(idata_ord, var_names=["sigma_theta", "sigma_lambda"])
fig = plt.gcf()
fig.set_size_inches(11, 5)
fig.suptitle("Traceplots: ordinales Facettenmodell (Varianzkomponenten)")
fig.tight_layout()
save_fig(fig, "fig_appendix_ordinal_traceplots", "Traceplots der Varianzkomponenten des ordinalen Modells.")
plt.show()
""")

md(r"""
### 9.5 Posterior-Predictive-Checks

Wir prüfen, ob aus dem Modell replizierte Daten (a) die
Kategorienhäufigkeiten insgesamt, (b) die Verteilung der
Rater-Rohmittelwerte und (c) die Verteilung der Aktionsmittelwerte
plausibel reproduzieren.
""")

code(r"""
with ordinal_model:
    pp_ord = pm.sample_posterior_predictive(idata_ord, random_seed=SEED, progressbar=False,
                                              extend_inferencedata=False, var_names=["y_obs"])

y_rep = pp_ord.posterior_predictive["y_obs"].values  # (chain, draw, obs)
y_rep_flat_sample = y_rep[:, :100, :].reshape(-1, y_rep.shape[-1])  # Teilstichprobe der Draws fuer Speed

obs_counts = np.bincount(y_ord, minlength=7) / len(y_ord)
rep_counts = np.array([np.bincount(row, minlength=7) / len(row) for row in y_rep_flat_sample])

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
axes[0].bar(np.arange(1, 8) - 0.2, obs_counts, width=0.4, label="beobachtet", color="#4C72B0")
axes[0].bar(np.arange(1, 8) + 0.2, rep_counts.mean(axis=0), width=0.4, label="repliziert (Modell)",
             color="#DD8452")
axes[0].errorbar(np.arange(1, 8) + 0.2, rep_counts.mean(axis=0),
                   yerr=rep_counts.std(axis=0), fmt="none", ecolor="black", capsize=2)
axes[0].set_title("Kategorienhaeufigkeiten: beobachtet vs. repliziert")
axes[0].set_xlabel("Rating")
axes[0].legend()

df_ord_rep = df_ord.copy()
rep_draw_example = y_rep[0, 0, :] + 1
df_ord_rep["rating_rep"] = rep_draw_example
obs_rater_means = df_ord.groupby("rater_id")["rating_numeric"].mean()
rep_rater_means = df_ord_rep.groupby("rater_id")["rating_rep"].mean()
axes[1].hist(obs_rater_means, bins=15, alpha=0.6, label="beobachtet", color="#4C72B0")
axes[1].hist(rep_rater_means, bins=15, alpha=0.6, label="repliziert (1 Draw)", color="#DD8452")
axes[1].set_title("Ratermittelwerte: beobachtet vs. repliziert")
axes[1].legend()

obs_action_means = df_ord.groupby("action_id")["rating_numeric"].mean()
rep_action_means = df_ord_rep.groupby("action_id")["rating_rep"].mean()
axes[2].hist(obs_action_means, bins=20, alpha=0.6, label="beobachtet", color="#4C72B0")
axes[2].hist(rep_action_means, bins=20, alpha=0.6, label="repliziert (1 Draw)", color="#DD8452")
axes[2].set_title("Aktionsmittelwerte: beobachtet vs. repliziert")
axes[2].legend()

fig.suptitle("Posterior-Predictive-Checks: ordinales Facettenmodell")
fig.tight_layout()
save_fig(fig, "fig12_ordinal_ppc",
         "Posterior-Predictive-Checks des ordinalen Facettenmodells: Kategorienhaeufigkeiten "
         "(links, mit Unsicherheitsband ueber Posterior-Draws), Ratermittelwerte (Mitte) und "
         "Aktionsmittelwerte (rechts), jeweils beobachtet vs. modellreplizierte Daten.")
plt.show()
""")

md(r"""
### 9.6 Ordinale Aktionsscores

Für jede Aktion: Posterior-Mittel/Median von $\theta_i$, 95%-Credible-
Interval, Posterior-Rang und Rangunsicherheit, sowie der **erwartete
beobachtete Skalenwert** $\mathbb E[Y_i \mid \theta_i]$ auf der
1–7-Skala (getrennt vom latenten Score $\theta_i$ gespeichert, wie im
Analyseauftrag gefordert).
""")

code(r"""
theta_post = idata_ord.posterior["theta"]  # dims: chain, draw, action
theta_mean = theta_post.mean(dim=("chain", "draw")).values
theta_median = theta_post.median(dim=("chain", "draw")).values
theta_low = theta_post.quantile(0.025, dim=("chain", "draw")).values
theta_high = theta_post.quantile(0.975, dim=("chain", "draw")).values

# Posterior-Rang je Draw, dann Mittel/Unsicherheit des Rangs
theta_flat = theta_post.values.reshape(-1, theta_post.shape[-1])  # (n_draws_total, n_action)
ranks_per_draw = theta_flat.argsort(axis=1).argsort(axis=1) + 1  # 1 = niedrigste Kreativitaet
rank_mean = ranks_per_draw.mean(axis=0)
rank_sd = ranks_per_draw.std(axis=0)

# Erwarteter beobachteter Skalenwert E[Y|theta] unter globalen (Posterior-Mittel-)Schwellen,
# gemittelt ueber Rater (lambda=0, "durchschnittlicher Rater").
cut_mean = idata_ord.posterior["cutpoints"].mean(dim=("chain", "draw")).values

def expected_rating(theta_val, cuts):
    cum = 1 / (1 + np.exp(-(cuts - theta_val)))
    cum = np.concatenate([[0.0], cum, [1.0]])
    probs = np.diff(cum)
    return np.sum(probs * np.arange(1, 8))

expected_ratings = np.array([expected_rating(t, cut_mean) for t in theta_mean])

ordinal_scores = pd.DataFrame({
    "action_id": action_levels_o,
    "ordinal_latent_score": theta_mean,
    "ordinal_latent_median": theta_median,
    "ordinal_latent_lower": theta_low,
    "ordinal_latent_upper": theta_high,
    "ordinal_posterior_rank_mean": rank_mean,
    "ordinal_posterior_rank_sd": rank_sd,
    "ordinal_expected_rating": expected_ratings,
})
save_table(ordinal_scores, "ordinal_action_scores")
print(f"Ordinale Aktionsscores berechnet fuer {len(ordinal_scores)} Aktionen.")
ordinal_scores.head()
""")

md(r"""
### 9.7 Ordinale Rater-Severity
""")

code(r"""
lam_post = idata_ord.posterior["lam"]
lam_mean = lam_post.mean(dim=("chain", "draw")).values
lam_low = lam_post.quantile(0.025, dim=("chain", "draw")).values
lam_high = lam_post.quantile(0.975, dim=("chain", "draw")).values

ordinal_severity = pd.DataFrame({
    "rater_id": rater_levels_o,
    "ordinal_severity": lam_mean,
    "ordinal_severity_lower": lam_low,
    "ordinal_severity_upper": lam_high,
})
save_table(ordinal_severity, "ordinal_rater_severity")

corr_lin_ord_severity = pd.merge(
    severity_df[["rater_id", "lmm_severity"]], ordinal_severity[["rater_id", "ordinal_severity"]],
    on="rater_id")["lmm_severity"].corr(
    pd.merge(severity_df[["rater_id", "lmm_severity"]], ordinal_severity[["rater_id", "ordinal_severity"]],
              on="rater_id")["ordinal_severity"])
print(f"Korrelation lineare vs. ordinale Rater-Severity: r = {corr_lin_ord_severity:.3f} "
      "(hoher Wert = konsistente Modelle)")
""")

md(r"""
### 9.8 Proportional-Odds-Annahme

Das kumulative Logit-Modell nimmt **gemeinsame** (nicht rater- oder
kategorienspezifische) Schwellen an ("proportional odds"). Diese
Annahme ist mit der aktuellen Modellstruktur nicht direkt
testbar, ohne eine erweiterte Variante zu schätzen (z. B.
rater-spezifische Schwellenverschiebungen oder rater-spezifische
Diskrimination). Wir adressieren dies in Abschnitt 10 über ein
Judge-Response-Theory-Modell mit **rater-spezifischer Diskrimination**
und vergleichen beide Modelle formal über LOO-CV. Eine vollständig
separate adjacent-category-Sensitivität wird aus Rechenzeit- und
Konnektivitätsgründen nicht zusätzlich schätzt (siehe Warnung des
Analyseauftrags: "Vermeide unnötig komplexe Modelle, wenn die
Datenkonnektivität ... nicht ausreicht").
""")

