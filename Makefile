.PHONY: help setup install test lint format clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

setup:  ## Sync deps + install pre-commit hook
	uv sync
	uv run pre-commit install

install:  ## Sync dependencies (idempotent)
	uv sync

test:  ## Run tests with coverage
	uv run pytest

lint:  ## Run ruff + mypy
	uv run ruff check src tests
	uv run mypy src

format:  ## Format with black + ruff --fix
	uv run black src tests
	uv run ruff check --fix src tests

clean:  ## Remove caches and build artifacts
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
