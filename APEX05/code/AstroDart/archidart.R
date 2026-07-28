
path <- "/PATH/APEX_RSML"
path<-"/Users/richardbarker/Desktop/Desktop - Richard’s MacBook Air/APEX5_RSML_day4_/FL_&_GC"

archi <- rsmlToTable(path, fitter=F, show.progress = T)

length(unique(archi$plant))

# Correct the "plant" values, in case there is more than one plant per image
archi$plant[archi$order == 1] <- paste0(archi$plant[archi$order == 1], "_", archi$root[archi$order == 1])
archi$plant[archi$order == 2] <- paste0(archi$plant[archi$order == 2], "_", archi$parentroot[archi$order == 2])

length(unique(archi$plant))

architect <- architect(inputrsml = archi, fitter = F)

architect$genotype <- unlist(lapply(strsplit(as.character(architect$FileName), "_"), `[[`, 1))[]
architect$treatment <- unlist(lapply(strsplit(as.character(architect$FileName), "_"), `[[`, 2))[]
architect$time <- unlist(lapply(strsplit(as.character(architect$FileName), "_"), `[[`, 4))[]


architect %>%
  filter( time == "2") %>%
  ggplot(aes(treatment, TRL, fill=treatment)) + 
  geom_boxplot() +
  facet_grid(~genotype) + 
  theme_classic()



##### DRB enhanced
ggplot(data = architect, 
       aes(x = genotypes, y = TRL, fill = treatment)) +  
  geom_boxplot(coef = 10) + 
  xlab("genotypes") +
  ylab("Total root system length") +
  theme_bw() +
  ## change looks
  theme(text = element_text(size = 16), 
        ## Change text on x axis so that it is at a 45 degree angle 
        axis.text.x = element_text(angle = 45, hjust = 1))



