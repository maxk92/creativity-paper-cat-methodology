# ============================================================
# 04 - Comparison: JRT as GPCM vs. MFRM (spec section 5)
# ============================================================
# Nested adjacent-category ladder, all on the shared wide matrix, all MML (EM):
#   M1 "rsm"   shared thresholds shifted by rater location, equal slopes  = MFRM
#   M2 "Rasch" (PCM) rater-specific thresholds, equal slopes            = MFRM + rater thresholds
#   M3 "gpcm"  rater-specific thresholds and slopes                      = JRT as GPCM
# The GRM (cumulative family) is not part of the ladder; it is compared by
# information criteria only.
#
# Latent scale: mirt fixes the latent mean at 0 in all models. For "rsm" and
# "Rasch" the latent variance is estimated (slopes fixed to 1); for "gpcm" and
# "graded" the variance is fixed to 1. M2 is nested in M3 (all a_j equal <=> PCM
# with a free variance), df = J - 1.
#
# Category gaps (results/data/category_usage.csv): mirt recodes each rater's
# observed categories. mirt's "rsm" refuses raters with different numbers of
# categories, so with all 7 categories kept (decision 2026-10-22) M1 may not be
# estimable in mirt. The script records that outcome instead of changing the
# data; the fix is a decision for the author (see AUDIT.md).
#
# Outputs (results/comparison/): model_fit.csv, lr_tests.csv, theta_correlations.csv,
#   rater_parameters_by_model.csv, threshold_order.csv, discrimination_summary.csv,
#   rater_fit_m1.csv, marginal_reliability.csv, mfrm_equivalence.md, models_*.rds
# SERVER: four mirt fits with SEs plus sirt::rm.facets.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))
suppressPackageStartupMessages(library(sirt))

d <- load_design()
wide <- d$wide
long <- d$long
rated <- !is.na(wide)
raters <- colnames(wide)
J <- ncol(wide)
category_usage <- readr::read_csv(file.path(DIR_DATA, "category_usage.csv"), show_col_types = FALSE)

# --- fits ----------------------------------------------------------------------
try_fit <- function(itemtype, label) {
  message("04: fitting ", label, " (", itemtype, ")")
  tryCatch(fit_mirt(wide, itemtype, label),
           error = function(e) {
             msg <- gsub("\\s+", " ", conditionMessage(e))
             WARNINGS[[length(WARNINGS) + 1]] <<- data.frame(
               context = paste("mirt fit", label), warning = paste("ERROR:", msg))
             structure(list(error = msg), class = "fit_error")
           })
}
is_fit <- function(m) !inherits(m, "fit_error")

models <- list(
  M1_RSM = try_fit("rsm", "M1_RSM"),
  M2_PCM = try_fit("Rasch", "M2_PCM"),
  M3_GPCM = try_fit("gpcm", "M3_GPCM")
)
grm <- readRDS(file.path(DIR_GRM, "model.rds"))
assert_same_data(grm, wide, "GRM")
all_models <- c(models, list(GRM = grm))
for (nm in names(models)) if (is_fit(models[[nm]])) {
  saveRDS(models[[nm]], file.path(DIR_CMP, paste0("model_", nm, ".rds")))
}

# Identical data basis (spec 5): same products, raters, ratings, NA pattern.
fitted <- Filter(is_fit, all_models)
n_check <- vapply(fitted, function(m) c(nrow(extract.mirt(m, "data")), sum(!is.na(extract.mirt(m, "data")))),
                  numeric(2))
stopifnot(all(n_check[1, ] == nrow(wide)), all(n_check[2, ] == sum(rated)))

# --- model fit and information criteria ------------------------------------------
model_fit <- bind_rows(lapply(names(all_models), function(nm) {
  m <- all_models[[nm]]
  if (is_fit(m)) {
    convergence_row(m, nm) %>% mutate(status = "estimated", family = ifelse(
      nm == "GRM", "cumulative (not in LR ladder)", "adjacent category"))
  } else {
    data.frame(model = nm, status = paste("not estimable in mirt:", m$error))
  }
}))
save_csv(model_fit, DIR_CMP, "model_fit")

# --- LR tests ----------------------------------------------------------------------
# Expected df with K categories for every rater: M1 vs M2 (J-1)(K-2), M2 vs M3 J-1.
# With category gaps the actual df differ (raters with fewer categories have
# fewer step parameters), so both are reported.
lr_row <- function(a, b, label, df_formula) {
  if (!is_fit(models[[a]]) || !is_fit(models[[b]])) {
    return(data.frame(comparison = label, df_expected_formula = df_formula,
                      note = "not computed: a model of the pair is not estimable"))
  }
  av <- anova(models[[a]], models[[b]])
  npar_diff <- extract.mirt(models[[b]], "nest") - extract.mirt(models[[a]], "nest")
  data.frame(comparison = label,
             logLik_restricted = av$logLik[1], logLik_general = av$logLik[2],
             X2 = av$X2[2], df = av$df[2], p = av$p[2],
             df_from_npar = npar_diff, df_expected_formula = df_formula,
             df_matches_formula = av$df[2] == df_formula,
             note = ifelse(av$df[2] == df_formula, "",
                           "df differ from the formula because raters use different numbers of categories"))
}
K <- K_CATEGORIES
lr_tests <- bind_rows(
  lr_row("M1_RSM", "M2_PCM", "M1 vs M2: rater-specific thresholds", (J - 1) * (K - 2)),
  lr_row("M2_PCM", "M3_GPCM", "M2 vs M3: rater-specific discriminations", J - 1)
)
save_csv(lr_tests, DIR_CMP, "lr_tests")

# --- theta estimates and correlations ------------------------------------------------------
eap <- lapply(fitted, function(m)
  fscores(m, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE))
theta_tab <- as_tibble(lapply(eap, function(f) f[, "F1"]))

# --- existing MFRM: sirt::rm.facets ---------------------------------------------------------
# Same long data (internal coding 0-6), one "item" (creativity), raters as facet.
# Model (sirt documentation, ?rm.facets):
#   P(X_pr = k | theta_p) ∝ exp(a_i a_r q_k theta_p - q_k b_r - tau_k),  q_k = k,
#   theta_p ~ N(0, sigma^2) with sigma estimated, MML via EM on the grid theta.k.
# Settings (defaults of the original call, written out): est.b.rater = TRUE
# (rater severities b_r), est.a.item = FALSE, est.a.rater = FALSE (all slopes 1),
# rater_item_int = FALSE, est.mean = FALSE (latent mean 0), b.rater.center = 2
# (severities sum to zero), theta.k = seq(-9, 9, len = 30).
# This is the adjacent-category rating scale model with a rater shift, i.e. M1.
# Unlike mirt, rm.facets does not recode categories per rater: every rater
# shares the full 0-6 category set, so unused categories do not shift thresholds.
message("04: fitting sirt::rm.facets")
mfrm_settings <- list(est.b.rater = TRUE, est.a.item = FALSE, est.a.rater = FALSE,
                      rater_item_int = FALSE, est.mean = FALSE, b.rater.center = 2,
                      theta.k = seq(-9, 9, len = 30))
mfrm <- tryCatch(with_warnings(
  do.call(sirt::rm.facets, c(list(
    dat = data.frame(creativity = long$rating_internal),
    pid = long$product_id, rater = long$rater_id), mfrm_settings)),
  "sirt::rm.facets"), error = function(e) structure(list(error = conditionMessage(e)),
                                                     class = "fit_error"))
if (is_fit(mfrm)) {
  saveRDS(mfrm, file.path(DIR_CMP, "model_rm_facets.rds"))
  mfrm_theta <- mfrm$person
  theta_tab$rm_facets <- mfrm_theta$EAP[match(rownames(wide), mfrm_theta$pid)]
}

theta_cor <- bind_rows(lapply(c("pearson", "spearman"), function(meth) {
  cm <- cor(theta_tab, method = meth, use = "pairwise.complete.obs")
  as_tibble(cm, rownames = "model") %>% mutate(method = meth, .before = 1)
}))
save_csv(theta_cor, DIR_CMP, "theta_correlations")

# --- rater parameters by model ---------------------------------------------------------------
pars_long <- function(m, nm) {
  cf <- tryCatch(coef(m, IRTpars = TRUE, printSE = TRUE),
                 error = function(e) coef(m, IRTpars = FALSE, printSE = TRUE))
  bind_rows(lapply(raters, function(r) {
    x <- cf[[r]]
    tibble(model = nm, rater_id = r, parameter = colnames(x), estimate = x["par", ],
           se = if ("SE" %in% rownames(x)) x["SE", ] else NA_real_)
  })) %>% bind_rows(
    if (!is.null(cf$GroupPars)) tibble(model = nm, rater_id = "(group)",
                                       parameter = colnames(cf$GroupPars),
                                       estimate = cf$GroupPars["par", ],
                                       se = if ("SE" %in% rownames(cf$GroupPars))
                                         cf$GroupPars["SE", ] else NA_real_))
}
rater_pars <- bind_rows(lapply(names(fitted), function(nm) pars_long(fitted[[nm]], nm)))
if (is_fit(mfrm)) {
  rater_pars <- bind_rows(rater_pars, tibble(
    model = "rm_facets", rater_id = as.character(mfrm$rater$rater), parameter = "b_rater",
    estimate = mfrm$rater$b, se = mfrm$rater$se.b))
}
save_csv(rater_pars, DIR_CMP, "rater_parameters_by_model")

# Threshold order in M2 and M3 (IRT metric b_k). Unordered steps are flagged.
threshold_order <- rater_pars %>%
  filter(model %in% c("M2_PCM", "M3_GPCM"), grepl("^b\\d+$", parameter)) %>%
  group_by(model, rater_id) %>%
  summarise(n_steps = n(), ordered = all(diff(estimate) > 0),
            n_reversals = sum(diff(estimate) <= 0),
            steps = paste(sprintf("%.2f", estimate), collapse = ";"), .groups = "drop")
save_csv(threshold_order, DIR_CMP, "threshold_order")

discrimination_summary <- rater_pars %>%
  filter(model == "M3_GPCM", parameter == "a") %>%
  left_join(category_usage %>% select(rater_id, n_ratings), by = "rater_id") %>%
  arrange(estimate)
save_csv(discrimination_summary, DIR_CMP, "discrimination_m3")
if (nrow(discrimination_summary)) {
  save_csv(tibble(statistic = c("min", "q1", "median", "q3", "max", "ratio_max_min", "sd"),
                  value = c(quantile(discrimination_summary$estimate),
                            max(discrimination_summary$estimate) / min(discrimination_summary$estimate),
                            sd(discrimination_summary$estimate))),
           DIR_CMP, "discrimination_summary")
}

# --- rater fit in M1 ---------------------------------------------------------------------------
if (is_fit(models$M1_RSM)) {
  th1 <- eap$M1_RSM[, "F1", drop = FALSE]
  fit_m1 <- with_warnings(itemfit(models$M1_RSM, fit_stats = "infit", Theta = th1), "itemfit M1")
  fit_m1 <- fit_m1 %>% rename(rater_id = item) %>%
    mutate(flag = infit < 0.7 | infit > 1.3 | outfit < 0.7 | outfit > 1.3,
           source = "mirt M1 (rsm)")
} else {
  fit_m1 <- tibble(rater_id = raters, source = "M1 not estimable in mirt; see model_fit.csv")
}
save_csv(fit_m1, DIR_CMP, "rater_fit_m1")

# --- marginal reliability (comparison only) ----------------------------------------------------
# Posterior-based convention on each model's own latent scale theta ~ N(0, s2):
#   rel(theta) = s2 I(theta) / (s2 I(theta) + 1), averaged over N(0, s2).
# For s2 = 1 this is I/(I+1) and equals mirt::marginal_rxx (reported as a check;
# marginal_rxx assumes a standard normal density, so it is not used for s2 != 1).
marginal_rel <- function(nm) {
  m <- fitted[[nm]]
  s2 <- as.numeric(coef(m, simplify = TRUE)$cov)
  z <- THETA_GRID
  info <- rowSums(rater_information(m, sqrt(s2) * z))
  w <- normal_weights(z)
  c(latent_variance = s2,
    marginal_reliability = sum(w * s2 * info / (s2 * info + 1)) / sum(w),
    marginal_rxx_mirt = if (abs(s2 - 1) < 1e-8) marginal_rxx(m) else NA_real_,
    empirical_rxx = unname(empirical_rxx(eap[[nm]])))
}
marg <- bind_rows(lapply(names(fitted), function(nm)
  as_tibble(as.list(marginal_rel(nm))) %>% mutate(model = nm, .before = 1)))
if (is_fit(mfrm)) marg <- bind_rows(marg, tibble(model = "rm_facets",
                                                latent_variance = mfrm$sigma^2,
                                                empirical_rxx = mfrm$EAP.rel))
save_csv(marg, DIR_CMP, "marginal_reliability")

# --- MFRM equivalence report ----------------------------------------------------------------------
fmt <- function(x, d = 3) ifelse(is.na(x), "NA", formatC(x, digits = d, format = "f"))
eq_lines <- c(
  "# Equivalence check: `sirt::rm.facets` vs. `mirt` M1 (rating scale model)",
  "",
  "_Generated by `R/04_model_comparison.R`. Do not edit by hand._",
  "",
  "## Parametrisation of the existing MFRM",
  "",
  "The call in the former `notebooks/02_creativity_ratings_R.qmd` (`rm.facets(dat, pid, rater)`)",
  "uses the package defaults. From `?sirt::rm.facets` (sirt ",
  as.character(packageVersion("sirt")), "):",
  "",
  "- Model: P(X_pr = k | θ_p) ∝ exp(a_i a_r q_k θ_p − q_k b_r − τ_k), q_k = k.",
  "- `est.b.rater = TRUE`: rater severities b_r estimated, centred to sum to zero (`b.rater.center = 2`).",
  "- `est.a.item = FALSE`, `est.a.rater = FALSE`: all slopes fixed to 1 (Rasch).",
  "- `rater_item_int = FALSE`, one item: one set of thresholds τ_k shared by all raters (rating scale structure).",
  "- `est.mean = FALSE`: latent mean 0; the latent SD σ is estimated.",
  "- Estimation: marginal maximum likelihood, EM algorithm, integration on the fixed grid `theta.k = seq(-9, 9, len = 30)`.",
  "- Identification: θ mean 0, Σ b_r = 0, slopes 1.",
  "",
  "This is the same model as M1 (`itemtype = \"rsm\"`). Differences to expect: severity b_r",
  "(rm.facets, higher = stricter) against mirt's rater location (sign may be reversed),",
  "different integration grids (30 points on [−9, 9] vs. 61 quadrature points), and",
  "rm.facets keeps every rater on the full 0–6 category set, while mirt recodes per rater.",
  "",
  "## Results",
  ""
)
if (is_fit(models$M1_RSM) && is_fit(mfrm)) {
  loc <- rater_pars %>% filter(model == "M1_RSM", parameter == "c") %>%
    select(rater_id, mirt_location = estimate) %>%
    inner_join(rater_pars %>% filter(model == "rm_facets") %>%
                 select(rater_id, rm_facets_b = estimate), by = "rater_id")
  eq_lines <- c(eq_lines,
    sprintf("| Quantity | mirt M1 | rm.facets |"), "|---|---|---|",
    sprintf("| logLik | %s | %s |", fmt(extract.mirt(models$M1_RSM, "logLik"), 2),
            fmt(as.numeric(logLik(mfrm)), 2)),
    sprintf("| latent variance | %s | %s |", fmt(as.numeric(coef(models$M1_RSM, simplify = TRUE)$cov)),
            fmt(mfrm$sigma^2)),
    "",
    sprintf("- Correlation of rater locations (mirt `c` vs. rm.facets `b`): %s",
            fmt(cor(loc$mirt_location, loc$rm_facets_b))),
    sprintf("- Correlation of θ̂ (EAP): Pearson %s, Spearman %s",
            fmt(cor(theta_tab$M1_RSM, theta_tab$rm_facets, use = "complete.obs")),
            fmt(cor(theta_tab$M1_RSM, theta_tab$rm_facets, method = "spearman",
                    use = "complete.obs"))))
} else {
  eq_lines <- c(eq_lines,
    "**The check could not be completed as specified.**", "",
    if (!is_fit(models$M1_RSM)) paste0("- mirt M1 (`rsm`) is not estimable: `", models$M1_RSM$error,
                                       "`. Cause: raters use different numbers of categories ",
                                       "(results/data/category_usage.csv), and all 7 categories were ",
                                       "kept (decision 2026-10-22)."),
    if (!is_fit(mfrm)) paste0("- rm.facets failed: `", mfrm$error, "`."),
    if (is_fit(mfrm)) c(
      sprintf("- rm.facets: logLik %s, latent variance %s, EAP reliability %s.",
              fmt(as.numeric(logLik(mfrm)), 2), fmt(mfrm$sigma^2), fmt(mfrm$EAP.rel)),
      sprintf("- Correlation of rm.facets θ̂ with M2 (PCM): Pearson %s; with GRM: Pearson %s.",
              fmt(if (!is.null(theta_tab$M2_PCM)) cor(theta_tab$M2_PCM, theta_tab$rm_facets) else NA),
              fmt(cor(theta_tab$GRM, theta_tab$rm_facets)))),
    "", "The author must decide how to make M1 estimable (see AUDIT.md, open decisions).")
}
eq_lines <- c(eq_lines, "",
  "LR tests use the mirt ladder only, so the likelihoods are comparable (same software,",
  "same integration, same data object).")
writeLines(eq_lines, file.path(DIR_CMP, "mfrm_equivalence.md"))

print(model_fit %>% select(any_of(c("model", "status", "converged", "logLik", "npar", "AIC", "BIC", "SABIC"))))
print(lr_tests)
write_warnings("04_model_comparison")
write_session_info("04_model_comparison")
message("04 model comparison: done")
