#!/usr/bin/env python3
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def run(*args):
    return subprocess.run([sys.executable, *map(str,args)], text=True, capture_output=True)

def assert_ok(p):
    assert p.returncode == 0, f'rc={p.returncode}\nstdout={p.stdout}\nstderr={p.stderr}'

def run_json(*args):
    p=run(*args)
    assert_ok(p)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError as e:
        raise AssertionError(f'non-JSON output from {args[0]}: {e}') from e

with tempfile.TemporaryDirectory() as td:
    d=Path(td)
    a=d/'a.txt'
    b=d/'b.txt'
    a.write_text('他没带伞，因此淋湿了。她似乎没看见，同时把门关上。', encoding='utf-8')
    b.write_text('他没带伞。到办公室时袖口还在滴水。她似乎没看见，把门关上。', encoding='utf-8')

    data=run_json(ROOT/'skills/relation-scaffolding/scripts/zh_style_scan.py', a, '--json', '--allow-char-fallback')
    assert data['characters'] > 0 and data['sentences'] == 2
    assert data['candidates']['因此']['count'] == 1
    assert data['candidates']['似乎']['count'] == 1
    assert not data['source_modified']

    rows=run_json(ROOT/'skills/relation-scaffolding/scripts/concordance.py', a, '似乎', '因此', '--json', '--window', '5')
    assert {r['pattern'] for r in rows} == {'似乎','因此'}
    assert all('match' in r and 'left' in r and 'right' in r for r in rows)

    diff=run_json(ROOT/'skills/counterfactual-revision/scripts/revision_diff.py', a, b, '--json')
    assert diff['original']['sentences'] == 2
    assert diff['revision']['sentences'] == 3
    assert any(op['tag'] != 'equal' for op in diff['ops'])

    c=d/'c.txt'
    c.write_text('他推开门。她推开门。雨打在门上。', encoding='utf-8')
    rec=run_json(ROOT/'skills/literary-evals/scripts/phrase_recurrence.py', a, b, c, '-n', '3', '--min-count', '2', '--json')
    assert rec['n'] == 3
    assert all(item['count'] >= 2 for item in rec['items'])


    # CLI should exit cleanly when a downstream pager/head closes early.
    # Portable substitute for `... | head -1` (no bash): the child blocks on a
    # full OS pipe buffer, then we close our read end mid-stream; the child must
    # catch BrokenPipeError and exit 0. rc != 0 would mean a traceback.
    longf=d/'long.txt'
    longf.write_text(''.join(chr(0x4e00 + (i % 18000)) for i in range(70000)), encoding='utf-8')
    p=subprocess.Popen([sys.executable, str(ROOT/'skills/literary-evals/scripts/phrase_recurrence.py'),
                        str(longf), '-n', '4', '--min-count', '1'],
                       stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    assert p.stdout is not None  # Popen with stdout=PIPE
    p.stdout.read(64)   # block until the child is mid-stream
    p.stdout.close()    # downstream closes early -> broken pipe in the child
    rc=p.wait()
    assert rc == 0, f'expected clean exit after early close, rc={rc}'

    before=a.read_bytes()
    run(ROOT/'skills/relation-scaffolding/scripts/concordance.py', a, '因此')
    assert a.read_bytes() == before

print('PASS: script smoke tests')
