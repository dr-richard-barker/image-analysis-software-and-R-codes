# NASA OSDR — plant morphometric imaging (mirror)

Curated, web-compressed plant imaging from the [NASA Open Science Data
Repository](https://osdr.nasa.gov/) (OSDR/GeneLab), for the [AstroBotany
calibration image database](https://dr-richard-barker.github.io/AstroBotany_calibration_image_sharing_and_analysis/).
Discovered with [`tools/osdr_scan.py`](https://github.com/dr-richard-barker/AstroBotany_calibration_image_sharing_and_analysis/blob/main/tools/osdr_scan.py)
(the OSDR API is CORS-restricted, so images are mirrored here rather than
fetched live).

| Folder | OSDR study | Content | Images |
|---|---|---|---|
| `OSD-120/` | [OSD-120](https://osdr.nasa.gov/bio/repo/data/studies/OSD-120) | *Arabidopsis thaliana* root morphometric photography — 3 genotypes (Ws, Col-0, Col-0 phyD) × Flight/Ground × days 3–13 × light/dark | 48 |
| `OSD-121/` | [OSD-121](https://osdr.nasa.gov/bio/repo/data/studies/OSD-121) | BRIC-16 *Arabidopsis* morphometric photography (Flight vs Ground) | 26 |
| `OSD-476/` | [OSD-476](https://osdr.nasa.gov/bio/repo/data/studies/OSD-476) | Arabidopsis grown in Apollo lunar regolith — plate/shoot scans | 20 |

Each folder has `images/` (JPEG, ≤1600–2000 px; originals are 2–75 MB each and were
not mirrored) and `images/metadata.csv` (species, genotype, tissue, condition,
light, day, and the original OSDR filename in `osdr_source`). OSD-476 originals
are large TIFFs, converted to JPEG for browser viewing.

Data courtesy of NASA OSDR / GeneLab and the original investigators; see each
study page for citation and licensing.
