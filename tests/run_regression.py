#!/usr/bin/env python3
from __future__ import annotations
import json
import re
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={p.parent.name for p in ROOT.glob('skills/*/SKILL.md')}
TRANSFER={'chinese-derived-event-geometry','english-derived-motion-packaging','french-derived-motion-packaging'}

def fail(msg):
    print('FAIL:',msg)
    return 1

def main():
    try:
        data=json.loads((ROOT/'tests/eval_cases.yaml').read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        return fail(f'eval_cases.yaml unreadable: {e}')
    if set(data['skills']) != EXPECTED:
        return fail(f'eval skill set mismatch: eval={len(data["skills"])} files={len(EXPECTED)}')
    for name,c in data['skills'].items():
        for key,minn in [('should_trigger',8),('should_not_trigger',8),('ambiguous',4),('quality_cases',2)]:
            if len(c.get(key,[]))<minn:
                return fail(f'{name}: {key} < {minn}')
    forbidden=[r'only works in (Chinese|Japanese|English|French)', r'can only be used in (Chinese|Japanese|English|French)', r'(Chinese|Japanese|English|French) cannot express']
    for path in ROOT.glob('**/*.md'):
        text=path.read_text(encoding='utf-8')
        if re.search(r'\b(TODO|TBD|FIXME)\b',text):
            return fail(f'placeholder in {path}')
        for pat in forbidden:
            if re.search(pat,text,re.I):
                return fail(f'language exclusivity in {path}: {pat}')
    for name in TRANSFER:
        text=(ROOT/'skills'/name/'SKILL.md').read_text(encoding='utf-8')
        if '## Transfer' not in text or 'Transfer the operation, not the costume.' not in text:
            return fail(f'{name}: transfer contract missing')
    p=subprocess.run([sys.executable,str(ROOT/'tests/validate_pack.py'),str(ROOT)],text=True,capture_output=True)
    if p.returncode:
        print(p.stdout,p.stderr)
        return fail('structural validator failed')
    print(f'PASS: regression fixtures complete for {len(EXPECTED)} skills')
    print('NOTE: prompt-trigger fixtures require a host agent/model to execute; this script validates fixture coverage and package invariants.')
    return 0
if __name__=='__main__':
    raise SystemExit(main())
