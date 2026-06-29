#!/usr/bin/env bash
#
# restructure.sh — Tier 4 directory restructure for the FAIR overhaul.
# See REORGANIZATION_PLAN.md (§1–2) and PROJECT_TRACKER.md (Tier 4).
#
# WHAT IT DOES
#   * Creates the docs/ notebooks/ scripts/ data/ software/ tree
#   * Moves & renames every file into it (fixing typos, dropping "Copy of")
#   * Rewrites the Colab badge URLs inside the notebooks to their new paths
#   * Regenerates SUMMARY.md (GitBook table of contents) for the new layout
#
# HOW TO RUN (do this on a BRANCH of the real git repo, not the OneDrive ZIP):
#   git checkout -b restructure
#   bash restructure.sh
#   # review `git status`, build/preview the GitBook, then:
#   git commit -am "Tier 4: restructure into docs/notebooks/scripts/data/software"
#
# It is git-aware: if a .git dir exists it uses `git mv` (preserves history);
# otherwise it falls back to plain `mv` so you can also test on a plain copy.
#
# SAFETY: it's idempotent-ish — it skips a move if the source is already gone.
# Review the unverified items flagged "VERIFY (Q8)" before running.

set -euo pipefail
cd "$(dirname "$0")"

if [ -d .git ]; then MV() { git mv "$@"; }; else MV() { mv "$@"; }; fi

# Move helper: MOVE <src> <dst> — skips if src missing, makes parent dir.
MOVE() {
  local src="$1" dst="$2"
  if [ ! -e "$src" ]; then echo "  skip (gone): $src"; return 0; fi
  mkdir -p "$(dirname "$dst")"
  echo "  $src  ->  $dst"
  MV "$src" "$dst"
}

echo "==> Creating target directories"
mkdir -p docs notebooks/plantcv notebooks/cellpose notebooks/growth notebooks/cara \
         scripts/python scripts/r/rootnav-stats \
         data/rsml data/images/aquatic software
# NOTE: scripts/r/morphometrics is intentionally NOT pre-created — the whole
# Morphometric_R-codes folder is renamed into it below. Pre-creating it would
# make `mv` nest the folder inside instead of renaming it.

echo "==> Extract loose R scripts FIRST (before their parent folders move)"
MOVE "Brachypodium_root_tips"            "scripts/r/Brachypodium_root_tips.R"
MOVE "RootNav/RootNav_Natasha_codes"     "scripts/r/rootnav-stats/RootNav_Natasha_codes.R"

echo "==> Docs (GitBook chapters)"
MOVE "README (1).md"                                          "docs/introduction.md"
MOVE "README (1) (1).md"                                      "docs/plant-image-analysis.md"
MOVE "example-cara-root-modeling-example-reanalysis-paper.md" "docs/cara-reanalysis.md"
MOVE "rootnav-statisitics-from-evt-ksc-summer-2016.md"       "docs/rootnav-statistics-evt-ksc-2016.md"  # fix typo
MOVE "space-chilie.md"                                        "docs/space-chile.md"                       # fix typo
MOVE "astroroot-modelling-plan.md"                            "docs/astroroot-modelling-plan.md"
MOVE "rootnav2-and-astrodart-in-cyverse.md"                   "docs/rootnav2-and-astrodart-in-cyverse.md"
MOVE "wegas-analysis-codes.md"                                "docs/wegas-analysis-codes.md"
MOVE "spectrum-sticker.md"                                    "docs/spectrum-sticker.md"
MOVE "web-glyphics-app.md"                                    "docs/web-glyphics-app.md"
MOVE "streamlit-automated-analysis.md"                        "docs/streamlit-automated-analysis.md"
MOVE "streamlit-planet-neural-web-for-plant-detection-and-progress-tracking.md" "docs/streamlit-planet.md"
MOVE "leaf_outlines_with_dr-kribel.md"                        "docs/leaf_outlines_with_dr-kribel.md"
MOVE "morphometric_script_leaves_dr-kribel.r.md"             "docs/morphometric_script_leaves_dr-kribel.md"

echo "==> Notebooks"
MOVE "SpaceChile_phenotyping_v1.ipynb"        "notebooks/plantcv/SpaceChile_phenotyping_v1.ipynb"
MOVE "Plantcv_for_SPECTRUM_images.ipynb"      "notebooks/plantcv/Plantcv_for_SPECTRUM_images.ipynb"
MOVE "Spectrum_RFP_Basic_Analysis.ipynb"      "notebooks/plantcv/Spectrum_RFP_Basic_Analysis.ipynb"
MOVE "Copy of run_cellpose_2.0.ipynb"         "notebooks/cellpose/run_cellpose_2.0.ipynb"
MOVE "Copy of Cellpose_cell_segmentation_2D_prediction_only.ipynb" "notebooks/cellpose/Cellpose_cell_segmentation_2D_prediction_only.ipynb"
MOVE "An_Attempt_To_Gauge_Growth_v2.ipynb"    "notebooks/growth/An_Attempt_To_Gauge_Growth_v2.ipynb"
MOVE "Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb" "notebooks/growth/Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb"
MOVE "RACARA_root_physio.ipynb"               "notebooks/cara/RACARA_root_physio.ipynb"

echo "==> Scripts (Python + R)"
MOVE "Plant_gauge_growth.py"                      "scripts/python/Plant_gauge_growth.py"
MOVE "an_attempt_to_gauge_growth(streamlist_test).py" "scripts/python/gauge_growth_streamlit.py"
MOVE "Basics Statisic on RootNav"                 "scripts/r/rootnav-stats/_moved"  # see note below
# The line above moves the whole folder; flatten it:
if [ -d "scripts/r/rootnav-stats/_moved" ]; then
  for f in "scripts/r/rootnav-stats/_moved"/*; do MOVE "$f" "scripts/r/rootnav-stats/$(basename "$f")"; done
  rmdir "scripts/r/rootnav-stats/_moved" 2>/dev/null || true
fi
MOVE "Morphometric_R-codes"                       "scripts/r/morphometrics"

echo "==> Data"
MOVE "18_way_skew"                "data/rsml/18_way_skew"
MOVE "APEX03"                     "data/images/apex03"
MOVE "ABRS_NASA_Roots_TimeLapse"  "data/images/abrs_timelapse"
MOVE "Lemna"                      "data/images/aquatic/lemna"
MOVE "Azola"                      "data/images/aquatic/azolla"     # fix typo: Azola -> Azolla
MOVE "Wolfinia"                   "data/images/aquatic/wolffia"    # VERIFY (Q8): Wolffia?
MOVE "Londultia"                  "data/images/aquatic/landoltia"  # VERIFY (Q8): Landoltia?

echo "==> Software (binaries already .gitignored; folders keep PDFs/licenses/readmes)"
MOVE "RootNav"        "software/RootNav"
MOVE "RootTrace"      "software/RootTrace"
MOVE "RootTraceV2-1"  "software/RootTraceV2-1"
MOVE "Germinator"     "software/Germinator"

echo "==> Rewriting Colab badge URLs in notebooks to new paths"
# Each notebook's badge points at blob/master/<oldname>.ipynb; repoint to new path.
sedi() { if sed --version >/dev/null 2>&1; then sed -i "$@"; else sed -i '' "$@"; fi; }  # GNU vs BSD sed
sedi 's#blob/master/SpaceChile_phenotyping_v1.ipynb#blob/master/notebooks/plantcv/SpaceChile_phenotyping_v1.ipynb#g' notebooks/plantcv/SpaceChile_phenotyping_v1.ipynb
sedi 's#blob/master/Plantcv_for_SPECTRUM_images.ipynb#blob/master/notebooks/plantcv/Plantcv_for_SPECTRUM_images.ipynb#g' notebooks/plantcv/Plantcv_for_SPECTRUM_images.ipynb
sedi 's#blob/master/Spectrum_RFP_Basic_Analysis.ipynb#blob/master/notebooks/plantcv/Spectrum_RFP_Basic_Analysis.ipynb#g' notebooks/plantcv/Spectrum_RFP_Basic_Analysis.ipynb
sedi 's#blob/master/Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb#blob/master/notebooks/growth/Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb#g' notebooks/growth/Gauge_Growth_of_Arabidopsis_seedlings_in_petri_dish_timelapse.ipynb
# NOTE: this notebook's badge had a mismatched name (..._v2_streamlit_attempt.ipynb); repoint to the real file:
sedi 's#blob/master/An_Attempt_To_Gauge_Growth_v2_streamlit_attempt.ipynb#blob/master/notebooks/growth/An_Attempt_To_Gauge_Growth_v2.ipynb#g' notebooks/growth/An_Attempt_To_Gauge_Growth_v2.ipynb

echo "==> Regenerating SUMMARY.md (GitBook ToC) for the new layout"
cat > SUMMARY.md <<'EOF'
# Table of contents

* [Overview](README.md)
* [Project tracker](PROJECT_TRACKER.md)
* [Reorganization plan](REORGANIZATION_PLAN.md)

## Documentation

* [Introduction](docs/introduction.md)
* [Plant image analysis software and R codes](docs/plant-image-analysis.md)
* [Data dictionary](docs/DATA_DICTIONARY.md)
* [Example CARA root modeling re-analysis](docs/cara-reanalysis.md)
* [RootNav statistics (EVT @ KSC, summer 2016)](docs/rootnav-statistics-evt-ksc-2016.md)
* [weGAS analysis codes](docs/wegas-analysis-codes.md)
* [RootNav2 and AstroDart in CyVerse](docs/rootnav2-and-astrodart-in-cyverse.md)
* [AstroRoot modelling plan](docs/astroroot-modelling-plan.md)
* [Space Chile](docs/space-chile.md)
* [Morphometric script — leaves (Dr Kribel)](docs/morphometric_script_leaves_dr-kribel.md)
* [Leaf outlines with Dr Kribel](docs/leaf_outlines_with_dr-kribel.md)
* [StreamLit: PlaNet — plant detection & progress tracking](docs/streamlit-planet.md)
* [StreamLit: automated analysis](docs/streamlit-automated-analysis.md)
* [Web-glyphics app](docs/web-glyphics-app.md)
* [Spectrum sticker](docs/spectrum-sticker.md)

## Data

* [Datasets overview](data/README.md)

## Software

* [Tools, downloads & licenses](software/README.md)

## Code

* [RootNav statistics (R)](scripts/r/rootnav-stats/README.md)
* [Morphometrics (R)](scripts/r/morphometrics/README.md)
EOF

echo ""
echo "==> DONE. Next:"
echo "    1. Review:  git status   (and open the GitBook preview)"
echo "    2. Update relative links between moved .md files if any 404 (grep below)"
echo "    3. Commit on the branch."
echo ""
echo "Find any now-broken intra-doc links to fix by hand:"
echo "    grep -rngE '\\]\\((\\.\\./)?[A-Za-z0-9_-]+\\.md' docs/ README.md || true"
