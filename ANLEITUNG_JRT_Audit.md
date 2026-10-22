# Auftrag: Audit und Bereinigung der JRT-/MFRM-Analyse von Kreativitätsratings

## Kontext für dich (Claude Code)

In diesem Repository liegt bereits eine umfangreiche Analyse von Kreativitätsratings mit Code und mehreren Notebooks. Bewertet werden viele Stimuli bzw. Produkte von einem kleinen Panel aus Ratern. Das Design ist **dünn besetzt**: Nicht jede Raterin bewertet jedes Produkt. Ein Many-Facet Rasch Model wurde bisher mit `sirt::rm.facets()` geschätzt.

Deine Aufgabe ist **nicht**, die Analyse neu zu erfinden. Du sollst:

1. prüfen, ob die vorhandene Umsetzung der Spezifikation unten in allen technischen Details entspricht,
2. Abweichungen korrigieren und fehlende Teile ergänzen,
3. alle Analysen, die **nicht** in dieser Spezifikation stehen, nach Rückfrage entfernen.

Das **zentrale Modell** ist JRT mit dem **Graded Response Model (GRM)**, geschätzt per **MML**. Mit seinen Scores, Informations- und Reliabilitätswerten wird später weitergearbeitet. Das GPCM, das MFRM und die naiven Kennwerte (Cronbachs α, Krippendorffs α) dienen nur dem Vergleich.

---

## Arbeitsweise und Regeln

- **Zuerst einen Branch anlegen** (`git switch -c audit/jrt-spec`). Arbeite nur dort und committe in kleinen, thematischen Schritten.
- **Sprache und Struktur beibehalten:** die vorhandene Sprache (vermutlich R), die Paketkonventionen, die Ordnerstruktur und den Notebook-Stil. Lege keine neue Parallelstruktur an, wenn sich vorhandene Funktionen korrigieren lassen.
- **Nichts löschen ohne Bestätigung.** Erstelle erst eine Liste der Kandidaten zum Entfernen (Abschnitt 1) und warte auf meine Freigabe. Rohdaten und Daten-Importskripte werden nie gelöscht.
- **Fehlende Informationen nicht raten.** Ist die Datenstruktur anders als erwartet (z. B. mehrere Bewertungsdimensionen oder Aufgaben pro Rating, siehe Abschnitt 2), stoppe und frag nach.
- **Reproduzierbarkeit:** feste Seeds, `sessionInfo()` bzw. Paketversionen in die Outputs schreiben, und Ergebnisse nur über Code erzeugen, keine manuell bearbeiteten Dateien.
- Wenn eine Prüfung **nicht** bestanden wird, beschreibe in `AUDIT.md` kurz die Ursache und die Korrektur.

---

## 1. Bestandsaufnahme (vor jeder Änderung)

Lies das Repository vollständig: Notebooks, Skripte, Funktionen, Konfiguration und vorhandene Outputs. Erstelle dann `AUDIT.md` mit:

1. **Inventar:** jede Analyse bzw. jeder Analyseblock, mit Datei, Zellen- oder Funktionsname und einem Satz zum Inhalt.
2. **Zuordnung** jeder Analyse zu einem Spezifikationsschritt (Abschnitte 2–7), mit Status:
   - ✅ entspricht der Spezifikation,
   - ⚠️ vorhanden, aber abweichend (mit Nennung der Abweichung),
   - ❌ fehlt,
   - 🗑️ nicht in der Spezifikation, also Kandidat zum Entfernen.
3. **Abhängigkeiten der 🗑️-Kandidaten:** Wird ihr Output von spezifizierten Analysen genutzt? Falls ja, nicht entfernen, sondern markieren.

**Stopp:** Zeig mir die Zusammenfassung von `AUDIT.md` und warte auf meine Freigabe der Lösch-Liste. Mit den Prüfungen und Korrekturen der Abschnitte 2–7 kannst du parallel weitermachen.

---

## 2. Daten und Design

**Ziel:** eine einzige, geprüfte Datengrundlage, die *alle* Modelle identisch verwenden.

1. Long-Format: `product_id`, `rater_id`, `rating` (+ ggf. weitere Spalten).
2. Wide-Matrix: Produkte × Rater, `NA` für nicht bewertete Kombinationen. Dieselbe Matrix (gleiche Produkte, gleiche Rater, gleiche NA-Struktur) geht in GRM, GPCM, die Modellleiter (RSM/PCM) und α ein. Das MFRM bekommt dieselben Daten im Long-Format, das von `sirt::rm.facets()` erwartet wird.

**Prüfpunkte:**

- [ ] **Mehrere Facetten?** Prüfen, ob es pro Rating weitere Facetten gibt (Bewertungsdimension, Aufgabe, Zeitpunkt). Falls ja: **stoppen und nachfragen**. Die Spezifikation unten geht von *einer* Bewertungsdimension aus, also Produkt × Raterin mit Ratern als „Items“.
- [ ] **Doppelte Ratings** (gleiche Produkt-Rater-Kombination mehrfach) identifizieren und melden, nicht stillschweigend mitteln.
- [ ] **Kategorien:** Die Skala und die Kodierung sind dokumentiert (z. B. 1–5 → intern 0–4).
- [ ] **Kategoriennutzung pro Raterin:** Häufigkeitstabelle Raterin × Kategorie speichern. **Wichtig:** `mirt` rekodiert die beobachteten Kategorien jedes Items intern auf aufeinanderfolgende Ganzzahlen. Nutzt eine Raterin eine Kategorie nie, verschieben sich ihre Kategorien. Dann sind ihre Schwellen nicht mehr mit denen der anderen vergleichbar, und das RSM (gemeinsame Schwellen) ist nicht korrekt spezifiziert. Prüfe, ob das vorkommt und wie der Code damit umgeht. Bei Problemen melden und eine Lösung vorschlagen (z. B. Kategorien zusammenlegen), aber erst nach Rückfrage umsetzen.
- [ ] **Verbundenheit des Designs:** Den bipartiten Graphen Produkt–Raterin auf Zusammenhang prüfen (eine Komponente?). Zusätzlich die Overlap-Matrix der Rater speichern: Anzahl gemeinsam bewerteter Produkte pro Rater-Paar. Ein nicht verbundenes Design ist ein harter Fehler für alle Modelle.
- [ ] **Deskriptive Kennwerte:** Ratings pro Produkt (Verteilung), Ratings pro Raterin, Mittelwert und SD pro Raterin.

**Outputs:** `results/data/ratings_long.*`, `results/data/ratings_wide.*`, `results/data/category_usage.csv`, `results/data/rater_overlap.csv`, `results/data/design_summary.*`

---

## 3. Zentrales Modell: JRT mit Graded Response Model (MML)

**Modell:** Raterinnen werden als Items behandelt, Produkte als Personen.

P(X_nj ≥ k | θ_n) = 1 / (1 + exp(−a_j (θ_n − b_jk)))

mit raterspezifischer Trennschärfe a_j und raterspezifischen, geordneten Schwellen b_jk.

**Schätzung:** `mirt::mirt(data, 1, itemtype = "graded")` auf der Wide-Matrix mit `NA`.

**Prüfpunkte:**

- [ ] **Schätzverfahren:** MML mit EM und Quadratur (Standard bei `mirt`). Das Verfahren ist explizit im Code gesetzt bzw. dokumentiert, ebenso die Zahl der Quadraturpunkte. Für eindimensionale Modelle ist der Standard ausreichend, sollte aber angegeben werden.
- [ ] **Identifikation:** θ ~ N(0, 1), alle a_j und b_jk frei. Es gibt keine zusätzlichen Restriktionen, die nicht begründet sind.
- [ ] **Konvergenz:** Konvergenz geprüft (`extract.mirt(mod, "converged")`), Anzahl der Iterationen gemeldet, keine Warnungen ignoriert.
- [ ] **Standardfehler der Parameter:** mit `SE = TRUE` berechnet. Die Methode ist angegeben (z. B. `SE.type = "Oakes"` oder `"crossprod"`). Prüfen, ob die Informationsmatrix positiv definit ist.
- [ ] **Plausibilität der Parameter:** keine extremen a_j (z. B. > 4) oder b_jk (|b| > 5) ohne Kommentar. Auffällige Werte mit Kategoriennutzung und Ratingzahl der betroffenen Raterin abgleichen.
- [ ] **Parameter in IRT-Metrik ausgeben** (`coef(mod, IRTpars = TRUE, simplify = TRUE)`), nicht nur in der Slope-Intercept-Form.
- [ ] **Rater-Fit:**
  - Item-Fit mit `mirt::itemfit()`. Bei fehlenden Werten sind S-X² und Infit/Outfit nicht direkt verfügbar; dann `impute` verwenden, die Zahl der Imputationen angeben und einen Seed setzen.
  - Infit/Outfit zusätzlich berichten.
- [ ] **Lokale Abhängigkeit:** Q3-Residuen (`residuals(mod, type = "Q3")`). Mit NA basiert Q3 auf paarweisen Überlappungen. Paare mit wenig Überlappung kennzeichnen (Anzahl gemeinsamer Produkte aus der Overlap-Matrix danebenstellen).
- [ ] **Absoluter Fit:** `M2(mod, type = "C2")`. Bei fehlenden Werten nur mit `impute` möglich. Wenn nicht sinnvoll durchführbar (zu dünn besetzt), das dokumentieren statt erzwingen.
- [ ] **Category Response Functions** pro Raterin plotten.

**Produktscores:**

- [ ] `fscores(mod, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE)`. Gespeichert werden θ̂ (EAP) **und** der Posterior-SD (PSD) pro Produkt.
- [ ] Hinweis in der Doku: Bei wenigen Ratings pro Produkt werden EAP-Werte zur 0 hin geschrumpft. Die Varianz der θ̂ ist kleiner als 1, das ist erwartet und kein Fehler.

**Outputs:** `results/grm/model.rds`, `results/grm/rater_parameters.csv` (a, b_k, SEs), `results/grm/rater_fit.csv`, `results/grm/q3.csv`, `results/grm/global_fit.*`, `results/grm/product_scores.csv` (siehe Abschnitt 4), Plots unter `results/grm/figures/`

---

## 4. Information und Reliabilität (GRM)

Das ist der Kern für die weitere Nutzung der Scores. Bitte besonders genau prüfen.

**Definitionen**, einheitlich im ganzen Repo:

- Rater-Information: I_j(θ) = Σ_k P′_jk(θ)² / P_jk(θ)
- Gesamtinformation bei einer gegebenen Rater-Menge R: I_R(θ) = Σ_{j ∈ R} I_j(θ). Information ist additiv, unter lokaler Unabhängigkeit.
- Bedingte Reliabilität (posteriorbasiert, θ ~ N(0, 1)): rel(θ) = I(θ) / (I(θ) + 1), SE(θ) = 1 / √(I(θ) + 1). Diese Konvention wird **durchgehend** verwendet. Falls im Code irgendwo die ML-Version 1 − 1/I(θ) steht, auf die posteriorbasierte umstellen bzw. eindeutig kennzeichnen.

### 4a. Rater-Ebene

- [ ] Information pro Raterin auf einem festen θ-Gitter, z. B. −4 bis 4 in Schritten von 0,05 (`iteminfo(extract.item(mod, j), Theta)`).
- [ ] Pro Raterin speichern: Gesamtinformation (Fläche unter der Kurve, gewichtet mit der N(0, 1)-Dichte), θ-Position des Maximums, Maximalwert.
- [ ] Anteil jeder Raterin an der Gesamtinformation, bei θ = −2, −1, 0, 1, 2 und gewichtet über N(0, 1).
- [ ] Plot: Informationskurven aller Rater in einer Grafik, plus gestapelte Anteile.

### 4b. Test- bzw. Panel-Ebene

- [ ] Informations- und Reliabilitätskurve für das **vollständige Panel** (alle Rater) auf dem Gitter. Diese Kurve ist hypothetisch: Sie gilt für ein Produkt, das von *allen* Ratern bewertet würde.
- [ ] **Modellbasierte marginale Reliabilität:** `mirt::marginal_rxx(mod)` bzw. 1 − E[1/(I(θ) + 1)] über N(0, 1). Das ist ebenfalls die Kennzahl für das vollständige Panel.

### 4c. Produktebene (wichtig wegen des dünn besetzten Designs)

Jedes Produkt wurde nur von einer Teilmenge R_n der Rater bewertet. Seine Information ist I_n(θ) = Σ_{j ∈ R_n} I_j(θ), **nicht** die Information des vollständigen Panels.

- [ ] Prüfen, dass Reliabilität und SE pro Produkt aus der **tatsächlichen Rater-Menge** des Produkts kommen. Die `fscores`-PSD berücksichtigen das automatisch. Eine Berechnung über `testinfo(mod, θ̂)` mit allen Ratern wäre dagegen **falsch**.
- [ ] Pro Produkt speichern:
  - `theta_eap`, `psd`
  - `rel_post = 1 − psd²`
  - `info_at_eap = Σ_{j ∈ R_n} I_j(θ̂_n)`
  - `rel_info = info_at_eap / (info_at_eap + 1)`
  - `n_ratings`, `raters` (IDs)
- [ ] **Konsistenzcheck:** `rel_post` und `rel_info` sollten eng zusammenhängen. `rel_info` ist eine Näherung an der Stelle θ̂, `rel_post` integriert über die Posterior. Korrelation und mittlere Differenz berichten, starke Abweichungen untersuchen.
- [ ] **Empirische marginale Reliabilität:** Var(θ̂) / (Var(θ̂) + mean(PSD²)), entspricht `mirt::empirical_rxx()`. Das ist die Kennzahl für die **tatsächlich vorliegenden** Scores und die primäre Reliabilitätsangabe.
- [ ] Verteilung von `rel_post` über alle Produkte (Histogramm). Zusätzlich `rel_post` in Abhängigkeit von `n_ratings` und von θ̂ (Streudiagramme).
- [ ] Keine Filterung oder Gewichtung von Produkten in diesem Schritt. Hier wird nur berechnet und gespeichert, die Verwendung erfolgt später.

**Outputs:** `results/grm/rater_information_grid.csv` (long: rater, theta, info), `results/grm/rater_information_summary.csv`, `results/grm/panel_information_grid.csv` (theta, info, se, rel), `results/grm/product_scores.csv` (Spalten wie oben), `results/grm/reliability_summary.csv` (marginal, empirisch, Verteilung von `rel_post`), Plots

---

## 5. Vergleich: JRT als GPCM vs. MFRM

**Ziel:** prüfen, ob raterspezifische Schwellen und raterspezifische Trennschärfen nötig sind, also ob das MFRM die Daten angemessen beschreibt.

Damit der Vergleich sauber ist, werden alle Modelle in **derselben Adjacent-Category-Familie** geschätzt, auf **denselben Daten** und mit **derselben Schätzmethode** (MML). Das GRM gehört zur kumulativen Familie und ist **nicht** Teil der genesteten Leiter.

**Modellleiter in `mirt`**, alle auf der Wide-Matrix aus Abschnitt 2:

| Modell | `itemtype` | Schwellen | Trennschärfe | Entspricht |
|---|---|---|---|---|
| M1 | `"rsm"` | gemeinsam, um die Rater-Lage verschoben | gleich | MFRM (Produkt × Raterin) |
| M2 | `"Rasch"` (PCM) | raterspezifisch | gleich | MFRM mit raterspezifischen Schwellen |
| M3 | `"gpcm"` | raterspezifisch | raterspezifisch | JRT als GPCM |

**Prüfpunkte:**

- [ ] **Identische Datenbasis:** gleiche Matrix, gleiche Zahl von Produkten und Ratings in allen Modellen (im Code assertieren).
- [ ] **Bestehendes MFRM** (`sirt::rm.facets()`) dokumentieren: Welche Parametrisierung ist gesetzt (`est.b.rater`, `est.a.item`, `est.a.rater` usw.), welche Schätzmethode und welche Identifikation? In der Doku von `sirt` nachsehen, nicht raten.
- [ ] **Äquivalenzcheck:** Entspricht das bestehende `rm.facets`-Modell M1? Log-Likelihood, Rater-Lageparameter (Korrelation) und θ̂ (Korrelation) zwischen `rm.facets` und `mirt` M1 vergleichen. Unterschiede erklären (Parametrisierung, Vorzeichen, Normierung, Integration). Für die LR-Tests wird die `mirt`-Leiter verwendet, damit die Likelihoods vergleichbar sind.
- [ ] **LR-Tests** mit `anova()`:
  - M1 vs. M2: Braucht man raterspezifische Schwellen? df = (J − 1)(K − 2).
  - M2 vs. M3: Braucht man raterspezifische Trennschärfen? df = J − 1.
  - Die df im Output gegen diese Formeln prüfen (J = Anzahl Rater, K = Anzahl Kategorien).
- [ ] **Informationskriterien:** AIC, BIC und SABIC für M1–M3 sowie zusätzlich für das GRM. Das GRM wird nur über Informationskriterien verglichen, **nicht** per LRT, weil es nicht genestet ist.
- [ ] **Praktische Relevanz:**
  - Korrelationen der θ̂ (Pearson und Spearman) zwischen M1, M2, M3 und GRM.
  - Spannweite und Verteilung der a_j in M3.
  - Geordnetheit der Schwellen in M2 und M3 (ungeordnete Schwellen markieren).
  - Rater-Infit/Outfit in M1: Welche Rater passen schlecht zu gemeinsamen Schwellen bzw. gleichen Trennschärfen?
- [ ] **Keine Informations- und Reliabilitätsanalyse für M1–M3** außer der marginalen Reliabilität zum Vergleich. Die ausführliche Analyse gibt es nur für das GRM (Abschnitt 4).

**Outputs:** `results/comparison/model_fit.csv` (logLik, npar, AIC, BIC, SABIC pro Modell), `results/comparison/lr_tests.csv`, `results/comparison/theta_correlations.csv`, `results/comparison/rater_parameters_by_model.csv`, `results/comparison/mfrm_equivalence.md`

---

## 6. Naive Kennwerte: Cronbachs α und Krippendorffs α

Diese Kennwerte dienen als Referenz für die übliche Praxis. Sie werden **nicht** für die weitere Arbeit verwendet.

**Cronbachs α** (Konsistenz des *ungewichteten* Rater-Mittelwerts)

- [ ] Berechnung auf der Wide-Matrix. Bei einem dünn besetzten Design ist listwise Deletion meist unmöglich. Dokumentieren, wie mit NA umgegangen wird (z. B. `psych::alpha()` mit paarweisen Kovarianzen) und auf wie vielen Produkten bzw. Paaren das basiert.
- [ ] Falls es eine voll gekreuzte Teilmenge gibt (alle Rater bewerten dieselben Produkte), α zusätzlich dort berechnen und beide Werte berichten.
- [ ] Interpretation im Output vermerken: α bezieht sich auf den Mittelwert über die Rater, setzt τ-Äquivalenz voraus und ist nicht direkt mit der IRT-Reliabilität der θ̂ vergleichbar.

**Krippendorffs α** (Konsens bzw. Übereinstimmung, ordinal)

- [ ] Ordinales Skalenniveau (z. B. `irr::kripp.alpha(t(wide_matrix), method = "ordinal")`). Auf die Orientierung der Matrix achten: Rater × Einheiten.
- [ ] Fehlende Werte werden vom Verfahren nativ behandelt. Prüfen, dass `NA` korrekt übergeben wird.
- [ ] Bootstrap-Konfidenzintervall durch Resampling über **Produkte** (z. B. 1000 Replikationen, Seed setzen).

**Outputs:** `results/naive/cronbach_alpha.csv`, `results/naive/krippendorff_alpha.csv`

---

## 7. Zusammenfassung

Erzeuge eine Übersichtstabelle `results/summary/reliability_overview.csv` und einen kurzen Bericht `results/summary/REPORT.md` mit:

| Kennwert | Bezieht sich auf | Wert |
|---|---|---|
| Krippendorffs α (ordinal) | Konsens einzelner Ratings | |
| Cronbachs α | Konsistenz des ungewichteten Mittelwerts | |
| GRM: empirische marginale Reliabilität | tatsächliche θ̂ (primär) | |
| GRM: modellbasierte marginale Reliabilität | hypothetisches vollständiges Panel | |
| GRM: Median und IQR von `rel_post` | Präzision pro Produkt | |
| M1 / M2 / M3: marginale Reliabilität | Vergleich | |

Außerdem soll der Bericht enthalten:

- Ergebnis der Modellleiter (LR-Tests und Informationskriterien) in zwei, drei Sätzen.
- Korrelation der θ̂ zwischen den Modellen.
- Rater mit auffälligem Fit, auffälliger Kategoriennutzung oder sehr geringem Informationsbeitrag.
- Liste aller Abweichungen von der Spezifikation, die korrigiert wurden (Verweis auf `AUDIT.md`).

---

## Abschluss-Checkliste

- [ ] `AUDIT.md` ist vollständig, und jede Analyse hat einen Status.
- [ ] Die Lösch-Liste wurde von mir freigegeben, und nur diese Analysen wurden entfernt.
- [ ] Alle Notebooks und Skripte laufen von oben nach unten ohne Fehler auf frischem Kernel bzw. in frischer Session.
- [ ] Alle Outputs aus Abschnitt 2–7 existieren und werden ausschließlich per Code erzeugt.
- [ ] Die Reliabilitätskonvention I/(I + 1) wird überall einheitlich verwendet.
- [ ] Reliabilitäten auf Produktebene basieren auf den tatsächlichen Ratern des Produkts.
- [ ] Alle Modelle verwenden dieselbe Datenbasis (assertiert).
- [ ] Seeds und Paketversionen sind dokumentiert.
- [ ] Die Commits auf dem Branch `audit/jrt-spec` sind thematisch getrennt. Kein Merge ohne meine Freigabe.
