# Security Policy

## Public defaults

Public Neuruh components should default to:

- no network access;
- no shell execution;
- no filesystem mutation;
- no implicit credentials;
- dry-run where applicable;
- explicit capabilities;
- fail-closed validation;
- synthetic fixtures.

## Reporting

Do not post credentials, personal data, customer data, or active exploit
details in public issues.

A private vulnerability contact must be selected before this repository becomes
public.

## Release gate

A clean current directory is insufficient. Git history, generated artifacts,
examples, logs, and documentation must also be scanned.
