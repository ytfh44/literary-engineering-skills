#!/usr/bin/env python3
"""Protocol and blinding regression tests for run_trigger_battery.py."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tests/run_trigger_battery.py'
OPAQUE_ID_RE = re.compile(r'case-[0-9a-f]{16}\Z')


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, args)],
        text=True,
        capture_output=True,
    )


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


with tempfile.TemporaryDirectory() as td:
    directory = Path(td)
    public = directory / 'judge_input.json'
    mapping = directory / 'scoring_map.json'
    same_seed_public = directory / 'judge_input_same.json'
    same_seed_mapping = directory / 'scoring_map_same.json'
    other_seed_public = directory / 'judge_input_other.json'
    other_seed_mapping = directory / 'scoring_map_other.json'

    generated = run_cli(
        'gen', public, '--map', mapping, '--seed', '42'
    )
    assert generated.returncode == 0, generated.stderr
    public_payload = json.loads(public.read_text(encoding='utf-8'))
    mapping_payload = json.loads(mapping.read_text(encoding='utf-8'))

    assert public_payload['format_version'] == 1
    assert mapping_payload['format_version'] == 1
    assert mapping_payload['seed'] == 42
    assert len(public_payload['prompts']) == len(mapping_payload['cases']) == 474
    assert all(set(item) == {'id', 'prompt'} for item in public_payload['prompts'])

    descriptions = public_payload['descriptions']
    mapped_by_id = {case['id']: case for case in mapping_payload['cases']}
    public_ids = [item['id'] for item in public_payload['prompts']]
    assert len(set(public_ids)) == len(public_ids)
    assert set(public_ids) == set(mapped_by_id)
    assert all(OPAQUE_ID_RE.fullmatch(case_id) for case_id in public_ids)
    assert all(
        not any(skill_name in case_id for skill_name in descriptions)
        for case_id in public_ids
    )

    canonical_sources = [case['source'] for case in mapping_payload['cases']]
    public_sources = [mapped_by_id[case_id]['source'] for case_id in public_ids]
    assert public_sources != canonical_sources

    same_seed = run_cli(
        'gen', same_seed_public, '--map', same_seed_mapping, '--seed', '42'
    )
    assert same_seed.returncode == 0, same_seed.stderr
    assert public.read_bytes() == same_seed_public.read_bytes()
    assert mapping.read_bytes() == same_seed_mapping.read_bytes()

    other_seed = run_cli(
        'gen', other_seed_public, '--map', other_seed_mapping, '--seed', '43'
    )
    assert other_seed.returncode == 0, other_seed.stderr
    assert public.read_bytes() != other_seed_public.read_bytes()
    assert mapping.read_bytes() != other_seed_mapping.read_bytes()

    routes = {}
    for case in mapping_payload['cases']:
        if case['class'] == 'ST':
            routes[case['id']] = case['acceptable'][0]
        elif case['class'] == 'SN':
            routes[case['id']] = 'NONE'
        else:
            routes[case['id']] = 'ASK'

    complete = directory / 'complete.json'
    write_json(complete, routes)
    scored = run_cli('score', '--map', mapping, complete)
    assert scored.returncode == 0, scored.stdout + scored.stderr
    assert 'RESULT: should_trigger 194/194  should_not_trigger 186/186' in scored.stdout

    midpoint = len(routes) // 2
    ids = list(routes)
    first_slice = directory / 'judge_a.json'
    second_slice = directory / 'judge_b.json'
    write_json(first_slice, {case_id: routes[case_id] for case_id in ids[:midpoint]})
    write_json(second_slice, {case_id: routes[case_id] for case_id in ids[midpoint:]})
    split_scored = run_cli('score', '--map', mapping, first_slice, second_slice)
    assert split_scored.returncode == 0, split_scored.stdout + split_scored.stderr

    empty = directory / 'empty.json'
    write_json(empty, {})
    empty_scored = run_cli('score', '--map', mapping, empty)
    assert empty_scored.returncode != 0
    assert 'VALIDATION FAILED:' in empty_scored.stdout
    assert 'RESULT:' not in empty_scored.stdout

    duplicate = directory / 'duplicate.json'
    first_id = ids[0]
    write_json(duplicate, {first_id: routes[first_id]})
    duplicate_scored = run_cli('score', '--map', mapping, complete, duplicate)
    assert duplicate_scored.returncode != 0
    assert 'duplicate id across judge outputs' in duplicate_scored.stdout
    assert 'RESULT:' not in duplicate_scored.stdout

    invalid = directory / 'invalid.json'
    invalid_routes = dict(routes)
    invalid_routes[first_id] = 'NOT-A-SKILL'
    write_json(invalid, invalid_routes)
    invalid_scored = run_cli('score', '--map', mapping, invalid)
    assert invalid_scored.returncode != 0
    assert 'invalid route' in invalid_scored.stdout
    assert 'RESULT:' not in invalid_scored.stdout

    unknown = directory / 'unknown.json'
    unknown_routes = dict(routes)
    unknown_routes['case-deadbeefdeadbeef'] = 'NONE'
    write_json(unknown, unknown_routes)
    unknown_scored = run_cli('score', '--map', mapping, unknown)
    assert unknown_scored.returncode != 0
    assert 'unknown judge id' in unknown_scored.stdout
    assert 'RESULT:' not in unknown_scored.stdout

print('PASS: trigger battery protocol tests')
