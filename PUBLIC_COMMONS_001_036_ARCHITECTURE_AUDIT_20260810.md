# PUBLIC COMMONS 001–036 ARCHITECTURE AUDIT — 2026-08-10

Scope: all 36 registered/qualified Public Commons releases — 001–034 public on `NeuruhAI/public-commons` main `ba6a7b5f15d8e05f95d7d842e5476851eedb44cc` (PR #20 merged), plus 035/036 locally qualified in Wave 16 package `Neuruh_Public_Commons_Wave_16_v0.1.0-alpha` (sealed tarball SHA256 `a3ed07c4a629863b5bfe830c5d4459a561d8bde2d5f75705da2566f9f419a99c`).

Evidence basis: source-level reads of 025/026/029/030/033/034/035/036 cores; wave 11–16 composition scripts and results; registry text for the remainder; fresh gitleaks full-history scans (public-commons: 51 commits clean; 035: 2 commits clean; 036: 2 commits clean). Claims sourced only from the registry (not re-verified at source today) are marked *registry-claimed*.

---

## A. Authority graph

Authority-carrying artifacts (each single-domain, each with cross-domain flags hard-false):

| Domain | Grantor | Verified boundary |
|---|---|---|
| delegation | 016 Authority Delegation Contract | registry-claimed |
| promotion eligibility | 020 Promotion Gate (+ 014 human approval) | registry-claimed |
| deployment | 023 Deployment Authorization Contract | registry-claimed |
| reconciliation (restore reality) | 031 Reconciliation Authorization Contract | registry-claimed |
| canonical revision (change truth) | 033 Canonical State Revision Authorization Contract | **verified at source**: `canonical_state_revision_authority=true`, deployment/execution/reconciliation/lifecycle_transition all hard-false, `max_uses=1` |

Everything else is evidence, proposal, or projection and hard-codes its authority flags false. Verified at source for 026, 029, 030, 034, 035, 036; the 035/036 additions extend denial to `lifecycle_transition_authority` and generic `mutation_authority`. No artifact in the 019→036 chain grants an authority outside its declared domain. **No cross-domain authority leak found.**

The one retirement path is 025: authority becomes unusable by consumption, not by expiry alone. Waves 11–16 compositions prove 025 retires 023-, 031-, and 033-class authorities with replay blocked.

## B. Single-use / replay graph

- 033 authority: `max_uses=1` (source) → consumed exactly once via 025 (`authority_retired=true`, replay `ConsumptionValidationError` — proven again in the Wave 16 composition).
- 034 receipt: `authorization_use_index=0` enforced (source).
- 026: stage-transition receipts, rollback receipts, and consumption digests each usable at most once per ledger (source).
- 035: receipt digest AND authorization digest each at most once per lineage; replayed append rejected (tested).
- Cross-lineage replay residual, closed compositionally: the same 034 receipt consumed into two *different* lineages at the same anchor produces either identical chains (deduped/prefix-merged by 036) or diverging chains → `FORKED_REVISION_LINEAGE` → fail-closed ambiguous. The global single-use anchor remains 025 on the authorization: one 033 authority ⇒ one legitimate 034 receipt ⇒ at most one legitimate lineage position. **No replayable object found that survives its intended single use.**

## C. State graph

- Stage vocabulary is one fixed 4-tuple (`sandbox, canary, pilot, production`) across 026/029/030/033/034/035/036 — no drift.
- Three state threads now exist and are formally related: 026 (lifecycle stage+state, hash-chained), 035 (state-revision memory anchored to one 026 tip, hash-chained), 036 (unique read-only projection over both). Wave 16 closes the "two competing facts" problem identified at the end of Wave 15.
- **Finding C-1 (real, bounded):** 026's internal thread requires each transition's `pre_state_digest` to equal its *own* previous `post_state_digest`. After a canonical revision (X→Y at tip A), a later legitimate transition still cites pre-state X, not effective state Y. 036 makes read-side truth deterministic (the transition supersedes the revision), but the lifecycle ledger's writer-side thread does not acknowledge revisions. This is a documented seam, not a defect — 026 entries are observation evidence with `source_evidence_digest` — but it is the strongest candidate justification for future work (see K).

## D. Recovery-vs-truth-revision graph

Two repair paths, two authority domains, verified disjoint:

- **Path A — reality is wrong:** 029 drift → 030 `restore_canonical` → 031 authority → 025 → private executor → 032 receipt → 028 attestation → 029 IN_SYNC. Canonical truth never moves.
- **Path B — truth is stale:** 029 drift → 030 `adopt_observed` → 033 authority → 025 → external canonical-store write → 034 receipt → 035 lineage → 036 projection. Reality never moves; lifecycle stage never moves.

033 carries `reconciliation_authority=false`; 031-class authority cannot advance a 035 lineage (035 demands a 034-shaped successful receipt bound to the lineage anchor). Wave 15 hardening plus 035's schema make the stage boundary unrepresentable in Path B; the Wave 16 negative composition proves `pilot/state-A → production/state-B` via revision is blocked at four independent layers (033, 034, 035, 036), including a hash-consistent re-sealed forgery (fails closed `LIFECYCLE_ANCHOR_CONTENT_MISMATCH`).

## E. Lifecycle / canonical interaction

Precedence and supersession are now deterministic (036, tested): a revision lineage is valid only against the exact 026 tip it was anchored to; a newer legitimate tip supersedes stale-anchored lineages (`superseded_stale_anchor` — evidence retained, power none); truth = tip unless exactly one valid current-anchored lineage exists.

**Finding E-1 (convention, not contract):** the anchor bridge — `lifecycle_anchor_digest = "sha256:" + <026 entry_hash>` — is established by composition tests and Wave 16 docs, not by any schema. 026 exposes no `digest_ref` property (029 and 035 do). 029/033/034 accept any well-formed `sha256:` digest as a lifecycle-entry reference. Recommend a one-line derivation note in the 026 README at its next patch; no new release is justified by this.

## F. Composition gaps

Proven end-to-end this cycle: 026→029→030→033→025→034→035→036 (three scenarios, from the sealed extract). Proven in prior waves per registry: 019→028 promotion/deployment/intent/attestation chain; 029→032 restore loop; 025/026 lifecycle integration.

Remaining unproven compositions (none blocking):
1. 036's resolution as *input* to anything — by design it is currently the terminal projection; the moment any contract consumes `resolution_digest`, that binding needs a composition test (see K-1).
2. 013 explainability / 017 calibration remain leaf artifacts outside the 019→036 spine — acceptable; they evidence decisions, not state.
3. The 022 rollback receipt → 026 rollback-entry path was proven in Wave 11 (*registry-claimed*), not re-executed today.

## G. Schema / version consistency

- Naming uniform: `neuruh.<artifact>.v0.1` across all inspected cores; no collisions. 036 pins the exact 035 `schema_version` string for its lineage inputs — the first schema-identity cross-pin in the stack; correct pattern.
- Versions: 005–008 and 033/034 at `v0.1.1-alpha`, all others `v0.1.0-alpha`, 035/036 enter at `v0.1.0-alpha`. Consistent with hardening history.
- Digest formats: bare 64-hex for intra-ledger `entry_hash`/chain, `sha256:`-prefixed for cross-artifact references — uniform; bridged by `digest_ref` in 029/035 (026 gap noted in E-1).
- **Finding G-1 (cosmetic drift):** authority-denial vocabularies grow monotonically (026: 1 flag; 029: 3; 033: 5; 034: 6; 035/036: 8). Not exploitable — every artifact rejects unknown fields, so absent flags cannot be smuggled in — but a canonical denial set should be settled before any v0.2 wave to stop the per-release bespoke lists.

## H. Private-boundary leakage

- gitleaks, full git history, today: public-commons 51 commits clean; 035 and 036 repos clean.
- Source scans of 035/036 for production identifiers, hostnames, keys, personal identifiers: clean (the only matches are the boundary declarations naming what stays private).
- 001–034 receipts carry `git_history_gitleaks: PASS` and boundary scans (*registry-claimed*, spot-verified for 033/034).
- Registry/docs expose only generic stage names and synthetic digests. Routing intelligence, Mother/Father orchestration, AXON, private policies, connectors, memory, and customer data remain unreferenced anywhere in the public tree. **No leakage found.**

## I. Impossible / ambiguous state cases

Explicitly terminal (fail-closed, truth-free) in 036: missing lifecycle evidence; competing distinct tips; forked lineage at the current tip; anchor-content mismatch. All four tested; ambiguous resolutions cannot carry an effective stage/state/source (schema-enforced).

Known residual seams, all bounded and documented:
1. **C-1** (026 writer-side thread ignores revisions) — see C and K.
2. **Fork permanence:** two valid diverging lineages at the current tip yield `FORKED_REVISION_LINEAGE` forever; today the only legitimate exit is a new lifecycle transition (which supersedes both). There is no authority that retires one lineage branch. Correct fail-closed posture; noted in K-2.
3. **Garbage-in tip claims:** 036 verifies structure and content-binding of everything it is handed, but cannot know a *withheld* newer tip exists. The consumer contract (documented in 036's README/architecture) is that the caller supplies the current 026 tip; `evidence_digest` makes the resolution auditable against exactly what was supplied. Inherent to any pure projection; not fixable inside 036 without violating its no-live-systems boundary.

## J. Primitives that duplicate each other

Reviewed pairs: 032 vs 034 (sibling receipt shapes, disjoint authority domains — intentionally parallel, not mergeable without collapsing the Path A/Path B separation); 024 vs 026 (026 consumes 024 digests — producer/consumer); 028 vs 029 (attestation vs drift comparison — producer/consumer); 001 vs 011 vs 015 (agent receipt / evidence ledger / decision receipt — layered scopes, *registry-claimed*; watch for overlap if any reaches v0.2); 021 vs 017 (canary vs calibration — different questions). **No merge is justified at v0.1.** The parallel authorization-contract family (023/031/033) shares shape by design; a future generic "authority contract" abstraction would trade explicitness for reuse and is not recommended while the stack is alpha.

## K. Gaps that actually justify future work (numbers deliberately not assigned)

1. **Revision-aware lifecycle transition binding** — closes C-1/F-1: a lifecycle transition (and rollback) contract whose pre-state evidence must cite the current 036 `resolution_digest` (or explicitly attest "no applied revisions"), making the writer-side lifecycle thread acknowledge effective truth. This is the first real consumer of 036's output and the concrete, evidence-backed gap this audit found.
2. **Lineage-fork retirement authority** — closes I-2: a narrow, single-use, human-approved authority to retire exactly one identified lineage branch, so a fork can be resolved without forcing a lifecycle transition. Only justified if forks are expected in practice; defer until operational evidence exists.

Nothing else in 001–036 currently justifies a new primitive. The queue after 036 should remain empty until the founder weighs K-1/K-2.

---

## Verdict

The 001–036 stack is coherent: one authority per domain, one retirement path, evidence never carries power, canonical truth and lifecycle stage are separately governed, and effective truth is now a unique deterministic projection that fails closed. The two real seams found (C-1 writer-side thread, I-2 fork permanence) are bounded, documented, and constitute the only justified future work.
