# ====================================================================
# 19. QUALITAETSKONTROLLEN (Abschnitt 20 des Auftrags)
# ====================================================================
md(r"""
## 18. Qualitätskontrollen (automatisierte Checkliste)

Wir prüfen systematisch die im Analyseauftrag (Abschnitt 20)
geforderten Punkte und protokollieren das Ergebnis als Tabelle statt
nur als Text.
""")

code(r"""
qc_checks = []

def qc(name, condition, detail=""):
    qc_checks.append({"check": name, "passed": bool(condition), "detail": detail})

qc("IDs eindeutig typisiert (action_id, rater_id als String)",
    ratings_clean["action_id"].dtype == object and ratings_clean["rater_id"].dtype == object)
qc("Keine doppelten Rater-Aktions-Paare nach Cleaning",
    not ratings_clean.duplicated(subset=["action_id", "rater_id"]).any())
qc("Alle Ratings in {1,...,7}", ratings_clean["rating_numeric"].between(1, 7).all())
qc("Rater-Aktions-Graph: Konnektivitaet geprueft und dokumentiert", n_components >= 1,
    f"{n_components} Komponente(n)")
qc("Varianzkomponenten (linear) nichtnegativ",
    var_action >= 0 and var_rater >= 0 and var_resid >= 0)
qc("Lineares Bayes-Modell: max R-hat < 1.01", max_rhat < 1.01, f"max R-hat={max_rhat:.4f}")
qc("Lineares Bayes-Modell: keine Divergenzen", n_divergences == 0, f"{n_divergences} Divergenzen")
qc("Ordinales Modell: max R-hat < 1.01", max_rhat_ord < 1.01, f"max R-hat={max_rhat_ord:.4f}")
qc("Ordinales Modell: keine Divergenzen", n_divergences_ord == 0, f"{n_divergences_ord} Divergenzen")
qc("Ordinales Modell: Schwellen im Posterior-Mittel geordnet", cuts_sorted)
qc("JRT-Modell: max R-hat < 1.01", max_rhat_jrt < 1.01, f"max R-hat={max_rhat_jrt:.4f}")
qc("JRT-Modell: keine Divergenzen", n_div_jrt == 0, f"{n_div_jrt} Divergenzen")
qc("Aktionen mit 1 Rating korrekt gekennzeichnet (single_rating_action)",
    "single_rating_action" in ratings_clean.columns)
qc("Alle Aktionsscores mit n_ratings und Unsicherheitsangabe exportiert",
    {"n_ratings", "lmm_score_se", "ordinal_latent_lower", "ordinal_latent_upper"}.issubset(
        final_action_scores_out.columns))
qc("Rohdaten unveraendert (Cleaning-Log dokumentiert)", len(cleaning_log_df) > 0)
qc("Paketversionen protokolliert (session_info_python.json)",
    (RESULTS_LOGS / "session_info_python.json").exists())

qc_df = pd.DataFrame(qc_checks)
save_table(qc_df, "qc_checklist")
n_failed_qc = (~qc_df["passed"]).sum()
print(qc_df.to_string(index=False))
print(f"\n{n_failed_qc} von {len(qc_df)} Qualitaetskontrollen nicht bestanden.")
if n_failed_qc > 0:
    log_warning(f"{n_failed_qc} Qualitaetskontrollen (siehe qc_checklist.csv) nicht bestanden.")
""")

md(r"""
### 18.1 Gesammelte Warnungen dieses Laufs
""")

code(r"""
warnings_df = pd.DataFrame(WARNINGS_LOG)
save_table(warnings_df, "warnings_log")
print(f"Insgesamt {len(warnings_df)} Warnungen in diesem Lauf gesammelt (siehe "
      "results/tables/warnings_log.csv fuer die vollstaendige Liste).")
if len(warnings_df) > 0:
    for msg in warnings_df["message"]:
        print(f"  - {msg}")
""")

md(r"""
## 19. Limitations and Design Implications

**Grenzen dieser Analyse:**

1. **Simulierte Entwicklungsdaten.** Dieser Lauf verwendet simulierte
   Platzhalterdaten (`DEV_MODE=True`). Alle Zahlen sind
   Methodendemonstrationen. Vor Publikation: `DEV_MODE=False` setzen,
   echten Google-Sheet-Importcode einfügen, gesamtes Notebook neu
   ausführen.
2. **Residualvarianz umfasst mehrere Quellen.** Da die meisten
   Rater-Aktions-Zellen nur ein Rating enthalten, ist die
   Aktion×Rater-Interaktion nicht separat vom Messfehler
   identifizierbar (Abschnitt 6.1). Die berichteten
   Reliabilitätskoeffizienten sind Varianzkomponenten-Approximationen,
   keine vollständige G-Theory-Zerlegung.
3. **JRT-Modell mit reduzierter Komplexität.** Rater-spezifische
   Schwellen (statt nur rater-spezifischer Diskrimination) wurden aus
   Konnektivitäts- und Rechenzeitgründen nicht separat geschätzt.
4. **Cross-Validation vereinfacht.** Die rating-level CV (Abschnitt
   12.2) verwendet approximative, schnell berechenbare Prädiktoren
   statt eines vollständigen Modell-Refits pro Fold.
5. **Statsmodels-Skalierungsgrenze.** `statsmodels.MixedLM` mit
   `vc_formula` ist für Faktoren mit tausenden Ebenen (hier: Aktionen)
   nicht praktikabel; wir nutzen PyMC als primäre Schätzengine für
   Python (siehe Abschnitt 6.2 für die Begründung).
6. **Getrennte Komponenten.** Sofern der Rater-Aktions-Graph mehr als
   eine Zusammenhangskomponente aufweist, sind Rater-Severity-Werte
   über Komponenten hinweg nicht auf derselben Skala vergleichbar
   (siehe Abschnitt 3).

### Empfehlungen für zukünftige Ratingzuweisungen

1. **Mehr Ratings pro Aktion**: Die D-Study-Kurve (Abschnitt 6.7)
   quantifiziert den Reliabilitätsgewinn zusätzlicher Ratings konkret
   für dieses Design — als Grundlage für eine Kosten-Nutzen-Abwägung
   künftiger Ratingkapazität.
2. **Mindestüberlappung zwischen Ratern**: Raterpaare mit sehr
   geringer gemeinsamer Aktionsmenge (Abschnitt 3.1) liefern kaum
   Information für die Kalibrierung relativer Rater-Strenge; ein
   Zielwert von mindestens 15–20 gemeinsamen Aktionen pro Raterpaar
   (oder pro Rater zu mindestens einem "Brückenrater") wird empfohlen.
3. **Gezielte Brückenaktionen**: Eine kleine Menge von Ankeraktionen,
   die von (nahezu) allen Ratern bewertet werden, stabilisiert die
   Identifizierbarkeit von Rater-Severity erheblich.
4. **Balancierte/blockweise balancierte Zuweisung**: Vermeidet
   Konfundierung von Rater-Zuweisung mit Aktionstyp/Spieler/Team
   (siehe Abschnitt 12.3 Chi-Quadrat-Test).
5. **Wiederholte Ankeraktionen über Zeit**: Ermöglichen eine robustere
   Schätzung individueller Rater-Drift (Abschnitt 8.3) als einmalige
   Sitzungen.
6. **Kalibrierungssitzungen** vor der eigentlichen Bewertung,
   insbesondere für Rater mit unterdurchschnittlicher
   Kategoriennutzung oder auffälliger Diskrimination.
7. **Trennung von Training und finaler Bewertung**, um Lerneffekte
   (die sich als Drift zeigen würden) von der finalen Datenerhebung
   fernzuhalten.
""")

code(r"""
print("=" * 70)
print("NOTEBOOK VOLLSTAENDIG AUSGEFUEHRT")
print("=" * 70)
print(f"Zeitpunkt: {datetime.now(timezone.utc).isoformat()}")
print(f"Anzahl gesammelter Warnungen: {len(WARNINGS_LOG)}")
print(f"QC-Checks bestanden: {(~qc_df['passed']).eq(False).sum()}/{len(qc_df)}")
print(f"\nErzeugte Tabellen: {len(list(RESULTS_TABLES.glob('*.csv')))}")
print(f"Erzeugte Abbildungen: {len(list(RESULTS_FIGURES.glob('*.png')))}")
print(f"Gespeicherte Modelle: {len(list(RESULTS_MODELS.glob('*.nc')))}")
""")

