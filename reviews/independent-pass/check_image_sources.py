"""Verify figure PNG pixels against embedded PDF images on caption pages.

Read-only. This checks asset identity and numbering, not figure meaning or translation.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import pymupdf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--chapter', type=int)
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
pdf_path = root.parent / 'Fundamentals of Software Architecture An Engineering Approach (Mark Richards, Neal Ford) (Z-Library).pdf'
pdf = pymupdf.open(pdf_path)

def signature(pix):
    if pix.alpha:
        pix = pymupdf.Pixmap(pix, 0)
    if pix.colorspace.n != 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    return (pix.width, pix.height, hashlib.sha256(pix.samples).hexdigest())

caption_pages = {}
image_pages = {}
cached = {}
for page_no, page in enumerate(pdf, 1):
    for chapter, number in re.findall(r'^Figure[ \t]+(\d+)-(\d+)\.[ \t]+\S', page.get_text(), re.M):
        caption_pages.setdefault((int(chapter), int(number)), set()).add(page_no)
    for info in page.get_images():
        xref = info[0]
        if xref not in cached:
            cached[xref] = signature(pymupdf.Pixmap(pdf, xref))
        image_pages.setdefault(cached[xref], set()).add(page_no)

results = []
for path in sorted((root / 'chapters').glob('*/images/figure-*.png')):
    match = re.fullmatch(r'figure-(\d+)-(\d+)\.png', path.name)
    if not match:
        continue
    key = tuple(map(int, match.groups()))
    if args.chapter is not None and key[0] != args.chapter:
        continue
    expected = caption_pages.get(key, set())
    identical = image_pages.get(signature(pymupdf.Pixmap(str(path))), set())
    results.append({
        'file': path.relative_to(root).as_posix(),
        'caption_pdf_pages': sorted(expected),
        'identical_image_pdf_pages': sorted(identical),
        'passes': bool(expected & identical),
    })
print(json.dumps({'checked': len(results), 'passed': sum(r['passes'] for r in results),
                  'scope': 'Figure asset pixels and caption numbering only; not semantic review.',
                  'figures': results}, ensure_ascii=False, indent=2))
raise SystemExit(0 if all(r['passes'] for r in results) else 1)
