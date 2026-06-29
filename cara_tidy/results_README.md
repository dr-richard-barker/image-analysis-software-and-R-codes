# results/ — data dictionary (drop-in for CARA_GeneLab_AWG/results/README.md)

Documents the analysis outputs so the network/enrichment tables are reusable.
Fill in the bracketed TODOs with the exact tool versions / parameters.

## Enrichment_GO/ — Gene Ontology enrichment
| File | What it is |
|------|-----------|
| `GO_AllLists.csv` | GO terms enriched across all input gene lists |
| `GO_membership.csv`, `GO_membership_parent.csv` | gene→GO-term membership (term and parent level) |
| `GeneGo_membership.csv` | gene→GO mapping used for the network |
| `_FINAL_GO.csv` | final curated GO enrichment table |
| `GONetwork.xgmml` / `.cys` | the GO network (Cytoscape source) |

> TODO: source gene lists, background set, tool + version (Metascape? clusterProfiler?), p-value/FDR cutoff.

## Enrichment_PPI/ — protein–protein interaction / MCODE
| File | What it is |
|------|-----------|
| `MCODE_PPI.cys` | PPI network with MCODE clusters (Cytoscape) |
| `GO_MCODE.csv`, `GO_MCODE_Top3.csv` | GO terms per MCODE cluster (all / top 3) |
| `xgmml/*.xgmml` | network exports (renamed from illegal `|` filenames by tidy_cara.sh) |

> TODO: PPI source (STRING? BioGRID? version), MCODE parameters.

## Root-skewing intersections
| File | What it is |
|------|-----------|
| `Skewing_loci_12870_2017_975_*.csv` | skewing loci from BMC Plant Biol. 2017 (12870_2017_975), within/between WS tables |
| `skewing_OSDR_intersct_metascape*.xlsx` | intersection of skewing loci with OSDR spaceflight DEGs (Metascape) |
| `Evidence.csv`, `Evidence/Evidence.csv` | supporting evidence table (de-duplicate these two) |

> TODO: which OSD accession(s) the OSDR DEGs come from; Metascape run date/params.
> Define the key columns (locus ID, gene, p/FDR, direction, source study).

## Reports
| File | What it is |
|------|-----------|
| `AnalysisReport.html` | rendered analysis report |
| `AnalysisReport.pptx` | slide version (consider moving to a Release) |
| `metascape_result.xlsx` | raw Metascape output |
| `3d-root-single-cells-data.md` | single-cell root data notes |

## Provenance
- Link the **OSD accession(s)** (e.g. OSD-120) this analysis is based on.
- Cross-link the sibling image-analysis repo:
  https://github.com/dr-richard-barker/image-analysis-software-and-R-codes
