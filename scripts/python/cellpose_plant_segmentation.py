#!/usr/bin/env python3
"""Cellpose plant segmentation for the well-plate images (Lemna / Londultia).

Adapts the repo's Cellpose *cell* notebooks to segment whole **plants**: the
Lemna/ and Londultia/ folders are 12-well plates of small green plants
(Water / GA / Nutrients / GA+Nutrient treatments) photographed with a ruler.
Cellpose's generalist model treats each plant as an "object", giving per-plant
area and per-image plant counts.

What it adds over the original notebooks:
  * works on macro RGB plate photos (not microscopy), using the green channel
  * segments plants, filters out well-rim / noise blobs by size
  * batches whole folders, writes a per-image summary + an overlay montage
  * version-robust: works with Cellpose 3.x (`models.Cellpose`) and
    4.x / cellpose-SAM (`models.CellposeModel`)

Run:  python scripts/python/cellpose_plant_segmentation.py [--diameter 0] [--folders Lemna Londultia]
Deps: cellpose, torch, numpy, scikit-image, matplotlib, pandas
GPU:  uses GPU if a CUDA build of torch is present; otherwise CPU (fine for ~5 imgs).
"""
from __future__ import annotations
import os, glob, argparse
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from skimage.io import imread
from skimage.transform import rescale
from skimage.measure import regionprops
from skimage.color import label2rgb

TARGET_W = 512   # downscale wide plate photos for speed (cellpose-SAM is heavy on CPU)


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / 'Lemna').exists() or (c / 'data' / 'images' / 'aquatic').exists():
            return c
    return p


def make_model():
    import torch
    from cellpose import models
    gpu = bool(getattr(torch, 'cuda', None) and torch.cuda.is_available())
    # Prefer the fast CNN model (cellpose 3.x `Cellpose`/cyto3) — the v4 `CellposeModel`
    # (cellpose-SAM ViT) is accurate but ~24 min/image on CPU here, impractical.
    if hasattr(models, 'Cellpose'):
        return ('v3', models.Cellpose(gpu=gpu, model_type='cyto3'), gpu)
    if hasattr(models, 'CellposeModel'):
        return ('v4', models.CellposeModel(gpu=gpu), gpu)
    raise RuntimeError('Unsupported cellpose version (no Cellpose/CellposeModel).')


def segment(model_api, model, img_rgb, diameter):
    api = model_api
    d = None if not diameter else diameter
    if api == 'v4':
        # cellpose-SAM: channel-agnostic, takes RGB directly
        out = model.eval(img_rgb, diameter=d)
    else:
        # 3.x: green channel as cytoplasm (channels=[cyto, nucleus]; 2 = green)
        out = model.eval(img_rgb, diameter=d, channels=[2, 0])
    masks = out[0]
    return masks


def analyse_folder(folder, model_api, model, diameter, limit=0):
    rows, previews = [], []
    files = sorted(glob.glob(str(folder / '*.jpg')))
    if limit:
        files = files[:limit]
    for f in files:
        im = imread(f)
        scale = TARGET_W / im.shape[1]
        small = rescale(im, (scale, scale, 1), anti_aliasing=True, preserve_range=True).astype(np.uint8)
        masks = segment(model_api, model, small, diameter)
        # size-filter: drop specks and huge (well-rim / background) blobs
        area_img = small.shape[0] * small.shape[1]
        props = [p for p in regionprops(masks) if 0.0008 * area_img <= p.area <= 0.15 * area_img]
        keep = np.isin(masks, [p.label for p in props])
        masks_f = masks * keep
        areas = [p.area for p in props]
        rows.append(dict(file=os.path.basename(f), folder=folder.name,
                         n_plants=len(props),
                         total_plant_area_px=int(sum(areas)),
                         mean_plant_area_px=int(np.mean(areas)) if areas else 0))
        previews.append((os.path.basename(f), small, masks_f))
        print(f"  {folder.name:10} {os.path.basename(f):22} plants={len(props):2} "
              f"total_area={int(sum(areas)):7}")
    return rows, previews


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--folders', nargs='+', default=['Lemna', 'Londultia'])
    ap.add_argument('--diameter', type=float, default=0, help='plant diameter px (0 = auto-estimate)')
    ap.add_argument('--limit', type=int, default=0, help='process only first N images per folder (0 = all)')
    ap.add_argument('--target-w', type=int, default=TARGET_W, help='downscale width (smaller = faster on CPU)')
    args = ap.parse_args()
    globals()['TARGET_W'] = args.target_w   # override module default for analyse()

    repo = find_repo_root()
    out = repo / 'results' / 'cellpose_plants'; out.mkdir(parents=True, exist_ok=True)
    api, model, gpu = make_model()
    print(f"cellpose API {api}, GPU={gpu}")

    all_rows, all_prev = [], []
    for name in args.folders:
        folder = repo / name
        if not folder.exists():
            folder = repo / 'data' / 'images' / 'aquatic' / name.lower()
        if not folder.exists():
            print(f"  (skip missing folder {name})"); continue
        r, p = analyse_folder(folder, api, model, args.diameter, args.limit)
        all_rows += r; all_prev += p

    df = pd.DataFrame(all_rows)
    df.to_csv(out / 'summary.csv', index=False)
    print("\n=== Per-folder means ===")
    print(df.groupby('folder')[['n_plants', 'total_plant_area_px', 'mean_plant_area_px']].mean().round(1).to_string())

    n = min(len(all_prev), 8)
    fig, axes = plt.subplots(2, n, figsize=(2.6 * n, 5.4))
    axes = np.atleast_2d(axes)
    for j in range(n):
        name, small, masks_f = all_prev[j]
        axes[0, j].imshow(small); axes[0, j].set_title(name[:14], fontsize=7); axes[0, j].axis('off')
        axes[1, j].imshow(label2rgb(masks_f, image=small/255.0, bg_label=0, alpha=0.45)); axes[1, j].axis('off')
    plt.tight_layout(); plt.savefig(out / 'montage.png', dpi=110)
    print(f"\nwrote {out/'summary.csv'} and {out/'montage.png'}")


if __name__ == '__main__':
    main()
