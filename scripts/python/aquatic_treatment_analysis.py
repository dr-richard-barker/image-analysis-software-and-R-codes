#!/usr/bin/env python3
"""Plant size by treatment for the aquatic well-plate experiment.

The Lemna / Londultia / Azola / Wolfinia folders are 12-well plates of small
plants in a 4-treatment x 3-row layout. The label strip reads, left->right:
  column 1 = Water, 2 = GA, 3 = Nutrients, 4 = GA+Nutrient.

This measures GREEN PLANT AREA per well (fast LAB-colourfulness segmentation —
no slow cellpose), assigns each plant to a treatment column by position, and
compares plant size across treatments and species.

⚠️ ASSUMPTIONS (please confirm):
  * column order left->right is Water / GA / Nutrients / GA+Nutrient
  * plate is roughly axis-aligned and upright (label strip at the bottom)
  * the 5 images per folder are independent samples (if they are time-lapse of
    one plate, treat per-treatment means as descriptive, not replicated)

Run:  python scripts/python/aquatic_treatment_analysis.py
Out:  results/aquatic_treatments/{per_well.csv, figure.png}
Deps: numpy, scikit-image, matplotlib, pandas
"""
from __future__ import annotations
import os, glob
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab
from skimage.filters import threshold_otsu, gaussian
from skimage.morphology import remove_small_objects, binary_opening, binary_closing, disk
from skimage.measure import label, regionprops
from scipy import ndimage as ndi

TREATMENTS = ['Water', 'GA', 'Nutrients', 'GA+Nutrient']
FOLDERS = ['Lemna', 'Londultia', 'Azola', 'Wolfinia']
TARGET_W = 700


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / 'Lemna').exists():
            return c
    return p


def green_plants(path):
    """Segment green plant tissue; return labelled plants + the small RGB image."""
    im = imread(path)
    s = TARGET_W / im.shape[1]
    rgb = rescale(im, (s, s, 1), anti_aliasing=True, preserve_range=True).astype(np.uint8)
    lab = rgb2lab(rgb)
    a, b, L = lab[..., 1], lab[..., 2], lab[..., 0]
    # green plant tissue: negative a* (green), not too dark (exclude black gaps)
    green = (a < -8) & (L > 12)
    green = binary_opening(green, disk(1))
    green = binary_closing(green, disk(2))
    green = remove_small_objects(green, 60)
    green = ndi.binary_fill_holes(green)
    return label(green), rgb


def main():
    repo = find_repo_root()
    out = repo / 'results' / 'aquatic_treatments'; out.mkdir(parents=True, exist_ok=True)

    rows, previews = [], []
    for folder in FOLDERS:
        d = repo / folder
        if not d.exists():
            d = repo / 'data' / 'images' / 'aquatic' / folder.lower()
        if not d.exists():
            print(f"  (skip missing {folder})"); continue
        for f in sorted(glob.glob(str(d / '*.jpg'))):
            lab, rgb = green_plants(f)
            props = [p for p in regionprops(lab) if p.area >= 60]
            if not props:
                continue
            xs = np.array([p.centroid[1] for p in props])
            x0, x1 = xs.min(), xs.max()
            span = max(x1 - x0, 1)
            for p in props:
                cx = p.centroid[1]
                col = int(np.clip(4 * (cx - x0) / span, 0, 3.999))   # 0..3 -> column
                rows.append(dict(folder=folder, file=os.path.basename(f),
                                 treatment=TREATMENTS[col], area_px=p.area,
                                 cx=round(cx, 1), cy=round(p.centroid[0], 1)))
            if len(previews) < 6:
                previews.append((folder, os.path.basename(f), rgb, lab))
            print(f"  {folder:10} {os.path.basename(f):20} plants={len(props)}")

    df = pd.DataFrame(rows)
    df.to_csv(out / 'per_well.csv', index=False)
    if df.empty:
        print("no plants segmented"); return

    print("\n=== Total green plant area per treatment (px, summed across images) ===")
    piv = df.pivot_table('area_px', 'folder', 'treatment', aggfunc='sum', fill_value=0)
    piv = piv.reindex(columns=TREATMENTS)
    print(piv.round(0).to_string())
    print("\n=== Mean plant area per treatment (all species pooled) ===")
    print(df.groupby('treatment')['area_px'].agg(['mean', 'count']).reindex(TREATMENTS).round(1).to_string())

    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
    piv.T.plot(kind='bar', ax=ax[0]); ax[0].set_ylabel('total green area (px)')
    ax[0].set_title('Plant area by treatment & species'); ax[0].set_xlabel('treatment')
    order = df.groupby('treatment')['area_px'].mean().reindex(TREATMENTS)
    ax[1].bar(TREATMENTS, order.values, color='seagreen'); ax[1].set_ylabel('mean plant area (px)')
    ax[1].set_title('Mean plant size by treatment (pooled)')
    plt.setp(ax[1].get_xticklabels(), rotation=20); plt.tight_layout()
    plt.savefig(out / 'figure.png', dpi=120)

    n = len(previews)
    fig2, axes = plt.subplots(2, n, figsize=(2.5*n, 5)); axes = np.atleast_2d(axes)
    from skimage.color import label2rgb
    for j, (folder, name, rgb, lab) in enumerate(previews):
        axes[0, j].imshow(rgb); axes[0, j].set_title(f"{folder[:6]} {name[:10]}", fontsize=7); axes[0, j].axis('off')
        axes[1, j].imshow(label2rgb(lab, image=rgb/255.0, bg_label=0, alpha=0.5)); axes[1, j].axis('off')
    plt.tight_layout(); plt.savefig(out / 'montage.png', dpi=110)
    print(f"\nwrote {out/'per_well.csv'}, figure.png, montage.png")


if __name__ == '__main__':
    main()
