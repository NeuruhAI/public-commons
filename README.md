# Neuruh Public Commons

[![ci](https://github.com/NeuruhAI/public-commons/actions/workflows/ci.yml/badge.svg)](https://github.com/NeuruhAI/public-commons/actions/workflows/ci.yml)

Small, inspectable Python libraries for agent execution, policy, receipts, and run identity.

## Start here

The starter composes the public libraries into one governed local run:

```bash
git clone https://github.com/NeuruhAI/neuruh-sovereign-agent-starter.git
cd neuruh-sovereign-agent-starter
python -m venv .venv
source .venv/bin/activate
pip install .
neuruh-sovereign-agent examples/starter.synthetic.json --out-dir run-output
```

```text
RUN COMPLETED: run-87f295783d3e46fb96ab6a7c7e3ce0c0
MANIFEST: run-output/manifest.json
RECEIPTS: run-output/receipts.jsonl
```

The example uses no remote model and needs no API key. It executes one exact predeclared
command in a sandbox and writes a tamper-evident receipt chain and an independently
verifiable run manifest to `run-output/`. Verify them with tools that know nothing about
the agent that produced them:

```bash
neuruh-agent-run-manifest validate run-output/manifest.json   # VALID run-... sha256:...
neuruh-agent-receipt verify run-output/receipts.jsonl         # PASS: 3 receipts
```

Requires Python 3.11 or newer.

## The chain

Each library owns one stage of a single loop, and each stage fails closed when it cannot
prove its inputs:

```text
observation
  -> evidence          what was seen, with provenance
  -> decision          ALLOW / DENY / ESCALATE, deterministically
  -> authority         who permitted this, bounded and single-use
  -> governed execution  exactly one declared command, contained
  -> receipt           tamper-evident proof of what ran
  -> outcome           what actually happened afterwards
  -> calibration       what the system may learn from it
```

## Core libraries

Seven repositories form the runnable path from a mission to a verifiable receipt.
The `Stage` column is that package's position in the chain above.

| Stage | Library | Release | Tests | Purpose |
|---|---|---|---:|---|
| capability | [`neuruh-capability-registry`](https://github.com/NeuruhAI/neuruh-capability-registry) | `v0.1.2-alpha` | 10 PASS | Typed capability manifests; validates operation arguments before anything else runs |
| decision | [`neuruh-policy-gate`](https://github.com/NeuruhAI/neuruh-policy-gate) | `v0.1.2-alpha` | 7 PASS | Deterministic ALLOW / DENY / ESCALATE with content-derived policy versioning |
| inference | [`neuruh-inference-health`](https://github.com/NeuruhAI/neuruh-inference-health) | `v0.1.2-alpha` | 7 PASS | Provider-neutral health checks for local-first and mixed inference stacks |
| execution | [`neuruh-governed-exec`](https://github.com/NeuruhAI/neuruh-governed-exec) | `v0.1.2-alpha` | 8 PASS | Exact-argv, no-shell execution contained inside approved worktrees |
| receipt | [`agent-receipt`](https://github.com/NeuruhAI/agent-receipt) | `v0.1.2-alpha` | 7 PASS | Hash-chained execution receipts and a standalone CLI verifier |
| run identity | [`neuruh-agent-run-manifest`](https://github.com/NeuruhAI/neuruh-agent-run-manifest) | `v0.1.2-alpha` | 20 PASS | Content-bound run manifests that can be validated independently |
| composition | [`neuruh-sovereign-agent-starter`](https://github.com/NeuruhAI/neuruh-sovereign-agent-starter) | `v0.1.1-alpha` | 23 PASS | Runnable composition of the six libraries above |

Each repository is independently versioned, tested, and installable. The core rule is
simple: **model output is evidence, never command authority.**

## Advanced protocol

The later packages are building blocks for teams implementing a governed promotion
lifecycle. They are protocol components, not dependencies of the starter — install only
the ones you need.

**Evidence and human authority**

| Stage | Package | Release | Tests |
|---|---|---|---:|
| evidence | [`neuruh-evidence-ledger`](https://github.com/NeuruhAI/neuruh-evidence-ledger) | `v0.1.1-alpha` | 30 PASS |
| evidence | [`neuruh-connector-contract-kit`](https://github.com/NeuruhAI/neuruh-connector-contract-kit) | `v0.1.1-alpha` | 29 PASS |
| decision | [`neuruh-decision-explainability`](https://github.com/NeuruhAI/neuruh-decision-explainability) | `v0.1.1-alpha` | 36 PASS |
| decision | [`neuruh-decision-receipt`](https://github.com/NeuruhAI/neuruh-decision-receipt) | `v0.1.1-alpha` | 45 PASS |
| authority | [`neuruh-human-approval-checkpoint`](https://github.com/NeuruhAI/neuruh-human-approval-checkpoint) | `v0.1.1-alpha` | 38 PASS |
| authority | [`neuruh-authority-delegation-contract`](https://github.com/NeuruhAI/neuruh-authority-delegation-contract) | `v0.1.1-alpha` | 44 PASS |

**Learning and promotion**

| Stage | Package | Release | Tests |
|---|---|---|---:|
| outcome | [`neuruh-outcome-calibration-ledger`](https://github.com/NeuruhAI/neuruh-outcome-calibration-ledger) | `v0.1.1-alpha` | 57 PASS |
| execution | [`neuruh-reversibility-contract`](https://github.com/NeuruhAI/neuruh-reversibility-contract) | `v0.1.1-alpha` | 54 PASS |
| calibration | [`neuruh-learning-update-proposal`](https://github.com/NeuruhAI/neuruh-learning-update-proposal) | `v0.1.1-alpha` | 47 PASS |
| promotion | [`neuruh-promotion-gate`](https://github.com/NeuruhAI/neuruh-promotion-gate) | `v0.1.1-alpha` | 49 PASS |

**Canary and deployment lifecycle**

| Stage | Package | Release | Tests |
|---|---|---|---:|
| promotion | [`neuruh-canary-evaluation-ledger`](https://github.com/NeuruhAI/neuruh-canary-evaluation-ledger) | `v0.1.1-alpha` | 56 PASS |
| promotion | [`neuruh-rollback-receipt`](https://github.com/NeuruhAI/neuruh-rollback-receipt) | `v0.1.1-alpha` | 43 PASS |
| authority | [`neuruh-deployment-authorization-contract`](https://github.com/NeuruhAI/neuruh-deployment-authorization-contract) | `v0.1.1-alpha` | 57 PASS |
| promotion | [`neuruh-stage-transition-receipt`](https://github.com/NeuruhAI/neuruh-stage-transition-receipt) | `v0.1.1-alpha` | 49 PASS |
| authority | [`neuruh-authorization-consumption-ledger`](https://github.com/NeuruhAI/neuruh-authorization-consumption-ledger) | `v0.1.1-alpha` | 54 PASS |
| promotion | [`neuruh-lifecycle-state-ledger`](https://github.com/NeuruhAI/neuruh-lifecycle-state-ledger) | `v0.1.1-alpha` | 75 PASS |

**Canonical-state reconciliation**

| Stage | Package | Release | Tests |
|---|---|---|---:|
| execution | [`neuruh-execution-intent-manifest`](https://github.com/NeuruhAI/neuruh-execution-intent-manifest) | `v0.1.1-alpha` | 72 PASS |
| reconciliation | [`neuruh-state-attestation-envelope`](https://github.com/NeuruhAI/neuruh-state-attestation-envelope) | `v0.1.1-alpha` | 55 PASS |
| reconciliation | [`neuruh-state-drift-ledger`](https://github.com/NeuruhAI/neuruh-state-drift-ledger) | `v0.1.1-alpha` | 60 PASS |
| reconciliation | [`neuruh-reconciliation-proposal`](https://github.com/NeuruhAI/neuruh-reconciliation-proposal) | `v0.1.1-alpha` | 62 PASS |
| reconciliation | [`neuruh-reconciliation-authorization-contract`](https://github.com/NeuruhAI/neuruh-reconciliation-authorization-contract) | `v0.1.1-alpha` | 27 PASS |
| reconciliation | [`neuruh-reconciliation-receipt`](https://github.com/NeuruhAI/neuruh-reconciliation-receipt) | `v0.1.1-alpha` | 22 PASS |

**Canonical revision memory and effective truth**

| Stage | Package | Release | Tests |
|---|---|---|---:|
| reconciliation | [`neuruh-canonical-state-revision-authorization-contract`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-authorization-contract) | `v0.1.2-alpha` | 29 PASS |
| reconciliation | [`neuruh-canonical-state-revision-ledger`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-ledger) | `v0.1.0-alpha` | 35 PASS |
| reconciliation | [`neuruh-canonical-state-revision-receipt`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-receipt) | `v0.1.2-alpha` | 29 PASS |
| reconciliation | [`neuruh-effective-canonical-state-resolver`](https://github.com/NeuruhAI/neuruh-effective-canonical-state-resolver) | `v0.1.0-alpha` | 33 PASS |

See [`RELEASE_REGISTRY.md`](RELEASE_REGISTRY.md) for the complete compatibility and qualification record, including what each package excludes. These packages are protocol components, not required dependencies for the starter.

## Maturity and dependencies

Every package here is **Active Alpha**: released, tested, and used, but the interfaces are
still moving. Pin the tag. `RELEASE_REGISTRY.md` records the qualification evidence and the
status vocabulary behind that label.

**32 of the 33 Python packages declare zero runtime dependencies.** They are standard
library only, which is why they can be read end to end and dropped into an existing stack
without pulling a tree behind them. The one exception is
`neuruh-sovereign-agent-starter`, whose six dependencies are the core libraries above,
each pinned to an immutable tag.

Test totals in the tables above were produced by running each repository's own suite
(`python -m unittest discover -s tests`): **1,269 tests across the 33 Python packages, all
passing.** `notion-auto-exporter` adds 16 Node tests. Every repository runs the same suite
in CI on push and pull request.

## Installing a pinned release

Every package installs from an immutable tag. Nothing here resolves to a branch:

```bash
pip install "neuruh-governed-exec @ git+https://github.com/NeuruhAI/neuruh-governed-exec.git@v0.1.2-alpha"
```

[`scripts/verify_index.py`](scripts/verify_index.py) re-checks every repository, tag and version
this index advertises against GitHub, and exits nonzero if any of them has drifted.

## Verifying this repository

```bash
pip install jsonschema
python3 scripts/verify_failure_lab.py            # invalid fixtures must be rejected
python3 scripts/verify_estate_wave_01_contracts.py
python3 scripts/verify_index.py                  # every advertised tag and version exists
```

The first two need no network. `verify_index.py` queries GitHub, and uses the GitHub CLI when
it is available to also check package versions and releases.

## Public boundary

Public artifacts use synthetic fixtures and contain no customer data, production credentials, commercial recipes, vertical scoring, private prompts, privileged connectors, or production routing. The complete rules are in [`PUBLIC_PRIVATE_BOUNDARY.md`](PUBLIC_PRIVATE_BOUNDARY.md).

## Other public tools

Not part of the Commons protocol, but published under the same account and boundary rules:

| Repository | Release | Purpose |
|---|---|---|
| [`nimdp-validator`](https://github.com/NeuruhAI/nimdp-validator) | `v1.0.0` | Launch-readiness scoring of a specification against a token map, usable as a CI gate |
| [`notion-auto-exporter`](https://github.com/NeuruhAI/notion-auto-exporter) | `v1.0.1` | Exports checked Notion pages to markdown, organised by section, for RAG upload |

`notion-auto-exporter` carries 16 unit tests. `nimdp-validator` has no unit-test suite on
`main`; its CI runs the validator against a sample specification as a smoke gate. Neither
is on the Commons release track, and neither is a dependency of anything above.

## Project documents

- [`CHARTER.md`](CHARTER.md)
- [`PUBLIC_PRIVATE_BOUNDARY.md`](PUBLIC_PRIVATE_BOUNDARY.md)
- [`SECURITY.md`](SECURITY.md)
- [`DATA_RELEASE_POLICY.md`](DATA_RELEASE_POLICY.md)
- [`RELEASE_REGISTRY.md`](RELEASE_REGISTRY.md)

Apache-2.0. See [`LICENSE`](LICENSE).
