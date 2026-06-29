# cara_tidy/ — ready-to-apply clean-up for `CARA_GeneLab_AWG`

Staging folder of files + a script to start making the **sibling**
`CARA_GeneLab_AWG` repo FAIR and tidy. Full rationale:
[`../docs/CARA_REPO_ASSESSMENT.md`](../docs/CARA_REPO_ASSESSMENT.md).

> These apply to the **other** repo, not this one. Run them inside a clone of
> `CARA_GeneLab_AWG` on **macOS/Linux**.

## ⚠️ Headline finding

`CARA_GeneLab_AWG` **cannot be checked out on Windows.** Three files contain a
`|` character (illegal in Windows filenames):
- `results/Enrichment_PPI/tortosity|5 OSDR|3 OSDR_PPIColorByCluster.pdf`
- `results/Enrichment_PPI/tortosity|5 OSDR|3 OSDR_PPIColorByCluster.png`
- `results/Enrichment_PPI/xgmml/tortosity|5 OSDR|3 OSDR.xgmml`

`git clone` on Windows produces **zero working files**. Fixing this (Step 1 of
the script) is the single most important change. (Bonus: `tortosity` is a typo
for `tortuosity`.)

## What's here

| File | Apply as | Purpose |
|------|----------|---------|
| `tidy_cara.sh` | run in the CARA clone | renames the 3 pipe files; removes only **byte-identical** duplicate assets; reports manual items |
| `CITATION.cff` | copy to repo root | citation metadata (add ORCIDs, OSD accession, DOI) |
| `gitignore` | copy to repo root as `.gitignore` | keep vendored web app + big binaries out of git |
| `results_README.md` | copy to `results/README.md` | data dictionary for the GO/PPI/skewing tables |
| `README_consolidated.md` | starting point to merge the two READMEs | one clear landing page |

## Safety notes (why it's conservative)

- Of the 32 `(1)/(2)`-suffixed assets, **only 15 are true byte-identical
  duplicates** (the gene-structure `AT…(1).jpg`). The other 17 — the
  `image (N).png` series and `README (1).md` — are **distinct content**. The
  script removes ONLY the hash-identical ones and leaves the rest. *Do not* bulk-
  delete `(1)` files by name.
- The vendored `results/CyJS/` Cytoscape.js site (incl. a 715 KB `vendor.js`) is
  **not** auto-removed — the script only flags it, because it may be a linked
  interactive figure. The network *source* (`.xgmml`/`.cys`) lives in
  `results/Enrichment_*` and is kept regardless.

## Steps

```bash
git clone https://github.com/dr-richard-barker/CARA_GeneLab_AWG.git
cd CARA_GeneLab_AWG
git checkout -b tidy
bash /path/to/cara_tidy/tidy_cara.sh
cp /path/to/cara_tidy/CITATION.cff .
cp /path/to/cara_tidy/gitignore .gitignore
cp /path/to/cara_tidy/results_README.md results/README.md
# review, then:
git add -A && git commit -m "Tidy: fix illegal filenames, dedupe assets, add FAIR metadata"
```

Then follow the FAIR steps from this repo's [`RELEASING.md`](../RELEASING.md) to
add a Zenodo DOI, and cross-link the two repos in both READMEs (record OSD-120).

## Not automated (deliberate — needs your judgement)

- Merge `README (1).md` into `README.md` (see `README_consolidated.md`).
- Decide CyJS site: remove (keep source networks) or move to a Release / Pages.
- Reconcile the duplicated CARA root-physiology with this repo's
  `RACARA_root_physio.ipynb` (single source of truth + cross-link).
- Add a `datapackage.json` for the results tables (mirror this repo's pattern).
