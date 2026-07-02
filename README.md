# startup_beauty

> One-line description goes here.

[![CI](https://github.com/<USER>/startup_beauty/actions/workflows/ci.yml/badge.svg)](https://github.com/<USER>/startup_beauty/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000)
![Linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)

## Setup

```bash
# 1) Install uv if not already (https://docs.astral.sh/uv/)
curl -LsSf https://astral.sh/uv/install.sh | sh         # macOS / Linux
# powershell -c "irm https://astral.sh/uv/install.ps1 | iex"   # Windows

# 2) Sync (creates .venv automatically + installs dev deps + writes uv.lock)
uv sync

# 3) Install pre-commit hook
uv run pre-commit install
```

## Usage

```bash
uv run startup_beauty --help        # CLI
uv run pytest               # tests
uv run jupyter lab          # notebooks (notebook group is in dev deps)
```

## Development

```bash
make help       # list all available targets
make test       # run tests
make lint       # ruff + mypy
make format     # black + ruff --fix
```

## License

MIT
