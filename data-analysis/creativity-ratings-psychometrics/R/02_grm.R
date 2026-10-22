# ============================================================
# 02 - Central model: JRT as a graded response model, MML (spec section 3)
# ============================================================
# Raters = items, products = persons:
#   P(X_nj >= k | theta_n) = 1 / (1 + exp(-a_j (theta_n - b_jk))),  theta ~ N(0, 1)
# Estimation: mirt::mirt(wide, 1, itemtype = "graded"), MML via EM with
# fixed-quadrature integration (settings in jrt_functions.R). All a_j and b_jk
# free, latent mean 0 and variance 1 fixed (mirt default for "graded"); no
# further constraints.
#
# Outputs (results/grm/):
#   model.rds, convergence.csv, rater_parameters.csv, rater_parameters_slope_intercept.csv,
#   rater_fit.csv, q3.csv, global_fit.csv, figures/grm_category_response_functions.*
# SERVER: S-X2 multiple imputation and M2/C2 are the slow parts.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))

N_IMPUTATIONS <- if (SMOKE) 2L else 20L
Q3_MIN_OVERLAP <- 3L   # below this, a pairwise Q3 is not computed
Q3_LOW_OVERLAP <- 30L  # pairs below this are flagged as unstable

d <- load_design()
wide <- d$wide
rated <- !is.na(wide)
category_usage <- readr::read_csv(file.path(DIR_DATA, "category_usage.csv"), show_col_types = FALSE)
overlap <- as.matrix(readr::read_csv(file.path(DIR_DATA, "rater_overlap.csv"),
                                     show_col_types = FALSE)[, -1])
rownames(overlap) <- colnames(overlap)

# --- fit ------------------------------------------------------------------------
message("02 GRM: fitting mirt graded model (", nrow(wide), " products x ", ncol(wide), " raters)")
mod <- fit_mirt(wide, "graded", "GRM")
saveRDS(mod, file.path(DIR_GRM, "model.rds"))

# Identification check: latent mean/variance fixed, no extra constraints.
gp <- coef(mod, simplify = TRUE)$means
gv <- coef(mod, simplify = TRUE)$cov
stopifnot(abs(gp) < 1e-8, abs(gv - 1) < 1e-8, length(extract.mirt(mod, "constrain")) == 0)

conv <- convergence_row(mod, "GRM")
save_csv(conv, DIR_GRM, "convergence")
if (!conv$converged) warning("GRM did not converge - results are not usable.")
if (isFALSE(conv$information_matrix_pd)) warning("GRM information matrix is not positive definite.")
message(sprintf("  converged=%s after %d EM cycles; information matrix PD=%s",
                conv$converged, conv$iterations, conv$information_matrix_pd))

# --- parameters in IRT metric, with SEs -------------------------------------------------
# mirt's b_k refer to the boundaries between the categories a rater actually used
# (mirt recodes observed categories to consecutive integers). The column
# `category_boundaries` states which original categories each b_k separates, so
# thresholds of raters with category gaps are not misread.
raters <- colnames(wide)
cf_irt <- coef(mod, IRTpars = TRUE, printSE = TRUE)
cf_si <- coef(mod, IRTpars = FALSE, printSE = TRUE)
max_b <- K_CATEGORIES - 1L

par_rows <- lapply(raters, function(r) {
  m <- cf_irt[[r]]
  est <- m["par", ]; se <- if ("SE" %in% rownames(m)) m["SE", ] else rep(NA_real_, length(est))
  b_est <- est[grepl("^b", names(est))]; b_se <- se[grepl("^b", names(se))]
  used <- sort(unique(d$long$rating[d$long$rater_id == r]))
  bounds <- paste0(head(used, -1), "|", tail(used, -1))
  out <- data.frame(rater_id = r, a = est[["a"]], a_se = se[["a"]], n_thresholds = length(b_est),
                    category_boundaries = paste(bounds, collapse = ";"), stringsAsFactors = FALSE)
  for (k in seq_len(max_b)) {
    out[[paste0("b", k)]] <- if (k <= length(b_est)) b_est[[k]] else NA_real_
    out[[paste0("b", k, "_se")]] <- if (k <= length(b_se)) b_se[[k]] else NA_real_
  }
  out
})
rater_pars <- do.call(rbind, par_rows) %>%
  left_join(category_usage %>% select(rater_id, n_ratings, n_categories_used, missing_categories,
                                      internal_gap, end_gap),
            by = "rater_id") %>%
  mutate(
    thresholds_ordered = apply(across(matches("^b\\d$")), 1, function(b) {
      b <- b[!is.na(b)]; all(diff(b) > 0)
    }),
    max_abs_b = apply(across(matches("^b\\d$")), 1, function(b) max(abs(b), na.rm = TRUE)),
    flag_a_gt_4 = a > 4,
    flag_abs_b_gt_5 = max_abs_b > 5,
    flag_missing_se = is.na(a_se),
    plausibility_note = case_when(
      flag_a_gt_4 | flag_abs_b_gt_5 ~ paste0("extreme parameter; n_ratings=", n_ratings,
                                             ", categories used=", n_categories_used),
      internal_gap ~ "internal category gap: b_k compare different boundaries than for other raters",
      TRUE ~ "")
  )
save_csv(rater_pars, DIR_GRM, "rater_parameters")

si_rows <- lapply(raters, function(r) {
  m <- cf_si[[r]]
  data.frame(rater_id = r, parameter = colnames(m), estimate = m["par", ],
             se = if ("SE" %in% rownames(m)) m["SE", ] else NA_real_, row.names = NULL)
})
save_csv(do.call(rbind, si_rows), DIR_GRM, "rater_parameters_slope_intercept")
message(sprintf("  extreme parameters: a>4: %d, |b|>5: %d raters",
                sum(rater_pars$flag_a_gt_4), sum(rater_pars$flag_abs_b_gt_5)))

# --- EAP scores (used for Q3 and fit; the full product table is written in 03) ---
fs <- fscores(mod, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE)
theta_eap <- fs[, "F1", drop = FALSE]

# --- rater fit --------------------------------------------------------------------------
# (a) Infit/outfit on the observed ratings (mirt computes them with missing data).
fit_infit <- with_warnings(itemfit(mod, fit_stats = "infit", Theta = theta_eap, method = "EAP"),
                           "itemfit infit/outfit")

# (b) S-X2 needs complete data. mirt 1.46 no longer has an `impute` argument
# (the code path is disabled internally), so the multiple imputation is done
# explicitly: draw plausible values, impute the missing ratings from the fitted
# model, evaluate S-X2 on the completed data with ALL parameters fixed at the
# estimates, and pool by averaging S-X2 and df over imputations (the pooling
# rule of the former mirt `impute` option). With ~90% of the matrix missing, the
# completed data are mostly model-generated, so S-X2 is strongly conservative
# (biased towards fit). It is reported, but not as primary evidence.
sx2_pooled <- tryCatch({
  sv <- mod2values(mod)
  sv$est <- FALSE
  set.seed(SEED)
  imps <- lapply(seq_len(N_IMPUTATIONS), function(m) {
    pv <- fscores(mod, method = "EAP", plausible.draws = 1, verbose = FALSE)
    dat_m <- with_warnings(imputeMissing(mod, pv), "imputeMissing")
    mod_m <- with_warnings(
      mirt(dat_m, 1, itemtype = "graded", pars = sv, TOL = NaN, quadpts = MIRT_QUADPTS,
           verbose = FALSE), "fixed-parameter refit on imputed data")
    f <- with_warnings(itemfit(mod_m, fit_stats = "S_X2"), "itemfit S_X2 (imputed)")
    data.frame(imputation = m, rater_id = f$item, S_X2 = f$S_X2, df = f$df.S_X2)
  })
  do.call(rbind, imps) %>%
    group_by(rater_id) %>%
    summarise(S_X2_sd_over_imputations = sd(S_X2), S_X2 = mean(S_X2), df_S_X2 = mean(df),
              .groups = "drop") %>%
    mutate(p_S_X2 = pchisq(S_X2, df_S_X2, lower.tail = FALSE),
           RMSEA_S_X2 = sqrt(pmax(S_X2 - df_S_X2, 0) / (df_S_X2 * (nrow(wide) - 1))))
}, error = function(e) {
  warning("S-X2 via imputation failed: ", conditionMessage(e))
  data.frame(rater_id = raters, S_X2 = NA_real_, df_S_X2 = NA_real_,
             S_X2_sd_over_imputations = NA_real_, p_S_X2 = NA_real_, RMSEA_S_X2 = NA_real_)
})

rater_fit <- fit_infit %>%
  rename(rater_id = item) %>%
  left_join(sx2_pooled, by = "rater_id") %>%
  left_join(category_usage %>% select(rater_id, n_ratings), by = "rater_id") %>%
  mutate(n_imputations = N_IMPUTATIONS, imputation_seed = SEED,
         share_cells_imputed = mean(!rated),
         flag_infit = infit < 0.7 | infit > 1.3,
         flag_outfit = outfit < 0.7 | outfit > 1.3)
save_csv(rater_fit, DIR_GRM, "rater_fit")

# --- local dependence: Q3 ------------------------------------------------------------------
# Yen's Q3 = correlation of the residuals (observed - expected | EAP theta) of two
# raters, over the products both rated (pairwise; same definition as
# mirt::residuals(type = "Q3"), which uses na.omit per pair). Computed directly so
# that pairs with almost no overlap can be skipped instead of producing errors.
obs_int <- extract.mirt(mod, "data")  # mirt's internal (recoded) categories
resid_mat <- vapply(seq_along(raters), function(j) {
  obs_int[, j] - expected.item(extract.item(mod, j), theta_eap)
}, numeric(nrow(wide)))
colnames(resid_mat) <- raters
q3_rows <- list()
for (i in seq_along(raters)) for (j in seq_along(raters)) if (i < j) {
  both <- rated[, i] & rated[, j]
  n_common <- sum(both)
  q3 <- if (n_common >= Q3_MIN_OVERLAP &&
            sd(resid_mat[both, i]) > 0 && sd(resid_mat[both, j]) > 0)
    cor(resid_mat[both, i], resid_mat[both, j]) else NA_real_
  q3_rows[[length(q3_rows) + 1]] <- data.frame(rater_1 = raters[i], rater_2 = raters[j],
                                               n_common = n_common, q3 = q3)
}
q3 <- do.call(rbind, q3_rows)
q3_mean <- mean(q3$q3, na.rm = TRUE)
q3 <- q3 %>%
  mutate(q3_minus_mean = q3 - q3_mean,
         overlap_flag = case_when(n_common < Q3_MIN_OVERLAP ~ "not computable",
                                  n_common < Q3_LOW_OVERLAP ~ "low overlap (unstable)",
                                  TRUE ~ ""),
         flag_q3 = !is.na(q3) & n_common >= Q3_LOW_OVERLAP & abs(q3_minus_mean) > 0.2)
stopifnot(all(q3$n_common == overlap[cbind(q3$rater_1, q3$rater_2)]))
save_csv(q3, DIR_GRM, "q3")

# Cross-check against mirt's own implementation (if it runs on this sparse matrix).
q3_check <- tryCatch({
  qm <- residuals(mod, type = "Q3", Theta = theta_eap, verbose = FALSE)
  ok <- !is.na(q3$q3)
  max(abs(unclass(qm)[cbind(q3$rater_1[ok], q3$rater_2[ok])] - q3$q3[ok]), na.rm = TRUE)
}, error = function(e) paste("mirt::residuals(Q3) failed:", conditionMessage(e)))

# --- absolute fit: M2 / C2 ----------------------------------------------------------------
# mirt 1.46 computes the uni- and bivariate moments of M2-type statistics from
# the available pairs when data are missing (no imputation option exists any
# more). Pairs of raters with no overlap contribute nothing. If C2 fails, the
# reason is recorded instead of forcing a result.
global_fit <- tryCatch({
  m2 <- with_warnings(M2(mod, type = "C2", calcNull = TRUE, quadpts = MIRT_QUADPTS), "M2 C2")
  data.frame(statistic = "C2", as.data.frame(m2), note = paste(
    "Computed on pairwise-available moments; rater pairs without overlap",
    "contribute no information. Interpret with caution for this sparse design."))
}, error = function(e) {
  data.frame(statistic = "C2", note = paste("Not computable:", conditionMessage(e)))
})
global_fit$q3_mirt_crosscheck_max_abs_diff <- as.character(q3_check)
save_csv(global_fit, DIR_GRM, "global_fit")

# --- category response functions per rater ---------------------------------------------------
crf <- do.call(rbind, lapply(seq_along(raters), function(j) {
  p <- probtrace(extract.item(mod, j), matrix(THETA_GRID))
  used <- sort(unique(d$long$rating[d$long$rater_id == raters[j]]))
  data.frame(rater_id = raters[j], theta = rep(THETA_GRID, ncol(p)),
             category = factor(rep(used, each = length(THETA_GRID)), levels = SCALE_MIN:SCALE_MAX),
             probability = as.vector(p))
}))
crf$rater_id <- factor(crf$rater_id, levels = raters)
p_crf <- ggplot(crf, aes(theta, probability, colour = category)) +
  geom_line(linewidth = 0.5) +
  facet_wrap(~ rater_id, ncol = 5) +
  scale_colour_viridis_d(end = 0.92, drop = FALSE) +
  labs(x = expression(theta), y = "P(category)", colour = "Rating",
       title = "GRM category response functions per rater") +
  theme_minimal(base_size = 9)
save_fig(p_crf, "grm_category_response_functions", width = 11, height = 9)

write_warnings("02_grm")
write_session_info("02_grm")
message("02 GRM: done")
