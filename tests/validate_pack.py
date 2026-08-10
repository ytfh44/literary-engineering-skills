#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

EXPECTED = [
    'relation-scaffolding','metaphor-audit','verb-event-engineering',
    'chinese-derived-event-geometry','english-derived-motion-packaging',
    'french-derived-motion-packaging','adverb-particle-viewpoint-engineering',
    'property-and-adjective-engineering','naming-and-address-engineering',
    'predicate-licensing-and-personification',
    'camera-attention-engineering','sentence-pressure','dialogue-voice',
    'narrator-intervention-abstraction-control','character-motive-engineering',
    'counterfactual-revision','literary-style-router','literary-evals',
]
TRANSFER = {'chinese-derived-event-geometry','english-derived-motion-packaging','french-derived-motion-packaging'}
SCRIPT_PATHS = {
    'relation-scaffolding': ['scripts/zh_style_scan.py','scripts/concordance.py'],
    'counterfactual-revision': ['scripts/revision_diff.py'],
    'literary-evals': ['scripts/phrase_recurrence.py'],
}
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')

def frontmatter(text: str) -> dict[str,str]:
    if not text.startswith('---\n'):
        return {}
    end=text.find('\n---\n',4)
    if end < 0:
        return {}
    block=text[4:end]
    out={}
    key=None
    for raw in block.splitlines():
        if raw.startswith((' ', '\t')) and key:
            out[key] += ' ' + raw.strip()
            continue
        if ':' in raw:
            k,v=raw.split(':',1)
            key=k.strip()
            out[key]=v.strip().strip('>')
    return out

def validate(root: Path) -> list[str]:
    errors=[]
    if not (root/'README.md').exists():
        errors.append('missing README.md')
    if not (root/'LICENSE').exists():
        errors.append('missing LICENSE')
    for name in EXPECTED:
        d=root/'skills'/name
        p=d/'SKILL.md'
        if not p.exists():
            errors.append(f'missing skill: {name}')
            continue
        text=p.read_text(encoding='utf-8')
        meta=frontmatter(text)
        if meta.get('name') != name:
            errors.append(f'{name}: frontmatter name mismatch')
        desc=meta.get('description','').strip()
        if not desc:
            errors.append(f'{name}: missing description')
        if len(desc)>1024:
            errors.append(f'{name}: description >1024 chars')
        if desc and not desc.startswith(('"', "'")) and re.search(r':\s', desc):
            errors.append(f'{name}: unquoted colon in description breaks YAML')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name):
            errors.append(f'{name}: invalid name')
        if len(name)>64:
            errors.append(f'{name}: name >64 chars')
        lines=text.count('\n')+1
        if lines>500:
            errors.append(f'{name}: SKILL.md >500 lines ({lines})')
        if '## Minimal pair' not in text:
            errors.append(f'{name}: no Minimal pair section')
        if '## Counterexamples' not in text:
            errors.append(f'{name}: no Counterexamples section')
        if name in TRANSFER:
            if '## Transfer' not in text:
                errors.append(f'{name}: missing Transfer section')
            if 'Transfer the operation, not the costume.' not in text:
                errors.append(f'{name}: missing transfer maxim')
            if '## Transfer residue' not in text:
                errors.append(f'{name}: missing Transfer residue section')
        for link in LINK_RE.findall(text):
            if '://' in link or link.startswith('#'):
                continue
            target=(d/link).resolve()
            if not target.exists():
                errors.append(f'{name}: broken link {link}')
        for rel in SCRIPT_PATHS.get(name,[]):
            if not (d/rel).exists():
                errors.append(f'{name}: missing script {rel}')
    return errors

def main() -> int:
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    errors=validate(root)
    if errors:
        print(f'FAIL {len(errors)} issue(s)')
        for e in errors:
            print(f'- {e}')
        return 1
    print(f'PASS: {len(EXPECTED)} skills structurally valid')
    return 0
if __name__=='__main__':
    raise SystemExit(main())
