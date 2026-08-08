# Neuruh Agent Failure Lab v0.1

## Status

Active Alpha — Public Commons synthetic negative-test pack.

## Purpose

Reliable agent infrastructure needs fixtures that prove invalid states are rejected, not only examples that demonstrate the happy path.

This pack contains deliberately invalid, fully synthetic documents for the Public Commons contracts. Each fixture is syntactically valid JSON but violates a specific contract invariant.

## Included failures

| Fixture | Contract | Expected rejection |
|---|---|---|
| `single-writer.missing-writer.json` | Single Writer v0.1 | mutable domain has no declared writer |
| `evidence.supported-no-evidence.json` | Evidence Envelope v0.1 | supported claim has zero evidence references |
| `evidence.abstained-with-value.json` | Evidence Envelope v0.1 | abstained claim carries a non-null value |
| `evidence.confidence-out-of-range.json` | Evidence Envelope v0.1 | confidence exceeds 1.0 |

See `manifest.json` for machine-readable expected outcomes.

## Boundary

All subjects, component names, identifiers, hashes, and values are synthetic. This pack contains no production routes, credentials, customer information, private source taxonomy, proprietary weights, or real authority assignments.

## Use

Consumers can load the matching JSON Schema from `../schemas/` and assert that each listed fixture fails validation for the declared reason.

Passing an invalid fixture is a regression.
