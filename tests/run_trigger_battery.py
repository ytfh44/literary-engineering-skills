#!/usr/bin/env python3
"""Agent-based trigger battery for the literary-engineering-skills pack.

Prompt-trigger accuracy cannot be measured by static scripts; it must be
executed by the agent/model that will use the skills (see the literary-evals
skill). This script packages the two static halves of that eval:

  gen   - emit judge input with opaque prompt ids, plus a private scoring map;
  score - validate judge routing JSON and grade it against that private map.

Usage:
  python tests/run_trigger_battery.py gen judge_input.json \
      --map scoring_map.json --seed 42
  python tests/run_trigger_battery.py score --map scoring_map.json \
      judge_output.json...

Only judge_input.json should be handed to a judge. The scoring map contains
the expected answers and source fixtures and must remain private.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_FORMAT_VERSION = 1
MAPPING_FORMAT_VERSION = 1
CASE_BUCKETS = (
    ('should_trigger', 'ST'),
    ('should_not_trigger', 'SN'),
    ('ambiguous', 'AM'),
)
CASE_CLASSES = {prefix for _, prefix in CASE_BUCKETS}
VALID_SPECIAL_ROUTES = {'NONE', 'ASK'}
OPAQUE_ID_RE = re.compile(r'case-[0-9a-f]{16}\Z')


class ProtocolError(ValueError):
    """Raised when an eval artifact does not follow the battery protocol."""


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


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key {key!r}')
        result[key] = value
    return result


def read_json(path: Path):
    try:
        text = path.read_text(encoding='utf-8')
    except OSError as e:
        raise ProtocolError(f'{path} unreadable: {e}') from e
    try:
        return json.loads(text, object_pairs_hook=_reject_duplicate_keys)
    except (json.JSONDecodeError, ValueError) as e:
        raise ProtocolError(f'{path} invalid JSON: {e}') from e


def write_json(path: Path, payload) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
        encoding='utf-8',
    )


def _normalise_fixture(
    skill: str,
    bucket: str,
    prefix: str,
    index: int,
    raw,
) -> dict:
    if isinstance(raw, str):
        prompt = raw
        primary = skill if bucket == 'should_trigger' else None
        acceptable = [skill] if bucket == 'should_trigger' else []
        forbidden = [skill] if bucket == 'should_not_trigger' else []
    elif isinstance(raw, dict):
        prompt = raw.get('prompt')
        if not isinstance(prompt, str):
            raise ProtocolError(
                f'{skill}/{bucket}/{index} must contain a string prompt'
            )
        primary = raw.get(
            'primary', skill if bucket == 'should_trigger' else None
        )
        acceptable = raw.get(
            'acceptable', [primary] if primary is not None else []
        )
        forbidden = raw.get(
            'forbidden', [skill] if bucket == 'should_not_trigger' else []
        )
    else:
        raise ProtocolError(f'{skill}/{bucket}/{index} is not a string or object')

    if primary is not None and not isinstance(primary, str):
        raise ProtocolError(f'{skill}/{bucket}/{index}: primary must be a string or null')
    for field, values in [('acceptable', acceptable), ('forbidden', forbidden)]:
        if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
            raise ProtocolError(f'{skill}/{bucket}/{index}: {field} must be a string list')

    return {
        'source': f'{skill}#{prefix}#{index}',
        'prompt': prompt,
        'class': prefix,
        'target': skill,
        'primary': primary,
        'acceptable': acceptable,
        'forbidden': forbidden,
    }


def fixture_records(data: dict) -> list[dict]:
    skills = data.get('skills')
    if not isinstance(skills, dict):
        raise ProtocolError('eval cases must contain a skills object')

    records = []
    for skill, cases in skills.items():
        if not isinstance(skill, str) or not isinstance(cases, dict):
            raise ProtocolError('each eval skill must map to an object')
        for bucket, prefix in CASE_BUCKETS:
            raw_cases = cases.get(bucket)
            if not isinstance(raw_cases, list):
                raise ProtocolError(f'{skill}/{bucket} must be a list')
            for index, raw in enumerate(raw_cases):
                records.append(_normalise_fixture(skill, bucket, prefix, index, raw))
    return records


def valid_routes(descriptions: dict[str, str]) -> set[str]:
    return set(descriptions) | VALID_SPECIAL_ROUTES


def new_opaque_id(rng: random.Random, used: set[str]) -> str:
    while True:
        candidate = f'case-{rng.getrandbits(64):016x}'
        if candidate not in used:
            used.add(candidate)
            return candidate


def _assert_fixture_skills_have_descriptions(data: dict, descriptions: dict[str, str]) -> None:
    missing = sorted(set(data['skills']) - set(descriptions))
    if missing:
        raise ProtocolError(f'eval skills missing descriptions: {", ".join(missing)}')


def gen(out: Path, mapping: Path, seed: int) -> int:
    data = load_eval_cases()
    descriptions = load_descriptions()
    _assert_fixture_skills_have_descriptions(data, descriptions)
    records = fixture_records(data)

    if out.resolve() == mapping.resolve():
        raise ProtocolError('judge input and scoring map must be different files')

    rng = random.Random(seed)
    used_ids = set()
    mapped_records = []
    for record in records:
        mapped = dict(record)
        mapped['id'] = new_opaque_id(rng, used_ids)
        mapped_records.append(mapped)

    public_records = list(mapped_records)
    rng.shuffle(public_records)

    public_payload = {
        'format_version': PUBLIC_FORMAT_VERSION,
        'descriptions': descriptions,
        'prompts': [
            {'id': record['id'], 'prompt': record['prompt']}
            for record in public_records
        ],
    }
    mapping_payload = {
        'format_version': MAPPING_FORMAT_VERSION,
        'fixture_version': data.get('version'),
        'seed': seed,
        'cases': mapped_records,
    }
    write_json(out, public_payload)
    write_json(mapping, mapping_payload)
    print(
        f'Wrote {len(public_records)} prompts for {len(descriptions)} skills to {out}'
    )
    print(f'Wrote private scoring map to {mapping}')
    return 0


def _validate_string_list(value, field: str, label: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        errors.append(f'{label}: {field} must be a string list')


def load_scoring_map(
    path: Path,
    data: dict,
    descriptions: dict[str, str],
) -> tuple[list[dict], list[str]]:
    try:
        payload = read_json(path)
    except ProtocolError as e:
        return [], [str(e)]

    errors = []
    if not isinstance(payload, dict):
        return [], [f'{path}: scoring map must be a JSON object']
    if payload.get('format_version') != MAPPING_FORMAT_VERSION:
        errors.append(f'{path}: unsupported scoring map format_version')
    if not isinstance(payload.get('seed'), int) or isinstance(payload.get('seed'), bool):
        errors.append(f'{path}: seed must be an integer')
    if payload.get('fixture_version') != data.get('version'):
        errors.append(f'{path}: fixture_version does not match eval_cases.yaml')

    raw_cases = payload.get('cases')
    if not isinstance(raw_cases, list):
        return [], errors + [f'{path}: cases must be a list']

    fixture_by_source = {record['source']: record for record in fixture_records(data)}
    allowed_routes = valid_routes(descriptions)
    seen_ids = set()
    seen_sources = set()
    cases = []

    for position, raw in enumerate(raw_cases):
        label = f'{path}: cases[{position}]'
        if not isinstance(raw, dict):
            errors.append(f'{label} must be an object')
            continue

        case_id = raw.get('id')
        if not isinstance(case_id, str) or not OPAQUE_ID_RE.fullmatch(case_id):
            errors.append(f'{label}: id is not an opaque case id')
        elif case_id in seen_ids:
            errors.append(f'{label}: duplicate case id {case_id}')
        else:
            seen_ids.add(case_id)

        source = raw.get('source')
        expected = fixture_by_source.get(source) if isinstance(source, str) else None
        if expected is None:
            errors.append(f'{label}: unknown source fixture {source!r}')
        elif source in seen_sources:
            errors.append(f'{label}: duplicate source fixture {source}')
        else:
            seen_sources.add(source)

        primary = raw.get('primary')
        if primary is not None and not isinstance(primary, str):
            errors.append(f'{label}: primary must be a string or null')
        for field in ('acceptable', 'forbidden'):
            _validate_string_list(raw.get(field), field, label, errors)

        case_class = raw.get('class')
        if not isinstance(case_class, str) or case_class not in CASE_CLASSES:
            errors.append(f'{label}: class must be one of {sorted(CASE_CLASSES)}')
        for field in ('target', 'primary'):
            value = raw.get(field)
            if value is not None and (
                not isinstance(value, str) or value not in allowed_routes
            ):
                errors.append(f'{label}: {field} contains an unknown route {value!r}')
        for field in ('acceptable', 'forbidden'):
            values = raw.get(field)
            if isinstance(values, list):
                for value in values:
                    if value not in allowed_routes:
                        errors.append(
                            f'{label}: {field} contains an unknown route {value!r}'
                        )

        if expected is not None:
            for field in (
                'prompt',
                'class',
                'target',
                'primary',
                'acceptable',
                'forbidden',
            ):
                if raw.get(field) != expected[field]:
                    errors.append(f'{label}: {field} does not match source fixture')

        if isinstance(case_id, str) and OPAQUE_ID_RE.fullmatch(case_id):
            cases.append(raw)

    missing_sources = set(fixture_by_source) - seen_sources
    if missing_sources:
        errors.append(f'{path}: missing {len(missing_sources)} source fixtures')
    if len(cases) != len(fixture_by_source):
        errors.append(
            f'{path}: expected {len(fixture_by_source)} mapped cases, found {len(cases)}'
        )
    return cases, errors


def collect_routes(
    paths: list[Path],
    expected_ids: set[str],
    allowed_routes: set[str],
) -> tuple[dict[str, str], list[str]]:
    routes = {}
    seen_ids = set()
    errors = []

    for path in paths:
        try:
            payload = read_json(path)
        except ProtocolError as e:
            errors.append(str(e))
            continue
        if not isinstance(payload, dict):
            errors.append(f'{path}: judge output must be a JSON object')
            continue

        for case_id, route in payload.items():
            label = f'{path}: {case_id!r}'
            if case_id in seen_ids:
                errors.append(f'{label}: duplicate id across judge outputs')
            seen_ids.add(case_id)
            if case_id not in expected_ids:
                errors.append(f'{label}: unknown judge id')
            if not isinstance(route, str) or route not in allowed_routes:
                errors.append(f'{label}: invalid route {route!r}')
            routes[case_id] = route

    missing = expected_ids - seen_ids
    if missing:
        sample = ', '.join(sorted(missing)[:3])
        suffix = '...' if len(missing) > 3 else ''
        errors.append(f'missing {len(missing)} expected judge ids ({sample}{suffix})')
    return routes, errors


def print_validation_errors(errors: list[str]) -> None:
    print('VALIDATION FAILED:')
    for error in errors:
        print(f'  - {error}')


def score(mapping_path: Path, paths: list[Path]) -> int:
    data = load_eval_cases()
    descriptions = load_descriptions()
    _assert_fixture_skills_have_descriptions(data, descriptions)
    cases, map_errors = load_scoring_map(mapping_path, data, descriptions)
    if map_errors:
        print_validation_errors(map_errors)
        return 2

    expected_ids = {case['id'] for case in cases}
    routes, output_errors = collect_routes(paths, expected_ids, valid_routes(descriptions))
    if output_errors:
        print_validation_errors(output_errors)
        return 2

    st_hit = st_tot = sn_hit = sn_tot = 0
    for case in cases:
        case_id = case['id']
        route = routes[case_id]
        case_class = case['class']
        source = case['source']
        prompt = case['prompt']
        if case_class == 'ST':
            st_tot += 1
            hit = route in case['acceptable']
            st_hit += hit
            if not hit:
                expected = ', '.join(case['acceptable'])
                print(f'  ST miss {source}: route={route} expected one of [{expected}] | {prompt[:60]}')
        elif case_class == 'SN':
            sn_tot += 1
            hit = route not in case['forbidden']
            sn_hit += hit
            if not hit:
                print(f'  SN hit  {source}: route={route} | {prompt[:60]}')
        else:
            print(f'  AM {route:>22} | {prompt[:50]}')

    print(f'RESULT: should_trigger {st_hit}/{st_tot}  should_not_trigger {sn_hit}/{sn_tot}')
    return 0 if (st_hit == st_tot and sn_hit == sn_tot) else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest='mode', required=True)

    gen_parser = subparsers.add_parser('gen', help='generate blinded judge input')
    gen_parser.add_argument('output', type=Path, help='public judge input JSON')
    gen_parser.add_argument('--map', dest='mapping', type=Path, required=True)
    gen_parser.add_argument('--seed', type=int, required=True)

    score_parser = subparsers.add_parser('score', help='validate and score judge output')
    score_parser.add_argument('--map', dest='mapping', type=Path, required=True)
    score_parser.add_argument('outputs', nargs='+', type=Path)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.mode == 'gen':
            return gen(args.output, args.mapping, args.seed)
        return score(args.mapping, args.outputs)
    except (OSError, ProtocolError, json.JSONDecodeError) as e:
        print(f'ERROR: {e}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
