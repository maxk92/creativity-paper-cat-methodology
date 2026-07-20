# ====================================================================
# 11. JUDGE-RESPONSE-THEORY-ARTIGE ERWEITERUNG (Abschnitt 12 des Auftrags)
# ====================================================================
md(r"""
## 10. Judge-Response-Theory (JRT) / Many-Facet-Rasch-artige Erweiterung

### 10.1 Konzeption

Judge Response Theory (Myszkowski & Storme, 2019) überträgt polytome
IRT-Modelle auf Urteilsdaten: Rater werden als Messinstrumente
("Items") betrachtet, Aktionen als zu messende Objekte. Eine
Graded-Response-Form ist:

$$
P(Y_{ij}\ge k \mid \theta_i) = \operatorname{logit}^{-1}
\left[a_j(\theta_i-b_{jk})\right]
$$

mit $\theta_i$ = Kreativität von Aktion $i$, $a_j$ = **Diskrimination**
von Rater $j$ (wie stark differenziert Rater $j$ zwischen Aktionen?),
$b_{jk}$ = rater-spezifische Schwelle für Kategorie $k$. Ein
Many-Facet-Rasch-Modell setzt üblicherweise $a_j \equiv 1$ voraus;
JRT lässt rater-spezifische Diskrimination zu.

### 10.2 Vereinfachte, identifizierbare Variante

Volle rater-spezifische Schwellen $b_{jk}$ (40 Rater × 6 Schwellen =
240 zusätzliche Parameter) sind mit der vorliegenden Konnektivität
(median Überlappung siehe Abschnitt 3) nicht mit ausreichender
Präzision schätzbar. Wir schätzen daher eine **reduzierte JRT-Variante**
mit rater-spezifischer Diskrimination bei **globalen** Schwellen:

$$
\eta_{ij} = a_j \cdot \theta_i + \lambda_j, \qquad
\Pr(Y_{ij}\le k) = \operatorname{logit}^{-1}(\tau_k - \eta_{ij})
$$

**Identifikation** (Abschnitt 12.5 des Auftrags): Da $a_j\cdot\theta_i$
eine Skalen-Nichtidentifizierbarkeit aufweist ($a_j\cdot c$ und
$\theta_i/c$ ergeben denselben Fit für beliebiges $c$), fixieren wir
$\theta_i \sim \mathcal N(0,1)$ **exakt** (keine freie
Aktionsvarianz — anders als im Modell aus Abschnitt 9, wo
$\sigma_\theta$ frei geschätzt wird) und lassen $a_j>0$ (über
$a_j=\exp(\log a_j)$) frei. $\lambda_j$ bleibt wie zuvor die
Severity/Leniency.
""")

code(r"""
with pm.Model(coords={"action": action_levels_o, "rater": rater_levels_o,
                        "cut": range(6)}) as jrt_model:
    theta_jrt = pm.Normal("theta", 0, 1, dims="action")  # fixierte Skala: Var(theta)=1

    sigma_lambda_jrt = pm.Exponential("sigma_lambda", 1.0)
    lam_raw_jrt = pm.Normal("lam_raw", 0, 1, dims="rater")
    lam_jrt = pm.Deterministic("lam", lam_raw_jrt * sigma_lambda_jrt, dims="rater")

    sigma_log_a = pm.Exponential("sigma_log_a", 2.0)
    log_a_raw = pm.Normal("log_a_raw", 0, 1, dims="rater")
    log_a = pm.Deterministic("log_a", log_a_raw * sigma_log_a, dims="rater")
    a_j = pm.Deterministic("discrimination", pm.math.exp(log_a), dims="rater")

    cutpoints_jrt = pm.Normal(
        "cutpoints", mu=np.linspace(-2.5, 2.5, 6), sigma=1.5,
        transform=pm.distributions.transforms.ordered, dims="cut",
    )
    # Bugfix: kein initval= (siehe Kommentar im ordinalen Modell, Abschnitt 9).

    eta_jrt = a_j[rater_idx_o] * theta_jrt[action_idx_o] + lam_jrt[rater_idx_o]
    pm.OrderedLogistic("y_obs", eta=eta_jrt, cutpoints=cutpoints_jrt, observed=y_ord)

    idata_jrt = pm.sample(draws=800, tune=800, chains=4, cores=4,
                            target_accept=0.9, random_seed=SEED,
                            progressbar=False)
    pm.compute_log_likelihood(idata_jrt)

idata_jrt.to_netcdf(str(RESULTS_MODELS / "jrt_discrimination_model.nc"))
print("Modell gespeichert: results/models/jrt_discrimination_model.nc")
""")

md(r"""
### 10.3 Diagnostik und Modellvergleich (LOO-CV)

Wir prüfen Konvergenz wie zuvor und vergleichen das JRT-Modell mit dem
einfacheren Facettenmodell aus Abschnitt 9 über
**Pareto-smoothed-importance-sampling LOO-CV**. Ein niedrigerer
`elpd_loo` bzw. ein negatives `elpd_diff` relativ zum Referenzmodell
zeigt schlechtere Out-of-sample-Vorhersage; die Pareto-$k$-Diagnostik
zeigt an, wie verlässlich die LOO-Approximation je Beobachtung ist.
""")

code(r"""
summary_jrt = az.summary(idata_jrt, var_names=["sigma_lambda", "sigma_log_a", "cutpoints"],
                           round_to=4)
print(summary_jrt)
save_table(summary_jrt.reset_index().rename(columns={"index": "parameter"}), "jrt_model_summary")

n_div_jrt = int(idata_jrt.sample_stats["diverging"].sum())
max_rhat_jrt = float(summary_jrt["r_hat"].max())
print(f"Divergenzen: {n_div_jrt}, Max R-hat: {max_rhat_jrt:.4f}")
if max_rhat_jrt >= 1.01:
    log_warning(f"Max R-hat = {max_rhat_jrt:.4f} >= 1.01 fuer das JRT-Modell.")
if n_div_jrt > 0:
    log_warning(f"{n_div_jrt} Divergenzen im JRT-Modell.")

disc = idata_jrt.posterior["discrimination"].mean(dim=("chain", "draw")).values
disc_low = idata_jrt.posterior["discrimination"].quantile(0.025, dim=("chain", "draw")).values
disc_high = idata_jrt.posterior["discrimination"].quantile(0.975, dim=("chain", "draw")).values
jrt_rater_table = pd.DataFrame({
    "rater_id": rater_levels_o,
    "jrt_discrimination": disc,
    "jrt_discrimination_lower": disc_low,
    "jrt_discrimination_upper": disc_high,
    "jrt_severity": idata_jrt.posterior["lam"].mean(dim=("chain", "draw")).values,
})
save_table(jrt_rater_table, "jrt_rater_table")

print(f"\nDiskrimination: Median={np.median(disc):.2f}, Range=[{disc.min():.2f}, {disc.max():.2f}]")
print("Rater mit auffaellig niedriger Diskrimination (< 0.5, d.h. differenzieren kaum "
      f"zwischen Aktionen): {(disc < 0.5).sum()}")
""")

code(r"""
try:
    loo_ordinal = az.loo(idata_ord, pointwise=True)
    loo_jrt = az.loo(idata_jrt, pointwise=True)
    print("LOO ordinales Modell (globale Diskrimination=1):")
    print(loo_ordinal)
    print("\nLOO JRT-Modell (rater-spezifische Diskrimination):")
    print(loo_jrt)

    loo_comparison = pd.DataFrame({
        "model": ["ordinal (a=1 fuer alle Rater)", "JRT (rater-spez. Diskrimination)"],
        "elpd_loo": [float(loo_ordinal.elpd_loo), float(loo_jrt.elpd_loo)],
        "se": [float(loo_ordinal.se), float(loo_jrt.se)],
        "p_loo": [float(loo_ordinal.p_loo), float(loo_jrt.p_loo)],
    })
    loo_comparison["elpd_diff_vs_best"] = loo_comparison["elpd_loo"] - loo_comparison["elpd_loo"].max()
    save_table(loo_comparison, "loo_model_comparison")
    print(loo_comparison)

    pareto_k_ord = loo_ordinal.pareto_k.values
    pareto_k_jrt = loo_jrt.pareto_k.values
    print(f"\nAnteil Pareto-k > 0.7 (ordinal): {(pareto_k_ord > 0.7).mean():.1%}")
    print(f"Anteil Pareto-k > 0.7 (JRT): {(pareto_k_jrt > 0.7).mean():.1%}")
    if (pareto_k_ord > 0.7).mean() > 0.05 or (pareto_k_jrt > 0.7).mean() > 0.05:
        log_warning("Mehr als 5% der Beobachtungen haben Pareto-k > 0.7 - LOO-Schaetzung "
                     "fuer diese Punkte ist unzuverlaessig.")
except Exception as e:
    log_warning(f"LOO-Modellvergleich fehlgeschlagen: {e}")
    loo_comparison = pd.DataFrame()
""")

md(r"""
### 10.4 Interpretation

Ein höherer `elpd_loo` beim JRT-Modell würde dafür sprechen, dass
rater-spezifische Diskrimination echte, vorhersagerelevante
Heterogenität abbildet. Ein vernachlässigbarer oder negativer
Unterschied (innerhalb ~1-2 Standardfehlern von `elpd_diff`) spricht
für das einfachere Modell aus Abschnitt 9 (Sparsamkeitsprinzip: "JRT
ist nicht automatisch besser als ein einfacheres Modell", Abschnitt 22
des Analyseauftrags). Der tatsächliche Vergleichswert steht in
`results/tables/loo_model_comparison.csv` und wird im automatisierten
Interpretationsblock (Abschnitt 17) referenziert.

**Hinweis zu Python vs. R für JRT:** Für Python existiert kein
etabliertes, eigenständiges JRT-Paket (Stand dieser Analyse); wir
implementieren daher die JRT-Logik direkt in PyMC (wie oben). Das
**R-Notebook** verwendet zusätzlich das dedizierte CRAN-Paket `jrt`
(Myszkowski, 2021) als Cross-Check, sofern dessen Installation im
jeweiligen Lauf erfolgreich war.
""")

