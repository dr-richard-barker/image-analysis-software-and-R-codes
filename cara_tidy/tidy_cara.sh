#!/usr/bin/env bash
#
# tidy_cara.sh — conservative, FAIR clean-up for the CARA_GeneLab_AWG repo.
# See docs/CARA_REPO_ASSESSMENT.md (in the image-analysis repo) for the rationale.
#
# RUN IT INSIDE A CLONE OF CARA_GeneLab_AWG, on macOS/Linux (NOT Windows — the
# repo currently can't even be checked out on Windows; fixing that is Step 1):
#
#   git clone https://github.com/dr-richard-barker/CARA_GeneLab_AWG.git
#   cd CARA_GeneLab_AWG
#   git checkout -b tidy
#   bash /path/to/tidy_cara.sh           # review with: git status / git diff --stat
#   # then drop in CITATION.cff, .gitignore, results/README.md (see cara_tidy/)
#   git commit -am "Tidy: fix illegal filenames, remove byte-identical dup assets"
#
# It is CONSERVATIVE and SAFE:
#   * Step 1 renames the 3 pipe-`|` files (illegal on Windows) + fixes the
#     "tortosity"->"tortuosity" typo, repointing references.
#   * Step 2 removes ONLY dup-suffixed assets that are BYTE-IDENTICAL to a base
#     twin (hash-gated), repointing references first. The `image (N).png` series
#     are DISTINCT GitBook assets and are deliberately LEFT ALONE.
#   * Step 3 only *reports* the things needing human judgement (the 2nd README,
#     the vendored CyJS site, large binaries) — it does not delete them.

set -uo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)"
if [ ! -d .git ]; then echo "Run inside a git clone of CARA_GeneLab_AWG."; exit 1; fi
MV(){ git mv -k "$@" 2>/dev/null || mv "$@"; }

# Repoint references to a renamed/removed asset across md/html, handling raw,
# %20-encoded, and parenthesis-encoded spellings. Best-effort.
repoint(){
  local old="$1" new="$2"
  local old_e="${old// /%20}" new_e="${new// /%20}"
  grep -rIl --null -e "$old" -e "$old_e" -- . 2>/dev/null \
    | while IFS= read -r -d '' f; do
        [ "$f" = "./$old" ] && continue
        sed -i.bak -e "s#$(printf '%s' "$old" | sed 's/[#&]/\\&/g')#$new#g" \
                   -e "s#$(printf '%s' "$old_e" | sed 's/[#&]/\\&/g')#$new_e#g" "$f" 2>/dev/null \
          && rm -f "$f.bak"
      done
}

echo "==> Step 1: fix illegal pipe-char filenames (Windows-breaking) + 'tortosity' typo"
while IFS= read -r f; do
  [ -z "$f" ] && continue
  new="$(printf '%s' "$f" | sed 's/|/-/g; s/tortosity/tortuosity/g')"
  if [ "$f" != "$new" ]; then
    echo "   rename: $f  ->  $new"
    mkdir -p "$(dirname "$new")"
    MV "$f" "$new"
    repoint "$(basename "$f")" "$(basename "$new")"
  fi
done < <(git ls-files | grep -F '|')

echo "==> Step 2: remove byte-identical duplicate assets (hash-gated)"
removed=0; kept=0
while IFS= read -r dup; do
  [ -z "$dup" ] && continue
  base="$(printf '%s' "$dup" | sed -E 's/ \(([12])\)(\.[^.]+)$/\2/')"
  if [ "$dup" != "$base" ] && [ -f "$dup" ] && [ -f "$base" ] && cmp -s "$dup" "$base"; then
    echo "   dup (identical) -> remove: $dup"
    repoint "$(basename "$dup")" "$(basename "$base")"
    git rm -q "$dup" 2>/dev/null || rm -f "$dup"
    removed=$((removed+1))
  else
    kept=$((kept+1))   # distinct image (N).png etc. — leave it
  fi
done < <(git ls-files | grep -E ' \([12]\)\.[^.]+$')
echo "   removed $removed identical duplicates; left $kept distinct/uncertain files untouched"

echo ""
echo "==> Step 3: MANUAL items (not touched — review by hand):"
echo "   - Two READMEs: consolidate 'README (1).md' into 'README.md' (see cara_tidy/README_consolidated.md as a starting point)."
echo "   - Distinct GitBook assets 'image (N).png' / 'image (1) (1)...png' are NOT duplicates — keep, but consider renaming meaningfully."
echo "   - Vendored Cytoscape.js site 'results/CyJS/' (bower_components, vendor.js, fonts): keep the source .xgmml/.cys in results/Enrichment_*, and either"
echo "       git rm -r results/CyJS   # if the interactive export isn't needed in-repo"
echo "     or move it to a GitHub Release / GitHub Pages."
echo "   - Large binaries (results/AnalysisReport.pptx, *.html): consider a Release."
echo "   - Add drop-ins from cara_tidy/: CITATION.cff, .gitignore, results/README.md"
echo ""
echo "Done. Review:  git status   &&   git diff --stat"
