#!/usr/bin/env python3
# /// script
# dependencies = ["jieba>=0.42.1"]
# ///
from __future__ import annotations
import argparse
import errno
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

TERMS = [
    '因此','所以','于是','从而','因而','然而','但是','同时','与此同时','意味着','体现','反映',
    '关系','层面','维度','状态','过程','变化','某种','似乎','仿佛','真正','并非','而是','正因为'
]
SENT_RE = re.compile(r'[^。！？!?]+[。！？!?]?')

def parse_args():
    p=argparse.ArgumentParser(description='Count Chinese relation-language candidates. Counts are not quality scores.')
    p.add_argument('file', type=Path)
    p.add_argument('--json', action='store_true')
    p.add_argument('--top', type=int, default=30)
    p.add_argument('--allow-char-fallback', action='store_true', help='Continue without jieba; skips token/POS metrics and reports fallback explicitly.')
    return p.parse_args()

def load_jieba(allow_fallback: bool):
    try:
        import jieba
        import jieba.posseg as pseg
        return jieba, pseg, 'jieba'
    except Exception:
        if allow_fallback:
            return None, None, 'char-fallback'
        print('Error: jieba is not installed. Run with a PEP-723-capable runner such as `uv run scripts/zh_style_scan.py FILE`, install jieba, or pass --allow-char-fallback for explicit reduced analysis.', file=sys.stderr)
        raise SystemExit(3) from None

def main():
    a=parse_args()
    try:
        text=a.file.read_text(encoding='utf-8')
    except OSError as e:
        print(f'Error: cannot read {a.file}: {e}', file=sys.stderr)
        return 2
    _, pseg, tokenizer = load_jieba(a.allow_char_fallback)
    chars=''.join(ch for ch in text if not ch.isspace())
    sentences=[s.strip() for s in SENT_RE.findall(text) if s.strip()]
    counts={t:text.count(t) for t in TERMS if text.count(t)}
    cands={t:{'count':n,'per_1000_chars': round(n*1000/max(len(chars),1),3)} for t,n in sorted(counts.items(), key=lambda kv:(-kv[1],kv[0]))[:a.top]}
    openings=Counter()
    for s in sentences:
        core=re.sub(r'^[“”"\'‘’\s]+','',s)
        if core:
            openings[core[:4]] += 1
    repeated=[{'opening':k,'count':v} for k,v in sorted(openings.items(), key=lambda kv:(-kv[1],kv[0])) if v>1]
    pos={}
    if pseg is not None:
        pc=Counter(flag for _,flag in pseg.cut(text))
        pos=dict(sorted(pc.items(), key=lambda kv:(-kv[1],kv[0]))[:20])
    out={
        'file': str(a.file), 'tokenizer': tokenizer, 'characters': len(chars), 'sentences': len(sentences),
        'candidates': cands, 'repeated_sentence_openings': repeated, 'pos_summary': pos,
        'source_modified': False, 'warning':'Candidate frequency is an alarm, not a verdict.'
    }
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f'characters={out["characters"]} sentences={out["sentences"]} tokenizer={tokenizer}')
        for t,v in cands.items():
            print(f'{t}\t{v["count"]}\t{v["per_1000_chars"]}/1000c')
        if repeated:
            print('\nRepeated openings:')
            for r in repeated:
                print(f'{r["opening"]}\t{r["count"]}')
        print('\nCandidate frequency is an alarm, not a verdict.')
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
