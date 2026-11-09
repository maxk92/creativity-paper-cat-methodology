# ============================================================
# 08 - Reliability if every product had at least MIN_RATINGS ratings
# ============================================================
# Projection from the fitted GRM, like 07, but built on the ACTUAL design instead
# of an idealised one. Two designs are simulated with the same machinery:
#   "actual"        each product keeps exactly the raters who rated it
#                   (validation: should reproduce the observed empirical
#                   marginal reliability of the real scores, 03);
#   "min_<k>"       each product keeps its raters, and products with fewer than
#                   MIN_RATINGS ratings get additional raters, drawn at random
#                   (equal probability) from the panel raters who had not rated
#                   them, until they have MIN_RATINGS. Products that already have
#                   MIN_RATINGS or more are unchanged.
# Per replication: products theta ~ N(0, 1) (one per real product), ratings drawn
# from the fitted GRM, raters masked by the design, EAP scoring with the fitted
# parameters (fixed). Same summaries as 07: empirical marginal reliability
# Var(theta_hat) / (Var(theta_hat) + mean PSD^2), squared correlation with the
# true theta, mean product-level rel_post = 1 - PSD^2.
# The parameters are treated as known (no parameter uncertainty).
#
# Output (results/grm/): reliability_min_ratings.csv
# Reloads results/grm/model.rds, no refit.
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))

d <- load_design()
wide <- d$wide
mod <- readRDS(file.path(DIR_GRM, "model.rds"))
assert_same_data(mod, wide, "GRM")

MIN_RATINGS <- 4L
N_REPS <- if (SMOKE) 3L else 50L

rated <- !is.na(wide)
n_obs <- rowSums(rated)
N <- nrow(wide)

top_up <- function(rated, k) {
  # add random raters (not yet rating the product) until each product has >= k
  for (i in which(rowSums(rated) < k)) {
    free <- which(!rated[i, ])
    need <- k - sum(rated[i, ])
    rated[i, free[sample.int(length(free), need)]] <- TRUE
  }
  rated
}

one_rep <- function(design) {
  mask <- if (design == "actual") rated else top_up(rated, MIN_RATINGS)
  theta <- rnorm(N)
  ratings <- simdata(model = mod, Theta = matrix(theta))
  ratings[!mask] <- NA
  fs <- fscores(mod, response.pattern = ratings, method = "EAP",
                append_response.pattern = FALSE, verbose = FALSE)
  th <- fs[, "F1"]; psd <- fs[, "SE_F1"]
  c(empirical = var(th) / (var(th) + mean(psd^2)),
    true_r2 = cor(th, theta)^2,
    mean_rel_post = mean(1 - psd^2),
    n_ratings = sum(mask))
}

# observed value of the real scores (03), for the validation row
obs_rel <- readr::read_csv(file.path(DIR_GRM, "reliability_summary.csv"), show_col_types = FALSE) %>%
  filter(grepl("^empirical_marginal_reliability", quantity)) %>% pull(value)
stopifnot(length(obs_rel) == 1)

designs <- c("actual", paste0("min_", MIN_RATINGS))
set.seed(SEED)
sims <- bind_rows(lapply(designs, function(dz) {
  reps <- t(vapply(seq_len(N_REPS), function(r) one_rep(dz), numeric(4)))
  as_tibble(reps) %>% mutate(design = dz, rep = seq_len(N_REPS))
}))

out <- sims %>%
  pivot_longer(c(empirical, true_r2, mean_rel_post), names_to = "quantity") %>%
  group_by(design, quantity) %>%
  summarise(mean = mean(value), q025 = unname(quantile(value, 0.025)),
            q975 = unname(quantile(value, 0.975)), n_ratings = first(n_ratings), .groups = "drop") %>%
  pivot_wider(names_from = quantity, values_from = c(mean, q025, q975), names_glue = "{quantity}_{.value}") %>%
  rename_with(~ sub("_mean$", "", .x)) %>%
  mutate(min_ratings = ifelse(design == "actual", NA_integer_, MIN_RATINGS),
         n_products = N,
         n_products_topped_up = ifelse(design == "actual", 0L, sum(n_obs < MIN_RATINGS)),
         n_ratings_added = n_ratings - sum(rated),
         observed_empirical_reliability = obs_rel,
         n_reps = N_REPS, seed = SEED) %>%
  select(design, min_ratings, n_products, n_products_topped_up, n_ratings, n_ratings_added,
         starts_with("empirical"), starts_with("true_r2"), starts_with("mean_rel_post"),
         observed_empirical_reliability, n_reps, seed) %>%
  arrange(match(design, designs))
save_csv(out, DIR_GRM, "reliability_min_ratings")
print(out %>% select(design, n_ratings, n_ratings_added, empirical, empirical_q025, empirical_q975, true_r2))

write_session_info("08_reliability_min_ratings")
write_warnings("08_reliability_min_ratings")
message("08 reliability with minimum ratings: done")
