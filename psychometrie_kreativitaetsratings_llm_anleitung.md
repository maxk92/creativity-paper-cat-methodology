# Implementierungsauftrag: Psychometrische Analyse unvollständig gekreuzter Kreativitätsratings

## 0. Rolle, Ziel und Arbeitsweise

Du bist eine lokale LLM-Coding-Instanz mit Expertise in Psychometrie, Generalisierbarkeitstheorie, Mixed-Effects-Modellen, ordinalen Modellen, Item-Response-Theory und reproduzierbarer Datenanalyse.

Erstelle **zwei inhaltlich parallele, vollständig ausführbare Analyse-Notebooks**:

1. `01_creativity_ratings_python.ipynb`
2. `01_creativity_ratings_R.qmd` oder alternativ `01_creativity_ratings_R.ipynb`

Erstelle zusätzlich:

- `README.md`
- `requirements.txt` oder `environment.yml`
- `renv.lock` beziehungsweise ein R-Skript zur reproduzierbaren Paketinstallation
- `data/raw/ratings_long_raw.csv`
- `data/processed/ratings_long_clean.csv`
- `data/processed/action_scores.csv`
- `data/processed/rater_diagnostics.csv`
- `results/tables/`
- `results/figures/`
- `results/models/`
- `results/logs/`
- `reports/analysis_report.html`

Die Notebooks sollen nicht nur Code enthalten, sondern auch:

- theoretische Erläuterungen in Markdown-Zellen,
- mathematische Modellgleichungen,
- Begründungen der Methodenwahl,
- Annahmen und Grenzen jeder Methode,
- Interpretationshilfen,
- diagnostische Prüfungen,
- Sensitivitätsanalysen,
- Literaturhinweise,
- automatisch generierte Tabellen und Abbildungen.

Verwende keine simulierten oder erfundenen Ergebnisse als reale Befunde. Falls für die Entwicklung Beispieldaten notwendig sind, kennzeichne sie eindeutig als simuliert und ersetze sie im finalen Lauf durch die echten Ratings.

---

# 1. Forschungsdesign und zentrale Begriffe

## 1.1 Datensituation

Es liegen Kreativitätsratings für ungefähr 4.000 Fußballaktionen vor. Die Aktionen wurden auf einer unipolaren siebenstufigen Skala bewertet:

- 1 = nicht kreativ
- 7 = sehr kreativ

Die Anzahl der Ratings pro Aktion ist ungleich:

- ungefähr 600 Aktionen mit einem Rating,
- ungefähr 2.000 Aktionen mit zwei Ratings,
- verbleibende Aktionen mit drei bis sieben Ratings.

Nicht alle Rater bewerteten dieselben Aktionen. Das Design ist daher:

- unbalanciert,
- unvollständig,
- teilweise gekreuzt,
- mit variabler Zahl von Ratern pro Aktion.

Die Daten liegen bereits im Long-Format vor. Erwartete Mindestvariablen:

| Variable | Bedeutung |
|---|---|
| `action_id` | eindeutige Kennung der Fußballaktion |
| `rater_id` | eindeutige Kennung des Raters |
| `rating` | Kreativitätsurteil von 1 bis 7 |

Optionale Variablen können beispielsweise sein:

- `player_id`
- `match_id`
- `team_id`
- `action_type`
- `timestamp`
- `session_id`
- `rating_order`
- Ratermerkmale wie Erfahrung oder Expertise.

## 1.2 Zu unterscheidende Zielgrößen

Die Analyse muss klar zwischen folgenden Konzepten unterscheiden.

### Absolute Übereinstimmung

Absolute Übereinstimmung verlangt, dass zwei Rater derselben Aktion ungefähr denselben Zahlenwert geben. Ein systematisch strengerer oder großzügigerer Rater reduziert absolute Übereinstimmung.

### Relative Konsistenz

Relative Konsistenz verlangt primär, dass Rater Aktionen ähnlich ordnen. Ein Rater darf beispielsweise systematisch zwei Punkte höher urteilen, solange die Rangordnung der Aktionen ähnlich bleibt.

### Reliabilität eines einzelnen Ratings

Diese Größe beantwortet:

> Wie stark reflektiert ein einzelnes beobachtetes Rating stabile Unterschiede zwischen Aktionen?

### Reliabilität eines aggregierten Aktionsscores

Diese Größe beantwortet:

> Wie zuverlässig ist ein Mittelwert oder modellbasierter Score, wenn eine Aktion durch \(k\) Rater bewertet wird?

### Rater-Severity/Leniency

Dies bezeichnet die systematische Tendenz eines Raters, niedrigere oder höhere Werte als andere Rater zu vergeben.

### Rater-Diskrimination beziehungsweise Skalenstreuung

Dies bezeichnet, wie stark ein Rater zwischen Aktionen differenziert. Manche Rater verwenden fast nur die Skalenmitte; andere nutzen die ganze Skala.

---

# 2. Projektstruktur und Reproduzierbarkeit

Lege folgende Struktur an:

```text
project/
├── README.md
├── requirements.txt
├── renv.lock
├── data/
│   ├── raw/
│   │   └── ratings_long_raw.csv
│   └── processed/
│       ├── ratings_long_clean.csv
│       ├── action_scores.csv
│       └── rater_diagnostics.csv
├── notebooks/
│   ├── 01_creativity_ratings_python.ipynb
│   └── 01_creativity_ratings_R.qmd
├── results/
│   ├── figures/
│   ├── tables/
│   ├── models/
│   └── logs/
└── reports/
    └── analysis_report.html
```

Setze in beiden Sprachen einen festen Zufallsseed. Speichere:

- Python-Paketversionen,
- R-Session-Informationen,
- Betriebssysteminformationen,
- Datum und Uhrzeit der Analyse,
- Git-Commit-Hash, falls das Projekt unter Versionskontrolle steht.

### Python

Empfohlene Pakete:

```text
pandas
numpy
scipy
statsmodels
patsy
scikit-learn
networkx
matplotlib
plotnine
pingouin
krippendorff
pyarrow
openpyxl
cmdstanpy
arviz
bambi
pymc
python-dotenv
jupyter
nbformat
```

Hinweis: Für gekreuzte Random Effects kann `statsmodels.MixedLM` über Varianzkomponenten verwendet werden. Für ordinale hierarchische Modelle ist ein Bayesianischer Workflow mit `bambi`/`pymc` oder direkt mit Stan häufig flexibler. Implementiere keine scheinbar fertige Funktion, wenn das verwendete Paket die gewünschte Modellstruktur tatsächlich nicht unterstützt.

### R

Empfohlene Pakete:

```r
tidyverse
data.table
janitor
skimr
naniar
igraph
lme4
lmerTest
performance
insight
broom.mixed
sjPlot
ggeffects
krippendorffsalpha
irr
psych
brms
posterior
bayesplot
loo
tidybayes
jrt
mirt
TAM
ordinal
glmmTMB
arrow
here
renv
targets
quarto
```

Prüfe vor dem Einsatz jeweils die aktuelle Dokumentation und Paketversion.

---

# 3. Datenimport aus Google Sheets

## 3.1 Python-Platzhalter

Füge eine klar markierte Codezelle ein:

```python
# ============================================================
# PLACEHOLDER: Google-Sheet-Import
# ============================================================
# Hier den bereits vorhandenen Python-Code des Forschers einfügen.
# Erwartetes Ergebnis:
# ratings_raw = pandas.DataFrame mit mindestens:
# action_id, rater_id, rating
#
# Beispiel:
# ratings_raw = load_ratings_from_google_sheet(...)
# ============================================================

raise NotImplementedError(
    "Google-Sheet-Importcode hier einsetzen und anschließend "
    "die NotImplementedError-Zeile entfernen."
)
```

Direkt danach:

```python
from pathlib import Path

RAW_PATH = Path("data/raw/ratings_long_raw.csv")
RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

ratings_raw.to_csv(RAW_PATH, index=False)
```

Speichere die unbearbeiteten Rohdaten unmittelbar nach dem Download. Verändere die Rohdatei danach nicht mehr.

## 3.2 R-Platzhalter

Da der eigentliche Import in Python vorliegt, soll das R-Notebook standardmäßig die gespeicherte Roh-CSV einlesen:

```r
library(readr)
library(here)

ratings_raw <- read_csv(
  here("data", "raw", "ratings_long_raw.csv"),
  show_col_types = FALSE
)
```

Optional kann ein eigener R-Platzhalter für `googlesheets4` ergänzt werden, er ist aber nicht erforderlich.

---

# 4. Datenvalidierung und Cleaning

Implementiere alle Prüfungen in beiden Sprachen.

## 4.1 Schema prüfen

Prüfe:

- Existenz von `action_id`, `rater_id`, `rating`,
- keine fehlenden IDs,
- `rating` numerisch oder sicher in numerisch konvertierbar,
- Ratings ausschließlich in \(\{1,2,3,4,5,6,7\}\),
- eindeutige Kombinationen aus `action_id` und `rater_id`.

Falls dieselbe Rater-Aktions-Kombination mehrfach vorkommt:

1. nicht automatisch mitteln,
2. Duplikate tabellarisch ausgeben,
3. mögliche Ursachen prüfen, etwa Wiederholungsrating, versehentliche Dopplung oder mehrere Dimensionen,
4. nur anhand einer explizit dokumentierten Regel auflösen.

## 4.2 Typkonvertierung

- IDs als kategoriale/string Variablen behandeln.
- Rating zusätzlich in zwei Formen anlegen:
  - `rating_numeric`: numerisch 1–7,
  - `rating_ordinal`: geordnete Kategorie 1–7.

## 4.3 Missingness

Erzeuge:

- Anzahl fehlender Werte je Variable,
- Missingness-Muster,
- Anzahl Ratings je Aktion,
- Anzahl Ratings je Rater,
- Verteilung der Anzahl Ratings pro Aktion,
- Verteilung der Anzahl bewerteter Aktionen pro Rater.

Aktionen mit nur einem Rating:

- bleiben für die modellbasierte Score-Schätzung grundsätzlich erhalten,
- tragen jedoch nicht direkt zu paarweisen Agreement-Informationen innerhalb der Aktion bei,
- sollen in Agreement-Analysen separat gekennzeichnet werden.

## 4.4 Plausibilitäts- und Verteilungschecks

Erzeuge Tabellen und Grafiken zu:

- Gesamthäufigkeiten der sieben Kategorien,
- Mittelwert, Median, SD und IQR je Rater,
- Floor- und Ceiling-Anteilen je Rater,
- Anzahl verwendeter Kategorien je Rater,
- Anteil mittlerer Kategorien 3–5,
- Anteil extremer Kategorien 1 und 7,
- Ratingverteilung nach Anzahl Ratings pro Aktion,
- mögliche zeitliche Drift, falls `rating_order` oder Zeitstempel vorhanden sind.

## 4.5 Saubere Datei speichern

```text
data/processed/ratings_long_clean.csv
```

Dokumentiere jede Veränderung gegenüber den Rohdaten in einer Cleaning-Log-Tabelle.

---

# 5. Konnektivität und Identifizierbarkeit des Rater–Aktions-Designs

Dieser Schritt ist zwingend und muss vor allen Rater-korrigierenden Modellen erfolgen.

## 5.1 Bipartiter Graph

Konstruiere einen bipartiten Graphen:

- Knotenmenge A: Aktionen,
- Knotenmenge R: Rater,
- Kante: Rater \(j\) hat Aktion \(i\) bewertet.

Berechne:

- Zahl zusammenhängender Komponenten,
- Größe jeder Komponente,
- Anzahl Aktionen und Rater pro Komponente,
- Gradverteilung für Aktionen und Rater,
- isolierte oder schwach verbundene Rater,
- Raterpaare mit gemeinsamer Bewertungsmenge,
- Zahl gemeinsamer Aktionen pro Raterpaar.

## 5.2 Interpretation

Schreibe im Notebook:

> Rater-Severity-Parameter sind nur relativ zu anderen Ratern identifizierbar, wenn das Ratingdesign ausreichend verbunden ist. Befinden sich Ratergruppen in getrennten Komponenten ohne gemeinsame Aktionen oder Brückenrater, können ihre Niveaus nicht empirisch auf dieselbe Skala gesetzt werden.

Falls mehrere Komponenten existieren:

- analysiere die größte verbundene Komponente separat,
- liefere komponentenspezifische Ergebnisse,
- berechne keine scheinbar global vergleichbaren Rater-Severity-Werte ohne zusätzliche Identifikationsannahmen,
- kennzeichne Aktionsscores aus getrennten Komponenten.

## 5.3 Visualisierungen

Bei großen Daten nicht den vollständigen Graphen unlesbar plotten. Stattdessen:

- Komponentenübersicht,
- Heatmap der Anzahl gemeinsam bewerteter Aktionen pro Raterpaar,
- Rater-Projektionsgraph mit Kantengewicht = gemeinsame Aktionen,
- Histogramm der Überlappungszahlen.

---

# 6. Deskriptives paarweises Agreement

Diese Analysen sind ergänzend und nicht die alleinige Hauptanalyse.

## 6.1 Paarweise Raterstatistiken

Für jedes Raterpaar mit hinreichender Überlappung, beispielsweise mindestens 10 oder 20 gemeinsam bewerteten Aktionen, berechne:

- Zahl gemeinsamer Aktionen,
- Pearson-Korrelation,
- Spearman-Korrelation,
- Kendall-\(\tau\),
- mittlere Differenz \( \bar y_j - \bar y_k \),
- SD der Differenzen,
- mittlere absolute Differenz,
- quadratisch gewichtetes Cohen-\(\kappa\),
- optional paarweise ICC nur bei ausreichender Überlappung.

Korrelationen messen Konsistenz beziehungsweise Rangähnlichkeit, nicht absolute Übereinstimmung.

## 6.2 Bland–Altman-artige Darstellung

Für ausgewählte Raterpaare mit hoher Überlappung:

- x-Achse: Mittelwert der beiden Ratings,
- y-Achse: Differenz der beiden Ratings,
- mittlere Differenz,
- Limits of Agreement.

Beachte, dass die Likert-Skala diskret und begrenzt ist. Die Darstellung ist diagnostisch, nicht die alleinige Inferenzgrundlage.

## 6.3 Raterpaar-Heatmaps

Erzeuge getrennte Heatmaps für:

- gemeinsame Aktionen,
- Spearman-Korrelation,
- mittlere Differenz,
- gewichtetes \(\kappa\).

Maskiere Raterpaare mit zu geringer Überlappung.

---

# 7. Krippendorffs Alpha

## 7.1 Zweck

Berechne Krippendorffs Alpha, weil es:

- unterschiedliche Raterzahlen pro Einheit,
- fehlende Ratings,
- mehrere Rater,
- verschiedene Skalenniveaus

grundsätzlich unterstützt.

Berechne mindestens:

1. ordinales Alpha,
2. intervallskaliertes Alpha als Sensitivitätsanalyse.

Das ordinale Alpha ist die primäre Variante, sofern die Abstände zwischen den sieben Kategorien nicht als exakt gleich angenommen werden sollen.

## 7.2 Datenform

Für viele Implementierungen muss Long- in Wide-Format transformiert werden:

- Zeilen oder Spalten = Rater,
- Gegenachse = Aktionen,
- fehlende Kombinationen = `NA` beziehungsweise `np.nan`.

Prüfe die von der jeweiligen Paketfunktion erwartete Orientierung ausdrücklich.

## 7.3 Unsicherheit

Berechne Konfidenzintervalle vorzugsweise durch Resampling auf Ebene der Aktionen, nicht durch naives Resampling einzelner Ratings.

Wichtig:

- Eine Aktion ist die primäre Beobachtungseinheit.
- Alle Ratings einer gezogenen Aktion bleiben beim Cluster-Bootstrap zusammen.
- Dokumentiere die Zahl der Bootstrap-Replikationen, etwa 2.000.
- Setze einen Seed.

## 7.4 Subgruppen- und Sensitivitätsanalysen

Berechne Alpha zusätzlich:

- nur für Aktionen mit mindestens zwei Ratings,
- nur für Aktionen mit mindestens drei Ratings,
- innerhalb der größten verbundenen Komponente,
- optional nach Aktionstyp oder Raterexpertise.

Warne davor, Alpha-Werte verschiedener Teilmengen unkritisch zu vergleichen, weil sich die Heterogenität der Aktionen verändern kann.

## 7.5 Python

Nutze ein geprüftes Paket oder implementiere die Distanzfunktion transparent. Erstelle Unit-Tests mit kleinen bekannten Beispielen.

## 7.6 R

Bevorzugt:

```r
library(krippendorffsalpha)
```

Nutze die ordinale und intervallskalierte Distanz entsprechend der aktuellen Paketdokumentation.

---

# 8. Lineares gekreuztes Mixed-Effects-Modell

## 8.1 Basismodell

Behandle die siebenstufige Skala zunächst als näherungsweise intervallskaliert:

\[
y_{ij} = \mu + u_i + v_j + \varepsilon_{ij},
\]

mit

\[
u_i \sim \mathcal{N}(0,\sigma^2_{\text{action}}),
\]

\[
v_j \sim \mathcal{N}(0,\sigma^2_{\text{rater}}),
\]

\[
\varepsilon_{ij} \sim \mathcal{N}(0,\sigma^2_e).
\]

Dabei ist:

- \(u_i\): latente Abweichung der Kreativität von Aktion \(i\),
- \(v_j\): Severity/Leniency von Rater \(j\),
- \(\varepsilon_{ij}\): nicht erklärte Abweichung einschließlich aktionsspezifischer Raterabweichungen.

Das Design ist gekreuzt, nicht einfach hierarchisch: Ein Rater bewertet mehrere Aktionen, und eine Aktion kann von mehreren Ratern bewertet werden.

## 8.2 R-Implementierung

```r
library(lme4)

model_lmm <- lmer(
  rating_numeric ~ 1 + (1 | action_id) + (1 | rater_id),
  data = ratings_clean,
  REML = TRUE
)
```

Extrahiere:

- fixe Interzeptschätzung,
- Varianzkomponenten,
- BLUPs/conditional modes für Aktionen,
- BLUPs für Rater,
- Standardfehler oder konditionale Varianzen, sofern verfügbar,
- Konvergenzdiagnostik,
- Singularitätsprüfung.

## 8.3 Python-Implementierung

Nutze `statsmodels.MixedLM` mit einer einzigen künstlichen Gruppe und Varianzkomponenten für beide gekreuzten Faktoren:

```python
import statsmodels.formula.api as smf

df = ratings_clean.copy()
df["all_obs"] = 1

model_lmm = smf.mixedlm(
    "rating_numeric ~ 1",
    data=df,
    groups=df["all_obs"],
    vc_formula={
        "action": "0 + C(action_id)",
        "rater": "0 + C(rater_id)",
    },
    re_formula="0",
)

result_lmm = model_lmm.fit(reml=True, method="lbfgs")
```

Prüfe anhand der aktuellen `statsmodels`-Dokumentation, wie Varianzkomponenten und Random-Effect-Schätzungen zuverlässig extrahiert werden. Falls die BLUP-Extraktion für einzelne Varianzkomponenten nicht robust zugänglich ist, verwende für Score-Schätzungen ergänzend ein Bayesianisches Modell in PyMC/Bambi/Stan.

## 8.4 Absolute und relative Reliabilitätskoeffizienten

Für ein einzelnes Rating:

### Absolute Übereinstimmung

\[
\rho_{\text{abs},1}
=
\frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_{\text{rater}}+\sigma^2_e}.
\]

### Relative Konsistenz

\[
\rho_{\text{rel},1}
=
\frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+\sigma^2_e}.
\]

Die Rater-Haupteffektvarianz wird bei relativen Entscheidungen nicht als Fehler behandelt, weil systematische Unterschiede im Raterniveau die Rangordnung nicht notwendigerweise verändern.

Für einen Mittelwert aus \(k\) unabhängig gezogenen Ratern:

### Absolute Reliabilität des Mittelwerts

\[
\rho_{\text{abs},k}
=
\frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+
\sigma^2_{\text{rater}}/k+
\sigma^2_e/k}.
\]

### Relative Reliabilität des Mittelwerts

\[
\rho_{\text{rel},k}
=
\frac{\sigma^2_{\text{action}}}
{\sigma^2_{\text{action}}+
\sigma^2_e/k}.
\]

Berechne diese Werte für \(k=1,\ldots,7\) und visualisiere eine D-Study-Kurve.

## 8.5 Wichtige Einschränkung

Bei dem einfachen Modell ist die Aktion×Rater-Interaktion nicht separat vom Residuum identifizierbar, weil jede konkrete Rater-Aktions-Zelle typischerweise nur ein Rating enthält. Das Residuum umfasst daher:

- Aktion×Rater-Interaktion,
- momentane Bewertungsfehler,
- weitere nicht modellierte Einflüsse.

Beschreibe dies korrekt als Generalizability-/Varianzkomponenten-Approximation und nicht als vollständige Zerlegung aller G-Theory-Facetten.

## 8.6 Unsicherheit der Koeffizienten

Erzeuge Konfidenz- oder Credible-Intervalle für die Varianzkomponenten und abgeleiteten Reliabilitätskoeffizienten:

- parametrischer Bootstrap für `lme4`, oder
- Cluster-Bootstrap über Aktionen, oder
- posteriorbasierte Intervalle aus einem Bayesianischen Modell.

Die Unsicherheit darf nicht nur über eine Delta-Methode aus asymptotischen Standardfehlern approximiert werden, wenn diese für Varianzkomponenten instabil ist.

---

# 9. Modellbasierte Integration der Ratings

Erzeuge mindestens vier Aktionsscores.

## 9.1 Rohmittelwert

\[
\bar y_i = \frac{1}{n_i}\sum_j y_{ij}.
\]

Speichere:

- Mittelwert,
- Median,
- SD,
- Anzahl Ratings,
- Standardfehler des Mittelwerts, falls \(n_i>1\).

Vorteil: transparent.

Nachteil: nicht für unterschiedliche Raterstrenge korrigiert; extreme Werte bei wenigen Ratings sind instabil.

## 9.2 Rater-zentrierter Mittelwert

Berechne:

\[
y^{c}_{ij}=y_{ij}-\bar y_j+\bar y.
\]

Dann:

\[
\bar y^{c}_{i}=\frac{1}{n_i}\sum_j y^{c}_{ij}.
\]

Alternativ robust:

- Ratermedian statt Ratermittel,
- globale Mediananpassung.

Wichtige Einschränkung:

> Eine einfache Raterzentrierung ist nur dann sinnvoll interpretierbar, wenn Rater hinreichend vergleichbare und verbundene Aktionsmengen bewerten. Bei stark selektiver Zuweisung kann ein niedriger Ratermittelwert sowohl Strenge als auch eine schwierigere beziehungsweise weniger kreative Aktionsstichprobe reflektieren.

Deshalb Raterzentrierung nur als deskriptive Sensitivitätsanalyse behandeln.

## 9.3 LMM-Empirical-Bayes-/BLUP-Score

Definiere den Aktionsscore als:

\[
\hat \theta_i = \hat \mu + \hat u_i.
\]

Diese Scores werden zur Gesamtmittelwertschätzung hin geschrumpft. Die Schrumpfung ist bei Aktionen mit wenigen Ratings stärker.

Speichere:

- Punktschätzung,
- Standardfehler oder Unsicherheitsintervall,
- Zahl Ratings,
- Raterzusammensetzung,
- Komponentenzugehörigkeit.

## 9.4 Ordinaler posteriorer Aktionsscore

Aus dem ordinalen hierarchischen Modell, siehe Abschnitt 11:

- posteriorer Mittelwert oder Median von \(\theta_i\),
- 95-%-Credible-Interval,
- posteriorer Rang,
- Unsicherheit des Rangs,
- erwarteter Ratingwert auf der ursprünglichen 1–7-Skala.

Der latente Score und der erwartete beobachtete Skalenwert sind getrennt zu speichern.

---

# 10. Rater-Effekte im linearen Modell

## 10.1 Severity/Leniency

Extrahiere:

\[
\hat v_j.
\]

Positiv bedeutet bei der verwendeten Parametrisierung tendenziell großzügiger; negativ tendenziell strenger. Prüfe das Vorzeichen anhand der Modellkodierung.

Stelle dar:

- Caterpillar-Plot mit Unsicherheitsintervallen,
- Rangfolge der Rater,
- Zusammenhang mit Ratermittelwert,
- Anzahl Ratings je Rater,
- mittlere Kreativität der zugewiesenen Aktionen.

## 10.2 Skalenbreite und Diskrimination

Ein zufälliger Interzept allein erfasst keine unterschiedliche Skalenstreuung. Untersuche daher deskriptiv:

- SD je Rater,
- IQR je Rater,
- Zahl verwendeter Kategorien,
- Entropie der Kategorienutzung,
- Anteil mittlerer und extremer Kategorien.

Für eine modellbasierte Untersuchung verwende das ordinale JRT-/Facettenmodell mit rater-spezifischer Diskrimination oder rater-spezifischen Schwellen.

## 10.3 Raterdrift

Falls Reihenfolge oder Zeit verfügbar ist, modelliere beispielsweise:

\[
y_{ij} =
\mu + u_i + v_j +
\beta t_{ij} +
b_j t_{ij} +
\varepsilon_{ij}.
\]

Dabei ist \(b_j\) ein rater-spezifischer Zeittrend. Zentriere Zeit innerhalb des Raters.

Prüfe:

- lineare Drift,
- nichtlineare Drift mit Splines,
- Sitzungseffekte,
- Ermüdung,
- Veränderungen der Kategorienutzung.

---

# 11. Ordinales hierarchisches Facettenmodell

Dies ist die zentrale Sensitivitäts- beziehungsweise bevorzugte ordinale Modellierung.

## 11.1 Kumulatives Logit-Modell

Für die sieben Kategorien mit Schwellen \(\tau_1,\ldots,\tau_6\):

\[
\Pr(Y_{ij} \le k)
=
\operatorname{logit}^{-1}
\left(
\tau_k - \theta_i - \lambda_j
\right).
\]

Äquivalent kann Rater-Severity mit umgekehrtem Vorzeichen parametrisiert werden. Dokumentiere die gewählte Konvention.

- \(\theta_i\): Kreativität der Aktion,
- \(\lambda_j\): Leniency/Severity des Raters,
- \(\tau_k\): globale Kategorienschwellen.

## 11.2 R mit `brms`

Grundmodell:

```r
library(brms)

ratings_clean <- ratings_clean |>
  mutate(rating_ordinal = ordered(rating_numeric, levels = 1:7))

model_ord <- brm(
  rating_ordinal ~ 1 + (1 | action_id) + (1 | rater_id),
  data = ratings_clean,
  family = cumulative(link = "logit"),
  prior = c(
    prior(normal(0, 1.5), class = "Intercept"),
    prior(exponential(1), class = "sd")
  ),
  chains = 4,
  iter = 4000,
  warmup = 2000,
  cores = 4,
  seed = 20260713,
  control = list(adapt_delta = 0.95)
)
```

Die konkrete Prior-Spezifikation für ordinale Intercepts muss anhand der aktuellen `brms`-Syntax geprüft werden. Verwende Prior-Predictive-Checks, bevor das finale Modell geschätzt wird.

## 11.3 Python mit Bambi/PyMC oder Stan

Bevorzugte Strategie:

- Prüfe, ob die installierte Bambi-Version ordinale kumulative Modelle mit beiden gekreuzten Random Intercepts zuverlässig unterstützt.
- Falls nicht, implementiere das Modell direkt in PyMC oder CmdStanPy.

Pseudocode für ein PyMC-Modell:

```python
with pm.Model(coords=coords) as ordinal_model:
    action_sd = pm.Exponential("action_sd", 1.0)
    rater_sd = pm.Exponential("rater_sd", 1.0)

    action_raw = pm.Normal("action_raw", 0, 1, dims="action")
    rater_raw = pm.Normal("rater_raw", 0, 1, dims="rater")

    action_eff = pm.Deterministic(
        "action_eff", action_raw * action_sd, dims="action"
    )
    rater_eff = pm.Deterministic(
        "rater_eff", rater_raw * rater_sd, dims="rater"
    )

    cutpoints = pm.Normal(
        "cutpoints",
        mu=np.linspace(-2.5, 2.5, 6),
        sigma=1.0,
        transform=pm.distributions.transforms.ordered,
        shape=6,
    )

    eta = action_eff[action_idx] + rater_eff[rater_idx]

    y = pm.OrderedLogistic(
        "y",
        eta=eta,
        cutpoints=cutpoints,
        observed=rating_zero_based,
    )
```

Achte darauf, dass PyMC-Kategorien meist nullbasiert kodiert werden müssen. Prüfe dies anhand der installierten Version.

## 11.4 Diagnostik

Für Bayesianische Modelle zwingend:

- \(\hat R < 1.01\),
- ausreichend große Bulk- und Tail-ESS,
- keine beziehungsweise sehr wenige Divergenzen,
- Energy/BFMI prüfen,
- Traceplots,
- Rankplots,
- Posterior-Predictive-Checks,
- Kategorienhäufigkeiten replizierter Daten,
- Verteilung der Ratings pro Rater,
- Verteilung der Aktionsmittelwerte,
- extreme Rater und Aktionen.

## 11.5 Proportional-Odds-Annahme

Das kumulative Logit-Modell nimmt zunächst gemeinsame Schwellen beziehungsweise proportionale Effekte an. Prüfe Modellvarianten:

1. globale Schwellen,
2. rater-spezifische Schwellen,
3. rater-spezifische Diskrimination,
4. adjacent-category-Modell als Sensitivität.

Vergleiche Modelle mit:

- LOO-CV,
- Pareto-\(k\)-Diagnostik,
- Posterior-Predictive-Checks,
- wissenschaftlicher Interpretierbarkeit,
- Parameteridentifizierbarkeit.

Vermeide unnötig komplexe Modelle, wenn die Datenkonnektivität oder Zahl der Ratings je Rater nicht ausreicht.

---

# 12. Many-Facet-Rasch- und Judge-Response-Theory-Analyse

## 12.1 Konzeption

Judge Response Theory überträgt polytome IRT-Modelle auf Urteilsdaten. Dabei werden Rater als Messinstrumente beziehungsweise „Items“ betrachtet und Aktionen als zu messende Objekte.

Eine mögliche Graded-Response-Form ist:

\[
P(Y_{ij}\ge k \mid \theta_i)
=
\operatorname{logit}^{-1}
\left[
a_j(\theta_i-b_{jk})
\right],
\]

mit:

- \(\theta_i\): Kreativität von Aktion \(i\),
- \(a_j\): Diskrimination von Rater \(j\),
- \(b_{jk}\): rater-spezifische Schwelle für Kategorie \(k\).

Dieses Modell kann erfassen:

- unterschiedliche Strenge,
- unterschiedliche Diskrimination,
- unterschiedliche Kategorienutzung,
- Informationsbeitrag einzelner Rater.

## 12.2 Wichtiger Unterschied zum einfachen Facettenmodell

Ein Many-Facet-Rasch-Modell setzt häufig eine gemeinsame Diskrimination von 1 voraus und modelliert additive Facetten wie Aktion, Rater und Schwellen.

JRT kann flexibler sein und rater-spezifische IRT-Parameter zulassen. Diese Flexibilität erfordert jedoch:

- ausreichend viele Ratings pro Rater,
- gute Konnektivität,
- genügend Nutzung mehrerer Kategorien,
- sorgfältige Fitdiagnostik.

## 12.3 R-Implementierung mit `jrt`

Nutze das aktuelle CRAN-Paket `jrt`.

Vorgehen:

1. Erzeuge eine Wide-Matrix:
   - Zeilen = Aktionen,
   - Spalten = Rater,
   - Zellen = Rating,
   - fehlende Ratings = `NA`.

2. Prüfe, welche Mindestanzahl beobachteter Ratings je Rater für stabile Schätzungen sinnvoll ist.

3. Nutze die aktuelle Paketvignette und implementiere:
   - automatische Modellvergleiche,
   - Judge Category Curves,
   - Judge Information Functions,
   - Judge Reliability Functions,
   - latente Aktionsscores,
   - Standardfehler der Scores,
   - Fit- und Residualdiagnostik.

4. Speichere die exakte Funktionssignatur aus der installierten Paketversion im Notebook. Erfinde keine veraltete API.

5. Prüfe insbesondere, wie das Paket mit stark unvollständigen Matrizen und Aktionen mit nur einem Rating umgeht.

6. Führe JRT gegebenenfalls auf einer methodisch begründeten Teilmenge aus:
   - größte verbundene Komponente,
   - Rater mit Mindestzahl an Bewertungen,
   - Aktionen mit mindestens zwei Ratings,
   - anschließend externe Score-Schätzung für übrige Aktionen nur, wenn das Modell dies valide unterstützt.

## 12.4 Python-Strategie

Für Python gibt es möglicherweise kein gleichwertig etabliertes JRT-Paket. Deshalb:

- implementiere das äquivalente Modell in PyMC oder Stan,
- oder rufe das R-Paket reproduzierbar über einen separaten R-Schritt auf,
- behaupte nicht, dass ein generisches Python-IRT-Paket automatisch das unvollständig gekreuzte JRT-Design korrekt abbildet.

Eine flexible Bayesianische JRT-Implementierung kann enthalten:

```text
theta_action[i]          latente Kreativität
severity_rater[j]        Raterniveau
log_discrimination[j]    rater-spezifische Diskrimination
threshold_base[k]        globale geordnete Schwellen
threshold_shift[j, k]    optional rater-spezifische Schwellenabweichungen
```

Beginne mit einem einfacheren Modell und erhöhe die Komplexität schrittweise.

## 12.5 Identifikation

Setze explizite Identifikationsbedingungen, beispielsweise:

- Mittelwert der Aktionsparameter = 0,
- SD der Aktionsparameter = 1, oder alternative Skalierung,
- Summe der Rater-Severity-Parameter = 0,
- geordnete Schwellen,
- positive Diskriminationsparameter.

Dokumentiere die Identifikationskonvention.

---

# 13. Rater-Fit und Rater-Effekt-Diagnostik

Erzeuge pro Rater:

- Anzahl Ratings,
- Zahl unterschiedlicher bewerteter Aktionen,
- Zahl gemeinsam bewerteter Aktionen mit anderen Ratern,
- Rohmittelwert und SD,
- Kategorienutzung,
- Severity-Schätzung,
- Diskriminationsschätzung, falls modelliert,
- Infit/Outfit, falls im Rasch-Modell verfügbar,
- Posterior-Predictive-Discrepancy,
- mittlere absolute modellbasierte Residuen,
- Korrelation mit Konsens- oder leave-one-rater-out Score,
- mögliche Driftparameter,
- Unsicherheitsintervalle.

## 13.1 Leave-one-rater-out-Konsistenz

Für jede Beobachtung beziehungsweise jeden Rater:

1. Schätze den Aktionskonsens ohne den betreffenden Rater.
2. Vergleiche dessen Ratings mit diesem unabhängigen Konsens.
3. Berechne:
   - Spearman-Korrelation,
   - mittlere Differenz,
   - MAE,
   - quadratisch gewichtetes \(\kappa\).

Vermeide mathematische Zirkularität, bei der der Rater mit seinem eigenen Rating im Konsensscore enthalten ist.

## 13.2 Flagging

Markiere Rater nur explorativ, nicht automatisch als „schlecht“. Mögliche Flag-Kriterien:

- sehr geringe Kategorienvariation,
- extrem geringe Überlappung,
- starke Severity bei großer Unsicherheit,
- auffälliger Misfit,
- starke Drift,
- negative oder sehr geringe Konsistenz mit leave-one-out Konsens.

Alle Flags müssen gemeinsam mit Unsicherheit und Stichprobengröße interpretiert werden.

---

# 14. Modellvergleiche und Sensitivitätsanalysen

Vergleiche mindestens folgende Aktionsscores:

1. Rohmittelwert,
2. rater-zentrierter Mittelwert,
3. LMM-BLUP,
4. ordinaler posteriorer Score,
5. JRT/MFRM-Score, falls stabil schätzbar.

## 14.1 Vergleichsgrößen

Berechne:

- Pearson- und Spearman-Korrelationen,
- Rangkorrelationen,
- mittlere absolute Rangverschiebung,
- Überlappung der Top-5 %, Top-10 % und Bottom-10 %,
- Scatterplots,
- Rangdifferenzplots,
- Unterschiede nach Zahl der Ratings,
- Unterschiede nach Raterzusammensetzung.

## 14.2 Stabilität nach Zahl der Ratings

Stratifiziere nach:

- 1 Rating,
- 2 Ratings,
- 3 Ratings,
- 4–7 Ratings.

Erwarte stärkere Schrumpfung und größere Unsicherheit bei weniger Ratings.

## 14.3 Cross-Validation

Führe eine rating-level Cross-Validation durch, bei der einzelne beobachtete Ratings vorhergesagt werden. Wegen der gekreuzten Struktur sind mehrere Ziele zu unterscheiden:

- Vorhersage eines weiteren Ratings für eine bekannte Aktion und bekannten Rater,
- Vorhersage für bekannte Aktion und neuen Rater,
- Vorhersage für neue Aktion,
- Vorhersage für neue Aktion und neuen Rater.

Nicht jede Modellklasse kann alle Ziele identisch behandeln. Dokumentiere das konkrete Vorhersageziel.

## 14.4 Rater-Assignment-Sensitivität

Falls Rater nicht zufällig Aktionen zugeordnet wurden, prüfe:

- Zusammenhang zwischen Rater und Aktionstyp,
- Zusammenhang zwischen Rater und Match/Team/Spieler,
- unterschiedliche Rohkreativität der zugewiesenen Aktionen,
- mögliche Confounding-Strukturen.

Erweitere bei Bedarf:

\[
y_{ij}
=
\mu + u_i + v_j +
\boldsymbol{x}_i^\top \boldsymbol{\beta}
+\varepsilon_{ij}.
\]

Die Einbeziehung von Aktionsmerkmalen dient nicht primär dazu, den Kreativitätsscore zu „bereinigen“, sondern um systematische Zuweisungsunterschiede und bekannte Struktur zu untersuchen.

---

# 15. Erweiterte Abhängigkeiten im Fußballdatensatz

Prüfe, ob Aktionen innerhalb von Spielern, Matches oder Teams gruppiert sind.

Ein mögliches erweitertes Modell:

\[
y_{ijmpt}
=
\mu +
u_i^{(\text{action})} +
v_j^{(\text{rater})} +
w_m^{(\text{match})} +
q_p^{(\text{player})} +
z_t^{(\text{team})} +
\varepsilon_{ijmpt}.
\]

Wichtig:

- Eine Aktion gehört typischerweise genau zu einem Spieler und Match.
- Der Aktions-Random-Effect bleibt das primäre Messobjekt.
- Zusätzliche Ebenen verändern die Interpretation der Aktionsvarianz.
- Vergleiche Basismodell und erweitertes Modell.
- Prüfe, ob Score-Rangfolgen wesentlich verändert werden.

---

# 16. Simulation und Recovery-Check

Erstelle einen optionalen Simulationsabschnitt, der das reale Ratingdesign nachbildet:

1. Verwende dieselbe Rater–Aktions-Inzidenzmatrix wie im echten Datensatz.
2. Simuliere bekannte:
   - Aktionsparameter,
   - Rater-Severity,
   - Residualvarianz,
   - gegebenenfalls ordinale Schwellen.
3. Fitte die vorgesehenen Modelle.
4. Prüfe:
   - Bias,
   - RMSE,
   - Coverage,
   - Rangkorrelation,
   - Recovery der Rater-Severity,
   - Verhalten bei Aktionen mit einem Rating.

Dieser Schritt zeigt, welche Parameter mit dem konkreten unbalancierten Design empirisch identifizierbar sind.

---

# 17. Ergebnisdateien

## 17.1 `action_scores.csv`

Mindestens folgende Spalten:

```text
action_id
n_ratings
connected_component
raw_mean
raw_median
rater_centered_mean
lmm_score
lmm_score_se
lmm_score_lower
lmm_score_upper
ordinal_latent_score
ordinal_latent_lower
ordinal_latent_upper
ordinal_expected_rating
jrt_score
jrt_score_se
score_flag
```

Nicht verfügbare Modellwerte als fehlend speichern, nicht als Null.

## 17.2 `rater_diagnostics.csv`

Mindestens:

```text
rater_id
n_ratings
n_actions
n_categories_used
raw_mean
raw_sd
extreme_category_rate
central_category_rate
network_component
network_degree
mean_pair_overlap
lmm_severity
lmm_severity_se
ordinal_severity
ordinal_severity_lower
ordinal_severity_upper
jrt_discrimination
jrt_severity
leave_one_out_spearman
leave_one_out_mae
drift_estimate
diagnostic_flag
```

## 17.3 Tabellen

Erzeuge publication-ready Tabellen:

- Stichprobenbeschreibung,
- Ratings pro Aktion,
- Ratings pro Rater,
- Konnektivität,
- Krippendorffs Alpha mit Intervallen,
- Varianzkomponenten,
- absolute und relative Reliabilität für \(k=1,\ldots,7\),
- Modellvergleich,
- Raterdiagnostik,
- Sensitivitätsanalysen.

---

# 18. Kernabbildungen

Erzeuge mindestens:

1. Verteilung der Ratings.
2. Zahl der Ratings pro Aktion.
3. Zahl der Bewertungen pro Rater.
4. Heatmap der Raterüberlappung.
5. Heatmap paarweiser Spearman-Korrelationen.
6. Heatmap mittlerer Raterdifferenzen.
7. Varianzkomponenten mit Unsicherheit.
8. D-Study-Kurven für absolute und relative Reliabilität.
9. Caterpillar-Plot der Rater-Severity.
10. Rohmittelwert gegen modellbasierten Score.
11. Score-Unterschiede nach Anzahl Ratings.
12. Posterior-Predictive-Checks des ordinalen Modells.
13. Judge Category Curves beziehungsweise Kategorienkurven.
14. Raterinformation beziehungsweise Informationsfunktionen.
15. Unsicherheitsintervalle ausgewählter Aktionsscores.

Alle Abbildungen benötigen:

- verständliche Achsentitel,
- Untertitel mit Stichprobengröße,
- erklärende Caption,
- exportierbare Version als PNG und PDF/SVG,
- keine irreführenden abgeschnittenen Achsen.

---

# 19. Automatisierter Interpretationsblock

Schreibe im finalen Bericht automatisch generierte, aber vorsichtige Interpretationen.

Beispielstruktur:

```text
Das lineare Varianzkomponentenmodell zerlegte die beobachtete
Ratingvarianz in Unterschiede zwischen Aktionen, systematische
Unterschiede zwischen Ratern und residuale Abweichungen. Die
relative Reliabilität fiel [höher/niedriger] als die absolute
Reliabilität aus. Dieses Muster ist mit [starken/schwachen]
systematischen Rater-Niveaueffekten vereinbar.

Die Interpretation bezieht sich auf das vorliegende, unvollständig
gekreuzte Design. Aktionen mit nur einem Rating tragen zur
modellbasierten Schätzung der Aktionsverteilung bei, liefern aber
keine innerhalb der Aktion beobachtete Information über
Interrater-Übereinstimmung.
```

Keine festen Grenzwerte mechanisch als gut/schlecht deklarieren. Falls Schwellenwerte aus der Literatur erwähnt werden, kennzeichne sie als heuristisch und kontextabhängig.

---

# 20. Qualitätskontrollen

Die Coding-Instanz muss vor Abschluss prüfen:

- Sind alle IDs eindeutig und korrekt typisiert?
- Gibt es doppelte Rater-Aktions-Paare?
- Sind alle Ratings zwischen 1 und 7?
- Ist der Rater–Aktions-Graph verbunden?
- Sind Varianzkomponenten nichtnegativ und plausibel?
- Haben Modelle konvergiert?
- Gibt es singuläre Fits?
- Sind Bayesianische Diagnostiken akzeptabel?
- Stimmen Formeln und Codekonventionen überein?
- Sind Vorzeichen der Severity-Parameter klar erklärt?
- Werden Aktionen mit einem Rating korrekt behandelt?
- Werden Unsicherheiten mit ausgegeben?
- Sind Ergebnisse aus Python und R numerisch ähnlich, soweit dieselben Modelle geschätzt werden?
- Werden Unterschiede zwischen ML/REML und Bayes korrekt erklärt?
- Sind sämtliche Tabellen und Abbildungen reproduzierbar?
- Sind Rohdaten unverändert erhalten?
- Sind Paketversionen dokumentiert?

Implementiere automatisierte Assertions und Tests.

---

# 21. Empfohlene Reihenfolge der finalen Analyse

## Primäranalyse

1. Datenvalidierung und Cleaning.
2. Konnektivitätsanalyse.
3. Deskriptive Raterdiagnostik.
4. Krippendorffs ordinales Alpha mit Cluster-Bootstrap.
5. Lineares gekreuztes Random-Intercept-Modell.
6. Absolute und relative Reliabilität.
7. D-Study für ein bis sieben Ratings.
8. LMM-BLUP-Aktionsscores und Rater-Severity.
9. Bayesianisches ordinales gekreuztes Modell.
10. Ordinale Aktionsscores und Rater-Severity.
11. Vergleich der Scoremethoden.

## Erweiterte Analyse

12. JRT/MFRM.
13. Rater-spezifische Diskrimination oder Schwellen.
14. Raterdrift.
15. zusätzliche Match-/Spieler-/Team-Struktur.
16. Design-basierte Simulation.
17. Cross-Validation und Scorestabilität.

Die lineare und ordinale Modellierung sollen beide berichtet werden. Das lineare Modell ist besonders transparent für Varianzzerlegung und D-Study; das ordinale Modell respektiert die begrenzte geordnete Skala.

---

# 22. Methodische Leitlinien für die Interpretation

1. **Agreement ist nicht dasselbe wie Korrelation.**  
   Hohe Korrelation kann trotz großer systematischer Mittelwertunterschiede auftreten.

2. **Klassische ICC-Tabellen setzen häufig vollständigere Designs voraus.**  
   Bei unbalancierten, unvollständig gekreuzten Daten sollen Varianzkomponenten aus Mixed Models verwendet werden.

3. **Aktionen mit einem Rating liefern keine direkte Agreement-Information.**  
   Sie können aber in einem hierarchischen Modell einen unsicheren, stark geschrumpften Score erhalten.

4. **Raterzentrierung kann mit Assignment-Confounding verwechselt werden.**  
   Modellbasierte Korrektur ist nur bei ausreichender Vernetzung glaubwürdig.

5. **BLUPs sind keine unverzerrten Rohschätzungen.**  
   Ihre Schrumpfung ist beabsichtigt und verbessert häufig die Vorhersage, erschwert aber naive Ranginterpretationen.

6. **Ordinale Modelle benötigen ausreichende Kategorienutzung.**  
   Sehr selten verwendete Kategorien können instabile Schwellen verursachen.

7. **JRT ist nicht automatisch besser als ein einfacheres Modell.**  
   Rater-spezifische Diskrimination und Schwellen müssen durch die Daten getragen werden.

8. **Rater-Fit ist keine moralische Bewertung.**  
   Misfit kann auf uneindeutige Aktionen, unterschiedliche Interpretationsstrategien, geringe Stichprobe oder Datenfehler hinweisen.

9. **Unvollständige Konnektivität begrenzt Vergleichbarkeit.**  
   Getrennte Komponenten sind ohne zusätzliche Anker nicht auf einer gemeinsamen Severity-Skala identifizierbar.

10. **Die Scoreunsicherheit ist ein Ergebnis, kein Nebenaspekt.**  
    Ranglisten ohne Unsicherheitsangaben sind insbesondere bei einem oder zwei Ratings problematisch.

---

# 23. Referenzen, die in den Notebooks erläutert werden sollen

Verwende und überprüfe die bibliografischen Angaben. Mindestens folgende Literatur aufnehmen:

- Amabile, T. M. (1982). Social psychology of creativity: A consensual assessment technique. *Journal of Personality and Social Psychology, 43*(5), 997–1013.
- Amabile, T. M. (1996). *Creativity in Context*. Westview Press.
- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language, 59*(4), 390–412.
- Bates, D., Mächler, M., Bolker, B., & Walker, S. (2015). Fitting linear mixed-effects models using lme4. *Journal of Statistical Software, 67*(1), 1–48.
- Brennan, R. L. (2001). *Generalizability Theory*. Springer.
- Bürkner, P.-C. (2017). brms: An R package for Bayesian multilevel models using Stan. *Journal of Statistical Software, 80*(1), 1–28.
- Eckes, T. (2015). *Introduction to Many-Facet Rasch Measurement* (2nd ed.). Peter Lang.
- Krippendorff, K. (2004/2018). *Content Analysis: An Introduction to Its Methodology*. Sage.
- Linacre, J. M. (1989). *Many-Facet Rasch Measurement*. MESA Press.
- Myszkowski, N., & Storme, M. (2019). Judge Response Theory? A call to upgrade our psychometrical account of creativity judgments. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175. https://doi.org/10.1037/aca0000225
- Myszkowski, N. (2021). Development of the R library `jrt`: Automated item-response theory procedures for judgment data and their application with the Consensual Assessment Technique. Prüfe die endgültigen Publikationsdaten und DOI anhand der aktuellen Paketdokumentation.
- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts*. Prüfe Band, Ausgabe, Seiten und DOI.
- Shavelson, R. J., & Webb, N. M. (1991). *Generalizability Theory: A Primer*. Sage.
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin, 86*(2), 420–428.
- McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some intraclass correlation coefficients. *Psychological Methods, 1*(1), 30–46.
- Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine, 15*(2), 155–163.

Füge zusätzlich die jeweils verwendete Softwaredokumentation ein:

- aktuelle `statsmodels`-Dokumentation zu `MixedLM` und gekreuzten Varianzkomponenten,
- aktuelle `lme4`-Dokumentation,
- aktuelle `brms`-Dokumentation für kumulative ordinale Modelle,
- aktuelle `jrt`-Paketdokumentation,
- aktuelle Dokumentation des verwendeten Krippendorff-Alpha-Pakets.

---

# 24. Erwartetes Endprodukt

Das Endprodukt muss ohne manuelles Kopieren einzelner Zwischenergebnisse:

1. Rohdaten importieren beziehungsweise den Python-Platzhalter bereitstellen,
2. Rohdaten als CSV sichern,
3. Daten validieren und bereinigen,
4. alle Analysen ausführen,
5. Modelle und Diagnostiken speichern,
6. Aktionsscores und Raterdiagnostik exportieren,
7. einen vollständigen HTML-Bericht rendern,
8. einen Abschnitt „Limitations and design implications“ erzeugen,
9. konkrete Empfehlungen für zukünftige Ratingzuweisungen geben.

Die Empfehlungen für künftige Datenerhebungen sollen insbesondere behandeln:

- ausreichend viele Ratings pro Aktion,
- Mindestüberlappung zwischen Ratern,
- gezielte Brückenaktionen,
- balancierte oder blockweise balancierte Zuweisung,
- wiederholte Ankeraktionen,
- Prüfung von Raterdrift,
- Kalibrierungssitzungen,
- Trennung von Training und finaler Bewertung.

---

# 25. Abbruch- und Warnregeln

Breche nicht kommentarlos ab. Erzeuge stattdessen klare Warnungen, wenn:

- der Google-Sheet-Platzhalter nicht ersetzt wurde,
- Pflichtvariablen fehlen,
- Ratings außerhalb 1–7 liegen,
- Duplikate ungeklärt sind,
- der Graph mehrere große getrennte Komponenten enthält,
- ein Modell nicht konvergiert,
- ein Bayesianisches Modell Divergenzen zeigt,
- Schwellen nicht geordnet oder Kategorien extrem dünn besetzt sind,
- JRT-Parameter nicht identifiziert erscheinen,
- ein Rater zu wenige Beobachtungen für individuelle Diagnostik hat.

In solchen Fällen:

- sichere alle bis dahin validen Ergebnisse,
- erkläre die Ursache,
- schlage eine methodisch vertretbare reduzierte Analyse vor,
- erzeuge keine irreführenden finalen Scores.

---

# 26. Kurze Zusammenfassung für den Coding-Agenten

Implementiere die Analyse nicht als Sammlung isolierter Kennwerte, sondern als zusammenhängenden psychometrischen Workflow:

- Netzwerk/Konnektivität bestimmt, ob Rater vergleichbar sind.
- Krippendorffs Alpha liefert eine globale Agreement-Perspektive für unvollständige ordinale Daten.
- Ein lineares gekreuztes Mixed Model liefert transparente Varianzkomponenten, absolute und relative Reliabilität sowie D-Study-Kurven.
- Empirical-Bayes-Scores integrieren ungleich viele Ratings und quantifizieren Unsicherheit.
- Ein ordinales hierarchisches Modell respektiert die 1–7-Skala.
- MFRM/JRT untersucht Severity, Kategorienutzung, Diskrimination und Informationsbeitrag der Rater.
- Alle Scoremethoden werden vergleichend und sensitivitätsanalytisch bewertet.
- Kein Aktionsscore wird ohne Anzahl Ratings und Unsicherheitsangabe ausgegeben.
