install.packages("shiny")

library(shiny)
shiny::runGitHub("archidart/astrodart", "astridart")
/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX5_RSML_day4_/FL_&_GC
/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX_corners_for_R
/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX_RSML_day_corners
/Users/richardbarker/Desktop/APEX_RSML
/Users/richardbarker/Desktop/Cotton_RSML_Soil

/Users/richardbarker/Desktop/APEX_RSML_corners_fixed_2_7_18

/Users/richardbarker/Desktop/DataRevised

library(shiny)
shiny::runGitHub("plantmodelling/archishiny", "plantmodelling")

## Using this RSML & archiDART package will link into the Primal Machine learning system
##library(shiny)
##shiny::runGitHub("plantmodelling/primal", "plantmodelling")

library(devtools)
install_github("archiDART/archiDART")
library(archiDART)
library(ggplot2)
library(tidyverse)
library(Hmisc)
library(DT) #
library(shinyBS) #
library(plotly)
library(gridExtra) #
library(ggrepel) #
library(vegan)

########################################//

##path <- "~/Desktop/EVT_and_SVT_RSML_format_v2/"
path<- "~/Desktop/Desktop - Richard’s MacBook Air/APEX5_RSML_day4/FL_&_GC"
path<-"/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX5_RSML_day4_/FL_&_GC"
path<-"/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX_corners_for_R/Just_RSML"
path<-"/Users/richardbarker/Desktop/Just_RSML"
path<-"/Users/richardbarker/Desktop/APEX_RSMLL"
path<-"/Users/richardbarker/Desktop/APEX_RSML_corners"
path<-"/Users/richardbarker/Desktop/APEX_RSML_corners_fixed_2_7_18"
path<-"/Users/richardbarker/Desktop/Cotton_RSML_Soil"
path<-"/Users/richardbarker/Desktop/Cotton_RSML_Soil_Petri_for_R"

table <- rsmlToTable(inputrsml=path, rsml.connect=TRUE)
archi <- architect(inputrsml=table, fitter=FALSE)

##archi <- rsmlToTable(path, fitter=T, rsml.connect = T, rsml.date="age")
location <- unlist(lapply(strsplit(as.character(archi$FileName), "_"), `[[`, 1))[]
treatment <- unlist(lapply(strsplit(as.character(archi$FileName), "_"), `[[`, 2))[]
genotypes <- unlist(lapply(strsplit(as.character(archi$FileName), "_"), `[[`, 3))[]
archi$genotypes <- genotypes
archi$location <- location
archi$treatment <- treatment

### archi$age <- as.numeric(archi$age)
### If you had time series data you could try this filter
### Example <- filter(architect, age == 7)

########################################
##Box Plots of Total Root Length??
library(tidyverse)
##ggplot(data = archi, aes(age, TRL, fill="age")) +  
#                    geom_boxplot() + 
#                   xlab("age") +
#                  ylab("Total root system length") + 
#                 theme_classic()

# These worked! :)

### ralph enhanced....
ggplot(data = archi, 
       aes(x = genotypes, y = TRL, fill = treatment)) +  
  geom_boxplot(coef = 10) + 
  xlab("genotypes") +
  ylab("Total root system length") + 
  scale_fill_manual(name = 'Treatment',
                    values = c('FL' = 'blue', 'GC' = 'yellow')) +
  theme_bw() +
  ## change looks
  theme(text = element_text(size = 16), 
        ## Change text on x axis so that it is at a 45 degree angle 
        axis.text.x = element_text(angle = 45, hjust = 1))


### Richard Enhanced....
ggplot(data = archi, 
       aes(x = genotypes, y = TRL, fill = treatment)) +  
  geom_boxplot(coef = 10) + 
  xlab("genotypes") +
  ylab("Total root system length") +
  theme_bw() +
  ## change looks
  theme(text = element_text(size = 16), 
        ## Change text on x axis so that it is at a 45 degree angle 
        axis.text.x = element_text(angle = 45, hjust = 1))



ggplot(data = archi, aes(treatment, TRL, fill="treatment")) +  
  geom_boxplot() + 
  xlab("treatment") +
  ylab("Total root system length") + 
  theme_classic()

ggplot(data = archi, aes(location, TRL, fill="location")) +  
  geom_boxplot() + 
  xlab("location") +
  ylab("Total root system length") + 
  theme_classic()
  

#ggplot(data = archi, aes(location, TRL, fill="location")) +  
#  geom_boxplot() + 
#  xlab("location") +
#  ylab("Total root system length") + 
#  theme_classic()
#  theme_classic() + theme(axis.text = element_text(12))



### archiDraw stage
######################################## Fail?
### RootMap

table$genotypes <- unlist(lapply(strsplit(as.character(table$file), "_"), `[[`, 1))[]
table$location <- unlist(lapply(strsplit(as.character(table$file), "_"), `[[`, 2))[]
table$location <- tolower(table$location)
table$treatment <- unlist(lapply(strsplit(as.character(table$file), "_"), `[[`, 3))[]

ggplot(table) + 
  geom_segment(aes(x = x1, y = -y1, xend = x2, yend = -y2, colour = location), size = 0.5, alpha = 0.5) + 
  coord_fixed() + 
  theme_bw() + 
  facet_wrap(~genotypes, ncol=3)

ggplot(table) + 
  geom_segment(aes(x = x1, y = -y1, xend = x2, yend = -y2, colour = treatment), size = 0.5, alpha = 0.5) + 
  coord_fixed() + 
  theme_bw() + 
  facet_wrap(~genotypes, ncol=3)

ggplot(table) + 
  geom_segment(aes(x = x1, y = -y1, xend = x2, yend = -y2, colour = location), size = 0.5, alpha = 0.5) + 
  coord_fixed() + 
  theme_bw() + 
  facet_wrap(~treatment, ncol=3)

### archiDraw stage
################################################# Fail?
# Compute the magnitude data to make the histgram (diameter not found?)
#histogram <- archi %>% 
#  mutate(value = round(Width)) %>%
#  ddply(.(genotypes, file, treatment, location, Width, Height), plyr::summarize, n=ceiling(sum(length/10))) %>%
#  ddply(.(genotypes, treatmenr, file, location, Width, Height), plyr::summarize, value = rep(rdepth,n)) %>%
#  filter(genotype %in% cax22) %>%
#  filter(as.numeric(treatment) <= 3)

#pl <- ggplot(histogram, aes(x=value, colour=genotype, group=file)) + 
#  geom_density() +
#  theme_classic() + 
#  theme(legend.position = "null") + 
#  facet_wrap(~genotype, ncol=4)

### archiDraw stage
######################################## Fail?
### Box plot of ?....
#archi_summary <- plyr::ddply(archi, .(file, genotypes, location, treatment), summarise, 
#                             n_root=length(x1),
                             depth = max(y1),
                             tot_length = sum(length),
                             max_magnitude = max(magnitude),
                             max_path_length = max(pathlength),
                             mean_magnitude = mean(magnitude),
                             mean_path_length = mean(pathlength))

#libpl <- ggplot(archi_summary, aes(genotype, n_root, fill=genotype)) + 
#  geom_boxplot() + 
  theme_classic() +
  theme(legend.position = "none",
        text=element_text(size=15),
        axis.text.x = element_text(angle = 45, hjust = 1))+
  ylab(n_root) + 
  xlab("Genotype")

## archiHomology
####################################################
## NMDS plot
perhomology <- perhomology(table)
distance <- as.data.frame(bottleneckdist(perhomology))  ### UNCOMMENT THIS LINE
mds <- metaMDS(as.dist(distance[,-(length(distance))]), trymax=200, autotransform=FALSE, wascores = FALSE, noshare=FALSE, expand=FALSE)
data2 <- as.data.frame(mds$points, genotype=genotypes) 
#data3 <- as.data.frame(mds$points, genotype=location) 
#data4 <- as.data.frame(mds$points, genotype=treatment) 
genotypes <- c(rep("cax22", 10),rep("cax23", 10),rep("Col-0", 10),rep("rbohD", 10))

#########################################
## Treatment = MDS2 plot for SVT vs EVT
ggplot(data2) +
  geom_point(aes(MDS1, MDS2, colour=treatment)) +
  stat_ellipse(aes(MDS1, MDS2, colour=treatment), level = 0.9, size=1) +
  theme_bw() +
  xlab("NMDS-1") +
  ylab("NMDS-2")

#########################################
##Fail#### Location = MDS2 plot for SVT vs EVT
ggplot(data4) +
  geom_point(aes(MDS1, MDS2, colour=location)) +
  stat_ellipse(aes(MDS1, MDS2, colour=location), level = 0.9, size=1) +
  theme_bw() +
  xlab("NMDS-1") +
  ylab("NMDS-2")

##Fail## Location = MDS2 plot for treatment
ggplot(data3) +
  geom_point(aes(MDS1, MDS2, colour=location)) +
  stat_ellipse(aes(MDS1, MDS2, colour=location), level = 0.9, size=1) +
  theme_bw() +
  xlab("NMDS-1") +
  ylab("NMDS-2")



#########################################
# FAIL ## Genotype = MDS2 plot for SVT vs EVT
ggplot(data2= reprex, aes(x, y)) +
  geom_point(aes(MDS1, MDS2, colour=genotypes)) +
  stat_ellipse(aes(MDS1, MDS2, colour=gentotypes), level = 0.9, size=1) +
  theme_bw() +
  xlab("NMDS-1") +
  ylab("NMDS-2")

## archiHomology
########################################
## archibarcodes
# Compile the data in a table
perhomology <- perhomology(archi, FUN="")
names  <- names(perhomology)
perh <- NULL
for(i in c(1:length(perhomology))){
  temp <- data.frame(perhomology[[i]])
  temp$y <- c(1:nrow(temp))
  temp$file <- names[i]
  perh <- rbind(perh, temp)
}
genotypes <- unlist(lapply(strsplit(as.character(perh$file), "-"), `[[`, 1))[]
rep <- unlist(lapply(strsplit(as.character(perh$file), "-"), `[[`, 3))[]
perh$genotype <- genotypes
perh$rep <- rep

ggplot(perh) + 
  geom_segment(aes(x = birth, y=y, xend=death, yend=y, alpha=0.1)) + 
  facet_wrap(~genotype) + 
  theme_classic() +
  theme(legend.position = "none")+
  ylab("H0") + 
  xlab(" distance (cm)")

########################################
### Where does the rs come from?
####PCA plot  # Do the PCA analysis
plants <- rs$architect$FileName
genotypes <- rs$architect$genotype
temp <- rs$architect[,c(Total root system length,Growth rate of the root system,First-order root length,First-order root growth rate,Total number of first-order roots,Total number of lateral roots,Total lateral root length,Mean length of lateral roots,Growth rate of lateral roots,Density of secondary roots,Topological magnitude,External path length)]
pca <- prcomp(temp, retx = T, scale=T)  # Make the PCA
pca.results <- cbind(plant=plants, genotype=genotypes, data.frame(pca$x)[,])

vars <- apply(pca$x, 2, var)  
props <- round((vars / sum(vars) * 100), 1)
xl <- paste0("Principal Component 1 (",props[1],"%)")
yl <-paste0("Principal Component 2 (",props[2],"%)
            ")

pl1 <- ggplot(data = pca.results) + 
  geom_point(aes(PC1, PC2, colour=genotype)) +
  stat_ellipse(aes(PC1, PC2, colour=genotype), level = 0.9, size=1) + 
  theme_bw() + 
  xlab(xl) + 
  ylab(yl)

z2 <- data.frame(var_names = rownames(pca$rotation), pca$rotation[, 1:2])
z2$var_names <- gsub("_", " ", z2$var_names)

pl2 <- ggplot(data=z2, aes(0, 0, xend=PC1, yend=PC2)) + 
  geom_segment(col="grey", size=1.2, arrow = arrow(length = unit(0.5,"cm")), alpha=0.9) +
  geom_text_repel(data=z2, aes(PC1, PC2, label=var_names), col="black", size=9) +
  geom_point(aes(x=0, y=0), colour="grey") +
  #scale_y_continuous(limits = c(-1, 0.3)) +
  theme_classic() +
  xlab(xl) + ylab(yl)

pl <- grid.arrange(pl1, pl2, ncol=1)



##Growth over time ## This data set contains only one time point
####Plot individuals by genotype
library(ggplot2)
ggplot(data = architect) +  
  xlab("Time [days]") + 
  ylab("Total root system length") + 
  ggtitle("Total root system length") + 
  theme_classic() +
  stat_smooth(aes(Time,Total root system length, colour = genotype))


####Plot average by genotype
library(ggplot2)
ggplot(data = architect) +  
  xlab("Time [days]") + 
  ylab("Total root system length") + 
  ggtitle("Total root system length") + 
  theme_classic() +
  geom_line(aes(Time,Total root system length, colour = genotype, group = FileName))


