#!/usr/bin/env python3
from __future__ import annotations
import argparse
import errno
import json
import os
import re
import sys
from pathlib import Path

def args():
    p=argparse.ArgumentParser(description='Print literal or regex concordance from UTF-8 text.')
    p.add_argument('file', type=Path)
    p.add_argument('patterns', nargs='+')
    p.add_argument('--regex', action='store_true')
    p.add_argument('--window', type=int, default=20)
    p.add_argument('--json', action='store_true')
    return p.parse_args()

def main():
    a=args()
    try:
        text=a.file.read_text(encoding='utf-8')
    except OSError as e:
        print(f'Error: cannot read {a.file}: {e}', file=sys.stderr)
        return 2
    rows=[]
    for pat in a.patterns:
        try:
            rgx=re.compile(pat if a.regex else re.escape(pat))
        except re.error as e:
            print(f'Error: invalid regex {pat!r}: {e}', file=sys.stderr)
            return 2
        for m in rgx.finditer(text):
            rows.append({'pattern':pat,'start':m.start(),'end':m.end(),'left':text[max(0,m.start()-a.window):m.start()], 'match':m.group(0), 'right':text[m.end():m.end()+a.window]})
    rows.sort(key=lambda r:(r['start'],r['pattern']))
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        for r in rows:
            print(f'{r["start"]:>6}  {r["pattern"]}: {r["left"]}⟦{r["match"]}⟧{r["right"]}')
    return 0
if __name__=='__main__':
    try:
        raise SystemExit(main())
    except OSError as e:
        if getattr(e,'errno',None) not in (errno.EPIPE, errno.EINVAL):
            raise
        devnull=os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        raise SystemExit(0) from None
