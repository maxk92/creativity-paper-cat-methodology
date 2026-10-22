# ============================================================
# 01 - Data and design (spec section 2)
# ============================================================
# Builds the single, checked data basis that ALL models use:
#   results/data/ratings_long.csv     product_id, rater_id, rating (1-7), rating_internal (0-6)
#   results/data/ratings_wide.csv     products x raters, internal coding 0-6, NA = not rated
#   results/data/data_fingerprint.txt asserted by every later script
# plus the design checks (duplicates, categories, connectivity, overlap, descriptives).
# Light: no models are fitted here, so this script can run locally.
#
# Run from the analysis folder:  Rscript R/01_data_design.R
# ============================================================

source(file.path(local({a <- grep("^--file=", commandArgs(FALSE), value = TRUE)
                        if (length(a)) dirname(sub("^--file=", "", a)) else "R"}), "jrt_functions.R"))
suppressPackageStartupMessages(library(igraph))

message("01 data/design: reading ", INPUT_CSV)
raw <- readr::read_csv(INPUT_CSV, show_col_types = FALSE,
                       col_types = cols(action_id = "c", rater_id = "c", .default = "?"))

# --- long format --------------------------------------------------------------
# Only the creativity rating is modelled (decision 2026-10-22). The secondary
# dimensions technical_correctness / aesthetic_appeal are not used by any model.
long <- raw %>%
  transmute(product_id = action_id, rater_id,
            rating = as.integer(rating_numeric),
            rating_internal = rating - SCALE_MIN,
            rating_order = as.integer(rating_order))

stopifnot(!anyNA(long$product_id), !anyNA(long$rater_id), !anyNA(long$rating))
stopifnot(all(long$rating >= SCALE_MIN & long$rating <= SCALE_MAX))

# --- check: duplicate ratings --------------------------------------------------
# 00_data_loading_preprocessing.ipynb resolves duplicates ("last entry kept") and
# lists them in results/tables/flagged_duplicate_rater_action_pairs.csv. Here we
# (a) assert that none remain and (b) report how many there were and whether the
# repeated entries disagree. Nothing is averaged.
dup_left <- long %>% count(product_id, rater_id) %>% filter(n > 1)
if (nrow(dup_left) > 0) stop(nrow(dup_left), " duplicate product-rater pairs in the input. ",
                             "Resolve them in 00 (do not average here).")
flagged_path <- file.path(ROOT, "results", "tables", "flagged_duplicate_rater_action_pairs.csv")
dup_report <- if (file.exists(flagged_path)) {
  readr::read_csv(flagged_path, show_col_types = FALSE, col_types = cols(.default = "c")) %>%
    group_by(product_id = action_id, rater_id) %>%
    summarise(n_entries = n(), ratings = paste(rating, collapse = " | "),
              conflicting = n_distinct(rating) > 1, .groups = "drop") %>%
    mutate(resolution_in_00 = "last entry kept")
} else {
  tibble(product_id = character(), rater_id = character(), n_entries = integer(),
         ratings = character(), conflicting = logical(), resolution_in_00 = character())
}
save_csv(dup_report, DIR_DATA, "duplicate_ratings_report")
message(sprintf("  duplicates resolved upstream: %d pairs, %d with conflicting values",
                nrow(dup_report), sum(dup_report$conflicting)))

save_csv(long, DIR_DATA, "ratings_long")

# --- wide matrix ---------------------------------------------------------------
raters <- rater_order(unique(long$rater_id))
wide_df <- long %>%
  select(product_id, rater_id, rating_internal) %>%
  pivot_wider(names_from = rater_id, values_from = rating_internal) %>%
  arrange(product_id) %>%
  select(product_id, all_of(raters))
save_csv(wide_df, DIR_DATA, "ratings_wide")
wide <- as.matrix(wide_df[, -1])
storage.mode(wide) <- "integer"
rownames(wide) <- wide_df$product_id
stopifnot(sum(!is.na(wide)) == nrow(long), all(rowSums(!is.na(wide)) >= 1))
writeLines(data_fingerprint(wide), file.path(DIR_DATA, "data_fingerprint.txt"))

# --- check: categories -----------------------------------------------------------
# Scale 1-7, coded 0-6 internally. mirt recodes the OBSERVED categories of each
# rater to consecutive integers: a rater who never uses a category gets fewer
# categories. A missing end category only removes the outermost threshold(s); a
# missing INTERNAL category shifts all higher thresholds, so they are no longer
# comparable with other raters. The rating scale model (shared thresholds) needs
# the same number of categories for every rater. Decision 2026-10-22: keep all
# 7 categories, document the gaps (see AUDIT.md).
cat_counts <- long %>%
  mutate(category = factor(rating, levels = SCALE_MIN:SCALE_MAX)) %>%
  count(rater_id, category, .drop = FALSE) %>%
  pivot_wider(names_from = category, values_from = n, names_prefix = "cat_")
category_usage <- cat_counts %>%
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
  arrange(rater_id)
save_csv(category_usage, DIR_DATA, "category_usage")
message(sprintf("  raters with category gaps: %d of %d (internal gap: %s)",
                sum(category_usage$end_gap | category_usage$internal_gap), nrow(category_usage),
                paste(category_usage$rater_id[category_usage$internal_gap], collapse = ", ")))

# --- check: connectivity ----------------------------------------------------------
g <- graph_from_data_frame(
  long %>% transmute(from = paste0("P::", product_id), to = paste0("R::", rater_id)),
  directed = FALSE)
comp <- components(g)
connectivity <- tibble(
  n_components = comp$no,
  largest_component_nodes = max(comp$csize),
  n_products = n_distinct(long$product_id),
  n_raters = n_distinct(long$rater_id))
save_csv(connectivity, DIR_DATA, "connectivity")
if (comp$no != 1) stop("The product-rater graph has ", comp$no, " components. ",
                       "A disconnected design is a hard error for all models (spec 2).")
message("  design is connected (1 component)")

# --- rater overlap ------------------------------------------------------------------
rated <- !is.na(wide)
overlap <- crossprod(rated * 1L)  # diagonal = number of ratings per rater
save_csv(as_tibble(overlap, rownames = "rater_id"), DIR_DATA, "rater_overlap")

# --- descriptives ---------------------------------------------------------------------
per_product <- long %>% count(product_id, name = "n_ratings")
products_dist <- per_product %>% count(n_ratings, name = "n_products") %>%
  mutate(share = n_products / sum(n_products))
save_csv(products_dist, DIR_DATA, "design_summary_ratings_per_product")

rater_desc <- long %>%
  group_by(rater_id) %>%
  summarise(n_ratings = n(), mean = mean(rating), sd = sd(rating),
            median = median(rating), .groups = "drop") %>%
  mutate(rater_id = factor(rater_id, levels = raters)) %>% arrange(rater_id)
save_csv(rater_desc, DIR_DATA, "design_summary_raters")

pair_overlap <- overlap[upper.tri(overlap)]
design_summary <- tibble(
  quantity = c("n_ratings", "n_products", "n_raters", "n_categories", "scale",
               "internal_coding", "ratings_per_product_mean", "ratings_per_product_median",
               "ratings_per_product_min", "ratings_per_product_max",
               "ratings_per_product_harmonic_mean", "products_with_1_rating",
               "ratings_per_rater_min", "ratings_per_rater_max", "matrix_fill",
               "n_components", "rater_pairs_total", "rater_pairs_without_overlap",
               "rater_pairs_overlap_median", "raters_with_category_gaps",
               "raters_with_internal_gap", "duplicate_pairs_resolved_in_00",
               "duplicate_pairs_conflicting", "data_fingerprint"),
  value = c(nrow(long), nrow(wide), ncol(wide), K_CATEGORIES, "1-7", "rating - 1 (0-6)",
            mean(per_product$n_ratings), median(per_product$n_ratings),
            min(per_product$n_ratings), max(per_product$n_ratings),
            1 / mean(1 / per_product$n_ratings), sum(per_product$n_ratings == 1),
            min(rater_desc$n_ratings), max(rater_desc$n_ratings), mean(rated),
            comp$no, length(pair_overlap), sum(pair_overlap == 0), median(pair_overlap),
            sum(category_usage$end_gap | category_usage$internal_gap),
            sum(category_usage$internal_gap), nrow(dup_report), sum(dup_report$conflicting),
            data_fingerprint(wide)) %>% as.character())
save_csv(design_summary, DIR_DATA, "design_summary")
print(design_summary, n = Inf)

write_warnings("01_data_design")
write_session_info("01_data_design")
message("01 data/design: done")
