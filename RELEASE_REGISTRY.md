# Public Commons Release Registry

This registry tracks approved public Neuruh primitives. Each project remains independently versioned, tested, and maintained.

| Release | Repository / Artifact | Version | Class | Status | Purpose |
|---|---|---:|---|---|---|
| 001 | `NeuruhAI/agent-receipt` | 0.1.0 | A — Public Commons | Public / Active Alpha | Portable tamper-evident agent receipt specification and verifier |
| 002 | `specs/SINGLE_WRITER_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Single authoritative writer contract for canonical mutable domains |
| 003 | `specs/EVIDENCE_ENVELOPE_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Portable evidence, provenance, contradiction, uncertainty, and abstention envelope |
| 004 | `failure-lab/` | 0.1 | A — Public Commons | Public / Active Alpha | Synthetic negative-test pack proving invalid contract states are rejected |

## Queue

1. Neuruh Canonical State Revision Ledger
2. Neuruh Effective Canonical State Resolver

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


---

## Release Wave 09 — Canary Evaluation + Rollback Evidence

Wave 09 closes the canary failure/recovery loop with deterministic evaluation evidence and a content-bound rollback receipt while keeping evaluation and evidence separate from execution authority.

### 021 — Neuruh Canary Evaluation Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-canary-evaluation-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 56/56 tests PASS; exact public Wave 09 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

An append-only tamper-evident ledger binding the exact proposal, Promotion Gate decision, candidate/baseline digests, canary exposure, sample count, metrics, incidents and a deterministic PASS / HOLD / ROLLBACK verdict.

Critical boundary: canary evaluation evidence hard-codes `deployment_authority=false`. A PASS verdict does not deploy or promote anything, and a ROLLBACK verdict does not authorize rollback execution.

**Private exclusions:** production traffic routing, real canary metrics, private thresholds, customer data, release policy, deployment topology and production incident systems.

### 022 — Neuruh Rollback Receipt

**Repository:** https://github.com/NeuruhAI/neuruh-rollback-receipt
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 43/43 tests PASS; exact public Wave 09 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound receipt binding proposal, promotion, canary evidence, the predeclared reversibility contract, separate human rollback approval, pre-state, exact restoration target, rollback execution evidence, post-state and verification evidence.

Critical boundary: the receipt records externally governed rollback evidence and hard-codes `execution_authority=false`. A SUCCEEDED direct rollback requires the post-state digest to equal the exact declared restoration target.

**Private exclusions:** production rollback commands, infrastructure state, credentials, production authority routing, customer state, private connectors and commercial recovery logic.

### Wave 09 aggregate qualification

- **99/99 unit tests PASS**
- **021: 56/56 PASS**
- **022: 43/43 PASS**
- **Exact public 019 → 018 → 014 → 020 → 021 → 018 → 014 → 022 → 015 → 009 composition E2E PASS**
- **Promotion lifecycle eligibility retains deployment_authority=false PASS**
- **Canary critical failure deterministically returns ROLLBACK PASS**
- **Canary evaluation retains deployment_authority=false PASS**
- **Exact Reversibility Contract eligibility PASS**
- **Separate rollback human approval PASS**
- **Rollback exact restoration target verification PASS**
- **Rollback Receipt retains execution_authority=false PASS**
- **Decision Receipt + Agent Run Manifest binding PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 09 makes failure recovery auditable without letting evaluation or receipt evidence become deployment or rollback authority.


---

## Release Wave 10 — Deployment Authorization + Stage Transition

Wave 10 separates lifecycle eligibility from actual deployment authority, then records the externally executed stage transition as evidence.

### 023 — Neuruh Deployment Authorization Contract

**Repository:** https://github.com/NeuruhAI/neuruh-deployment-authorization-contract
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 57/57 tests PASS; exact public Wave 10 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic, single-use, time-bound authorization artifact binding one exact run/action/target/actor, authority class, capability, adjacent lifecycle transition, current/candidate state, learning proposal, Promotion Gate result, stage-evaluation evidence, human approval, authority delegation, reversibility contract and policy version.

Critical boundary: this is the dedicated authority-bearing artifact and explicitly carries `deployment_authority=true`, but contains no deployment mechanism. A separate governed executor must authenticate the actor, verify every bound prerequisite and enforce this exact contract.

**Private exclusions:** production actor identities, deployment capability map, credentials, infrastructure topology, production state, private policies, routing and executor implementation.

### 024 — Neuruh Stage Transition Receipt

**Repository:** https://github.com/NeuruhAI/neuruh-stage-transition-receipt
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 49/49 tests PASS; exact public Wave 10 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic receipt binding the exact Deployment Authorization to proposal, promotion, stage-evaluation evidence, pre-state, target state, external execution evidence, observed post-state and verification evidence for one adjacent forward lifecycle transition.

Critical boundary: the receipt hard-codes `execution_authority=false`. A SUCCEEDED transition requires the observed post-state digest to equal the exact authorized target state. Rollback remains Release 022 rather than being overloaded into this receipt.

**Private exclusions:** production deployment commands, rollout topology, credentials, real state stores, customer data, release policy and operational routing.

### Wave 10 aggregate qualification

- **106/106 unit tests PASS**
- **023: 57/57 PASS**
- **024: 49/49 PASS**
- **Exact public 019 → 018 → 016 → 014 → 020 → 021 → 023 → 024 → 015 → 009 composition E2E PASS**
- **Stage evaluation PASS prerequisite bound**
- **Promotion Gate PROMOTE retains deployment_authority=false PASS**
- **Authority delegation + exact human approval binding PASS**
- **023 single-use/time-bound deployment_authority=true PASS**
- **023 exact action/actor/state/stage binding PASS**
- **024 exact target-state verification PASS**
- **024 execution_authority=false PASS**
- **Decision Receipt + Agent Run Manifest binding PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 10 establishes the narrow boundary where lifecycle eligibility becomes exact, consumable deployment authority and where the resulting lifecycle transition becomes auditable evidence.


---

## Release Wave 11 — Authority Consumption + Canonical Lifecycle State

Wave 11 closes two post-authorization custody gaps: it retires single-use deployment authority exactly once, and it makes each target's lifecycle stage/state a canonical append-only record rather than something inferred from scattered receipts.

### 025 — Neuruh Authorization Consumption Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-authorization-consumption-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 54/54 tests PASS; exact public Wave 11 composition E2E PASS; replay rejection PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

An append-only tamper-evident ledger that permanently retires one exact Release 023 authorization digest as either consumed or voided. A consumed entry is bound to a pre-execution execution-intent digest; a voided entry is retired without execution and requires an explicit reason.

Critical boundary: consumption evidence hard-codes `authority_retired=true` and `deployment_authority=false`. Duplicate authorization IDs and digests are rejected across the full history. This public primitive does not pretend to be a distributed lock: production atomic consumption storage and concurrency control remain private executor responsibilities.

**Private exclusions:** production atomic authority store, distributed locks, actor identities, credentials, executor implementation, production targets, private authority topology, customer state and deployment routing.

### 026 — Neuruh Lifecycle State Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-lifecycle-state-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 75/75 tests PASS; exact public Wave 11 composition E2E PASS; canonical state/replay tests PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A canonical append-only hash-chained ledger for a target's exact lifecycle stage and state digest. Forward transitions advance exactly one adjacent stage and bind both the Release 024 Stage Transition Receipt and the immutable specific Release 025 consumption-entry digest. Rollback entries bind Release 022 rollback evidence and move only to an earlier lifecycle stage.

Critical boundary: lifecycle state evidence hard-codes `execution_authority=false`. The ledger rejects stale previous stages/states, transition-receipt reuse, consumption-entry reuse, rollback-receipt reuse, chain breaks, timestamp regression and target mutation.

**Private exclusions:** production state store, deployment/rollback commands, credentials, infrastructure topology, customer data, actor identity, private policies, observation agents and routing.

### Wave 11 aggregate qualification

- **129/129 unit tests PASS**
- **025: 54/54 PASS**
- **026: 75/75 PASS**
- **Exact public 023 → 025 → 024 → 026 → 015 → 009 composition E2E PASS**
- **023 exact deployment_authority=true and single-use binding PASS**
- **025 exact authorization retirement PASS**
- **025 duplicate/replay authorization rejection PASS**
- **025 deployment_authority=false PASS**
- **024 exact externally executed adjacent stage transition PASS**
- **026 canonical current stage/state PASS**
- **026 stale from-stage/pre-state rejection PASS**
- **026 transition receipt / consumption entry / rollback receipt reuse rejection PASS**
- **026 execution_authority=false PASS**
- **Decision Receipt + Agent Run Manifest binding PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 11 turns single-use authorization into auditable retirement and turns lifecycle position into explicit canonical state without exporting the production coordination machinery.


---

## Release Wave 12 — Execution Intent + State Attestation

Wave 12 makes two previously opaque evidence links explicit: it turns the authorization-consumption `execution_intent_digest` into a concrete pre-execution manifest, and it turns post-transition state verification into a content-bound expected-vs-observed attestation before canonical lifecycle state advances.

### 027 — Neuruh Execution Intent Manifest

**Repository:** https://github.com/NeuruhAI/neuruh-execution-intent-manifest
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 72/72 tests PASS; exact public Wave 12 composition E2E PASS; authorization-window containment PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound pre-execution manifest binding the exact Release 023 authorization to one run/action/target/actor/capability, one adjacent lifecycle transition, exact pre/target state, prerequisite governance evidence, hashed input/context, deterministic idempotency key, authorization use index zero, one execution attempt and an execution window fully contained by the parent authorization window.

Critical boundary: the intent hard-codes `deployment_authority=false` and `execution_authority=false`. Release 023 remains the authority-bearing artifact. Release 027 describes exactly what that authority will be consumed for; it does not authorize or execute anything.

**Private exclusions:** executable commands, production connector graph, credentials, deployment endpoints, actor identity proof, private context/input payloads, production state and executor implementation.

### 028 — Neuruh State Attestation Envelope

**Repository:** https://github.com/NeuruhAI/neuruh-state-attestation-envelope
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 55/55 tests PASS; exact public Wave 12 composition E2E PASS; expected-vs-observed mismatch rejection PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound state evidence envelope binding target/stage, expected and observed state digests, observation evidence, observer/timestamp, Release 023 authorization, Release 027 execution intent and Release 024 transition receipt. It deterministically records `match`, `mismatch` or `uncompared`.

Critical boundary: the envelope hard-codes `deployment_authority=false`, `execution_authority=false` and `canonical_state_authority=false`. The composed gate must verify an exact post-transition MATCH before supplying the attestation digest to Release 026 as canonical-state source evidence. Release 026 and 028 remain independently reusable packages and do not silently import each other.

**Private exclusions:** production state probes, observer authentication, credentials, infrastructure topology, private state payloads, customer data, deployment/rollback implementation and production state stores.

### Wave 12 aggregate qualification

- **127/127 unit tests PASS**
- **027: 72/72 PASS**
- **028: 55/55 PASS**
- **Exact public 023 → 027 → 025 → 024 → 028 → 026 → 015 → 009 composition E2E PASS**
- **023 remains exact single-use deployment_authority=true PASS**
- **027 exact authorization tuple binding PASS**
- **027 execution window contained inside 023 authorization window PASS**
- **027 deployment_authority=false and execution_authority=false PASS**
- **025 consumes the exact immutable 027 intent digest PASS**
- **025 authorization replay rejection PASS**
- **024 exact externally governed transition receipt PASS**
- **028 exact expected-vs-observed MATCH verification PASS**
- **028 mismatched state blocked before canonical 026 append PASS**
- **028 canonical_state_authority=false PASS**
- **026 canonical current stage/state PASS**
- **Decision Receipt + Agent Run Manifest binding PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 12 turns execution intent and state observation into first-class, independently verifiable public evidence without transferring deployment, execution or canonical-state authority into those evidence objects.


---

## Release Wave 13 — State Drift + Reconciliation Proposals

Wave 13 closes the observed-state drift loop without granting remediation authority: it records deterministic divergence between canonical and attested state, then produces a bounded reconciliation proposal that must pass separate approval and authorization before any mutation.

### 029 — Neuruh State Drift Ledger

**Repository:** https://github.com/NeuruhAI/neuruh-state-drift-ledger
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 60/60 tests PASS; exact public Wave 13 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

An append-only tamper-evident ledger comparing an exact Release 026 canonical lifecycle entry with an exact Release 028 state attestation and deterministically deriving stage drift, state drift and `in_sync | drifted` status.

Critical boundary: drift evidence hard-codes `deployment_authority=false`, `execution_authority=false` and `canonical_state_authority=false`. It records divergence but cannot reconcile or mutate canonical state.

### 030 — Neuruh Reconciliation Proposal

**Repository:** https://github.com/NeuruhAI/neuruh-reconciliation-proposal
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 62/62 tests PASS; exact public Wave 13 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic content-bound proposal for one exact Release 029 drift entry with `restore_canonical`, `adopt_observed`, or `hold_manual_review`. Mutation proposals bind authority class, capability and reversibility evidence; every mode requires explicit approval.

Critical boundary: proposals hard-code `approval_required=true`, `deployment_authority=false`, `execution_authority=false` and `canonical_state_authority=false`. Release 030 cannot approve, authorize, execute or mutate Release 026.

### Wave 13 aggregate qualification

- **122/122 unit tests PASS**
- **029: 60/60 PASS**
- **030: 62/62 PASS**
- **Exact public 026 → 028 → 029 → 030 → 015 → 009 composition E2E PASS**
- **028 periodic attestation mismatch becomes explicit 029 drift evidence PASS**
- **029 deterministic stage/state drift classification PASS**
- **029 attestation replay / broken-chain / contradiction rejection PASS**
- **030 restore-canonical / adopt-observed / hold-manual-review semantics PASS**
- **030 actual drift required PASS**
- **030 explicit approval required PASS**
- **030 mutating modes require reversibility evidence PASS**
- **030 stale canonical/drift binding rejection PASS**
- **015 records escalation with blocked execution and pending outcome PASS**
- **009 seals evidence/proposal custody PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 13 makes state drift measurable and response proposals auditable while preserving the boundary that observation and recommendation do not become authority.


---

## Release Wave 14 — Reconciliation Authority + Receipt

Wave 14 closes the restore-canonical remediation path: an exact drift-bound proposal receives one narrow single-use reconciliation authority, that authority is retired through the existing Authorization Consumption Ledger, and the externally governed remediation is recorded as evidence before independent attestation confirms the system is back in sync.

### 031 — Neuruh Reconciliation Authorization Contract

**Repository:** https://github.com/NeuruhAI/neuruh-reconciliation-authorization-contract
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 27/27 tests PASS; exact public Wave 14 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic single-use, time-bound authority contract binding exact run/action/target/actor identity, Release 030 proposal, Release 029 drift entry, state attestation, authority/capability, canonical/observed state, exact restore target, approval, delegation, reversibility contract and policy version.

Critical boundary: 031 carries `reconciliation_authority=true` but hard-codes `deployment_authority=false`, `execution_authority=false` and `canonical_state_authority=false`. v0.1 authorizes `restore_canonical` only. `adopt_observed` is deliberately excluded because changing canonical truth is a separate authority domain.

### 032 — Neuruh Reconciliation Receipt

**Repository:** https://github.com/NeuruhAI/neuruh-reconciliation-receipt
**Version:** `v0.1.0-alpha` / Python `0.1.0a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 22/22 tests PASS; exact public Wave 14 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic receipt binding the exact Release 031 authority, Release 030 proposal, Release 029 drift entry, pre-state, authorized restore target, execution evidence, observed post-state, verification evidence, status, chronology and authorization use index.

Critical boundary: a successful receipt requires exact target-state equality and hard-codes `execution_authority=false`, `canonical_state_authority=false`, and `reconciliation_authority=false`.

### Wave 14 aggregate qualification

- **49/49 unit tests PASS**
- **031: 27/27 PASS**
- **032: 22/22 PASS**
- **Exact public 029 → 030 → 031 → 025 → 032 → 028 → 029 composition E2E PASS**
- **Pre-reconciliation 029 status = drifted PASS**
- **030 restore-canonical proposal binding PASS**
- **031 reconciliation_authority=true / single-use / time-bound PASS**
- **031 adopt_observed rejected as wrong authority domain PASS**
- **025 retires exact 031 authorization PASS**
- **025 duplicate consumption/replay rejection PASS**
- **032 successful post-state must equal exact restore target PASS**
- **028 post-reconciliation state attestation = MATCH PASS**
- **Post-reconciliation 029 status = in_sync PASS**
- **032 execution/canonical/reconciliation authority = false PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 14 proves that restoring runtime state to canonical truth can be governed, single-use, auditable and independently re-verified without letting remediation evidence become reusable authority.


---

## Release Wave 15 — Canonical State Revision Authority + Receipt

Wave 15 governs the separate authority domain required to change canonical truth itself. It permits one exact approved `adopt_observed` revision, retires that authority through Release 025, and records the externally applied canonical-store revision without pretending Release 026 was mutated.

### 033 — Neuruh Canonical State Revision Authorization Contract

**Repository:** https://github.com/NeuruhAI/neuruh-canonical-state-revision-authorization-contract
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 29/29 tests PASS; exact public Wave 15 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic, single-use, time-bound `adopt_observed` authority contract binding the exact Release 030 proposal, Release 029 drift evidence, source attestation, current Release 026 lifecycle-entry digest, current canonical state, observed state, exact target canonical state, actor/capability, approval, delegation, reversibility contract and policy version.

Critical boundary: 033 carries `canonical_state_revision_authority=true` while `deployment_authority=false`, `execution_authority=false`, `reconciliation_authority=false`, and `lifecycle_transition_authority=false`.

### 034 — Neuruh Canonical State Revision Receipt

**Repository:** https://github.com/NeuruhAI/neuruh-canonical-state-revision-receipt
**Version:** `v0.1.1-alpha` / Python `0.1.1a0`
**Class:** A — Public Commons
**Status:** Public / Active Alpha
**Qualification:** 29/29 tests PASS; exact public Wave 15 composition E2E PASS; wheel and CLI smoke PASS; final Git-history gitleaks PASS; Apache-2.0; release receipt present.

A deterministic evidence receipt binding the exact Release 033 authority, Release 030 proposal, Release 029 drift evidence, prior canonical lifecycle entry, pre-canonical state, exact revision target, canonical-store write evidence, post-canonical record, verification evidence and single-use index.

Critical boundary: 034 hard-codes `lifecycle_ledger_mutated=false` and carries no canonical-state, execution, deployment, reconciliation or reusable revision authority. It is not a Release 026 lifecycle entry.

### Wave 15 aggregate qualification

- **58/58 unit tests PASS**
- **033: 29/29 PASS**
- **034: 29/29 PASS**
- **Exact public 029 → 030 → 033 → 025 → 034 composition E2E PASS**
- **029 exact drift evidence PASS**
- **030 adopt_observed proposal PASS**
- **033 canonical_state_revision_authority=true / single-use / time-bound PASS**
- **033 cross-domain authority flags=false PASS**
- **025 exact 033 authority retirement PASS**
- **025 replay rejection PASS**
- **034 exact target canonical state verification PASS**
- **034 lifecycle_ledger_mutated=false PASS**
- **034 evidence authority flags=false PASS**
- **2/2 wheel builds PASS**
- **2/2 CLI smoke suites PASS**
- **2/2 final Git histories gitleaks PASS**
- **2/2 Apache-2.0**
- **2/2 release receipts present**
- **Synthetic fixtures only**
- **No private organism implementation exported**

Wave 15 separates changing canonical truth from restoring runtime state. The next public layer must establish revision lineage and resolve an effective canonical state across Release 026 lifecycle history plus canonical revision evidence.

### Wave 15 hardening v0.1.1-alpha

The canonical-state revision authority boundary was narrowed after post-release architecture review. Release 033 now rejects any `adopt_observed` request whose observed stage differs from the current canonical lifecycle stage, and Release 034 rejects any receipt whose target canonical stage differs from its pre-canonical stage. This makes canonical revision explicitly state-only and preserves lifecycle-stage changes for the separate lifecycle transition authority path.

- **033 cross-stage canonical revision rejection PASS**
- **034 cross-stage canonical revision receipt rejection PASS**
- **Same-stage Wave 15 composition remains PASS**
- **Release numbers remain 033–034; this is a hardening patch, not a new primitive wave**
