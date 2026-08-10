#!/usr/bin/env python3
"""Package DOUBLE-BLIND A/B grading input.

Mixes control and treatment answers, assigns opaque random ids, strips all
condition/skill information. Graders see only prompt + answer + criteria;
the condition is recovered afterward from the mapping table.

Usage: python tests/package_grades.py
Reads gen_{ctrl,treat}_{A,B}_out.json + ab_{ctrl,treat}_{A,B}.json.
Writes grade_blind_1.json / grade_blind_2.json + grade_blind_mapping.json.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
random.seed(20260810)


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def main() -> None:
    pooled = []
    for cond in ('ctrl', 'treat'):
        for half in ('A', 'B'):
            cases = load(f'ab_{cond}_{half}.json')['cases']
            answers = load(f'gen_{cond}_{half}_out.json')
            for c in cases:
                aid = c['id']
                pooled.append({
                    'prompt': c['prompt'],
                    'answer': answers.get(aid, 'MISSING'),
                    'fail_criteria': c['fail_criteria'],
                    'pass_criteria': c['pass_criteria'],
                    '_case_id': aid,
                    '_cond': cond,
                })
    random.shuffle(pooled)
    mapping = {}
    half = (len(pooled) + 1) // 2
    for i, item in enumerate(pooled):
        gid = f'g_{i:04d}'
        mapping[gid] = {'case_id': item['_case_id'], 'condition': item['_cond']}
        item['id'] = gid
        del item['_case_id'], item['_cond']
    for g, part in ((1, pooled[:half]), (2, pooled[half:])):
        out = ROOT / f'grade_blind_{g}.json'
        out.write_text(json.dumps({'cases': part}, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'grade_blind_{g}.json: {len(part)} cases (mixed, opaque ids)')
    (ROOT / 'grade_blind_mapping.json').write_text(
        json.dumps(mapping, ensure_ascii=False, indent=1), encoding='utf-8')
    print('mapping saved (do NOT share with graders)')


if __name__ == '__main__':
    main()
