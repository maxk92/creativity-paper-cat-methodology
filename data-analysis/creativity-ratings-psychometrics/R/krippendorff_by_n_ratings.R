# ============================================================
# Krippendorff's alpha (ordinal) by number of ratings per product
# ------------------------------------------------------------
# Standalone, hard-coded script (not part of run_pipeline.sh). Reads the
# pipeline's wide matrix (results/data/ratings_wide.csv: products x the 24
# retained raters, ratings coded 0-6) and computes irr::kripp.alpha
# (method = "ordinal", same call as R/02_comparison.R) on product subsets
# defined by how many ratings a product has: at least k and exactly k, for
# k = 2, 3, 4, 5. No bootstrap.
#
# Run from the analysis folder:  Rscript R/krippendorff_by_n_ratings.R
# Output: results/krippendorff_by_n_ratings.csv
# ============================================================
suppressPackageStartupMessages({library(readr); library(irr)})

wide_df <- read_csv("results/data/ratings_wide.csv", show_col_types = FALSE,
                    col_types = cols(product_id = "c", .default = "i"))
wide <- as.matrix(wide_df[, -1]); rownames(wide) <- wide_df$product_id
wide <- wide + 1L  # internal 0-6 back to the 1-7 scale (ordinal alpha is shift-invariant)
n_ratings <- rowSums(!is.na(wide))

alpha_for <- function(keep) {
  sub <- wide[keep, , drop = FALSE]
  sub <- sub[, colSums(!is.na(sub)) > 0, drop = FALSE]  # drop raters without ratings in the subset
  ka <- irr::kripp.alpha(t(sub), method = "ordinal")      # raters x units; NA handled natively
  data.frame(alpha = ka$value, n_products = nrow(sub), n_ratings = sum(!is.na(sub)),
             n_raters = ncol(sub), n_categories_used = length(unique(na.omit(as.vector(sub)))))
}

rows <- list()
for (k in 2:5) {
  rows[[length(rows) + 1]] <- cbind(subset = paste0("at least ", k, " ratings"), min_ratings = k, max_ratings = NA,
                                    alpha_for(n_ratings >= k))
  rows[[length(rows) + 1]] <- cbind(subset = paste0("exactly ", k, " ratings"), min_ratings = k, max_ratings = k,
                                    alpha_for(n_ratings == k))
}
out <- do.call(rbind, rows)
out$method <- "ordinal"; out$package <- paste("irr", packageVersion("irr"))
out$source <- "results/data/ratings_wide.csv"
print(out, row.names = FALSE)
write_csv(out, "results/krippendorff_by_n_ratings.csv", na = "")
