# Changelog

## 2026-08-20 — index accuracy and release hygiene

- Releases 035 (Canonical State Revision Ledger) and 036 (Effective Canonical State Resolver)
  are published and registered. The queue is now empty.
- Every version and tag in `RELEASE_REGISTRY.md` and `README.md` was refreshed from the remotes.
  Both documents now name an exact immutable tag for every repository they advertise.
- `scripts/verify_index.py` checks that every repository, tag and version this index advertises
  actually exists, and that a GitHub release accompanies each tag. It runs in CI, including
  weekly, so the index cannot drift silently.
- `scripts/verify_failure_lab.py` runs the Release 004 negative-test pack against the published
  schemas. The pack previously declared expected rejections without anything that proved them;
  each fixture is now shown to fail for its declared reason, and both positive examples are shown
  to validate.
- Continuous integration added: contract and failure-lab checks on Python 3.11, 3.12 and 3.13,
  plus the index check.
- Removed `LICENSE_DECISION_REQUIRED.md`. The repository is public and Apache-2.0; the file was
  stale staging scaffolding that contradicted `LICENSE`.
