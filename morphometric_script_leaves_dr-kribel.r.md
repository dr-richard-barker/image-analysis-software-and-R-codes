# Morphometric\_script\_leaves\_Dr Kribel.R

setwd("\~/Dropbox/1\_misc/Richards\_plots/outlines\_edited") library(Momocs)

#### ### ### ### ### ##\#

#### First we read in the outlines

#### ### ### ### ### ##\#

jpg.list <- list.files(pattern = ".jpg") import\_jpg(jpg.list)->returns\_leaves Out(returns\_leaves)-> leaves

#### look at the outlines

panel(leaves, col=1)

#### Lets read in the grouping variable which is in the folder with the outlines

read.csv("groups.csv")-> groups groups\_leaves <-data.frame(groups\[,1:2]) leaves$fac <- groups\_leaves

par(mfrow=c(1,3)) stack(leaves) coo\_center(leaves) -> centered\_leaves stack(centered\_leaves) coo\_template(centered\_leaves) -> template\_leaves stack(template\_leaves)

#### Now lets run the elliptic Fourier analysis

efourier(template\_leaves, norm=T, nb.h=32, smooth.it=1)-> efou\_leaves

#### And now the PCA of the eFa harmonic coefficients

pca\_leaves <- PCA(efou\_leaves, center=T)

#### Here we can see the contribution of each component

summary(pca\_leaves)

#### Lets create a vector of colors for coloring

cols<-c("red","blue")

plant\_col <- character(length(groups$plant)) plant\_col\[groups$plant == "control"] <- "blue" plant\_col\[groups$plant == "treatment"] <- "red"

#### Now lets save a pdf with the results

pdf("leaves\_Richard.pdf") panel(leaves, col=plant\_col, names="plant", cex=0.3) plot(pca\_leaves, "plant",xax = 1, yax = 2, ellipsesax=T, density=F, contour=F,ellipses=T, col=cols, eigen=F, rug=F, delaunay=F, loadings=F, pch=16,cex=0.4, points=T) plot(pca\_leaves, "plant", pos="li",xax = 1, yax = 2, ellipsesax=T, density=F, size.shp=0.5,contour=F,ellipses=T, col=cols, eigen=F, rug=F, delaunay=F, loadings=F, cex=0.75, points=F) PCcontrib(pca\_leaves) boxplot(pca\_leaves, "plant",cex.legend = 0.75) mshapes(efou\_leaves, "plant") -> mshapes\_pca\_leaves mshapes\_pca\_leaves$shp -> mshapes tps\_iso(mshapes$control, mshapes$treatment)

par(mfrow=c(1,2))\
coo\_plot(mshapes$control, col="blue", border=1, lwd=1, centroid=F, xy.axis=F, first.point=F) title('Mean shape control') coo\_plot(mshapes$treatment, col="red", border=1, lwd=1, centroid=F, xy.axis=F, first.point=F) title('Mean shape treatment')

dev.off()
