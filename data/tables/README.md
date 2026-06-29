# Trait tables (CSV inputs for the R statistics)

This folder is the **expected home** for the measurement tables that the R
scripts in [`../../scripts/r/`](../../scripts/r/) read. The scripts were
updated to load their inputs from here via `here::here("data/tables/<file>")`
instead of hard-coded `~/Desktop` / `~/Downloads` / Dropbox paths, so the
analyses become reproducible once these files are added.

> ⚠️ **Status:** several of these CSVs are **not yet in the repository** — the
> original scripts read them from local machines. They need to be recovered and
> committed here (see [`../../PROJECT_TRACKER.md`](../../PROJECT_TRACKER.md),
> open question #6). The `RootTrace/*.csv` files elsewhere in the repo are empty
> stubs and are *not* these tables.

## Expected files

| File | Read by | Original location (pre-fix) | Status |
|------|---------|------------------------------|--------|
| `weGAS.csv` | `scripts/r/rootnav-stats/weGAS Analyses.R` | `~/Desktop/weGAS.csv` | ❓ missing |
| `Root measurements_KSC_SVT_processed.csv` | `scripts/r/rootnav-stats/NASA SVT statistical analysis.R` | `~/Desktop/...` | ❓ missing |
| `EVT_Root_measurements.csv` | `scripts/r/rootnav-stats/EVT_R-MarkDown_report.Rmd` | `~/Downloads/Google Drive/...` | ❓ missing |
| `c.csv` | `scripts/r/Brachypodium_root_tips.R` | `~/Desktop/c.csv` | ❓ missing (Brachypodium tip kinetics) |
| `groups.csv` | `scripts/r/morphometrics/*.R` | script working dir | ❓ missing (leaf group labels) |

## Known column semantics

The `weGAS` / RootNav-derived tables use the trait columns defined in
[`../../docs/DATA_DICTIONARY.md` §3](../../docs/DATA_DICTIONARY.md#3-derived-measurement-columns-csv):
`Emergence.Angle`, `Tip.Angle`, `Total.Length`, `Total.Primary.Angle`,
`Tortuosity` (plus grouping columns such as genotype / organ / treatment).

> When adding a real CSV here, also confirm its headers against the data
> dictionary and add/append the column definitions there.

## Note on `weGAS.csv`

`weGAS Analyses.R` currently splits the table by hard-coded row ranges
(rows 1–511 = Shoot, 512–1238 = Root). When the file is added, prefer adding an
explicit `organ` column and grouping on it, rather than relying on row order.
