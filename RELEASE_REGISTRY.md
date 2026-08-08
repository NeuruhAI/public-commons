# Public Commons Release Registry

This registry tracks approved public Neuruh primitives. Each project remains independently versioned, tested, and maintained.

| Release | Repository / Artifact | Version | Class | Status | Purpose |
|---|---|---:|---|---|---|
| 001 | `NeuruhAI/neuruh-agent-receipt` | 0.1.0 | A — Public Commons | Release-ready | Portable tamper-evident agent receipt specification and verifier |
| 002 | `specs/SINGLE_WRITER_SPEC.md` | 0.1 | A — Public Commons | Release-ready | Single authoritative writer contract for canonical mutable domains |
| 003 | `specs/EVIDENCE_ENVELOPE_SPEC.md` | 0.1 | A — Public Commons | Release-ready | Portable evidence, provenance, contradiction, uncertainty, and abstention envelope |
| 004 | `failure-lab/` | 0.1 | A — Public Commons | Release-ready | Synthetic negative-test pack proving invalid contract states are rejected |

## Queue

1. Neuruh Capability Registry
2. Neuruh Sovereign Agent Starter

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

