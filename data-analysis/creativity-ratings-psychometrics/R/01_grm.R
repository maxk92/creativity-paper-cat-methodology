# ============================================================
# 01 - Data basis and the JRT analysis: graded response model by MML
# ============================================================
# Raters = items, products = persons (judge response theory):
#   P(X_nj >= k | theta_n) = 1 / (1 + exp(-a_j (theta_n - b_jk))),  theta ~ N(0, 1)
# fitted with mirt::mirt(wide, 1, itemtype = "graded") by marginal maximum
# likelihood (EM, fixed quadrature). Missing ratings are left out of the
# likelihood, not imputed.
#
# Part A (main results): data basis, GRM fit, rater parameters, EAP scores,
#   information, reliability, raw mean vs GRM score, figures.
# Part B (supplementary diagnostics): 95% intervals from parameter draws,
#   rater fit (infit/outfit, S-X2), local dependence (Q3), global fit (C2).
#
# Run from the analysis folder:  Rscript R/01_grm.R   (a few minutes)
# ============================================================

source(if (interactive()) "R/jrt_functions.R" else
  file.path(dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1])), "jrt_functions.R"))
suppressPackageStartupMessages(library(igraph))

# ==============================================================================
# A. Data basis
# ==============================================================================
message("01 GRM: reading ", INPUT_CSV)
raw <- read_csv(INPUT_CSV, show_col_types = FALSE,
                col_types = cols(action_id = "c", rater_id = "c", .default = "?"))

# Only the creativity rating is modelled; technical_correctness and
# aesthetic_appeal stay in the data but go into no model.
long <- raw %>%
  transmute(product_id = action_id, rater_id,
            rating = as.integer(rating_numeric), rating_internal = rating - SCALE_MIN)
stopifnot(!anyNA(long$product_id), !anyNA(long$rater_id), !anyNA(long$rating),
          all(long$rating >= SCALE_MIN & long$rating <= SCALE_MAX))

# Duplicates are resolved in notebook 00 (latest entry kept); none may remain.
if (any(duplicated(long[, c("product_id", "rater_id")])))
  stop("Duplicate product-rater pairs in the input. Resolve them in notebook 00.")
dup_report <- if (file.exists(DUPLICATES_CSV)) {
  read_csv(DUPLICATES_CSV, show_col_types = FALSE, col_types = cols(.default = "c")) %>%
    group_by(action_id, rater_id) %>% summarise(conflicting = n_distinct(rating) > 1, .groups = "drop")
} else tibble(conflicting = logical())

# Rater exclusion: fewer than MIN_RATINGS_PER_RATER ratings. Products whose only
# ratings came from excluded raters drop out. Notebook 01 reads excluded_raters.csv.
n_before <- c(ratings = nrow(long), products = n_distinct(long$product_id))
excluded <- long %>% count(rater_id, name = "n_ratings") %>%
  filter(n_ratings < MIN_RATINGS_PER_RATER) %>%
  mutate(reason = sprintf("fewer than %d ratings", MIN_RATINGS_PER_RATER)) %>%
  arrange(factor(rater_id, levels = rater_order(rater_id)))
long <- long %>% filter(!rater_id %in% excluded$rater_id)
products_dropped <- n_before[["products"]] - n_distinct(long$product_id)
save_csv(excluded, "excluded_raters", "data")
message(sprintf("  excluded raters (< %d ratings): %s; %d ratings removed, %d products dropped",
                MIN_RATINGS_PER_RATER, paste(excluded$rater_id, collapse = ", "),
                n_before[["ratings"]] - nrow(long), products_dropped))

# Wide matrix: products x raters, internal coding 0-6, NA = not rated.
raters <- rater_order(unique(long$rater_id))
wide_df <- long %>%
  select(product_id, rater_id, rating_internal) %>%
  pivot_wider(names_from = rater_id, values_from = rating_internal) %>%
  arrange(product_id) %>%
  select(product_id, all_of(raters))
save_csv(wide_df, "ratings_wide", "data")
wide <- as.matrix(wide_df[, -1])
storage.mode(wide) <- "integer"
rownames(wide) <- wide_df$product_id
rated <- !is.na(wide)
stopifnot(sum(rated) == nrow(long), all(rowSums(rated) >= 1))

# Category use per rater. mirt recodes the OBSERVED categories of each rater to
# consecutive integers: an unused END category only removes the outermost
# threshold(s); an unused INTERNAL category shifts all higher thresholds, so they
# are no longer comparable with other raters. All 7 categories are kept.
category_usage <- long %>%
  mutate(category = factor(rating, levels = SCALE_MIN:SCALE_MAX)) %>%
  count(rater_id, category, .drop = FALSE) %>%
  pivot_wider(names_from = category, values_from = n, names_prefix = "cat_") %>%
  rowwise() %>%
  mutate(
    n_ratings = sum(c_across(starts_with("cat_"))),
    used = list(which(c_across(starts_with("cat_")) > 0)),
    n_categories_used = length(used),
    missing_categories = paste(setdiff(seq_len(K_CATEGORIES), used), collapse = ";"),
    lowest_used = min(used), highest_used = max(used),
    internal_gap = any(!(seq(min(used), max(used)) %in% used)),
    end_gap = min(used) > 1 | max(used) < K_CATEGORIES,
    mirt_categories = n_categories_used,
    flag = case_when(
      internal_gap ~ "internal gap: thresholds above the gap shifted in mirt",
      end_gap ~ "end gap: fewer thresholds; RSM not estimable with unequal categories",
      TRUE ~ "all categories used")
  ) %>%
  ungroup() %>%
  select(-used) %>%
  mutate(rater_id = factor(rater_id, levels = raters)) %>%
  arrange(rater_id) %>%
  mutate(rater_id = as.character(rater_id))
save_csv(category_usage, "category_usage", "supplement")

# Connectivity: all raters and products must lie in one component (hard stop).
g <- graph_from_data_frame(
  long %>% transmute(from = paste0("P::", product_id), to = paste0("R::", rater_id)), directed = FALSE)
n_components <- components(g)$no
if (n_components != 1) stop("The product-rater graph has ", n_components, " components.")

# Descriptives of the design.
overlap <- crossprod(rated * 1L)  # diagonal = ratings per rater
pair_overlap <- overlap[upper.tri(overlap)]
per_product <- long %>% count(product_id, name = "n_ratings")
save_csv(per_product %>% count(n_ratings, name = "n_products") %>% mutate(share = n_products / sum(n_products)),
         "design_summary_ratings_per_product", "supplement")
rater_desc <- long %>%
  group_by(rater_id) %>%
  summarise(n_ratings = n(), mean = mean(rating), sd = sd(rating), median = median(rating), .groups = "drop") %>%
  arrange(factor(rater_id, levels = raters))
save_csv(rater_desc, "design_summary_raters", "main")
design_summary <- tibble(
  quantity = c("n_ratings", "n_products", "n_raters",
               "min_ratings_per_rater (exclusion cut-off)", "raters_excluded",
               "ratings_excluded", "products_dropped", "n_categories", "scale",
               "internal_coding", "ratings_per_product_mean", "ratings_per_product_median",
               "ratings_per_product_min", "ratings_per_product_max",
               "ratings_per_product_harmonic_mean", "products_with_1_rating",
               "ratings_per_rater_min", "ratings_per_rater_max", "matrix_fill",
               "n_components", "rater_pairs_total", "rater_pairs_without_overlap",
               "rater_pairs_overlap_median", "raters_with_category_gaps",
               "raters_with_internal_gap", "duplicate_pairs_resolved_in_00",
               "duplicate_pairs_conflicting"),
  value = c(nrow(long), nrow(wide), ncol(wide),
            MIN_RATINGS_PER_RATER, if (nrow(excluded)) paste(excluded$rater_id, collapse = ";") else "none",
            n_before[["ratings"]] - nrow(long), products_dropped,
            K_CATEGORIES, "1-7", "rating - 1 (0-6)",
            mean(per_product$n_ratings), median(per_product$n_ratings),
            min(per_product$n_ratings), max(per_product$n_ratings),
            1 / mean(1 / per_product$n_ratings), sum(per_product$n_ratings == 1),
            min(rater_desc$n_ratings), max(rater_desc$n_ratings), mean(rated),
            n_components, length(pair_overlap), sum(pair_overlap == 0), median(pair_overlap),
            sum(category_usage$end_gap | category_usage$internal_gap),
            sum(category_usage$internal_gap), nrow(dup_report), sum(dup_report$conflicting)) %>% as.character())
save_csv(design_summary, "design_summary", "main")
print(design_summary, n = Inf)

# ==============================================================================
# B. GRM fit, rater parameters, scores
# ==============================================================================
message("01 GRM: fitting mirt graded model (", nrow(wide), " products x ", ncol(wide), " raters)")
mod <- fit_mirt(wide, "graded")
saveRDS(mod, file.path(DIRS$models, "grm.rds"))
conv <- convergence_row(mod, "GRM")
save_csv(conv, "convergence", "supplement")
if (!conv$converged) warning("GRM did not converge - results are not usable.")
if (isFALSE(conv$information_matrix_pd)) warning("GRM information matrix is not positive definite.")
message(sprintf("  converged=%s after %d EM cycles; information matrix PD=%s",
                conv$converged, conv$iterations, conv$information_matrix_pd))

# Rater parameters in IRT metric with SEs. mirt's b_k refer to the boundaries
# between the categories a rater actually used; `category_boundaries` says which.
cf_irt <- coef(mod, IRTpars = TRUE, printSE = TRUE)
max_b <- K_CATEGORIES - 1L
rater_pars <- bind_rows(lapply(raters, function(r) {
  m <- cf_irt[[r]]
  est <- m["par", ]; se <- if ("SE" %in% rownames(m)) m["SE", ] else rep(NA_real_, length(est))
  b_est <- est[grepl("^b", names(est))]; b_se <- se[grepl("^b", names(se))]
  used <- sort(unique(long$rating[long$rater_id == r]))
  out <- data.frame(rater_id = r, a = est[["a"]], a_se = se[["a"]], n_thresholds = length(b_est),
                    category_boundaries = paste(paste0(head(used, -1), "|", tail(used, -1)), collapse = ";"),
                    stringsAsFactors = FALSE)
  for (k in seq_len(max_b)) {
    out[[paste0("b", k)]] <- if (k <= length(b_est)) b_est[[k]] else NA_real_
    out[[paste0("b", k, "_se")]] <- if (k <= length(b_se)) b_se[[k]] else NA_real_
  }
  out
})) %>%
  left_join(category_usage %>% select(rater_id, n_ratings, n_categories_used, missing_categories,
                                      internal_gap, end_gap), by = "rater_id") %>%
  mutate(
    thresholds_ordered = apply(across(matches("^b\\d$")), 1, function(b) { b <- b[!is.na(b)]; all(diff(b) > 0) }),
    max_abs_b = apply(across(matches("^b\\d$")), 1, function(b) max(abs(b), na.rm = TRUE)),
    flag_a_gt_4 = a > 4,
    flag_abs_b_gt_5 = max_abs_b > 5,
    flag_missing_se = is.na(a_se),
    plausibility_note = case_when(
      flag_a_gt_4 | flag_abs_b_gt_5 ~ paste0("extreme parameter; n_ratings=", n_ratings, ", categories used=", n_categories_used),
      internal_gap ~ "internal category gap: b_k compare different boundaries than for other raters",
      TRUE ~ "")
  )
save_csv(rater_pars, "rater_parameters", "main")

# EAP scores with posterior SD; product-level reliability from the product's own raters.
fs <- eap_scores(mod)
theta_hat <- fs[, "F1"]
psd <- fs[, "SE_F1"]
info_at_eap <- product_information(mod, theta_hat, rated)
product_scores <- tibble(
  product_id = rownames(wide), theta_eap = theta_hat, psd = psd,
  rel_post = 1 - psd^2, info_at_eap = info_at_eap, rel_info = rel_from_info(info_at_eap),
  n_ratings = rowSums(rated), raters = apply(rated, 1, function(r) paste(raters[r], collapse = ";")))
save_csv(product_scores, "product_scores", "supplement")
rel_by_n <- product_scores %>%
  group_by(n_ratings) %>%
  summarise(n_products = n(), rel_post_mean = mean(rel_post), rel_post_median = median(rel_post),
            rel_info_mean = mean(rel_info), psd_mean = mean(psd), .groups = "drop")
save_csv(rel_by_n, "reliability_by_n_ratings", "main")

# ==============================================================================
# C. Information and reliability
# ==============================================================================
# Rater information I_j(theta) adds up over raters (local independence). The
# full-panel quantities are HYPOTHETICAL: a product rated by all raters.
w_norm <- normal_weights(THETA_GRID)
info_grid <- rater_information(mod, THETA_GRID)  # grid x raters
panel_info <- rowSums(info_grid)
info_long <- as_tibble(info_grid) %>% mutate(theta = THETA_GRID) %>%
  pivot_longer(-theta, names_to = "rater", values_to = "info") %>% select(rater, theta, info)
save_csv(info_long, "rater_information_grid", "main")

idx_points <- vapply(THETA_POINTS, function(t) which.min(abs(THETA_GRID - t)), integer(1))
weighted_area <- colSums(info_grid * w_norm)  # integral of I_j(theta) * phi(theta)
info_summary <- tibble(
  rater_id = raters, n_ratings = colSums(rated), info_weighted_area = weighted_area,
  theta_at_max = THETA_GRID[apply(info_grid, 2, which.max)], info_max = apply(info_grid, 2, max),
  share_weighted = weighted_area / sum(weighted_area))
for (k in seq_along(THETA_POINTS)) {
  info_summary[[sprintf("share_at_theta_%+g", THETA_POINTS[k])]] <- info_grid[idx_points[k], ] / panel_info[idx_points[k]]
}
save_csv(info_summary, "rater_information_summary", "supplement")

panel <- tibble(theta = THETA_GRID, info = panel_info, se = se_from_info(panel_info), rel = rel_from_info(panel_info))
save_csv(panel, "panel_information_grid", "supplement")
marginal_mirt <- marginal_rxx(mod)                                  # hypothetical full panel
marginal_grid <- sum(w_norm * rel_from_info(panel_info)) / sum(w_norm)  # same on the fixed grid

empirical <- unname(empirical_rxx(fs))  # = var(theta_hat) / (var(theta_hat) + mean(psd^2))
stopifnot(abs(empirical - empirical_rel(fs)) < 1e-8)
cons_diff <- product_scores$rel_info - product_scores$rel_post
rel_q <- quantile(product_scores$rel_post, c(0, .1, .25, .5, .75, .9, 1))
reliability_summary <- tibble(
  quantity = c("empirical_marginal_reliability (primary; actual scores)",
               "model_based_marginal_reliability_mirt (hypothetical full panel)",
               "model_based_marginal_reliability_grid (check)",
               "var_theta_eap", "mean_psd_squared",
               "rel_post_min", "rel_post_p10", "rel_post_q1", "rel_post_median", "rel_post_q3",
               "rel_post_p90", "rel_post_max", "rel_post_mean", "rel_post_iqr",
               "consistency_cor_rel_post_rel_info", "consistency_mean_diff_rel_info_minus_rel_post",
               "consistency_max_abs_diff", "products_abs_diff_gt_0.1"),
  value = c(empirical, marginal_mirt, marginal_grid, var(theta_hat), mean(psd^2),
            rel_q, mean(product_scores$rel_post), IQR(product_scores$rel_post),
            cor(product_scores$rel_post, product_scores$rel_info), mean(cons_diff), max(abs(cons_diff)),
            sum(abs(cons_diff) > 0.1)))
save_csv(reliability_summary, "reliability_summary", "supplement")
print(reliability_summary, n = Inf)

# ==============================================================================
# D. Raw rater mean vs GRM score
# ==============================================================================
# The unweighted mean of a product's ratings (common practice) against its GRM
# score, separately for products with 1, 2 and 3+ ratings. The raw mean is tied
# for almost all products, so agreement is Kendall's tau-b and the share of
# product pairs with different raw means that the GRM orders the other way round.
raw_mean <- rowMeans(wide, na.rm = TRUE) + SCALE_MIN
n_group <- function(n) ifelse(n >= 3, "3+", as.character(n))
raw_vs_grm_stats <- function(x, ref) {
  dx <- sign(outer(x, x, "-")); dr <- sign(outer(ref, ref, "-"))
  untied <- upper.tri(dx) & dx != 0
  ranges <- tapply(ref, x, function(t) if (length(t) >= 2) diff(range(t)) else NA_real_)
  tibble(kendall_tau_b = cor(x, ref, method = "kendall"),
         share_discordant_pairs = mean(dx[untied] != dr[untied]),
         mean_theta_range_same_raw_mean = mean(ranges, na.rm = TRUE),
         max_theta_range_same_raw_mean = max(ranges, na.rm = TRUE))
}
raw_vs_grm <- bind_rows(lapply(c("1", "2", "3+"), function(g) {
  i <- n_group(product_scores$n_ratings) == g
  raw_vs_grm_stats(raw_mean[i], theta_hat[i]) %>% mutate(n_ratings = g, n_products = sum(i), .before = 1)
}))
save_csv(raw_vs_grm, "raw_mean_vs_grm", "main")

# ==============================================================================
# E. Figures
# ==============================================================================
p_raw <- tibble(raw = raw_mean, theta = theta_hat,
                n_ratings = paste(n_group(product_scores$n_ratings), "ratings")) %>%
  mutate(n_ratings = sub("^1 ratings$", "1 rating", n_ratings)) %>%
  ggplot(aes(raw, theta)) +
  geom_jitter(width = 0.04, height = 0, size = 0.5, alpha = 0.35) +
  facet_wrap(~ n_ratings) +
  scale_x_continuous(breaks = SCALE_MIN:SCALE_MAX) +
  labs(x = "Raw mean rating", y = expression("GRM score " * hat(theta)[EAP])) +
  theme_minimal(base_size = 10)
save_fig(p_raw, "grm_raw_mean_vs_theta", "main", width = 9, height = 3.6)

crf <- bind_rows(lapply(seq_along(raters), function(j) {
  p <- probtrace(extract.item(mod, j), matrix(THETA_GRID))
  used <- sort(unique(long$rating[long$rater_id == raters[j]]))
  data.frame(rater_id = raters[j], theta = rep(THETA_GRID, ncol(p)),
             category = factor(rep(used, each = length(THETA_GRID)), levels = SCALE_MIN:SCALE_MAX),
             probability = as.vector(p))
})) %>% mutate(rater_id = factor(rater_id, levels = raters))
p_crf <- ggplot(crf, aes(theta, probability, colour = category)) +
  geom_line(linewidth = 0.5) +
  facet_wrap(~ rater_id, ncol = 5) +
  scale_colour_viridis_d(end = 0.92, drop = FALSE) +
  labs(x = expression(theta), y = "P(category)", colour = "Rating") +
  theme_minimal(base_size = 9)
save_fig(p_crf, "grm_category_response_functions", "main", width = 11, height = 9)

info_long$rater <- factor(info_long$rater, levels = raters)
p_info <- ggplot(info_long, aes(theta, info, colour = rater)) +
  geom_line(linewidth = 0.4) +
  scale_colour_viridis_d(end = 0.95) +
  labs(x = expression(theta), y = expression(I[j](theta)), colour = "Rater") +
  guides(colour = guide_legend(ncol = 2)) +
  theme_minimal(base_size = 10)
save_fig(p_info, "grm_rater_information", "main")

p_share <- info_long %>% group_by(theta) %>% mutate(share = info / sum(info)) %>% ungroup() %>%
  ggplot(aes(theta, share, fill = rater)) +
  geom_area(position = "stack", colour = NA) +
  scale_fill_viridis_d(end = 0.95) +
  labs(x = expression(theta), y = "Share of panel information", fill = "Rater") +
  guides(fill = guide_legend(ncol = 2)) +
  theme_minimal(base_size = 10)
save_fig(p_share, "grm_rater_information_shares", "supplement")

p_panel <- panel %>%
  pivot_longer(c(info, rel), names_to = "quantity") %>%
  mutate(quantity = recode(quantity, info = "Information~italic(I)(theta)", rel = "Reliability~italic(I)/(italic(I)+1)")) %>%
  ggplot(aes(theta, value)) + geom_line() +
  facet_wrap(~ quantity, scales = "free_y", labeller = label_parsed) +
  labs(x = expression(theta), y = "Value") +
  theme_minimal(base_size = 10)
save_fig(p_panel, "grm_panel_information_reliability", "supplement", width = 9, height = 4)

p_hist <- ggplot(product_scores, aes(rel_post)) +
  geom_histogram(bins = 50, fill = "grey40") +
  labs(x = expression(rel[post] == 1 - PSD^2), y = "Products") +
  theme_minimal(base_size = 10)
save_fig(p_hist, "grm_rel_post_histogram", "supplement", width = 7, height = 4)

p_n <- ggplot(product_scores, aes(factor(n_ratings), rel_post)) +
  geom_boxplot(outlier.size = 0.4) +
  labs(x = "Number of ratings", y = expression(rel[post])) +
  theme_minimal(base_size = 10)
save_fig(p_n, "grm_rel_post_by_n_ratings", "supplement", width = 7, height = 4)

p_theta <- ggplot(product_scores, aes(theta_eap, rel_post, colour = factor(pmin(n_ratings, 5)))) +
  geom_point(size = 0.6, alpha = 0.5) +
  scale_colour_viridis_d(labels = c("1", "2", "3", "4", "5+"), end = 0.9) +
  labs(x = expression(hat(theta)[EAP]), y = expression(rel[post]), colour = "Ratings per product") +
  guides(colour = guide_legend(override.aes = list(size = 2.5, alpha = 1))) +
  theme_minimal(base_size = 10)
save_fig(p_theta, "grm_rel_post_by_theta", "supplement", width = 7, height = 4)

p_cons <- ggplot(product_scores, aes(rel_info, rel_post)) +
  geom_abline(linetype = "dashed", colour = "grey50") +
  geom_point(size = 0.6, alpha = 0.4) +
  labs(x = expression(rel[info] == I[n](hat(theta)) / (I[n](hat(theta)) + 1)),
       y = expression(rel[post] == 1 - PSD^2)) +
  theme_minimal(base_size = 10)
save_fig(p_cons, "grm_rel_consistency", "supplement", width = 6, height = 5)

# ==============================================================================
# F. Supplementary diagnostics
# ==============================================================================
# --- F1. 95% intervals from parameter draws ------------------------------------
# Parameters are drawn from their asymptotic normal distribution (estimates and
# Oakes covariance). Draws with a <= 0 or non-decreasing GRM intercepts are
# rejected (count reported). For each accepted draw the GRM is evaluated with all
# parameters fixed, EAP scores and PSDs recomputed, and the products resampled
# with replacement for the empirical reliability. Parameters treated as known
# otherwise. (mirt::draw_parameters() fails on this model in mirt 1.46.1.)
message("01 GRM: parameter draws for 95% intervals")
N_DRAWS <- if (QUICK) 10L else 200L
V <- vcov(mod)
sv <- mod2values(mod)
par_idx <- match(as.integer(sub(".*\\.", "", colnames(V))), sv$parnum)
stopifnot(!anyNA(par_idx), all(sv$est[par_idx]), length(par_idx) == sum(sv$est))
item_rows <- split(seq_len(nrow(sv)), sv$item)[raters]
valid_draw <- function(values) all(vapply(item_rows, function(r) {
  a <- values[r][sv$name[r] == "a1"]
  dd <- values[r][grepl("^d\\d+$", sv$name[r])]
  a > 0 && all(diff(dd) < 0)
}, logical(1)))

set.seed(SEED)
draw_stats <- list()
n_rejected <- 0L
while (length(draw_stats) < N_DRAWS && n_rejected < 50L * N_DRAWS) {
  values <- sv$value
  values[par_idx] <- MASS::mvrnorm(1, sv$value[par_idx], V)
  if (!valid_draw(values)) { n_rejected <- n_rejected + 1L; next }
  sv_d <- sv; sv_d$value <- values; sv_d$est <- FALSE
  mod_d <- suppressWarnings(mirt(wide, 1, itemtype = "graded", pars = sv_d, TOL = NaN,
                                 quadpts = MIRT_QUADPTS, verbose = FALSE))
  fs_d <- eap_scores(mod_d)
  b <- sample.int(nrow(fs_d), replace = TRUE)
  area_d <- colSums(rater_information(mod_d, THETA_GRID) * w_norm)
  draw_stats[[length(draw_stats) + 1]] <- list(
    empirical = var(fs_d[b, "F1"]) / (var(fs_d[b, "F1"]) + mean(fs_d[b, "SE_F1"]^2)),
    model_based = sum(w_norm * rel_from_info(rowSums(rater_information(mod_d, THETA_GRID)))) / sum(w_norm),
    area = area_d, share = area_d / sum(area_d))
}
n_draws <- length(draw_stats)
ci <- function(x) unname(quantile(x, c(0.025, 0.975)))
emp_ci <- ci(vapply(draw_stats, `[[`, numeric(1), "empirical"))
mb_ci <- ci(vapply(draw_stats, `[[`, numeric(1), "model_based"))
reliability_ci <- tibble(
  quantity = c("empirical_marginal_reliability", "model_based_marginal_reliability"),
  estimate = c(empirical, marginal_grid),
  ci_low = c(emp_ci[1], mb_ci[1]), ci_high = c(emp_ci[2], mb_ci[2]),
  n_draws = n_draws, n_draws_rejected = n_rejected, seed = SEED,
  method = c("percentile interval over parameter draws (asymptotic normal, Oakes covariance) with products resampled",
             "percentile interval over parameter draws (asymptotic normal, Oakes covariance); grid version of marginal_rxx"))
save_csv(reliability_ci, "reliability_ci", "supplement")

area_draws <- do.call(rbind, lapply(draw_stats, `[[`, "area"))
share_draws <- do.call(rbind, lapply(draw_stats, `[[`, "share"))
info_ci <- info_summary %>%
  select(rater_id, n_ratings, info_weighted_area, share_weighted) %>%
  mutate(info_ci_low = apply(area_draws, 2, quantile, 0.025),
         info_ci_high = apply(area_draws, 2, quantile, 0.975),
         share_ci_low = apply(share_draws, 2, quantile, 0.025),
         share_ci_high = apply(share_draws, 2, quantile, 0.975),
         n_draws = n_draws, .after = info_weighted_area) %>%
  relocate(share_weighted, .before = share_ci_low)
save_csv(info_ci, "rater_information_ci", "main")

# --- F2. Rater fit: infit/outfit and S-X2 ---------------------------------------
# Infit/outfit on the observed ratings. S-X2 needs complete data: the missing
# ratings are imputed N_IMPUTATIONS times from the fitted model (plausible values),
# S-X2 is computed with all parameters fixed and pooled by averaging S-X2 and df.
# With ~90% of the cells imputed it is strongly conservative; not primary evidence.
message("01 GRM: rater fit (infit/outfit, S-X2 by multiple imputation)")
N_IMPUTATIONS <- if (QUICK) 2L else 20L
theta_eap <- fs[, "F1", drop = FALSE]
fit_infit <- itemfit(mod, fit_stats = "infit", Theta = theta_eap, method = "EAP")
sv_fixed <- mod2values(mod); sv_fixed$est <- FALSE
set.seed(SEED)
sx2_pooled <- bind_rows(lapply(seq_len(N_IMPUTATIONS), function(m) {
  pv <- fscores(mod, method = "EAP", plausible.draws = 1, verbose = FALSE)
  dat_m <- imputeMissing(mod, pv)
  mod_m <- mirt(dat_m, 1, itemtype = "graded", pars = sv_fixed, TOL = NaN, quadpts = MIRT_QUADPTS, verbose = FALSE)
  f <- itemfit(mod_m, fit_stats = "S_X2")
  data.frame(imputation = m, rater_id = f$item, S_X2 = f$S_X2, df = f$df.S_X2)
})) %>%
  group_by(rater_id) %>%
  summarise(S_X2_sd_over_imputations = sd(S_X2), S_X2 = mean(S_X2), df_S_X2 = mean(df), .groups = "drop") %>%
  mutate(p_S_X2 = pchisq(S_X2, df_S_X2, lower.tail = FALSE),
         RMSEA_S_X2 = sqrt(pmax(S_X2 - df_S_X2, 0) / (df_S_X2 * (nrow(wide) - 1))))
rater_fit <- fit_infit %>%
  rename(rater_id = item) %>%
  left_join(sx2_pooled, by = "rater_id") %>%
  left_join(category_usage %>% select(rater_id, n_ratings), by = "rater_id") %>%
  mutate(n_imputations = N_IMPUTATIONS, imputation_seed = SEED, share_cells_imputed = mean(!rated),
         flag_infit = infit < 0.7 | infit > 1.3, flag_outfit = outfit < 0.7 | outfit > 1.3)
save_csv(rater_fit, "rater_fit", "supplement")

# --- F3. Local dependence: Yen's Q3 ----------------------------------------------
# Correlation of two raters' residuals (observed - expected | EAP theta) over the
# products both rated. Pairs with < Q3_MIN_OVERLAP shared products are skipped;
# pairs below Q3_LOW_OVERLAP are flagged as unstable. Q3 is biased negatively
# with few raters per product, so pairs are judged by their deviation from the mean Q3.
Q3_MIN_OVERLAP <- 3L
Q3_LOW_OVERLAP <- 30L
obs_int <- extract.mirt(mod, "data")  # mirt's internal (recoded) categories
resid_mat <- vapply(seq_along(raters), function(j) obs_int[, j] - expected.item(extract.item(mod, j), theta_eap),
                    numeric(nrow(wide)))
pairs <- t(combn(length(raters), 2))  # (1,2), (1,3), ..., (J-1, J)
q3 <- bind_rows(lapply(seq_len(nrow(pairs)), function(p) {
  i <- pairs[p, 1]; j <- pairs[p, 2]
  both <- rated[, i] & rated[, j]
  n_common <- sum(both)
  q <- if (n_common >= Q3_MIN_OVERLAP && sd(resid_mat[both, i]) > 0 && sd(resid_mat[both, j]) > 0)
    cor(resid_mat[both, i], resid_mat[both, j]) else NA_real_
  data.frame(rater_1 = raters[i], rater_2 = raters[j], n_common = n_common, q3 = q)
}))
q3 <- q3 %>%
  mutate(q3_minus_mean = q3 - mean(q3, na.rm = TRUE),
         overlap_flag = case_when(n_common < Q3_MIN_OVERLAP ~ "not computable",
                                  n_common < Q3_LOW_OVERLAP ~ "low overlap (unstable)", TRUE ~ ""),
         flag_q3 = !is.na(q3) & n_common >= Q3_LOW_OVERLAP & abs(q3_minus_mean) > 0.2)
save_csv(q3, "q3", "supplement")

# --- F4. Global fit: C2 ------------------------------------------------------------
# C2 needs the bivariate moments of every rater pair; pairs without shared
# products have none, so C2 is undefined on this design (recorded, not forced).
n_pairs <- sum(upper.tri(overlap)); n_no_overlap <- sum(overlap[upper.tri(overlap)] == 0)
c2 <- tryCatch(M2(mod, type = "C2", calcNull = FALSE, quadpts = MIRT_QUADPTS), error = function(e) e)
global_fit <- data.frame(statistic = "C2", computable = !inherits(c2, "error") && is.finite(c2$M2),
                         rater_pairs = n_pairs, rater_pairs_without_overlap = n_no_overlap)
global_fit <- if (global_fit$computable) {
  cbind(global_fit, as.data.frame(c2), note = "Computed on pairwise-available moments; rater pairs without overlap contribute no information. Interpret with caution.")
} else {
  cbind(global_fit, note = if (inherits(c2, "error")) paste("Not computable:", conditionMessage(c2)) else
    sprintf("Not computable: %d of %d rater pairs share no products, so their bivariate moments and hence C2 are undefined.", n_no_overlap, n_pairs))
}
save_csv(global_fit, "global_fit", "supplement")

writeLines(c(paste("Run:", format(Sys.time()), " seed:", SEED, " quick:", QUICK), "", capture.output(sessionInfo())),
           file.path(DIRS$logs, "session_info.txt"))
message("01 GRM: done")
