# ====================================================================
# 18. AUTOMATISIERTER INTERPRETATIONSBLOCK (Abschnitt 19 des Auftrags)
# ====================================================================
md(r"""
## 17. Automatisierte, vorsichtige Interpretation

Der folgende Text wird **automatisch aus den tatsächlich berechneten
Zahlen dieses Laufs generiert** (keine erfundenen Werte). Er ersetzt
keine inhaltliche Diskussion durch die Autor:innen, sondern fasst die
statistischen Befunde vorsichtig zusammen. **Feste Grenzwerte werden
nicht mechanisch als gut/schlecht deklariert.**
""")

code(r"""
rel_vs_abs = "hoeher" if d_study.loc[0, "rho_rel"] > d_study.loc[0, "rho_abs"] else "nicht wesentlich hoeher"
rater_effect_strength = "spuerbaren" if var_rater / (var_action + var_rater + var_resid) > 0.05 else "eher geringen"

pct_action = variance_components_df.loc[0, "pct_of_total"]
pct_rater = variance_components_df.loc[1, "pct_of_total"]
pct_resid = variance_components_df.loc[2, "pct_of_total"]
rho_rel_1 = d_study.loc[0, "rho_rel"]
rho_abs_1 = d_study.loc[0, "rho_abs"]
rho_abs_7 = d_study.loc[6, "rho_abs"]
n_single = int((ratings_per_action == 1).sum())
n_outside_largest = ratings_clean.action_id.nunique() - len(largest_component_actions)

if n_components == 1:
    component_note = "Alle Rater-Severity-Schaetzungen sind daher auf einer gemeinsamen Skala interpretierbar."
else:
    component_note = (
        f"Rater-Severity-Schaetzungen aus kleineren Komponenten (insgesamt {n_outside_largest} "
        "Aktionen ausserhalb der groessten Komponente) sind NICHT direkt mit denen der groessten "
        "Komponente vergleichbar und wurden entsprechend gekennzeichnet."
    )

if len(loo_comparison) > 0:
    elpd_diff = loo_comparison["elpd_loo"].iloc[1] - loo_comparison["elpd_loo"].iloc[0]
    loo_note = (
        f"elpd_loo-Unterschied von {elpd_diff:.1f} (JRT minus einfaches Modell, positiv = JRT "
        "sagt Out-of-Sample besser vorher); falls dieser Unterschied klein relativ zum "
        "Standardfehler ist, ist das einfachere Modell aus Sparsamkeitsgruenden vorzuziehen."
    )
else:
    loo_note = "LOO-Modellvergleich konnte in diesem Lauf nicht berechnet werden."

interpretation_text = f'''
Das lineare Varianzkomponentenmodell (Abschnitt 6) zerlegte die beobachtete
Ratingvarianz in {pct_action:.1%} Unterschiede zwischen Aktionen,
{pct_rater:.1%} systematische Unterschiede zwischen Ratern und {pct_resid:.1%}
residuale Abweichungen (Aktion x Rater-Interaktion, Messfehler, weitere nicht
modellierte Einfluesse). Die relative Reliabilitaet eines Einzelratings
(rho_rel={rho_rel_1:.2f}) fiel {rel_vs_abs} aus als die absolute
Reliabilitaet (rho_abs={rho_abs_1:.2f}). Dieses Muster ist mit
{rater_effect_strength} systematischen Rater-Niveaueffekten vereinbar
(sigma^2_rater macht {pct_rater:.1%} der Gesamtvarianz aus).

Krippendorffs ordinales Alpha lag bei {alpha_ordinal:.2f}
(95%-Cluster-Bootstrap-CI [{ci_ord[0]:.2f}, {ci_ord[1]:.2f}], n_boot={N_BOOT}).
Dieser Wert beschreibt die globale Uebereinstimmung ueber alle Aktionen und
Rater hinweg unter Beruecksichtigung des unvollstaendigen Designs.

Die D-Study-Kurve zeigt, dass die absolute Reliabilitaet des Aktionsmittelwerts
von rho_abs(k=1)={rho_abs_1:.2f} auf rho_abs(k=7)={rho_abs_7:.2f} ansteigt, wenn
sieben statt einem Rater gemittelt werden - ein direkter quantitativer Beleg
fuer den Wert zusaetzlicher Ratings pro Aktion, besonders relevant fuer die
{n_single} Aktionen mit aktuell nur einem Rating.

Der Rater-Aktions-Graph zerfaellt in {n_components} Zusammenhangskomponente(n).
{component_note}

Der Modellvergleich zwischen dem einfachen ordinalen Facettenmodell und der
JRT-Erweiterung mit rater-spezifischer Diskrimination ergab einen {loo_note}

Die Interpretation bezieht sich auf das vorliegende, unvollstaendig
gekreuzte Design. Aktionen mit nur einem Rating tragen zur modellbasierten
Schaetzung der Aktionsverteilung bei, liefern aber keine innerhalb der Aktion
beobachtete Information ueber Interrater-Uebereinstimmung.

WICHTIG: Dieser Lauf verwendet SIMULIERTE Platzhalterdaten (DEV_MODE=True).
Die oben genannten Zahlen sind Methodendemonstrationen, keine realen Befunde
ueber tatsaechliche Kreativitaetsratings.
'''

print(interpretation_text)
with open(RESULTS_LOGS / "automated_interpretation.txt", "w") as f:
    f.write(interpretation_text)
""")

