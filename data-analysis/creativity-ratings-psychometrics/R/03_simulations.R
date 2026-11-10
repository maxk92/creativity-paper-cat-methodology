# ============================================================
# 03 - Reliability by number of ratings: two simulations from the fitted GRM
# ============================================================
# The observed relation between the number of ratings and reliability is
# confounded (products with more ratings were rated by different raters), so it
# is projected from the fitted GRM instead. In both simulations the products get
# theta ~ N(0, 1), their ratings are drawn from the fitted GRM, and they are
# scored by EAP with the fitted parameters treated as known (no parameter
# uncertainty). Per replication: empirical marginal reliability
# Var(theta_hat) / (Var(theta_hat) + mean PSD^2), squared correlation of
# theta_hat with the true theta, and mean product-level rel_post = 1 - PSD^2.
#
#   Projection   k = 1 ... K_MAX ratings per simulated product from k distinct
#                raters of the panel, drawn at random with equal probability.
#   Top-up       the ACTUAL rater-product assignment; "actual" keeps it as is
#                (validation: should reproduce the observed empirical
#                reliability); "min_4" adds randomly drawn raters to products
#                with fewer than MIN_RATINGS ratings until they have MIN_RATINGS.
#
# Run after 01_grm.R:  Rscript R/03_simulations.R   (a few minutes)
# ============================================================

source(if (interactive()) "R/jrt_functions.R" else
  file.path(dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1])), "jrt_functions.R"))

wide_df <- read_csv(file.path(DIRS$data, "ratings_wide.csv"), show_col_types = FALSE, col_types = cols(product_id = "c", .default = "i"))
wide <- as.matrix(wide_df[, -1]); rownames(wide) <- wide_df$product_id
rated <- !is.na(wide)
mod <- readRDS(file.path(DIRS$models, "grm.rds"))
raters <- colnames(wide)
J <- length(raters)
N <- nrow(wide)

summarise_rep <- function(ratings, theta) {
  fs <- fscores(mod, response.pattern = ratings, method = "EAP", append_response.pattern = FALSE, verbose = FALSE)
  th <- fs[, "F1"]; psd <- fs[, "SE_F1"]
  c(empirical = var(th) / (var(th) + mean(psd^2)), true_r2 = cor(th, theta)^2, mean_rel_post = mean(1 - psd^2))
}
summarise_sims <- function(sims, by) {
  sims %>%
    pivot_longer(c(empirical, true_r2, mean_rel_post), names_to = "quantity") %>%
    group_by(across(all_of(by)), quantity) %>%
    summarise(mean = mean(value), q025 = unname(quantile(value, 0.025)), q975 = unname(quantile(value, 0.975)),
              .groups = "drop") %>%
    pivot_wider(names_from = quantity, values_from = c(mean, q025, q975), names_glue = "{quantity}_{.value}") %>%
    rename_with(~ sub("_mean$", "", .x))
}

# --- Projection: k random raters per product ------------------------------------------
K_MAX <- min(10L, J)
N_PRODUCTS <- if (QUICK) 200L else 2000L
N_REPS <- if (QUICK) 3L else 50L
random_raters <- function(k, n) {  # n x J logical matrix: which raters rate each product
  sel <- matrix(FALSE, n, J, dimnames = list(NULL, raters))
  for (i in seq_len(n)) sel[i, sample.int(J, k)] <- TRUE
  sel
}
one_rep_projection <- function(k) {
  theta <- rnorm(N_PRODUCTS)
  ratings <- simdata(model = mod, Theta = matrix(theta))
  ratings[!random_raters(k, N_PRODUCTS)] <- NA
  summarise_rep(ratings, theta)
}
message("03: projection, k = 1..", K_MAX, " (", N_REPS, " replications x ", N_PRODUCTS, " products)")
set.seed(SEED)
sims <- bind_rows(lapply(seq_len(K_MAX), function(k) {
  reps <- t(vapply(seq_len(N_REPS), function(r) one_rep_projection(k), numeric(3)))
  as_tibble(reps) %>% mutate(k = k, rep = seq_len(N_REPS))
}))
projection <- summarise_sims(sims, "k") %>%
  select(k, starts_with("empirical"), starts_with("true_r2"), starts_with("mean_rel_post")) %>%
  mutate(n_products_per_rep = N_PRODUCTS, n_reps = N_REPS, seed = SEED) %>%
  arrange(k)
save_csv(projection, "reliability_projection", "main")

p_proj <- ggplot(projection, aes(k, empirical)) +
  geom_ribbon(aes(ymin = empirical_q025, ymax = empirical_q975), alpha = 0.2) +
  geom_line() + geom_point(size = 1.2) +
  scale_x_continuous(breaks = seq_len(K_MAX)) +
  labs(x = "Ratings per product (k)", y = "Empirical marginal reliability") +
  theme_minimal(base_size = 10)
save_fig(p_proj, "grm_reliability_projection", "supplement", width = 6, height = 3.8)

# --- Top-up: actual design, and at least MIN_RATINGS ratings per product -----------------
MIN_RATINGS <- 4L
n_obs <- rowSums(rated)
top_up <- function(rated, k) {  # add random raters (not yet rating the product) until each product has >= k
  for (i in which(rowSums(rated) < k)) {
    free <- which(!rated[i, ]); need <- k - sum(rated[i, ])
    rated[i, free[sample.int(length(free), need)]] <- TRUE
  }
  rated
}
one_rep_topup <- function(design) {
  mask <- if (design == "actual") rated else top_up(rated, MIN_RATINGS)
  theta <- rnorm(N)
  ratings <- simdata(model = mod, Theta = matrix(theta))
  ratings[!mask] <- NA
  c(summarise_rep(ratings, theta), n_ratings = sum(mask))
}
obs_rel <- read_csv(file.path(DIRS$supplement, "reliability_summary.csv"), show_col_types = FALSE) %>%
  filter(grepl("^empirical_marginal_reliability", quantity)) %>% pull(value)
designs <- c("actual", paste0("min_", MIN_RATINGS))
message("03: top-up simulation (", N_REPS, " replications)")
set.seed(SEED)
sims <- bind_rows(lapply(designs, function(dz) {
  reps <- t(vapply(seq_len(N_REPS), function(r) one_rep_topup(dz), numeric(4)))
  as_tibble(reps) %>% mutate(design = dz, rep = seq_len(N_REPS))
}))
min_ratings <- summarise_sims(sims %>% select(-n_ratings), "design") %>%
  left_join(sims %>% group_by(design) %>% summarise(n_ratings = first(n_ratings), .groups = "drop"), by = "design") %>%
  mutate(min_ratings = ifelse(design == "actual", NA_integer_, MIN_RATINGS), n_products = N,
         n_products_topped_up = ifelse(design == "actual", 0L, sum(n_obs < MIN_RATINGS)),
         n_ratings_added = n_ratings - sum(rated), observed_empirical_reliability = obs_rel,
         n_reps = N_REPS, seed = SEED) %>%
  select(design, min_ratings, n_products, n_products_topped_up, n_ratings, n_ratings_added,
         starts_with("empirical"), starts_with("true_r2"), starts_with("mean_rel_post"),
         observed_empirical_reliability, n_reps, seed) %>%
  arrange(match(design, designs))
save_csv(min_ratings, "reliability_min_ratings", "supplement")
print(min_ratings %>% select(design, n_ratings, n_ratings_added, empirical, empirical_q025, empirical_q975, true_r2))
message("03 simulations: done")
