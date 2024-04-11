# Space Chilie

{% @github-files/github-code-block url="https://github.com/dr-richard-barker/image-analysis-software-and-R-codes/blob/master/SpaceChile_phenotyping_v1.ipynb" %}

[https://github.com/dr-richard-barker/image-analysis-software-and-R-codes/blob/master/SpaceChile\_phenotyping\_v1.ipynb](SpaceChile\_phenotyping\_v1.ipynb)



pip install plantcv

## Set the notebook display method

## inline = embedded plots, notebook = interactive plots

%matplotlib inline

## Import libraries

from plantcv import plantcv as pcv import numpy as np import requests import shutil import re, os, json

## Download sample images

### CHOOSE STUDY:

## Use the study title for unique study titles or study hash for studies without unique titles

study\_title="The SpaceChileChallenge CoSE" study\_hash="651e968eccaf4f4699d15398b08a5e37\_5f22c4df22dd4"

## Space Chile Prototype Data Sharing Image downloader

## 1) Download API JSON

api\_link = "https://five.epicollect.net/api/export/entries/the-spacechilechallenge-cose?form\_ref=651e968eccaf4f4699d15398b08a5e37\_5f22c4df22dd4"

file\_name = api\_link.split("=")\[-1]+".json" if not os.path.isfile(file\_name): res = requests.get(api\_link) if res.status\_code == 200: open(file\_name, "wb").write(res.content) else: print('Image Couldn't be retrieved') else: pass

## 2) Parse JSON

with open(file\_name, "rb") as f: api\_json\_dict = json.load(f)

print("Studies in Collection:\n(Study Title : Study Hash)\n-----") for study in api\_json\_dict\["data"]\["entries"]: print(study\["title"] + " : " + study\["ec5\_uuid"])

print("-----")

## 3) Download images from study

## Download loop

for study in api\_json\_dict\["data"]\["entries"]: if (study\["title"] == study\_title) or (study\["ec5\_uuid"] == study\_hash): for key in study: if (isinstance(study\[key], str)) and ("https://" in study\[key]): img\_file\_name = study\[key].split("=")\[-1] if not os.path.isfile(img\_file\_name): r = requests.get(study\[key], stream=True) if r.status\_code == 200: with open(img\_file\_name, "wb") as f: shutil.copyfileobj(r.raw, f) print('Image sucessfully Downloaded: ',img\_file\_name) else: print('Image Couldn't be retrieved') else: print(f"Image {img\_file\_name} already retrieved.")

