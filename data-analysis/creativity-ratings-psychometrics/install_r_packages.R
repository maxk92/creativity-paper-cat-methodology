# ============================================================
# Reproduzierbare R-Paketinstallation
# ============================================================
# Diese Datei ersetzt eine vollstaendige renv.lock-Datei, weil renv
# eine bereits initialisierte, mit dem Internet synchronisierte
# renv-Umgebung voraussetzt. Stattdessen: ein deterministisches
# Installationsskript mit fixiertem CRAN-Snapshot (Posit Package
# Manager), das denselben Reproduzierbarkeitszweck erfuellt.
#
# Verwendung:
#   Rscript install_r_packages.R
#
# Danach kann optional "renv::init(); renv::snapshot()" ausgefuehrt
# werden, um ein renv.lock aus der so entstandenen Bibliothek zu
# erzeugen.
# ============================================================

# Fixierter Zeitpunkt-Snapshot fuer reproduzierbare Paketversionen.
# (Posit Package Manager CRAN-Spiegel, gefroren auf ein festes Datum)
options(repos = c(CRAN = "https://packagemanager.posit.co/cran/2026-07-01"))

pkgs_core <- c(
  "tidyverse", "data.table", "janitor", "skimr", "naniar",
  "igraph", "here", "renv"
)

pkgs_models <- c(
  "lme4", "lmerTest", "performance", "insight", "broom.mixed",
  "sjPlot", "ggeffects", "ordinal", "glmmTMB", "irr", "psych"
)

# Krippendorffs Alpha: bevorzugtes Paket laut Analyseauftrag.
# Stand 2026 heisst das CRAN-Paket "krippendorffsalpha"; falls es
# nicht verfuegbar ist, wird ersatzweise "irr::kripp.alpha" (nur
# intervall-/nominal-/ordinalskaliert, ohne fehlende Werte pro
# Design-Zelle in derselben Flexibilitaet) sowie eine transparente
# Eigenimplementierung im Notebook verwendet.
pkgs_agreement <- c("krippendorffsalpha")

# Bayesianischer ordinaler Workflow. ACHTUNG: brms benoetigt im
# Hintergrund Stan (rstan oder cmdstanr) inkl. C++-Toolchain und
# Kompilierung -- dies kann in einer frischen Umgebung 15-30+
# Minuten dauern und schlaegt ohne funktionierenden C++-Compiler
# fehl. Das Skript versucht die Installation, bricht aber den
# Gesamtlauf nicht ab, falls sie scheitert (siehe try()).
pkgs_bayes <- c("brms", "posterior", "bayesplot", "loo", "tidybayes")

# Judge Response Theory / Many-Facet-Rasch.
pkgs_irt <- c("jrt", "mirt", "TAM")

pkgs_io <- c("arrow", "quarto")

install_safely <- function(pkgs) {
  for (p in pkgs) {
    if (!requireNamespace(p, quietly = TRUE)) {
      message(sprintf("---- installiere %s ----", p))
      ok <- tryCatch({
        install.packages(p, dependencies = TRUE)
        TRUE
      }, error = function(e) {
        message(sprintf("FEHLER bei %s: %s", p, conditionMessage(e)))
        FALSE
      })
      if (!ok || !requireNamespace(p, quietly = TRUE)) {
        message(sprintf("WARNUNG: %s konnte nicht installiert werden. ",
                         p),
                "Abhaengige Notebook-Abschnitte sind entsprechend als ",
                "eval=FALSE markiert bzw. geben eine klare Warnung aus.")
      }
    } else {
      message(sprintf("%s bereits installiert.", p))
    }
  }
}

install_safely(pkgs_core)
install_safely(pkgs_models)
install_safely(pkgs_agreement)
install_safely(pkgs_irt)
install_safely(pkgs_io)
install_safely(pkgs_bayes)

# Protokolliere den Installationsstatus fuer den Reproduzierbarkeits-Log.
all_pkgs <- c(pkgs_core, pkgs_models, pkgs_agreement, pkgs_irt, pkgs_io,
              pkgs_bayes)
status <- data.frame(
  package = all_pkgs,
  installed = vapply(all_pkgs, requireNamespace, logical(1), quietly = TRUE)
)
dir.create("results/logs", showWarnings = FALSE, recursive = TRUE)
write.csv(status, "results/logs/r_package_install_status.csv",
          row.names = FALSE)
print(status)
