---
description: >-
  "Installing RootNav2 (and other image analysis software) in the cloud will
  make image analysis easier for students, researchers and educators" Dr Richard
  Barker.
---

# RootNav2 and AstroDart in CyVerse

### Dr Richard Barker - An astrobiology researcher has a computational challenge he can’t solve alone…

How to run RootNav2 (and other image analysis software) in the cloud?

What's the best way to make image easier for students, researchers and educators



**Historical Goal:** Installing RootNav2 in CyVerse discovery environment

Why: Free limitless storage space for teachers, students, and researchers provided by NSF. This cloud store is attached to supercomputers and provides access to limitless cloud compute time. Installing the latest images analysis software can create an easy to use analysis platform that is accessible all over the world increasing equity in education and research.&#x20;

The main challenge: Can you try adding the python-based image analysis software [RootNav2](https://github.com/robail-yasrab/RootNav-2.0) in the [Cyverse](https://cyverse.org/) Discovery Environment (DE)?&#x20;

![](.gitbook/assets/image.png)\


**Docker to build an environment**

The first step is to create a docker container.  This site has more information on the creation of dockers ([https://hub.docker.com/u/continuumio](https://hub.docker.com/u/continuumio)).

Apparently, CyVerse has a team who can help if you encounter any problems while adding this tool.

{% embed url="https://cyverse-de-tool-integration-quickstart.readthedocs-hosted.com/en/latest/index.html" %}

\


**Visualizing the data**

The data produced by RootNav2 is in RSML format. Dr Guileum Lobert from Germany has created the AstroDart R-shiny app to help make the data viz quicker and more insightful. We could then start using Astrodart in the Discovery Environment by launching their "RStudio Geospatial Latest" VICE app, which has all the Rstudio dependencies needed to run a R-shiny app.&#x20;

\
Here is more information about “DE VICE” apps in general, including tips and instructions to build your own customized app:&#x20;

{% embed url="https://learning.cyverse.org/projects/vice/en/latest/index.html" %}



So we could we convert it to run in R studio / **R shiny AstroDart application** to visualize the data

\## Shiny tools

install.packages("shiny")

\##Example data from the original paper

\##library(shiny)

\##shiny::runGitHub("plantmodelling/archishiny", "plantmodelling")

\##Version that allows user to add their own data.

library(shiny)

shiny::runGitHub("archidart/astrodart", "astrodart")

\
\


So apparently we just need to put the RootNav2 python code into a docker, then[ install the docker in CyVerse](https://cyverse-de-tool-integration-quickstart.readthedocs-hosted.com/en/latest/osg.html). But I really don't understand how to pull all this together with code...&#x20;

\
**RootNav viewer**



{% @github-files/github-code-block url="https://github.com/robail-yasrab/RootNav-Viewer-2.0" %}



More information on the alternative analysis and modelling tools can be foun in the Root System Markdown Language github repo. &#x20;

{% @github-files/github-code-block url="https://github.com/RootSystemML" %}
