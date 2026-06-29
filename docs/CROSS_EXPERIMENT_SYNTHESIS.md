# Cross-experiment synthesis — what organises root growth direction, on the ground and in space

This repo's separate analyses turn out to tell one story. Pulling them together
gives a unifying readout (**root-angle organisation**) and a testable model that
connects the ground-based nutrient-skew assay to the spaceflight image sets.

> **Status:** the individual results are quantified (links below); the unifying
> model here is an **interpretation / hypothesis** that the data support and that
> makes testable predictions — not a proven claim.

## The common question

Across every dataset in this repo, the underlying question is the same:
**what controls the *direction* and *organisation* of root growth** — and what
happens to it when you change the medium, or remove gravity?

The key insight is that a single **scale-free** readout — the **distribution of
root angles** (its spread = dispersion, its mean = handedness) — is measurable in
*all* of them, and is robust to the calibration problems that plague absolute
sizes (see the calibration lesson below).

## What each dataset showed

| Dataset | Setting | Readout | Result | Source |
|---------|---------|---------|--------|--------|
| **18-way skew** (RSML, ground) | agar vs phytogel × conc × sucrose | tip-angle strength + handedness | **Agar** → stronger skew (7.2° vs 5.7°, p=0.003) **and consistent handedness** (+2.65°, p<1e-4); **phytogel** → no handedness | [skew findings](SKEW_ANALYSIS_FINDINGS.md) |
| **OSD-121** (images, flight vs ground) | spaceflight Arabidopsis seedlings | root-angle dispersion | **Flight > ground dispersion** (51.2° vs 45.3°, p<1e-4); size difference was a calibration artifact | [OSD-121 findings](OSD121_MORPHOMETRIC_FINDINGS.md) |
| **ABRS time-lapse** (images, flight vs ground) | spaceflight root growth | qualitative angle organisation | Flight roots visibly **disorganised / multi-directional**; ground roots gravitropic-vertical | [data](../data/images/) |
| **APEX-03** (images, flight vs ground) | *sku* skewing mutants + WT | (imaging context) | Includes `Sku5`/`Sku6` skewing mutants — the genetic handle on the same phenotype | [data](../data/images/) |

## The unifying model

**On the ground**, gravity supplies a dominant directional cue and roots align
near-vertical. The medium then modulates the *residual* skewing:
- **agar** imposes a **consistent chiral (handed) skew** — a reproducible
  surface/mechanical interaction;
- **phytogel** permits similar-magnitude deviation but **without handedness** —
  roots *wander* rather than skew systematically.

**In microgravity**, the dominant cue (gravity) is removed, and roots **lose
tight directional alignment → angle dispersion rises** (OSD-121, quantified;
ABRS, qualitative). Phenotypically this **resembles the phytogel case**: remove
the organising vector (gravity, or the agar-surface interaction) and you get
dispersed, non-handed growth.

So the same axis — *organised/handed* ↔ *dispersed/wandering* — is moved by
**either** changing the gelling agent **or** removing gravity. Skewing strength
and angular dispersion are two views of how strongly root growth direction is
being constrained.

## Why angles, not sizes — the calibration lesson

The OSD-121 analysis is a cautionary tale: flight seedlings looked ~20% smaller,
but that was a **~12% imaging-magnification difference** (flight 10.6 vs ground
11.9 px/mm, validated by the calibrated dish diameters matching at ~65 mm). In
real mm², the size difference vanished (p=0.30). **Angle dispersion and
handedness need no calibration**, which is exactly why they are the right common
currency for comparing across these heterogeneously-imaged datasets.

## Testable predictions

1. **ABRS, quantified:** running the angle-dispersion pipeline (RootNav2 Path A,
   or the model-free Path B in [`notebooks/rootnav2/`](../notebooks/rootnav2/))
   on ABRS flight vs ground should reproduce **flight > ground dispersion**, as
   OSD-121 did.
2. **Genetics (APEX-03):** `sku` mutants — already perturbed in handed skewing on
   the ground — should show an **altered dispersion response** to spaceflight vs WT.
3. **Medium × gravity interaction:** phytogel-grown roots (already non-handed on
   the ground) should show a **smaller** ground→flight increase in dispersion
   than agar-grown roots, if gravity and the agar interaction act on the same axis.
4. **Mechanism (omics link):** the root-skewing loci and their OSDR spaceflight
   DEG intersections in the sibling **CARA_GeneLab_AWG** repo are candidate genes
   bridging the phenotype here to expression — a phenotype↔transcriptome bridge.

## How to reproduce / extend

```bash
python scripts/python/skew_analysis.py            # ground baseline (handedness)
python scripts/python/seedling_morphometrics.py   # OSD-121 flight vs ground dispersion
# then: RootNav2 pilot notebook on ABRS frames to close prediction #1
```

All datasets carry their **OSD accession** for provenance; pair the phenotypes
here with the matching OSDR transcriptomics (e.g. OSD-120/121) for the
genotype↔phenotype analyses above.
