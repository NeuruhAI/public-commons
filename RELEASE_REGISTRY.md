# Public Commons Release Registry

This registry tracks approved public Neuruh primitives. Each project remains independently versioned, tested, and maintained.

| Release | Repository / Artifact | Version | Class | Status | Purpose |
|---|---|---:|---|---|---|
| 001 | `NeuruhAI/agent-receipt` | 0.1.0 | A — Public Commons | Public / Active Alpha | Portable tamper-evident agent receipt specification and verifier |
| 002 | `specs/SINGLE_WRITER_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Single authoritative writer contract for canonical mutable domains |
| 003 | `specs/EVIDENCE_ENVELOPE_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Portable evidence, provenance, contradiction, uncertainty, and abstention envelope |
| 004 | `failure-lab/` | 0.1 | A — Public Commons | Public / Active Alpha | Synthetic negative-test pack proving invalid contract states are rejected |

## Queue

1. Neuruh Canary Evaluation Ledger
2. Neuruh Rollback Receipt

## Registration rule

A project or specification enters this registry only after ownership, licensing, security, data, public/private boundary, documentation, and validation review are complete and a release receipt exists.

---

## Release Wave 02 — Runnable Components

Wave 02 moves the Public Commons from contracts and test artifacts into
bounded, independently runnable reference components.

### 005 — Neuruh Governed Exec

**Repository:** https://github.com/NeuruhAI/neuruh-governed-exec
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 8/8 tests PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A fail-closed governed command-execution primitive using exact executable +
argv allowlisting, no shell, worktree containment, symlink-escape protection,
environment allowlisting, timeouts, output bounds and dry-run execution.

**Private exclusions:** production command sets, production paths, execution
authority topology, private policies and Neuruh production runtime integration.

### 006 — Neuruh Policy Gate

**Repository:** https://github.com/NeuruhAI/neuruh-policy-gate
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 7/7 tests PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic ALLOW / DENY / ESCALATE action-policy boundary with blocked
domains, tool allowlists, approval tags, spend escalation and content-derived
policy versioning.

**Private exclusions:** production policies, real thresholds, authority maps,
commercial rules and production routing intelligence.

### 007 — Neuruh Capability Registry

**Repository:** https://github.com/NeuruhAI/neuruh-capability-registry
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 7/7 tests PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A typed capability manifest and fail-closed validator for declaring operations,
argument schemas, target types, receipt requirements and preconditions.

**Private exclusions:** Neuruh's production capability map, component ownership,
real authority topology and privileged production capabilities.

### 008 — Neuruh Inference Health

**Repository:** https://github.com/NeuruhAI/neuruh-inference-health
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 7/7 tests PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A provider-neutral health adapter for local-first and mixed inference stacks,
including multi-path probes, backend/model reporting, degraded states and
local-first availability summaries.

**Private exclusions:** production IAR routing, cost optimization, private
fallback rules, credentials, private provider selection and Neuruh inference
authority configuration.

### Wave 02 aggregate qualification

- **4 runnable standalone repositories**
- **29/29 unit tests PASS**
- **4/4 final Git histories gitleaks PASS**
- **4/4 Apache-2.0**
- **4/4 release receipts present**
- **4/4 clean standalone histories**
- **Synthetic examples only**
- **No customer data**
- **No production routing**
- **No proprietary scoring or recipes**
- **No production authority topology**

Wave 02 principle:

> **Open the rails. Protect the routing intelligence.**

---

## Release Wave 03 — Composition

Wave 03 composes the Public Commons primitives into a reproducible governed
agent run and a runnable sovereign reference agent.

### 009 — Neuruh Agent Run Manifest

**Repository:** https://github.com/NeuruhAI/neuruh-agent-run-manifest
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 20/20 tests PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic, content-bound manifest for governed agent runs. It binds
run and actor identity, mission, timestamps, component versions, policy
identity/version, inference state, content-hashed artifacts, evidence,
decisions, execution references, Agent Receipt references and a deterministic
manifest digest.

Validation fails closed on malformed hashes, unknown fields, duplicate IDs,
broken references, inconsistent policy versions, invalid receipt sequencing,
impossible timestamps, status contradictions and manifest tampering.

**Private exclusions:** production routing, production authority topology,
private prompts/policies/memory, proprietary scoring/recipes, customer data
and private connectors.

### 010 — Neuruh Sovereign Agent Starter

**Repository:** https://github.com/NeuruhAI/neuruh-sovereign-agent-starter
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 22/22 tests PASS; synthetic governed E2E PASS; generated Release 009 manifest independently validates; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A runnable governed-agent reference stack composed from Agent Receipt,
Governed Exec, Policy Gate, Capability Registry, Inference Health and Agent
Run Manifest.

Critical safety property:

> **Model output is evidence, never command authority.**

Execution is restricted to an exact operator-declared executable + argv
binding after capability validation and policy evaluation. DENY and ESCALATE
do not execute. v0.1 inference is loopback-only.

**Private exclusions:** AXON, AEGIS/IAR, Governance Core, Mother/Father,
LandOS, Recipe Engine, DeedSonar, production authority topology, private
routing, private prompts/policies/memory and proprietary scoring.

### Wave 03 aggregate qualification

- **2 independently runnable Public Commons packages**
- **42/42 unit tests PASS**
- **Synthetic governed E2E PASS**
- **E2E Release 009 manifest independently verified**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **No private organism implementation exported**

Wave 03 advances the Public Commons from standalone runnable primitives into
a composed governed reference runtime.

---

## Release Wave 04 — Evidence + Connector Contracts

Wave 04 adds a tamper-evident evidence custody primitive and a fail-closed
connector contract-testing primitive to the Public Commons.

### 011 — Neuruh Evidence Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-evidence-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 28/28 tests PASS; Wave 04 composition E2E PASS; final Git-history gitleaks PASS; wheel build PASS; CLI smoke PASS; Apache-2.0; release receipt present.

An append-only, tamper-evident ledger for evidence objects and their
provenance/custody graph.

It preserves sequence, content hashes, provenance, contradictions,
derivation, supersession and ledger-tip integrity while keeping evidence
separate from execution/governance authority.

**Private exclusions:** production evidence stores, private datasets,
customer data, credentials, production source topology, proprietary
confidence calibration and private routing intelligence.

### 012 — Neuruh Connector Contract Kit

**Repository:** https://github.com/NeuruhAI/neuruh-connector-contract-kit
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 29/29 tests PASS; Wave 04 composition E2E PASS; final Git-history gitleaks PASS; wheel build PASS; CLI smoke PASS; Apache-2.0; release receipt present.

A portable fail-closed contract-testing framework for connectors.

It mechanically validates declared operations, inputs, outputs, side effects,
network requirements, allowed hosts, authentication declarations, timeouts,
retry bounds, idempotency and evidence/receipt requirements using synthetic
adapters.

**Private exclusions:** production Neuruh connectors, credentials, production
endpoints, DeedSonar/LandOS private APIs, connector routing, customer data and
production authority topology.

### Wave 04 aggregate qualification

- **57/57 unit tests PASS**
- **011: 28/28 PASS**
- **012: 29/29 PASS**
- **012 → 011 → exact public 009 composition E2E PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 04 extends the governed reference runtime with evidence custody and
connector-boundary verification.

---

## Release Wave 05 — Explainability + Human Authority

Wave 05 makes governed decisions auditable without exposing chain-of-thought, then binds human approval to one exact decision/evidence/policy/run state.

### 013 — Neuruh Decision Explainability

**Repository:** https://github.com/NeuruhAI/neuruh-decision-explainability
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 36/36 tests PASS; exact public Wave 05 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound audit explanation recording the chosen decision, declared policy reasons, hashed evidence used/excluded, rejected alternatives and limitations. It does not request, store or reconstruct hidden model chain-of-thought.

**Private exclusions:** chain-of-thought, model scratchpads, private prompts/policies, production thresholds, proprietary scoring, customer data, routing and authority topology.

### 014 — Neuruh Human Approval Checkpoint

**Repository:** https://github.com/NeuruhAI/neuruh-human-approval-checkpoint
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 38/38 tests PASS; exact public Wave 05 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A fail-closed human approval record bound to exact run/action identity, decision digest, policy version, evidence digest, authorized approver set, required authority and expiry. Changed state, stale approvals, unauthorized approvers and replay attempts fail closed.

**Private exclusions:** real employee identities, production RBAC/authority topology, credentials, production approval routing, customer data, private policies and execution systems.

### Wave 05 aggregate qualification

- **74/74 unit tests PASS**
- **Exact public 006 Policy Gate → 013 → 014 → 009 Agent Run Manifest composition E2E PASS**
- **Pre-approval authorization blocked; exact post-approval state authorized**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**
---

## Release Wave 06 — Decision Receipts + Delegated Authority

Wave 06 binds the complete auditable anatomy of one governed decision and adds a mechanically bounded authority delegation contract.

### 015 — Neuruh Decision Receipt

**Repository:** https://github.com/NeuruhAI/neuruh-decision-receipt
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 45/45 tests PASS; exact public Wave 06 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound receipt spanning identity, evidence, declared reasoning artifacts, governance, execution, economics and outcome. It references Decision Explainability, Human Approval, Authority Delegation and optional Agent Receipt hashes without conflating evidence with authority.

**Private exclusions:** hidden chain-of-thought, production economics/scoring logic, private policies, customer data, production routing, production authority topology and private connectors.

### 016 — Neuruh Authority Delegation Contract

**Repository:** https://github.com/NeuruhAI/neuruh-authority-delegation-contract
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 44/44 tests PASS; exact public Wave 06 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A fail-closed authority contract binding principal, delegate, authority classes, capabilities, domains, optional action IDs, time window, spend ceiling and delegation depth. Child delegations must be strict subsets of their parent and revoked/expired/out-of-scope authority fails closed.

**Private exclusions:** production RBAC, real employee identities, cryptographic key material, credentials, production authority graph, private approval routing and private commercial thresholds.

### Wave 06 aggregate qualification

- **89/89 unit tests PASS**
- **015: 45/45 PASS**
- **016: 44/44 PASS**
- **Exact public 006 → 013 → 016 → 014 → 015 → 009 composition E2E PASS**
- **Delegation authorization PASS**
- **Pre-approval block PASS; exact post-approval authorization PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

---

## Release Wave 07 — Calibration + Reversibility

Wave 07 closes two critical trust loops: it records whether pre-outcome probability forecasts were calibrated after outcomes arrive, and it requires reversibility/compensation claims to be declared before execution.

### 017 — Neuruh Outcome Calibration Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-outcome-calibration-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 57/57 tests PASS; exact public Wave 07 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

An append-only, tamper-evident calibration ledger that binds a genuinely pre-outcome probability forecast to the later Decision Receipt and observed outcome. It deterministically recomputes Brier score, absolute error, probability bucket, ledger chain/tip and aggregate calibration summaries.

Critical boundary: calibration evidence can measure error but cannot modify models, policies, thresholds, routing, capabilities or authority.

**Private exclusions:** proprietary scoring, model weights, customer outcomes, domain-specific labels, calibration thresholds, policy promotion rules, model selection, production memory and routing.

### 018 — Neuruh Reversibility Contract

**Repository:** https://github.com/NeuruhAI/neuruh-reversibility-contract
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 54/54 tests PASS; exact public Wave 07 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A content-bound pre-execution contract classifying an action as reversible, compensatable or irreversible. It binds exact forward action/state, reversal or compensation capability and plan, time window, authority class, approval requirements, dependencies, verification requirements and bounded attempts.

Critical boundary: the contract validates whether a declared reversal/compensation path remains eligible; it never executes that path.

**Private exclusions:** production rollback commands, production state stores, credentials, infrastructure topology, real authority routing, private connectors, customer state and commercial recovery logic.

### Wave 07 aggregate qualification

- **111/111 unit tests PASS**
- **017: 57/57 PASS**
- **018: 54/54 PASS**
- **Exact public 006 → 013 → 016 → 014 → 018 → 015 → 017 → 009 composition E2E PASS**
- **Prediction digest proven sealable before final Decision Receipt/outcome**
- **Delegation authorization PASS**
- **Pre-approval block PASS; exact post-approval authorization PASS**
- **Reversal eligibility against exact action/post-state PASS**
- **Calibration Brier/error recomputation PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 07 adds measurable post-outcome calibration and pre-execution reversibility while preserving the rule that evidence does not acquire authority.


---

## Release Wave 08 — Learning Proposals + Promotion Gates

Wave 08 turns calibration evidence into reviewable learning proposals and adds a deterministic lifecycle promotion gate without allowing evidence to mutate production state or acquire deployment authority.

### 019 — Neuruh Learning Update Proposal

**Repository:** https://github.com/NeuruhAI/neuruh-learning-update-proposal
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 47/47 tests PASS; exact public Wave 08 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound proposal that binds exact current/candidate target versions and digests, calibration ledger/summary evidence, sample count, hashed change descriptors and explicit metric projections.

Critical boundary: the proposal can recommend a candidate update but contains no apply, deploy, shell, network, model-update, policy-update or authority-granting path. Human review and Promotion Gate evaluation are mandatory in v0.1.

**Private exclusions:** model weights, private prompts/policies, proprietary scoring and thresholds, customer data, production calibration rules, routing logic and deployment systems.

### 020 — Neuruh Promotion Gate

**Repository:** https://github.com/NeuruhAI/neuruh-promotion-gate
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 49/49 tests PASS; exact public Wave 08 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A fail-closed lifecycle eligibility gate that evaluates proposal identity, target/stage allowlists, calibration sample count, test evidence, regressions, human approval and reversibility evidence and returns PROMOTE, HOLD or BLOCK.

Critical boundary: PROMOTE means eligible to progress to the requested lifecycle stage. Promotion decisions hard-code `deployment_authority=false`; the gate never deploys or mutates a target.

**Private exclusions:** production promotion thresholds, release policy, model selection, production stage routing, credentials, customer data and deployment topology.

### Wave 08 aggregate qualification

- **96/96 unit tests PASS**
- **019: 47/47 PASS**
- **020: 49/49 PASS**
- **Exact public 017 → 019 → 018 → 014 → 020 → 015 → 009 composition E2E PASS**
- **Calibration evidence → proposal binding PASS**
- **Pre-approval Promotion Gate HOLD PASS**
- **Exact human approval binding PASS**
- **Reversibility prerequisite binding PASS**
- **Post-approval Promotion Gate PROMOTE eligibility PASS**
- **Deployment authority remains false PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 08 establishes a bounded learning loop: measure error, propose change, obtain independent prerequisites, and evaluate lifecycle eligibility without self-modification or autonomous deployment.
