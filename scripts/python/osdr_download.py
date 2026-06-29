#!/usr/bin/env python3
"""Download files from a NASA OSDR / GeneLab study via the public file API.

Built for the FAIR overhaul (Tier 8) to pull deposited plant images into this
repo — e.g. the 24 morphometric leaf photos in OSD-121 that the R scripts in
scripts/r/morphometrics/ were written for.

API used (no auth required):
  list:     https://osdr.nasa.gov/osdr/data/osd/files/<NUMBER>
  download: https://osdr.nasa.gov<remote_url>   (remote_url is in each file record)

Examples
--------
  # the OSD-121 leaf images, into the folder the morphometric R scripts expect:
  python osdr_download.py 121 --ext jpg --out ../../data/images/leaves

  # everything matching a regex, dry-run first:
  python osdr_download.py 670 --pattern "leaf|plant" --list-only

  # any study, any extension:
  python osdr_download.py 120 --ext jpg,acr,tiff --out ../../data/images/apex03_osdr
"""
from __future__ import annotations
import argparse, os, re, sys, json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

BASE = "https://osdr.nasa.gov"
LIST_URL = BASE + "/osdr/data/osd/files/{num}"
UA = {"User-Agent": "osdr-download/1.0 (astrobotany FAIR repo)"}


def _get(url: str, timeout: int = 60) -> bytes:
    req = Request(url, headers=UA)
    with urlopen(req, timeout=timeout) as r:
        return r.read()


def list_files(accession: str) -> list[dict]:
    """Return the study_files records for an OSD accession (e.g. 'OSD-121' or '121')."""
    num = re.sub(r"\D", "", accession)
    data = json.loads(_get(LIST_URL.format(num=num)))
    studies = data.get("studies", {})
    key = next((k for k in studies if k.endswith(num)), None)
    if key is None:
        raise SystemExit(f"No study found for accession '{accession}' (parsed number {num}).")
    return studies[key].get("study_files", [])


def _matches(name: str, exts: list[str] | None, pattern: str | None) -> bool:
    if exts and not any(name.lower().endswith("." + e.lstrip(".").lower()) for e in exts):
        return False
    if pattern and not re.search(pattern, name, re.IGNORECASE):
        return False
    return True


def download(accession: str, out: str, exts=None, pattern=None, list_only=False, overwrite=False):
    files = list_files(accession)
    sel = [f for f in files if _matches(f.get("file_name", ""), exts, pattern)]
    total_bytes = sum(int(f.get("file_size") or 0) for f in sel)
    print(f"{accession}: {len(files)} files total, {len(sel)} selected "
          f"({total_bytes/1e6:.1f} MB).")
    if not sel:
        print("Nothing matched. Adjust --ext / --pattern (try --list-only with no filter).")
        return
    if list_only:
        for f in sel:
            print(f"  {int(f.get('file_size') or 0)/1e6:7.2f} MB  {f['file_name']}")
        print("\n(list-only: nothing downloaded)")
        return

    os.makedirs(out, exist_ok=True)
    ok = skipped = failed = 0
    for i, f in enumerate(sel, 1):
        name = f["file_name"]
        dest = os.path.join(out, name)
        if os.path.exists(dest) and not overwrite and os.path.getsize(dest) > 0:
            print(f"  [{i}/{len(sel)}] skip (exists): {name}")
            skipped += 1
            continue
        url = BASE + f["remote_url"] if f.get("remote_url", "").startswith("/") else f.get("remote_url", "")
        if not url:
            print(f"  [{i}/{len(sel)}] no remote_url: {name}"); failed += 1; continue
        try:
            blob = _get(url, timeout=300)
            with open(dest, "wb") as fh:
                fh.write(blob)
            print(f"  [{i}/{len(sel)}] saved {len(blob)/1e6:6.2f} MB  {name}")
            ok += 1
        except (URLError, HTTPError) as e:
            print(f"  [{i}/{len(sel)}] FAILED {name}: {e}")
            failed += 1
    print(f"\nDone: {ok} downloaded, {skipped} skipped, {failed} failed -> {out}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Download files from a NASA OSDR/GeneLab study.")
    p.add_argument("accession", help="OSD accession, e.g. 121 or OSD-121")
    p.add_argument("--out", default=".", help="output directory")
    p.add_argument("--ext", default=None,
                   help="comma-separated extensions to keep, e.g. jpg,png,tiff")
    p.add_argument("--pattern", default=None, help="regex to match filenames (case-insensitive)")
    p.add_argument("--list-only", action="store_true", help="list matches, do not download")
    p.add_argument("--overwrite", action="store_true", help="re-download even if file exists")
    a = p.parse_args(argv)
    exts = [e for e in a.ext.split(",")] if a.ext else None
    try:
        download(a.accession, a.out, exts=exts, pattern=a.pattern,
                 list_only=a.list_only, overwrite=a.overwrite)
    except (URLError, HTTPError) as e:
        sys.exit(f"Network error reaching OSDR: {e}")


if __name__ == "__main__":
    main()
