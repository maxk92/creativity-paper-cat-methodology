# ============================================================
# 04 - Comparison: JRT as GPCM vs. MFRM (spec section 5)
# ============================================================
# Nested adjacent-category ladder, same data, all MML:
#   M1  RSM / MFRM   shared thresholds, rater shift, equal slopes   sirt::rm.facets
#   M2  PCM          rater-specific thresholds, equal slopes        mirt itemtype "Rasch"
#   M3  GPCM         rater-specific thresholds and slopes (= JRT)   mirt itemtype "gpcm"
# The GRM (cumulative family) is not part of the ladder; it is compared by
# information criteria only.
#
# Why M1 is fitted with rm.facets (decision 2026-10-22): mirt recodes each
# rater's observed categories, and its "rsm" refuses raters with different
# numbers of categories. Eight raters leave categories unused, and all 7
# categories are kept, so mirt's RSM is not estimable. rm.facets keeps every
# rater on the full 0-6 category set, which is the correctly specified RSM.
# mirt's "rsm" is still attempted so its outcome on the real data is recorded.
#
# Comparability of the likelihoods across software: rm.facets integrates on a
# fixed theta grid. M1 uses a fine grid (321 points on [-8, 8]), which reproduces
# mirt's RSM log-likelihood on data without category gaps (cross-check below,
# computed in this script on simulated data). The original call with the sirt
# default grid (30 points on [-9, 9]) is fitted as well and documented.
#
# Nesting with category gaps: an unused END category has probability 0 in the
# ML solution of M2, so mirt's M2 with fewer categories for that rater is the
# limit of the full-category PCM and M1 stays nested. A rater with an INTERNAL
# gap is rescored by mirt (categories above the gap move down), so for such a
# rater M1 is not strictly nested in M2 (flagged; R20 and R22 had internal gaps
# but are excluded by the minimum of MIN_RATINGS_PER_RATER ratings).
#
# Latent scale: latent mean 0 in all models. RSM and PCM estimate the latent
# variance (slopes 1); GPCM and GRM fix it to 1. M2 is nested in M3, df = J - 1.
#
# Outputs (results/comparison/): model_fit.csv, lr_tests.csv, theta_correlations.csv,
#   rater_parameters_by_model.csv, threshold_order.csv, discrimination_m3.csv,
#   discrimination_summary.csv, rater_fit_m1.csv, marginal_reliability.csv,
#   software_crosscheck.csv, mfrm_equivalence.md, model_*.rds, score_agreement.csv,
#   sensitivity_rater_exclusion.csv (GRM refitted on all raters, no SEs)
# SERVER: two mirt fits with SEs plus two rm.facets fits.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))
suppressPackageStartupMessages(library(sirt))

RMF_GRID_M1 <- seq(-8, 8, length.out = 321)      # M1 (comparable with mirt)
RMF_GRID_DEFAULT <- seq(-9, 9, length.out = 30)  # sirt default = original call

d <- load_design()
wide <- d$wide
long <- d$long
rated <- !is.na(wide)
raters <- colnames(wide)
J <- ncol(wide)
K <- K_CATEGORIES
N <- nrow(wide)
category_usage <- readr::read_csv(file.path(DIR_DATA, "category_usage.csv"), show_col_types = FALSE)
internal_gap_raters <- category_usage$rater_id[category_usage$internal_gap]

fit_error <- function(label, e) {
  msg <- gsub("\\s+", " ", conditionMessage(e))
  WARNINGS[[length(WARNINGS) + 1]] <<- data.frame(context = label, warning = paste("ERROR:", msg))
  structure(list(error = msg), class = "fit_error")
}
is_fit <- function(m) !inherits(m, "fit_error")

# --- M1: rm.facets ---------------------------------------------------------------------
# Same long data (internal coding 0-6), one item (creativity), raters as facet.
# Model (?sirt::rm.facets): P(X_pr = k | theta_p) ∝ exp(k theta_p - k b_r - tau_k),
# theta_p ~ N(0, sigma^2), sigma estimated, MML via EM on the grid theta.k.
# Settings (= the defaults of the original call, written out): est.b.rater = TRUE,
# est.a.item = FALSE, est.a.rater = FALSE, rater_item_int = FALSE, est.mean = FALSE,
# b.rater.center = 2 (severities sum to zero).
# Rows are ordered as in the wide matrix so the person table lines up with it.
rmf_long <- long %>%
  mutate(product_id = factor(product_id, levels = rownames(wide))) %>%
  arrange(product_id, rater_id)
fit_rm_facets <- function(theta_k, label) {
  message("04: fitting sirt::rm.facets (", label, ")")
  tryCatch(with_warnings(
    sirt::rm.facets(dat = data.frame(creativity = rmf_long$rating_internal),
                    pid = as.character(rmf_long$product_id), rater = rmf_long$rater_id,
                    theta.k = theta_k, est.b.rater = TRUE, est.a.item = FALSE,
                    est.a.rater = FALSE, rater_item_int = FALSE, est.mean = FALSE,
                    b.rater.center = 2),
    paste("sirt::rm.facets", label)), error = function(e) fit_error(paste("rm.facets", label), e))
}
m1 <- fit_rm_facets(RMF_GRID_M1, "M1, 321-point grid")
mfrm_default <- fit_rm_facets(RMF_GRID_DEFAULT, "original call, sirt default grid")
if (!is_fit(m1)) stop("M1 (rm.facets) failed: ", m1$error)
saveRDS(m1, file.path(DIR_CMP, "model_M1_rm_facets.rds"))
if (is_fit(mfrm_default)) saveRDS(mfrm_default, file.path(DIR_CMP, "model_rm_facets_default_grid.rds"))

# Same data basis as the mirt models (spec 5).
m1_person <- m1$person[match(rownames(wide), as.character(m1$person$pid)), ]
stopifnot(nrow(m1$person) == N, !anyNA(m1_person$EAP),
          sum(m1$rater$N) == sum(rated), setequal(as.character(m1$rater$rater), raters))

# Free parameters of the RSM with J raters and K categories: J - 1 rater
# locations (sum zero) + K - 1 thresholds + latent variance = J + K - 1.
# rm.facets' own count (ic$np) is reported alongside.
m1_npar <- J + K - 1
m1_ll <- as.numeric(logLik(m1))
m1_b <- setNames(m1$rater$b, as.character(m1$rater$rater))[raters]
m1_tau <- as.numeric(m1$tau.item[1, ])
m1_sigma2 <- m1$sigma^2

rsm_probs <- function(theta, b) {  # matrix length(theta) x K
  k <- 0:(K - 1)
  e <- exp(outer(theta, k) - matrix(k * b + c(0, m1_tau), length(theta), K, byrow = TRUE))
  e / rowSums(e)
}

# --- mirt models -------------------------------------------------------------------------
try_mirt <- function(itemtype, label) {
  message("04: fitting ", label, " (", itemtype, ")")
  tryCatch(fit_mirt(wide, itemtype, label), error = function(e) fit_error(paste("mirt fit", label), e))
}
mirt_rsm <- try_mirt("rsm", "mirt rsm (record only)")
models <- list(M2_PCM = try_mirt("Rasch", "M2_PCM"), M3_GPCM = try_mirt("gpcm", "M3_GPCM"))
for (nm in names(models)) if (is_fit(models[[nm]])) {
  saveRDS(models[[nm]], file.path(DIR_CMP, paste0("model_", nm, ".rds")))
}
grm <- readRDS(file.path(DIR_GRM, "model.rds"))
assert_same_data(grm, wide, "GRM")
mirt_models <- Filter(is_fit, c(models, list(GRM = grm)))
n_check <- vapply(mirt_models, function(m) c(nrow(extract.mirt(m, "data")),
                                             sum(!is.na(extract.mirt(m, "data")))), numeric(2))
stopifnot(all(n_check[1, ] == N), all(n_check[2, ] == sum(rated)))

# --- model fit and information criteria ---------------------------------------------------
ic_row <- function(model, ll, npar, ...) {
  data.frame(model = model, logLik = ll, npar = npar,
             AIC = -2 * ll + 2 * npar, BIC = -2 * ll + npar * log(N),
             SABIC = -2 * ll + npar * log((N + 2) / 24), n_products = N,
             n_ratings = sum(rated), ..., stringsAsFactors = FALSE)
}
model_fit <- bind_rows(
  ic_row("M1_RSM", m1_ll, m1_npar, software = "sirt::rm.facets",
         status = "estimated", family = "adjacent category",
         converged = m1$iter < 1000, iterations = m1$iter,
         note = sprintf("grid %d points on [%g, %g]; rm.facets ic$np = %d", length(RMF_GRID_M1),
                        min(RMF_GRID_M1), max(RMF_GRID_M1), m1$ic$np)),
  bind_rows(lapply(names(mirt_models), function(nm) {
    convergence_row(mirt_models[[nm]], nm) %>%
      mutate(software = "mirt", status = "estimated",
             family = ifelse(nm == "GRM", "cumulative (not in LR ladder)", "adjacent category"))
  })),
  data.frame(model = "mirt_rsm", software = "mirt",
             status = if (is_fit(mirt_rsm)) "estimated (not used)" else
               paste("not estimable:", mirt_rsm$error))
)
# Differences to the best model on each criterion (effect sizes for model choice).
est <- model_fit$status == "estimated"
for (ic in c("AIC", "BIC", "SABIC")) {
  model_fit[[paste0("delta_", ic)]] <- ifelse(est, model_fit[[ic]] - min(model_fit[[ic]][est]), NA_real_)
}
save_csv(model_fit, DIR_CMP, "model_fit")

# --- LR tests -----------------------------------------------------------------------------
npar_of <- function(nm) model_fit$npar[model_fit$model == nm]
ll_of <- function(nm) model_fit$logLik[model_fit$model == nm]
lr_row <- function(a, b, label, df_formula, note) {
  if (!all(c(a, b) %in% model_fit$model[model_fit$status == "estimated"])) {
    return(data.frame(comparison = label, df_expected_formula = df_formula,
                      note = "not computed: a model of the pair is not estimable"))
  }
  x2 <- 2 * (ll_of(b) - ll_of(a))
  df <- npar_of(b) - npar_of(a)
  data.frame(comparison = label, logLik_restricted = ll_of(a), logLik_general = ll_of(b),
             X2 = x2, df = df, p = pchisq(x2, df, lower.tail = FALSE),
             df_expected_formula = df_formula, df_matches_formula = df == df_formula,
             note = note)
}
lr_tests <- bind_rows(
  lr_row("M1_RSM", "M2_PCM", "M1 vs M2: rater-specific thresholds", (J - 1) * (K - 2),
         paste0("Across software (rm.facets vs mirt). df differ from (J-1)(K-2) when raters ",
                "leave END categories unused (fewer step parameters in M2). ",
                if (length(internal_gap_raters)) paste0("Raters with internal category gaps (",
                  paste(internal_gap_raters, collapse = ", "), ") make the nesting approximate.")
                else "No rater has an internal category gap, so M1 is nested in M2.")),
  lr_row("M2_PCM", "M3_GPCM", "M2 vs M3: rater-specific discriminations", J - 1, "mirt, same object")
)
# Cross-check with mirt's own LR test for M2 vs M3.
if (all(c("M2_PCM", "M3_GPCM") %in% names(mirt_models))) {
  av <- anova(mirt_models$M2_PCM, mirt_models$M3_GPCM)
  stopifnot(abs(av$X2[2] - lr_tests$X2[2]) < 1e-6, av$df[2] == lr_tests$df[2])
}
save_csv(lr_tests, DIR_CMP, "lr_tests")

# --- theta estimates -----------------------------------------------------------------------
eap <- lapply(mirt_models, function(m)
  fscores(m, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE))
theta_tab <- as_tibble(c(list(M1_RSM = m1_person$EAP), lapply(eap, function(f) f[, "F1"])))
if (is_fit(mfrm_default)) {
  theta_tab$rm_facets_default_grid <- mfrm_default$person$EAP[match(rownames(wide),
                                                                    as.character(mfrm_default$person$pid))]
}
theta_cor <- bind_rows(lapply(c("pearson", "spearman"), function(meth) {
  as_tibble(cor(theta_tab, method = meth), rownames = "model") %>% mutate(method = meth, .before = 1)
}))
save_csv(theta_cor, DIR_CMP, "theta_correlations")

# How much the product ranking changes between models (reference: GRM).
# Percentile ranks in [0, 1]; quintiles 1-5 of each model's own score distribution.
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
if ("GRM" %in% names(theta_tab)) {
  score_agreement <- bind_rows(lapply(intersect(c("M1_RSM", "M2_PCM", "M3_GPCM"), names(theta_tab)),
    function(m) rank_change(theta_tab[[m]], theta_tab$GRM) %>% mutate(model = m, reference = "GRM", .before = 1)))
  save_csv(score_agreement, DIR_CMP, "score_agreement")
}

# --- sensitivity: rater exclusion -----------------------------------------------------------
# The final data exclude raters with fewer than MIN_RATINGS_PER_RATER ratings
# (01_data_design.R). Here the GRM is refitted on ALL raters of the cleaned input
# (same settings, no SEs) and compared with the final GRM: scores of the common
# products, reliability, and the parameters of the common raters.
raw_all <- readr::read_csv(INPUT_CSV, show_col_types = FALSE,
                           col_types = cols(action_id = "c", rater_id = "c", .default = "?"))
wide_all_df <- raw_all %>%
  transmute(product_id = action_id, rater_id,
            rating_internal = as.integer(rating_numeric) - SCALE_MIN) %>%
  pivot_wider(names_from = rater_id, values_from = rating_internal) %>%
  arrange(product_id)
raters_all <- rater_order(setdiff(names(wide_all_df), "product_id"))
wide_all <- as.matrix(wide_all_df[, raters_all])
storage.mode(wide_all) <- "integer"
rownames(wide_all) <- wide_all_df$product_id
excluded_raters <- readr::read_csv(file.path(DIR_DATA, "excluded_raters.csv"), show_col_types = FALSE)
stopifnot(setequal(setdiff(raters_all, raters), excluded_raters$rater_id))

message("04: fitting the GRM on all raters (sensitivity)")
grm_all <- fit_mirt(wide_all, "graded", "GRM all raters (sensitivity)", SE = FALSE)
fs_all <- fscores(grm_all, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE)
fs_fin <- eap$GRM
common <- intersect(rownames(wide), rownames(wide_all))
th_fin <- fs_fin[match(common, rownames(wide)), "F1"]
th_all <- fs_all[match(common, rownames(wide_all)), "F1"]
emp_rel <- function(fs) var(fs[, "F1"]) / (var(fs[, "F1"]) + mean(fs[, "SE_F1"]^2))
a_of <- function(m) vapply(raters, function(r) coef(m, IRTpars = TRUE)[[r]][1, "a"], numeric(1))
a_diff <- a_of(grm_all) - a_of(grm)
rc <- rank_change(th_all, th_fin)
sensitivity <- tibble(
  quantity = c("n_raters", "n_ratings", "n_products", "excluded_raters",
               "empirical_marginal_reliability", "model_based_marginal_reliability",
               "theta_pearson_common_products", "theta_spearman_common_products",
               "theta_mean_abs_diff", "theta_max_abs_diff",
               "share_products_changing_quintile", "a_max_abs_diff_common_raters",
               "a_pearson_common_raters"),
  final_data = c(ncol(wide), sum(rated), nrow(wide), "", emp_rel(fs_fin), marginal_rxx(grm),
                 rc$pearson, rc$spearman, mean(abs(th_all - th_fin)), max(abs(th_all - th_fin)),
                 rc$share_products_changing_quintile, max(abs(a_diff)),
                 cor(a_of(grm_all), a_of(grm))) %>% as.character(),
  all_raters = c(ncol(wide_all), sum(!is.na(wide_all)), nrow(wide_all),
                 paste(excluded_raters$rater_id, collapse = ";"), emp_rel(fs_all),
                 marginal_rxx(grm_all), rep("", 7)) %>% as.character(),
  note = c(rep("", 4), "Var(theta)/(Var(theta)+mean(PSD^2))", "mirt::marginal_rxx (hypothetical full panel)",
           rep(sprintf("all-raters vs final GRM, %d common products", length(common)), 5),
           rep(sprintf("all-raters vs final GRM, %d common raters", length(raters)), 2))
)
save_csv(sensitivity, DIR_CMP, "sensitivity_rater_exclusion")

# --- rater parameters by model --------------------------------------------------------------
pars_long <- function(m, nm) {
  cf <- coef(m, IRTpars = TRUE, printSE = TRUE)
  bind_rows(lapply(c(raters, "GroupPars"), function(r) {
    x <- cf[[r]]
    tibble(model = nm, rater_id = ifelse(r == "GroupPars", "(group)", r),
           parameter = colnames(x), estimate = x["par", ],
           se = if ("SE" %in% rownames(x)) x["SE", ] else NA_real_)
  }))
}
rater_pars <- bind_rows(
  tibble(model = "M1_RSM", rater_id = as.character(m1$rater$rater), parameter = "b_rater",
         estimate = m1$rater$b, se = m1$se.b.rater),
  tibble(model = "M1_RSM", rater_id = "(shared)", parameter = paste0("tau", seq_along(m1_tau)),
         estimate = m1_tau, se = as.numeric(m1$se.tau.item[1, ])),
  tibble(model = "M1_RSM", rater_id = "(group)", parameter = "latent_variance",
         estimate = m1_sigma2, se = NA_real_),
  bind_rows(lapply(names(mirt_models), function(nm) pars_long(mirt_models[[nm]], nm)))
)
save_csv(rater_pars, DIR_CMP, "rater_parameters_by_model")

# Threshold order in M2 and M3 (IRT metric). Unordered steps are flagged.
threshold_order <- rater_pars %>%
  filter(model %in% c("M2_PCM", "M3_GPCM"), grepl("^b\\d+$", parameter)) %>%
  group_by(model, rater_id) %>%
  summarise(n_steps = n(), ordered = all(diff(estimate) > 0),
            n_reversals = sum(diff(estimate) <= 0),
            steps = paste(sprintf("%.2f", estimate), collapse = ";"), .groups = "drop")
save_csv(threshold_order, DIR_CMP, "threshold_order")

discrimination <- rater_pars %>%
  filter(model == "M3_GPCM", parameter == "a") %>%
  left_join(category_usage %>% select(rater_id, n_ratings), by = "rater_id") %>%
  arrange(estimate)
save_csv(discrimination, DIR_CMP, "discrimination_m3")
if (nrow(discrimination)) {
  save_csv(tibble(statistic = c("min", "q1", "median", "q3", "max", "ratio_max_min", "sd"),
                  value = c(quantile(discrimination$estimate),
                            max(discrimination$estimate) / min(discrimination$estimate),
                            sd(discrimination$estimate))),
           DIR_CMP, "discrimination_summary")
}

# --- rater fit in M1 ---------------------------------------------------------------------------
# Rasch mean squares at the EAP estimate of each product: z = (x - E) / sqrt(W),
# outfit = mean(z^2), infit = sum((x - E)^2) / sum(W) per rater.
th1 <- m1$person$EAP[match(as.character(rmf_long$product_id), as.character(m1$person$pid))]
b_obs <- m1_b[rmf_long$rater_id]
k <- 0:(K - 1)
P_obs <- t(vapply(seq_along(th1), function(i) rsm_probs(th1[i], b_obs[i]), numeric(K)))
E_obs <- as.vector(P_obs %*% k)
W_obs <- as.vector(P_obs %*% k^2) - E_obs^2
fit_m1 <- tibble(rater_id = rmf_long$rater_id, x = rmf_long$rating_internal, E = E_obs, W = W_obs) %>%
  group_by(rater_id) %>%
  summarise(n_ratings = n(), outfit = mean((x - E)^2 / W), infit = sum((x - E)^2) / sum(W),
            .groups = "drop") %>%
  left_join(category_usage %>% select(rater_id, missing_categories, internal_gap), by = "rater_id") %>%
  mutate(flag = infit < 0.7 | infit > 1.3 | outfit < 0.7 | outfit > 1.3,
         source = "M1 (rm.facets), mean squares at EAP") %>%
  mutate(rater_id = factor(rater_id, levels = raters)) %>% arrange(rater_id)
save_csv(fit_m1, DIR_CMP, "rater_fit_m1")

# --- marginal reliability (comparison only) ------------------------------------------------------
# Posterior-based convention on each model's own latent scale theta ~ N(0, s2):
#   rel(theta) = s2 I(theta) / (s2 I(theta) + 1), averaged over N(0, s2).
# For s2 = 1 this is I/(I+1) and equals mirt::marginal_rxx (reported as a check;
# marginal_rxx assumes a standard normal density, so it is not used for s2 != 1).
z <- THETA_GRID
w <- normal_weights(z)
marginal_from_info <- function(info, s2) sum(w * s2 * info / (s2 * info + 1)) / sum(w)
m1_info <- rowSums(vapply(raters, function(r) {   # RSM item information = Var(X | theta)
  p <- rsm_probs(sqrt(m1_sigma2) * z, m1_b[[r]])
  as.vector(p %*% k^2) - as.vector(p %*% k)^2
}, numeric(length(z))))
marg <- bind_rows(
  tibble(model = "M1_RSM", latent_variance = m1_sigma2,
         marginal_reliability = marginal_from_info(m1_info, m1_sigma2),
         marginal_rxx_mirt = NA_real_,
         empirical_rxx = var(m1_person$EAP) / (var(m1_person$EAP) + mean(m1_person$SE.EAP^2))),
  bind_rows(lapply(names(mirt_models), function(nm) {
    m <- mirt_models[[nm]]
    s2 <- as.numeric(coef(m, simplify = TRUE)$cov)
    tibble(model = nm, latent_variance = s2,
           marginal_reliability = marginal_from_info(rowSums(rater_information(m, sqrt(s2) * z)), s2),
           marginal_rxx_mirt = if (abs(s2 - 1) < 1e-8) marginal_rxx(m) else NA_real_,
           empirical_rxx = unname(empirical_rxx(eap[[nm]])))
  }))
)
save_csv(marg, DIR_CMP, "marginal_reliability")

# --- software cross-check on simulated data without category gaps -----------------------------------
# Shows that rm.facets (M1 grid) and mirt "rsm" give the same log-likelihood and
# rater locations when mirt's RSM is estimable, which justifies the cross-software
# M1-vs-M2 LR test. Small simulation, seconds.
set.seed(SEED)
sim_J <- 6; sim_N <- 2000
# Direct RSM simulation with the rm.facets parametrisation and a latent SD close
# to that of the real data: P(X = k | theta) ∝ exp(k theta - k b_r - tau_k).
sim_tau <- cumsum(seq(-1.2, 1.2, length.out = K - 1))
sim_b <- seq(-0.4, 0.4, length.out = sim_J)
sim_theta <- rnorm(sim_N, 0, 0.7)
sim <- vapply(sim_b, function(b) {
  e <- exp(outer(sim_theta, 0:(K - 1)) - matrix((0:(K - 1)) * b + c(0, sim_tau), sim_N, K, byrow = TRUE))
  apply(e / rowSums(e), 1, function(p) sample(0:(K - 1), 1, prob = p))
}, numeric(sim_N))
colnames(sim) <- paste0("S", seq_len(sim_J))
sim[matrix(runif(sim_N * sim_J) < 0.6, sim_N)] <- NA
sim <- sim[rowSums(!is.na(sim)) > 0, ]
stopifnot(all(apply(sim, 2, function(x) length(unique(na.omit(x)))) == K))
sim_mirt <- mirt(sim, 1, itemtype = "rsm", method = MIRT_METHOD, quadpts = MIRT_QUADPTS, verbose = FALSE)
idx <- which(!is.na(sim), arr.ind = TRUE)
sim_rmf <- sirt::rm.facets(dat = data.frame(c = sim[idx]), pid = idx[, 1], rater = idx[, 2],
                           theta.k = RMF_GRID_M1)
crosscheck <- tibble(
  quantity = c("logLik_mirt_rsm", "logLik_rm_facets_M1_grid", "abs_difference",
               "cor_rater_locations (mirt c vs rm.facets b)", "latent_variance_mirt",
               "latent_variance_rm_facets"),
  value = c(extract.mirt(sim_mirt, "logLik"), as.numeric(logLik(sim_rmf)),
            abs(extract.mirt(sim_mirt, "logLik") - as.numeric(logLik(sim_rmf))),
            cor(coef(sim_mirt, simplify = TRUE)$items[, "c"], sim_rmf$rater$b),
            as.numeric(coef(sim_mirt, simplify = TRUE)$cov), sim_rmf$sigma^2))
save_csv(crosscheck, DIR_CMP, "software_crosscheck")

# --- MFRM equivalence report ------------------------------------------------------------------------
fmt <- function(x, d = 3) ifelse(is.na(x), "NA", formatC(as.numeric(x), digits = d, format = "f"))
cc <- setNames(crosscheck$value, crosscheck$quantity)
eq_lines <- c(
  "# The MFRM: `sirt::rm.facets` as M1",
  "",
  "_Generated by `R/04_model_comparison.R`. Do not edit by hand._",
  "",
  "## Parametrisation of the existing MFRM",
  "",
  paste0("The original call (`rm.facets(dat, pid, rater)`, formerly in `02_creativity_ratings_R.qmd`) ",
         "uses the package defaults. From `?sirt::rm.facets` (sirt ", packageVersion("sirt"), "):"),
  "",
  "- Model: P(X_pr = k | θ_p) ∝ exp(a_i a_r k θ_p − k b_r − τ_k), checked numerically against the fitted category probabilities.",
  "- `est.b.rater = TRUE`: rater severities b_r (higher = stricter), centred to sum to zero (`b.rater.center = 2`).",
  "- `est.a.item = FALSE`, `est.a.rater = FALSE`: all slopes 1 (Rasch).",
  "- `rater_item_int = FALSE` with one item: one set of thresholds τ_k shared by all raters (rating scale structure).",
  "- `est.mean = FALSE`: latent mean 0; the latent SD σ is estimated.",
  "- Estimation: marginal maximum likelihood via EM, integration on the fixed grid `theta.k` (default 30 points on [−9, 9]).",
  "- Identification: mean of θ is 0, Σ b_r = 0, slopes are 1.",
  "- Every rater keeps the full 0–6 category set (no recoding per rater), so unused categories do not shift thresholds.",
  "",
  "This is the rating scale model with a rater shift, i.e. M1. Its free parameters are J − 1 + K − 1 + 1 = J + K − 1",
  sprintf("(%d here); rm.facets' own count `ic$np` is %d.", m1_npar, m1$ic$np),
  "",
  "## Why M1 is fitted with rm.facets, not mirt",
  "",
  paste0("mirt `itemtype = \"rsm\"` on the shared matrix: ",
         if (is_fit(mirt_rsm)) "estimated (not used, see AUDIT.md)." else paste0("**not estimable** — `", mirt_rsm$error, "`.")),
  "mirt recodes each rater's observed categories, and 8 raters leave categories unused (`results/data/category_usage.csv`);",
  "the author decided to keep all 7 categories (2026-10-22).",
  "",
  "## Software cross-check (simulated data without category gaps)",
  "",
  "| Quantity | Value |", "|---|---|",
  sprintf("| %s | %s |", crosscheck$quantity, fmt(crosscheck$value, 4)),
  "",
  "With the M1 grid (321 points on [−8, 8]) both packages give the same marginal log-likelihood up to",
  "integration error, so M1 (rm.facets) and M2 (mirt) likelihoods can be compared in an LR test.",
  "",
  "## Original call (default grid) vs. M1 (fine grid), real data",
  ""
)
if (is_fit(mfrm_default)) {
  eq_lines <- c(eq_lines,
    "| Quantity | Original call (30 points, [−9, 9]) | M1 (321 points, [−8, 8]) |", "|---|---|---|",
    sprintf("| logLik | %s | %s |", fmt(logLik(mfrm_default), 2), fmt(m1_ll, 2)),
    sprintf("| latent variance | %s | %s |", fmt(mfrm_default$sigma^2), fmt(m1_sigma2)),
    sprintf("| EAP reliability (sirt) | %s | %s |", fmt(mfrm_default$EAP.rel), fmt(m1$EAP.rel)),
    "",
    sprintf("- Correlation of rater severities: %s", fmt(cor(mfrm_default$rater$b, m1$rater$b))),
    sprintf("- Correlation of θ̂ (EAP): Pearson %s, Spearman %s",
            fmt(cor(theta_tab$M1_RSM, theta_tab$rm_facets_default_grid)),
            fmt(cor(theta_tab$M1_RSM, theta_tab$rm_facets_default_grid, method = "spearman"))),
    "",
    "Differences come only from the integration grid (same model, data and identification).")
} else {
  eq_lines <- c(eq_lines, paste0("The original call failed: `", mfrm_default$error, "`."))
}
eq_lines <- c(eq_lines, "", if (length(internal_gap_raters))
  sprintf("Raters with internal category gaps (%s): the M1-vs-M2 test is approximate for them, because mirt rescores their categories in M2.",
          paste(internal_gap_raters, collapse = ", ")) else
  "No rater has an internal category gap, so M1 is strictly nested in M2 (end gaps only).")
writeLines(eq_lines, file.path(DIR_CMP, "mfrm_equivalence.md"))

print(model_fit %>% select(any_of(c("model", "software", "status", "logLik", "npar", "AIC", "BIC", "SABIC"))))
print(lr_tests %>% select(any_of(c("comparison", "X2", "df", "df_expected_formula", "p"))))
write_warnings("04_model_comparison")
write_session_info("04_model_comparison")
message("04 model comparison: done")
