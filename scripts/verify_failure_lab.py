#!/usr/bin/env python3
"""Run the failure lab: every listed fixture must fail its contract, and every
positive example must pass.

Release 004 asserts that invalid contract states are rejected. This script proves
it rather than leaving the claim to the reader. It validates each fixture in
`failure-lab/manifest.json` against the JSON Schema named there and against the
positive examples in `examples/`.

    pip install jsonschema
    python3 scripts/verify_failure_lab.py

Exits 0 when every expectation holds, 1 otherwise. Passing an invalid fixture is a
regression, and so is rejecting a valid example.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:  # pragma: no cover - reported, not raised
    print(
        "error: jsonschema is required (pip install jsonschema)",
        file=sys.stderr,
    )
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
POSITIVE = {
    "examples/single-writer.synthetic.json": "schemas/single-writer.v0.1.schema.json",
    "examples/evidence-envelope.synthetic.json": "schemas/evidence-envelope.v0.1.schema.json",
}


def errors_for(document: Path, schema: Path) -> list[str]:
    validator = Draft202012Validator(
        json.loads(schema.read_text(encoding="utf-8")),
        format_checker=FormatChecker(),
    )
    return [
        f"{'/'.join(str(x) for x in e.path) or '<root>'}: {e.message}"
        for e in validator.iter_errors(json.loads(document.read_text(encoding="utf-8")))
    ]


def main() -> int:
    manifest = json.loads((ROOT / "failure-lab" / "manifest.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    checked = 0

    for fixture in manifest["fixtures"]:
        document = ROOT / "failure-lab" / fixture["path"]
        schema = ROOT / fixture["contract"]
        if not document.exists():
            problems.append(f"{fixture['path']}: fixture is missing")
            continue
        if not schema.exists():
            problems.append(f"{fixture['path']}: contract {fixture['contract']} is missing")
            continue
        found = errors_for(document, schema)
        checked += 1
        if fixture["expected"] == "reject":
            if found:
                print(f"ok   reject   {fixture['path']}  ({found[0]})")
            else:
                problems.append(
                    f"{fixture['path']}: expected rejection ({fixture['reason']}) but it validated"
                )
                print(f"FAIL reject   {fixture['path']}")
        else:
            if found:
                problems.append(f"{fixture['path']}: expected acceptance but got {found[0]}")
                print(f"FAIL accept   {fixture['path']}")
            else:
                print(f"ok   accept   {fixture['path']}")

    for example, contract in POSITIVE.items():
        document, schema = ROOT / example, ROOT / contract
        if not document.exists() or not schema.exists():
            problems.append(f"{example}: example or contract is missing")
            continue
        found = errors_for(document, schema)
        checked += 1
        if found:
            problems.append(f"{example}: valid example was rejected: {found[0]}")
            print(f"FAIL accept   {example}")
        else:
            print(f"ok   accept   {example}")

    print()
    if problems:
        print(f"{len(problems)} problem(s):")
        for line in problems:
            print(f"  - {line}")
        return 1
    print(f"failure lab holds: {checked} document(s) behaved as declared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
