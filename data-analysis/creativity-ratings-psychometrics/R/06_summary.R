# ============================================================
# 06 - Summary (spec section 7)
# ============================================================
# Builds results/summary/reliability_overview.csv and results/summary/REPORT.md
# from the CSV outputs of 01-05. Nothing is typed in by hand; rerun this script
# after any upstream change. Light: reads CSVs only.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))

rd <- function(dir, name) readr::read_csv(file.path(dir, paste0(name, ".csv")), show_col_types = FALSE)
fmt <- function(x, d = 3) ifelse(is.na(x), "NA", formatC(as.numeric(x), digits = d, format = "f"))
get_q <- function(tab, key) tab$value[startsWith(tab$quantity, key)][1]

design <- rd(DIR_DATA, "design_summary")
cat_use <- rd(DIR_DATA, "category_usage")
rel <- rd(DIR_GRM, "reliability_summary")
conv <- rd(DIR_GRM, "convergence")
rfit <- rd(DIR_GRM, "rater_fit")
rpars <- rd(DIR_GRM, "rater_parameters")
info_sum <- rd(DIR_GRM, "rater_information_summary")
mfit <- rd(DIR_CMP, "model_fit")
lr <- rd(DIR_CMP, "lr_tests")
tcor <- rd(DIR_CMP, "theta_correlations")
marg <- rd(DIR_CMP, "marginal_reliability")
cron <- rd(DIR_NAIVE, "cronbach_alpha")
kripp <- rd(DIR_NAIVE, "krippendorff_alpha")
global_fit <- rd(DIR_GRM, "global_fit")
rel_ci <- rd(DIR_GRM, "reliability_ci")
ci_txt <- function(lo, hi, what) sprintf("95%% CI [%s, %s] (%s)", fmt(lo), fmt(hi), what)
rel_ci_of <- function(q) {
  r <- rel_ci[rel_ci$quantity == q, ]
  if (nrow(r) == 0) "" else ci_txt(r$ci_low, r$ci_high, sprintf("%d parameter draws", r$n_draws))
}
cron_ci_of <- function(i) if (!"ci_low" %in% names(cron) || nrow(cron) < i) "" else
  ci_txt(cron$ci_low[i], cron$ci_high[i],
         if (cron$n_boot_failed[i] > 0)
           sprintf("bootstrap, %d of %d replications computable, approximate", cron$n_boot[i] - cron$n_boot_failed[i], cron$n_boot[i])
         else sprintf("bootstrap, %d replications", cron$n_boot[i]))

# --- overview table --------------------------------------------------------------------
marg_of <- function(m) {
  r <- marg[marg$model == m, ]
  if (nrow(r) == 0) NA_real_ else r$marginal_reliability[1]
}
overview <- tibble(
  index = c("Krippendorff's alpha (ordinal)",
            "Cronbach's alpha (pairwise covariances)",
            "Cronbach's alpha (fully crossed block)",
            "GRM: empirical marginal reliability",
            "GRM: model-based marginal reliability",
            "GRM: median rel_post", "GRM: IQR rel_post",
            "M1 (RSM): marginal reliability", "M2 (PCM): marginal reliability",
            "M3 (GPCM): marginal reliability"),
  refers_to = c("consensus of single ratings",
                "consistency of the unweighted rater mean",
                "consistency of the unweighted rater mean (crossed subset)",
                "actual theta_hat (primary)",
                "hypothetical full panel",
                "precision per product", "precision per product",
                "comparison", "comparison", "comparison"),
  value = c(kripp$alpha[1],
            cron$raw_alpha[cron$variant == "pairwise covariances, all usable raters"][1],
            if (any(grepl("crossed", cron$variant))) cron$raw_alpha[grepl("crossed", cron$variant)][1] else NA,
            get_q(rel, "empirical_marginal_reliability"),
            get_q(rel, "model_based_marginal_reliability_mirt"),
            get_q(rel, "rel_post_median"), get_q(rel, "rel_post_iqr"),
            marg_of("M1_RSM"), marg_of("M2_PCM"), marg_of("M3_GPCM")),
  ci_or_note = c(sprintf("95%% bootstrap CI [%s, %s], %d replications", fmt(kripp$ci_low),
                         fmt(kripp$ci_high), kripp$n_boot),
                 sprintf("%s; %d raters; removed: %s", cron_ci_of(1), cron$n_raters[1],
                         ifelse(is.na(cron$raters_removed[1]) | cron$raters_removed[1] == "",
                                "none", cron$raters_removed[1])),
                 if (any(grepl("crossed", cron$variant))) sprintf("%s; %s raters, %s products",
                   cron_ci_of(which(grepl("crossed", cron$variant))[1]),
                   cron$n_raters[grepl("crossed", cron$variant)][1],
                   cron$n_products_contributing[grepl("crossed", cron$variant)][1]) else "no block",
                 paste0(rel_ci_of("empirical_marginal_reliability"), "; Var(theta)/(Var(theta)+mean(PSD^2))"),
                 paste0(rel_ci_of("model_based_marginal_reliability"), "; mirt::marginal_rxx, all raters"),
                 sprintf("Q1 %s, Q3 %s", fmt(get_q(rel, "rel_post_q1")), fmt(get_q(rel, "rel_post_q3"))),
                 "",
                 ifelse(is.na(marg_of("M1_RSM")), "M1 not estimable in mirt (see model_fit.csv)", ""),
                 "", "")
)
save_csv(overview, DIR_SUM, "reliability_overview")

# --- report ------------------------------------------------------------------------------
ladder_text <- function() {
  ic <- mfit %>% filter(status == "estimated") %>% select(model, AIC, BIC, SABIC)
  best <- sapply(c("AIC", "BIC", "SABIC"), function(k) ic$model[which.min(ic[[k]])])
  lr_txt <- vapply(seq_len(nrow(lr)), function(i) {
    if (is.na(lr$X2[i])) return(sprintf("%s: %s.", lr$comparison[i], lr$note[i]))
    sprintf("%s: X2 = %s, df = %d (formula: %d), p = %s.", lr$comparison[i], fmt(lr$X2[i], 2),
            as.integer(lr$df[i]), as.integer(lr$df_expected_formula[i]), format.pval(lr$p[i], digits = 3))
  }, "")
  c(lr_txt, sprintf("Lowest AIC: %s; lowest BIC: %s; lowest SABIC: %s (GRM compared by information criteria only).",
                    best[["AIC"]], best[["BIC"]], best[["SABIC"]]))
}

pear <- tcor %>% filter(method == "pearson")
spear <- tcor %>% filter(method == "spearman")
cor_lines <- c("| Model | Pearson r with GRM | Spearman ρ with GRM |", "|---|---|---|",
               vapply(setdiff(pear$model, "GRM"), function(m)
                 sprintf("| %s | %s | %s |", m, fmt(pear$GRM[pear$model == m]),
                         fmt(spear$GRM[spear$model == m])), ""))

low_info_cut <- 0.01
flags <- cat_use %>% select(rater_id, n_ratings, missing_categories, flag) %>%
  left_join(rfit %>% select(rater_id, infit, outfit, p_S_X2), by = "rater_id") %>%
  left_join(rpars %>% select(rater_id, a, max_abs_b, thresholds_ordered), by = "rater_id") %>%
  left_join(info_sum %>% select(rater_id, share_weighted), by = "rater_id") %>%
  rowwise() %>%
  mutate(reasons = paste(c(
    if (!is.na(infit) && (infit < 0.7 || infit > 1.3)) sprintf("infit %.2f", infit),
    if (!is.na(outfit) && (outfit < 0.7 || outfit > 1.3)) sprintf("outfit %.2f", outfit),
    if (!is.na(missing_categories)) paste0("unused categories ", missing_categories),
    if (!is.na(a) && a > 4) sprintf("a = %.2f", a),
    if (!is.na(max_abs_b) && max_abs_b > 5) sprintf("max |b| = %.2f", max_abs_b),
    if (!is.na(thresholds_ordered) && !thresholds_ordered) "unordered b",
    if (!is.na(share_weighted) && share_weighted < low_info_cut)
      sprintf("information share %.1f%%", 100 * share_weighted)), collapse = "; ")) %>%
  ungroup() %>%
  filter(reasons != "")

report <- c(
  "# JRT audit — summary report",
  "",
  sprintf("_Generated by `R/06_summary.R` on %s. Do not edit by hand. Corrections and deviations from the specification: see [`../../AUDIT.md`](../../AUDIT.md)._",
          format(Sys.Date())),
  if (SMOKE) "\n> **SMOKE RUN** — reduced imputations/bootstraps; numbers are not for the paper.\n" else "",
  "",
  "## Data",
  sprintf("%s ratings of %s products by %s raters on a 1–7 scale (coded 0–6). Design connected (%s component). Harmonic mean of ratings per product: %s.",
          get_q(design, "n_ratings"), get_q(design, "n_products"), get_q(design, "n_raters"),
          get_q(design, "n_components"), fmt(get_q(design, "ratings_per_product_harmonic_mean"))),
  "",
  "## Reliability overview",
  "",
  "| Index | Refers to | Value | Note |", "|---|---|---|---|",
  sprintf("| %s | %s | %s | %s |", overview$index, overview$refers_to, fmt(overview$value),
          overview$ci_or_note),
  "",
  sprintf("GRM: converged = %s after %s EM cycles; information matrix positive definite = %s. C2: %s.",
          conv$converged, conv$iterations, conv$information_matrix_pd,
          if ("M2" %in% names(global_fit)) sprintf("%s (df = %s, p = %s, RMSEA = %s)",
            fmt(global_fit$M2, 2), global_fit$df, format.pval(global_fit$p, digits = 3),
            fmt(global_fit$RMSEA)) else global_fit$note),
  "",
  "## Model ladder (M1 RSM → M2 PCM → M3 GPCM; GRM by information criteria)",
  "",
  paste("-", ladder_text()),
  "",
  "## Agreement of θ̂ between models",
  "",
  cor_lines,
  "",
  "## Raters with notable fit, category use or information",
  "",
  if (nrow(flags)) c("| Rater | n | Reasons |", "|---|---|---|",
                     sprintf("| %s | %d | %s |", flags$rater_id, as.integer(flags$n_ratings),
                             flags$reasons))
  else "None.",
  "",
  "Fit flags use 0.7–1.3 for infit/outfit mean squares; S-X² (multiple imputation) is reported in `results/grm/rater_fit.csv` but is conservative with ~90% imputed cells.",
  "",
  "## Corrections relative to the specification",
  "",
  "All deviations found in the existing analysis and how they were corrected are listed in `AUDIT.md`."
)
writeLines(report, file.path(DIR_SUM, "REPORT.md"))
message("  wrote results/summary/REPORT.md")
write_session_info("06_summary")
message("06 summary: done")
