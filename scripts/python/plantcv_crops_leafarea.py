#!/usr/bin/env python3
"""PlantCV leaf-area pilot for OSD-670 crop images (lettuce / radish / pepper).

The OSD-670 morphometric photos are detached leaves laid on cm **graph paper** —
the canonical PlantCV leaf-area workflow. This pilot:

  1. PlantCV reads the image and extracts a colour channel (LAB) that separates
     leaf tissue from the white/blue-grid paper
  2. thresholds + cleans -> leaf mask; labels individual leaves
  3. measures per-leaf and per-image leaf area (px, and mm^2 via grid calibration)
  4. calibrates px -> mm from the graph-paper grid period (FFT; default 5 mm
     squares, override with --grid-mm)
  5. groups by crop species (from filename) and writes a table + montage

A first-pass segmentation — eyeball the montage and tune `--grid-mm` to your
paper. Leaf *counts* and *relative* areas are robust; absolute mm^2 depend on the
grid calibration being right.

Run:  python scripts/python/plantcv_crops_leafarea.py [--grid-mm 5]
Deps: plantcv, opencv, numpy, scipy, scikit-image, matplotlib, pandas
"""
from __future__ import annotations
import os, glob, re, argparse
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from plantcv import plantcv as pcv
from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects, binary_closing, disk
from scipy import ndimage as ndi


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / 'data' / 'images' / 'crops').exists():
            return c
    return p


def paper_mask(gray):
    """Largest bright region = the graph paper sheet."""
    from skimage.filters import threshold_otsu
    t = threshold_otsu(gray)
    fg = gray > t
    fg = ndi.binary_fill_holes(binary_closing(fg, disk(3)))
    lab = label(fg)
    if lab.max() == 0:
        return np.ones_like(gray, bool)
    big = 1 + np.argmax(np.bincount(lab.flat)[1:])
    return lab == big


def grid_period_px(channel, paper):
    """Estimate graph-paper grid spacing (px) via FFT of a paper-only profile."""
    ys, xs = np.where(paper)
    if ys.size == 0:
        return None
    r0, r1, c0, c1 = ys.min(), ys.max(), xs.min(), xs.max()
    strip = channel[(r0+r1)//2 - 5:(r0+r1)//2 + 5, c0:c1].mean(axis=0)
    strip = strip - strip.mean()
    f = np.abs(np.fft.rfft(strip * np.hanning(len(strip))))
    freqs = np.fft.rfftfreq(len(strip))
    band = (freqs > 1/80) & (freqs < 1/6)      # grid square 6..80 px
    if not band.any() or f[band].max() <= 0:
        return None
    fb = f.copy(); fb[~band] = 0
    return 1.0 / freqs[int(np.argmax(fb))]


def analyse(path, grid_mm):
    img, _, _ = pcv.readimage(filename=path)
    # LAB channels. Leaves are COLOURED (green/brown); white paper + light-blue grid
    # are near-neutral, so "colourfulness" = distance from the neutral point (128)
    # isolates leaf tissue and ignores the paper and grid.
    a = pcv.rgb2gray_lab(rgb_img=img, channel='a').astype(float)
    b = pcv.rgb2gray_lab(rgb_img=img, channel='b').astype(float)
    L = pcv.rgb2gray_lab(rgb_img=img, channel='l')
    paper = paper_mask(L.astype(float) / 255.0)

    from skimage.filters import threshold_otsu
    from skimage.morphology import binary_opening, binary_closing
    colourful = np.hypot(a - 128, b - 128)
    thr = max(threshold_otsu(colourful[paper]), 18)   # floor avoids grabbing faint grid
    leaf = (colourful > thr) & paper
    leaf = binary_opening(leaf, disk(2))              # break thin grid lines
    leaf = binary_closing(leaf, disk(4))             # merge fragments of the same leaf
    leaf = remove_small_objects(leaf, 400)
    leaf = ndi.binary_fill_holes(leaf)

    # drop paper-sized blobs (mis-segmentation) before instance segmentation
    paper_area = int(paper.sum())
    lab0 = label(leaf)
    leaf = np.isin(lab0, [p.label for p in regionprops(lab0)
                          if 200 <= p.area <= 0.08 * paper_area])

    # Watershed instance segmentation: split touching/adjacent leaves so the
    # count reflects real leaves, not connected-component fragments.
    from skimage.feature import peak_local_max
    from skimage.segmentation import watershed
    dist = ndi.distance_transform_edt(leaf)
    coords = peak_local_max(dist, min_distance=18, labels=leaf, exclude_border=False)
    seeds = np.zeros(dist.shape, dtype=bool)
    if len(coords):
        seeds[tuple(coords.T)] = True
    markers = label(seeds)
    inst = watershed(-dist, markers, mask=leaf)
    props = [p for p in regionprops(inst) if p.area >= 400]
    grid_px = grid_period_px(b.astype(float), paper)
    px_per_mm = (grid_px / grid_mm) if grid_px else None
    px2mm2 = (1.0 / px_per_mm ** 2) if px_per_mm else None

    total_px = int(sum(p.area for p in props))
    return dict(
        n_leaves=len(props),
        total_leaf_area_px=total_px,
        mean_leaf_area_px=round(total_px / len(props), 1) if props else 0,
        grid_px=round(grid_px, 2) if grid_px else None,
        px_per_mm=round(px_per_mm, 3) if px_per_mm else None,
        total_leaf_area_mm2=round(total_px * px2mm2, 2) if px2mm2 else None,
        mean_leaf_area_mm2=round(total_px / len(props) * px2mm2, 2) if (px2mm2 and props) else None,
    ), (img, leaf)


def species_of(fname):
    for s in ('Lettuce', 'Radish', 'Pepper'):
        if s.lower() in fname.lower():
            return s
    return 'unknown'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid-mm', type=float, default=5.0, help='graph-paper square size in mm')
    args = ap.parse_args()
    pcv.params.debug = None

    repo = find_repo_root()
    src = repo / 'data' / 'images' / 'crops'
    out = repo / 'results' / 'osd670_leafarea'; out.mkdir(parents=True, exist_ok=True)
    # only the per-crop leaf photos (skip block-overview 'sup' montages)
    files = [f for f in sorted(glob.glob(str(src / '*.jpg')))
             if species_of(os.path.basename(f)) != 'unknown']
    print(f"{len(files)} crop images; grid square = {args.grid_mm} mm")

    rows, previews = [], []
    for i, f in enumerate(files, 1):
        name = os.path.basename(f)
        traits, prev = analyse(f, args.grid_mm)
        traits.update(file=name, species=species_of(name))
        rows.append(traits)
        if len(previews) < 6:
            previews.append((name, prev))
        print(f"  [{i}/{len(files)}] {name:52} {traits['species']:8} "
              f"leaves={traits['n_leaves']:3} area={traits['total_leaf_area_mm2']} mm2 ppm={traits['px_per_mm']}")

    df = pd.DataFrame(rows)
    df.to_csv(out / 'summary.csv', index=False)
    print("\n=== Per-species (means) ===")
    print(df.groupby('species')[['n_leaves', 'total_leaf_area_px', 'mean_leaf_area_px']].mean().round(1).to_string())

    fig, axes = plt.subplots(2, len(previews), figsize=(3*len(previews), 6))
    for j, (name, (img, leaf)) in enumerate(previews):
        axes[0, j].imshow(img[..., ::-1] if img.ndim == 3 else img); axes[0, j].set_title(name[:18], fontsize=7); axes[0, j].axis('off')
        axes[1, j].imshow(leaf, cmap='Greens'); axes[1, j].axis('off')
    plt.tight_layout(); plt.savefig(out / 'montage.png', dpi=110)
    print('wrote', out / 'summary.csv', 'and', out / 'montage.png')


if __name__ == '__main__':
    main()
