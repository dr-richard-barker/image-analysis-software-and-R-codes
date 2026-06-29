# Assessment — `CARA_GeneLab_AWG` repo (FAIR + tidy)

Review of **https://github.com/dr-richard-barker/CARA_GeneLab_AWG** and how it
should relate to *this* image-analysis repo. Inspected 2026-06-28 via the GitHub
API (231 files).

## What it is

A **GitBook manuscript + omics re-analysis** for the CARA study —
*"Modulation of Photomorphogenesis in Spaceflight Influences Root System
Architecture"* (an OSDR Analysis Working Group paper in progress). Contents:

- **Narrative chapters** (`*.md`): introduction, plant tropisms & microgravity,
  gravitropism, epigenetic map of the root tip, discussion, conclusion,
  references — plus a `SUMMARY.md` GitBook ToC.
- **`methods/`** — ANOVA reports for root **diameter / length / surface /
  volume** physiology, and a GLARE-paper summary. (These mirror the root
  physiology in *this* repo's `RACARA_root_physio.ipynb`.)
- **`results/`** — GO enrichment (`GONetwork.cys/.xgmml`, `GO_*.csv`), PPI/MCODE
  enrichment, `Evidence.csv`, **root-skewing loci tables** (from BMC Plant Biol.
  2017, `12870_2017_975`), and **Metascape** intersections of skewing loci with
  OSDR (`skewing_OSDR_intersct_metascape*.xlsx`), an `AnalysisReport.html/pptx`,
  and a vendored **Cytoscape.js** web export (`results/CyJS/…`).
- **113 `.gitbook/assets/`** — mostly per-gene structure figures
  (`AT1G…-GENE front/back.jpg`).
- **`LICENSE`** — Creative Commons (good for a data/manuscript repo).

In short: it's the **omics / network-biology + write-up** companion to the
**image-analysis / phenotyping** work in this repo. Both orbit the same CARA
experiment (**OSDR OSD-120**) and the same root-skewing biology (this repo's
`18_way_skew` ↔ CARA's skewing-loci tables).

## FAIR scorecard

| Principle | State | Notes |
|-----------|-------|-------|
| **Findable** | 🟡 | Has a GitBook + structure, but no `CITATION.cff`, no DOI, no OSD accession recorded. |
| **Accessible** | 🟢 | Public, CC-licensed, plain files. |
| **Interoperable** | 🟡 | CSV/XGMML/CYS are open formats, but **no data dictionary / datapackage** for the GO/PPI/skewing tables; column meanings undocumented. |
| **Reusable** | 🟡 | CC license is good; hurt by duplicate assets, vendored web libs, and no provenance linking figures→data→OSDR. |

## Tidy issues (concrete)

> **Verified 2026-06-28 by cloning the repo.** Two findings were sharper than the
> first-pass review and are reflected below.

0. **🔴 CRITICAL — the repo can't be checked out on Windows.** Three files contain
   a `|` character (illegal in Windows filenames):
   `results/Enrichment_PPI/tortosity|5 OSDR|3 OSDR_PPIColorByCluster.{pdf,png}` and
   `results/Enrichment_PPI/xgmml/tortosity|5 OSDR|3 OSDR.xgmml`. `git clone` on
   Windows yields **zero working files** — even `git rm` of those paths errors
   (`invalid path`). Fix first. (`tortosity` is also a typo for `tortuosity`.)
1. **Duplicate assets — 32 `(1)/(2)` files, but only 15 are true duplicates.**
   Verified via git blob hashes: the 15 byte-identical ones are the gene-structure
   `AT…(1).jpg`. The other 17 — the `image (N).png` series and `README (1).md` —
   are **distinct content**, NOT duplicates. Remove only the hash-identical 15;
   a name-based bulk delete would destroy real figures. (`cara_tidy/tidy_cara.sh`
   does this safely, hash-gated.)
2. **Two READMEs** — `README.md` + `README (1).md` (same collision this repo
   had). Consolidate to one.
3. **Vendored web app** — `results/CyJS/bower_components/…` incl. a 715 KB
   `vendor.js` and bundled fonts (eot/ttf/woff/svg). Bower is deprecated; this
   is bloat. Keep the **source network** (`.xgmml`/`.cys`) + a link to an online
   Cytoscape viewer instead of committing the whole exported site.
4. **Undocumented data** — `GO_*.csv`, `Evidence.csv`, skewing-loci tables,
   Metascape `.xlsx` have no schema/README. Add a `results/README.md` +
   `datapackage.json` defining each table and its source.
5. **No `CITATION.cff` / DOI** — add both; mint a Zenodo DOI like this repo.
6. **No OSDR linkage** — record the **OSD-120** accession (and any others) so the
   manuscript, data, and the spaceflight study are mutually discoverable.
7. **Large binaries in git** — `AnalysisReport.pptx` (832 KB), HTML report →
   consider Releases, as with this repo's binaries.
8. **Filenames with `|`** — e.g. `tortosity|5 OSDR|3 OSDR.xgmml` (also a typo,
   "tortosity"). Pipe chars break some tools/OSes; rename.

## The key decision — two repos, one CARA story

`CARA_GeneLab_AWG` (omics + manuscript) and this repo (image analysis + tools +
RSML/phenotype data) **overlap** (CARA root physiology lives in both). Don't
merge them — that muddies a clean tools repo with a manuscript. Instead **scope
and cross-link**:

| Repo | Canonical home for |
|------|--------------------|
| **this repo** | Reusable image-analysis code, RSML traces, phenotype/image datasets, RootNav/PlantCV workflows |
| **CARA_GeneLab_AWG** | The CARA manuscript, GO/PPI networks, skewing-loci↔OSDR omics, figures |

Then, in **both** READMEs:
- add a "Related repositories" section linking the other,
- have both cite **OSD-120** and (eventually) each other's Zenodo DOI,
- move the *duplicated* CARA root-physiology analysis to ONE home (recommend
  keeping the runnable `RACARA_root_physio.ipynb` here, and having the CARA
  manuscript link to it rather than restating the ANOVA).

## Prioritized actions for `CARA_GeneLab_AWG`

1. **Quick FAIR wins:** add `CITATION.cff`, consolidate the two READMEs, record
   the OSD-120 accession, add a "Related repos" cross-link to this repo.
2. **De-bloat:** remove the 32 duplicate assets and the vendored `CyJS/` site
   (keep `.xgmml`/`.cys`); move `.pptx`/HTML to a Release.
3. **Document data:** `results/README.md` + `datapackage.json` for the GO/PPI/
   skewing/Metascape tables; rename pipe-char files.
4. **Publish:** Zenodo DOI on a tagged release (reuse this repo's `RELEASING.md`).
5. **Reconcile CARA physiology** with this repo's `RACARA_root_physio.ipynb`
   (single source of truth + cross-link).

> Most of the tooling already written here (`RELEASING.md`, `.zenodo.json`
> pattern, `datapackage.json` pattern, the no-binaries `.gitignore`) is directly
> reusable for `CARA_GeneLab_AWG`.
