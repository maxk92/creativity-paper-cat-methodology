# ============================================================
# 02 - Comparison models, naive indices, sensitivity, reliability overview
# ============================================================
# Adjacent-category ladder on the same data, all MML:
#   M1  RSM / MFRM   shared thresholds, rater severity, equal slopes   sirt::rm.facets
#   M2  PCM          rater-specific thresholds, equal slopes           mirt "Rasch"
#   M3  GPCM         rater-specific thresholds and slopes              mirt "gpcm"
# The GRM (cumulative family, 01_grm.R) is compared by information criteria only.
#
# M1 uses rm.facets because mirt recodes each rater's observed categories and its
# RSM refuses raters with different numbers of categories (eight raters leave
# categories unused). rm.facets keeps every rater on the full 0-6 set. It
# integrates on a fixed grid; the 321-point grid reproduces mirt's log-likelihood,
# so the cross-software M1-vs-M2 LR test is usable (approximate). The sirt default
# grid is fitted too, as a check. Latent mean 0 in all models; RSM and PCM
# estimate the latent variance (slopes 1), GPCM and GRM fix it to 1.
#
# Then: Cronbach's alpha and Krippendorff's alpha (reference values for common
# practice), the GRM refitted on all raters (sensitivity), the overview table.
#
# Run after 01_grm.R:  Rscript R/02_comparison.R   (~20 min, mostly the Krippendorff bootstrap)
# ============================================================

source(if (interactive()) "R/jrt_functions.R" else
  file.path(dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1])), "jrt_functions.R"))
suppressPackageStartupMessages({library(sirt); library(psych); library(irr)})

rd <- function(name, where = "supplement") read_csv(file.path(DIRS[[where]], paste0(name, ".csv")), show_col_types = FALSE)
wide_df <- read_csv(file.path(DIRS$data, "ratings_wide.csv"), show_col_types = FALSE, col_types = cols(product_id = "c", .default = "i"))
wide <- as.matrix(wide_df[, -1]); rownames(wide) <- wide_df$product_id
rated <- !is.na(wide)
raters <- colnames(wide)
J <- ncol(wide); K <- K_CATEGORIES; N <- nrow(wide)
grm <- readRDS(file.path(DIRS$models, "grm.rds"))
category_usage <- rd("category_usage")
internal_gap_raters <- category_usage$rater_id[category_usage$internal_gap]

# ==============================================================================
# A. Model ladder
# ==============================================================================
# --- M1: sirt::rm.facets ------------------------------------------------------
# Model: P(X_pr = k | theta_p) ∝ exp(k theta_p - k b_r - tau_k), theta ~ N(0, sigma^2).
# Settings (= the package defaults, written out): severities b_r sum to zero,
# slopes 1, one shared threshold set, latent mean 0, sigma estimated.
long <- wide_df %>%
  pivot_longer(-product_id, names_to = "rater_id", values_to = "rating_internal", values_drop_na = TRUE) %>%
  mutate(product_id = factor(product_id, levels = rownames(wide))) %>%
  arrange(product_id, rater_id)
fit_rm_facets <- function(theta_k) {
  sirt::rm.facets(dat = data.frame(creativity = long$rating_internal),
                  pid = as.character(long$product_id), rater = long$rater_id,
                  theta.k = theta_k, est.b.rater = TRUE, est.a.item = FALSE,
                  est.a.rater = FALSE, rater_item_int = FALSE, est.mean = FALSE,
                  b.rater.center = 2)
}
message("02: fitting M1 (sirt::rm.facets, 321-point grid) and the sirt default-grid check")
m1 <- fit_rm_facets(seq(-8, 8, length.out = 321))
m1_default <- fit_rm_facets(seq(-9, 9, length.out = 30))
saveRDS(m1, file.path(DIRS$models, "m1_rm_facets.rds"))
saveRDS(m1_default, file.path(DIRS$models, "m1_default_grid.rds"))
m1_person <- m1$person[match(rownames(wide), as.character(m1$person$pid)), ]
stopifnot(nrow(m1$person) == N, !anyNA(m1_person$EAP), sum(m1$rater$N) == sum(rated))
m1_npar <- J + K - 1  # J - 1 rater locations + K - 1 thresholds + latent variance
m1_ll <- as.numeric(logLik(m1))
m1_b <- setNames(m1$rater$b, as.character(m1$rater$rater))[raters]
m1_tau <- as.numeric(m1$tau.item[1, ])
m1_sigma2 <- m1$sigma^2
rsm_probs <- function(theta, b) {  # matrix length(theta) x K
  k <- 0:(K - 1)
  e <- exp(outer(theta, k) - matrix(k * b + c(0, m1_tau), length(theta), K, byrow = TRUE))
  e / rowSums(e)
}

# --- M2, M3 (mirt) ----------------------------------------------------------------
message("02: fitting M2 (PCM) and M3 (GPCM)")
m2 <- fit_mirt(wide, "Rasch")
m3 <- fit_mirt(wide, "gpcm")
saveRDS(m2, file.path(DIRS$models, "m2_pcm.rds"))
saveRDS(m3, file.path(DIRS$models, "m3_gpcm.rds"))
mirt_models <- list(M2_PCM = m2, M3_GPCM = m3, GRM = grm)

# --- model fit, information criteria, LR tests ----------------------------------
model_fit <- bind_rows(
  data.frame(model = "M1_RSM", logLik = m1_ll, npar = m1_npar,
             AIC = -2 * m1_ll + 2 * m1_npar, BIC = -2 * m1_ll + m1_npar * log(N),
             SABIC = -2 * m1_ll + m1_npar * log((N + 2) / 24), n_products = N, n_ratings = sum(rated),
             software = "sirt::rm.facets", family = "adjacent category",
             converged = m1$iter < 1000, iterations = m1$iter,
             note = sprintf("grid 321 points on [-8, 8]; rm.facets ic$np = %d", m1$ic$np)),
  bind_rows(lapply(names(mirt_models), function(nm) {
    convergence_row(mirt_models[[nm]], nm) %>%
      mutate(software = "mirt", family = ifelse(nm == "GRM", "cumulative (not in LR ladder)", "adjacent category"))
  })))
for (ic in c("AIC", "BIC", "SABIC")) model_fit[[paste0("delta_", ic)]] <- model_fit[[ic]] - min(model_fit[[ic]])
save_csv(model_fit, "model_fit", "main")

lr_row <- function(a, b, label, df_formula, note) {
  ll <- function(nm) model_fit$logLik[model_fit$model == nm]
  np <- function(nm) model_fit$npar[model_fit$model == nm]
  x2 <- 2 * (ll(b) - ll(a)); df <- np(b) - np(a)
  data.frame(comparison = label, logLik_restricted = ll(a), logLik_general = ll(b),
             X2 = x2, df = df, p = pchisq(x2, df, lower.tail = FALSE),
             df_expected_formula = df_formula, df_matches_formula = df == df_formula, note = note)
}
lr_tests <- bind_rows(
  lr_row("M1_RSM", "M2_PCM", "M1 vs M2: rater-specific thresholds", (J - 1) * (K - 2),
         paste0("Across software (rm.facets vs mirt). df differ from (J-1)(K-2) when raters ",
                "leave END categories unused (fewer step parameters in M2). ",
                if (length(internal_gap_raters)) paste0("Raters with internal category gaps (",
                  paste(internal_gap_raters, collapse = ", "), ") make the nesting approximate.")
                else "No rater has an internal category gap, so M1 is nested in M2.")),
  lr_row("M2_PCM", "M3_GPCM", "M2 vs M3: rater-specific discriminations", J - 1, "mirt, same object"))
save_csv(lr_tests, "lr_tests", "supplement")

# --- theta estimates: correlations and ranking changes ------------------------------
eap <- lapply(mirt_models, eap_scores)
theta_tab <- as_tibble(c(list(M1_RSM = m1_person$EAP), lapply(eap, function(f) f[, "F1"])))
theta_tab$rm_facets_default_grid <- m1_default$person$EAP[match(rownames(wide), as.character(m1_default$person$pid))]
theta_cor <- bind_rows(lapply(c("pearson", "spearman"), function(meth) {
  as_tibble(cor(theta_tab, method = meth), rownames = "model") %>% mutate(method = meth, .before = 1)
}))
save_csv(theta_cor, "theta_correlations", "supplement")
score_agreement <- bind_rows(lapply(c("M1_RSM", "M2_PCM", "M3_GPCM"), function(m)
  rank_change(theta_tab[[m]], theta_tab$GRM) %>% mutate(model = m, reference = "GRM", .before = 1)))
save_csv(score_agreement, "score_agreement", "main")

# --- rater parameters by model, threshold order, M3 discriminations ----------------
pars_long <- function(m, nm) {
  cf <- coef(m, IRTpars = TRUE, printSE = TRUE)
  bind_rows(lapply(c(raters, "GroupPars"), function(r) {
    x <- cf[[r]]
    tibble(model = nm, rater_id = ifelse(r == "GroupPars", "(group)", r), parameter = colnames(x),
           estimate = x["par", ], se = if ("SE" %in% rownames(x)) x["SE", ] else NA_real_)
  }))
}
rater_pars <- bind_rows(
  tibble(model = "M1_RSM", rater_id = as.character(m1$rater$rater), parameter = "b_rater",
         estimate = m1$rater$b, se = m1$se.b.rater),
  tibble(model = "M1_RSM", rater_id = "(shared)", parameter = paste0("tau", seq_along(m1_tau)),
         estimate = m1_tau, se = as.numeric(m1$se.tau.item[1, ])),
  tibble(model = "M1_RSM", rater_id = "(group)", parameter = "latent_variance", estimate = m1_sigma2, se = NA_real_),
  bind_rows(lapply(names(mirt_models), function(nm) pars_long(mirt_models[[nm]], nm))))
save_csv(rater_pars, "rater_parameters_by_model", "supplement")

threshold_order <- rater_pars %>%
  filter(model %in% c("M2_PCM", "M3_GPCM"), grepl("^b\\d+$", parameter)) %>%
  group_by(model, rater_id) %>%
  summarise(n_steps = n(), ordered = all(diff(estimate) > 0), n_reversals = sum(diff(estimate) <= 0),
            steps = paste(sprintf("%.2f", estimate), collapse = ";"), .groups = "drop")
save_csv(threshold_order, "threshold_order", "supplement")

discrimination <- rater_pars %>%
  filter(model == "M3_GPCM", parameter == "a") %>%
  left_join(category_usage %>% select(rater_id, n_ratings), by = "rater_id") %>%
  arrange(estimate)
save_csv(discrimination, "discrimination_m3", "supplement")
save_csv(tibble(statistic = c("min", "q1", "median", "q3", "max", "ratio_max_min", "sd"),
                value = c(quantile(discrimination$estimate),
                          max(discrimination$estimate) / min(discrimination$estimate), sd(discrimination$estimate))),
         "discrimination_summary", "supplement")

# --- rater fit in M1 (Rasch mean squares at the EAP estimate) -------------------------
th1 <- m1$person$EAP[match(as.character(long$product_id), as.character(m1$person$pid))]
b_obs <- m1_b[long$rater_id]
k <- 0:(K - 1)
P_obs <- t(vapply(seq_along(th1), function(i) rsm_probs(th1[i], b_obs[i]), numeric(K)))
E_obs <- as.vector(P_obs %*% k)
W_obs <- as.vector(P_obs %*% k^2) - E_obs^2
fit_m1 <- tibble(rater_id = long$rater_id, x = long$rating_internal, E = E_obs, W = W_obs) %>%
  group_by(rater_id) %>%
  summarise(n_ratings = n(), outfit = mean((x - E)^2 / W), infit = sum((x - E)^2) / sum(W), .groups = "drop") %>%
  left_join(category_usage %>% select(rater_id, missing_categories, internal_gap), by = "rater_id") %>%
  mutate(flag = infit < 0.7 | infit > 1.3 | outfit < 0.7 | outfit > 1.3,
         source = "M1 (rm.facets), mean squares at EAP") %>%
  arrange(factor(rater_id, levels = raters))
save_csv(fit_m1, "rater_fit_m1", "supplement")

# --- marginal reliability per model (comparison only) -------------------------------
# rel(theta) = s2 I(theta) / (s2 I(theta) + 1) averaged over N(0, s2); for s2 = 1
# this is I/(I+1) and equals mirt::marginal_rxx (reported as a check).
z <- THETA_GRID; w <- normal_weights(z)
marginal_from_info <- function(info, s2) sum(w * s2 * info / (s2 * info + 1)) / sum(w)
m1_info <- rowSums(vapply(raters, function(r) {   # RSM item information = Var(X | theta)
  p <- rsm_probs(sqrt(m1_sigma2) * z, m1_b[[r]])
  as.vector(p %*% k^2) - as.vector(p %*% k)^2
}, numeric(length(z))))
marg <- bind_rows(
  tibble(model = "M1_RSM", latent_variance = m1_sigma2,
         marginal_reliability = marginal_from_info(m1_info, m1_sigma2), marginal_rxx_mirt = NA_real_,
         empirical_rxx = var(m1_person$EAP) / (var(m1_person$EAP) + mean(m1_person$SE.EAP^2))),
  bind_rows(lapply(names(mirt_models), function(nm) {
    m <- mirt_models[[nm]]
    s2 <- as.numeric(coef(m, simplify = TRUE)$cov)
    tibble(model = nm, latent_variance = s2,
           marginal_reliability = marginal_from_info(rowSums(rater_information(m, sqrt(s2) * z)), s2),
           marginal_rxx_mirt = if (abs(s2 - 1) < 1e-8) marginal_rxx(m) else NA_real_,
           empirical_rxx = unname(empirical_rxx(eap[[nm]])))
  })))
save_csv(marg, "marginal_reliability", "supplement")

# ==============================================================================
# B. Sensitivity: GRM refitted on ALL raters (no exclusion, no SEs)
# ==============================================================================
message("02: fitting the GRM on all raters (sensitivity)")
raw_all <- read_csv(INPUT_CSV, show_col_types = FALSE, col_types = cols(action_id = "c", rater_id = "c", .default = "?"))
wide_all_df <- raw_all %>%
  transmute(product_id = action_id, rater_id, rating_internal = as.integer(rating_numeric) - SCALE_MIN) %>%
  pivot_wider(names_from = rater_id, values_from = rating_internal) %>%
  arrange(product_id)
raters_all <- rater_order(setdiff(names(wide_all_df), "product_id"))
wide_all <- as.matrix(wide_all_df[, raters_all]); storage.mode(wide_all) <- "integer"
rownames(wide_all) <- wide_all_df$product_id
# A rater who used a single category has no estimable parameters at all; such
# raters (if any) stay out of the refit and are named in the table.
one_category <- raters_all[apply(wide_all, 2, function(x) length(unique(na.omit(x))) < 2)]
wide_all <- wide_all[, setdiff(raters_all, one_category), drop = FALSE]
wide_all <- wide_all[rowSums(!is.na(wide_all)) > 0, , drop = FALSE]
excluded_raters <- rd("excluded_raters", "data")
grm_all <- fit_mirt(wide_all, "graded", SE = FALSE)
fs_all <- eap_scores(grm_all)
fs_fin <- eap$GRM
common <- intersect(rownames(wide), rownames(wide_all))
th_fin <- fs_fin[match(common, rownames(wide)), "F1"]
th_all <- fs_all[match(common, rownames(wide_all)), "F1"]
a_of <- function(m) vapply(raters, function(r) coef(m, IRTpars = TRUE)[[r]][1, "a"], numeric(1))
a_diff <- a_of(grm_all) - a_of(grm)
rc <- rank_change(th_all, th_fin)
sensitivity <- tibble(
  quantity = c("n_raters", "n_ratings", "n_products", "excluded_raters",
               "empirical_marginal_reliability", "model_based_marginal_reliability",
               "theta_pearson_common_products", "theta_spearman_common_products",
               "theta_mean_abs_diff", "theta_max_abs_diff", "share_products_changing_quintile",
               "a_max_abs_diff_common_raters", "a_pearson_common_raters"),
  final_data = c(ncol(wide), sum(rated), nrow(wide), "", empirical_rel(fs_fin), marginal_rxx(grm),
                 rc$pearson, rc$spearman, mean(abs(th_all - th_fin)), max(abs(th_all - th_fin)),
                 rc$share_products_changing_quintile, max(abs(a_diff)), cor(a_of(grm_all), a_of(grm))) %>% as.character(),
  all_raters = c(ncol(wide_all), sum(!is.na(wide_all)), nrow(wide_all),
                 paste(c(excluded_raters$rater_id, if (length(one_category)) paste0(one_category, " (one category, not estimable)")), collapse = ";"),
                 empirical_rel(fs_all), marginal_rxx(grm_all), rep("", 7)) %>% as.character(),
  note = c(rep("", 4), "Var(theta)/(Var(theta)+mean(PSD^2))", "mirt::marginal_rxx (hypothetical full panel)",
           rep(sprintf("all-raters vs final GRM, %d common products", length(common)), 5),
           rep(sprintf("all-raters vs final GRM, %d common raters", length(raters)), 2)))
save_csv(sensitivity, "sensitivity_rater_exclusion", "supplement")

# ==============================================================================
# C. Naive indices (reference values for common practice; not used downstream)
# ==============================================================================
N_BOOT <- if (QUICK) 20L else 1000L
# JRT_SKIP_KRIPP_BOOT=1 skips the Krippendorff bootstrap (the slowest step, ~15 min):
# the alpha is still computed, its CI is left empty.
KRIPP_BOOT <- !nzchar(Sys.getenv("JRT_SKIP_KRIPP_BOOT"))
MIN_PAIR_OVERLAP <- 3L  # a covariance needs at least this many shared products
wide17 <- wide + SCALE_MIN  # back to 1-7
overlap <- crossprod(rated * 1L)

# Cronbach's alpha (consistency of the unweighted rater mean, tau-equivalence).
# No product is rated by all raters, so covariances are pairwise; raters whose
# covariance with some other rater is not computable are removed one at a time.
pair_ok <- overlap >= MIN_PAIR_OVERLAP
keep <- raters; removed <- character()
repeat {
  bad <- rowSums(!pair_ok[keep, keep, drop = FALSE])
  if (all(bad == 0)) break
  drop <- names(which.max(bad)); removed <- c(removed, drop); keep <- setdiff(keep, drop)
}
alpha_cov <- cov(wide17[, keep], use = "pairwise.complete.obs")
alpha_fit <- psych::alpha(alpha_cov, n.obs = sum(rowSums(rated[, keep]) >= 2), check.keys = FALSE, warnings = FALSE)
pairs_used <- overlap[keep, keep][upper.tri(overlap[keep, keep])]
cronbach <- tibble(
  variant = "pairwise covariances, all usable raters",
  raw_alpha = alpha_fit$total$raw_alpha, std_alpha = alpha_fit$total$std.alpha, average_r = alpha_fit$total$average_r,
  n_raters = length(keep), raters_removed = paste(removed, collapse = ";"),
  n_products_contributing = sum(rowSums(rated[, keep]) >= 2), n_rater_pairs = length(pairs_used),
  rater_pairs_min_overlap = min(pairs_used), rater_pairs_median_overlap = median(pairs_used),
  missing_handling = paste0("psych::alpha on cov(use = 'pairwise.complete.obs'); pairs need >= ", MIN_PAIR_OVERLAP, " shared products"),
  interpretation = "Consistency of the unweighted mean over the raters; assumes tau-equivalence; not comparable with the IRT reliability of theta_hat.")

# Largest fully crossed block (raters who all rated the same products), from the
# rater sets that occur and their subsets up to size 4; reported block: the
# largest with at least 3 raters, else the best pair.
sets <- unique(lapply(seq_len(nrow(rated)), function(i) raters[rated[i, ]]))
sets <- sets[lengths(sets) >= 2]
cand <- unique(c(sets, unlist(lapply(sets, function(s) {
  unlist(lapply(2:min(4, length(s)), function(k) combn(s, k, simplify = FALSE)), recursive = FALSE)
}), recursive = FALSE)))
cand_n <- vapply(cand, function(s) sum(rowSums(rated[, s, drop = FALSE]) == length(s)), integer(1))
blocks <- tibble(k = lengths(cand), raters = vapply(cand, paste, "", collapse = ";"), n_products = cand_n) %>%
  group_by(k) %>% slice_max(n_products, n = 1, with_ties = FALSE) %>% ungroup() %>%
  filter(k >= 2, n_products >= 10)
best <- blocks %>% filter(k >= 3) %>% slice_max(n_products, n = 1, with_ties = FALSE)
if (nrow(best) == 0) best <- blocks %>% slice_max(n_products, n = 1, with_ties = FALSE)
alpha_raw <- function(x) suppressWarnings(psych::alpha(x, check.keys = FALSE, warnings = FALSE)$total$raw_alpha)
s_best <- strsplit(best$raters, ";")[[1]]
x_best <- wide17[rowSums(rated[, s_best, drop = FALSE]) == length(s_best), s_best, drop = FALSE]
cronbach <- bind_rows(cronbach, tibble(
  variant = "fully crossed block (listwise complete)", raw_alpha = alpha_raw(x_best),
  n_raters = best$k, n_products_contributing = best$n_products, raters_removed = paste("block raters:", best$raters),
  missing_handling = "complete block, no missing values", interpretation = cronbach$interpretation[1]))
cronbach$all_raters_fully_crossed_subset_exists <- any(rowSums(rated) == ncol(rated))

# Bootstrap CIs over products (percentile). Pairwise replications in which some
# rater pair loses all shared products are not computable (counted).
message("02: bootstrapping Cronbach's alpha")
set.seed(SEED)
boot_pair <- vapply(seq_len(N_BOOT), function(b) {
  idx <- sample.int(nrow(wide17), replace = TRUE)
  C <- cov(wide17[idx, keep], use = "pairwise.complete.obs")
  if (anyNA(C)) return(NA_real_)
  tryCatch(suppressWarnings(psych::alpha(C, n.obs = sum(rowSums(rated[idx, keep]) >= 2),
                                         check.keys = FALSE, warnings = FALSE)$total$raw_alpha),
           error = function(e) NA_real_)
}, numeric(1))
boot_block <- vapply(seq_len(N_BOOT), function(b) tryCatch(
  alpha_raw(x_best[sample.int(nrow(x_best), replace = TRUE), , drop = FALSE]), error = function(e) NA_real_), numeric(1))
boot_list <- list(boot_pair, boot_block)
cronbach$ci_low <- vapply(boot_list, function(x) unname(quantile(x, 0.025, na.rm = TRUE)), numeric(1))
cronbach$ci_high <- vapply(boot_list, function(x) unname(quantile(x, 0.975, na.rm = TRUE)), numeric(1))
cronbach$ci_type <- "percentile bootstrap, resampling products"
cronbach$n_boot <- N_BOOT
cronbach$n_boot_failed <- vapply(boot_list, function(x) sum(is.na(x)), integer(1))
cronbach$seed <- SEED
save_csv(cronbach, "cronbach_alpha", "supplement")

# Krippendorff's alpha (ordinal): agreement of single ratings, raters interchangeable.
message("02: Krippendorff's alpha", if (KRIPP_BOOT) paste0(" with bootstrap (", N_BOOT, " replications, slow)") else " (bootstrap skipped)")
rel_data <- t(wide17)  # raters x units; NA handled natively
ka <- irr::kripp.alpha(rel_data, method = "ordinal")$value
set.seed(SEED)
boot <- if (KRIPP_BOOT) vapply(seq_len(N_BOOT), function(b) {
  idx <- sample.int(ncol(rel_data), replace = TRUE)
  tryCatch(irr::kripp.alpha(rel_data[, idx], method = "ordinal")$value, error = function(e) NA_real_)
}, numeric(1)) else numeric(0)
krippendorff <- tibble(
  method = "ordinal", alpha = ka,
  ci_low = if (KRIPP_BOOT) quantile(boot, 0.025, na.rm = TRUE) else NA_real_,
  ci_high = if (KRIPP_BOOT) quantile(boot, 0.975, na.rm = TRUE) else NA_real_,
  ci_type = if (KRIPP_BOOT) "percentile bootstrap, resampling products" else "no bootstrap in this run (JRT_SKIP_KRIPP_BOOT)",
  n_boot = if (KRIPP_BOOT) N_BOOT else 0L, n_boot_failed = sum(is.na(boot)), seed = SEED,
  n_units = ncol(rel_data), n_pairable_units = sum(colSums(!is.na(rel_data)) >= 2), n_raters = nrow(rel_data),
  package = paste0("irr ", packageVersion("irr")),
  interpretation = "Agreement (consensus) of single ratings; raters treated as interchangeable.")
save_csv(krippendorff, "krippendorff_alpha", "supplement")

# ==============================================================================
# D. Reliability overview (all indices side by side, with what each refers to)
# ==============================================================================
rel <- rd("reliability_summary"); rel_ci <- rd("reliability_ci")
fmt <- function(x, d = 3) ifelse(is.na(x), "NA", formatC(as.numeric(x), digits = d, format = "f"))
big <- function(n) formatC(n, big.mark = ",", format = "d")
get_q <- function(key) rel$value[startsWith(rel$quantity, key)][1]
ci_txt <- function(lo, hi, what) sprintf("95%% CI [%s, %s] (%s)", fmt(lo), fmt(hi), what)
rel_ci_of <- function(q) { r <- rel_ci[rel_ci$quantity == q, ]; ci_txt(r$ci_low, r$ci_high, sprintf("%d parameter draws", r$n_draws)) }
cron_ci_of <- function(i) ci_txt(cronbach$ci_low[i], cronbach$ci_high[i],
  if (cronbach$n_boot_failed[i] > 0)
    sprintf("bootstrap, %s of %s replications computable, approximate", big(cronbach$n_boot[i] - cronbach$n_boot_failed[i]), big(cronbach$n_boot[i]))
  else sprintf("bootstrap, %s replications", big(cronbach$n_boot[i])))
marg_of <- function(m) marg$marginal_reliability[marg$model == m][1]
overview <- tibble(
  index = c("Krippendorff's alpha (ordinal)", "Cronbach's alpha (pairwise covariances)",
            "Cronbach's alpha (fully crossed block)", "GRM: empirical marginal reliability",
            "GRM: model-based marginal reliability", "GRM: median rel_post", "GRM: IQR rel_post",
            "M1 (rating-scale MFRM): marginal reliability", "M2 (partial-credit MFRM): marginal reliability",
            "M3 (GPCM): marginal reliability"),
  refers_to = c("consensus of single ratings", "consistency of the unweighted rater mean",
                "consistency of the unweighted rater mean (crossed subset)", "actual theta_hat (primary)",
                "hypothetical full panel", "precision per product", "precision per product",
                "comparison", "comparison", "comparison"),
  value = c(krippendorff$alpha, cronbach$raw_alpha[1], cronbach$raw_alpha[2],
            get_q("empirical_marginal_reliability"), get_q("model_based_marginal_reliability_mirt"),
            get_q("rel_post_median"), get_q("rel_post_iqr"), marg_of("M1_RSM"), marg_of("M2_PCM"), marg_of("M3_GPCM")),
  ci_or_note = c(
    if (KRIPP_BOOT) sprintf("95%% bootstrap CI [%s, %s], %s replications", fmt(krippendorff$ci_low), fmt(krippendorff$ci_high), big(krippendorff$n_boot)) else "no bootstrap in this run",
    sprintf("%s; %d raters; removed: %s", cron_ci_of(1), cronbach$n_raters[1],
            ifelse(cronbach$raters_removed[1] == "", "none", cronbach$raters_removed[1])),
    sprintf("%s; %s raters, %s products", cron_ci_of(2), cronbach$n_raters[2], cronbach$n_products_contributing[2]),
    paste0(rel_ci_of("empirical_marginal_reliability"), "; Var(theta)/(Var(theta)+mean(PSD^2))"),
    paste0(rel_ci_of("model_based_marginal_reliability"), "; mirt::marginal_rxx, all raters"),
    sprintf("first quartile %s, third quartile %s", fmt(get_q("rel_post_q1")), fmt(get_q("rel_post_q3"))),
    "", "", "", ""))
save_csv(overview, "reliability_overview", "supplement")

print(model_fit %>% select(model, software, logLik, npar, AIC, BIC, SABIC))
print(lr_tests %>% select(comparison, X2, df, df_expected_formula, p))
print(overview %>% select(index, value))
writeLines(c(paste("Run:", format(Sys.time()), " seed:", SEED, " quick:", QUICK), "", capture.output(sessionInfo())),
           file.path(DIRS$logs, "session_info.txt"))
message("02 comparison: done")
