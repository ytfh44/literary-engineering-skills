#!/usr/bin/env python3
"""Package A/B grading input: case criteria + generated answers -> grade_<cond>.json.

Usage: python tests/package_grades.py
Reads gen_{ctrl,treat}_{A,B}_out.json + ab_{ctrl,treat}_{A,B}.json,
writes grade_{ctrl,treat}_{A,B}.json for the second-wave grading agents.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def main() -> None:
    for cond in ('ctrl', 'treat'):
        for half in ('A', 'B'):
            cases = load(f'ab_{cond}_{half}.json')['cases']
            answers = load(f'gen_{cond}_{half}_out.json')
            graded = []
            for c in cases:
                aid = c['id']
                graded.append({
                    'id': aid,
                    'prompt': c['prompt'],
                    'answer': answers.get(aid, 'MISSING'),
                    'fail_criteria': c['fail_criteria'],
                    'pass_criteria': c['pass_criteria'],
                })
            out = ROOT / f'grade_{cond}_{half}.json'
            out.write_text(json.dumps({'cases': graded}, ensure_ascii=False, indent=1), encoding='utf-8')
            missing = [c['id'] for c in cases if c['id'] not in answers]
            print(f'{cond}_{half}: {len(graded)} cases, missing answers: {missing or "none"}')


if __name__ == '__main__':
    main()
