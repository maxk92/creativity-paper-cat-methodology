# Schlanke Nachinstallation nur der noch fehlenden, tatsaechlich benoetigten
# Pakete (Depends/Imports/LinkingTo, OHNE Suggests -- der vorige Lauf mit
# dependencies=TRUE zog unnoetig grosse optionale Abhaengigkeitsbaeume nach
# sich, z.B. duckdb/xgboost/mlr3 als reine Vignetten-/Test-Suggests von
# tidyverse-Paketen).
options(repos = c(CRAN = "https://packagemanager.posit.co/cran/2026-07-01"))

pkgs <- c("nloptr", "lme4", "lmerTest", "glmmTMB", "jrt", "mirt", "arrow", "quarto", "tidybayes")

install_safely <- function(pkgs) {
  for (p in pkgs) {
    if (!requireNamespace(p, quietly = TRUE)) {
      message(sprintf("---- installiere %s ----", p))
      tryCatch(
        install.packages(p, dependencies = c("Depends", "Imports", "LinkingTo")),
        error = function(e) message(sprintf("FEHLER bei %s: %s", p, conditionMessage(e)))
      )
    } else {
      message(sprintf("%s bereits installiert.", p))
    }
  }
}
install_safely(pkgs)

status <- data.frame(package = pkgs,
                      installed = vapply(pkgs, requireNamespace, logical(1), quietly = TRUE))
dir.create("results/logs", showWarnings = FALSE, recursive = TRUE)
write.csv(status, "results/logs/r_package_install_status_narrow.csv", row.names = FALSE)
print(status)
