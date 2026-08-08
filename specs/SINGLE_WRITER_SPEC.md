# Neuruh Single-Writer Specification v0.1

## Status

Active Alpha — Public Commons specification.

## Purpose

Single-writer discipline prevents silent corruption when multiple components can plausibly mutate the same canonical state or apply the same logical effect.

The rule is simple:

> For every canonical mutable domain, exactly one declared authority owns the write path.

Other components may read, observe, recommend, calculate, or request a change. They do not become writers merely because they can derive or display the same information.

## Why this exists

Distributed and agentic systems frequently fail through overlapping authority rather than obvious exceptions. Two services can both appear correct locally while double-applying an adjustment, overwriting a canonical field, or creating incompatible versions of the same truth.

Single-writer discipline makes ownership machine-declared and reviewable before those conflicts reach production.

## Public contract

A manifest contains:

- `schema_version` — the contract version;
- `domains` — a map of canonical mutable domains;
- `writer` — the one authority permitted to mutate that domain;
- `consumers` — optional readers or downstream consumers;
- `restriction` — optional human-readable boundary or escalation rule.

See `../schemas/single-writer.v0.1.schema.json`.

## Invariants

1. Every mutable domain has one declared writer.
2. Consumers do not acquire write authority by reading or deriving the domain.
3. Writer ownership is scoped only to the declared domain.
4. Human or external authorities may be declared as writers where software must not own the final decision.
5. An implementation should fail closed when a write target has no declared writer.
6. An implementation should reject duplicate domain declarations before or during parsing.
7. A component attempting to write a domain it does not own should fail validation or CI before deployment.
8. A change in writer ownership is a contract change and should be reviewed like an API or schema migration.

## What this specification does not provide

- production authority maps;
- Neuruh's internal component topology;
- authentication or identity proof;
- distributed locking;
- database transaction isolation;
- conflict-free replication;
- authorization to perform a real-world action.

## Synthetic example

See `../examples/single-writer.synthetic.json`.

The example intentionally uses generic component names and synthetic domains. It is not a map of Neuruh's private runtime.

## Implementation guidance

A practical CI linter should compare declared write capabilities against this manifest and fail when:

- a component writes an undeclared domain;
- a component writes a domain owned by another writer;
- a domain is missing an owner;
- a manifest contains duplicate or malformed domain keys;
- a writer transition occurs without an explicit reviewed change.

## Origin of the public pattern

This specification is a neutral extraction from repeated internal use of single-writer discipline across data, adjustment, execution, and human-authority boundaries. Private domain maps, repository names, production rules, and vertical-specific ownership assignments are intentionally excluded.
