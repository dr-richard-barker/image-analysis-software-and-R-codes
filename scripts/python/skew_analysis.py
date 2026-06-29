#!/usr/bin/env python3
"""Statistical analysis of the 18-way nutritional root-skew assay (RSML).

The flagship dataset: 53 RootNav RSML files, ~500 primary roots, from a
2 (gelling agent: agar/phytogel) x 3 (gelling %: 0.5/1/1.5) x 3 (sucrose %:
0/0.3/1) design. Question the assay was built to answer: which media factors
drive root **skewing** (chiral deviation from the vertical)?

Extracts scale-free skew traits per root (signed tip angle, |tip angle|,
tortuosity), then tests the media factors with ANOVA. RSML is uncalibrated
(unit=pixel) so we use only angle/shape traits, which need no calibration.

Run:  python scripts/python/skew_analysis.py
Out:  results/skew_analysis/{root_traits.csv, anova.txt, figure.png}
"""
from __future__ import annotations
import os, glob, re, math, itertools
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import xml.etree.ElementTree as ET
from scipy import stats


def find_repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for c in [p, *p.parents]:
        if (c / '18_way_skew').exists() or (c / 'data' / 'rsml' / '18_way_skew').exists():
            return c
    return p


def poly_points(root_el):
    pts = root_el.findall('.//polyline/point') or root_el.findall('.//point')
    return [(float(p.get('x')), float(p.get('y'))) for p in pts]


def signed_tip_angle(pts):
    """Angle (deg) of the root tip direction from vertical; sign = skew direction."""
    if len(pts) < 4:
        return None
    seg = max(3, len(pts) // 10)
    p0, p1 = pts[-min(seg, len(pts))], pts[-1]
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    return math.degrees(math.atan2(dx, dy))   # 0 = straight down


def tortuosity(pts):
    if len(pts) < 2:
        return None
    path = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    chord = math.dist(pts[0], pts[-1])
    return path / chord if chord else None


def parse(fname):
    m = re.match(r'Gradient_([\d.]+)%([AP])_([\d.]+)%S_(\d+)', fname)
    g, agent, s, rep = m.groups()
    return dict(gelling_agent={'A': 'agar', 'P': 'phytogel'}[agent],
                gelling_pct=float(g), sucrose_pct=float(s), replicate=int(rep))


def main():
    repo = find_repo_root()
    src = repo / 'data' / 'rsml' / '18_way_skew'
    if not src.exists():
        src = repo / '18_way_skew'
    out = repo / 'results' / 'skew_analysis'; out.mkdir(parents=True, exist_ok=True)

    rows = []
    for f in sorted(glob.glob(str(src / '*.rsml'))):
        meta = parse(os.path.basename(f))
        for r in ET.parse(f).getroot().findall('.//root'):
            pts = poly_points(r)
            ta = signed_tip_angle(pts)
            if ta is None:
                continue
            rows.append(dict(**meta, tip_angle=ta, abs_tip_angle=abs(ta),
                             tortuosity=tortuosity(pts)))
    df = pd.DataFrame(rows)
    df.to_csv(out / 'root_traits.csv', index=False)
    print(f"{len(df)} roots from {df.groupby(['gelling_agent','gelling_pct','sucrose_pct']).ngroups} treatments")

    lines = []
    def log(s): print(s); lines.append(s)

    # |tip angle| = how strongly skewed (regardless of direction)
    log("\n=== Mean |tip angle| (deg) by factor ===")
    log(df.groupby('gelling_agent')['abs_tip_angle'].agg(['mean', 'std', 'count']).round(2).to_string())
    log(df.groupby('sucrose_pct')['abs_tip_angle'].mean().round(2).to_string())
    log(df.groupby('gelling_pct')['abs_tip_angle'].mean().round(2).to_string())

    # one-way tests for each factor on |tip angle| and tortuosity
    log("\n=== One-way ANOVA / t-tests ===")
    for trait in ['abs_tip_angle', 'tortuosity']:
        d = df.dropna(subset=[trait])
        # gelling agent: 2 groups -> Welch t
        a = d[d.gelling_agent == 'agar'][trait]; p = d[d.gelling_agent == 'phytogel'][trait]
        t, pv = stats.ttest_ind(a, p, equal_var=False)
        log(f"  {trait:14} agar({a.mean():.2f}) vs phytogel({p.mean():.2f}): t={t:.2f} p={pv:.4f}{' *' if pv<.05 else ''}")
        # sucrose: 3 groups -> one-way ANOVA
        groups = [g[trait].values for _, g in d.groupby('sucrose_pct')]
        F, pv = stats.f_oneway(*groups)
        log(f"  {trait:14} sucrose% ANOVA: F={F:.2f} p={pv:.4f}{' *' if pv<.05 else ''}")
        groups = [g[trait].values for _, g in d.groupby('gelling_pct')]
        F, pv = stats.f_oneway(*groups)
        log(f"  {trait:14} gelling% ANOVA: F={F:.2f} p={pv:.4f}{' *' if pv<.05 else ''}")

    # directional bias: is mean signed tip angle != 0 (consistent skew direction)?
    log("\n=== Directional skew (signed tip angle, mean != 0 => consistent handedness) ===")
    for agent, g in df.groupby('gelling_agent'):
        t, pv = stats.ttest_1samp(g.tip_angle, 0)
        log(f"  {agent:9}: mean signed tip angle = {g.tip_angle.mean():+.2f} deg  (t={t:.2f}, p={pv:.4f}{' *' if pv<.05 else ''})")

    (out / 'anova.txt').write_text("\n".join(lines), encoding='utf-8')

    # figure: |tip angle| by gelling agent x sucrose, tortuosity by sucrose
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    piv = df.pivot_table('abs_tip_angle', 'sucrose_pct', 'gelling_agent', 'mean')
    piv.plot(kind='bar', ax=ax[0]); ax[0].set_ylabel('mean |tip angle| (deg)')
    ax[0].set_title('Root skew strength by gelling agent x sucrose'); ax[0].set_xlabel('sucrose %')
    df.boxplot('tip_angle', by='gelling_agent', ax=ax[1])
    ax[1].axhline(0, color='k', lw=0.6, ls='--'); ax[1].set_ylabel('signed tip angle (deg)')
    ax[1].set_title('Skew direction by gelling agent'); plt.suptitle('')
    plt.tight_layout(); plt.savefig(out / 'figure.png', dpi=120)
    print(f"\nwrote {out/'root_traits.csv'}, anova.txt, figure.png")


if __name__ == '__main__':
    main()
