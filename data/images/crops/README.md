# OSD-670 crop leaf images (asteroid-regolith plant growth)

16 photographs from **NASA OSDR study OSD-670** — *"CI Asteroid Regolith as an
In Situ Plant Growth Medium for Space Crop Production"* — downloaded 2026-06-28.
Detached **Lettuce / Radish / Pepper** leaves laid on **cm graph paper**.

- **Source:** https://osdr.nasa.gov/bio/repo/data/studies/OSD-670
- **Fetched with:** `python scripts/python/osdr_download.py 670 --ext jpg,jpeg --out data/images/crops`
- **Files:** 11 per-crop leaf photos (`LSDS-73_morphometric-photography_ExpA_B{1,2,3}_{Lettuce,Radish,Pepper}*`)
  + 5 block-overview `OSD-670_sup_ExpA/B-Block*` jpegs.
- **License:** NASA OSDR data — see [`../../../LICENSE-DATA.md`](../../../LICENSE-DATA.md). Attribute NASA OSDR / OSD-670.
- **Integrity:** `MANIFEST.sha256.csv` records SHA-256 + size for verification.

## Analysis

PlantCV leaf-area pilot:

```bash
python scripts/python/plantcv_crops_leafarea.py --grid-mm 5
```

Segments leaf tissue (LAB colourfulness), counts/measures leaves per image,
calibrates from the graph-paper grid, groups by species. Writes to
`results/osd670_leafarea/`. See
[`../../../docs/OSD670_PLANTCV_PILOT.md`](../../../docs/OSD670_PLANTCV_PILOT.md).
