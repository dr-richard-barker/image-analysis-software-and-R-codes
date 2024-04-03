---
description: 'Author: "DRB" date: "June 3, 2016"'
---

# RootNav Statisitics from EVT @ KSC summer 2016

###

### RootNav results: APEX5 EVT visualisation codes

###

This is an R Markdown document. Analysis of the primary root system of Col-0, cax2-2, cax2-3 and atrbohD grown at the KSC in the NASA VEGGIE as part of the Gilroy lab EVT in June 2016.

First install packages... \`\`\`{r} `echo = FALSE` install.packages("dplyr") install.packages("car") install.packages("ggplot2") install.packages("xtable")

````
Then activate them
```{r} 
library ('car')
library ('dplyr')
library ('ggplot2')
library(xtable)
````

The data is imported and then can be summarised as a table

```{r,
EVT_Root_measurements <- read.csv ("~/Downloads/Google Drive/R & Stats/APIX5 & thermal test/EVT_Root_measurements.csv")
knitr::kable(summary(EVT_Root_measurements))
knitr::kable(str(EVT_Root_measurements))
```

Histograms allow us to view the overall distrubution of the data

```{r}
hist(EVT_Root_measurements$Total.Primary.Angle) + theme_bw()
hist(EVT_Root_measurements$Total.Length) + theme_bw()
hist(EVT_Root_measurements$Convex.Hull) + theme_bw()
```

Scatter plot provides another rough overview of the data

```{r}
EVT_Root_measurements %>% ggplot (aes(x=Total.Primary.Angle, y=Total.Length)) + geom_point(aes(color=Genotype, shape=Genotype)) + theme_bw()
```

```{r}
EVT_Root_measurements %>% ggplot (aes(x=Convex.Hull, y=Total.Length)) + geom_point(aes(color=Genotype, shape=Genotype)) + theme_bw()
```

```{r}
EVT_Root_measurements %>% ggplot (aes(x=Convex.Hull, y=Total.Primary.Angle)) + geom_point(aes(color=Genotype, shape=Genotype)) + theme_bw()
```

Then we can perform anova statsical anlysis to see if there is a possitional effect on the direction of growth

```{r}
angle <- lm(EVT_Root_measurements$Total.Primary.Angle ~ EVT_Root_measurements$Possition + EVT_Root_measurements$Genotype)
anova(angle)
summary(angle)
```

Then we can perform anova statsical anlysis to see if there is a genotype effecton the direction of growth

```{r}
angle_geno <- lm(EVT_Root_measurements$Total.Primary.Angle ~ EVT_Root_measurements$Genotype)
anova(angle_geno)
summary(angle_geno)
```

Then we can perform anova statistical analysis to see if there is a positional effect on the length of growth

```{r}
length_posi <- aov(EVT_Root_measurements$Total.Length ~ EVT_Root_measurements$Possition + EVT_Root_measurements$Genotype)
anova(length_posi)
summary(length_posi)
```

Then we can perform statistical analysis to see if there is a genotype effect on the length of growth

```{r}
length_geno <- lm(EVT_Root_measurements$Total.Length ~ EVT_Root_measurements$Genotype)
anova(length_geno)
summary(length_geno)
```

Statistical analysis of Convex Hull data and its relationship to position

```{r}
curvature <- lm(EVT_Root_measurements $Convex.Hull ~ EVT_Root_measurements $Possition + EVT_Root_measurements $Genotype)
anova(curvature)
```

Statistical analysis of Convex Hull data and its relationship to genotype

```{r}
library(car)

qcurvature_geno <- lm(EVT_Root_measurements$Convex.Hull ~ EVT_Root_measurements$Genotype)
anova(curvature_geno)
summary(curvature_geno)
```

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.



## APEX5: SVT Data Analyses

Root <- read.csv("\~/Desktop/Root measurements\_KSC\_SVT\_processed.csv") str(Root)

## Checking distributions

hist(Root$Total.Primary.Angle) #Normal hist(Root$Total.Length) #Normal

## Anova

library(car)

### Skew angle vs Genotype

angle <- lm(Root$Total.Primary.Angle \~ Root$Position + Root$Genotype) anova(angle) #Anova(angle, type=c("III")) summary(angle)

### Skew angle

angle\_geno <- lm(Root$Total.Primary.Angle \~ Root$Genotype) anova(angle\_geno) summary(angle\_geno)

### Root Length vs Possition

length\_posi <- aov(Root$Total.Length \~ Root$Position + Root$Genotype) anova(length\_posi) summary(length\_posi)

### Root Length vs Genotype

length\_geno <- lm(Root$Total.Length \~ Root$Genotype) anova(length\_geno) summary(length\_geno)

#### Convex Hull vs position

curvature\_posi <- lm(Root$Convex.Hull \~ Root$Position + Root$Genotype) anova(curvature\_posi) #Anova(curvature, type=c("III")) summary(curvature\_posi)

**Convex Hull vs genotype**

curvature\_geno <- lm(Root$Convex.Hull \~ Root$Genotype) anova(curvature\_geno) #Anova(curvature, type=c("III")) summary(curvature\_geno)
