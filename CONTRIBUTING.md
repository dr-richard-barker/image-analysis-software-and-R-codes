# Contributing

Thanks for helping improve this astrobotany image-analysis collection. The repo
is being made more **FAIR** — see [`PROJECT_TRACKER.md`](PROJECT_TRACKER.md) for
the live plan and open questions.

## Ways to contribute

- **Add data** — new plant/root images or RSML traces (especially from NASA
  OSDR/GeneLab spaceflight studies). See "Adding a dataset" below.
- **Add/clean code** — notebooks, R scripts, analysis pipelines.
- **Documentation** — fill gaps in `docs/`, the data dictionary, or tool READMEs.
- **Answer an open question** — several blockers in the tracker (e.g. missing
  trait CSVs, species names) need someone with the original context.

## Ground rules

- **Licensing:** code contributions are under **MIT**, data/images under
  **CC-BY-4.0** (see `LICENSE`, `LICENSE-DATA.md`). Don't add third-party
  material whose license forbids this.
- **No binaries in git** — tools and large archives go to GitHub Releases or
  upstream links (see `software/README.md`). Large derived videos likewise.
- **Paths stay portable** — Python: resolve from repo root; R: use
  `here::here("data/...")`, never `~/Desktop` or drive-letter paths.
- **Cite provenance** — for any dataset, record where it came from (experiment,
  OSDR accession, instrument, date).

## Adding a dataset

1. Put images under `data/images/<dataset>/`, RSML under `data/rsml/<dataset>/`,
   trait tables under `data/tables/`.
2. Add a row/section to [`data/README.md`](data/README.md) and define any new
   columns in [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md).
3. For tabular/RSML datasets, add a `datapackage.json` mirroring
   `data/rsml/18_way_skew/datapackage.json`.
4. If it's NASA-derived, note the **OSDR accession** (e.g. `OSD-###`) and link it.

## Workflow

1. Branch from the default branch.
2. Make the change; keep notebooks' "Open in Colab" badge paths correct.
3. Open a pull request describing what and why. Reference any tracker item it
   advances.

## Questions

Open a GitHub issue, or add to the planning docs linked from the README.
