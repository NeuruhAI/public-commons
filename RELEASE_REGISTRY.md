# Public Commons Release Registry

This registry tracks approved public Neuruh primitives. Each project remains independently versioned, tested, and maintained.

| Release | Repository / Artifact | Version | Class | Status | Purpose |
|---|---|---:|---|---|---|
| 001 | `NeuruhAI/agent-receipt` | 0.1.0 | A — Public Commons | Public / Active Alpha | Portable tamper-evident agent receipt specification and verifier |
| 002 | `specs/SINGLE_WRITER_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Single authoritative writer contract for canonical mutable domains |
| 003 | `specs/EVIDENCE_ENVELOPE_SPEC.md` | 0.1 | A — Public Commons | Public / Active Alpha | Portable evidence, provenance, contradiction, uncertainty, and abstention envelope |
| 004 | `failure-lab/` | 0.1 | A — Public Commons | Public / Active Alpha | Synthetic negative-test pack proving invalid contract states are rejected |

## Queue

1. Neuruh Evidence Ledger
2. Neuruh Connector Contract Kit

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

