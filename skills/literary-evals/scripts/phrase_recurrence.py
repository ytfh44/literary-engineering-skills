#!/usr/bin/env python3
from __future__ import annotations
import argparse
import errno
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

def norm(s):
    return re.sub(r'\s+','',s)

def main():
    p=argparse.ArgumentParser(description='Find recurrent character n-grams across generated samples.')
    p.add_argument('files',nargs='+',type=Path)
    p.add_argument('-n',type=int,default=4)
    p.add_argument('--min-count',type=int,default=2)
    p.add_argument('--json',action='store_true')
    a=p.parse_args()
    if a.n < 2:
        print('Error: -n must be >= 2.',file=sys.stderr)
        return 2
    counts=Counter()
    docs=defaultdict(set)
    for idx,path in enumerate(a.files):
        try:
            text=norm(path.read_text(encoding='utf-8'))
        except OSError as e:
            print(f'Error: cannot read {path}: {e}',file=sys.stderr)
            return 2
        for i in range(max(0,len(text)-a.n+1)):
            g=text[i:i+a.n]
            if all(ch in '，。！？；：,.!?;:"\'“”‘’（）()[]{}-' for ch in g):
                continue
            counts[g]+=1
            docs[g].add(idx)
    items=[{'phrase':g,'count':c,'document_coverage':len(docs[g])} for g,c in counts.items() if c>=a.min_count]
    items.sort(key=lambda x:(-x['document_coverage'],-x['count'],x['phrase']))
    out={'n':a.n,'min_count':a.min_count,'documents':len(a.files),'items':items,'warning':'Recurrence is a manual-inspection trigger, not proof of bad style.'}
    if a.json:
        print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
    else:
        for it in items:
            print(f'{it["document_coverage"]}/{len(a.files)} docs\t{it["count"]}\t{it["phrase"]}')
        print('\nRecurrence is a manual-inspection trigger, not proof of bad style.')
    return 0
if __name__=='__main__':
    try:
        raise SystemExit(main())
    except OSError as e:
        if getattr(e,'errno',None) not in (errno.EPIPE, errno.EINVAL):
            raise
        # Downstream (head/pager) closed the pipe. Redirect stdout to devnull so
        # the interpreter's shutdown flush cannot fail again (exit 120). Windows
        # surfaces broken pipes as EINVAL (WinError 232), not BrokenPipeError.
        devnull=os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        raise SystemExit(0) from None
