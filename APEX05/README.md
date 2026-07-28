# APEX05 — root architecture dataset

Mirror of the APEX05 spaceflight root-architecture study, imported from Google
Drive for use in the [AstroBotany calibration image database](https://dr-richard-barker.github.io/AstroBotany_calibration_image_sharing_and_analysis/)
and the [AstroRoot](https://dr-richard-barker.github.io/astroroot/) RSML viewer.

*Arabidopsis thaliana* seedlings (genotypes **Col-0**, **cax2-2**, **cax2-3**,
**rbohD**) grown in **Flight** (spaceflight) and **Ground control** conditions,
imaged over an ~8-day time course. Root system architecture was traced with
[SmartRoot](https://smartroot.github.io/) / [archiDART](https://archidart.github.io/)
into RSML.

## Contents

| Folder | What | Count |
|---|---|---|
| `images/` | Curated, web-compressed specimen photos (JPEG, ≤1600 px). Camera originals on Drive are ~10 MB each; these are downscaled for browsing. | 120 |
| `images/metadata.csv` | Per-image metadata (condition, day, genotype, processing, original Drive path) — sidecar read by the calibration database gallery. | — |
| `rsml/` | SmartRoot RSML traces (`.rsml` plus SmartRoot revision files `.rsml01`–`.rsml04`), preserving the original Drive folder grouping. | 424 |
| `code/` | Analysis code: the AstroDart R/ImageJ toolkit, archiDART example scripts, and `RSML_APEX_DRB.R`. | 11 |
| `graphs/` | Rendered result figures (root-trait comparisons, GC vs FL). | 10 |

The `images/` selection is a representative subset spanning both conditions,
all four genotypes, and days 1–8 (the full set of 846 camera-original JPEGs is
~8 GB and was not mirrored). RSML, code and graphs are mirrored in full.

## Provenance

Source: Google Drive folder `APEX05` (owner: dr-richard-barker). Images were
downscaled and re-encoded (EXIF stripped); RSML, code and graphs are byte-for-byte
copies. `source_path` in `metadata.csv` records each image's original Drive path.
