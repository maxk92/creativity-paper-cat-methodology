# ============================================================
# Shared helpers for the JRT audit pipeline (R/01_*.R ... R/06_*.R)
# ============================================================
# Spec: ../../ANLEITUNG_JRT_Audit.md. Audit log: ../AUDIT.md.
# Every script sources this file first, so paths, seed, data loading and the
# information/reliability definitions are defined exactly once.
#
# Reliability convention (used everywhere, posterior-based, theta ~ N(0, 1)):
#   rel(theta) = I(theta) / (I(theta) + 1),   SE(theta) = 1 / sqrt(I(theta) + 1)
# The ML version 1 - 1/I(theta) is NOT used anywhere in this pipeline.
# ============================================================

suppressPackageStartupMessages({
  library(mirt)
  library(dplyr)
  library(tidyr)
  library(readr)
  library(ggplot2)
})

SEED <- 20260713
set.seed(SEED)

# Smoke mode (server/run_jrt_audit_server.sh --smoke): small imputation and
# bootstrap counts. Outputs of a smoke run are NOT for the paper.
SMOKE <- identical(Sys.getenv("JRT_SMOKE"), "1")

# --- paths ------------------------------------------------------------------
script_dir <- function() {
  arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
  if (length(arg) == 1) return(dirname(normalizePath(sub("^--file=", "", arg))))
  normalizePath("R")  # interactive use from the analysis folder
}
# JRT_ROOT overrides the analysis folder (used to test the pipeline on a toy copy).
ROOT <- normalizePath(Sys.getenv("JRT_ROOT", file.path(script_dir(), "..")))
INPUT_CSV <- file.path(ROOT, "data", "processed", "ratings_long_clean.csv")
RES <- file.path(ROOT, "results")
DIR_DATA <- file.path(RES, "data")
DIR_GRM <- file.path(RES, "grm")
DIR_GRM_FIG <- file.path(DIR_GRM, "figures")
DIR_CMP <- file.path(RES, "comparison")
DIR_NAIVE <- file.path(RES, "naive")
DIR_SUM <- file.path(RES, "summary")
DIR_LOGS <- file.path(RES, "logs")
DIR_MODELS <- file.path(RES, "models")  # gitignored
for (d in c(DIR_DATA, DIR_GRM, DIR_GRM_FIG, DIR_CMP, DIR_NAIVE, DIR_SUM, DIR_LOGS, DIR_MODELS)) {
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
}

# Raters with fewer ratings than this are excluded from the whole pipeline
# (decision 2026-10-22): with up to 7 parameters per rater in the GRM, their
# parameters are not identified (all-raters run: R21 a = -0.09, R22 a = -3.86
# with huge SEs). Applied once, in 01_data_design.R; listed in
# results/data/excluded_raters.csv.
MIN_RATINGS_PER_RATER <- 15L

# Category coding: the 1-7 rating scale is coded 0-6 internally (rating - 1).
SCALE_MIN <- 1L
SCALE_MAX <- 7L
K_CATEGORIES <- SCALE_MAX - SCALE_MIN + 1L

# Fixed theta grid for all information computations (spec 4a).
THETA_GRID <- seq(-4, 4, by = 0.05)
THETA_POINTS <- c(-2, -1, 0, 1, 2)

# Estimation settings for every mirt model (spec 3 and 5): MML via EM with
# fixed-quadrature integration. 61 points is mirt's own default for a
# unidimensional model; it is set explicitly here so it is documented.
MIRT_METHOD <- "EM"
MIRT_QUADPTS <- 61L
MIRT_SE_TYPE <- "Oakes"
MIRT_TOL <- 1e-4  # mirt default for EM, written out
MIRT_NCYCLES <- 2000L

# --- output helpers ---------------------------------------------------------
save_csv <- function(x, dir, name) {
  path <- file.path(dir, paste0(name, ".csv"))
  readr::write_csv(as.data.frame(x), path, na = "NA")
  message("  wrote ", sub(paste0(ROOT, "/"), "", path))
  invisible(path)
}

save_fig <- function(plot, name, width = 8, height = 5, dir = DIR_GRM_FIG) {
  # No plot title: the manuscript caption carries it.
  if (inherits(plot, "ggplot")) plot <- plot + labs(title = NULL)
  for (ext in c("png", "svg")) {
    ggsave(file.path(dir, paste0(name, ".", ext)), plot, width = width, height = height,
           dpi = 300, bg = "white")
  }
  message("  wrote ", name, ".{png,svg}")
}

# Captures every warning of an expression into a log instead of letting it
# scroll past (spec 3: "no warnings ignored").
WARNINGS <- list()
with_warnings <- function(expr, context) {
  withCallingHandlers(expr, warning = function(w) {
    WARNINGS[[length(WARNINGS) + 1]] <<- data.frame(
      context = context, warning = conditionMessage(w), stringsAsFactors = FALSE)
    invokeRestart("muffleWarning")
  })
}
write_warnings <- function(stage) {
  df <- if (length(WARNINGS)) do.call(rbind, WARNINGS) else
    data.frame(context = character(), warning = character())
  save_csv(df, DIR_LOGS, paste0("warnings_jrt_audit_", stage))
}

write_session_info <- function(stage) {
  path <- file.path(DIR_LOGS, paste0("session_info_jrt_audit_", stage, ".txt"))
  sink(path)
  cat("Stage:", stage, "\nTimestamp:", format(Sys.time()), "\nSeed:", SEED,
      "\nSmoke run:", SMOKE, "\n\n")
  print(sessionInfo())
  sink()
}

# --- data -------------------------------------------------------------------
# The single data source of all models (written by 01_data_design.R).
load_design <- function() {
  long <- readr::read_csv(file.path(DIR_DATA, "ratings_long.csv"), show_col_types = FALSE,
                          col_types = cols(product_id = "c", rater_id = "c", .default = "d"))
  wide_df <- readr::read_csv(file.path(DIR_DATA, "ratings_wide.csv"), show_col_types = FALSE,
                             col_types = cols(product_id = "c", .default = "i"))
  wide <- as.matrix(wide_df[, -1])
  rownames(wide) <- wide_df$product_id
  fp <- readLines(file.path(DIR_DATA, "data_fingerprint.txt"))
  stopifnot(identical(data_fingerprint(wide), fp))
  list(long = long, wide = wide)
}

data_fingerprint <- function(wide) {
  tmp <- tempfile()
  writeLines(c(colnames(wide), rownames(wide),
               apply(wide, 1, paste, collapse = ",")), tmp)
  sprintf("%d products x %d raters | %d ratings | md5 %s",
          nrow(wide), ncol(wide), sum(!is.na(wide)), unname(tools::md5sum(tmp)))
}

# Spec 5: identical data basis in all models (asserted, not assumed).
assert_same_data <- function(mod, wide, label) {
  d <- extract.mirt(mod, "data")
  ok <- nrow(d) == nrow(wide) && ncol(d) == ncol(wide) &&
    identical(colnames(d), colnames(wide)) && identical(is.na(unname(d)), is.na(unname(wide)))
  if (!ok) stop(sprintf("Model %s does not use the shared wide matrix.", label))
  invisible(TRUE)
}

fit_mirt <- function(wide, itemtype, label, SE = TRUE) {
  set.seed(SEED)
  mod <- with_warnings(
    mirt(wide, model = 1, itemtype = itemtype, method = MIRT_METHOD,
         quadpts = MIRT_QUADPTS, SE = SE, SE.type = MIRT_SE_TYPE, TOL = MIRT_TOL,
         technical = list(NCYCLES = MIRT_NCYCLES), verbose = FALSE),
    context = paste0("mirt fit ", label))
  assert_same_data(mod, wide, label)
  mod
}

convergence_row <- function(mod, label) {
  data.frame(
    model = label,
    itemtype = paste(unique(extract.mirt(mod, "itemtype")), collapse = ","),
    method = MIRT_METHOD, quadpts = MIRT_QUADPTS, se_type = MIRT_SE_TYPE, tol = MIRT_TOL,
    converged = extract.mirt(mod, "converged"),
    iterations = extract.mirt(mod, "iterations"),
    information_matrix_pd = tryCatch(extract.mirt(mod, "secondordertest"),
                                     error = function(e) NA),
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

# --- absolute fit: C2 (spec 3) ------------------------------------------------
# mirt 1.46 computes the uni- and bivariate moments of M2-type statistics from
# the available pairs when data are missing. A rater pair that shares no products
# has undefined bivariate moments, so C2 becomes NaN. The null model (calcNull)
# is not requested: with a NaN statistic its comparison errors out. If C2 is not
# finite, the reason is recorded instead of forcing a result.
c2_global_fit <- function(mod) {
  d <- extract.mirt(mod, "data")
  ov <- crossprod(!is.na(d))
  n_pairs <- sum(upper.tri(ov))
  n_no_overlap <- sum(ov[upper.tri(ov)] == 0)
  res <- tryCatch(with_warnings(M2(mod, type = "C2", calcNull = FALSE, quadpts = MIRT_QUADPTS), "M2 C2"),
                  error = function(e) e)
  ok <- !inherits(res, "error") && is.finite(res$M2)
  out <- data.frame(statistic = "C2", computable = ok,
                    rater_pairs = n_pairs, rater_pairs_without_overlap = n_no_overlap)
  if (ok) {
    cbind(out, as.data.frame(res), note = paste(
      "Computed on pairwise-available moments; rater pairs without overlap",
      "contribute no information. Interpret with caution."))
  } else {
    out$note <- if (inherits(res, "error")) paste("Not computable:", conditionMessage(res)) else
      sprintf("Not computable: %d of %d rater pairs share no products, so their bivariate moments and hence C2 are undefined.",
              n_no_overlap, n_pairs)
    out
  }
}

# --- information and reliability (spec 4) -----------------------------------
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

# N(0, 1) quadrature weights on an equally spaced grid (sum to ~1 over -4..4).
normal_weights <- function(theta) dnorm(theta) * mean(diff(theta))

# Product-level information at the EAP estimate, summed ONLY over the raters
# who actually rated the product (spec 4c). Using testinfo(mod, theta) with all
# raters here would be wrong for an incomplete design.
product_information <- function(mod, theta_hat, rated) {
  stopifnot(nrow(rated) == length(theta_hat))
  info_all <- rater_information(mod, theta_hat)  # products x raters
  stopifnot(identical(dim(info_all), dim(rated)))
  rowSums(info_all * rated)
}

# --- agreement of product rankings -----------------------------------------------
# Percentile ranks in [0, 1] (ties get their mean rank); quintiles 1-5 of each
# score's own distribution. Used for model comparison (04) and raw mean vs GRM (03).
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

# Pretty rater-ID order (R01, R02, ...).
rater_order <- function(ids) ids[order(as.integer(gsub("\\D", "", ids)), ids)]

# --- pseudonym key (local inspection only) ------------------------------------
# data/raw/rater_pseudonym_key.csv (written by notebook 00, gitignored) maps the
# original user IDs to R01, R02, ... Use these helpers interactively to look up
# raters in the raw data. No pipeline script calls them, and their output must
# never be written to results/.
RATER_KEY_CSV <- file.path(ROOT, "data", "raw", "rater_pseudonym_key.csv")
rater_key <- function() {
  if (!file.exists(RATER_KEY_CSV)) stop("No pseudonym key at ", RATER_KEY_CSV, " (run notebook 00)")
  key <- read_csv(RATER_KEY_CSV, col_types = cols(.default = "c"))
  setNames(key$original_rater_id, key$rater_id)  # named vector: pseudonym -> original
}
# to = "original" adds/replaces with original IDs; to = "pseudonym" maps back.
switch_rater_ids <- function(ids, to = c("original", "pseudonym")) {
  key <- rater_key()
  if (match.arg(to) == "pseudonym") key <- setNames(names(key), key)
  out <- unname(key[ids])
  if (anyNA(out[!is.na(ids)])) stop("IDs not in the key: ", paste(unique(ids[is.na(out) & !is.na(ids)]), collapse = ", "))
  out
}
