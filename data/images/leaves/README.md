# OSD-121 seedling morphometric photographs

26 JPG photographs downloaded from **NASA OSDR study OSD-121** (Arabidopsis
morphometric photography, flight vs ground), 2026-06-28.

> **What these actually are:** petri **dishes of Arabidopsis seedlings**
> photographed against a ruler — i.e. whole-seedling / root-system morphometry,
> **not** isolated leaf outlines. (The folder is named `leaves/` for continuity
> with the morphometric R workflow, but the Momocs leaf-outline scripts are not
> the right tool here — use the seedling/root pipeline below.)

- **Source:** https://osdr.nasa.gov/bio/repo/data/studies/OSD-121
- **Files:** 6 `LSDS-56_morphometric-photography_{F,G}_*` + 20 `OSD-121_sup_{F,G}_*`
  (`F` = flight, `G` = ground control). 4000×3000 px JPEG, ~3.2 MB each.
- **License:** NASA OSDR data — see [`../../../LICENSE-DATA.md`](../../../LICENSE-DATA.md).
  Attribute NASA OSDR / OSD-121.

## Provenance & integrity (kept in-repo *and* reproducible)

These images are **committed to the repo** for convenience **and** are fully
reproducible from OSDR:

```bash
# re-fetch (skips files already present):
python scripts/python/osdr_download.py 121 --ext jpg --out data/images/leaves
# verify the in-repo copies against their recorded hashes:
python - <<'PY'
import hashlib,csv,os
for r in csv.DictReader(open("data/images/leaves/MANIFEST.sha256.csv")):
    h=hashlib.sha256(open(os.path.join("data/images/leaves",r["filename"]),"rb").read()).hexdigest()
    print("OK " if h==r["sha256"] else "BAD", r["filename"])
PY
```

`MANIFEST.sha256.csv` records the SHA-256 + size of every file so the committed
copies can be validated against the OSDR originals at any time.

## Analysis

These dishes are analysed by the seedling/root morphometric pipeline, not the
leaf-outline Momocs scripts:

```bash
python scripts/python/seedling_morphometrics.py
```

It segments the seedlings in each dish, computes per-dish morphometrics
(plant area, root-system extent, angular dispersion), writes a results table +
montage to `results/osd121_morphometrics/`, and emits a
`data/tables/groups.csv` (flight/ground labels) for downstream stats.
