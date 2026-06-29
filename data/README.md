# Data

This is the entry point to the datasets in the repository: a per-dataset
summary, formats, and provenance. For the **deep detail** — filename grammars,
the 18-treatment skew matrix, RSML internals, and trait-column definitions —
see **[`../docs/DATA_DICTIONARY.md`](../docs/DATA_DICTIONARY.md)**.

> **Note on location:** the datasets currently live in folders at the
> repository root (`18_way_skew/`, `APEX03/`, `ABRS_NASA_Roots_TimeLapse/`,
> etc.). The [reorganization plan](../REORGANIZATION_PLAN.md) proposes moving
> them under `data/`. This README documents them wherever they currently sit;
> update the paths here when the move happens.

---

## License

All data — images, time-lapse videos, RSML traces, and derived tables — is
released under **CC-BY-4.0**. See [`../LICENSE-DATA.md`](../LICENSE-DATA.md).
NASA-derived imagery (APEX-03, ABRS) carries the additional attribution notes
described there.

---

## Datasets at a glance

| Dataset (folder) | What it is | Files | Format | Calibrated? |
|------------------|------------|-------|--------|-------------|
| `18_way_skew/` | RootNav root traces, nutrient-skew assay | 53 | RSML (XML) | ❌ pixels |
| `APEX03/` | ISS APEX-03 seedling photos, flight vs ground | 12 + 12 | JPG + ACR pairs | ⚠️ see note |
| `ABRS_NASA_Roots_TimeLapse/` | ABRS root time-lapse, flight vs ground | ~88 + 4 | JPG frames + AVI | ⚠️ grid in-frame |
| `Azola/` | Aquatic fern *Azolla* | 5 | JPG | ❌ |
| `Lemna/` | Duckweed *Lemna* | 5 | JPG | ❌ |
| `Wolfinia/` | Watermeal (*Wolffia*?) | 5 | JPG | ❌ |
| `Londultia/` | Duckweed (*Landoltia*?) | 5 | JPG | ❌ |
| `data/images/leaves/` | **OSD-121** Arabidopsis seedling-dish photos (flight/ground) | 26 | JPG | ruler (px→mm) |
| `data/images/crops/` | **OSD-670** lettuce/radish/pepper leaves on graph paper | 16 | JPG | cm grid |

---

## 1. `18_way_skew/` — RSML root traces

53 RSML traces of Arabidopsis roots grown on 18 media treatments (agar/phytogel
× concentration × sucrose), used to study **root skewing**. This is the
structured, interoperable core of the repository.

- **Format:** RSML (open XML standard, https://rootsystemml.github.io/).
- **Traced with:** RootNav v1 (2017, `gilroylab`); geometry only (polyline +
  spline), ~10 plants per file.
- **Filename grammar, treatment matrix, replicate counts, and the
  pixel-calibration caveat:** see
  [`DATA_DICTIONARY.md` §1–2](../docs/DATA_DICTIONARY.md#1-18_way_skew--rsml-root-traces).
- **Purpose:** these assays were designed to help interpret the root behaviour
  seen in `ABRS_NASA_Roots_TimeLapse/` and `APEX03/` (see Tier 7 in the
  [project tracker](../PROJECT_TRACKER.md)).
- **Machine-readable:** `datapackage.json` (Frictionless) + `index.csv`
  (one row per file: gelling agent/%, sucrose %, replicate, plant/root counts,
  RSML metadata) make this dataset programmatically loadable.

## 2. `APEX03/` — ISS APEX-03 spaceflight seedlings

Photographs of 11-day Arabidopsis seedlings from the APEX-03 experiment, paired
flight vs ground control, used here as PlantCV analysis examples.

- **Filename scheme:** `<age> <FLT|GC> <genotype> <id> <image-id>.jpg`
  - `FLT` = flight (ISS, image IDs like `iss042e158911`) · `GC` = ground control
  - Genotypes: `Col-0` (wild type), `WS` (Wassilewskija), `Sku5`, `SKU6` (*sku*
    **skewing mutants** — on-theme for this repo)
  - `11D` = 11-day timepoint
- **Formats:**
  - `.jpg` — the open, usable image. **Use these.**
  - `.acr` — a **proprietary container** (file header is `ACR…JPG…`, i.e. an ACR
    wrapper around a JPG, evidently written by an analysis app). Not an open
    format; the matching `.jpg` is the canonical copy. *⚠️ Confirm the ACR
    tool/spec, or drop these in favour of the JPGs.*
  - `analysis_config (soapp).json` — a saved **PlantCV-style analysis recipe**
    (colorspace masking A/B with OTSU/BINARY thresholds, ROI grid) for one image
    (`11D FLT Col-0 304 …`), produced by a segmentation app ("soapp"). Useful as
    a worked example of the masking parameters.
- **Best root-analysis pilot target in the repo:** color, white roots on a
  dark/clear plate, high contrast, and a **printed grid** (enables px→mm
  calibration). The GC plates (organized downward roots) are the cleanest input
  for the RootNav2 pilot — see `notebooks/rootnav2/ABRS_APEX_RootNav2_pilot.ipynb`
  and Tier 7 in the [project tracker](../PROJECT_TRACKER.md).

## 3. `ABRS_NASA_Roots_TimeLapse/` — ABRS root time-lapse

Time-lapse imagery of Arabidopsis root growth from NASA's ABRS facility,
flight vs ground control. **This is the target dataset for the planned RootNav2
re-analysis** (project tracker, Tier 7).

| Subfolder | Contents |
|-----------|----------|
| `ABRS_Flight/` | 28 JPG frames + 2 AVI (4 & 8 fps) + a `Removed/` cull |
| `ABRS_Flight_11_days_11_photos/` | 11 curated daily JPG frames (flight) |
| `ABRS_Ground_11_days_11_photos/` | 11 curated daily JPG frames (ground) |
| `ABRS_Ground_control/` | 39 JPG frames + 2 AVI (4 & 8 fps) |
| `FL_GC_Combined/` | 8 JPG flight-vs-ground comparison composites |

- **Frames:** 1444×1448 px JPG, monochrome green (green-LED imaging),
  timestamped filenames `YYYY_MM_DD_HH_MM_SS-####.jpg` (Feb–Mar 2010).
- **Videos:** the `.avi`s are **derived** renders of the frame sequences →
  candidates to move to GitHub Releases or regenerate (see
  [reorg plan §3](../REORGANIZATION_PLAN.md)).
- **Analysis caveats:** dense (~20+ seedlings/plate), overlapping/crossing
  roots, an in-frame grid overlay, glare, and a label card — see the Tier 7
  feasibility notes before attempting automatic segmentation.

## 4. Aquatic plant image sets

Small example image sets of floating aquatic plants (`IMG_####_cropped.jpg`,
~5 each). Folder names contain typos to fix in the restructure:

| Folder | Likely species | Correct name |
|--------|----------------|--------------|
| `Azola/` | water fern | ***Azolla*** |
| `Lemna/` | common duckweed | *Lemna* (ok) |
| `Wolfinia/` | watermeal | ***Wolffia*** (verify) |
| `Londultia/` | duckweed | ***Landoltia*** (verify) |

> *⚠️ Confirm the intended species for `Wolfinia` and `Londultia` before
> renaming — these are best-guess corrections.*

---

## Known gaps (tracked)

- **Uncalibrated RSML** (`unit=pixel`) — prefer scale-free traits (angles,
  tortuosity) for cross-plate comparison. [DICT §2](../docs/DATA_DICTIONARY.md#2-rsml-file-internals)
- **Missing trait CSVs** — the R scripts read `weGAS.csv` / EVT inputs from
  `~/Desktop`; the in-repo `RootTrace/*.csv` are empty stubs. Stats are not
  reproducible until these are added here (project tracker, Q6).
- **Proprietary `.acr` format** — verify or replace with the paired JPGs.
- **Folder-name typos** — `Azola`, `Wolfinia`, `Londultia` (and elsewhere
  `Statisic`, `Oringal`) to fix during the restructure.

See **[`../PROJECT_TRACKER.md`](../PROJECT_TRACKER.md)** for status.
