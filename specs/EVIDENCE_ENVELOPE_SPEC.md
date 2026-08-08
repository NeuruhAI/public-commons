# Neuruh Evidence Envelope Specification v0.1

## Status

Active Alpha — Public Commons specification.

## Purpose

The Evidence Envelope is a portable return contract for systems that need to separate a claim from the evidence, uncertainty, gaps, producer identity, and reproducibility metadata behind that claim.

The core rule is:

> A result should carry enough provenance to explain what was asserted, what supported it, what was missing, and which versioned producer created it.

## Public contract

An envelope contains:

- `schema_version` — contract version;
- `claim_id` — stable identifier for the claim or result;
- `subject` — the thing the claim concerns;
- `status` — `supported`, `observed`, `abstained`, or `contradicted`;
- `value` — the result payload, or `null` when abstaining;
- `confidence` — optional 0–1 confidence when meaningful;
- `evidence_refs` — traceable source references;
- `gaps` — explicit missing-evidence or abstention reasons;
- `contradictions` — optional contradictory observations or unresolved conflicts;
- `producer` — versioned producer identity;
- `input_hash` — deterministic hash of the normalized input when available;
- `produced_at` — UTC-compatible timestamp.

See `../schemas/evidence-envelope.v0.1.schema.json`.

## Evidence reference

Each evidence reference contains:

- `source_type` — generic source category;
- `retrieved_at` — when the source was retrieved or observed;
- `content_hash` — SHA-256 hash of the retrieved content or canonical observation;
- optional `citation` — page, line, section, record, or descriptive locator;
- optional `uri` — public or otherwise safe locator when appropriate.

A content hash makes later comparison possible; it does not by itself prove that the source was true or trustworthy.

## Invariants

1. Supported or observed results carry at least one evidence reference.
2. Abstention is a valid result, not an error or invitation to guess.
3. An abstained envelope must include at least one explicit gap and must set `value` to `null`.
4. Confidence, when present, must be between 0 and 1.
5. The producer identifier and version are explicit.
6. Input identity is represented by a content hash when reproducibility matters.
7. Evidence metadata does not grant execution or authorization authority.
8. Contradictory evidence may be preserved rather than silently collapsed.
9. Real customer data, credentials, private endpoints, and proprietary derived weights do not belong in public fixtures.

## What this specification does not provide

- proof that a source is correct;
- digital signatures or identity attestation;
- authorization to execute an action;
- policy evaluation;
- storage or retention policy;
- private source access;
- domain-specific confidence calibration.

## Synthetic example

See `../examples/evidence-envelope.synthetic.json`.

## Origin of the public pattern

This specification is a neutral extraction from repeated internal evidence-envelope and deterministic-result patterns. Domain-specific source taxonomies, private datasets, vertical gaps, production paths, and private decision logic are intentionally excluded.
