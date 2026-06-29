# ABRS root-angle dispersion — testing synthesis prediction #1

Prediction #1 (from [the synthesis](CROSS_EXPERIMENT_SYNTHESIS.md)): spaceflight
roots lose tight directional alignment, so **flight angle dispersion > ground**,
as OSD-121 showed. This tests it on the ABRS 11-day time-lapse.
Script: [`scripts/python/abrs_angle_analysis.py`](../scripts/python/abrs_angle_analysis.py); outputs in `results/abrs_angle/`.

## Result — direction supports the prediction

| Metric (mean over 11 days) | Flight | Ground |
|----------------------------|-------:|-------:|
| Root-angle dispersion (°) | **59.1** | 57.7 |
| Mean \|angle from vertical\| (°) | **51.7** | 48.7 |

Flight roots stay **consistently more dispersed and more deviated from vertical**
than ground for most of the time course (days 0–7; see `timecourse.png`), with
the two converging late (days 8–10). The **direction matches prediction #1** and
the OSD-121 result.

## Important caveats (why this is suggestive, not conclusive)

- **n = 1 plate per condition.** ABRS here is a *single* flight plate vs a
  *single* ground plate imaged over 11 days — the timepoints are not independent
  replicates. This is a **descriptive time course**, not a powered test (unlike
  OSD-121's 13 dishes/group, p<1e-4). The ~1–3° flight–ground gap is small.
- **Grid contamination inflates absolute values.** The chamber's etched grid adds
  fixed 0°/90° components, so ABRS dispersion (~57–61°) is not comparable to
  OSD-121 (~45–51°). But the grid is identical in both conditions, so the
  flight-vs-ground **contrast** remains informative.
- **Late convergence.** Ground dispersion rises again at days 8–10 (roots may be
  reaching plate edges / spreading), narrowing the gap — worth a closer look.

## Verdict

Prediction #1 is **directionally confirmed** on ABRS (flight > ground angle
dispersion), consistent with OSD-121, but the single-plate design makes it
suggestive rather than statistically powered. To strengthen it: analyse the
fuller `ABRS_Flight/` and `ABRS_Ground_control/` frame sets (28 + 39 frames),
suppress the grid (e.g. notch-filter the 0/90° orientations), or — best —
quantify additional independent flight/ground plates if available in OSDR.

## Reproduce
```bash
python scripts/python/abrs_angle_analysis.py
```
