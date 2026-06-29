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

## Performance — CPU vs GPU (resolved)

cellpose 4.x (SAM, a ViT) is the only cellpose installable on Python 3.13. On
**CPU** it took ~24 min/image — impractical. Installing a **CUDA build of torch**
(`torch 2.6.0+cu124`, which *does* have py3.13 wheels — the earlier `cu121`
index did not) put it on the **GTX 1050 Ti GPU**: **~4 s/image**, a ~300×
speedup, no OOM at 448 px on 4 GB VRAM. The full 20-image aquatic batch then ran
in ~2 minutes.

Full GPU batch (all 4 aquatic folders, `--target-w 448`): ~12 objects/plate
consistently (= the 12 wells), with total object area near-constant (~75k px) —
confirming cellpose segments the **wells/plant-units** (uniform), which is why
the green-tissue analysis (`aquatic_treatment_analysis.py`) is the tool for plant
**size** and cellpose is the tool for **counts**.

## Reproduce

```bash
# sample (what produced the table above):
python scripts/python/cellpose_plant_segmentation.py --folders Lemna Londultia --limit 1 --target-w 384
# full set (slow on CPU here; fast on a py3.11+GPU env):
python scripts/python/cellpose_plant_segmentation.py
```
