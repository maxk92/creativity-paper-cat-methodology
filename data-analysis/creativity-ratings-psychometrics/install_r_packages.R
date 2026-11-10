# R packages for the JRT pipeline in R/. Usage (from this folder): Rscript install_r_packages.R
# Installs Depends/Imports only (dependencies = TRUE would pull in a huge Suggests tree).
pkgs <- c("dplyr", "tidyr", "readr", "ggplot2", "svglite",  # data handling, figures
          "igraph",                                         # design connectivity
          "mirt", "sirt",                                   # IRT / facet models
          "psych", "irr")                                   # Cronbach's and Krippendorff's alpha
missing <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing)) install.packages(missing, repos = "https://cloud.r-project.org",
                                      dependencies = c("Depends", "Imports", "LinkingTo"))
print(data.frame(package = pkgs, installed = vapply(pkgs, requireNamespace, logical(1), quietly = TRUE)), row.names = FALSE)
