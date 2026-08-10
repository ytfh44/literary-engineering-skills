#!/usr/bin/env python3
from __future__ import annotations
import argparse
import difflib
import errno
import json
import os
import re
import sys
from pathlib import Path
REL=['因此','所以','于是','从而','然而','同时','意味着','体现','关系','状态','过程','变化','某种','似乎','并非','而是']
SENT_RE=re.compile(r'[^。！？!?]+[。！？!?]?')

def summary(text):
    return {'characters':len(''.join(c for c in text if not c.isspace())), 'sentences':len([s for s in SENT_RE.findall(text) if s.strip()]), 'relation_candidates':{t:text.count(t) for t in REL if text.count(t)}}

def main():
    p=argparse.ArgumentParser(description='Inspect original/revision differences without scoring prose.')
    p.add_argument('original',type=Path)
    p.add_argument('revision',type=Path)
    p.add_argument('--json',action='store_true')
    a=p.parse_args()
    try:
        x=a.original.read_text(encoding='utf-8')
        y=a.revision.read_text(encoding='utf-8')
    except OSError as e:
        print(f'Error: cannot read input: {e}', file=sys.stderr)
        return 2
    sm=difflib.SequenceMatcher(a=x,b=y)
    ops=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        ops.append({'tag':tag,'original':x[i1:i2],'revision':y[j1:j2],'original_span':[i1,i2],'revision_span':[j1,j2]})
    out={'original':summary(x),'revision':summary(y),'ops':ops,'source_modified':False}
    if a.json:
        print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
    else:
        print(''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile=str(a.original),tofile=str(a.revision))))
        print('Original:',out['original'])
        print('Revision:',out['revision'])
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
