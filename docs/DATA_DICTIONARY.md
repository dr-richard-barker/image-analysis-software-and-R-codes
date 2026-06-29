# Data Dictionary

Documentation of the datasets in this repository: what each file means, how
filenames are structured, the provenance of the measurements, and the meaning
of derived columns. This is the **Interoperable + Reusable** backbone — it lets
someone who has never met the experiment reuse the data correctly.

Datasets covered:

1. [`18_way_skew/` — RSML root traces](#1-18_way_skew--rsml-root-traces)
2. [RSML file internals](#2-rsml-file-internals)
3. [Derived measurement columns (CSV)](#3-derived-measurement-columns-csv)
4. [Image datasets](#4-image-datasets)

---

## 1. `18_way_skew/` — RSML root traces

Root System Markup Language (RSML) traces of Arabidopsis seedlings grown on
media of varying gelling agent and sucrose concentration, used to study how
media composition affects **root skewing** (the chiral deviation of roots
growing along a near-vertical surface).

### Filename grammar

```
Gradient_<GEL%><GEL>_<SUC%>S_<REP>.rsml
         └──┬──┘ └┬┘  └─┬─┘    └┬┘
            │     │     │       └── replicate number (1–4)
            │     │     └────────── sucrose concentration (% w/v)
            │     └──────────────── gelling agent: A = Agar, P = Phytogel
            └────────────────────── gelling-agent concentration (% w/v)
```

**Worked example —** `Gradient_0.5%A_0.3%S_2.rsml`:
> Gradient plate, **0.5 % agar**, **0.3 % sucrose**, **replicate 2**.

### Treatment factors

| Token | Meaning | Levels |
|-------|---------|--------|
| Gelling agent | Substance solidifying the medium | **A** = Agar · **P** = Phytogel (a gellan-gum gelling agent) |
| Gelling % | Concentration of the gelling agent (% w/v) | 0.5, 1, 1.5 |
| Sucrose % (`S`) | Sucrose concentration in the medium (% w/v) | 0, 0.3, 1 |
| Replicate | Independent plate/seedling repeat | 1–4 |

The design is **2 gelling agents × 3 gelling concentrations × 3 sucrose levels
= 18 treatments** — this is the "18-way" skew experiment. Agar and Phytogel
differ in stiffness and surface properties, which (together with sucrose
osmotic effects) modulate the skew response.

### Treatment matrix & replicate completeness (53 files)

| Gelling agent | Gel % | Sucrose % | n | Replicates present |
|---------------|------:|----------:|--:|--------------------|
| Agar     | 0.5 | 0   | 3 | 1, 2, 3 |
| Agar     | 0.5 | 0.3 | 4 | 1, 2, 3, 4 |
| Agar     | 0.5 | 1   | 3 | 1, 2, 3 |
| Agar     | 1   | 0   | 3 | 1, 2, 3 |
| Agar     | 1   | 0.3 | 3 | 1, 2, 3 |
| Agar     | 1   | 1   | 3 | 1, 2, 3 |
| Agar     | 1.5 | 0   | 3 | 1, 2, 3 |
| Agar     | 1.5 | 0.3 | 2 | 1, 2 |
| Agar     | 1.5 | 1   | 3 | 1, 2, 3 |
| Phytogel | 0.5 | 0   | 3 | 1, 2, 3 |
| Phytogel | 0.5 | 0.3 | 4 | 1, 2, 3, 4 |
| Phytogel | 0.5 | 1   | 2 | 1, 2 |
| Phytogel | 1   | 0   | 3 | 1, 2, 3 |
| Phytogel | 1   | 0.3 | 3 | 1, 2, 3 |
| Phytogel | 1   | 1   | 3 | 1, 2, 3 |
| Phytogel | 1.5 | 0   | 3 | 1, 2, 3 |
| Phytogel | 1.5 | 0.3 | 2 | **2, 3** (rep 1 absent) |
| Phytogel | 1.5 | 1   | 3 | 1, 2, 3 |

> **Note on balance:** the design is *nearly* balanced at 3 replicates per
> treatment, with a few exceptions — two treatments have an extra rep 4, three
> have only 2 reps, and Phytogel/1.5/0.3 is missing rep 1 (files are numbered
> 2, 3). Account for this when running ANOVA / mixed models.

---

## 2. RSML file internals

RSML is an open XML standard for root system architecture
(spec: https://rootsystemml.github.io/; Lobet et al. 2015, *Plant & Cell
Physiology*). Each file here has the following structure.

### `<metadata>` block

| Field | Value in this dataset | Meaning |
|-------|-----------------------|---------|
| `version` | *(empty)* | RSML schema version (not populated by this RootNav export) |
| `unit` | `pixel` | Coordinate unit — see calibration caveat below |
| `resolution` | `1` | Pixels per `unit`; `1` means coordinates are raw pixels |
| `last-modified` | e.g. `2017-11-27T09:24:33` | Timestamp the trace was saved |
| `software` | `RootNav` | Tracing tool (Pound et al. 2013) |
| `user` | `gilroylab` | Tracer — the Gilroy Lab (UW–Madison astrobotany group) |
| `file-key` | e.g. `Gradient 0.5%A_0.3%S_2` | Human-readable trace key (matches filename) |

> ⚠️ **Calibration caveat (important for reuse):** `unit = pixel` and
> `resolution = 1` mean these traces are in **image pixels, not millimetres**.
> Absolute lengths/angles are only comparable across plates if the imaging
> setup (camera distance, dpi) was identical. To convert to physical units you
> need the pixels-per-mm scale for the imaging rig (e.g. from a ruler/sticker in
> the original photos). Skew *angle* and *tortuosity* are scale-independent and
> safe to compare directly.

### `<scene>` → `<plant>` → `<root>` → `<geometry>`

- Each file contains **~10 `<plant>`** elements (one seedling each), each with a
  single primary `<root>`. (Plant/root `ID` and `label` attributes are mostly
  blank in this export.)
- Geometry is stored two ways per root:
  - **`<polyline>`** — the raw traced points (`<point x= y= />`), the literal
    digitised path of the root.
  - **`<rootnavspline>`** — a smoothed spline fit (`controlpointseparation=40`,
    `tension=0.5`) RootNav uses for measurement.
- These files contain **geometry only** — no per-point diameter or functional
  annotations. Quantitative traits (length, angles, tortuosity, skew) are
  *derived* from the geometry, either by RootNav's measurement module
  (`RootNav.Measurement.dll`) or downstream in the R scripts.

---

## 3. Derived measurement columns (CSV)

Traits computed from root traces appear in the statistics inputs/outputs
(`Basics Statisic on RootNav/`, weGAS/EVT analyses, `RootTrace/measures.csv`).
Definitions:

| Column | Definition | Units |
|--------|------------|-------|
| `Emergence.Angle` | Angle of the root at its emergence from the seed/hypocotyl, relative to vertical/gravity vector | degrees |
| `Tip.Angle` | Angle of the root tip (growth direction) at the end of the trace | degrees |
| `Total.Length` | Path length of the root along its trace | pixels (or mm if calibrated) |
| `Total.Primary.Angle` | Overall angle of the primary root (start→end) vs vertical | degrees |
| `Tortuosity` | Path length ÷ straight-line (Euclidean) start→end distance; 1.0 = perfectly straight, higher = more wandering | dimensionless ratio |

> ⚠️ **Missing-data gap (flagged for fixing):** the trait CSVs needed to *use*
> the R scripts are **not in the repository**:
> - `RootTrace/measures.csv` and `RootTrace/debug.csv` are **empty stub files**
>   (0 bytes) left over from a RootTrace session — they contain no data.
> - `weGAS Analyses.R` reads `~/Desktop/weGAS.csv` and the EVT/SVT scripts read
>   similar local files that are **not included here**.
>
> So the column definitions above are reconstructed from the R script usage, not
> from a shipped data file. **Action (Tier 2/5):** locate the real `weGAS.csv` /
> EVT / SVT trait tables, add them under `data/`, confirm their headers against
> this table, and repoint the scripts to the in-repo relative paths. Until then
> the statistics are not reproducible from this repo alone.

> Note: `weGAS Analyses.R` splits rows 1–511 = Shoot, 512–1238 = Root — a
> hard-coded row split that should be replaced with an explicit grouping column
> when the data is re-added.

---

## 4. Image datasets

| Folder | Contents | Experiment / notes |
|--------|----------|--------------------|
| `APEX03/` | Arabidopsis seedling photos, `.jpg` + `.acr` (raw) | ISS **APEX-03** spaceflight. Filenames mark **FLT** (flight) vs **GC** (ground control), genotype (Col-0, WS, Sku5, Sku6), and ISS image IDs (`iss042e…`). 11-day (`11D`) timepoint. |
| `ABRS_NASA_Roots_TimeLapse/` | Time-lapse frames + rendered `.avi` | **ABRS** root growth, flight vs ground; 11-day / 11-photo sequences. Videos are derived from the frames. |
| `Azola/` | 5 images | Aquatic fern *Azolla* (folder name "Azola" is a typo). |
| `Lemna/` | 5 images (`IMG_*_cropped.jpg`) | Duckweed *Lemna*. |
| `Wolfinia/` | 5 images | Likely *Wolffia* (watermeal). |
| `Londultia/` | 5 images | Likely ***Landoltia*** (duckweed); folder name is a typo. |

**Genotype codes in APEX-03 filenames:** `Col-0` (wild-type Columbia),
`WS` (Wassilewskija), `Sku5` / `Sku6` (*sku* skewing mutants — directly relevant
to the skew theme of this repo).

> **TODO (Tier 2 stretch):** emit a machine-readable catalogue
> (`data/datapackage.json` Frictionless, or ISA-Tab for OSDR/GeneLab
> alignment) listing every image with species, experiment, flight/ground, date,
> genotype, and instrument.

---

## Provenance summary

```
Seedlings grown on 18 media treatments (agar/phytogel × conc × sucrose)
        │
        ▼   photographed (near-vertical plates)
   Plate images  ──────────────────────────────►  [APEX-03 / ABRS = separate spaceflight image sets]
        │
        ▼   traced in RootNav (2017, gilroylab), unit = pixel
   53 RSML files in 18_way_skew/   ◄── geometry: polyline + spline, ~10 plants each
        │
        ▼   measured (RootNav.Measurement.dll) → traits
   CSV trait tables (length, angles, tortuosity, skew)
        │
        ▼   analysed in R (Basics Statisic on RootNav/, weGAS/EVT)
   Statistics, plots, R-Shiny apps
```
