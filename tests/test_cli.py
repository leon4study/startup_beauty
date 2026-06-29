"""CLI tests using typer.testing.CliRunner."""

from typer.testing import CliRunner

from startup_beauty.cli import app

runner = CliRunner()


def test_hello_command() -> None:
    result = runner.invoke(app, ["hello", "--name", "test"])
    assert result.exit_code == 0


def test_info_command() -> None:
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
