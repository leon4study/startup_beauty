"""Shared pytest fixtures (auto-discovered by pytest)."""

import pytest


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Provide an isolated data directory for tests that need filesystem state."""
    d = tmp_path / "data"
    d.mkdir()
    return d
