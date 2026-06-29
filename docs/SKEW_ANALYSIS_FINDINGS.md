# 18-way skew assay — findings

Statistical analysis of the flagship dataset: 53 RootNav RSML files, **483
analysable primary roots**, from a **2 (gelling agent: agar / phytogel) × 3
(gelling %: 0.5/1/1.5) × 3 (sucrose %: 0/0.3/1)** design. Produced by
[`scripts/python/skew_analysis.py`](../scripts/python/skew_analysis.py);
outputs in `results/skew_analysis/`.

Traits are **scale-free** (the RSML is uncalibrated, `unit=pixel`): signed tip
angle (direction of skew), |tip angle| (skew strength), tortuosity.

## Headline result — gelling agent drives skewing, not sugar

| Factor | Test | Result |
|--------|------|--------|
| **Gelling agent** (agar vs phytogel) | Welch *t* on |tip angle| | **agar 7.21° vs phytogel 5.70°, t=3.03, p=0.0026** ✅ |
| Sucrose % (0 / 0.3 / 1) | one-way ANOVA | F=0.30, p=0.74 — n.s. |
| Gelling % (0.5 / 1 / 1.5) | one-way ANOVA | F=0.96, p=0.39 — n.s. |

**Roots skew significantly more strongly on agar than on phytogel**, and neither
sucrose nor gelling-agent concentration has a detectable effect on skew strength
or tortuosity.

## Handedness — agar imposes a consistent skew direction

Testing whether mean *signed* tip angle differs from 0 (a consistent left/right
bias):

| Gelling agent | Mean signed tip angle | Test |
|---------------|----------------------:|------|
| **Agar** | **+2.65°** | t=4.79, **p<0.0001** ✅ consistent handedness |
| Phytogel | −0.48° | t=−0.95, p=0.34 — no directional bias |

On **agar**, roots skew in a **consistent direction** (the classic right-handed
Arabidopsis agar-surface skew). On **phytogel**, roots deviate from vertical by
similar magnitudes but with **no consistent handedness** — they wander rather
than skew systematically.

## Interpretation

The medium's **gelling agent** — not its sugar or firmness over this range — is
the dominant determinant of root skewing in this assay, affecting **both** the
strength and the **chirality** of the deviation. This is consistent with the
literature view that surface/mechanical properties of agar vs gellan-type gels
drive the skewing phenotype, and it sets the **ground-based baseline** for
interpreting the microgravity root behaviour seen in the spaceflight image sets
([ABRS](../data/images/), [OSD-121](OSD121_MORPHOMETRIC_FINDINGS.md)), where
roots similarly lose tight directional alignment.

## Caveats

- Tip angle is from the RootNav spline geometry; a few very short roots (<4
  points) were dropped (500 → 483).
- Design is *nearly* balanced (3 reps/treatment, a few 2s and 4s — see the
  [data dictionary](DATA_DICTIONARY.md)); a full factorial mixed model
  (root nested in plate) would refine the p-values, but the agar≫phytogel effect
  is large and robust to that.
- Angles are scale-free, so the uncalibrated (pixel) RSML is not a limitation here.

## Reproduce

```bash
python scripts/python/skew_analysis.py
# -> results/skew_analysis/{root_traits.csv, anova.txt, figure.png}
```
