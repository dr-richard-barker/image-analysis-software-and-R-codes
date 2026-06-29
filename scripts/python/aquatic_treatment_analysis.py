#!/usr/bin/env python3
"""Plant size by treatment (calibrated) + growth curves for the aquatic plates.

The Lemna / Londultia / Azola / Wolfinia folders are 12-well plates of small
plants in a 4-treatment x 3-row layout. Label strip, left->right:
  column 1 = Water, 2 = GA, 3 = Nutrients, 4 = GA+Nutrient.

This script:
  1. detects the cm ruler in each photo (FFT of a bright horizontal band) ->
     px/mm, and converts green plant area to mm^2
  2. segments green plant tissue (LAB colourfulness, fast — no cellpose), assigns
     each plant to a treatment column by position
  3. reports mm^2 per treatment x species
  4. GROWTH CURVES: orders the images in each folder by IMG number (assumed time
     sequence) and plots total mm^2 per treatment over the sequence, with a
     linear growth-rate fit

⚠️ ASSUMPTIONS (please confirm): column order Water/GA/Nutrients/GA+Nutrient
left->right; plate upright; the 5 images/folder are an ordered TIME series
(IMG number = time). If they're independent plates instead, ignore the growth
curves and read the per-treatment means as descriptive.

Run:  python scripts/python/aquatic_treatment_analysis.py
Out:  results/aquatic_treatments/{per_well.csv, by_treatment_mm2.csv,
       growth_curves.csv, figure.png, growth_curves.png, montage.png}
"""
from __future__ import annotations
import os, glob, re
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab, rgb2gray, label2rgb
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


def ruler_px_per_mm(gray):
    """px-per-mm from the cm ruler: strongest periodic bright horizontal band."""
    h, w = gray.shape
    best = None
    for y0 in range(int(0.55 * h), int(0.92 * h), max(1, h // 40)):
        band = gray[y0:y0 + max(4, h // 60), :]
        prof = band.mean(axis=0)
        if prof.mean() < 0.4:           # ruler is bright/white
            continue
        p = prof - prof.mean()
        f = np.abs(np.fft.rfft(p * np.hanning(len(p))))
        fr = np.fft.rfftfreq(len(p))
        bm = (fr > 1 / 40) & (fr < 1 / 4)   # mm ticks ~4-40 px (full res)
        if not bm.any():
            continue
        fb = f.copy(); fb[~bm] = 0
        k = int(np.argmax(fb))
        if fb[k] <= 0:
            continue
        period = 1 / fr[k]; conf = fb[k] / (f[bm].mean() + 1e-9)
        if best is None or conf > best[1]:
            best = (period, conf)
    if best and best[1] >= 8:
        return best[0]                  # px per mm (1 mm ticks)
    return None


def green_plants(path):
    im = imread(path)
    full_w = im.shape[1]
    ppm_full = ruler_px_per_mm(rgb2gray(im))
    s = TARGET_W / full_w
    rgb = rescale(im, (s, s, 1), anti_aliasing=True, preserve_range=True).astype(np.uint8)
    lab = rgb2lab(rgb)
    a, L = lab[..., 1], lab[..., 0]
    green = (a < -8) & (L > 12)
    green = binary_opening(green, disk(1))
    green = binary_closing(green, disk(2))
    green = remove_small_objects(green, 60)
    green = ndi.binary_fill_holes(green)
    return label(green), rgb, ppm_full, s


def seq_num(fname):
    m = re.search(r'(\d+)', fname)
    return int(m.group(1)) if m else 0


def main():
    repo = find_repo_root()
    out = repo / 'results' / 'aquatic_treatments'; out.mkdir(parents=True, exist_ok=True)

    rows, previews, ppms = [], [], []
    for folder in FOLDERS:
        d = repo / folder
        if not d.exists():
            d = repo / 'data' / 'images' / 'aquatic' / folder.lower()
        if not d.exists():
            print(f"  (skip missing {folder})"); continue
        for f in sorted(glob.glob(str(d / '*.jpg')), key=lambda x: seq_num(os.path.basename(x))):
            lab, rgb, ppm_full, scale = green_plants(f)
            props = [p for p in regionprops(lab) if p.area >= 60]
            if not props:
                continue
            if ppm_full:
                ppms.append(ppm_full)
            xs = np.array([p.centroid[1] for p in props])
            x0, span = xs.min(), max(xs.max() - xs.min(), 1)
            for p in props:
                col = int(np.clip(4 * (p.centroid[1] - x0) / span, 0, 3.999))
                rows.append(dict(folder=folder, file=os.path.basename(f), seq=seq_num(os.path.basename(f)),
                                 treatment=TREATMENTS[col], area_px=p.area,
                                 ppm_full=ppm_full, scale=scale))
            if len(previews) < 6:
                previews.append((folder, os.path.basename(f), rgb, lab))
            print(f"  {folder:10} {os.path.basename(f):20} plants={len(props):2} ppm_full={ppm_full}")

    df = pd.DataFrame(rows)
    if df.empty:
        print("no plants segmented"); return

    # Calibrate: use the median full-res px/mm (constant rig) -> convert downscaled px to mm^2.
    ppm_full_med = float(np.median(ppms)) if ppms else None
    if ppm_full_med:
        # downscaled px/mm = full px/mm * scale; area_mm2 = area_px_ds / (ppm_ds)^2
        df['area_mm2'] = df.apply(lambda r: r.area_px / (ppm_full_med * r.scale) ** 2, axis=1).round(3)
        print(f"\nCalibration: median ruler = {ppm_full_med:.1f} px/mm (full res)")
    else:
        df['area_mm2'] = np.nan
        print("\nCalibration: ruler not detected -> mm^2 unavailable (px only)")
    df.to_csv(out / 'per_well.csv', index=False)

    metric = 'area_mm2' if ppm_full_med else 'area_px'
    unit = 'mm^2' if ppm_full_med else 'px'
    print(f"\n=== Mean plant area per treatment ({unit}, pooled) ===")
    print(df.groupby('treatment')[metric].agg(['mean', 'count']).reindex(TREATMENTS).round(3).to_string())
    bt = df.pivot_table(metric, 'folder', 'treatment', aggfunc='sum', fill_value=0).reindex(columns=TREATMENTS)
    bt.to_csv(out / 'by_treatment_mm2.csv')
    print(f"\n=== Total area per species x treatment ({unit}) ===")
    print(bt.round(1).to_string())

    # --- Growth curves: total area per (folder, treatment) over the image sequence ---
    seqmap = {folder: {s: i for i, s in enumerate(sorted(df[df.folder == folder].seq.unique()))}
              for folder in df.folder.unique()}
    df['t'] = df.apply(lambda r: seqmap[r.folder][r.seq], axis=1)
    gc = df.groupby(['folder', 'treatment', 't'])[metric].sum().reset_index()
    gc.to_csv(out / 'growth_curves.csv', index=False)
    print("\n=== Growth rate (linear slope of total area vs image-sequence index), pooled species ===")
    for tr in TREATMENTS:
        sub = gc[gc.treatment == tr]
        if sub.t.nunique() >= 2:
            slope = np.polyfit(sub.t, sub[metric], 1)[0]
            print(f"  {tr:12} slope = {slope:8.2f} {unit}/step  (n={len(sub)})")

    # figures
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
    bt.T.plot(kind='bar', ax=ax[0]); ax[0].set_ylabel(f'total green area ({unit})')
    ax[0].set_title('Plant area by treatment & species'); ax[0].set_xlabel('treatment')
    m = df.groupby('treatment')[metric].mean().reindex(TREATMENTS)
    ax[1].bar(TREATMENTS, m.values, color='seagreen'); ax[1].set_ylabel(f'mean plant area ({unit})')
    ax[1].set_title('Mean plant size by treatment (pooled)')
    plt.setp(ax[1].get_xticklabels(), rotation=20); plt.tight_layout(); plt.savefig(out / 'figure.png', dpi=120)

    fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
    pooled = gc.groupby(['treatment', 't'])[metric].mean().reset_index()
    for tr in TREATMENTS:
        s = pooled[pooled.treatment == tr]
        ax2.plot(s.t, s[metric], 'o-', label=tr)
    ax2.set_xlabel('image-sequence index (assumed time)'); ax2.set_ylabel(f'mean total area ({unit})')
    ax2.set_title('Growth curves by treatment (pooled species; time order assumed)'); ax2.legend()
    plt.tight_layout(); plt.savefig(out / 'growth_curves.png', dpi=120)

    n = len(previews)
    fig3, axes = plt.subplots(2, n, figsize=(2.5 * n, 5)); axes = np.atleast_2d(axes)
    for j, (folder, name, rgb, lab) in enumerate(previews):
        axes[0, j].imshow(rgb); axes[0, j].set_title(f"{folder[:6]} {name[:9]}", fontsize=7); axes[0, j].axis('off')
        axes[1, j].imshow(label2rgb(lab, image=rgb / 255.0, bg_label=0, alpha=0.5)); axes[1, j].axis('off')
    plt.tight_layout(); plt.savefig(out / 'montage.png', dpi=110)
    print(f"\nwrote per_well.csv, by_treatment_mm2.csv, growth_curves.csv, figure.png, growth_curves.png, montage.png")


if __name__ == '__main__':
    main()
