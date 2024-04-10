# CARA root modeling template

**Title:** "Modulation of Photomorphogenesis in Spaceflight Alters Root System Architecture in WT Col causing dwarfing effect that is not observed but not in Col-0-_phyD_ and WS Mutants: New Insights from Deep Learning using images from ABRS and CARA mission".

**Abstract:**&#x20;

Photomorphogenesis and auxin transport are important processes that regulate root growth in plants. We investigated the role of these processes in root growth in microgravity by growing Arabidopsis thaliana seedlings in spaceflight or ground control conditions under light or dark conditions. Root growth was measured at various time points. RNA sequencing was used to identify genes that were differentially expressed in the spaceflight and ground control conditions. Mathematical modeling was used to simulate the effects of auxin transport on root growth. Our results showed that root growth was significantly reduced in spaceflight compared to ground control conditions for WT Col-0, but this reduction in root growth was more pronounced in seedlings that were grown under light conditions. RNA sequencing identified a number of genes that were differentially expressed in the spaceflight vs ground control conditions in both light and dark grown samples. These genes included genes involved in auxin transport, sucrose/GA transport, photomorphogenesis, and cell signaling revealing that the addition of light enables more cellular and molecular adaptations to the effects of spaceflight. Mathematical modeling using PIN protein expression changes showed that the reduction in auxin accumulation in columella and lateral root caps of spaceflight samples explain the changes in root length and diameter. These results suggest that photomorphogenesis and auxin transport play important roles in root growth in microgravity. The reduction in auxin transport in spaceflight may be due to a number of factors, including changes in the cytoskeleton and cell wall structure. The results of this study have implications for the design of future plant-based life support systems for long-duration spaceflight.

**Keywords:** Arabidopsis, PIN transporters, auxin, spaceflight, root growth patterns, waving, skewing, circadian rhythm, Systems biology, mathematical modeling,



Paper figure options

{% embed url="https://docs.google.com/presentation/d/1Vr3eXuzvMWYQfodv9W8xeHwd7U6poq6ZMDsSzttPsys/edit?usp=sharing" %}

[Link to slide show for clear version](https://docs.google.com/presentation/d/1Vr3eXuzvMWYQfodv9W8xeHwd7U6poq6ZMDsSzttPsys/edit?usp=sharing).

## Introduction

* Photomorphogenesis is a process by which plants adjust their growth and development in response to light.
* One of the key players in photomorphogenesis is the phytochrome family of photoreceptors.
* Phytochromes are able to sense the presence or absence of light and regulate a variety of downstream genes, including genes involved in auxin transport.
* Auxin is a plant hormone that is involved in a wide range of developmental processes, including root growth.
* The goal of this study was to investigate the role of photomorphogenesis and auxin transport in root growth in microgravity.



**Introduction to plant tropisms:** Plants have evolved to grow and develop in the presence of gravity. However, when plants are grown in microgravity, their growth and development can be altered. This is because gravity plays an important role in a number of plant processes that include auxin transport including gravitropism, thigmotropism, chemotropism, oxytropism and hydrotropism.

**Introducing Auxin transport and the importance of gravity for polarity:** Auxin is a plant hormone that is involved in a wide range of developmental processes, including root growth, stem elongation, and leaf development. Auxin is transported from the shoot to the roots in a polar fashion, meaning that it is transported in a unidirectional manner. This polar transport is important for the development of a plant's root system.

**Gravitropism is the ability of plants to grow in response to a gravity vector:** Gravitropism is mediated by a number of factors, including auxin transport. When a plant is placed in a gravitational field, auxin is redistributed in the plant providing polarity in ion movement. This redistribution of auxin causes the plant to grow in a direction that is perpendicular to the gravitational field.

**Hydrotropism is the ability of plants to grow in response to water gradient:** Hydrotropism is mediated by a number of factors, including auxin transport. When a plant is placed in a water gradient, auxin is redistributed in the plant. This redistribution of auxin causes the plant to grow in the direction of the water gradient.

**Magnitude of tropisms are affected by microgravity:** Studies of effects of microgravity on a number of plant processes have provided evidence broadly links changes to auxin signaling and transport as being the primary mechanism for plants to adapt to spaceflight and the stresses related to spaceflight potentially indicating that they may be using part of their gravitropic response machinery to response to the stressors of spaceflight such as localized regions of hypoxia.

**Introducing system biology** In recent years, the application of systems biology and mathematical modeling to plant biology has grown rapidly. _Arabidopsis thaliana_ has emerged as a model system for these investigations due to its small genome and well-understood genetics. Many tools have been developed that allow researchers to use mathematical models to generate new and test old hypotheses.

* Read a [summary of the model here](https://www.ebi.ac.uk/biomodels/content/model-of-the-month?year=2013\&month=01) and down the [SimuPlant](https://www.simuplant.org/) modelling software
* Other modelling [tools and spaceflight astrobotany data are available on this website](https://astrobiology.botany.wisc.edu/gilroy-lab-home/astrobiology-course)

![](.gitbook/assets/0.jpeg)

![](.gitbook/assets/1.png)

**Figure X1: (A)** Cellular model showing the subcellular location of Auxin transport and signaling components. **(B)** Root tip model illustrating auxin levels predicted by the reverse foundation model of auxin movement in the root and lateral apexes. Here’s a link to a [video of the model in action](https://www.youtube.com/watch?v=emd6tUy1pBo\&ab\_channel=RichardBarker).

![](.gitbook/assets/3.png)

**Figure X2:** Illustration showing factors that are influence transcriptional regulation during plant adaption to space flight in the presence or absence of a light vector.&#x20;



**Supplimentary Table X1:** Summary of PIN proteins, their subcellular location and the tissues where they’ve been shown to transport auxin. Image of immuno-fluorescent antibodies localisation can be found at NCBI Nottingham [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7738516/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7738516/)

<table data-header-hidden><thead><tr><th width="151"></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>PIN protein</strong></td><td><strong>TAIR ID</strong></td><td><strong>Tissue</strong></td><td><strong>Subcellular location</strong></td><td><strong>Ref(s)</strong></td></tr><tr><td>PIN1</td><td>AT1G73590</td><td>Stelle, Vasculature, QC</td><td>Plasma membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN2</td><td>AT1G29760</td><td>Epidermis, cortex,</td><td>Plasma membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN3</td><td>AT1G29770</td><td>Columella</td><td>Plasma membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN4</td><td>AT1G73580</td><td>QC, Initial cells</td><td>Plasma membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN5</td><td>AT1G58860</td><td>x?x</td><td>Endoplasmic reticulum membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN6</td><td>AT1G29780</td><td>x?x</td><td>Endoplasmic reticulum membrane</td><td>Check &#x26; add ref</td></tr><tr><td>PIN7</td><td>AT1G29790</td><td>Columella</td><td>Plasma membrane</td><td>Check &#x26; add ref</td></tr></tbody></table>



### **Write & interacte Description of graphs below…**

Plants are a necessary component of any system of bioregenerative life-support for human space exploration. For this purpose, plants must be capable of surviving and adapting to gravity levels different from the Earth gravity, namely microgravity, as it exists on board of spacecrafts orbiting the Earth, and partial-_g,_ as it exists on the surface of the Moon or Mars. Gravity is a fundamental environmental factor for driving plant growth and development through gravitropism.&#x20;

Exposure to real or simulated microgravity produces a stress response in plants, which show cellular alterations and gene expression reprogramming. Partial-_g_ studies have been performed in the ISS using centrifuges and in ground based facilities, by implementing adaptations in them. Seedlings and cell cultures were used in these studies. The Mars gravity level is capable of stimulating the gravitropic response of the roots and preserving the auxin polar transport. Furthermore, whereas Moon gravity produces alterations comparable, or even stronger than microgravity, the intensity of the alterations found at Mars gravity was milder. An adaptive response has been found in these experiments, showing upregulation of WRKY transcription factors involved in acclimation. This knowledge must be improved by incorporating plants to the coming projects of Moon exploration.

The incorporation of a photoperiod regime was sufficient to attenuate or suppress the effects caused by gravitational stress at the cellular level in the root meristem. In all cases, values for variables recorded from samples receiving light stimuli in simulated microgravity were closer to values from the controls than values from samples grown in darkness. Differential sensitivities were obtained for the two nucleolin mutants.

**Table SX1: table summarizing tissue specific expression domains of PIN proteins on Earth.**&#x20;



The root is an important organ for obtaining nutrients and absorbing water and carbohydrates, and it depends on various endogenous and external environmental stimulations such as light, temperature, water, plant hormones, and metabolic constituents. Auxin, as an essential plant hormone, can mediate rooting under different light treatments. Therefore, this review focuses on summarizing the functions and mechanisms of light-regulated auxin signaling in root development. Some light-response components such as phytochromes (PHYs), cryptochromes (CRYs), phototropins (PHOTs), phytochrome-interacting factors (PIFs) and constitutive photo-morphorgenic 1 (COP1) regulate root development. Moreover, light mediates the primary root, lateral root, adventitious root, root hair, rhizoid, and seminal and crown root development via the auxin signaling transduction pathway. Additionally, the effect of light through the auxin signal on root negative phototropism, gravitropism, root greening and the root branching of plants is also illustrated. The review also summarizes diverse light target genes in response to auxin signaling during rooting. We conclude that the mechanism of light-mediated root development via auxin signaling is complex, and it mainly concerns in the differences in plant species, such as barley (Hordeum vulgare L.) and wheat (Triticum aestivum L.), changes of transcript levels and endogenous IAA content. Hence, the effect of light-involved auxin signaling on root growth and development is definitely a hot issue to explore in the horticultural studies now and in the future.



Plants cannot grow or develop properly without the support of their roots. Gravity plays an essential role in the formation of the root structure, but it is not clear how roots respond to gravity signals or how downward growth occurs. The two best-known models for root gravity sensing affirm the importance of starch. After the hyper-sensitive root crown perceives a gravity signal, starch granules within the rootlet cells settle to the endoplasmic reticulum in the direction of the signal, where they bind to specific receptors or open ion channels and release downstream signaling molecules. This triggers a series of signal transduction mechanisms, and this process involves signaling molecules such as indole-3‐acetic acid (IAA), reactive oxygen species, and calcium signaling, which ultimately induce groundward root growth. This review summarizes the mechanism of action underlying, and a research overview of, how plant roots sense and respond to gravity. The role of key signals such as starch, IAA, and calcium ions in root gravitropism is analyzed by integrating available information. The results provide a more complete theoretical basis for how roots grow toward gravity, which will contribute to our understanding of gravitropism and lay the foundation for discovering new directions of scientific research. Graphical abstract The graphics developed in this article are done by Microsoft Office PowerPoint 2010, Adobe Illustrator 2018 and ChemDraw 20.0.



In this study, we investigate the role of the PIN auxin transporter during spaceflight and translate environmental signals, such as light or dark, into changes in growth patterns. Additionally, we use mathematical modeling to study the effects of this transporter on Arabidopsis growth patterns during the CARA mission.



**Describe of the effect of dark on pin protein expression**

**Describe of the effect of DARK / skotomorphogenesis on PIN protein expression in microgravity**



### **Methods:**

* Arabidopsis thaliana seedlings were grown in spaceflight or ground control conditions under light or dark conditions.
* Root growth was measured at various time points.
* RNA sequencing was used to identify genes that were differentially expressed in the spaceflight and ground control conditions.
* Mathematical modeling was used to simulate the effects of auxin transport on root growth.

RNASeq data from CARA processed by NASA **GeneLab provide many interactive data visualization options** [https://visualization.genelab.nasa.gov/data/GLDS-120](https://visualization.genelab.nasa.gov/data/GLDS-120)



**Reanalysis of RNAseq:** The CARA (GLDS-120) experiments including RNAseq using the GeneLab data visualization system to observe gene expression provides new insights into hormonal changes caused by the addition of light that enable new and novel metabolic adaptations.

**Mathematical modeling of auxin transport**: to investigate the role of the PIN transporters in Arabidopsis auxin distribution patterns during spaceflight. The expression levels of the PIN proteins were used to provide conductivity values to the cell walls where they’ve been shown to be expressed (See Table X for PIN protein tissue specific pattern summary), using python jupyter notebook.

**Reanalysis of images from LSDA:** Images were downloaded from ALSDA, aligned in adobe bridge image raw, quantified with SmartRoot Fiji plugin, plotted with ArchiDart using Rstudio. MNDS and PCA dimensionality reduction was applied.



**Anoxia and hypoxia experiment:** Plants were grown on standard media as described by Choi et al., (XX), plates were then inserted into custom lids with valves attached that allow nitrogen gas to create an anoxic environment for 1, 2, or 3 hours. Plants were images during and after the anoxia treatment using a flatbed scanner recording images at 15min intervals. Nightingale plots were used to plot the direction of growth after hypoxia treatment.

###

## **Results:**

* Root growth was significantly reduced in spaceflight compared to ground control conditions.
* The reduction in root growth was more pronounced in seedlings that were grown under light conditions.
* RNA sequencing identified a number of genes that were differentially expressed in the spaceflight and ground control conditions.
* These genes included genes involved in auxin transport, photomorphogenesis, and cell signaling.
* Mathematical modeling showed that the reduction in root growth in spaceflight could be attributed to a decrease in auxin transport.







### 1. Image analysis

<figure><img src=".gitbook/assets/10.png" alt=""><figcaption></figcaption></figure>

![](.gitbook/assets/2.png)

Fig X: A) infographic of labeling method B) root length, C) root diameter/thickness

2\. Omics results



Fig X: A) DeSeq analysis B) Clustering

\-Summary of differential expression changes

\-Clustering of omics data with ICA into functional clusters



### 3. Auxin modeling

**(A)**

![](.gitbook/assets/4.png)

**(B)**

![](.gitbook/assets/5.png)



**Supplementary Figure XX: A.** Light  B. Dark. Foldhchange Data from CARA Flight vs Ground for the WT Col-0, Col-0 _phyD_ mutant and WS ecotype. Red shows a modelled increase in the auxin content of a particular tissue.&#x20;

Fig X: Auxin modeling output

4\. Regression modeling of omic clusters and root architecture

Fig X: Model outputs, clusters predictive of root length, and diameter



**Describe Auxin Transport modelling:** Our modeling experiment revealed that the PIN transporters are important for adaptation and development of Arabidopsis in spaceflight conditions and show that auxin distribution patterns may help explain physiological phenotypes observed during light. We found that the distribution of auxin in wild-type Arabidopsis (WS) resembles that of the Col-0 _phyD_ mutant during the CARA mission, as described by Paul et al. (2015). Our mathematical modeling revealed that this similarity in auxin distribution patterns may be responsible for the observed changes in growth patterns.



Description of the root system reanalysis.



To summarize the testing,

Length:

* There are significant difference in average root length between different treatment group (All 12) with p value = 3.35e-07
  * **Col-FLT-Light** was the most significant treatment having different root length with most of the other treatments
* There are significant difference in average root length between different genotype (All 3) with p value = 0.0284
  * The most significant difference was between WS and Col
  * PhyD and Col, PhyDand WS did not have significant differences in root length
* There are significant difference in average root length between different gravity treatments (All 2) with p value = 0.000609
* There are significant difference in average root length between different light treatments (All 2) with p value = 0.000594
* Is there significant difference in average length between different gravity treatments (2 gravity) within the same genotype?
  * Yes, all 3 genotypes had significant difference in root length, when having different gravity treatment with pvalue < 0.05
* Is there significant difference in average length between different light treatments (2 light) within the same genotype?
  * No, only **Col** had significant difference in root length, when having different light treatment with pvalue with < 0.05

Diameter:

* There are significant difference in average root diameter between different treatment group (All 12) with p value = 4.08e-09
  * **WS-FLT-Light/Dark and PhyD-FLT-Light/Dark** were the most significant treatment having different root diameter with most of the other treatments
* There are significant difference in average root diameter between different genotype (All 3) with p value = 0.000131
  * The most significant difference was between WS and PhyD
  * There was no significant difference between WS and Col
* There are significant difference in average root diameter between different gravity treatments (All 2) with p value = 0.0133
* There was **no** significant difference in average root diameter between different light treatments (All 2) with p value = 0.146
* Is there significant difference in average diameter between different gravity treatments (2 gravity) within the same genotype?
  * No, only **WS** had significant difference in root diameter, when having different gravity treatment with pvalue = 0.0115
* Is there significant difference in average diameter between different light treatments (2 light) within the same genotype?
  * No, only **PhyD** had significant difference in root diameter, when having different light treatment with pvalue = 0.016

Surface:

* There are significant difference in average root surface between different treatment group (All 12) with p value = 3.47e-07
  * **Col-FLT-Light** was the most significant treatment having different root surface with most of the other treatments
* There are **no** significant difference in average root surface between different genotype (All 3) with p value = 0.131
  * There were no significant difference between any genotype
* There are significant difference in average root surface between different gravity treatments (All 2) with p value = 4.36e-05
* There are **no** significant difference in average root surface between different light treatments (All 2) with p value = 0.228
* Is there significant difference in average surface between different gravity treatments (2 gravity) within the same genotype?
  * No, only **Col and WS** had significant difference in root surface, when having different gravity treatment with pvalue < 0.05
* Is there significant difference in average surface between different light treatments (2 light) within the same genotype?
  * No, only **Col** had significant difference in root surface, when having different light treatment with pvalue with < 0.05

Volume:

* There are significant difference in average root volume between different treatment group (All 12) with p value = 1.75e-07
  * **PhyD-FLT-Light** was the most significant treatment having different root volume with most of the other treatments
* There are significant difference in average root volume between different genotype (All 3) with p value = 0.00559
  * The most significant difference was between WS and PhyD
  * There was no significant difference between WS and Col
* There are significant difference in average root volume between different gravity treatments (All 2) with p value = 0.00497
* There are **no** significant difference in average root volume between different light treatments (All 2) with p value = 0.902
* Is there significant difference in average volume between different gravity treatments (2 gravity) within the same genotype?
  * No, only **Col and WS** had significant difference in root volume, when having different gravity treatment with pvalue < 0.05
* Is there significant difference in average volume between different light treatments (2 light) within the same genotype?
  * No, only **Col** had significant difference in root volume, when having different light treatment with pvalue with < 0.05



**Figure X: Light model**

**Figure X: Dark model**

**Describe Reanalysis images**



**Figure X: Increased variation in root tip angle and angle density”**

**Figure X: Enter description root length data and description of root diameter data**

**Figure X: Enter description of PCA and MDS Methods**

**Describe Analysis of new hypoxia response images**



**Figure X: Recovery rates reduction in O2 “Dark hypoxia skew**

**Figure X: Natural variation in recovery ates**



### **Discussion**

**Discussion**

* These results suggest that photomorphogenesis and auxin transport play important roles in root growth in microgravity.
* The reduction in auxin transport in spaceflight may be due to a number of factors, including changes in the cytoskeleton and cell wall structure.
* The results of this study have implications for the design of future plant-based life support systems for long-duration spaceflight.

**Prediction from image reanalysis: That Col-0-phyD should more closely resemble WS.**

**To summarize the stastical testing of the root systems,**

* **There are significant differences in average root length between different treatment group (All 12) with p value = 3.35e-07**
  * **Col-FLT-Light was the most significant treatment having different root length with most of the other treatments**
* **There are significant difference in average root length between different genotype (All 3) with p value = 0.0284**
  * **The most significant difference was between WS and Col**
* **There are significant difference in average root length between different gravity treatments (All 2) with p value = 0.000609**
* **There are significant difference in average root length between different light treatments (All 2) with p value = 0.000594**
* **Is there significant difference in average length between different gravity treatments (2 gravity) within the same genotype?**
  * **Yes, all 3 genotypes had pvalue < 0.05**
* **Is there significant difference in average length between different light treatments (2 light) within the same genotype?**
  * **No, only Col had significant pvalue with < 0.05**

**Prediction from IAA transport modeling: That auxin transport in Col-0-phyD should more closely resemble WS in darkness and to a lesser extend in light.**

The original paper states that there isn’t a reduction in root length in any of the genotypes when all treatments are considered. Interestingly if the light and dark treatments are separated then the Col-0 root are shorter in flight when grown in light and the _phyD_ roots have increased diameter in flight when grown in dark. These are 2 previously unseen phenotypes that may provide some clues about the potential influence of photomorphogenesis on plant architecture in microgravity. RNAseq shows upregulation of photosynthetic machinery, to increase the thylakoid number, may increase the efficiency of the dark reaction to process by products of anaerobic respiration and may even enable the roots to perform photosynthesis.

**Introduce Paper showing** confocal microscopy to observe DR5:GFP as a auxin signaling reporter during flight.

[https://bidd.group/spacelid/study.php?sid=SLID-284](https://bidd.group/spacelid/study.php?sid=SLID-284)

The effect of spaceflight on the gravity-sensing auxin gradient of roots: GFP reporter gene microscopy on orbit…“examined the spaceflight green fluorescent protein (GFP)-reporter gene expression in roots of transgenic lines of Arabidopsis thaliana: pDR5r::GFP, pTAA1::TAA1-GFP, pSCR::SCR-GFP to monitor auxin and pARR5::GFP to monitor cytokinin. Plants on the ISS were imaged live with the Light Microscopy Module (LMM), and compared with control plants imaged on the ground. Preserved spaceflight and ground control plants were examined post flight with confocal microscopy. Plants on orbit, growing in the absence of any physical reference to the terrestrial gravity vector, displayed typically "vertical" distribution of auxin in the primary root. This confirms that the establishment of the auxin-gradient system, the primary guide for gravity signaling in the root, is gravity-independent. The cytokinin distribution in the root tip differs between spaceflight and the ground controls, suggesting spaceflight-induced features of root growth may be cytokinin-related. The distribution of auxin in the gravity-sensing portion of the root is not dependent on gravity. Spaceflight appears benign to auxin and its role in the development of the primary root tip, whereas spaceflight may influence cytokinin-associated processes.”



**Awesome Cytokinin paper 2021** -> [https://www.mdpi.com/1422-0067/22/8/3874](https://www.mdpi.com/1422-0067/22/8/3874)

**Introduce Skewing data in ABRS & VEGGIE discussion**

Sucrose is used in the media

**Sucrose transport and anoxia.**

Loreti et al. (2005) + -> RNAseq reanalysis reveals import role for SWEET transporters.

**BRIC19/BRIC20: hypoxia in darkness leads to high light ROS response in WS and Col**

Other BRICs? -> Focus on RNAseq new BRIC study

Without light there is extensive adaption in relation to amino acid metabolism and transport.

**Introducing Col-**_**phyD**_** Where in the root could a **_**phyD**_** mutation effect root growth? (scell RNAseq and fluorescent cell sorting discussion)**

* **Columella and**
* **Lateral root cap**
* **Epidermis in before transition zones**



**Effect of low oxygen on auxin transport**

* **How might this affect auxin biosynthesis and cytokinin gradients?**
* **How would this change tip angle growth?**
* **How could these locations influence cell size and shape?**

**Taken together these data show the Col-0 **_**phyD**_** mutant root system architecture more closely resembles WS.**



**Description of graphs below…**

The ASLDS image archive supplied images that were initially aligned using Adobe Bridge Image Raw, followed by tracing with SmartRoot in ImageJ/FIJI. The tracing results were quantitatively analyzed and subsequently stored in the Root System Markup Language (RSML), facilitating the plotting process. As illustrated in Figures X, a discernible divergence in root orientation and associated root density alterations were evident on day 11. The Principal Component Analysis (PCA) and Multi-Dimensional Scaling (MNDS) plots indicate a noteworthy similarity between the phyD mutants and the WS ecotype, particularly when incorporating multiple phenotypes into the analytical model.



**Description of graphs below…**

Follow up investigation into ecotype variation in anoxia response. Root elongation rates show recovery rate is relative to the length of the anoxia experienced by the plant.



**(A)**

<figure><img src=".gitbook/assets/12.png" alt=""><figcaption></figcaption></figure>

**(B)**

![](.gitbook/assets/16.png)

**(C)**

![](.gitbook/assets/17.png)

**Supplementary FigureXX :** () Comparison of root elongation kinetics in Col-0 post 1 hour, 2 hours and 3 hours of anoxia treatment. n = 7-16. Comparison of GeneLAB varieties (Col-0, Ler-0, Cvi-0, WS-2) root elongation kinetics post 3 hours of anoxia treatment. WS-2 expressed the greatest root elongation, following with Col-0, Cvi-0, and Ler-0. n = 7-16.

**Supplementary Figure XX:** Summary of image analysis pipeline applied to the CARA image reanalysis. Overall correlation analysis summarized as a MDS and PCA plot. Raw data plotted as a skeleton with the orientation determined by the orientation magnitude. Root orientation plotted as density nightingale plots.

**Supplementary Figure XX:** Box and whisker plots showing root skewing direction: Center lines show the medians; box limits indicate the 25th and 75th percentiles; whiskers extend to minimum and maximum values. Nightingale plots showing root skew directs with a bin size of 10 degrees. n = 45.

####

#### Image Analysis Pipeline for CARA Image Reanalysis

The CARA image reanalysis pipeline uses a detailed and systematic method for analyzing complex image data. It employs Multidimensional Scaling (MDS), Principal Component Analysis (PCA), and sophisticated plotting techniques to thoroughly examine the dataset, revealing important insights and helping to understand the data's patterns and structures better.

A key focus of the analysis is on studying root orientation, represented innovatively with density nightingale plots. These plots provide clear visualizations of root orientations and reveal variations in density, giving insights into the spatial distribution and orientation strength within the images.

The pipeline begins with a correlation analysis, then processes the raw data into skeleton structures. This is essential for visualizing the basic framework of the imagery data. The orientation of the skeletons is carefully determined based on orientation magnitude, ensuring the data's structure is accurately portrayed.

In summary, the analysis pipeline for CARA image reanalysis uses advanced methods to deeply analyze the dataset, starting with correlation analysis and progressing through data processing and visualization. This approach is critical for extracting meaningful insights from the image data.



**Col-**_**phyD**_** and WS have similar auxin transport patterns and this is reflected in the similarity of their root system architecture.**

Follow up experiments (Figure X,X) show response to anoxia assays show low oxygen can effect root length and growth trajectory. There is ecotype variation in the plants response to low oxygen and it is interesting to note that WS exhibit large skews in response to changes in oxygen availability and this may potentially be the cause of the skewing root behavior observed during the ABRS mission (GLDS-7). In addition, these data also show that Ler has a left handed skew in response to low oxygen, a phenotypic response previously observed in the BRIC17 (Johnson et al., xx) and in the EMCS TROPI study (Vanderbrink et al., XX)

## **Conclusion**:

* This study has demonstrated the importance of photomorphogenesis and auxin transport in root growth in microgravity.
* A combination of environmental and genetic systems can be used to taylor plant architecture in microgravity.
* The results of this study have implications for the design of future plant-based life support systems for long-duration spaceflight.

The presence of light powers a circadian transport of Auxin in the root tip following the reverse fountain model (Swarup et al., 205), the photomorphogenesis enables a plethora of adaptive responses to spaceflight. The secondary biproducts of roots metabolism, microgravity induced root photosynthesis has the potential to change the root morphology making them growth either shorter or wider in diameter. The results of these studies have shown that microgravity can have a significant impact on plant growth and development. This is important information for scientists who are developing plant-based life support systems for long-duration spaceflight.

**Final model idea?…**. Does it need a protein-protein interaction model?-> could GPEC to pull some nodes from CARA?

How is the change in phytochrome dependent signaling during in plant experiencing spaceflight with light on their roots experiencing a reduction in growth, but if they have a Col-_phyD_ mutation then the root increases in diameter?

RNAseq shows -> something to do with sucrose transporters ;-)

[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330589/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330589/)

Figure below adapted from [Maciek Adamowski](https://pubmed.ncbi.nlm.nih.gov/?term=Adamowski%20M%5BAuthor%5D) and[ Jiří Friml](https://pubmed.ncbi.nlm.nih.gov/?term=Friml%20J%5BAuthor%5D)1 (2015)

_I wonder how this would look +/- gravity & +/- light?_











**Table X**: Studies related PIN proteins and auxin in space. Source the SpaceLID DB.

<table data-header-hidden><thead><tr><th width="237"></th><th></th><th width="270"></th><th></th></tr></thead><tbody><tr><td><strong>Study Titles</strong></td><td><strong>Studied Biophysical Phenomena</strong></td><td><strong>Studied Biological Phenomena</strong></td><td><strong>SpaceLid ID &#x26; weblink</strong></td></tr><tr><td>The effect of spaceflight on the gravity-sensing auxin gradient of roots: GFP reporter gene microscopy on orbit</td><td>●Study of fluorescent reporters for Auxin and cytokinin signaling</td><td><p>●Growth - Root ---> Microgravity response</p><p>●Reporter - Plant hormone ---> Auxin</p><p>●Reporter - Plant hormone ---> Cytokinin</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-284">SLID-284</a></td></tr><tr><td>A spaceflight experiment for the study of gravimorphogenesis and hydrotropism in cucumber seedlings</td><td>●Gravitational pull - Gravitropism</td><td><p>●Growth - Root ---> Hydrotropism</p><p>●Growth - Root ---> Gravitropism</p><p>●Component - Plant hormone ---> Auxin</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-196">SLID-196</a></td></tr><tr><td>Gravitropism interferes with hydrotropism via counteracting auxin dynamics in cucumber roots: clinorotation and spaceflight experiments</td><td>●Gravitational pull - Gravitropism</td><td><p>●Growth - Root ---> Hydrotropism</p><p>●Growth - Root ---> Gravitropism</p><p>●Component - Plant hormone ---> Auxin</p><p>●Component - Plant hormone ---> Auxin transport protein</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-197">SLID-197</a></td></tr><tr><td>The gravity-induced re-localization of auxin efflux carrier CsPIN1 in cucumber seedlings: spaceflight experiments for immunohistochemical microscopy</td><td>●Study of PIN location in microgravity</td><td><p>●Component - Plant hormone ---> Auxin</p><p>●Reporter - Plant hormone ---> Auxin transport protein</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-198">SLID-198</a></td></tr><tr><td>Gravity-regulated localization of PsPIN1 is important for polar auxin transport in etiolated pea seedlings: Relevance to the International Space Station experiment</td><td>●Gravitational pull - Gravitropism</td><td><p>●Component - Plant hormone ---> Auxin</p><p>●Reporter - Plant hormone ---> Auxin transport protein</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-172">SLID-172</a></td></tr><tr><td>STS-95 space experiment for plant growth and development, and auxin polar transport</td><td>●Gravitational pull - Gravitropism</td><td><p>●Growth - Seed germination ---> Epicotyls extensibility</p><p>●Growth - Seed germination ---> Coleoptiles extensibility</p><p>●Growth - Seed germination ---> Epicotyls direction</p><p>●Growth - Seed germination ---> Epicotyls angle</p><p>●Component - Plant hormone ---> Auxin</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-168">SLID-168</a></td></tr><tr><td>Polar auxin transport is essential to maintain growth and development of etiolated pea and maize seedlings grown under 1 g conditions: Relevance to the international space station experiment</td><td>●Gravitational pull - Gravitropism</td><td><p>●Growth - Seed germination ---> Coleoptile length</p><p>●Growth - Seed germination ---> Mesocotyls length</p><p>●Component - Plant hormone ---> Auxin</p></td><td><a href="https://bidd.group/spacelid/study.php?sid=SLID-169">SLID-169</a></td></tr></tbody></table>





_**Discuss the potential morphological effect of these changes tissue specific distributions of auxin…**_

&#x20;Box plots showing Root length, diameter, volume and surface of 13 day old seedlings. Col, WS and Col-_phyD_ on Earth and on the ISS

**Figure XX: Surface and volume…**

**Could simply this?**





### **References**

**Citation: Paul A-L, Sng NJ, Zupanska AK, Krishnamurthy A, Schultz ER, Ferl RJ (2017) Genetic dissection of the Arabidopsis spaceflight transcriptome: Are some responses dispensable for the physiological adaptation of plants to spaceflight? PLoS ONE 12(6): e0180186.** [**https://doi.org/10.1371/journal.pone.0180186**](https://doi.org/10.1371/journal.pone.0180186)

**DIETRICH D, PANG L, KOBAYASHI A, FOZARD JA, BOUDOLF V, BHOSALE R, ANTONI R, NGUYEN T, HIRATSUKA S, FUJII N, MIYAZAWA Y, BAE TW, WELLS DM, OWEN MR, BAND LR, DYSON RJ, JENSEN OE, KING JR, TRACY SR, STURROCK CJ, MOONEY SJ, ROBERTS JA, BHALERAO RP, DINNENY JR, RODRIGUEZ PL, NAGATANI A, HOSOKAWA Y, BASKIN TI, PRIDMORE TP, DE VEYLDER L, TAKAHASHI H and BENNETT MJ, 2017.**[ **Root hydrotropism is controlled via a cortex-specific growth mechanism.**](http://rdcu.be/rSsk) **Nature plants. 3, 17057**

**XUAN W, BAND LR, KUMPF RP, VAN DAMME D, PARIZOT B, DE ROP G, OPDENACKER D, MÖLLER BK, SKORZINSKI N, NJO MF, DE RYBEL B, AUDENAERT D, NOWACK MK, VANNESTE S and BEECKMAN T, 2016.**[ **Cyclic programmed cell death stimulates hormone signaling and root development in Arabidopsis.**](http://dx.doi.org/10.1126/science.aad2776) **Science (New York, N.Y.). 351(6271), 384-7**

**BAND, LEAH R., WELLS, DARREN M., FOZARD, JOHN A., GHETIU, TEODOR, FRENCH, ANDREW P., POUND, MICHAEL P., WILSON, MICHAEL H., YU, LEI, LI, WENDA, HIJAZI, HUSSEIN I., OH, JAESUNG, PEARCE, SIMON P., PEREZ-AMADOR, MIGUEL A., YUN, JEONGA, KRAMER, ERIC, ALONSO, JOSE M., GODIN, CHRISTOPHE, VERNOUX, TEVA, HODGMAN, T. CHARLIE, PRIDMORE, TONY P., SWARUP, RANJAN, KING, JOHN R. and BENNETT, MALCOLM J., 2014.**[ **Systems Analysis of Auxin Transport in the Arabidopsis Root Apex**](http://dx.doi.org/10.1105/tpc.113.119495) **PLANT CELL. 26(3), 862-875**

**DYSON, ROSEMARY J., VIZCAY-BARRENA, GEMA, BAND, LEAH R., FERNANDES, ANWESHA N., FRENCH, ANDREW P., FOZARD, JOHN A., HODGMAN, T. CHARLIE, KENOBI, KIM, PRIDMORE, TONY P., STOUT, MICHAEL, WELLS, DARREN M., WILSON, MICHAEL H., BENNETT, MALCOLM J. and JENSEN, OLIVER E., 2014.**[ **Mechanical modelling quantifies the functional importance of outer tissue layers during root elongation and bending**](http://dx.doi.org/10.1111/nph.12764) **NEW PHYTOLOGIST. 202(4), 1212-1222**

**J LAVENUS, LR BAND, AM MIDDLETON, M WILSON, M LUCAS, L LAPLAZE and MJ BENNETT, 2013.**[ **Toward a Virtual Root: Interaction of Genomics and Modeling to Develop Predictive Biology Approaches**](http://onlinelibrary.wiley.com/book/10.1002/9781118447093)**. **_**In:**_** M CRESPI, ed., Root Genomics and Soil Interactions John Wiley & Sons, Inc.. 79-92**

**PERET, BENJAMIN, MIDDLETON, ALISTAIR M., FRENCH, ANDREW P., LARRIEU, ANTOINE, BISHOPP, ANTHONY, NJO, MARIA, WELLS, DARREN M., PORCO, SILVANA, MELLOR, NATHAN, BAND, LEAH R., CASIMIRO, ILDA, KLEINE-VEHN, JUERGEN, VANNESTE, STEFFEN, SAIRANEN, ILKKA, MALLET, ROMAIN, SANDBERG, GORAN, LJUNG, KARIN, BEECKMAN, TOM, BENKOVA, EVA, FRIML, JIRI, KRAMER, ERIC, KING, JOHN R., DE SMET, IVE, PRIDMORE, TONY, OWEN, MARKUS and BENNETT, MALCOLM J., 2013.**[ **Sequential induction of auxin efflux and influx carriers regulates lateral root emergence**](http://dx.doi.org/10.1038/msb.2013.43) **MOLECULAR SYSTEMS BIOLOGY. 9,**

**BAND, LEAH R. and BENNETT, MALCOLM J., 2013.**[ **Mapping the site of action of the Green Revolution hormone gibberellin**](http://dx.doi.org/10.1073/pnas.1301609110) **PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES OF THE UNITED STATES OF AMERICA. 110(12), 4443-4444**

**BAND, L.R., UBEDA-TOMAS, S., DYSON, R.J., MIDDLETON, A.M., HODGMAN, T.C., OWEN, M.R., JENSEN, O.E., BENNETT, M.J and KING, J.R., 2012.**[ **Growth-induced hormone dilution can explain the dynamics of plant root cell elongation**](http://dx.doi.org/10.1073/pnas.1113632109) **Proceedings of the National Academy of Sciences of the United States of America: PNAS. 109(19), 7577-7582**

**BAND. L.R., WELLS, D.M., LARRIEU, A., SUN, J., MIDDLETON, A.M., FRENCH, A.P., BRUNOUD, G., SATO, E.M., WILSON, M.H., PÉRET, B., OLIVA, M., SWARUP, R., SAIRANEN, I., PARRY, G., LJUNG, K., BEECKMAN, T., GARIBALDI, J.M., ESTELLE, M., OWEN, M.R., VISSENBERG, K., HODGMAN, T.C., PRIDMORE, T.P., KING, J.R., VERNOUX, T. and BENNETT, M.J., 2012.**[ **Root gravitropism is regulated by a transient lateral auxin gradient controlled by a tipping-point mechanism**](http://www.pnas.org/content/109/12/4668) **Proceedings of the National Academy of Sciences of the United States of America. 109(12), 4668-4673**

**DYSON, R.J., BAND, L.R. and JENSEN, O.E., 2012.**[ **A model of crosslink kinetics in the expanding plant cell wall: yield stress and enzyme action**](http://www.sciencedirect.com/science/article/pii/S0022519312002251) **Journal of Theoretical Biology. 307, 125-136**

**PERET B, LI G, ZHAO J, BAND L, VOSS U, POSTAIRE O, LUU D, DA INES O, CASIMIRO I, LUCAS M, WELLS D, LAZZERINI L, NACRY P, KING J, JENSEN O, SCHAFFNER A, MAUREL C and BENNETT MJ, 2012.**[ **Auxin regulates Aquaporin function to facilitate lateral root emergence.**](http://dx.doi.org/10.1038/ncb2573) **Nature Cell Biology. 10, 991-8**

**BAND, L.R. and KING, J.R., 2012.**[ **Multiscale modelling of auxin transport in the plant-root elongation zone**](http://www.springerlink.com/content/x74n1467354q6075/) **Journal of Mathematical Biology. 65(4), 743-785**

**NELSON, M.R., BAND, L.R., DYSON, R.J., LESSINNES, T., WELLS, D.M., YANG, C., EVERITT, N.M., JENSEN, O.E. and WILSON, Z.A., 2012.**[ **A biomechanical model of anther opening reveals the roles of dehydration and secondary thickening**](http://onlinelibrary.wiley.com/doi/10.1111/j.1469-8137.2012.04329.x/abstract) **New Phytologist. 196(4), 1030-1037**

**LR BAND, JA FOZARD, C GODIN, OE JENSEN, T PRIDMORE, MJ BENNETT and JR KING, 2012.**[ **Multiscale Systems Analysis of Root Growth and Development: Modeling Beyond the Network and Cellular Scales**](http://www.plantcell.org/content/early/2012/10/29/tpc.112.101550) **The Plant Cell.**

**TWYCROSS, J., BAND, L.R., BENNETT, M.J., KING, J.R. and KRASNOGOR, N., 2010.**[ **Stochastic and deterministic multiscale models for systems biology: an auxin-transport case study**](http://www.biomedcentral.com/1752-0509/4/34) **BMC Systems Biology. 4, 34**





**Fold change source**

[https://osdr.nasa.gov/bio/repo/data/studies/OSD-37](https://osdr.nasa.gov/bio/repo/data/studies/OSD-37) -> 4 ecotypes for the natural variation to hypoxia in flight (dark BRIC)

Fold change = FL vs GC

[https://osdr.nasa.gov/bio/repo/data/studies/OSD-120](https://osdr.nasa.gov/bio/repo/data/studies/OSD-120) -> 3 genotypes for light vs DARK…

Fold change = FL vs GC



Metabolic flux viz’ / Pathway viewer options

[https://pathways.embl.de/](https://pathways.embl.de/)

[https://www.genome.jp/kegg/mapper/](https://www.genome.jp/kegg/mapper/)

Metabolite data -> Millar review supplementary data (light and dark)

[https://elicit.org/](https://elicit.org/)

