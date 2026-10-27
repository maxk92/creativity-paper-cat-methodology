# ============================================================
# 03 - Information and reliability of the GRM (spec section 4)
# ============================================================
# Definitions (identical throughout the pipeline, see jrt_functions.R):
#   rater information      I_j(theta) = sum_k P'_jk(theta)^2 / P_jk(theta)   (mirt::iteminfo)
#   information of a set R I_R(theta) = sum_{j in R} I_j(theta)   (local independence)
#   conditional reliability rel(theta) = I / (I + 1),  SE(theta) = 1 / sqrt(I + 1)
#
# Panel-level quantities (4b) are HYPOTHETICAL: a product rated by all raters.
# Product-level quantities (4c) use only the raters who rated that product.
# No products are filtered or weighted here; this script only computes and saves.
#
# Note on EAP shrinkage: with few ratings per product, EAP estimates are pulled
# towards the prior mean 0, so Var(theta_hat) < 1. This is expected, not an error.
#
# Outputs (results/grm/): rater_information_grid.csv, rater_information_summary.csv,
#   rater_information_shares.csv, panel_information_grid.csv, product_scores.csv,
#   reliability_summary.csv, reliability_ci.csv, rater_information_ci.csv, raw_mean_vs_grm.csv,
#   figures/grm_*.{png,svg}
# Reloads results/grm/model.rds, no refit. The parameter draws (4d) take a few minutes.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))

d <- load_design()
wide <- d$wide
rated <- !is.na(wide)
mod <- readRDS(file.path(DIR_GRM, "model.rds"))
assert_same_data(mod, wide, "GRM")
raters <- colnames(wide)
w_norm <- normal_weights(THETA_GRID)

# --- 4a. rater level ----------------------------------------------------------------
info_grid <- rater_information(mod, THETA_GRID)  # grid x raters
info_long <- as_tibble(info_grid) %>%
  mutate(theta = THETA_GRID) %>%
  pivot_longer(-theta, names_to = "rater", values_to = "info") %>%
  select(rater, theta, info)
save_csv(info_long, DIR_GRM, "rater_information_grid")

panel_info <- rowSums(info_grid)
idx_points <- vapply(THETA_POINTS, function(t) which.min(abs(THETA_GRID - t)), integer(1))
weighted_area <- colSums(info_grid * w_norm)
info_summary <- tibble(
  rater_id = raters,
  n_ratings = colSums(rated),
  info_weighted_area = weighted_area,  # integral of I_j(theta) * phi(theta)
  theta_at_max = THETA_GRID[apply(info_grid, 2, which.max)],
  info_max = apply(info_grid, 2, max),
  share_weighted = weighted_area / sum(weighted_area)
)
for (k in seq_along(THETA_POINTS)) {
  info_summary[[sprintf("share_at_theta_%+g", THETA_POINTS[k])]] <-
    info_grid[idx_points[k], ] / panel_info[idx_points[k]]
}
save_csv(info_summary, DIR_GRM, "rater_information_summary")

shares_long <- info_summary %>%
  select(rater_id, share_weighted, starts_with("share_at_theta")) %>%
  pivot_longer(-rater_id, names_to = "where", values_to = "share")
save_csv(shares_long, DIR_GRM, "rater_information_shares")

info_long$rater <- factor(info_long$rater, levels = raters)
p_info <- ggplot(info_long, aes(theta, info, colour = rater)) +
  geom_line(linewidth = 0.4) +
  scale_colour_viridis_d(end = 0.95) +
  labs(x = expression(theta), y = expression(I[j](theta)), colour = "Rater",
       title = "GRM rater information functions") +
  guides(colour = guide_legend(ncol = 2)) +
  theme_minimal(base_size = 10)
save_fig(p_info, "grm_rater_information")

shares_plot <- info_long %>%
  group_by(theta) %>% mutate(share = info / sum(info)) %>% ungroup()
p_share <- ggplot(shares_plot, aes(theta, share, fill = rater)) +
  geom_area(position = "stack", colour = NA) +
  scale_fill_viridis_d(end = 0.95) +
  labs(x = expression(theta), y = "Share of panel information", fill = "Rater",
       title = "Share of each rater in the full-panel information") +
  guides(fill = guide_legend(ncol = 2)) +
  theme_minimal(base_size = 10)
save_fig(p_share, "grm_rater_information_shares")

# --- 4b. full panel (hypothetical: every rater rates the product) --------------------------
panel <- tibble(theta = THETA_GRID, info = panel_info,
                se = se_from_info(panel_info), rel = rel_from_info(panel_info))
save_csv(panel, DIR_GRM, "panel_information_grid")

marginal_mirt <- marginal_rxx(mod)
# Same quantity on the fixed grid: 1 - E[1 / (I + 1)] = E[I / (I + 1)], theta ~ N(0, 1)
marginal_grid <- sum(w_norm * rel_from_info(panel_info)) / sum(w_norm)

p_panel <- panel %>%
  pivot_longer(c(info, rel), names_to = "quantity") %>%
  mutate(quantity = recode(quantity, info = "Information I(theta)",
                           rel = "Reliability I/(I+1)")) %>%
  ggplot(aes(theta, value)) + geom_line() +
  facet_wrap(~ quantity, scales = "free_y") +
  labs(x = expression(theta), y = NULL,
       title = "Full-panel information and conditional reliability (hypothetical: all raters)") +
  theme_minimal(base_size = 10)
save_fig(p_panel, "grm_panel_information_reliability", width = 9, height = 4)

# --- 4c. product level (actual rater set of each product) ------------------------------------
fs <- fscores(mod, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE)
theta_hat <- fs[, "F1"]
psd <- fs[, "SE_F1"]
info_at_eap <- product_information(mod, theta_hat, rated)

product_scores <- tibble(
  product_id = rownames(wide),
  theta_eap = theta_hat,
  psd = psd,
  rel_post = 1 - psd^2,
  info_at_eap = info_at_eap,
  rel_info = rel_from_info(info_at_eap),
  n_ratings = rowSums(rated),
  raters = apply(rated, 1, function(r) paste(raters[r], collapse = ";"))
)
stopifnot(nrow(product_scores) == nrow(wide), !anyNA(product_scores$theta_eap))
save_csv(product_scores, DIR_GRM, "product_scores")

# --- raw rater mean vs GRM score -------------------------------------------------------------
# What changes when rater differences are modelled: the unweighted mean of a
# product's ratings (common practice) against its GRM EAP score, separately for
# products with 1, 2 and 3+ ratings (pooling them would mix rater effects with
# the shrinkage that depends on the number of ratings). The raw mean is tied for
# almost all products, so agreement is measured by Kendall's tau-b and the share
# of product pairs with different raw means that the GRM orders the other way
# round. The same raw mean can map to different GRM scores, depending on the
# severity and discrimination of the raters who gave it: range of theta_hat
# among products with the same raw mean.
raw_mean <- rowMeans(wide, na.rm = TRUE) + SCALE_MIN  # back to the 1-7 scale
n_group <- function(n) ifelse(n >= 3, "3+", as.character(n))
raw_vs_grm_stats <- function(x, ref) {
  dx <- sign(outer(x, x, "-"))
  dr <- sign(outer(ref, ref, "-"))
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
save_csv(raw_vs_grm, DIR_GRM, "raw_mean_vs_grm")

p_raw <- tibble(raw = raw_mean, theta = theta_hat,
                n_ratings = paste(n_group(product_scores$n_ratings), "ratings")) %>%
  mutate(n_ratings = sub("^1 ratings$", "1 rating", n_ratings)) %>%
  ggplot(aes(raw, theta)) +
  geom_jitter(width = 0.04, height = 0, size = 0.5, alpha = 0.35) +
  facet_wrap(~ n_ratings) +
  scale_x_continuous(breaks = SCALE_MIN:SCALE_MAX) +
  labs(x = "Raw mean rating", y = expression("GRM score " * hat(theta)[EAP])) +
  theme_minimal(base_size = 10)
save_fig(p_raw, "grm_raw_mean_vs_theta", width = 9, height = 3.6)

# Guard against the wrong computation: full-panel information at theta_hat
# must exceed the product's own information for every product with < J raters.
full_panel_at_eap <- rowSums(rater_information(mod, theta_hat))
stopifnot(all(full_panel_at_eap[product_scores$n_ratings < ncol(wide)] >=
                info_at_eap[product_scores$n_ratings < ncol(wide)]))

empirical_mirt <- unname(empirical_rxx(fs))
empirical_manual <- var(theta_hat) / (var(theta_hat) + mean(psd^2))
stopifnot(abs(empirical_mirt - empirical_manual) < 1e-8)

cons_cor <- cor(product_scores$rel_post, product_scores$rel_info)
cons_diff <- product_scores$rel_info - product_scores$rel_post
rel_q <- quantile(product_scores$rel_post, c(0, .1, .25, .5, .75, .9, 1))

reliability_summary <- tibble(
  quantity = c(
    "empirical_marginal_reliability (primary; actual scores)",
    "model_based_marginal_reliability_mirt (hypothetical full panel)",
    "model_based_marginal_reliability_grid (check)",
    "var_theta_eap", "mean_psd_squared",
    "rel_post_min", "rel_post_p10", "rel_post_q1", "rel_post_median", "rel_post_q3",
    "rel_post_p90", "rel_post_max", "rel_post_mean", "rel_post_iqr",
    "consistency_cor_rel_post_rel_info", "consistency_mean_diff_rel_info_minus_rel_post",
    "consistency_max_abs_diff", "products_abs_diff_gt_0.1"),
  value = c(empirical_mirt, marginal_mirt, marginal_grid, var(theta_hat), mean(psd^2),
            rel_q, mean(product_scores$rel_post), IQR(product_scores$rel_post),
            cons_cor, mean(cons_diff), max(abs(cons_diff)), sum(abs(cons_diff) > 0.1))
)
save_csv(reliability_summary, DIR_GRM, "reliability_summary")

# --- 4d. uncertainty: parameter draws -------------------------------------------------------
# 95% intervals for the marginal reliabilities and for each rater's information.
# Parameters are drawn from their asymptotic normal distribution (estimates and
# Oakes covariance matrix). Draws with a <= 0 or GRM intercepts that are not
# strictly decreasing are rejected (the count is reported). For each accepted
# draw the GRM is evaluated with all parameters fixed, EAP scores and PSDs are
# recomputed, and the products are resampled with replacement for the empirical
# reliability, so its interval covers parameter uncertainty and product sampling.
# (mirt::draw_parameters() fails on this model in mirt 1.46.1, hence the manual draws.)
N_DRAWS <- if (SMOKE) 10L else 200L
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
  sv_d <- sv
  sv_d$value <- values
  sv_d$est <- FALSE
  mod_d <- suppressWarnings(mirt(wide, 1, itemtype = "graded", pars = sv_d, TOL = NaN,
                                 quadpts = MIRT_QUADPTS, verbose = FALSE))
  fs_d <- fscores(mod_d, method = "EAP", full.scores = TRUE, full.scores.SE = TRUE, verbose = FALSE)
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
  estimate = c(empirical_mirt, marginal_grid),
  ci_low = c(emp_ci[1], mb_ci[1]), ci_high = c(emp_ci[2], mb_ci[2]),
  n_draws = n_draws, n_draws_rejected = n_rejected, seed = SEED,
  method = c("percentile interval over parameter draws (asymptotic normal, Oakes covariance) with products resampled",
             "percentile interval over parameter draws (asymptotic normal, Oakes covariance); grid version of marginal_rxx"))
save_csv(reliability_ci, DIR_GRM, "reliability_ci")

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
save_csv(info_ci, DIR_GRM, "rater_information_ci")

rel_by_n <- product_scores %>%
  group_by(n_ratings) %>%
  summarise(n_products = n(), rel_post_mean = mean(rel_post), rel_post_median = median(rel_post),
            rel_info_mean = mean(rel_info), psd_mean = mean(psd), .groups = "drop")
save_csv(rel_by_n, DIR_GRM, "reliability_by_n_ratings")

# Products with the largest disagreement between the two product-level indices.
save_csv(product_scores %>% mutate(diff = rel_info - rel_post) %>%
           arrange(desc(abs(diff))) %>% head(25),
         DIR_GRM, "reliability_consistency_largest_differences")

p_hist <- ggplot(product_scores, aes(rel_post)) +
  geom_histogram(bins = 50, fill = "grey40") +
  labs(x = expression(rel[post] == 1 - PSD^2), y = "Products",
       title = "Product-level reliability (posterior-based)") +
  theme_minimal(base_size = 10)
save_fig(p_hist, "grm_rel_post_histogram", width = 7, height = 4)

p_n <- ggplot(product_scores, aes(factor(n_ratings), rel_post)) +
  geom_boxplot(outlier.size = 0.4) +
  labs(x = "Number of ratings", y = expression(rel[post]),
       title = "Product-level reliability by number of ratings") +
  theme_minimal(base_size = 10)
save_fig(p_n, "grm_rel_post_by_n_ratings", width = 7, height = 4)

p_theta <- ggplot(product_scores, aes(theta_eap, rel_post, colour = factor(pmin(n_ratings, 5)))) +
  geom_point(size = 0.6, alpha = 0.5) +
  scale_colour_viridis_d(labels = c("1", "2", "3", "4", "5+"), end = 0.9) +
  labs(x = expression(hat(theta)[EAP]), y = expression(rel[post]), colour = "Ratings",
       title = "Product-level reliability by EAP estimate") +
  theme_minimal(base_size = 10)
save_fig(p_theta, "grm_rel_post_by_theta", width = 7, height = 4)

p_cons <- ggplot(product_scores, aes(rel_info, rel_post)) +
  geom_abline(linetype = "dashed", colour = "grey50") +
  geom_point(size = 0.6, alpha = 0.4) +
  labs(x = expression(rel[info] == I[n](hat(theta)) / (I[n](hat(theta)) + 1)),
       y = expression(rel[post] == 1 - PSD^2),
       title = "Consistency of the two product-level reliability indices") +
  theme_minimal(base_size = 10)
save_fig(p_cons, "grm_rel_consistency", width = 6, height = 5)

print(reliability_summary, n = Inf)
write_warnings("03_grm_information")
write_session_info("03_grm_information")
message("03 GRM information: done")
