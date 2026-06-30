# RootNav2 on APEX-03 (Path A) — feasible on GPU, but dense plates trace poorly

Closes the open "RootNav2 Path A" item from the
[RootNav2 pilot](../notebooks/rootnav2/) now that the **GPU is available**
(torch 2.6.0+cu124 on a GTX 1050 Ti). Reproducible setup:
[`scripts/rootnav2_setup.sh`](../scripts/rootnav2_setup.sh).

## What ran

RootNav 2.0 (Yasrab et al. 2019) with the **`arabidopsis_plate`** model on
APEX-03 ground-control plates. RootNav 2.0 is a 2019 codebase; it needed two one-
line patches to run on this stack (both in the setup script):
1. `PIL.Image.BICUBIC` → `Image.Resampling.BICUBIC` (Pillow 12 removed it).
2. `torch.load(..., weights_only=False)` (PyTorch 2.6 changed the default).

On the **GPU** it processed each 4000-px plate in **~57 s** and wrote an RSML
trace + a `*_Color_output.png` overlay. (On CPU it would be far slower.)

## Result — fragmented traces on dense plates

For the Col-0 plate it produced an RSML with **149 root segments** and a
segmentation overlay (`results/rootnav2_apex/`). But the trace is **fragmented
and tangled**: the overlay shows seed points and partial root paths that do not
cleanly follow individual roots, and the extracted angles are scattered
(|angle| mean ≈108°, i.e. many lateral/sideways segments), not the clean near-
vertical primaries of the curated [skew RSML](SKEW_ANALYSIS_FINDINGS.md).

**Why:** the `arabidopsis_plate` model was trained on plates with **few,
well-separated** seedlings. The APEX-03 plates have ~15–20 seedlings in a row
with heavily overlapping, crossing roots — so the automatic seed→primary→lateral
tracing mis-assigns and fragments. This **confirms the feasibility caveat** in
the cross-experiment synthesis and the RootNav2 pilot.

## Recommendation

- **Don't rely on RootNav2 automatic tracing for the dense flight/ground
  plates.** For the angle-organisation question, the **model-free
  angle-dispersion** approach
  ([`abrs_angle_analysis.py`](../scripts/python/abrs_angle_analysis.py),
  [`seedling_morphometrics.py`](../scripts/python/seedling_morphometrics.py)) is
  more robust and already answers prediction #1.
- RootNav2 *is* a good fit for **sparse, few-plant** plates — if any OSDR
  Arabidopsis-plate study has those, it would give clean per-root RSML.
- To improve RootNav2 here would require **fine-tuning** the model on labelled
  dense-plate images (the `training/` code in the RootNav-2.0 repo supports this).

## Reproduce
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install kdtree pyyaml
bash scripts/rootnav2_setup.sh APEX03 results/rootnav2_apex
```
