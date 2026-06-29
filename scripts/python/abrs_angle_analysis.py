#!/usr/bin/env python3
"""ABRS root-angle dispersion over time — testing synthesis prediction #1.

Prediction (docs/CROSS_EXPERIMENT_SYNTHESIS.md): spaceflight roots lose tight
directional alignment, so flight root-angle DISPERSION should exceed ground —
as OSD-121 showed. This checks it on the ABRS time-lapse.

Per frame: enhance thin root structures (Sato ridge filter on the green channel),
skeletonize, and measure the SD of local root orientations (= angle dispersion,
scale-free) and mean |angle from vertical|. Plotted as a flight-vs-ground time
course.

CAVEAT — this is a single flight plate vs a single ground plate imaged over 11
days, so the timepoints are NOT independent replicates: treat this as a
DESCRIPTIVE time course, not a powered test (unlike OSD-121's 13 dishes/group).
A regular grid is etched in the chamber; it adds fixed 0/90 deg components to
BOTH conditions equally, so the flight-vs-ground CONTRAST remains informative.

Run:  python scripts/python/abrs_angle_analysis.py
Out:  results/abrs_angle/{summary.csv, timecourse.png}
"""
from __future__ import annotations
import os, glob, re
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from skimage.io import imread
from skimage.transform import rescale
from skimage.filters import sato, sobel_h, sobel_v, gaussian
from skimage.morphology import skeletonize, remove_small_objects

TARGET_W = 900


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / 'ABRS_NASA_Roots_TimeLapse').exists() or (c / 'data' / 'images' / 'abrs_timelapse').exists():
            return c
    return p


def green(im):
    if im.ndim == 3:
        return im[..., 1] / 255.0   # green channel (ABRS green-LED imaging)
    return im / 255.0


def root_angles(path):
    im = imread(path)
    g = green(im)
    g = rescale(g, TARGET_W / g.shape[1], anti_aliasing=True)
    g = gaussian(g, 1.0)
    ridge = sato(g, sigmas=(1, 2, 3), black_ridges=False)
    thr = ridge[ridge > 0].mean() + 1.0 * ridge[ridge > 0].std()
    mask = remove_small_objects(ridge > thr, 80)
    skel = skeletonize(mask)
    gx, gy = sobel_v(g), sobel_h(g)
    ang = (np.degrees(np.arctan2(gx, gy)) + 90) % 180
    a = ang[skel]
    a = np.where(a > 90, a - 180, a)   # -90..90, 0 = vertical
    return a, int(skel.sum())


def date_from(name):
    m = re.search(r'(\d{4}_\d{2}_\d{2})', name)
    return m.group(1) if m else name


def main():
    repo = find_repo_root()
    base = repo / 'ABRS_NASA_Roots_TimeLapse'
    if not base.exists():
        base = repo / 'data' / 'images' / 'abrs_timelapse'
    groups = {'flight': base / 'ABRS_Flight_11_days_11_photos',
              'ground': base / 'ABRS_Ground_11_days_11_photos'}
    out = repo / 'results' / 'abrs_angle'; out.mkdir(parents=True, exist_ok=True)

    rows = []
    for grp, d in groups.items():
        files = sorted(glob.glob(str(d / '*.jpg')))
        for i, f in enumerate(files):
            a, n = root_angles(f)
            if a.size == 0:
                continue
            rows.append(dict(group=grp, day=i, date=date_from(os.path.basename(f)),
                             n_skel_px=n, mean_abs_angle=round(float(np.mean(np.abs(a))), 2),
                             angle_dispersion=round(float(np.std(a)), 2)))
            print(f"  {grp:7} day {i:2} {date_from(os.path.basename(f))}  "
                  f"disp={rows[-1]['angle_dispersion']:.1f}  mean|ang|={rows[-1]['mean_abs_angle']:.1f}")
    df = pd.DataFrame(rows)
    df.to_csv(out / 'summary.csv', index=False)

    print("\n=== Mean over the time course (single plate per group — descriptive) ===")
    print(df.groupby('group')[['angle_dispersion', 'mean_abs_angle']].agg(['mean', 'std']).round(2).to_string())
    # later-stage frames (roots developed): days >= 5
    late = df[df.day >= 5]
    print("\n=== Late frames (day>=5) mean angle_dispersion ===")
    print(late.groupby('group')['angle_dispersion'].mean().round(2).to_string())

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    for grp, g in df.groupby('group'):
        ax[0].plot(g.day, g.angle_dispersion, 'o-', label=grp)
        ax[1].plot(g.day, g.mean_abs_angle, 'o-', label=grp)
    ax[0].set_title('Root-angle dispersion over time'); ax[0].set_xlabel('day'); ax[0].set_ylabel('angle SD (deg)'); ax[0].legend()
    ax[1].set_title('Mean |angle from vertical| over time'); ax[1].set_xlabel('day'); ax[1].set_ylabel('deg'); ax[1].legend()
    plt.tight_layout(); plt.savefig(out / 'timecourse.png', dpi=120)
    print(f"\nwrote {out/'summary.csv'} and {out/'timecourse.png'}")


if __name__ == '__main__':
    main()
