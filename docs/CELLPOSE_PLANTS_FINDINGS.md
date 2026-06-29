# Cellpose plant segmentation — Lemna / Londultia well plates

Adapting the repo's Cellpose *cell*-segmentation notebooks to segment whole
**plants** in the aquatic-plant well-plate photos (`Lemna/`, `Londultia/`):
12-well plates of small green plants (Water / GA / Nutrients / GA+Nutrient
treatments) shot with a ruler. Script:
[`scripts/python/cellpose_plant_segmentation.py`](../scripts/python/cellpose_plant_segmentation.py);
outputs in `results/cellpose_plants/`.

## Result (sample: 1 plate per folder)

| Plate | Objects detected | Total area (px) | Mean area (px) |
|-------|-----------------:|----------------:|---------------:|
| `Lemna/IMG_1211` | **12** | 53,199 | 4,433 |
| `Londultia/IMG_1212` | **15** | 53,119 | 3,541 |

Cellpose segments **one object per well** for Lemna (12 wells → 12 objects) and a
few extra for Londultia (15) where wells held multiple plantlets. The overlay
(`montage.png`) shows each well/plant as a distinct labelled region. So this
gives reliable **plant-per-well counts** and a per-well size proxy.

## What it does / doesn't do

- ✅ **Works on these macro plate photos** (the original notebooks targeted
  microscopy cells). Version-robust: uses cellpose 3.x's fast CNN `cyto3` model
  when available, else cellpose 4.x / cellpose-SAM.
- ✅ **Counts plants per well** correctly (12 ≈ the 12-well layout).
- ⚠️ **Segments the well/plant unit, not pure leaf tissue** — the reported "area"
  includes the well disc, not only the green plant. For true leaf area, mask to
  green tissue inside each cellpose region (the LAB-colourfulness approach in
  [`plantcv_crops_leafarea.py`](../scripts/python/plantcv_crops_leafarea.py)
  is the complementary tool), or tune `--diameter` to the plant size.

## Performance note (environment)

This machine has a GTX 1050 Ti, but **Python 3.13 has no CUDA torch wheels** and
**cellpose 3.x won't build on 3.13**, so only **cellpose 4.x (SAM, a ViT)** is
available, on **CPU**: ~24 min/image at 512 px (≈10 min at 384 px). Full-batch
processing is impractical here. To run all plates quickly, use a **Python 3.11
env** — that unlocks both the GPU (`pip install torch --index-url .../cu121`) and
cellpose 3.x's fast CNN models, dropping inference to seconds per image.

## Reproduce

```bash
# sample (what produced the table above):
python scripts/python/cellpose_plant_segmentation.py --folders Lemna Londultia --limit 1 --target-w 384
# full set (slow on CPU here; fast on a py3.11+GPU env):
python scripts/python/cellpose_plant_segmentation.py
```
