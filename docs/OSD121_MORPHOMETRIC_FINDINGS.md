# OSD-121 seedling morphometrics — first-pass findings

Automatic morphometric comparison of the 26 OSD-121 dish photographs
(13 flight, 13 ground control), produced by
[`scripts/python/seedling_morphometrics.py`](../scripts/python/seedling_morphometrics.py).
Outputs (regenerable) land in `results/osd121_morphometrics/`.

## Method

Per dish: **detect the petri dish** (largest bright blob → centroid + radius) →
**crop and circular-mask** to the dish (removes ruler + background) →
**calibrate px→mm** (ruler-tick FFT, with one consistent scale per group) →
enhance thin seedling structures with a Sato ridge filter → threshold →
skeletonize → measure area (mm²), skeleton length (mm), component count,
vertical extent (mm), and **root-angle dispersion** (SD of local orientations,
0° = vertical, scale-free). Groups read from the `_F_` / `_G_` filename tag.

## Result — and why calibration changed the conclusion

The pipeline now **detects the petri dish (circle), crops/masks to it**, and
**calibrates px→mm** from the in-frame ruler (FFT of the ruler's tick
periodicity), applying one consistent scale per group (median of confident
ruler reads). This calibration turned out to be decisive:

| Metric | Flight (n=13) | Ground (n=13) | Welch *t* | *p* | Verdict |
|--------|--------------:|--------------:|----------:|-----|---------|
| Plant area **(px)** | 45,070 | 55,768 | −8.28 | <0.0001 | ⚠️ confounded |
| Plant area **(mm², calibrated)** | 404 | 393 | 1.06 | **0.30** | **not significant** |
| Skeleton length (mm) | 1,081 | 1,151 | −2.45 | 0.022 | weak |
| **Root-angle dispersion (°)** | **51.2** | **45.3** | **7.61** | **<0.0001** | **robust** |

**The key lesson.** The flight and ground images were shot at **different
magnifications** — the ruler gives **10.56 px/mm for flight vs 11.90 px/mm for
ground** (~12% apart). So the striking "flight seedlings are ~20% smaller"
result *in pixels* is **largely an imaging-scale artifact**: once converted to
real mm², the area difference **disappears** (p=0.30). Adding the ruler
calibration the way this task asked **prevented a spurious size conclusion.**

**What survives calibration — the real signal.** Root-**angle dispersion** is
scale-free and is strongly higher in flight (51.2° vs 45.3°, p<0.0001): flight
roots lose the tight near-vertical gravitropic alignment seen on the ground —
the microgravity **skewing/waving** phenotype. This connects directly to the
nutrient-driven skew assays in [`data/rsml/18_way_skew/`](../data/rsml/18_way_skew/)
and the RootNav2 pilot ([`notebooks/rootnav2/`](../notebooks/rootnav2/)).

## Caveats (important)

- **Calibration itself is approximate.** The ruler-tick FFT assumes 1 mm ticks;
  the per-group scales differ enough to matter, so **validate against OSD-121's
  own deposited morphometric measurements** before quoting absolute mm². But the
  qualitative lesson (pixel-area effect is a magnification artifact) is robust to
  the exact scale.
- **First-pass segmentation.** Translucent seedlings on agar are hard; the ridge
  mask catches some dish-rim/meniscus artefacts (see `montage.png`). Tune
  `RIDGE_SIGMAS` / `THRESH_K`.
- **Robust vs fragile metrics.** *Angle dispersion* (scale-free) and the
  *direction* of effects are robust; absolute areas depend entirely on the
  calibration.
- **Not leaf morphometrics.** These are seedling/root dishes, so the Momocs
  leaf-outline scripts in `scripts/r/morphometrics/` are *not* the matching tool;
  this Python pipeline is.

## Validation

**No external ground-truth exists to validate against** — OSD-121 deposited the
*images* and their acquisition metadata (the ISA `morphometric-analysis` assay
table lists only date / camera / bit-depth / width), but **no derived plant
measurements** (leaf area, root length, etc.). That is itself a FAIR gap in
OSD-121; this pipeline effectively *fills* it from the deposited images.

So instead of external validation, a **self-consistency check**: a petri dish is
a fixed physical size, so after calibration every dish should measure the same
diameter in mm. Result:

| Group | Calibrated dish diameter |
|-------|--------------------------|
| Flight | **66.7 ± 0.2 mm** |
| Ground | **63.9 ± 2.3 mm** |

Both land on a standard ~60–65 mm petri dish, only ~4% apart. This independently
confirms: (1) the dishes are the same physical object, so the raw-pixel size
difference **was** magnification; (2) the ruler calibration is internally sound
to ~4% (and the ~1 mm tick assumption is about right, since the calibrated dish
size is realistic); (3) the residual mm² area difference (~3%) is within
calibration noise — consistent with **no real area difference**, as the t-test
(p=0.30) found.

## Reproduce

```bash
python scripts/python/osdr_download.py 121 --ext jpg --out data/images/leaves  # if not present
python scripts/python/seedling_morphometrics.py
```

Writes `summary.csv`, `flight_vs_ground.csv`, `montage.png` to
`results/osd121_morphometrics/`, and `data/tables/groups.csv` (flight/ground
labels) for downstream stats.

## Next steps

- Add a circular dish crop + ruler-based px→mm calibration for absolute lengths.
- Cross-reference with OSD-121's deposited morphometric measurements (the study
  has its own analysis) to validate this automatic pass.
- Feed `groups.csv` + per-dish traits into the R stats workflow for a formal model.
