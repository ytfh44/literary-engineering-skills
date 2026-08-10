#!/usr/bin/env python3
"""Agent-based trigger battery for the literary-engineering-skills pack.

Prompt-trigger accuracy cannot be measured by static scripts; it must be
executed by the agent/model that will use the skills (see the literary-evals
skill). This script packages the two static halves of that eval:

  gen   - emit judge input: all skill descriptions (as injected for
          discovery) plus every eval_cases.yaml prompt with an id, as JSON.
  score - grade a judge agent's routing JSON against eval_cases.yaml:
          should_trigger must route to the expected skill; should_not_trigger
          must route somewhere else; ambiguous is reported without failing.

Usage:
  python tests/run_trigger_battery.py gen judge_input.json
  python tests/run_trigger_battery.py score <judge_output.json...>

Typical loop: gen -> hand judge_input.json to a fresh agent ("route each id to
one of the listed skill names, NONE, or ASK") -> score its output.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_eval_cases() -> dict:
    # eval_cases.yaml is JSON-compatible on purpose; no yaml dependency.
    return json.loads((ROOT / 'tests/eval_cases.yaml').read_text(encoding='utf-8'))


def load_descriptions() -> dict[str, str]:
    descs = {}
    for f in sorted((ROOT / 'skills').glob('*/SKILL.md')):
        text = f.read_text(encoding='utf-8')
        m = re.search(r'^---\n(.*?)\n---', text, re.S | re.M)
        if not m:
            continue
        for line in m.group(1).splitlines():
            if line.startswith('description:'):
                descs[f.parent.name] = line.split(':', 1)[1].strip().strip('"\'')
                break
    return descs


def gen(out: Path) -> int:
    data = load_eval_cases()
    prompts = []
    for name, c in data['skills'].items():
        for kind, prefix in [('should_trigger', 'ST'), ('should_not_trigger', 'SN'), ('ambiguous', 'AM')]:
            for i, p in enumerate(c[kind]):
                prompts.append({'id': f'{name}#{prefix}#{i}', 'prompt': p})
    payload = {'descriptions': load_descriptions(), 'prompts': prompts}
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'Wrote {len(prompts)} prompts for {len(payload["descriptions"])} skills to {out}')
    return 0


def score(paths: list[Path]) -> int:
    data = load_eval_cases()
    routes = {}
    for p in paths:
        try:
            routes.update(json.loads(p.read_text(encoding='utf-8')))
        except (OSError, json.JSONDecodeError) as e:
            print(f'WARN: {p} unreadable: {e}')
    st_hit = st_tot = sn_hit = sn_tot = 0
    for name, c in data['skills'].items():
        for i, p in enumerate(c['should_trigger']):
            r = routes.get(f'{name}#ST#{i}', 'MISSING')
            st_tot += 1
            st_hit += (r == name)
            if r != name:
                print(f'  ST miss {name}#{i}: route={r} | {p[:60]}')
        for i, p in enumerate(c['should_not_trigger']):
            r = routes.get(f'{name}#SN#{i}', 'MISSING')
            sn_tot += 1
            sn_hit += (r != name)
            if r == name:
                print(f'  SN hit  {name}#{i}: route={r} | {p[:60]}')
        for i, p in enumerate(c['ambiguous']):
            print(f'  AM {routes.get(f"{name}#AM#{i}", "MISSING"):>22} | {p[:50]}')
    print(f'RESULT: should_trigger {st_hit}/{st_tot}  should_not_trigger {sn_hit}/{sn_tot}')
    return 0 if (st_hit == st_tot and sn_hit == sn_tot) else 1


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == 'gen':
        return gen(Path(args[0]))
    if mode == 'score':
        return score([Path(a) for a in args])
    print(f'Unknown mode: {mode}', file=sys.stderr)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
