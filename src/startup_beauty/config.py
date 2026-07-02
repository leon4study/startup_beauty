"""Application configuration loaded from environment / .env."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Centralized config. Override via environment variables or `.env` file.

    Field names map case-insensitively to env vars:
      project_name → PROJECT_NAME, log_level → LOG_LEVEL, etc.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    project_name: str = "startup_beauty"
    log_level: str = "INFO"
    log_dir: Path | None = None  # set to enable file logging
    data_path: Path = Path("./data")


# Singleton — import this everywhere instead of constructing Settings yourself.
settings = Settings()
