# ============================================================
# 07 - Reliability by number of ratings: projection from the fitted GRM
# ============================================================
# The observed relation between the number of ratings and reliability
# (reliability_by_n_ratings.csv) is confounded: products with more ratings were
# rated by different raters. This script projects it from the fitted GRM instead.
# For k = 1 ... K_MAX ratings per product it simulates products theta ~ N(0, 1),
# gives each product k raters, draws their ratings from the fitted GRM, and
# scores the products by EAP with the fitted parameters (fixed). Rater sets:
#   random              k distinct raters drawn uniformly for each product
#   most_informative    the k raters with the highest information per rating
#   least_informative   the k raters with the lowest information per rating
# The last two bracket what the choice of raters can do at a given k.
# Per replication: empirical marginal reliability Var(theta_hat) /
# (Var(theta_hat) + mean PSD^2) (as for the real scores), the squared correlation
# of theta_hat with the true theta, and the mean product-level rel_post = 1 - PSD^2.
# The parameters are treated as known (no parameter uncertainty).
#
# Outputs (results/grm/): reliability_projection.csv,
#   figures/grm_reliability_projection.{png,svg}
# Reloads results/grm/model.rds and rater_information_summary.csv, no refit.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))

d <- load_design()
wide <- d$wide
mod <- readRDS(file.path(DIR_GRM, "model.rds"))
assert_same_data(mod, wide, "GRM")
raters <- colnames(wide)
J <- length(raters)

K_MAX <- min(10L, J)
N_PRODUCTS <- if (SMOKE) 200L else 2000L
N_REPS <- if (SMOKE) 3L else 50L

info <- read_csv(file.path(DIR_GRM, "rater_information_summary.csv"), show_col_types = FALSE)
info_order <- info$rater_id[order(info$info_weighted_area, decreasing = TRUE)]
stopifnot(setequal(info_order, raters))

rater_sets <- function(scheme, k, n) {
  # n x J logical matrix: which raters rate each product
  sel <- matrix(FALSE, n, J, dimnames = list(NULL, raters))
  if (scheme == "random") {
    for (i in seq_len(n)) sel[i, sample.int(J, k)] <- TRUE
  } else {
    fixed <- if (scheme == "most_informative") head(info_order, k) else tail(info_order, k)
    sel[, fixed] <- TRUE
  }
  sel
}

one_rep <- function(scheme, k) {
  theta <- rnorm(N_PRODUCTS)
  ratings <- simdata(model = mod, Theta = matrix(theta))
  ratings[!rater_sets(scheme, k, N_PRODUCTS)] <- NA
  fs <- fscores(mod, response.pattern = ratings, method = "EAP",
                append_response.pattern = FALSE, verbose = FALSE)
  th <- fs[, "F1"]; psd <- fs[, "SE_F1"]
  c(empirical = var(th) / (var(th) + mean(psd^2)),
    true_r2 = cor(th, theta)^2,
    mean_rel_post = mean(1 - psd^2))
}

set.seed(SEED)
grid <- expand.grid(k = seq_len(K_MAX),
                    scheme = c("random", "most_informative", "least_informative"),
                    stringsAsFactors = FALSE)
sims <- bind_rows(lapply(seq_len(nrow(grid)), function(g) {
  reps <- t(vapply(seq_len(N_REPS), function(r) one_rep(grid$scheme[g], grid$k[g]), numeric(3)))
  as_tibble(reps) %>% mutate(scheme = grid$scheme[g], k = grid$k[g], rep = seq_len(N_REPS))
}))

projection <- sims %>%
  pivot_longer(c(empirical, true_r2, mean_rel_post), names_to = "quantity") %>%
  group_by(scheme, k, quantity) %>%
  summarise(mean = mean(value), q025 = unname(quantile(value, 0.025)),
            q975 = unname(quantile(value, 0.975)), .groups = "drop") %>%
  pivot_wider(names_from = quantity, values_from = c(mean, q025, q975), names_glue = "{quantity}_{.value}") %>%
  select(scheme, k, starts_with("empirical"), starts_with("true_r2"), starts_with("mean_rel_post")) %>%
  rename_with(~ sub("_mean$", "", .x)) %>%
  mutate(n_products_per_rep = N_PRODUCTS, n_reps = N_REPS, seed = SEED) %>%
  arrange(factor(scheme, c("random", "most_informative", "least_informative")), k)
save_csv(projection, DIR_GRM, "reliability_projection")

p_proj <- projection %>%
  mutate(scheme = recode(scheme, random = "Random raters",
                         most_informative = "Most informative raters",
                         least_informative = "Least informative raters")) %>%
  ggplot(aes(k, empirical, colour = scheme, fill = scheme)) +
  geom_ribbon(aes(ymin = empirical_q025, ymax = empirical_q975), alpha = 0.2, colour = NA) +
  geom_line() + geom_point(size = 1.2) +
  scale_x_continuous(breaks = seq_len(K_MAX)) +
  scale_colour_viridis_d(end = 0.8) + scale_fill_viridis_d(end = 0.8) +
  labs(x = "Ratings per product (k)", y = "Empirical marginal reliability", colour = NULL, fill = NULL) +
  theme_minimal(base_size = 10) + theme(legend.position = "bottom")
save_fig(p_proj, "grm_reliability_projection", width = 7, height = 4.5)

write_session_info("07_reliability_projection")
write_warnings("07_reliability_projection")
message("07 reliability projection: done")
