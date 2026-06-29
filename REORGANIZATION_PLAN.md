# Reorganization & FAIR Plan

A staged plan to make this repository **F**indable, **A**ccessible,
**I**nteroperable, and **R**eusable. Nothing here has been moved yet — this is
the proposed map and rationale so it can be reviewed before any files change.

> **Important:** This is a GitBook-published repo (`SUMMARY.md`, `.gitbook/`).
> Any file move must be paired with an update to `SUMMARY.md` and to the
> in-page links, or the published book will break. See "Migration mechanics".

---

## 1. Target directory structure

```
.
├── README.md                  # consolidated landing page (DONE)
├── LICENSE                    # MIT, code (DONE)
├── LICENSE-DATA.md            # CC-BY-4.0, data (DONE)
├── CITATION.cff               # citation metadata (DONE)
├── requirements.txt           # Python deps (DONE)
├── REORGANIZATION_PLAN.md     # this file (DONE)
├── SUMMARY.md                 # GitBook ToC — update paths after moves
├── .gitbook/                  # GitBook assets — leave in place
│
├── docs/                      # all narrative markdown (the GitBook chapters)
│   ├── DATA_DICTIONARY.md      # NEW — decode filenames, columns, RSML provenance
│   ├── introduction.md         # <- "README (1).md"
│   ├── plant-image-analysis.md # <- "README (1) (1).md"
│   ├── cara-reanalysis.md      # <- example-cara-root-modeling-example-reanalysis-paper.md
│   ├── astroroot-modelling-plan.md
│   ├── rootnav2-and-astrodart-in-cyverse.md
│   ├── rootnav-statisitics-from-evt-ksc-summer-2016.md   # fix typo -> statistics
│   ├── space-chile.md          # fix typo: space-chilie.md
│   ├── spectrum-sticker.md
│   ├── wegas-analysis-codes.md
│   ├── web-glyphics-app.md
│   ├── streamlit-automated-analysis.md
│   └── streamlit-planet-...md
│
├── notebooks/                 # all *.ipynb
│   ├── plantcv/   (SpaceChile, Plantcv_for_SPECTRUM, Spectrum_RFP)
│   ├── cellpose/  (run_cellpose_2.0, Cellpose_cell_segmentation_2D)
│   ├── growth/    (An_Attempt_To_Gauge_Growth_v2, Gauge_Growth_..._timelapse)
│   └── cara/      (RACARA_root_physio)
│
├── scripts/
│   ├── python/    (Plant_gauge_growth.py, an_attempt_to_gauge_growth_streamlit.py)
│   └── r/
│       ├── rootnav-stats/   (<- "Basics Statisic on RootNav/")
│       └── morphometrics/   (<- "Morphometric_R-codes/")
│
├── data/
│   ├── rsml/
│   │   └── 18_way_skew/        (53 RSML files)
│   ├── images/
│   │   ├── apex03/             (FLT/GC seedling jpg + acr)
│   │   ├── abrs_timelapse/     (ABRS_NASA_Roots_TimeLapse)
│   │   └── aquatic/
│   │       ├── azolla/  lemna/  wolffia/  landoltia/   # corrected names
│   └── README.md               # NEW — points to DATA_DICTIONARY.md
│
└── software/                  # OR remove from git entirely — see §3
    ├── RootNav/  RootTrace/  RootTraceV2-1/  Germinator/
    └── README.md               # NEW — what each tool is, upstream link, license
```

---

## 2. File-by-file moves (and renames)

### Rename to fix typos / collisions
| Current | New |
|---------|-----|
| `README (1).md` | `docs/introduction.md` |
| `README (1) (1).md` | `docs/plant-image-analysis.md` |
| `Basics Statisic on RootNav/` | `scripts/r/rootnav-stats/` |
| `Morphometric_R-codes/` | `scripts/r/morphometrics/` |
| `space-chilie.md` | `docs/space-chile.md` |
| `rootnav-statisitics-from-evt-ksc-summer-2016.md` | `docs/rootnav-statistics-evt-ksc-2016.md` |
| `Londultia/` | `data/images/aquatic/landoltia/` |
| `Azola/` | `data/images/aquatic/azolla/` |
| `an_attempt_to_gauge_growth(streamlist_test).py` | `scripts/python/gauge_growth_streamlit.py` |

> The three `README` variants currently collide in meaning. After the move,
> there is exactly **one** `README.md` (root) and the other two become normal
> `docs/` chapters.

### Notebooks with `"Copy of "` prefixes
`Copy of run_cellpose_2.0.ipynb` and
`Copy of Cellpose_cell_segmentation_2D_prediction_only.ipynb` → drop the
"Copy of " prefix when moving into `notebooks/cellpose/`.

---

## 3. Binaries: get them out of version control

~**160 MB of the 456 MB repo is committed binaries** (`.exe`, `.dll`, `.msi`,
the 79 MB `Germinator/GERMINATOR.zip`, `.avi` videos). Committing binaries
bloats every clone and is poor practice.

**Options (pick one per item):**
1. **Best — link upstream.** Replace `RootNav/`, `RootTrace/`, `RootTraceV2-1/`,
   `Germinator/` binaries with a `software/README.md` that links to the official
   download + the bundled paper PDF. Keeps the repo small and the tools findable.
2. **GitHub Releases / Zenodo.** Attach the binaries and the `.zip` as release
   assets; reference them from `software/README.md`.
3. **Git LFS.** If the binaries must live in-tree, track `*.exe *.dll *.msi
   *.zip *.avi` with Git LFS.

The large `.avi` time-lapse renders in `ABRS_NASA_Roots_TimeLapse/` are derived
products — consider keeping source frames and regenerating videos, or moving
the `.avi`s to release assets.

---

## 4. Data documentation (the biggest Interoperable/Reusable win)

Create **`docs/DATA_DICTIONARY.md`** covering:

- **`18_way_skew` filename grammar.** Decode e.g.
  `Gradient_0.5%A_0.3%S_2.rsml` → *medium gradient, 0.5% auxin (A) / 0.3%
  sucrose (S) (confirm), replicate 2*. Document every token, units, and the
  full treatment matrix (the "18 ways").
- **RSML provenance.** Which images these traces came from, RootNav version,
  pixel→mm resolution, who traced them (`user` field shows `gilroylab`).
- **CSV columns.** Define every column in `RootTrace/measures.csv`,
  `debug.csv`, and the weGAS/EVT inputs (Emergence.Angle, Tip.Angle,
  Total.Length, Tortuosity, etc.) with units.
- **Image metadata.** A catalogue table: file, species, experiment (APEX-03 /
  ABRS / SVT), flight vs ground, date, instrument, calibration sticker yes/no.

A machine-readable companion (`data/datapackage.json`, Frictionless Data
spec, or ISA-Tab for OSDR alignment) is the stretch goal — OSDR/GeneLab already
use ISA-Tab, so aligning with it would make this directly ingestible.

---

## 5. Reproducibility fixes

- **Hard-coded paths.** `weGAS Analyses.R` uses
  `read.csv("~/Desktop/weGAS.csv")`; `NASA SVT statistical analysis.R` and the
  `.Rmd` likely similar. Change to relative paths under `data/` and ship the
  referenced CSVs.
- **`environment.yml`** (conda) alongside `requirements.txt` for users who
  prefer conda; pin the OpenCV/PlantCV versions the notebooks expect.
- **Binder badge** + `runtime.txt` so notebooks launch with zero local setup.
- **`renv.lock`** for the R scripts to pin R package versions.

---

## 6. Findability / metadata

- **`CITATION.cff`** (DONE) — add ORCIDs and co-authors.
- **Zenodo DOI.** Enable the GitHub↔Zenodo integration, then cut a `v1.0.0`
  release → archived snapshot + citable DOI. Add the DOI badge to `README.md`
  and the `doi:` field to `CITATION.cff`.
- **`.zenodo.json`** (optional) for richer Zenodo metadata.
- **GitHub topics**: `astrobotany`, `rsml`, `plant-phenotyping`,
  `root-architecture`, `plantcv`, `spaceflight`.
- **`CONTRIBUTING.md`** + issue templates so the OSDR AWG can collaborate.

---

## 7. Migration mechanics (so nothing breaks)

1. Do the moves on a **branch**, not `master`.
2. For every moved `.md`, update its path in **`SUMMARY.md`** (GitBook ToC).
3. Grep for cross-references after moving:
   - relative links between markdown files,
   - the Colab badge URLs inside notebooks (they hard-code
     `.../master/<notebook>.ipynb` — update the path segment),
   - the README links added in this pass.
4. Verify the GitBook build still renders before merging.
5. Tag `v1.0.0` and let Zenodo archive it.

---

## 8. Suggested order of work

1. **Tier 1 (done):** `LICENSE`, `LICENSE-DATA.md`, `CITATION.cff`,
   `requirements.txt`, consolidated `README.md`, this plan.
2. **Data dictionary** (`docs/DATA_DICTIONARY.md`) — highest reuse value, no
   risk of breaking links.
3. **Binary handling** (§3) — biggest size win.
4. **Directory restructure** (§1–2) — do last, all at once, on a branch, with
   `SUMMARY.md` + Colab-URL updates.
5. **Zenodo DOI** on the first post-restructure release.
