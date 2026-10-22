"""Read-only Markdown checks; never a substitute for source comparison."""
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
files = sorted(p for p in ROOT.rglob('*.md')
               if not {'.git', '.idea', 'tmp'} & set(p.relative_to(ROOT).parts))
errors = []
links = images = markers = 0
for path in files:
    text = path.read_text(encoding='utf-8-sig')
    rel = path.relative_to(ROOT).as_posix()
    fence = None
    outside = []
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match[1]
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1]:
                fence = None
        elif fence is None:
            outside.append((number, line))
    if fence:
        errors.append(f'{rel}: unclosed code fence')
    ids = re.findall(r'<!--\s*((?:CH\d{2}|PF|APP|P\d{2})-\d+)\b', text)
    markers += len(ids)
    for ident, count in Counter(ids).items():
        if count > 1:
            errors.append(f'{rel}: duplicate marker {ident}')
    for number, line in outside:
        if '\ufffd' in line:
            errors.append(f'{rel}:{number}: replacement character')
        for match in re.finditer(r'(!?)\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)', line):
            target = match[2].strip('<>')
            if re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('#'):
                continue
            dest = unquote(target.split('#', 1)[0])
            links += 1
            images += bool(match[1])
            if dest and not (path.parent / dest).resolve().exists():
                errors.append(f'{rel}:{number}: missing {dest}')
print(f'Markdown files: {len(files)}; local links/images: {links}; images: {images}; paragraph markers: {markers}')
print('Checks: existing local targets, closed fences, unique markers per file, no U+FFFD outside code')
for error in errors:
    print(error)
print(f'Structure errors: {len(errors)}')
print('Does not verify translation, source coverage, external URLs, or Markdown rendering.')
sys.exit(bool(errors))
