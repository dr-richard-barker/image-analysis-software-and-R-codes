install.packages("shiny")
shiny::runGitHub("shiny-phyloseq","joey711")

source("https://bioconductor.org/biocLite.R")
biocLite("phyloseq")

install.packages('heatmaply')