# Neuruh Public Commons

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

The example uses no remote model. It executes one exact predeclared command in a sandbox and writes a tamper-evident receipt chain and independently verifiable run manifest to `run-output/`.

## Core libraries

| Library | Release | Purpose |
|---|---|---|
| [`agent-receipt`](https://github.com/NeuruhAI/agent-receipt) | `v0.1.2-alpha` | Hash-chained execution receipts and a CLI verifier |
| [`neuruh-governed-exec`](https://github.com/NeuruhAI/neuruh-governed-exec) | `v0.1.2-alpha` | Exact-argv, no-shell execution inside approved worktrees |
| [`neuruh-policy-gate`](https://github.com/NeuruhAI/neuruh-policy-gate) | `v0.1.2-alpha` | Deterministic `ALLOW`, `DENY`, and `ESCALATE` decisions |
| [`neuruh-capability-registry`](https://github.com/NeuruhAI/neuruh-capability-registry) | `v0.1.2-alpha` | Typed capability manifests and fail-closed argument validation |
| [`neuruh-inference-health`](https://github.com/NeuruhAI/neuruh-inference-health) | `v0.1.2-alpha` | Provider-neutral health checks for local and mixed inference |
| [`neuruh-agent-run-manifest`](https://github.com/NeuruhAI/neuruh-agent-run-manifest) | `v0.1.2-alpha` | Content-bound run manifests that can be independently verified |
| [`neuruh-sovereign-agent-starter`](https://github.com/NeuruhAI/neuruh-sovereign-agent-starter) | `v0.1.1-alpha` | Runnable composition of the six libraries above |

Each repository is independently versioned, tested, and installable. The core rule is simple: **model output is evidence, never command authority.**

## Advanced protocol

The later libraries are building blocks for teams implementing a governed promotion lifecycle:

- **Evidence and human authority:** evidence ledger, connector contracts, decision explainability, human approval, decision receipts, and delegated authority.
- **Learning and promotion:** outcome calibration, reversibility, learning proposals, and promotion gates.
- **Canary and deployment lifecycle:** canary evaluation, rollback receipts, deployment authorization, stage-transition receipts, authorization consumption, and lifecycle state.
- **Canonical-state reconciliation:** execution intent, state attestation, drift detection, reconciliation, and canonical-state revision receipts.
- **Canonical revision memory and effective truth:** a hash-chained revision lineage anchored to one lifecycle entry, and a deterministic resolver that projects one effective canonical state from that lineage — or fails closed as `ambiguous` rather than guessing.

| Package | Release |
|---|---|
| [`neuruh-authority-delegation-contract`](https://github.com/NeuruhAI/neuruh-authority-delegation-contract) | `v0.1.1-alpha` |
| [`neuruh-authorization-consumption-ledger`](https://github.com/NeuruhAI/neuruh-authorization-consumption-ledger) | `v0.1.1-alpha` |
| [`neuruh-canary-evaluation-ledger`](https://github.com/NeuruhAI/neuruh-canary-evaluation-ledger) | `v0.1.1-alpha` |
| [`neuruh-canonical-state-revision-authorization-contract`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-authorization-contract) | `v0.1.2-alpha` |
| [`neuruh-canonical-state-revision-ledger`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-ledger) | `v0.1.0-alpha` |
| [`neuruh-canonical-state-revision-receipt`](https://github.com/NeuruhAI/neuruh-canonical-state-revision-receipt) | `v0.1.2-alpha` |
| [`neuruh-connector-contract-kit`](https://github.com/NeuruhAI/neuruh-connector-contract-kit) | `v0.1.1-alpha` |
| [`neuruh-decision-explainability`](https://github.com/NeuruhAI/neuruh-decision-explainability) | `v0.1.1-alpha` |
| [`neuruh-decision-receipt`](https://github.com/NeuruhAI/neuruh-decision-receipt) | `v0.1.1-alpha` |
| [`neuruh-deployment-authorization-contract`](https://github.com/NeuruhAI/neuruh-deployment-authorization-contract) | `v0.1.1-alpha` |
| [`neuruh-effective-canonical-state-resolver`](https://github.com/NeuruhAI/neuruh-effective-canonical-state-resolver) | `v0.1.0-alpha` |
| [`neuruh-evidence-ledger`](https://github.com/NeuruhAI/neuruh-evidence-ledger) | `v0.1.1-alpha` |
| [`neuruh-execution-intent-manifest`](https://github.com/NeuruhAI/neuruh-execution-intent-manifest) | `v0.1.1-alpha` |
| [`neuruh-human-approval-checkpoint`](https://github.com/NeuruhAI/neuruh-human-approval-checkpoint) | `v0.1.1-alpha` |
| [`neuruh-learning-update-proposal`](https://github.com/NeuruhAI/neuruh-learning-update-proposal) | `v0.1.1-alpha` |
| [`neuruh-lifecycle-state-ledger`](https://github.com/NeuruhAI/neuruh-lifecycle-state-ledger) | `v0.1.1-alpha` |
| [`neuruh-outcome-calibration-ledger`](https://github.com/NeuruhAI/neuruh-outcome-calibration-ledger) | `v0.1.1-alpha` |
| [`neuruh-promotion-gate`](https://github.com/NeuruhAI/neuruh-promotion-gate) | `v0.1.1-alpha` |
| [`neuruh-reconciliation-authorization-contract`](https://github.com/NeuruhAI/neuruh-reconciliation-authorization-contract) | `v0.1.1-alpha` |
| [`neuruh-reconciliation-proposal`](https://github.com/NeuruhAI/neuruh-reconciliation-proposal) | `v0.1.1-alpha` |
| [`neuruh-reconciliation-receipt`](https://github.com/NeuruhAI/neuruh-reconciliation-receipt) | `v0.1.1-alpha` |
| [`neuruh-reversibility-contract`](https://github.com/NeuruhAI/neuruh-reversibility-contract) | `v0.1.1-alpha` |
| [`neuruh-rollback-receipt`](https://github.com/NeuruhAI/neuruh-rollback-receipt) | `v0.1.1-alpha` |
| [`neuruh-stage-transition-receipt`](https://github.com/NeuruhAI/neuruh-stage-transition-receipt) | `v0.1.1-alpha` |
| [`neuruh-state-attestation-envelope`](https://github.com/NeuruhAI/neuruh-state-attestation-envelope) | `v0.1.1-alpha` |
| [`neuruh-state-drift-ledger`](https://github.com/NeuruhAI/neuruh-state-drift-ledger) | `v0.1.1-alpha` |

See [`RELEASE_REGISTRY.md`](RELEASE_REGISTRY.md) for the complete compatibility and qualification record, including what each package excludes. These packages are protocol components, not required dependencies for the starter.

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

## Project documents

- [`CHARTER.md`](CHARTER.md)
- [`PUBLIC_PRIVATE_BOUNDARY.md`](PUBLIC_PRIVATE_BOUNDARY.md)
- [`SECURITY.md`](SECURITY.md)
- [`DATA_RELEASE_POLICY.md`](DATA_RELEASE_POLICY.md)
- [`RELEASE_REGISTRY.md`](RELEASE_REGISTRY.md)

Apache-2.0. See [`LICENSE`](LICENSE).
