# ============================================================
# Shared settings and helpers for the JRT pipeline (R/01_grm.R, 02_comparison.R,
# 03_simulations.R). Every script sources this file first.
#
# Reliability convention (posterior-based, theta ~ N(0, 1)):
#   rel(theta) = I(theta) / (I(theta) + 1),   SE(theta) = 1 / sqrt(I(theta) + 1)
# ============================================================

suppressPackageStartupMessages({
  library(mirt)
  library(dplyr)
  library(tidyr)
  library(readr)
  library(ggplot2)
})
options(warn = 1)  # print warnings where they occur (they end up in the run log)

SEED <- 20260713
set.seed(SEED)

# JRT_QUICK=1 lowers the number of draws, imputations, bootstraps and
# replications for a quick check. Outputs of a quick run are NOT for the paper.
QUICK <- nzchar(Sys.getenv("JRT_QUICK"))

# --- paths (ROOT = the analysis folder, parent of R/) -------------------------
this_file <- grep("^--file=", commandArgs(FALSE), value = TRUE)
ROOT <- if (length(this_file)) {
  normalizePath(file.path(dirname(sub("^--file=", "", this_file[1])), ".."))
} else normalizePath(".")  # interactive use from the analysis folder
# JRT_INPUT=<path> overrides the input file (e.g. to re-run on an archived data freeze).
INPUT_CSV <- Sys.getenv("JRT_INPUT", file.path(ROOT, "data", "processed", "ratings_long_clean.csv"))
# JRT_DUPLICATES=<path> overrides the duplicate log written by notebook 00 (only counted in the design summary).
DUPLICATES_CSV <- Sys.getenv("JRT_DUPLICATES", file.path(ROOT, "results", "tables", "flagged_duplicate_rater_action_pairs.csv"))
RES <- file.path(ROOT, "results")
DIRS <- list(main = file.path(RES, "main"), supplement = file.path(RES, "supplement"),
             data = file.path(RES, "data"), models = file.path(RES, "models"),
             logs = file.path(RES, "logs"))
for (d in DIRS) dir.create(d, recursive = TRUE, showWarnings = FALSE)
for (d in c("main", "supplement")) dir.create(file.path(DIRS[[d]], "figures"), showWarnings = FALSE)

# --- constants ----------------------------------------------------------------
# Raters with fewer ratings than this are excluded (decision 2026-10-22): with up
# to 7 parameters per rater, their parameters are not identified.
MIN_RATINGS_PER_RATER <- 15L
SCALE_MIN <- 1L  # the 1-7 rating scale is coded 0-6 internally (rating - 1)
SCALE_MAX <- 7L
K_CATEGORIES <- SCALE_MAX - SCALE_MIN + 1L
THETA_GRID <- seq(-4, 4, by = 0.05)  # grid for all information computations
THETA_POINTS <- c(-2, -1, 0, 1, 2)

# mirt estimation settings: MML via EM with fixed quadrature (61 points is
# mirt's default for a unidimensional model, written out so it is documented).
MIRT_METHOD <- "EM"
MIRT_QUADPTS <- 61L
MIRT_SE_TYPE <- "Oakes"
MIRT_TOL <- 1e-4
MIRT_NCYCLES <- 2000L

# --- output -------------------------------------------------------------------
# where = "main" (objects in the main text), "supplement", "data" or "models".
save_csv <- function(x, name, where = "main") {
  path <- file.path(DIRS[[where]], paste0(name, ".csv"))
  readr::write_csv(as.data.frame(x), path, na = "NA")
  message("  wrote ", sub(paste0(ROOT, "/"), "", path))
  invisible(path)
}

save_fig <- function(plot, name, where = "main", width = 8, height = 5) {
  if (inherits(plot, "ggplot")) plot <- plot + labs(title = NULL)  # the caption carries the title
  for (ext in c("png", "svg")) {
    ggsave(file.path(DIRS[[where]], "figures", paste0(name, ".", ext)), plot,
           width = width, height = height, dpi = 300, bg = "white")
  }
  message("  wrote ", where, "/figures/", name, ".{png,svg}")
}

# --- model fitting -------------------------------------------------------------
fit_mirt <- function(wide, itemtype, SE = TRUE) {
  set.seed(SEED)
  mirt(wide, model = 1, itemtype = itemtype, method = MIRT_METHOD, quadpts = MIRT_QUADPTS,
       SE = SE, SE.type = MIRT_SE_TYPE, TOL = MIRT_TOL,
       technical = list(NCYCLES = MIRT_NCYCLES), verbose = FALSE)
}

convergence_row <- function(mod, label) {
  data.frame(
    model = label,
    itemtype = paste(unique(extract.mirt(mod, "itemtype")), collapse = ","),
    method = MIRT_METHOD, quadpts = MIRT_QUADPTS, se_type = MIRT_SE_TYPE, tol = MIRT_TOL,
    converged = extract.mirt(mod, "converged"),
    iterations = extract.mirt(mod, "iterations"),
    information_matrix_pd = tryCatch(extract.mirt(mod, "secondordertest"), error = function(e) NA),
    condition_number = tryCatch(extract.mirt(mod, "condnum"), error = function(e) NA),
    logLik = extract.mirt(mod, "logLik"),
    npar = extract.mirt(mod, "nest"),
    AIC = extract.mirt(mod, "AIC"),
    BIC = extract.mirt(mod, "BIC"),
    SABIC = extract.mirt(mod, "SABIC"),
    n_products = nrow(extract.mirt(mod, "data")),
    n_ratings = sum(!is.na(extract.mirt(mod, "data"))),
    stringsAsFactors = FALSE
  )
}

eap_scores <- function(mod) {
  fscores(mod, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE)
}

# Empirical marginal reliability of EAP scores: Var(theta_hat) / (Var(theta_hat) + mean PSD^2)
empirical_rel <- function(fs) var(fs[, "F1"]) / (var(fs[, "F1"]) + mean(fs[, "SE_F1"]^2))

# --- information and reliability ------------------------------------------------
# Rater information on a theta grid: matrix (length(theta) x J).
rater_information <- function(mod, theta) {
  J <- extract.mirt(mod, "nitems")
  Th <- matrix(theta)
  info <- vapply(seq_len(J), function(j) iteminfo(extract.item(mod, j), Th), numeric(length(theta)))
  colnames(info) <- colnames(extract.mirt(mod, "data"))
  info
}
rel_from_info <- function(info) info / (info + 1)
se_from_info <- function(info) 1 / sqrt(info + 1)
normal_weights <- function(theta) dnorm(theta) * mean(diff(theta))  # N(0, 1) weights on a grid

# Information of a product at its EAP estimate, summed over the raters who rated it.
product_information <- function(mod, theta_hat, rated) {
  info_all <- rater_information(mod, theta_hat)  # products x raters
  rowSums(info_all * rated)
}

# --- agreement of product rankings --------------------------------------------------
pct_rank <- function(x) (rank(x) - 0.5) / length(x)
quintile <- function(x) pmin(5L, floor(pct_rank(x) * 5) + 1L)
rank_change <- function(x, ref) {
  shift <- abs(pct_rank(x) - pct_rank(ref))
  tibble(pearson = cor(x, ref), spearman = cor(x, ref, method = "spearman"),
         mean_abs_percentile_shift = mean(shift),
         p95_abs_percentile_shift = unname(quantile(shift, 0.95)),
         max_abs_percentile_shift = max(shift),
         share_products_changing_quintile = mean(quintile(x) != quintile(ref)),
         share_products_changing_quintile_by_2_or_more = mean(abs(quintile(x) - quintile(ref)) >= 2))
}

rater_order <- function(ids) ids[order(as.integer(gsub("\\D", "", ids)), ids)]  # R01, R02, ...

# --- pseudonym key (interactive use only) --------------------------------------------
# data/raw/rater_pseudonym_key.csv (written by notebook 00, gitignored) maps the
# original user IDs to R01, R02, ... No pipeline script calls these helpers, and
# their output must never be written to results/.
RATER_KEY_CSV <- file.path(ROOT, "data", "raw", "rater_pseudonym_key.csv")
rater_key <- function() {
  if (!file.exists(RATER_KEY_CSV)) stop("No pseudonym key at ", RATER_KEY_CSV, " (run notebook 00)")
  key <- read_csv(RATER_KEY_CSV, col_types = cols(.default = "c"))
  setNames(key$original_rater_id, key$rater_id)  # pseudonym -> original
}
switch_rater_ids <- function(ids, to = c("original", "pseudonym")) {
  key <- rater_key()
  if (match.arg(to) == "pseudonym") key <- setNames(names(key), key)
  out <- unname(key[ids])
  if (anyNA(out[!is.na(ids)])) stop("IDs not in the key: ", paste(unique(ids[is.na(out) & !is.na(ids)]), collapse = ", "))
  out
}
