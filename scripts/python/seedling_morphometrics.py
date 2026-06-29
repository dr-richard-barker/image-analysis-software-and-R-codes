#!/usr/bin/env python3
"""Seedling/root morphometrics for the OSD-121 dish photographs — calibrated.

These OSDR images are petri dishes of Arabidopsis seedlings shot against a
ruler (flight `_F_` vs ground `_G_`). Pipeline:

  1. detect the petri dish (Hough circle); CROP to it and mask outside the rim
     -> removes the ruler + background from the measurement region
  2. calibrate px -> mm two ways:
       (a) ruler ticks (FFT of the right-edge intensity profile), and
       (b) dish diameter (assumes --dish-mm, default 90 mm)
     and pick the ruler estimate when it looks reliable, else the dish.
  3. enhance thin seedling structures (Sato ridge filter), threshold, skeletonize
  4. per dish: plant area (mm^2), skeleton length (mm), components, vertical
     extent (mm), and root-angle dispersion (deg, scale-free)
  5. aggregate flight vs ground; write table, montage, groups.csv

Still a first pass on hard (translucent-seedling-on-agar) images — eyeball the
montage. Angle dispersion and flight-vs-ground contrasts are the robust readouts;
absolute mm^2 depend on the calibration being right (check `px_per_mm` + `calib`).

Run:  python scripts/python/seedling_morphometrics.py [--dish-mm 90]
Deps: numpy scipy scikit-image matplotlib pandas
"""
from __future__ import annotations
import os, glob, re, argparse
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from skimage.io import imread
from skimage.transform import rescale, hough_circle, hough_circle_peaks
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.filters import sato, threshold_otsu, sobel_h, sobel_v, gaussian
from skimage.morphology import skeletonize, remove_small_objects
from skimage.measure import label
from scipy import ndimage as ndi

RIDGE_SIGMAS = (1, 2, 3)
THRESH_K     = 1.0
TARGET_W     = 1000
MIN_OBJ      = 60
DEFAULT_DISH_MM = 90.0     # standard small petri dish; override with --dish-mm


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / 'data' / 'images' / 'leaves').exists():
            return c
    return p


def detect_dish(gray):
    """Return (cy, cx, r) of the petri dish from the largest bright blob (fast).

    The dish (bright agar) is the biggest bright region; its centroid + equivalent
    radius give a robust circle without the cost of a Hough transform.
    """
    from skimage.filters import threshold_otsu
    from skimage.measure import regionprops
    t = threshold_otsu(gray)
    fg = ndi.binary_fill_holes(gray > t)
    lab = label(fg)
    if lab.max() == 0:
        return None
    big = 1 + int(np.argmax(np.bincount(lab.flat)[1:]))
    p = regionprops((lab == big).astype(int))[0]
    cy, cx = p.centroid
    # radius from area (equivalent circle) and from bbox, averaged for robustness
    r_area = np.sqrt(p.area / np.pi)
    minr, minc, maxr, maxc = p.bbox
    r_bbox = 0.25 * ((maxr - minr) + (maxc - minc))
    r = 0.5 * (r_area + r_bbox)
    if r < 0.25 * gray.shape[1]:      # not a plausible full-frame dish
        return None
    return float(cy), float(cx), float(r)


def circular_mask(shape, cy, cx, r, shrink=0.96):
    yy, xx = np.ogrid[:shape[0], :shape[1]]
    return (yy - cy) ** 2 + (xx - cx) ** 2 <= (r * shrink) ** 2


def ruler_scale(gray, dish_cx):
    """Best-effort px-per-mm from ruler tick periodicity in the side strip.

    Returns (px_per_mm, confidence 0..1). The ruler is the bright strip on the
    side of the frame opposite-ish the dish; ticks are regularly spaced.
    """
    h, w = gray.shape
    # choose the side with more bright (ruler) pixels outside the dish column
    left = gray[:, : int(0.12 * w)].mean()
    right = gray[:, int(0.88 * w):].mean()
    strip = gray[:, int(0.88 * w):] if right >= left else gray[:, : int(0.12 * w)]
    prof = strip.mean(axis=1)
    prof = prof - prof.mean()
    # power spectrum; find dominant period in a plausible mm range (3..40 px)
    f = np.abs(np.fft.rfft(prof * np.hanning(len(prof))))
    freqs = np.fft.rfftfreq(len(prof))
    lo, hi = 1.0 / 40, 1.0 / 3
    band = (freqs > lo) & (freqs < hi)
    if not band.any():
        return None, 0.0
    fb = f.copy(); fb[~band] = 0
    k = int(np.argmax(fb))
    if fb[k] <= 0:
        return None, 0.0
    period_px = 1.0 / freqs[k]                 # px per tick (assume 1 mm ticks)
    conf = float(fb[k] / (f[band].mean() + 1e-9))   # peak-to-mean ratio
    conf = max(0.0, min(1.0, (conf - 3) / 10))      # >~3x mean -> some confidence
    return period_px, conf


def seedling_mask(gray, dish):
    g = gaussian(gray, 1.0)
    ridge = sato(g, sigmas=RIDGE_SIGMAS, black_ridges=False)
    vals = ridge[dish]
    thr = vals.mean() + THRESH_K * vals.std()
    mask = (ridge > thr) & dish
    return remove_small_objects(mask, MIN_OBJ), ridge


def angles_from(gray, skel):
    gx, gy = sobel_v(gray), sobel_h(gray)
    ang = (np.degrees(np.arctan2(gx, gy)) + 90) % 180
    a = ang[skel]
    return np.where(a > 90, a - 180, a)


def analyse(path, dish_mm):
    """Pass 1: raw px metrics + a ruler-scale estimate (scale APPLIED later, in main,
    so it can be made consistent within each group rather than guessed per image)."""
    im = imread(path)
    g0 = rgb2gray(im) if im.ndim == 3 else im / 255.0
    scale = TARGET_W / g0.shape[1]
    g = rescale(g0, scale, anti_aliasing=True)

    circ = detect_dish(g)
    if circ:
        cy, cx, r = circ
        dish = circular_mask(g.shape, cy, cx, r)
        rpx, conf = ruler_scale(g, cx)
        dish_ppm = (2 * r) / dish_mm
    else:
        dish = np.ones_like(g, bool)
        rpx, conf, dish_ppm = None, 0.0, None

    mask, _ = seedling_mask(g, dish)
    skel = skeletonize(mask)
    a = angles_from(g, skel)
    ys, xs = np.where(mask)
    return dict(
        plant_area_px=int(mask.sum()),
        skeleton_len_px=int(skel.sum()),
        vertical_extent_px=int(ys.max() - ys.min()) if ys.size else 0,
        dish_radius_px=round(circ[2], 1) if circ else np.nan,
        n_components=int(label(mask).max()),
        mean_abs_angle=round(float(np.mean(np.abs(a))), 2) if a.size else np.nan,
        angle_dispersion=round(float(np.std(a)), 2) if a.size else np.nan,
        ruler_ppm=round(rpx, 3) if rpx else np.nan,
        ruler_conf=round(conf, 2),
        dish_ppm=round(dish_ppm, 3) if dish_ppm else np.nan,
    ), (g, mask, circ)


def group_of(fname):
    m = re.search(r'_(F|G)_', fname)
    return {'F': 'flight', 'G': 'ground'}.get(m.group(1)) if m else 'unknown'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dish-mm', type=float, default=DEFAULT_DISH_MM,
                    help='petri dish diameter in mm for fallback calibration')
    args = ap.parse_args()

    repo = find_repo_root()
    src = repo / 'data' / 'images' / 'leaves'
    out = repo / 'results' / 'osd121_morphometrics'; out.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(src / '*.JPG')))
    print(f"{len(files)} images; dish-mm fallback = {args.dish_mm}")

    rows, previews = [], []
    for i, f in enumerate(files, 1):
        name = os.path.basename(f)
        traits, prev = analyse(f, args.dish_mm)
        traits.update(file=name, group=group_of(name))
        rows.append(traits)
        if len(previews) < 6:
            previews.append((name, prev))
        print(f"  [{i}/{len(files)}] {name:46} {traits['group']:7} "
              f"area_px={traits['plant_area_px']:6}  ruler_ppm={traits['ruler_ppm']}  conf={traits['ruler_conf']}")

    df = pd.DataFrame(rows)

    # --- Consistent calibration: per-group median of CONFIDENT ruler reads. ---
    # Mixing per-image scales (or guessing dish size) disagreed by ~50% and even
    # flipped the biology, so we apply one scale per group instead.
    CONF = 0.7
    conf_reads = df[df.ruler_conf >= CONF]
    group_ppm = conf_reads.groupby('group')['ruler_ppm'].median()
    global_ppm = conf_reads['ruler_ppm'].median()
    def scale_for(g):
        v = group_ppm.get(g, np.nan)
        return v if v == v else global_ppm        # NaN-safe fallback to global
    df['px_per_mm'] = df['group'].map(scale_for)
    df['calib'] = df['group'].map(lambda g: f"group-median ruler ({group_ppm.get(g, global_ppm):.2f} px/mm, "
                                            f"n={int((conf_reads.group==g).sum())})")
    df['plant_area_mm2'] = (df.plant_area_px / df.px_per_mm**2).round(2)
    df['skeleton_len_mm'] = (df.skeleton_len_px / df.px_per_mm).round(2)
    df['vertical_extent_mm'] = (df.vertical_extent_px / df.px_per_mm).round(2)

    # Self-consistency check: a petri dish is a fixed physical size, so calibrated
    # dish diameter should be ~constant across flight & ground if the calibration
    # correctly absorbs the magnification difference.
    df['dish_diam_mm'] = (2 * df.dish_radius_px / df.px_per_mm).round(1)

    df.to_csv(out / 'summary.csv', index=False)
    print(f"\nCalibration (per-group median ruler scale): "
          + ", ".join(f"{g}={p:.2f}px/mm" for g, p in group_ppm.items()))
    print("Self-consistency — calibrated dish diameter (should match across groups if calibration is sound):")
    print(df.groupby('group')['dish_diam_mm'].agg(['mean', 'std']).round(1).to_string())
    # report BOTH the robust px metrics and the calibrated mm^2
    metrics = ['plant_area_px', 'plant_area_mm2', 'skeleton_len_mm', 'vertical_extent_mm', 'angle_dispersion']
    print("\n=== Flight vs Ground (means) ===")
    print(df.groupby('group')[metrics].mean().round(2).to_string())
    df.groupby('group')[metrics].agg(['mean', 'std', 'count']).to_csv(out / 'flight_vs_ground.csv')

    df[['file', 'group']].to_csv(repo / 'data' / 'tables' / 'groups.csv', index=False)
    print(f"\nwrote {out/'summary.csv'}, flight_vs_ground.csv, data/tables/groups.csv")

    # montage: dish-cropped gray + detected circle + segmentation
    fig, axes = plt.subplots(2, len(previews), figsize=(3*len(previews), 6))
    for j, (name, (g, mask, circ)) in enumerate(previews):
        axes[0, j].imshow(g, cmap='gray')
        if circ:
            cy, cx, r = circ
            axes[0, j].add_patch(plt.Circle((cx, cy), r, color='cyan', fill=False, lw=1))
        axes[0, j].set_title(name[:16], fontsize=7); axes[0, j].axis('off')
        axes[1, j].imshow(g, cmap='gray')
        axes[1, j].imshow(np.ma.masked_where(~mask, mask), cmap='autumn', alpha=0.8)
        axes[1, j].axis('off')
    plt.tight_layout(); plt.savefig(out / 'montage.png', dpi=110)
    print('wrote', out / 'montage.png')


if __name__ == '__main__':
    main()
