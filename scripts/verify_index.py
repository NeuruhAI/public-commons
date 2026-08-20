#!/usr/bin/env python3
"""Check that every repository, tag and version this index advertises actually exists.

Reads README.md and RELEASE_REGISTRY.md, extracts every NeuruhAI repository and the
release tag claimed for it, and verifies against GitHub that:

  * the repository is public;
  * the tag exists on the remote;
  * the package version at that tag matches the version the registry claims;
  * a GitHub release exists for the tag.

Exits 0 when the index is accurate, 1 otherwise. Needs only git and network access;
the GitHub CLI is used when available for the release and version checks.

    python3 scripts/verify_index.py
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_TAG = re.compile(
    r"https://github\.com/NeuruhAI/([A-Za-z0-9_.\-]+)\)?\s*\|?\s*`(v[0-9][^`]*)`"
)
REGISTRY_ENTRY = re.compile(
    r"\*\*Repository:\*\* https://github\.com/NeuruhAI/([A-Za-z0-9_.\-]+)\s*\n"
    r"\*\*Version:\*\* `([^`]+)` / Python `([^`]+)`"
)


def advertised() -> dict[str, dict[str, str]]:
    claims: dict[str, dict[str, str]] = {}
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for repo, tag in REPO_TAG.findall(readme):
        claims.setdefault(repo, {})["tag"] = tag
    registry = (ROOT / "RELEASE_REGISTRY.md").read_text(encoding="utf-8")
    for repo, tag, version in REGISTRY_ENTRY.findall(registry):
        entry = claims.setdefault(repo, {})
        if entry.get("tag") and entry["tag"] != tag:
            entry["conflict"] = f'README says {entry["tag"]}, registry says {tag}'
        entry["tag"] = tag
        entry["version"] = version
    return claims


def remote_tags(repo: str) -> set[str]:
    out = subprocess.run(
        ["git", "ls-remote", "--tags", f"https://github.com/NeuruhAI/{repo}.git"],
        capture_output=True, text=True,
    ).stdout
    return {
        line.split("refs/tags/")[1]
        for line in out.splitlines()
        if "refs/tags/" in line and not line.endswith("^{}")
    }


def gh(*args: str) -> str | None:
    if not shutil.which("gh"):
        return None
    done = subprocess.run(["gh", *args], capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else None


def package_version(repo: str, tag: str) -> str | None:
    body = gh("api", f"repos/NeuruhAI/{repo}/contents/pyproject.toml?ref={tag}",
              "-H", "Accept: application/vnd.github.raw")
    if body is None:
        return None
    found = re.search(r'(?m)^version\s*=\s*"([^"]+)"', body)
    return found.group(1) if found else None


def main() -> int:
    claims = advertised()
    if not claims:
        print("error: no advertised repositories found", file=sys.stderr)
        return 1

    problems: list[str] = []
    for repo in sorted(claims):
        claim = claims[repo]
        tag = claim.get("tag")
        if "conflict" in claim:
            problems.append(f"{repo}: {claim['conflict']}")
        tags = remote_tags(repo)
        if not tags:
            problems.append(f"{repo}: no tags on the remote, or the repository is not public")
            print(f"FAIL {repo}")
            continue
        if tag not in tags:
            problems.append(f"{repo}: advertised tag {tag} does not exist")
            print(f"FAIL {repo} {tag}")
            continue

        detail = []
        claimed_version = claim.get("version")
        if claimed_version:
            actual = package_version(repo, tag)
            if actual is None:
                detail.append("version unchecked")
            elif actual != claimed_version:
                problems.append(
                    f"{repo}: registry claims Python {claimed_version} at {tag}, tag has {actual}"
                )
                print(f"FAIL {repo} {tag}")
                continue
            else:
                detail.append(f"python {actual}")

        releases = gh("release", "list", "-R", f"NeuruhAI/{repo}",
                      "--limit", "50", "--json", "tagName", "-q", ".[].tagName")
        if releases is None:
            detail.append("release unchecked")
        elif tag in releases.split():
            detail.append("release present")
        else:
            problems.append(f"{repo}: no GitHub release for {tag}")
            print(f"FAIL {repo} {tag}")
            continue

        print(f"ok   {repo} {tag}" + (f"  ({', '.join(detail)})" if detail else ""))

    print()
    if problems:
        print(f"{len(problems)} problem(s):")
        for line in problems:
            print(f"  - {line}")
        return 1
    print(f"index is accurate: {len(claims)} repositories verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
