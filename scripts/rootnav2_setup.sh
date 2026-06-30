#!/usr/bin/env bash
#
# rootnav2_setup.sh — clone + patch + run RootNav 2.0 on a GPU for the
# Arabidopsis plate images (APEX-03 / skew). RootNav 2.0 is a 2019 codebase;
# it needs two small patches to run under PyTorch 2.6 + Pillow 12 (this repo's
# stack). Verified working on a GTX 1050 Ti (torch 2.6.0+cu124).
#
# Prereqs: a CUDA build of torch (see below) + the deps installed here.
#   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
#   pip install kdtree pyyaml
#
# Usage:
#   bash scripts/rootnav2_setup.sh /path/to/input_images /path/to/output

set -uo pipefail
IN="${1:?input dir}"; OUT="${2:-${IN}_output}"
WORK="$(mktemp -d)/RootNav-2.0"

echo "==> clone RootNav 2.0"
git clone --depth 1 https://github.com/robail-yasrab/RootNav-2.0.git "$WORK"
cd "$WORK/inference"

echo "==> patch 1: Pillow 12 removed PIL.Image.BICUBIC"
find . -name '*.py' -exec sed -i \
  's/from PIL.Image import BICUBIC/from PIL.Image import Resampling\nBICUBIC = Resampling.BICUBIC/; s/Image\.BICUBIC/Image.Resampling.BICUBIC/g' {} +

echo "==> patch 2: PyTorch 2.6 defaults torch.load(weights_only=True); old ckpt needs False"
sed -i 's/torch\.load(\([^)]*\))/torch.load(\1, weights_only=False)/g' models/model_loader.py

echo "==> available models"
python rootnav.py --list

echo "==> run (arabidopsis_plate model) on $IN"
python rootnav.py --model arabidopsis_plate "$IN" "$OUT"
echo "==> RSML + *_Color_output.png written to $OUT"

# Models: arabidopsis_plate | osr_bluepaper (rapeseed) | wheat_bluepaper
# NOTE: the arabidopsis_plate model is trained on few-plant plates; on the dense
# multi-seedling APEX-03 / ABRS plates the automatic trace is fragmented (see
# docs/ROOTNAV2_APEX_FINDINGS.md). For those, the model-free angle-dispersion
# approach (scripts/python/abrs_angle_analysis.py) is more robust.
