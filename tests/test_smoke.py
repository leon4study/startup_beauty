"""Smoke test — confirms package imports and config loads."""

from startup_beauty import __version__
from startup_beauty.config import settings


def test_version() -> None:
    assert __version__


def test_settings_loads() -> None:
    assert settings.project_name
    assert settings.log_level
