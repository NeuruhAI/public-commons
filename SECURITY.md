# Security Policy

## Public defaults

Public Neuruh components should default to:

- no network access unless the component explicitly requires it;
- no shell execution by default;
- no filesystem mutation by default;
- no implicit credentials;
- dry-run where applicable;
- explicit capabilities;
- fail-closed validation;
- synthetic fixtures.

## Reporting

Please use GitHub private vulnerability reporting when available for security issues. Do not post credentials, personal data, customer data, private infrastructure details, or active exploit material in public issues.

## Release gate

A clean current directory is insufficient. Before public release, review current source plus relevant Git history, generated artifacts, examples, logs, documentation, dependencies, licensing, and data provenance.

Every release must also satisfy the Public Commons boundary and data-release policy in this repository.
