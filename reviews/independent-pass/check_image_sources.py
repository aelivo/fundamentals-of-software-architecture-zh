"""Verify figure PNG pixels against embedded PDF images on caption pages.

Read-only. This checks asset identity and numbering, not figure meaning or translation.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--chapter', type=int)
parser.add_argument('--pdf', type=Path, help='Explicit source PDF; defaults to the project or its parent.')
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
pdf_name = 'Fundamentals of Software Architecture An Engineering Approach (Mark Richards, Neal Ford) (Z-Library).pdf'
pdf_path = args.pdf or next((p for p in (root / pdf_name, root.parent / pdf_name) if p.is_file()), None)
if pdf_path is None:
    parser.error('Source PDF not found; supply --pdf.')
pdf = PdfReader(pdf_path)

def signature(image):
    rgb = image.convert('RGB')
    return (*rgb.size, hashlib.sha256(rgb.tobytes()).hexdigest())

caption_pages = {}
image_pages = {}
cached = {}
for page_no, page in enumerate(pdf.pages, 1):
    for chapter, number in re.findall(r'^Figure[ \t]+(\d+)-(\d+)\.[ \t]+\S', page.extract_text(), re.M):
        caption_pages.setdefault((int(chapter), int(number)), set()).add(page_no)
    for embedded in page.images:
        ref = embedded.indirect_reference
        key = (ref.idnum, ref.generation) if ref else (page_no, embedded.name)
        if key not in cached:
            cached[key] = signature(embedded.image)
        image_pages.setdefault(cached[key], set()).add(page_no)

results = []
for path in sorted((root / 'chapters').glob('*/images/figure-*.png')):
    match = re.fullmatch(r'figure-(\d+)-(\d+)\.png', path.name)
    if not match:
        continue
    key = tuple(map(int, match.groups()))
    if args.chapter is not None and key[0] != args.chapter:
        continue
    expected = caption_pages.get(key, set())
    with Image.open(path) as figure:
        identical = image_pages.get(signature(figure), set())
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
