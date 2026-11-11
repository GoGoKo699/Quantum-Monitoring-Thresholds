"""Static navigation and math-delimiter checks, separate from hosted review."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    seen = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'<[^>]+>', '', title).lower()
        title = re.sub(r'[^\w\s-]', '', title)
        slug = re.sub(r'\s', '-', title)
        count = seen.get(slug, 0)
        seen[slug] = count+1
        found.add(slug if not count else f'{slug}-{count}')
    return found


def main():
    failures = []
    links = 0
    math = 0
    pages = sorted(ROOT.rglob('*.md'))
    pages = [p for p in pages if not any(x in p.relative_to(ROOT).parts for x in ['build', '.git', '.venv'])]
    for p in pages:
        text = p.read_text()
        rel = p.relative_to(ROOT).as_posix()
        fence = None
        for n, line in enumerate(text.splitlines(), 1):
            marker = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                    math += marker.group(2).strip() == 'math'
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
        if fence:
            failures.append(f'{rel}: unclosed fenced block')
        if text.count('$`') != text.count('`$'):
            failures.append(f'{rel}: unmatched GitHub inline-math delimiter')
        for dest in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            dest = dest.strip().strip('<>')
            if re.match(r'^[a-z]+:', dest, re.I) or dest.startswith('//'):
                continue
            path, _, fragment = dest.partition('#')
            target = (p.parent/unquote(path)).resolve() if path else p
            if not target.is_relative_to(ROOT):
                failures.append(f'{rel}: local link escapes repository: {dest}')
            elif not target.is_file():
                failures.append(f'{rel}: missing local file: {dest}')
            elif fragment and target.suffix == '.md' and unquote(fragment) not in anchors(target.read_text()):
                failures.append(f'{rel}: missing anchor: {dest}')
            links += 1
        if rel != 'AGENTS.md' and re.search(r'Camelot|Merlin.Arthur|game_id|Guinevere', text):
            failures.append(f'{rel}: private-workflow text in public account')
    required = ['README.md', 'science/model.md', 'science/haar_entropy.md',
                'science/setting_frontier.md', 'science/shareability.md',
                'science/coding.md', 'science/interpretation.md',
                'references/RELATED_WORK.md', 'references/bibliography.json', 'llms.txt']
    for name in required:
        if not (ROOT/name).is_file():
            failures.append(f'missing scientific route: {name}')
    milestone_file = ROOT/'learning/MILESTONES.md'
    milestone_count = 0
    if milestone_file.is_file():
        milestone_text = milestone_file.read_text()
        sections = re.split(r'^### M(\d{2}) — ', milestone_text, flags=re.M)
        ids = sections[1::2]
        milestone_count = len(ids)
        if ids != [f'{i:02d}' for i in range(1, 31)]:
            failures.append('learning: expected exactly M01–M30 in order')
        fields = ['Central question', 'Understanding target', 'Dependencies and story role',
                  'Conceptual connection', 'Source pointers']
        for ident, body in zip(ids, sections[2::2]):
            for field in fields:
                if f'**{field}:**' not in body:
                    failures.append(f'M{ident}: missing {field}')
            dependency_text = re.search(r'\*\*Dependencies and story role:\*\* (.+)', body)
            if dependency_text:
                for predecessor in re.findall(r'\bM(\d{2})\b', dependency_text.group(1)):
                    if int(predecessor) >= int(ident):
                        failures.append(f'M{ident}: non-prior dependency M{predecessor}')
    else:
        failures.append('missing learning/MILESTONES.md')
    bib = ROOT/'references/bibliography.json'
    if bib.is_file():
        try:
            json.loads(bib.read_text())
        except ValueError as e:
            failures.append(f'bibliography JSON: {e}')
    print(json.dumps({'status': 'fail' if failures else 'pass', 'pages': len(pages),
                      'local_links': links, 'display_math_blocks': math,
                      'milestones': milestone_count,
                      'scope': 'Static source/navigation only; no hosted rendering or theorem certification.',
                      'failures': failures}, indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
