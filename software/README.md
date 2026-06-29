# Software (root & seed phenotyping tools)

This repository historically bundled the **Windows binaries** for several
third-party phenotyping tools (~120 MB of `.exe`, `.dll`, `.msi`, `.zip`).
Committing binaries into git bloats every clone, can't be diffed, mixes
third-party licenses into the repo, and excludes non-Windows users.

**Policy:** these tools are **not redistributed in version control**. Download
them from the official upstream source (links below), or grab the archived
copies attached to this repository's **GitHub Releases**. Each tool keeps its
own license — see the per-tool notes.

> See [`../REORGANIZATION_PLAN.md`](../REORGANIZATION_PLAN.md) §3 and the
> "Maintainers" section at the bottom of this file for how the binaries were
> removed from git and how to attach them to a Release.

---

## RootNav (v1)

- **What it does:** semi-automatic tracing of root system architecture from
  plate images; a human seeds start/end points and RootNav fits primary and
  lateral roots, exporting the open **RSML** format. The bundled build includes
  an extra `RootNav.Measurement.dll` enabling **root-skew** measurement — this
  is the tool used to produce the `18_way_skew/` RSML traces in this repo.
- **Reference:** Pound et al. (2013), *RootNav: Navigating Images of Complex
  Root Architectures*, **Plant Physiology** 162(4):1802–1814.
  (PDF previously bundled: `RootNav/Plant Physiol.-2013-Pound-1802-14.pdf`.)
- **Upstream / download:** University of Nottingham CVL / CPIB.
  ⚠️ *Verify current URL before publishing* — historically distributed via the
  Nottingham CVL software page and SourceForge.
- **License:** see the bundled `RootNav/license.txt` (retained with the binary).
- **Bundled dependencies:** `mysql.data.dll`, `RootNav.Data.dll`,
  `RootNav.Viewer.exe` — keep their own upstream licenses.
- **Files removed from git:** `RootNav.exe`, `RootNav.Viewer.exe`,
  `RootNav.Data.dll`, `mysql.data.dll`, `RootNav.Measurement.dll`,
  `Oringal RootNav measurements dll file/RootNav.Measurement.dll`.

## RootNav 2.0

- **What it does:** deep-learning successor to RootNav. Fully **automatic**
  segmentation of primary and lateral roots, also exporting RSML. Best on
  images with few, well-separated plants on a clean background.
- **Reference:** Yasrab et al. (2019), *RootNav 2.0: Deep learning for
  automatic navigation of complex plant root architectures*, **GigaScience**
  8(11):giz123.
- **Upstream / download (open source, Python):**
  https://github.com/robail-yasrab/RootNav-2.0
- **License:** as stated in the upstream repository (verify before
  redistribution).
- **Note:** not previously bundled here — listed because it is the natural tool
  for the planned re-analysis of the `ABRS_NASA_Roots_TimeLapse` images
  (see the FAIR tracker, "New analysis" task). See the feasibility caveats
  there: ABRS plates are dense, overlapping, multi-seedling and may need
  RootNav v1 semi-automatic tracing or fine-tuning instead.

## RootTrace

- **What it does:** high-throughput, automated quantification of root **growth
  rate** and tip position from time-lapse plate images (good fit for the ABRS
  time-lapse series).
- **Reference:** French et al. (2009), *High-Throughput Quantification of Root
  Growth Using a Novel Image-Analysis Tool*, **Plant Physiology**
  150(4):1784–1795. (PDF previously bundled:
  `RootTrace/Plant Physiol.-2009-French-1784-95.pdf`.)
- **Upstream / download:** University of Nottingham / SGT.
  ⚠️ *Verify current URL before publishing.*
- **License:** see bundled `RootTrace/licence.rtf` and
  `RootTrace/MathNet.Iridium.License.txt`.
- **Bundled dependencies:** OpenCV 1.0 runtime (`cv100.dll`, `cvaux100.dll`,
  `cvcam100.dll`, `cxcore100.dll`, `cxts001.dll`, `highgui100.dll`,
  `ml100.dll`), `libguide40.dll`, `MathNet.Iridium.dll` — each retains its own
  upstream license.
- **Files removed from git:** `RootTrace.exe`, all the `.dll`s above,
  `rthelp.chm`, and the `.lnk` shortcuts.

## RootTrace V2

- **What it does:** updated RootTrace; distributed as a Windows installer.
- **Upstream / download:** see `RootTraceV2-1/Readme_v2.pdf` (retained) for the
  authors' instructions. ⚠️ *Verify current URL.*
- **Files removed from git:** `RootTraceV2-1/RootTraceV2.msi`.

## Germinator

- **What it does:** high-throughput scoring and curve-fitting of seed
  germination from imaging plates.
- **Reference:** Joosen et al. (2010), *GERMINATOR: a software package for
  high-throughput scoring and curve fitting of Arabidopsis seed germination*,
  **The Plant Journal** 62(1):148–159. (PDF previously bundled:
  `Germinator/Joosen_et_al-2010-The_Plant_Journal(Germinator).pdf`.)
- **Upstream / download:** Wageningen UR.
  ⚠️ *Verify current URL before publishing.*
- **License:** as distributed by the authors (inside `GERMINATOR.zip`).
- **Files removed from git:** `Germinator/GERMINATOR.zip` (~79 MB — the single
  largest file in the repository).

---

## Reference PDFs (keep in repo)

The bundled journal PDFs are small and document the methods, so they **stay**
under each tool's folder (or move to `docs/references/`). They are the citable
record of how each tool works.

---

## Maintainers — how the binaries were removed from git

> The local working copy is a downloaded ZIP, not a git clone, so these steps
> are run against the **canonical GitHub repository**, not this folder. The
> binary files are kept on disk here as a convenience copy — they are simply no
> longer tracked by git.

**1. Stop tracking the binaries (keeps them on disk):**

```bash
git rm --cached -r \
  "RootNav/RootNav.exe" "RootNav/RootNav.Viewer.exe" "RootNav/RootNav.Data.dll" \
  "RootNav/mysql.data.dll" "RootNav/RootNav.Measurement.dll" \
  "RootNav/Oringal RootNav measurements dll file/RootNav.Measurement.dll" \
  "RootTrace/"*.dll "RootTrace/RootTrace.exe" "RootTrace/rthelp.chm" "RootTrace/"*.lnk \
  "RootTraceV2-1/RootTraceV2.msi" \
  "Germinator/GERMINATOR.zip" \
  "ABRS_NASA_Roots_TimeLapse/ABRS_Flight/"*.avi \
  "ABRS_NASA_Roots_TimeLapse/ABRS_Ground_control/"*.avi
git commit -m "Remove bundled binaries from version control (see software/README.md)"
```

**2. Prevent re-committing** — see the repo-root [`.gitignore`](../.gitignore).

**3. Attach the binaries to a GitHub Release** so users can still get them:

```bash
gh release create tools-v1 \
  "Germinator/GERMINATOR.zip" "RootTraceV2-1/RootTraceV2.msi" \
  --title "Bundled phenotyping tools" \
  --notes "Third-party Windows binaries (RootNav, RootTrace, Germinator). Each retains its own license — see software/README.md."
```

**4. (Optional) Purge them from git history** to actually shrink the repo —
removing from HEAD does not reclaim space already in history. Use
[`git filter-repo`](https://github.com/newren/git-filter-repo) or
[BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/), then
force-push. ⚠️ This rewrites history — coordinate with collaborators first.

**5. (Alternative to removal) Git LFS** — if a binary genuinely must stay
in-tree, track it with LFS instead; see the repo-root [`.gitattributes`](../.gitattributes).
