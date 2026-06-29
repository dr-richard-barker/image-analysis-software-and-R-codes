---
description: >-
  Image-analysis software, notebooks, R codes, and example datasets from
  spaceflight-related astrobotany experiments — with an emphasis on measuring
  root system architecture and exporting it in the open RSML format.
---

# Image Analysis Software and R Codes (Astrobotany)

This repository collects the tools, code, example images, and root-trace data
used across a series of astrobotany plant- and root-phenotyping experiments. It
is published as a GitBook and as a GitHub repository.

> **OSDR AWG Action Plan** — this repo is being improved by the NASA OSDR
> Analysis Working Group. Planning documents:

[Action plan (Google Doc) — add your name and join the team.](https://docs.google.com/document/d/1Igb2upYtWcvEPFgW\_-EQ8bMrY2kq92ObxFaj4XzsN7s/edit?usp=sharing)

{% embed url="https://docs.google.com/document/d/1Igb2upYtWcvEPFgW_-EQ8bMrY2kq92ObxFaj4XzsN7s/edit?usp=sharing" %}

[Project management sheet for improving the image-analysis repo.](https://docs.google.com/spreadsheets/d/1-rBnjQiX5aX0cKsppO-nc1\_Tq4o4fmkodtSiFfGHCZg/edit?usp=sharing)

{% embed url="https://docs.google.com/spreadsheets/d/1-rBnjQiX5aX0cKsppO-nc1_Tq4o4fmkodtSiFfGHCZg/edit?usp=sharing" %}

---

## What's in here

The repository contains **four different kinds of thing**. Knowing which is
which is the fastest way to find what you need:

| Kind | Where | Notes |
|------|-------|-------|
| 🧮 **Software (tools)** | `RootNav/`, `RootTrace/`, `RootTraceV2-1/`, `Germinator/` | Third-party binaries, bundled for convenience. Keep their own licenses. |
| 📓 **Notebooks** | `*.ipynb` (root) | PlantCV, Cellpose, "gauge growth", SpaceChile, CARA, Spectrum. Colab-ready. |
| 📜 **Scripts** | `*.py`, `Morphometric_R-codes/`, `Basics Statisic on RootNav/` | Python + R analysis and statistics. |
| 🖼️ **Data** | `18_way_skew/` (RSML), `APEX03/`, `ABRS_NASA_Roots_TimeLapse/`, `Azola/`, `Lemna/`, `Wolfinia/`, `Londultia/` | Images, time-lapse videos, and RSML root traces. |

### Software (root & seed phenotyping tools)

- **RootNav** (`RootNav/`) — semi-automated root system architecture tracing;
  exports **RSML**. Includes an extra `.dll` enabling root-skew measurement.
  Ref: Pound et al. 2013, *Plant Physiology*.
- **RootTrace** (`RootTrace/`) — high-throughput root growth quantification.
  Ref: French et al. 2009, *Plant Physiology*.
- **RootTraceV2** (`RootTraceV2-1/`) — installer (`.msi`) + readme.
- **Germinator** (`Germinator/`) — seed-germination scoring and curve fitting.
  Ref: Joosen et al. 2010, *The Plant Journal*.

> ⚠️ These are **Windows** tools, not maintained by this repository and
> retaining their upstream licenses. To keep the repo lean they are **not
> committed to git** — download them from upstream or the GitHub Releases.
> See [`software/README.md`](software/README.md) for per-tool download links,
> licenses, and details.

### Notebooks (Python / Colab)

| Notebook | Purpose |
|----------|---------|
| `SpaceChile_phenotyping_v1.ipynb` | Plant detection / segmentation with **PlantCV** |
| `Plantcv_for_SPECTRUM_images.ipynb`, `Spectrum_RFP_Basic_Analysis.ipynb` | SPECTRUM imaging with the Astrobotany calibration sticker |
| `Copy of run_cellpose_2.0.ipynb`, `Copy of Cellpose_cell_segmentation_2D_prediction_only.ipynb` | **Cellpose** cell/root segmentation |
| `An_Attempt_To_Gauge_Growth_v2.ipynb`, `Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb` | Time-lapse seedling growth measurement |
| `RACARA_root_physio.ipynb` | CARA root physiology re-analysis |

### Scripts (R + Python)

- `Basics Statisic on RootNav/` — R statistics for RootNav/weGAS output
  (`NASA SVT statistical analysis.R`, `weGAS Analyses.R`, `EVT_R-MarkDown_report.Rmd`).
- `Morphometric_R-codes/` — leaf morphometrics (outline analysis).
- `Plant_gauge_growth.py`, `an_attempt_to_gauge_growth(streamlist_test).py` —
  Python / Streamlit growth-gauging prototypes.

### Data

- **`18_way_skew/`** — **53 RSML files**: root traces from an 18-treatment skew
  experiment. Filenames encode the treatment (auxin/sucrose/replicate); a data
  dictionary is on the roadmap.
- **`APEX03/`** — ISS APEX-03 spaceflight (`FLT`) vs ground-control (`GC`)
  Arabidopsis seedling images (`.jpg` + `.acr` raw).
- **`ABRS_NASA_Roots_TimeLapse/`** — flight vs ground root time-lapse imagery
  and rendered videos.
- **`Azola/`, `Lemna/`, `Wolfinia/`, `Londultia/`** — aquatic-plant image sets
  (note: *Londultia* is likely *Landoltia*; *Azola* → *Azolla*).

---

## RSML — the open root data format

The structured root measurements here are stored as **RSML** (Root System
Markup Language), an open community standard. Each file carries metadata
(`unit`, `resolution`, `software`, `last-modified`) plus per-root geometry as
polylines and splines. RSML is the interoperable backbone of this repo and is
readable by RootNav, archiDART (R), and `rsml` Python tooling.

Spec: https://rootsystemml.github.io/

---

## Getting started

### Run the notebooks (easiest: Colab or Binder)

Each notebook has an **"Open in Colab"** badge at the top. Open it and run the
cells — the dependency installs are inline.

Or launch the whole repo in **Binder** (zero local setup):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dr-richard-barker/image-analysis-software-and-R-codes/master)

### Run locally

```bash
pip install -r requirements.txt   # or: conda env create -f environment.yml
jupyter lab
```

For Cellpose, install the PyTorch build matching your hardware from
https://pytorch.org/get-started/locally/.

### R scripts

```bash
Rscript install.R   # installs MASS, car, Momocs, here, etc.
```

Scripts resolve their data paths from the repo root via `here::here("data/…")`,
so they run regardless of your working directory. The trait-table CSVs they read
go in [`data/tables/`](data/tables/) — see that folder's README. (Some required
CSVs are not yet committed; see the [project tracker](PROJECT_TRACKER.md).)

---

## Analyses & findings

Reproducible analyses of the datasets here (scripts in `scripts/python/`):

- **[Cross-experiment synthesis](docs/CROSS_EXPERIMENT_SYNTHESIS.md)** — how the
  ground skew assay and the spaceflight image sets tell one story (root-angle
  organisation), with a unifying model + testable predictions. **Start here.**
- **[18-way skew assay](docs/SKEW_ANALYSIS_FINDINGS.md)** — gelling agent (agar)
  drives root skewing & handedness; sucrose/concentration do not.
- **[OSD-121 morphometrics](docs/OSD121_MORPHOMETRIC_FINDINGS.md)** — flight roots
  more angularly dispersed; the apparent size difference was an imaging artifact.
- **[ABRS time-lapse](docs/ABRS_ANGLE_FINDINGS.md)** — flight roots more dispersed
  than ground over 11 days (tests synthesis prediction #1).
- **[OSD-670 PlantCV pilot](docs/OSD670_PLANTCV_PILOT.md)** — crop leaf-area.
- **[Cellpose plant segmentation](docs/CELLPOSE_PLANTS_FINDINGS.md)** — per-well
  plant counts in the Lemna/Londultia plates.
- **[OSDR plant-image catalogue](docs/OSDR_PLANT_IMAGE_DATASETS.md)** — what's in
  NASA OSDR and what to pull next.

## Related tools & web apps

- **AstroBotany Spectrum calibration sticker** — https://astrobotany.com/product/airi-bio-imaging-spectrum-5cm/
- **Space Photography Guide** — https://dr-richard-barker.github.io/Space_Photography_Guide.io/
- **Web-glyphics** (calibration-sticker analysis) — https://web-glyphics.streamlit.app/ · [code](https://github.com/lvbauer/web-glyphics)
- **RootNav stats (R-Shiny)** — https://rmtrane.shinyapps.io/RootNav/
- **RootTrace stats (R-Shiny)** — https://rmtrane.shinyapps.io/RootTrace/
- Streamlit prototypes: [Plant detection](https://viva-fidel-planet-main-n4sviq.streamlit.app/) · [Health classifier](https://drplantclassifier.streamlit.app/) · [Cross-section quantification](https://nathanpouliquen-projet-m1-automated-analysis-app-it8h6s.streamlit.app/)

---

## License & citation

- **Code** (notebooks, `.py`, `.R`) — MIT, see [`LICENSE`](LICENSE).
- **Data** (images, videos, RSML, CSV) — CC-BY-4.0, see [`LICENSE-DATA.md`](LICENSE-DATA.md).
- **Bundled third-party software** retains its own license (see `LICENSE`).

To cite this repository, see [`CITATION.cff`](CITATION.cff). A citable DOI will
be minted via Zenodo on the first tagged release.

---

## Roadmap

This repository is being made more **FAIR** (Findable, Accessible,
Interoperable, Reusable).

- **[`PROJECT_TRACKER.md`](PROJECT_TRACKER.md)** — live checklist of goals,
  progress, and open questions (start here).
- **[`REORGANIZATION_PLAN.md`](REORGANIZATION_PLAN.md)** — detailed directory
  restructure, binary handling, and data-documentation design.

## Contributors

Richard Barker and collaborators, including Ralph Møller Trane (statistics /
R-Shiny apps). Contributions welcome — please open an issue or pull request.
