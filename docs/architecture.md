# Architecture

## Overview
High-level diagram of startup_beauty (replace with your actual design).

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Input   │ ──▶ │ Pipeline │ ──▶ │  Output  │
└──────────┘     └──────────┘     └──────────┘
```

## Modules
- `src/startup_beauty/__init__.py` — package metadata only (no side effects)
- `src/startup_beauty/__main__.py` — enables `python -m startup_beauty`
- `src/startup_beauty/cli.py` — typer entry points + logging bootstrap
- `src/startup_beauty/config.py` — pydantic-settings configuration

## Data flow
- `data/raw/` — read-only original inputs
- `data/processed/` — derived from raw via scripts in `src/`
- `data/external/` — third-party sources

## Decisions
See `docs/adr/` for Architecture Decision Records.
