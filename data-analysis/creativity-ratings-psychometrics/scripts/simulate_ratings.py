"""
============================================================
SIMULIERTE ENTWICKLUNGSDATEN -- KEINE ECHTEN BEFUNDE
============================================================
Dieses Skript erzeugt einen simulierten Datensatz, der die im
Analyseauftrag beschriebene Ratingsituation strukturell nachbildet:

  - ~4000 Fussballaktionen
  - unipolare 7-stufige Kreativitaetsskala (1 = nicht kreativ,
    7 = sehr kreativ)
  - ungleiche Anzahl Ratings pro Aktion (~600 mit 1, ~2000 mit 2,
    restliche mit 3-7 Ratings)
  - unbalanciertes, unvollstaendig gekreuztes Rater-Aktions-Design
    (Rater sind ueberwiegend "Matches" in Bloecken zugeordnet,
    einige "Brueckenrater" bewerten ueber Bloecke hinweg)
  - ein bewusst isolierter Mini-Cluster (2 Rater, 60 Aktionen ohne
    jede Ueberlappung zum Rest), um die Konnektivitaetspruefung aus
    Abschnitt 5 des Analyseauftrags tatsaechlich zu testen
  - realistische "Verschmutzungen" (Duplikate, Werte ausserhalb
    1-7, fehlende und nicht-numerische Werte), um die
    Validierungs-/Cleaning-Logik aus Abschnitt 4 zu testen

Die Daten werden aus einem bekannten Generierungsmodell (kumulatives
Logit-Modell mit Aktions-Theta, rater-spezifischer Severity und
Diskrimination) gezogen. Die "wahren" Parameter werden getrennt vom
Hauptdatensatz unter data/simulation/ gespeichert und AUSSCHLIESSLICH
fuer den Recovery-Check in Abschnitt 16 verwendet -- sie fliessen
nicht in die Hauptanalyse-Pipeline ein, die die Daten wie echte,
unbekannte Ratings behandelt.

WICHTIG: Sobald echte Ratings aus Google Sheets vorliegen, ersetzt
der Google-Sheet-Importschritt in den Notebooks (Abschnitt 3 des
Analyseauftrags) diese Datei. Dieses Skript dient ausschliesslich
der Entwicklung und Demonstration der Pipeline.
============================================================
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260713
rng = np.random.default_rng(SEED)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "ratings_long_raw.csv"
SIM_DIR = PROJECT_ROOT / "data" / "simulation"
RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
SIM_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
# 1. Grunddesign: Aktionen, Matches, Spieler, Teams, Aktionstypen
# ------------------------------------------------------------------
N_ACTIONS_MAIN = 3940       # Hauptpopulation (verbundene Komponente)
N_ACTIONS_ISOLATED = 60     # bewusst isolierter Mini-Cluster
N_ACTIONS = N_ACTIONS_MAIN + N_ACTIONS_ISOLATED   # ~4000 gesamt

N_RATERS_MAIN = 38
N_RATERS_ISOLATED = 2
N_RATERS = N_RATERS_MAIN + N_RATERS_ISOLATED

ACTION_TYPES = ["Pass", "Dribble", "Shot", "Cross", "Miscontrol",
                 "throwin", "Clearance", "Foul Won", "Dispossessed",
                 "Interception"]
ACTION_TYPE_P = np.array([0.44, 0.20, 0.08, 0.07, 0.05,
                            0.04, 0.04, 0.03, 0.03, 0.02])
ACTION_TYPE_P = ACTION_TYPE_P / ACTION_TYPE_P.sum()

N_MATCHES = 210
N_TEAMS = 24
N_PLAYERS = 260

action_id_main = [f"A{i:05d}" for i in range(N_ACTIONS_MAIN)]
action_id_iso = [f"AI{i:04d}" for i in range(N_ACTIONS_ISOLATED)]
action_ids = action_id_main + action_id_iso

match_ids_main = rng.integers(1, N_MATCHES + 1, size=N_ACTIONS_MAIN)
# Isolierter Cluster stammt aus eigenen, exklusiven Matches, damit er
# inhaltlich plausibel bleibt (z.B. ein separat annotiertes Turnier).
match_ids_iso = rng.integers(N_MATCHES + 1, N_MATCHES + 6,
                              size=N_ACTIONS_ISOLATED)
match_id = np.concatenate([match_ids_main, match_ids_iso])

team_id = rng.integers(1, N_TEAMS + 1, size=N_ACTIONS)
player_id = rng.integers(1, N_PLAYERS + 1, size=N_ACTIONS)
action_type = rng.choice(ACTION_TYPES, size=N_ACTIONS, p=ACTION_TYPE_P)

# ------------------------------------------------------------------
# 2. Latente Aktions-"Kreativitaet" theta_i (Standardnormal)
# ------------------------------------------------------------------
theta_action = rng.normal(0, 1, size=N_ACTIONS)
component_true = np.array(["main"] * N_ACTIONS_MAIN
                            + ["isolated"] * N_ACTIONS_ISOLATED)

# ------------------------------------------------------------------
# 3. Rater-Parameter: Severity, Diskrimination, Drift, Expertise
# ------------------------------------------------------------------
rater_ids = [f"R{j:02d}" for j in range(N_RATERS_MAIN)] + \
            [f"RI{j:01d}" for j in range(N_RATERS_ISOLATED)]

# Severity v_j: positiv = grosszuegiger, negativ = strenger.
severity_raw = rng.normal(0, 0.6, size=N_RATERS)
severity_true = severity_raw - severity_raw[:N_RATERS_MAIN].mean()  # zentriert auf Hauptgruppe

# Diskrimination a_j (log-normal um 1 herum; >1 = differenziert staerker)
discrimination_true = np.exp(rng.normal(0, 0.25, size=N_RATERS))

expertise = rng.choice(["novice", "intermediate", "expert"],
                        size=N_RATERS, p=[0.3, 0.45, 0.25])

# Ein Teil der Rater zeigt lineare Ermuedungs-/Drift-Effekte
# (rater-spezifischer Zeittrend b_j, siehe Abschnitt 10.3).
has_drift = rng.random(N_RATERS) < 0.15
drift_true = np.where(has_drift, rng.normal(-0.35, 0.1, size=N_RATERS), 0.0)

rater_df = pd.DataFrame({
    "rater_id": rater_ids,
    "severity_true": severity_true,
    "discrimination_true": discrimination_true,
    "drift_true": drift_true,
    "expertise": expertise,
})

# ------------------------------------------------------------------
# 4. Globale Kategorienschwellen (kumulatives Logit-Modell, 7 Kat.)
#    Leicht rechtsschief: die meisten Fussballaktionen sind wenig
#    kreativ, wenige Aktionen sind sehr kreativ.
# ------------------------------------------------------------------
tau_true = np.array([-1.2, -0.2, 0.6, 1.4, 2.2, 3.2])

# ------------------------------------------------------------------
# 5. Rater-Aktions-Design: block-strukturierte, unvollstaendige
#    Zuordnung ueber Matches, plus einige "Brueckenrater"
# ------------------------------------------------------------------
# Jedes Match bekommt eine "Dienst"-Gruppe von 4-7 Ratern zugewiesen,
# aus der bevorzugt (aber nicht ausschliesslich) gezogen wird. Ein
# Teil der Rater ("Brueckenrater", ~6) ist ueber viele Matches
# hinweg im Dienst und stellt die globale Konnektivitaet her.
main_rater_ids = rater_ids[:N_RATERS_MAIN]
n_bridge = 6
bridge_raters = list(rng.choice(main_rater_ids, size=n_bridge,
                                  replace=False))
non_bridge_raters = [r for r in main_rater_ids if r not in bridge_raters]

match_duty = {}
for m in range(1, N_MATCHES + 1):
    n_local = rng.integers(2, 5)
    local = list(rng.choice(non_bridge_raters, size=n_local, replace=False))
    match_duty[m] = local + bridge_raters

# Zielverteilung der Ratinganzahl je Aktion (Hauptkomponente):
# ~600 mit 1, ~2000 mit 2, Rest (1340) mit 3-7 (abnehmend).
n_ratings_pool = (
    [1] * 600
    + [2] * 2000
    + list(rng.choice([3, 4, 5, 6, 7], size=N_ACTIONS_MAIN - 2600,
                        p=[0.45, 0.27, 0.15, 0.08, 0.05]))
)
n_ratings_pool = np.array(n_ratings_pool)
rng.shuffle(n_ratings_pool)
assert len(n_ratings_pool) == N_ACTIONS_MAIN

records = []
rater_clock = {r: 0 for r in rater_ids}  # fuer rating_order je Rater
base_time = pd.Timestamp("2025-08-01 12:00:00")

for idx in range(N_ACTIONS_MAIN):
    aid = action_id_main[idx]
    m = match_id[idx]
    n_i = int(n_ratings_pool[idx])
    duty = match_duty[m]
    if len(duty) >= n_i:
        chosen = list(rng.choice(duty, size=n_i, replace=False))
    else:
        extra = list(rng.choice(
            [r for r in main_rater_ids if r not in duty],
            size=n_i - len(duty), replace=False))
        chosen = duty + extra

    for rater in chosen:
        rj = rater_df.loc[rater_df.rater_id == rater].iloc[0]
        eta = discrimination_true[rater_ids.index(rater)] * theta_action[idx] \
              + rj.severity_true
        t_within = rater_clock[rater]
        eta = eta + rj.drift_true * (t_within / 200.0)  # Drift ueber Zeit im Dienst
        cum_p = 1 / (1 + np.exp(-(tau_true - eta)))
        cum_p = np.concatenate([[0.0], cum_p, [1.0]])
        cat_p = np.diff(cum_p)
        cat_p = np.clip(cat_p, 1e-9, None)
        cat_p = cat_p / cat_p.sum()
        rating = rng.choice(np.arange(1, 8), p=cat_p)

        rater_clock[rater] += 1
        records.append({
            "action_id": aid,
            "rater_id": rater,
            "rating": rating,
            "player_id": f"P{player_id[idx]:04d}",
            "match_id": f"M{m:04d}",
            "team_id": f"T{team_id[idx]:03d}",
            "action_type": action_type[idx],
            "session_id": f"S{m:04d}_{rater}",
            "rating_order": rater_clock[rater],
            "timestamp": base_time + pd.Timedelta(minutes=5 * m)
                          + pd.Timedelta(seconds=37 * rater_clock[rater]),
            "rater_expertise": rj.expertise,
        })

# --- isolierter Mini-Cluster: nur die 2 isolierten Rater bewerten
#     nur die 60 isolierten Aktionen, jede Aktion von beiden Ratern.
for idx in range(N_ACTIONS_ISOLATED):
    aid = action_id_iso[idx]
    theta_i = theta_action[N_ACTIONS_MAIN + idx]
    m = match_id[N_ACTIONS_MAIN + idx]
    for rater in rater_ids[N_RATERS_MAIN:]:
        rj = rater_df.loc[rater_df.rater_id == rater].iloc[0]
        j_idx = rater_ids.index(rater)
        eta = discrimination_true[j_idx] * theta_i + rj.severity_true
        cum_p = 1 / (1 + np.exp(-(tau_true - eta)))
        cum_p = np.concatenate([[0.0], cum_p, [1.0]])
        cat_p = np.diff(cum_p)
        cat_p = np.clip(cat_p, 1e-9, None)
        cat_p = cat_p / cat_p.sum()
        rating = rng.choice(np.arange(1, 8), p=cat_p)

        rater_clock[rater] += 1
        records.append({
            "action_id": aid,
            "rater_id": rater,
            "rating": rating,
            "player_id": f"P{player_id[N_ACTIONS_MAIN + idx]:04d}",
            "match_id": f"M{m:04d}",
            "team_id": f"T{team_id[N_ACTIONS_MAIN + idx]:03d}",
            "action_type": action_type[N_ACTIONS_MAIN + idx],
            "session_id": f"S{m:04d}_{rater}",
            "rating_order": rater_clock[rater],
            "timestamp": base_time + pd.Timedelta(minutes=5 * int(m))
                          + pd.Timedelta(seconds=37 * rater_clock[rater]),
            "rater_expertise": rj.expertise,
        })

df = pd.DataFrame.from_records(records)

# ------------------------------------------------------------------
# 6. Realistische "Verschmutzung" zum Testen der Cleaning-Pipeline
#    (Abschnitt 4). Diese Zeilen werden bewusst NACH der sauberen
#    Generierung eingefuegt und muessen von der Validierung im
#    Notebook erkannt und dokumentiert (nicht stillschweigend
#    gemittelt) werden.
# ------------------------------------------------------------------
df["rating"] = df["rating"].astype(object)

dirt_rng = np.random.default_rng(SEED + 1)

# a) Echte Duplikate derselben Rater-Aktions-Kombination mit
#    abweichendem Ratingwert (z.B. Wiederholungsrating / Dopplung).
dup_rows = df.sample(n=6, random_state=int(SEED + 2)).copy()
dup_rows["rating"] = dup_rows["rating"].apply(
    lambda r: int(np.clip(int(r) + dirt_rng.choice([-1, 1]), 1, 7)))
df = pd.concat([df, dup_rows], ignore_index=True)

# b) Werte ausserhalb des zulaessigen Bereichs 1-7.
bad_idx = dirt_rng.choice(df.index, size=3, replace=False)
df.loc[bad_idx[0], "rating"] = 8
df.loc[bad_idx[1], "rating"] = 0
df.loc[bad_idx[2], "rating"] = -1

# c) Fehlende Ratingwerte.
na_idx = dirt_rng.choice(df.index, size=2, replace=False)
df.loc[na_idx, "rating"] = np.nan

# d) Nicht-numerische, aber prinzipiell konvertierbare/erkennbare
#    Rohwerte (z.B. Exporteigenheiten aus Google Sheets).
str_idx = dirt_rng.choice(df.index, size=2, replace=False)
df.loc[str_idx[0], "rating"] = "n/a"
df.loc[str_idx[1], "rating"] = "4 "  # mit Leerzeichen, aber konvertierbar

df = df.sample(frac=1.0, random_state=int(SEED + 3)).reset_index(drop=True)

df["data_source"] = "simulated_dev_placeholder"

# ------------------------------------------------------------------
# 7. Speichern: Rohdaten + Ground-Truth (getrennt!)
# ------------------------------------------------------------------
df.to_csv(RAW_PATH, index=False)

rater_df.to_csv(SIM_DIR / "ground_truth_rater_params.csv", index=False)
pd.DataFrame({
    "action_id": action_ids,
    "theta_true": theta_action,
    "component_true": component_true,
}).to_csv(SIM_DIR / "ground_truth_action_params.csv", index=False)
pd.DataFrame({"k": np.arange(1, 7), "tau_true": tau_true}).to_csv(
    SIM_DIR / "ground_truth_thresholds.csv", index=False)

print(f"Simulierte Rohdaten gespeichert: {RAW_PATH} ({len(df)} Zeilen)")
print(f"Ground-Truth-Parameter gespeichert unter: {SIM_DIR}")
print(df.head())
print("\nZeilen pro (action_id, rater_id) > 1 (Duplikate, absichtlich):")
print(df.groupby(["action_id", "rater_id"]).size().gt(1).sum())
