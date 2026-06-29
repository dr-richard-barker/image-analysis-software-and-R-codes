# R dependencies for the statistics & morphometrics scripts in this repository.
#
# Run once:   Rscript install.R
#
# Covers: scripts/r/rootnav-stats/ (RootNav/weGAS/EVT/SVT statistics) and
#         scripts/r/morphometrics/ (leaf outline analysis with Momocs).

pkgs <- c(
  # path management (lets scripts use here::here() instead of absolute paths)
  "here",
  # statistics
  "MASS", "car", "Hmisc", "xtable",
  # data wrangling
  "dplyr", "reshape2",
  # morphometrics + image IO
  "Momocs", "jpeg"
  # note: "stats" is part of base R — no install needed
)

installed <- rownames(installed.packages())
to_install <- setdiff(pkgs, installed)

if (length(to_install) == 0) {
  message("All required R packages are already installed.")
} else {
  message("Installing: ", paste(to_install, collapse = ", "))
  install.packages(to_install, repos = "https://cloud.r-project.org")
}

# Optional: pin versions reproducibly with renv instead of this script:
#   install.packages("renv"); renv::init(); renv::snapshot()
# which writes an renv.lock capturing exact versions.
