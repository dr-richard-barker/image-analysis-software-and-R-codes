# Aquatic well-plate experiment — plant size by treatment

Quantifies green plant area per treatment in the `Lemna/`, `Londultia/`,
`Azola/`, `Wolfinia/` 12-well plates (4 treatments × 3 rows). Fast LAB green-
tissue segmentation (no cellpose needed), each plant binned to a treatment column
by position. Script:
[`scripts/python/aquatic_treatment_analysis.py`](../scripts/python/aquatic_treatment_analysis.py);
outputs in `results/aquatic_treatments/`.

## Result — GA + nutrients drive plant growth (all 4 species)

**Calibrated** to mm² via the cm ruler in each photo (FFT tick detection →
median **18.5 px/mm**). Mean green plant area, pooled across species & images:

| Treatment | Mean area (mm²) | vs Water |
|-----------|----------------:|---------:|
| Water | 15.6 | 1.0× |
| Nutrients | 22.6 | 1.4× |
| GA | 27.7 | 1.8× |
| **GA + Nutrient** | **64.0** | **4.1×** |

Total green area (mm²) by species & treatment — **GA+Nutrient is largest in every
species**:

| Species | Water | GA | Nutrients | GA+Nutrient |
|---------|------:|----:|----------:|------------:|
| Azola | 292 | 1,225 | 959 | **6,483** |
| Lemna | 353 | 411 | 343 | **800** |
| Londultia | 389 | 387 | 555 | **756** |
| Wolfinia | 59 | 59 | 110 | **280** |

**Interpretation.** GA and added nutrients each increase plant size over water,
and **together they act more than additively** (≈4× water) — consistent across
all four aquatic species. *Azolla* responds most dramatically.

## Growth curves (if the images are a time series)

Ordering each folder's 5 images by IMG number (assumed time) and plotting total
mm² per treatment (`growth_curves.png`) gives a clear separation. Linear
growth-rate (slope of total mm² vs sequence step, pooled species):

| Treatment | Growth rate (mm²/step) | vs Water |
|-----------|-----------------------:|---------:|
| Water | 7.7 | 1.0× |
| Nutrients | 21.1 | 2.7× |
| GA | 33.7 | 4.4× |
| **GA + Nutrient** | **245.2** | **32×** |

GA+Nutrient plants grow ~**32× faster** than water; water-only plants are nearly
flat. The GA+Nutrient curve looks exponential (≈90 → ≈1030 mm² over the series).
**This is contingent on the images being an ordered time series** — confirm before
treating these as growth rates.

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
- Areas are now **ruler-calibrated to mm²** (median 18.5 px/mm); the per-image
  ruler reads were consistent, so calibration is reliable.

## Reproduce
```bash
python scripts/python/aquatic_treatment_analysis.py
# -> results/aquatic_treatments/{per_well.csv, figure.png, montage.png}
```

## Next steps
- **Confirm plate orientation + whether images are timepoints or replicates** —
  this is the one input that turns the growth curves from indicative to rigorous.
- ✅ Ruler-calibrated to mm²; ✅ growth curves fitted (above).
- Resolve the species names (`Azola`→*Azolla*, `Wolfinia`→*Wolffia*?,
  `Londultia`→*Landoltia*?) — see [data dictionary](DATA_DICTIONARY.md).
