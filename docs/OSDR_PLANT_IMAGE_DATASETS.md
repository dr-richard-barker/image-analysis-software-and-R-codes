# NASA OSDR plant-image datasets — gap analysis & download targets

An assessment of plant **image** datasets in the NASA Open Science Data
Repository (OSDR / GeneLab), how they map to the data already in this repo, and
which ones are worth downloading and analysing with the codes here.

Queried via the OSDR **biodata API** (`https://visualization.osdr.nasa.gov/biodata/api/`)
on 2026-06-28. Method: listed Arabidopsis accessions, then filtered assays for
`image-analysis` / `photography` / `microscopy` technology types.

> **Caveat:** the biodata API summarisation can under-report files for large
> datasets (e.g. OSD-120's listing is dominated by RNA-seq). Confirm exact image
> counts on each study's OSDR landing page before bulk download.

## How the API works (for re-running this)

```
# all Arabidopsis sample accessions
.../api/v2/query/metadata/?study.characteristics.organism=/Arabidopsis/&id.accession&format=csv
# every assay, to spot imaging/photography ones
.../api/v2/query/assays/?format=csv
# one dataset's assays / files
.../api/v2/dataset/OSD-121/assays/
.../api/v2/dataset/OSD-121/files/
```

Download files from a study's repo page: `https://osdr.nasa.gov/bio/repo/data/studies/OSD-121`.

---

## Datasets WITH plant photography / image-analysis assays

| OSD | Organism | Imaging assay | Images | Maps to your repo |
|-----|----------|---------------|--------|-------------------|
| **OSD-120** | *Arabidopsis* | `image-analysis_photography_cara` (+ RNA-seq) | CARA root photography (count TBC) | **APEX-03-2** root-skewing study → your `APEX03/` images + `RACARA_root_physio.ipynb` |
| **OSD-121** | *Arabidopsis* | `morphometric-analysis_image-analysis_photography` (+ microarray) | **24 JPG** flight/ground leaf-morphology photos (`LSDS-56_morphometric-photography_*`, `OSD-121_sup_*`) | **Your `Morphometric_R-codes/`** workflow — but the *images* are not in your repo |
| **OSD-670** | Lettuce, Radish, Pepper | `image-analysis_photography_camera` | Whole-plant + leaf photos on cm graph paper (ImageJ leaf area) | New crop-leaf set → analysable with PlantCV + your leaf morphometric / leaf-area codes |

### Verdict on "do I have all the deposited plant images?"
- **OSD-120 (APEX-03-2 / CARA):** this is your study. Cross-check the deposited
  CARA photography assay against your local `APEX03/` set — the OSDR copy is the
  citable archive and may include frames/genotypes you don't have locally.
- **OSD-121 (morphometric):** **likely a gap.** Your `Morphometric_R-codes/`
  folder ships the *scripts* but no images; OSDR has the 24 flight/ground leaf
  photos these scripts were written for. Good candidate to download into
  `data/images/leaves/` (which the R scripts now point at via `LEAF_IMAGE_DIR`).

---

## New plant-image datasets worth adding & analysing

1. **OSD-121 — Arabidopsis morphometric leaf photos (24 JPG, flight vs ground).**
   Drop into `data/images/leaves/`; run `scripts/r/morphometrics/` (Momocs
   outline analysis) directly. Closes the missing-image gap for that workflow.
2. **OSD-670 — crop leaves on asteroid-regolith simulant (lettuce/radish/pepper).**
   New species and a food-crop angle. Analyse leaf area/colour with PlantCV
   (`SpaceChile_phenotyping_v1.ipynb`, `Plantcv_for_SPECTRUM_images.ipynb`) and
   shape with the Momocs morphometric codes.
3. **Confirm the ABRS / APEX-TAGES accession** for your
   `ABRS_NASA_Roots_TimeLapse/` set. TAGES used the ABRS GFP-imaging facility on
   the ISS; the matching OSDR study would let you cite the source and pull the
   full-resolution time-lapse. Cross-reference the Gilroy Lab "Matrix of GeneLab
   MetaData" (astrobiology.botany.wisc.edu/astrobotany-toast/matrix-of-genelab-metadata).

## Other imaging datasets (not root/leaf photography — lower priority)

Mostly cellular/tissue **microscopy** (often non-plant): OSD-47, OSD-48,
OSD-137 (pannoramic slide scans); OSD-557, OSD-568, OSD-591, OSD-592, OSD-627,
OSD-628, OSD-662, OSD-898 (confocal / IHC / light microscopy). Cellpose
(`run_cellpose_2.0.ipynb`) could segment cells in the plant ones, but these are
not root-architecture/phenotyping images and aren't the focus here.

## Arabidopsis accessions seen in OSDR (mostly transcriptomics, no images)

OSD-7, 8, 16, 17, 22, 37, 38, 44, 45, 46, 120*, 121*, 134, 136, 144, 147, 193,
205, 208, 210, 213, 217, 218, 219, 220, 223, 251, 281, 282, 296.
(*image-bearing.) The rest are RNA-seq/microarray — useful to pair with the
image phenotypes for genotype↔phenotype analysis, but no images to download.

---

## Suggested next actions

- [ ] Download **OSD-121** images → `data/images/leaves/`, run the morphometric R scripts, add a `datapackage.json`.
- [ ] Download a sample of **OSD-670** crop images → pilot PlantCV leaf-area on a new species.
- [ ] Open **OSD-120** on osdr.nasa.gov, confirm the CARA photography file list vs your `APEX03/`, and record the OSD accession in `data/README.md` for provenance.
- [ ] Resolve the **ABRS/TAGES** accession and link it from `data/README.md`.
- [ ] For every OSDR set added, record the **OSD accession** (provenance) and link the future Zenodo DOI ↔ OSDR accession (see `RELEASING.md`).
