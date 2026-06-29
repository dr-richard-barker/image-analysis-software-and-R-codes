# Releasing & minting a DOI (Tier 6)

How to publish a citable, archived release of this repository via Zenodo. Do
this on the **canonical GitHub repo** (the local OneDrive copy is not a git
clone).

## One-time setup

1. Sign in to **https://zenodo.org** with your GitHub account.
2. Go to **Zenodo → Settings → GitHub**, find
   `dr-richard-barker/image-analysis-software-and-R-codes`, and flip the toggle
   **On**. This tells Zenodo to archive every future GitHub release.
3. Confirm [`.zenodo.json`](.zenodo.json) and [`CITATION.cff`](CITATION.cff) are
   committed — Zenodo reads `.zenodo.json` for the deposit metadata.

## Pre-release checklist

- [ ] Tier 3 done: binaries removed from git / attached to a Release
      (see [`software/README.md`](software/README.md))
- [ ] Tier 4 done: `restructure.sh` run on a branch and merged; GitBook builds
- [ ] Verify upstream tool URLs in `software/README.md` (the ⚠️ *verify* items)
- [ ] `CITATION.cff` has authors + ORCIDs filled in (currently a TODO)
- [ ] Decide copyright holder/year in `LICENSE`
- [ ] README renders; Binder badge works; notebooks open in Colab
- [ ] `python -c "import json;json.load(open('.zenodo.json'))"` parses
- [ ] `CITATION.cff` validates (e.g. `cffconvert --validate`)

## Cut the release

```bash
# from the repo, on the default branch, fully pushed:
git tag -a v1.0.0 -m "First FAIR release: docs, licenses, RSML datapackage, pilots"
git push origin v1.0.0
gh release create v1.0.0 --title "v1.0.0 — FAIR release" --notes-file RELEASE_NOTES.md
# (optionally attach the third-party tool binaries as assets — see software/README.md)
```

Zenodo will detect the GitHub release and create an archived deposit with a DOI.

## After the DOI is minted

1. Copy the **concept DOI** (the version-independent one Zenodo shows).
2. Add it to:
   - [ ] [`CITATION.cff`](CITATION.cff) → uncomment and set `doi:` and `version:` / `date-released:`
   - [ ] [`.zenodo.json`](.zenodo.json) → optional, add to `related_identifiers`
   - [ ] [`README.md`](README.md) → add the DOI badge near the top:
         `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)`
3. Set GitHub **About → topics**: `astrobotany`, `rsml`, `plant-phenotyping`,
   `root-architecture`, `plantcv`, `spaceflight`.

## Versioning

Use semantic-ish tags: `v1.0.0`, `v1.1.0` (new data/notebooks), `v1.0.1`
(doc fixes). Each GitHub release → a new Zenodo version under the same concept
DOI, so "cite the latest" and "cite this exact version" both work.

## OSDR / GeneLab note

If you deposit the derived datasets (RSML, trait CSVs) into NASA OSDR, link the
OSDR accession and the Zenodo DOI to each other via `related_identifiers` so the
data and the analysis code stay discoverable together.
