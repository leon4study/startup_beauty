"""Command-line interface for startup_beauty."""

import sys

import typer
from loguru import logger

from startup_beauty.config import settings


def setup_logging() -> None:
    """Configure loguru sinks based on settings. Called from app callback."""
    logger.remove()                     # drop the default sink
    logger.add(
        sys.stderr,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level:<8}</level> | "
            "<cyan>{name}</cyan> - <level>{message}</level>"
        ),
        level=settings.log_level,
    )
    if settings.log_dir is not None:
        settings.log_dir.mkdir(parents=True, exist_ok=True)
        logger.add(
            settings.log_dir / "startup_beauty_{time:YYYY-MM-DD}.log",
            rotation="00:00",
            retention="30 days",
            encoding="utf-8",
            level="DEBUG",
        )


app = typer.Typer(help="startup_beauty CLI")


@app.callback()
def _bootstrap() -> None:
    """Runs before every subcommand — initialize logging here."""
    setup_logging()


@app.command()
def info() -> None:
    """Print runtime configuration."""
    logger.info(f"Project: {settings.project_name}")
    logger.info(f"Data path: {settings.data_path}")
    logger.info(f"Model path: {settings.model_path}")


@app.command()
def hello(name: str = "world") -> None:
    """Sanity-check entry point."""
    logger.info(f"Hello, {name}!")


if __name__ == "__main__":
    app()
