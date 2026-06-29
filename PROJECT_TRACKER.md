# Project Tracker — FAIR Overhaul

A living checklist for making this repository **F**indable, **A**ccessible,
**I**nteroperable, and **R**eusable. This is the single place to see *what's
done, what's next, and what's still open*. Update the checkboxes as work lands.

- **The "how" (detailed design):** see [`REORGANIZATION_PLAN.md`](REORGANIZATION_PLAN.md)
- **The "what it is" (repo map):** see [`README.md`](README.md)
- **Last updated:** 2026-06-27
- **Licensing decision:** MIT (code) + CC-BY-4.0 (data) — locked in ✅

---

## Status at a glance

| Tier | Theme | Status |
|------|-------|--------|
| 1 | Legal + entry points (license, citation, README, deps) | ✅ Done |
| 2 | Data documentation (dictionary, provenance) | 🟡 In progress |
| 3 | Slim the repo (binaries out of git) | 🟡 In progress |
| 4 | Directory restructure (on a branch) | 🔲 Not started |
| 5 | Reproducibility (paths, Binder, pinned envs) | 🔲 Not started |
| 6 | Publish + DOI (Zenodo release) | 🔲 Not started |
| 7 | **New analysis** — RootNav2 on ABRS vs skew angles | 🟡 Scaffolded |
| 8 | **OSDR data integration** — pull deposited plant images | 🟡 Assessed |

Legend: ✅ done · 🟡 in progress · 🔲 not started · ⏸️ blocked

---

## FAIR scorecard

How each principle stands today, and what moves the needle. Update the "Now"
column as tasks complete.

| Principle | Now | Target | Key tasks |
|-----------|-----|--------|-----------|
| **Findable** | 🟡 | Repo + every dataset has a persistent ID and rich metadata | Zenodo DOI · `CITATION.cff` (done) · GitHub topics · per-dataset metadata |
| **Accessible** | 🟡 | Anyone can open code + data without Windows or paywalls | Binaries → upstream/Releases · Colab/Binder · open formats |
| **Interoperable** | 🟡 | Data uses open standards with documented semantics | RSML (already ✅) · DATA_DICTIONARY · datapackage.json / ISA-Tab |
| **Reusable** | 🟡 | Clear license + provenance + runnable environment | LICENSE (done) · relative paths · pinned envs · provenance links |

---

## Tier 1 — Legal + entry points ✅ DONE

- [x] `LICENSE` — MIT, with scope notes (code vs data vs third-party)
- [x] `LICENSE-DATA.md` — CC-BY-4.0 for images/videos/RSML/CSV
- [x] `CITATION.cff` — machine-readable citation
- [x] `requirements.txt` — Python deps pulled from notebooks/scripts
- [x] `README.md` — consolidated landing page (replaces 3 colliding READMEs)
- [x] `REORGANIZATION_PLAN.md` — detailed restructure design
- [x] `PROJECT_TRACKER.md` — this file

**Loose ends from Tier 1 (need your input):**
- [ ] Confirm copyright holder/year in `LICENSE` (currently "2025 Richard Barker and contributors")
- [ ] Add ORCID + co-authors to `CITATION.cff` (Ralph Møller Trane and others)
- [ ] Confirm skew treatment codes: `%A`, `%S`, `%P` meanings (blocks DATA_DICTIONARY)

---

## Tier 2 — Data documentation 🔲

> Highest reuse value, zero risk of breaking links. Do this next.

- [x] `docs/DATA_DICTIONARY.md`
  - [x] Decode `18_way_skew/` filename grammar (A=agar, P=phytogel, S=sucrose, +rep)
  - [x] Document the full 18-treatment matrix + replicate completeness (53 files)
  - [x] RSML provenance: source images, RootNav version, resolution, tracer (`gilroylab`)
  - [x] RSML internals + calibration caveat (unit=pixel, resolution=1)
  - [x] Define CSV columns + units — drafted from R-script usage. **Finding:** `RootTrace/measures.csv` & `debug.csv` are empty stubs; `weGAS.csv`/EVT inputs are NOT in the repo (read from `~/Desktop`). Stats are not reproducible until the real trait tables are added.
  - [x] Image dataset catalogue (APEX-03, ABRS, aquatic plants) + genotype codes
- [x] `data/README.md` — per-dataset catalogue (skew RSML, APEX-03, ABRS, aquatic), formats, license, known-gaps section
- [ ] **Recover missing trait CSVs** (weGAS / EVT / SVT) and add under `data/` — blocks reproducible stats (see Q6)
- [x] Machine-readable `18_way_skew/datapackage.json` (Frictionless) + generated `index.csv` (53 rows: parsed treatment factors + plant/root counts + RSML metadata). Validated: 53/53 RSML referenced, JSON parses.
- [ ] Stretch: extend datapackage approach to image datasets / ISA-Tab for OSDR alignment

---

## Tier 3 — Slim the repo 🔲

> **120 MB** of 456 MB is committed binaries (measured). Pick a handling per item.
> Local copy is a ZIP, not a git clone — the git steps below run on the GitHub repo.

- [x] Inventory binaries with sizes (120.4 MB total)
- [x] Add `software/README.md` documenting each tool + upstream + license + removal steps
- [x] Add `.gitignore` (blocks `*.exe/*.dll/*.msi/*.chm/*.lnk`, Germinator zip, `*.avi`)
- [x] Add `.gitattributes` (LFS template + binary/RSML handling)
- [ ] **On GitHub:** `git rm --cached` the binaries + commit (commands in `software/README.md`)
- [ ] **On GitHub:** attach binaries to a Release (`gh release create`) so they stay downloadable
- [ ] **On GitHub:** optional history purge (filter-repo/BFG) to actually reclaim the 120 MB
- [ ] Verify upstream download URLs in `software/README.md` (marked ⚠️ *verify*)
- [ ] Decide: regenerate ABRS `.avi`s from frames vs keep as Release assets

---

## Tier 4 — Directory restructure 🟡

> Do all at once on a branch. GitBook + Colab links will break if rushed.
> **Dry-run script written:** [`restructure.sh`](restructure.sh) — git-aware
> (`git mv` when `.git` present), syntax-checked, all source paths verified to
> exist. Run it on a branch of the real GitHub repo.

- [x] Author `restructure.sh` (creates tree, moves+renames, fixes typos, drops `Copy of`, rewrites Colab URLs, regenerates SUMMARY.md)
- [x] Validate: `bash -n` clean; all 38 move-sources confirmed present
- [x] **Sandbox-tested** on a 343-file skeleton mirror: found & fixed a folder-nesting bug (`Morphometric_R-codes`); re-test clean — 343/343 parity, all Colab URLs rewritten, no stray dirs
- [ ] **Run on a branch** of the GitHub repo (`git checkout -b restructure && bash restructure.sh`)
- [ ] After run: fix any intra-doc `.md` cross-links that 404 (script prints the grep)
- [ ] Verify GitBook build renders before merge
- [ ] Confirm aquatic species names before merge (Wolfinia→wolffia?, Londultia→landoltia? — Q8)

---

## Tier 5 — Reproducibility 🟡

- [x] Fix hard-coded paths in all R scripts → `here::here("data/tables/…")` or
      `Sys.getenv()` for external image dirs; originals preserved in comments.
      Files: weGAS Analyses.R, NASA SVT…R, EVT…Rmd, Brachypodium_root_tips,
      both Morphometric scripts. Verified no active absolute paths remain.
- [x] `.here` sentinel + `data/tables/README.md` (documents the expected CSVs = the Q6 contract)
- [x] `environment.yml` (conda mirror of requirements.txt)
- [x] `install.R` (R deps: here, MASS, car, Hmisc, xtable, dplyr, reshape2, Momocs, jpeg)
- [x] Binder badge in README + `runtime.txt` (python-3.10)
- [ ] **Ship the CSVs** the R scripts reference (blocked on Q6 — files not in repo)
- [ ] `renv.lock` for exact R version pinning (needs an R session: `renv::init()`)
- [ ] Pin exact package versions in requirements.txt/environment.yml (currently unpinned)

---

## Tier 6 — Publish + DOI 🟡

- [x] `.zenodo.json` (deposit metadata: creators, keywords, related identifiers, license note)
- [x] `RELEASING.md` (one-time Zenodo setup, pre-release checklist, tag/release commands, post-DOI steps)
- [x] `CONTRIBUTING.md` (licensing rules, no-binaries, portable paths, adding-a-dataset guide)
- [ ] **On GitHub:** enable GitHub ↔ Zenodo integration (RELEASING.md §setup)
- [ ] **On GitHub:** tag `v1.0.0` → archived snapshot + DOI
- [ ] After DOI: add to `CITATION.cff` (`doi:`) + DOI badge in `README.md`
- [ ] **On GitHub:** add topics: `astrobotany`, `rsml`, `plant-phenotyping`, `root-architecture`, `plantcv`, `spaceflight`
- [ ] Optional: issue/PR templates

---

## Tier 7 — New analysis: RootNav2 on ABRS vs. skew angles 🔲

> **Goal:** quantify root growth angles in `ABRS_NASA_Roots_TimeLapse/`
> (flight vs ground) and compare against the `18_way_skew/` nutrient-skew
> angle data. The skew assays were done to interpret these ABRS root images.

**Feasibility verdict (2026-06-27):** scientifically the right question, but the
ABRS images are a **hard target** — dense (~20+ seedlings/plate), overlapping
and crossing roots, monochrome green, gridded, with glare and a label card.
RootNav2's automatic seed→primary→lateral tracing will mis-assign where roots
cross. Expect poor automatic results, especially on flight plates.

**Caveats to respect:**
- **Method confound:** `18_way_skew` was traced with RootNav **v1**
  (semi-automatic). Measuring ABRS with RootNav **2.0** mixes tool differences
  into any angle comparison. Use the same method on both, or validate.
- **Calibration:** RSML is `unit=pixel`. Prefer **scale/method-robust traits**
  (emergence angle, tip angle, angular dispersion, tortuosity).

**APEX-03 finding (2026-06-28):** the `APEX03/` images are a **better pilot target than ABRS** —
full color, white roots on dark/clear plate, high contrast, and a **printed grid** (enables px→mm
calibration). GC plate shows organized downward roots; flight shows tangled microgravity waving. Still
multi-seedling/overlapping, but APEX-03 GC is the most tractable input in the repo.

**Plan:**
- [x] **Scaffold pilot notebook** → `notebooks/rootnav2/ABRS_APEX_RootNav2_pilot.ipynb` (16 cells):
      loads APEX-03 GC + ABRS GC frames; Path A = RootNav2→RSML scaffold; Path B = runnable CV
      angle-distribution fallback (robust to overlap); shared RSML→angle-trait reader; builds the
      18-way skew baseline. Verified: parses 500 roots, angles valid.
- [ ] Run Path A (RootNav2) on a GPU; spot-check traces by eye (decision gate)
- [ ] If automatic fails → RootNav **v1 semi-automatic** (matches skew method) or fine-tune
- [ ] Extract angle traits → compare flight vs ground vs the 18 skew treatments
- [ ] Document method + results; export new traces as RSML for consistency

---

## Tier 8 — OSDR / GeneLab data integration 🟡

> Assessed which deposited plant **images** in NASA OSDR map to this repo and
> which are worth adding. Full write-up: [`docs/OSDR_PLANT_IMAGE_DATASETS.md`](docs/OSDR_PLANT_IMAGE_DATASETS.md).

**Findings (biodata API, 2026-06-28):**
- **OSD-120** = APEX-03-2 root-skewing (Arabidopsis); has `image-analysis_photography_cara`
  assay → your `APEX03/` + `RACARA_root_physio.ipynb`. Confirm local set vs deposited.
- **OSD-121** = Arabidopsis morphometric photography; **24 flight/ground leaf JPGs** →
  your `Morphometric_R-codes/` workflow, but the *images* are a gap in this repo.
- **OSD-670** = lettuce/radish/pepper on asteroid regolith; whole-plant/leaf photos →
  new crop dataset, analysable with PlantCV + morphometric codes.

**Actions:**
- [x] **Built `scripts/python/osdr_download.py`** (OSDR file API client: list/filter/download, skips existing). Live-tested.
- [x] **Downloaded OSD-121** → `data/images/leaves/` (26 JPGs, 81 MB, flight/ground) + provenance README
- [x] **Calibrated** OSD-121 morphometrics: dish-crop + ruler px→mm → **key result: the "flight smaller" area effect was an imaging-scale artifact** (flight 10.56 vs ground 11.90 px/mm); calibrated area NOT significant (p=0.30); **angle dispersion robust** (p<0.0001). → `docs/OSD121_MORPHOMETRIC_FINDINGS.md`
- [x] **Piloted OSD-670** with PlantCV → `data/images/crops/` (16 imgs + manifest), `scripts/python/plantcv_crops_leafarea.py`, `docs/OSD670_PLANTCV_PILOT.md`. Leaf seg works; counts over-segmented; grid calib noisy.
- [x] **Validated calibration** — OSD-121 has NO deposited measurement table (only images + acquisition metadata; a FAIR gap this pipeline fills). Self-consistency check: calibrated dish diameter flight 66.7±0.2 / ground 63.9±2.3 mm (~standard 60–65 mm dish, ~4% apart) → calibration sound; magnification difference is real.
- [x] **Watershed instance-seg** added to `plantcv_crops_leafarea.py` — counts halved to a plausible range (Radish 59 > Pepper 36 > Lettuce 23 leaves/img).
- [ ] Robust 2-D grid-lattice fit for OSD-670 px→mm; `groups.csv`-driven formal R stats; trained model for exact leaf counts
- [ ] Confirm **OSD-120** CARA photography vs local `APEX03/`; record accession in `data/README.md`
- [ ] Resolve **ABRS/APEX-TAGES** OSD accession for `ABRS_NASA_Roots_TimeLapse/` (Gilroy GeneLab matrix)
- [ ] Record OSD accessions as provenance; link Zenodo DOI ↔ OSDR accession

### OSD-121 morphometric analysis (done)
- [x] `scripts/python/seedling_morphometrics.py` — ran on all 26 dishes. **Result
      (n=13/group, all p<0.001):** flight seedlings smaller (area, skeleton, extent)
      AND higher root-angle dispersion (51.6° vs 44.8°) = microgravity skewing signal.
      → `docs/OSD121_MORPHOMETRIC_FINDINGS.md`; emits `data/tables/groups.csv`.
- [x] In-repo copies kept + `MANIFEST.sha256.csv` (verifiable) + re-fetchable via downloader.
- [ ] Add dish crop + ruler px→mm calibration; validate vs OSD-121's own measurements.

### Sibling repo: `CARA_GeneLab_AWG` (tidy started)
Assessed → [`docs/CARA_REPO_ASSESSMENT.md`](docs/CARA_REPO_ASSESSMENT.md); clean-up staged in
[`cara_tidy/`](cara_tidy/) (tested syntax; can't run on Windows — see below).
- [x] **Verified by cloning:** repo is **un-checkout-able on Windows** (3 `|`-named files); only
      **15 of 32** `(1)/(2)` assets are true duplicates (rest are distinct `image (N).png`).
- [x] Built `cara_tidy/tidy_cara.sh` (hash-gated dedupe + pipe-file rename) + drop-ins
      (CITATION.cff, .gitignore, results/README.md, consolidated README).
- [ ] **Run `tidy_cara.sh` in a CARA clone on macOS** (you're on Mac), commit, apply drop-ins
- [ ] Decide CyJS site (remove vs Release); reconcile duplicated CARA physiology; add datapackage + DOI
- [ ] Cross-link both repos' READMEs; record OSD-120 in both

---

## Tier 11 — ABRS prediction test + cellpose plant segmentation 🟡

- [x] **ABRS angle dispersion** (`scripts/python/abrs_angle_analysis.py`) tests synthesis
  prediction #1 → flight > ground dispersion (59.1° vs 57.7°) & deviation (51.7° vs 48.7°)
  across 11 days, predicted direction. Single plate/condition = descriptive.
  → [`docs/ABRS_ANGLE_FINDINGS.md`](docs/ABRS_ANGLE_FINDINGS.md).
- [x] **Cellpose plant segmentation** (`scripts/python/cellpose_plant_segmentation.py`) — adapts
  the cell notebooks to segment whole plants in the Lemna/Londultia 12-well plates. Works:
  12 objects on Lemna (=12 wells), 15 on Londultia. Segments well/plant units; pure leaf area
  needs green-tissue refinement. → [`docs/CELLPOSE_PLANTS_FINDINGS.md`](docs/CELLPOSE_PLANTS_FINDINGS.md).
- **GPU note:** machine has a GTX 1050 Ti (4 GB) but Python 3.13 has no CUDA torch wheels →
  CPU-only torch installed; cellpose/RootNav2 run on CPU. (A py3.11 env would unlock the GPU.)

## Tier 10 — Cross-experiment synthesis ✅

[`docs/CROSS_EXPERIMENT_SYNTHESIS.md`](docs/CROSS_EXPERIMENT_SYNTHESIS.md): ties the
ground skew assay + spaceflight image sets into one model — root-angle organisation
(*organised/handed* ↔ *dispersed/wandering*) is shifted by either the gelling agent
(agar→handed; phytogel→wandering) or removing gravity (flight→dispersed). Angle
metrics are the calibration-free common currency. Includes 4 testable predictions
(ABRS quantified, sku mutants, medium×gravity interaction, CARA omics link). Linked
from README "Analyses & findings".

## Tier 9 — Analysis of the flagship 18-way skew dataset ✅

Ran a proper statistical analysis (`scripts/python/skew_analysis.py`, 483 roots)
→ [`docs/SKEW_ANALYSIS_FINDINGS.md`](docs/SKEW_ANALYSIS_FINDINGS.md):
- **Gelling agent drives skewing:** agar 7.21° vs phytogel 5.70° |tip angle| (p=0.0026).
- Sucrose % and gelling % have **no** significant effect (p=0.74, p=0.39).
- **Handedness:** agar imposes a consistent skew direction (+2.65°, p<0.0001); phytogel none (p=0.34).
- Sets the ground baseline for the spaceflight (ABRS/OSD-121) root behaviour.

## GitHub submission ✅

- [x] Pushed branch `fair-overhaul` (90 files, additive — master untouched) and opened
  **[PR #2](https://github.com/dr-richard-barker/image-analysis-software-and-R-codes/pull/2)**.
  Spurious line-ending diffs excluded; only the 7 intentionally-edited files + new files committed.
- [ ] Merge PR; then run `restructure.sh` on a branch (Tier 4) and the Zenodo release (Tier 6).

---

## Open questions / decisions needed

| # | Question | Blocks | Owner |
|---|----------|--------|-------|
| 1 | ~~What do `%A`, `%S`, `%P` mean in skew filenames?~~ **RESOLVED:** A=agar, P=phytogel, S=sucrose | ~~DATA_DICTIONARY~~ ✅ | Richard |
| 2 | Copyright holder + year for LICENSE? | finalizing LICENSE | Richard |
| 3 | Co-authors + ORCIDs for citation? | CITATION.cff | Richard |
| 4 | Binary strategy: upstream link vs Release vs LFS? | Tier 3 | Richard |
| 5 | Is this the canonical repo, or is GitHub the source of truth? (local copy is a downloaded zip, not a git clone) | all commits | Richard |
| 6 | Where are the real trait CSVs (`weGAS.csv`, EVT/SVT inputs)? The R scripts read them from `~/Desktop`; they're not in the repo and the RootTrace CSVs are empty stubs. | reproducible stats | Richard |
| 7 | What is the `.acr` format in `APEX03/` (ACR-wrapped JPG)? Keep + document, or drop for the paired JPGs? | data cleanup | Richard |
| 8 | Confirm species for `Wolfinia` (→ *Wolffia*?) and `Londultia` (→ *Landoltia*?) before renaming | restructure | Richard |

---

## Changelog

- **2026-06-28** — Validation + watershed: confirmed OSD-121 deposited no
  measurement table (FAIR gap; pipeline fills it). Self-consistency check —
  calibrated dish diameter ~same across groups (66.7 vs 63.9 mm) → calibration
  validated, magnification difference real. Added watershed instance-seg to the
  OSD-670 PlantCV pilot (counts → plausible range). Updated both findings docs.
- **2026-06-28** — Calibration + OSD-670 pilot: added dish-crop + ruler px→mm to
  `seedling_morphometrics.py` — **changed the OSD-121 conclusion** (flight "smaller"
  was a ~12% magnification artifact; calibrated area n.s.; angle dispersion is the
  robust signal). Built `plantcv_crops_leafarea.py`, downloaded OSD-670 (16 crop
  imgs), ran the PlantCV leaf-area pilot. Docs: `OSD670_PLANTCV_PILOT.md`; updated
  `OSD121_MORPHOMETRIC_FINDINGS.md`. Manifests for both image sets.
- **2026-06-28** — OSD-121 analysis + CARA tidy: ran `seedling_morphometrics.py`
  on 26 dishes → significant flight<ground size + flight>ground root-angle
  dispersion (microgravity skewing), `docs/OSD121_MORPHOMETRIC_FINDINGS.md`. Kept
  images in-repo with SHA-256 manifest. Cloned CARA repo → found it's
  un-checkout-able on Windows (pipe-char files) and only 15/32 "dups" are real;
  built tested `cara_tidy/` clean-up kit (script + drop-ins).
- **2026-06-28** — Tier 8 build: wrote `scripts/python/osdr_download.py` (OSDR
  file-API downloader), live-tested, and pulled OSD-121 (26 leaf JPGs, 81 MB)
  into `data/images/leaves/` with a provenance README. Assessed the sibling
  `CARA_GeneLab_AWG` repo → `docs/CARA_REPO_ASSESSMENT.md` (cross-link strategy,
  de-bloat, CITATION/DOI/datapackage, reconcile duplicated CARA physiology).
- **2026-06-28** — Tier 6 + Tier 8: added `.zenodo.json`, `RELEASING.md`,
  `CONTRIBUTING.md` (DOI/release prep — GitHub-side steps remain). Queried the
  OSDR biodata API for plant images → `docs/OSDR_PLANT_IMAGE_DATASETS.md`:
  OSD-120 (CARA root photos = your APEX-03), OSD-121 (24 morphometric leaf
  photos = a gap), OSD-670 (new crop-leaf set). ABRS/TAGES accession still TBC.
- **2026-06-28** — Tier 2 + Tier 7: added `18_way_skew/datapackage.json` +
  `index.csv` (Frictionless, machine-readable skew dataset; validated). Scaffolded
  `notebooks/rootnav2/ABRS_APEX_RootNav2_pilot.ipynb` (RootNav2 path + runnable CV
  fallback + skew baseline; 500 roots parse OK). Assessed APEX-03 images → better
  pilot target than ABRS (color, contrast, grid). Added `results/` to .gitignore.
- **2026-06-28** — Tier 4 sandbox test: ran `restructure.sh` on a 343-file
  skeleton mirror; caught & fixed a folder-nesting bug (`Morphometric_R-codes`),
  re-tested clean (343/343 parity, Colab URLs rewritten, no strays). Originals
  never touched.
- **2026-06-28** — Tier 5: converted all R-script hard-coded paths to
  `here::here()`/env-vars (originals kept in comments); added `.here`,
  `data/tables/README.md` (CSV contract for Q6), `environment.yml`, `install.R`,
  `runtime.txt`, and a Binder badge. Remaining: ship the missing CSVs, pin
  versions, optional `renv.lock`.
- **2026-06-28** — Tier 4 dry-run: wrote `restructure.sh` — a git-aware,
  self-contained migration that builds the docs/notebooks/scripts/data/software
  tree, moves & renames all files (typo fixes, `Copy of` drop, two loose R
  scripts given `.R`), rewrites the 5 Colab badge URLs, and regenerates
  `SUMMARY.md`. Syntax-checked and all 38 sources verified present. Ready to run
  on a branch of the real repo.
- **2026-06-27** — Tier 2: wrote `data/README.md` (per-dataset catalogue +
  formats + license + known-gaps). Identified `.acr` as an ACR-wrapped JPG
  container and the APEX-03 JSON as a PlantCV "soapp" analysis recipe. Logged
  open questions #7 (.acr format) and #8 (aquatic species names).
- **2026-06-27** — Tier 3 started: inventoried binaries (120.4 MB), wrote
  `software/README.md` (per-tool upstream + license + git-removal commands +
  Release/LFS guidance), added `.gitignore` and `.gitattributes`. Added Tier 7
  (RootNav2 ABRS re-analysis) with feasibility verdict and plan; logged open
  question #6 already covered missing CSVs.
- **2026-06-27** — Tier 2 started: `docs/DATA_DICTIONARY.md` written —
  decoded the 18-way skew design (agar/phytogel × conc × sucrose), full
  treatment matrix with replicate counts, RSML internals + pixel-calibration
  caveat, image-dataset catalogue, and provenance chain. Resolved open
  question #1. Remaining in Tier 2: verify CSV headers, add `data/README.md`.
- **2026-06-27** — Tier 1 complete: LICENSE, LICENSE-DATA, CITATION.cff,
  requirements.txt, consolidated README, REORGANIZATION_PLAN, this tracker.
  Licensing decided (MIT + CC-BY-4.0).
