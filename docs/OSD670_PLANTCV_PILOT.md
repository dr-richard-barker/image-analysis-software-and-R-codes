# OSD-670 crop leaf-area — PlantCV pilot

First-pass PlantCV analysis of the OSD-670 crop images (lettuce / radish /
pepper leaves on cm graph paper), produced by
[`scripts/python/plantcv_crops_leafarea.py`](../scripts/python/plantcv_crops_leafarea.py).
Outputs (regenerable) land in `results/osd670_leafarea/`.

## Method

PlantCV reads each image and extracts LAB channels. Leaf tissue is **coloured**
while the paper is white and the grid is light blue, so a **colourfulness** map
(distance from the neutral LAB point) isolates leaves; morphological clean-up
+ size-gating drops the grid and specks. Touching leaves are then split by
**watershed instance segmentation** (distance transform → peak markers) so the
count reflects individual leaves. px→mm comes from the **graph-paper grid
period** (FFT, default 5 mm squares). Species are read from the filename.

## Result (11 per-crop images, watershed counts)

| Species | mean leaves/img | mean total leaf area (px) |
|---------|----------------:|--------------------------:|
| Lettuce | 23 | 131,378 |
| Pepper  | 36 | 104,135 |
| Radish  | 59 | 417,520 |

Radish shows the most leaves and the largest total leaf area; the montage
confirms the segmentation captures the individual leaves well.

## Caveats

- **Leaf counts are improved but still approximate.** Watershed roughly halved the
  raw connected-component counts (which over-segmented folded leaves) to a
  plausible range, but dense multi-row layouts (the `B3` images) and small
  fragments still inflate counts somewhat. With no deposited ground-truth leaf
  count to tune against, treat counts as indicative; **total leaf area per image
  is the most trustworthy readout.**
- **Grid calibration is noisy** (per-image px/mm ranged ~8–16), so absolute mm²
  are indicative only — same calibration challenge as OSD-121. Use the grid more
  robustly (fit the full 2-D lattice) before quoting mm².
- Block-overview `*_sup_*` montages are skipped (multi-block, not single-crop).

## Reuse / next steps

- This validates that the repo's **PlantCV** workflows extend cleanly to OSDR
  crop datasets (a new food-crop angle beyond Arabidopsis).
- Swap in `SpaceChile_phenotyping_v1.ipynb`-style colour analysis for leaf
  colour/health, or add watershed instance segmentation for true leaf counts.
- Reproduce:
  ```bash
  python scripts/python/osdr_download.py 670 --ext jpg,jpeg --out data/images/crops
  python scripts/python/plantcv_crops_leafarea.py --grid-mm 5
  ```
