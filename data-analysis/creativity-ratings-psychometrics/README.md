# Psychometrische Analyse unvollständig gekreuzter Kreativitätsratings

Vollständiger, parallel in **Python** und **R** implementierter
psychometrischer Analyse-Workflow für Kreativitätsratings von ca. 4.000
Fußballaktionen, bewertet auf einer unipolaren 7-stufigen Skala (1 = nicht
kreativ, 7 = sehr kreativ) durch eine ungleiche Anzahl Rater pro Aktion
(unbalanciertes, unvollständig gekreuztes Design).

Diese Implementierung folgt dem Analyseauftrag in
`../../psychometrie_kreativitaetsratings_llm_anleitung.md` (26 Abschnitte:
Datenvalidierung, Konnektivitätsprüfung, deskriptives Agreement,
Krippendorffs Alpha, lineares gekreuztes Mixed-Model, Bayesianisches
ordinales Facettenmodell, Judge-Response-Theory-Erweiterung,
Rater-Fit-Diagnostik, Modellvergleich, Simulation/Recovery, Export,
automatisierte Interpretation, QC).

## ⚠️ Status dieses Repository-Snapshots

- **Python-Notebook** (`notebooks/01_creativity_ratings_python.ipynb`):
  inhaltlich vollständig (alle 20 Abschnitte, siehe unten), syntaktisch
  geprüft, **aber noch nicht end-to-end ausgeführt** in diesem Snapshot
  (die Bayesianischen Modelle — ordinales Facettenmodell und
  JRT-Erweiterung — benötigen je ca. 8–10 Minuten Rechenzeit; das wurde
  aus Zeitgründen für diesen Commit übersprungen). **Führe das Notebook
  vor Verwendung einmal komplett aus**, siehe unten.
- **R-Notebook** (`notebooks/01_creativity_ratings_R.qmd`): inhaltlich
  vollständig, R-Syntax geprüft (`knitr::purl()` + `parse()`, keine
  Fehler), **ebenfalls noch nicht gerendert/ausgeführt** (das
  `brms`-Modell kompiliert Stan-Code und kann je nach Maschine mehrere
  Minuten dauern; `lme4::bootMer` mit 200 Replikationen ebenfalls).
- `reports/analysis_report.html` existiert noch nicht — wird durch
  Rendern des R-Notebooks (oder Export des Python-Notebooks) erzeugt.
- Alle Daten in diesem Repository-Zustand sind **simuliert**
  (`DEV_MODE = True`, siehe unten) — klar gekennzeichnet, keine echten
  Befunde.

Siehe `PROGRESS.md` für den detaillierten Entwicklungsverlauf, gefundene
und behobene Bugs, sowie eine ausführliche Sektion-für-Sektion-Übersicht
beider Notebooks.

## Projektstruktur

```text
.
├── README.md                     <- diese Datei
├── PROGRESS.md                   <- Entwicklungsprotokoll, Debugging-Notizen
├── requirements.txt               <- Python-Abhängigkeiten
├── install_r_packages_narrow.R    <- R-Paketinstallation (schlank, empfohlen)
├── install_r_packages.R           <- R-Paketinstallation (breit, NICHT empfohlen — siehe PROGRESS.md)
├── scripts/
│   ├── simulate_ratings.py        <- erzeugt die simulierten Entwicklungsdaten
│   ├── build_python_notebook.py   <- baut das .ipynb aus Zellinhalten (nbformat)
│   └── _draft_sections/           <- Quellinhalt einzelner Notebook-Abschnitte (Backup)
├── data/
│   ├── raw/ratings_long_raw.csv           <- Rohdaten (unverändert nach Import)
│   ├── processed/                         <- bereinigte Daten, finale Scores
│   └── simulation/                        <- Ground-Truth-Parameter (nur für Recovery-Check)
├── notebooks/
│   ├── 01_creativity_ratings_python.ipynb
│   └── 01_creativity_ratings_R.qmd
├── results/
│   ├── figures/    <- PNG + SVG, mit Captions
│   ├── tables/     <- CSV-Tabellen
│   ├── models/     <- gespeicherte Modellobjekte (.nc für PyMC/ArviZ)
│   └── logs/       <- Session-Infos, Warnungen, automatisierte Interpretation
└── reports/
    └── analysis_report.html       <- (noch zu erzeugen, siehe unten)
```

## Installation

### Python

```bash
cd data-analysis/creativity-ratings-psychometrics
python3 -m venv ../../.venv        # falls noch nicht vorhanden
source ../../.venv/bin/activate
pip install -r requirements.txt
```

Bereits getestet mit Python 3.12.9; installierte Versionen werden bei
jedem Notebooklauf automatisch in `results/logs/session_info_python.json`
protokolliert.

**Hinweis Bayes-Engine:** Der Analyseauftrag schlägt `cmdstanpy` vor;
diese Implementierung verwendet stattdessen **PyMC** als primäre
Python-Bayes-Engine (siehe Begründung im Notebook, Abschnitt 6.2) — rein
pip-installierbar, kein separates CmdStan-Toolchain-Setup nötig.

### R

```bash
cd data-analysis/creativity-ratings-psychometrics
Rscript install_r_packages_narrow.R
```

**Nicht** `install_r_packages.R` (das breite Skript) verwenden — es
nutzt `dependencies = TRUE`, was den kompletten "Suggests"-Baum
transitiv installiert (in unserem Testlauf u. a. duckdb, xgboost, mlr3,
forecast — alles irrelevante Vignetten-/Test-Abhängigkeiten, die den
Installationslauf um über eine Stunde verlängerten, ohne für die
Analyse selbst gebraucht zu werden). `install_r_packages_narrow.R`
installiert gezielt nur Depends/Imports/LinkingTo.

**Bekannter offener Punkt:** Die Pakete `jrt`, `mirt`, `arrow`, `quarto`
(R-Wrapper; die `quarto`-CLI selbst muss separat installiert sein) und
`tidybayes` waren zum Zeitpunkt dieses Snapshots über den
Posit-Package-Manager-Snapshot nicht verfügbar ("package X is not
available for this version of R" — vermutlich Indexierungslücke für die
sehr neue R-Version 4.6.0). Nächster Versuch: Installation über den
Standard-CRAN-Spiegel statt des datumsgepinnten PPM-Snapshots:

```r
options(repos = c(CRAN = "https://cloud.r-project.org"))
install.packages(c("jrt", "mirt", "arrow", "quarto", "tidybayes"))
```

Das R-Notebook ist so geschrieben, dass es **ohne** diese Pakete
lauffähig bleibt (Verfügbarkeitsprüfung zur Laufzeit + klare Warnung
statt stillem Fehlschlag) — die JRT-Analyse läuft in diesem Fall
vollständig über PyMC im Python-Notebook plus eine `brms`-basierte
Annäherung (rater-spezifischer Diskriminationsparameter über
`disc ~ 0 + rater_id`) im R-Notebook.

## Verwendung

### 1. (Optional) Simulierte Entwicklungsdaten neu erzeugen

```bash
python3 scripts/simulate_ratings.py
```

Erzeugt `data/raw/ratings_long_raw.csv` (klar als `data_source =
"simulated_dev_placeholder"` markiert) sowie Ground-Truth-Parameter unter
`data/simulation/` für den Recovery-Check. Fester Seed (`20260713`) für
Reproduzierbarkeit.

### 2. Python-Notebook ausführen

```bash
cd notebooks
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=1200 01_creativity_ratings_python.ipynb
```

**Erwartete Laufzeit: ca. 20–30 Minuten** (dominiert durch das ordinale
Bayes-Modell ~10 min und die JRT-Erweiterung ~8 min; alle übrigen
Abschnitte zusammen < 5 min). Bei Bedarf `scripts/build_python_notebook.py`
anpassen und erneut ausführen, um das Notebook neu zu bauen (überschreibt
`notebooks/01_creativity_ratings_python.ipynb`).

### 3. R-Notebook rendern

```bash
cd notebooks
quarto render 01_creativity_ratings_R.qmd
```

Erzeugt `01_creativity_ratings_R.html` im selben Ordner. Für den finalen
`reports/analysis_report.html` diese Datei dorthin verschieben/kopieren
(oder das Quarto-YAML um einen `output-dir`-Eintrag ergänzen).
**Erwartete Laufzeit:** abhängig von der `brms`/Stan-Kompilierzeit und
`bootMer`-Replikationszahl — für einen schnellen Probelauf `iter`/`warmup`
im `brms::brm()`-Aufruf sowie `N_BOOT_LMM` reduzieren (im Notebook an den
jeweiligen Stellen kommentiert).

### 4. Mit echten Daten statt Simulation arbeiten

1. Im Python-Notebook, Abschnitt "1. Datenimport aus Google Sheets": den
   bereits vorhandenen Importcode aus
   `../paper1-data-analysis.ipynb` (Google-Sheets-Download-Logik) in die
   markierte Platzhalterzelle einfügen.
2. `DEV_MODE = True` auf `DEV_MODE = False` setzen.
3. Python-Notebook komplett neu ausführen — speichert automatisch die
   neuen Rohdaten nach `data/raw/ratings_long_raw.csv` (überschreibt die
   simulierten Daten) und lässt die gesamte Pipeline unverändert
   durchlaufen.
4. R-Notebook neu rendern (liest dieselbe `data/raw/ratings_long_raw.csv`).
5. **Abschnitt "Simulations-/Recovery-Check" wird dann automatisch
   ungültig** (kein `data/simulation/ground_truth_*` für echte Daten) —
   das Notebook selbst weist im Markdown-Text explizit darauf hin, dass
   dieser Abschnitt nur mit simulierten Daten aussagekräftig ist.

## Reproduzierbarkeit

- Fester Seed `20260713` in beiden Sprachen (Python: `np.random.seed` +
  `np.random.default_rng`; R: `set.seed`).
- Paketversionen werden bei jedem Lauf protokolliert:
  `results/logs/session_info_python.json`,
  `results/logs/sessionInfo_r.txt`.
- Git-Commit-Hash wird protokolliert, sofern das Projekt unter
  Versionskontrolle steht (aktuell nicht der Fall — `git init` optional).
- Betriebssystem und Zeitpunkt jedes Laufs werden mitgeloggt.

## Nicht-verhandelbare methodische Regeln (siehe Notebooks für Details)

- Absolute Übereinstimmung ≠ relative Konsistenz ≠ Reliabilität eines
  Einzelratings ≠ Reliabilität eines aggregierten Scores — diese Größen
  werden in beiden Notebooks explizit unterschieden (Abschnitt 6/7).
- Aktionen mit nur einem Rating bleiben für die modellbasierte Schätzung
  erhalten, tragen aber keine within-Aktion-Agreement-Information.
- Rater-Severity ist nur innerhalb verbundener Komponenten des
  Rater–Aktions-Graphen identifizierbar — beide Notebooks prüfen dies
  explizit vor jeder rater-korrigierenden Modellierung (Abschnitt 4/5).
- Kein Aktionsscore wird ohne Anzahl Ratings und Unsicherheitsangabe
  exportiert.
- Keine mechanischen Gut/Schlecht-Schwellenwerte in der automatisierten
  Interpretation.

## Qualitätskontroll-Checkliste (Kurzfassung)

Ausführliche, automatisiert geprüfte Checkliste siehe jeweils letzter
Abschnitt der Notebooks (`results/tables/qc_checklist.csv` bzw.
`qc_checklist_R.csv`). Manuell zu bestätigen vor Publikation:

- [ ] `DEV_MODE = False` gesetzt, echte Daten eingespielt
- [ ] Python-Notebook komplett neu ausgeführt, keine Fehlerzellen
- [ ] R-Notebook komplett neu gerendert, keine Fehler
- [ ] `results/tables/qc_checklist.csv` und `qc_checklist_R.csv`
      geprüft — alle Checks bestanden bzw. Abweichungen erklärt
- [ ] `results/tables/warnings_log.csv` durchgesehen — keine
      unerwarteten/unerklärten Warnungen
- [ ] Konnektivitätsprüfung: eine oder mehrere Komponenten? Falls mehrere:
      Ergebnisse entsprechend kommuniziert
- [ ] Bayesianische Diagnostik (R-hat, ESS, Divergenzen) für alle Modelle
      akzeptabel
- [ ] `action_scores.csv` / `rater_diagnostics.csv` enthalten
      ausschließlich `NaN` (nicht `0`) für nicht verfügbare Werte
- [ ] `reports/analysis_report.html` aktuell und vollständig gerendert

## Lizenz / Zitation

Interner Analyse-Workflow für das Projekt `11-paper-CAT-methodology`.
Literaturverweise siehe Notebook-Abschnitt 0 (Python) bzw. entsprechender
Abschnitt (R).
