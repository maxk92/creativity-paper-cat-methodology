# ============================================================
# 05 - Naive indices: Cronbach's alpha and Krippendorff's alpha (spec section 6)
# ============================================================
# Reference values for common practice only. They are NOT used downstream.
#
# Cronbach's alpha: consistency of the UNWEIGHTED mean over raters. Assumes
#   tau-equivalent raters and refers to the mean of all J raters. It is not
#   directly comparable with the IRT reliability of theta_hat.
# Krippendorff's alpha (ordinal): agreement (consensus) of single ratings.
#
# Both use the shared wide matrix (original scale 1-7 = internal + 1).
# Outputs (results/naive/): cronbach_alpha.csv, cronbach_crossed_blocks.csv,
#   krippendorff_alpha.csv
# SERVER: the Krippendorff bootstrap (1000 replications).
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))
suppressPackageStartupMessages({library(psych); library(irr)})

N_BOOT <- if (SMOKE) 20L else 1000L
MIN_PAIR_OVERLAP <- 3L  # a covariance needs at least this many shared products

d <- load_design()
wide <- d$wide + SCALE_MIN  # back to 1-7
rated <- !is.na(wide)
raters <- colnames(wide)
overlap <- crossprod(rated * 1L)

# --- Cronbach's alpha with pairwise covariances --------------------------------------
# Listwise deletion is impossible (no product is rated by all raters). Covariances
# are computed pairwise; a pair needs >= MIN_PAIR_OVERLAP shared products. Raters
# whose covariance with some other rater is not computable are removed one at a
# time (the rater with the most missing covariances first) until the covariance
# matrix is complete. Removed raters are reported.
pair_ok <- overlap >= MIN_PAIR_OVERLAP
keep <- raters
removed <- character()
repeat {
  bad <- rowSums(!pair_ok[keep, keep, drop = FALSE])
  if (all(bad == 0)) break
  drop <- names(which.max(bad))
  removed <- c(removed, drop)
  keep <- setdiff(keep, drop)
}
alpha_cov <- cov(wide[, keep], use = "pairwise.complete.obs")
# n.obs only affects psych's confidence bounds, which are not used here.
alpha_fit <- with_warnings(psych::alpha(alpha_cov, n.obs = sum(rowSums(rated[, keep]) >= 2),
                                        check.keys = FALSE, warnings = FALSE),
                           "psych::alpha (pairwise covariance matrix)")
sub_rated <- rated[, keep]
pairs_used <- overlap[keep, keep][upper.tri(overlap[keep, keep])]
cronbach <- tibble(
  variant = "pairwise covariances, all usable raters",
  raw_alpha = alpha_fit$total$raw_alpha,
  std_alpha = alpha_fit$total$std.alpha,
  average_r = alpha_fit$total$average_r,
  n_raters = length(keep),
  raters_removed = paste(removed, collapse = ";"),
  n_products_contributing = sum(rowSums(sub_rated) >= 2),
  n_rater_pairs = length(pairs_used),
  rater_pairs_min_overlap = min(pairs_used),
  rater_pairs_median_overlap = median(pairs_used),
  missing_handling = paste0("psych::alpha on cov(use = 'pairwise.complete.obs'); pairs need >= ",
                            MIN_PAIR_OVERLAP, " shared products"),
  interpretation = paste("Consistency of the unweighted mean over the raters; assumes",
                         "tau-equivalence; not comparable with the IRT reliability of theta_hat.")
)

# Fully crossed blocks: sets of raters who all rated the same products. No product
# is rated by all raters, so we search the largest crossed block for each block
# size k, using the rater sets that actually occur (and their subsets up to size 4).
sets <- unique(lapply(seq_len(nrow(rated)), function(i) raters[rated[i, ]]))
sets <- sets[lengths(sets) >= 2]
cand <- unique(c(sets, unlist(lapply(sets, function(s) {
  unlist(lapply(2:min(4, length(s)), function(k) combn(s, k, simplify = FALSE)), recursive = FALSE)
}), recursive = FALSE)))
cand_n <- vapply(cand, function(s) sum(rowSums(rated[, s, drop = FALSE]) == length(s)), integer(1))
blocks <- tibble(k = lengths(cand), raters = vapply(cand, paste, "", collapse = ";"), n_products = cand_n) %>%
  group_by(k) %>% slice_max(n_products, n = 1, with_ties = FALSE) %>% ungroup() %>%
  filter(k >= 2, n_products >= 10)
blocks$raw_alpha <- vapply(seq_len(nrow(blocks)), function(i) {
  s <- strsplit(blocks$raters[i], ";")[[1]]
  x <- wide[rowSums(rated[, s, drop = FALSE]) == length(s), s, drop = FALSE]
  psych::alpha(x, check.keys = FALSE, warnings = FALSE)$total$raw_alpha
}, numeric(1))
save_csv(blocks, DIR_NAIVE, "cronbach_crossed_blocks")

# The reported crossed-subset alpha: the largest block with at least 3 raters
# (if any), else the best pair.
best <- blocks %>% filter(k >= 3) %>% slice_max(n_products, n = 1, with_ties = FALSE)
if (nrow(best) == 0) best <- blocks %>% slice_max(n_products, n = 1, with_ties = FALSE)
if (nrow(best) == 1) {
  cronbach <- bind_rows(cronbach, tibble(
    variant = "fully crossed block (listwise complete)",
    raw_alpha = best$raw_alpha, n_raters = best$k, n_products_contributing = best$n_products,
    raters_removed = paste("block raters:", best$raters),
    missing_handling = "complete block, no missing values",
    interpretation = cronbach$interpretation[1]))
}
cronbach$all_raters_fully_crossed_subset_exists <- any(rowSums(rated) == ncol(rated))
save_csv(cronbach, DIR_NAIVE, "cronbach_alpha")

# --- Krippendorff's alpha (ordinal) ---------------------------------------------------------
# irr::kripp.alpha expects raters x units. NA marks a missing rating and is
# handled natively (units with fewer than two ratings are not pairable).
rel_data <- t(wide)
stopifnot(nrow(rel_data) == length(raters), ncol(rel_data) == nrow(wide),
          sum(!is.na(rel_data)) == sum(rated), identical(rownames(rel_data), raters))
ka <- irr::kripp.alpha(rel_data, method = "ordinal")$value

set.seed(SEED)
boot <- vapply(seq_len(N_BOOT), function(b) {
  idx <- sample.int(ncol(rel_data), replace = TRUE)
  tryCatch(irr::kripp.alpha(rel_data[, idx], method = "ordinal")$value,
           error = function(e) NA_real_)
}, numeric(1))
krippendorff <- tibble(
  method = "ordinal", alpha = ka,
  ci_low = quantile(boot, 0.025, na.rm = TRUE), ci_high = quantile(boot, 0.975, na.rm = TRUE),
  ci_type = "percentile bootstrap, resampling products",
  n_boot = N_BOOT, n_boot_failed = sum(is.na(boot)), seed = SEED,
  n_units = ncol(rel_data), n_pairable_units = sum(colSums(!is.na(rel_data)) >= 2),
  n_raters = nrow(rel_data), package = paste0("irr ", packageVersion("irr")),
  interpretation = "Agreement (consensus) of single ratings; raters treated as interchangeable."
)
save_csv(krippendorff, DIR_NAIVE, "krippendorff_alpha")

print(cronbach %>% select(variant, raw_alpha, n_raters, n_products_contributing))
print(krippendorff %>% select(alpha, ci_low, ci_high, n_boot))
write_warnings("05_naive_indices")
write_session_info("05_naive_indices")
message("05 naive indices: done")
