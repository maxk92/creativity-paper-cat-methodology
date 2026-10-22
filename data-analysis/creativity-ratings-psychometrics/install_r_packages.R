# ============================================================
# R package installation for notebooks/02_creativity_ratings_R.qmd
# ============================================================
# Usage (from this folder):
#   Rscript install_r_packages.R
#
# Installs only Depends/Imports/LinkingTo (no Suggests): installing with
# dependencies = TRUE pulls in a huge, irrelevant Suggests tree.
# Packages are taken from a date-pinned Posit Package Manager snapshot
# for reproducibility; anything missing there (e.g. jrt, mirt for very
# new R versions) is retried from the regular CRAN mirror.
# ============================================================

snapshot_repo <- "https://packagemanager.posit.co/cran/2026-07-01"
fallback_repo <- "https://cloud.r-project.org"

pkgs <- c(
  # data handling
  "tidyverse", "here", "janitor", "glue", "scales",
  # design / agreement
  "igraph", "irr", "psych", "krippendorffsalpha",
  # mixed models
  "nloptr", "lme4", "lmerTest", "performance", "ordinal",
  # IRT / facet models
  "sirt", "mirt", "jrt",
  # Bayesian
  "brms", "loo",
  # rendering
  "knitr", "rmarkdown"
)

install_safely <- function(p, repo) {
  tryCatch(
    install.packages(p, repos = repo,
                     dependencies = c("Depends", "Imports", "LinkingTo")),
    error = function(e) message(sprintf("ERROR installing %s: %s", p, conditionMessage(e)))
  )
}

for (p in pkgs) {
  if (requireNamespace(p, quietly = TRUE)) {
    message(sprintf("%s already installed.", p))
    next
  }
  message(sprintf("---- installing %s ----", p))
  install_safely(p, snapshot_repo)
  if (!requireNamespace(p, quietly = TRUE)) install_safely(p, fallback_repo)
}

status <- data.frame(package = pkgs,
                     installed = vapply(pkgs, requireNamespace, logical(1), quietly = TRUE))
print(status, row.names = FALSE)
