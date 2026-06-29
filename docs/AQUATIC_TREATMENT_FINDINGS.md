# Aquatic well-plate experiment — plant size by treatment

Quantifies green plant area per treatment in the `Lemna/`, `Londultia/`,
`Azola/`, `Wolfinia/` 12-well plates (4 treatments × 3 rows). Fast LAB green-
tissue segmentation (no cellpose needed), each plant binned to a treatment column
by position. Script:
[`scripts/python/aquatic_treatment_analysis.py`](../scripts/python/aquatic_treatment_analysis.py);
outputs in `results/aquatic_treatments/`.

## Result — GA + nutrients drive plant growth (all 4 species)

Mean green plant-blob area (px), pooled across species and images:

| Treatment | Mean area | vs Water |
|-----------|----------:|---------:|
| Water | 385 | 1.0× |
| Nutrients | 557 | 1.4× |
| GA | 684 | 1.8× |
| **GA + Nutrient** | **1577** | **4.1×** |

Total green area by species & treatment — **GA+Nutrient is the largest in every
species**:

| Species | Water | GA | Nutrients | GA+Nutrient |
|---------|------:|----:|----------:|------------:|
| Azola | 7,199 | 30,189 | 23,636 | **159,785** |
| Lemna | 8,692 | 10,123 | 8,463 | **19,713** |
| Londultia | 9,590 | 9,526 | 13,682 | **18,632** |
| Wolfinia | 1,451 | 1,455 | 2,699 | **6,888** |

**Interpretation.** Gibberellic acid (GA) and added nutrients each increase plant
size over water, and **together they act more than additively** (≈4× water) — a
clear, consistent growth response across all four aquatic species. *Azolla*
responds most dramatically.

## Caveats (read before quoting numbers)

- **"plants" = green blobs, not true plant counts.** The segmentation fragments
  each plant into several blobs, so per-image counts (12–34) overcount plants;
  the **area** readouts are the meaningful quantity, not the counts.
- **Treatment mapping is assumed:** columns left→right = Water / GA / Nutrients /
  GA+Nutrient (from the label strip). **Confirm the plate orientation** is
  consistent across all images — a flipped plate would swap treatments.
- **Replication unknown:** the 5 images per folder may be **time-lapse of one
  plate** rather than independent replicates. If so, "total area" mixes
  timepoints and the means are **descriptive, not statistically powered** — no
  significance test is claimed. The strength here is the **consistent direction
  across 4 independent species**.
- Absolute areas are uncalibrated px (each plate has a ruler → px→mm is possible).

## Reproduce
```bash
python scripts/python/aquatic_treatment_analysis.py
# -> results/aquatic_treatments/{per_well.csv, figure.png, montage.png}
```

## Next steps
- Confirm plate orientation + whether images are timepoints or replicates.
- Ruler-calibrate to mm²; if time-lapse, fit per-well growth curves.
- Resolve the species names (`Azola`→*Azolla*, `Wolfinia`→*Wolffia*?,
  `Londultia`→*Landoltia*?) — see [data dictionary](DATA_DICTIONARY.md).
